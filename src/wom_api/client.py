"""Connection management and request correlation for the browser data protocol."""

from __future__ import annotations

import asyncio
import json
import math
import re
import ssl
import time
from collections.abc import Mapping
from dataclasses import dataclass, field, replace
from types import TracebackType
from typing import Any, cast
from urllib.parse import urlsplit

import aiohttp
import socketio

from ._generated import ApiMethods
from .catalog import APIS, PROTOCOL_VERSION
from .events import EventStream
from .exceptions import (
    AuthorizationError,
    ClientClosed,
    ConnectionError,
    ProtocolError,
    RequestTimeout,
    ServerError,
    ServerRequired,
    WomError,
)
from .types import Authorization, Event, JsonValue, Payload


@dataclass
class _Connection:
    server: str
    socket: Any
    ready: asyncio.Event = field(default_factory=asyncio.Event)
    lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    send_lock: asyncio.Lock = field(default_factory=asyncio.Lock)
    pending: dict[int, asyncio.Future[JsonValue]] = field(default_factory=dict)
    last_sent: float = 0
    failure: WomError | None = None
    started: bool = False


class WomClient(ApiMethods):
    """Async client with lazy authorization and one connection per server.

    Parameters:
        session: Existing browser ``localStorage['_session']``; empty creates a guest.
        base_url: HTTP authorization origin.
        servers: Optional role-to-shard overrides, or HTTP URLs for local testing.
        timeout: Total request deadline in seconds.
        min_request_interval: Minimum seconds between requests to each shard.
        protocol_version: Reviewed browser version to include in each request.
        ssl_context: Optional verified TLS context, also used for WebSockets.
        transports: Socket.IO transports; WebSocket is the default.

    Use within one asyncio event loop and close with an async context manager.
    Reconnection restores transport only; requests are never replayed.
    """

    def __init__(
        self,
        session: str = "",
        *,
        base_url: str = "https://minesweeper.online",
        servers: Mapping[str, str] | None = None,
        timeout: float = 20,
        min_request_interval: float = 0.125,
        protocol_version: int = PROTOCOL_VERSION,
        ssl_context: ssl.SSLContext | None = None,
        transports: tuple[str, ...] = ("websocket",),
    ) -> None:
        self._validate_timeout(timeout)
        if not math.isfinite(min_request_interval) or min_request_interval < 0:
            raise ValueError("min_request_interval must be finite and nonnegative")
        self._validate_origin(base_url)
        if not transports or any(t not in ("websocket", "polling") for t in transports):
            raise ValueError("transports must contain websocket and/or polling")
        self._session = session
        self._base_url = base_url.rstrip("/")
        self._servers = dict(servers or {})
        self._timeout = timeout
        self._interval = min_request_interval
        self._version = protocol_version
        self._ssl_context = ssl_context
        self._transports = list(transports)
        self._authorization: Authorization | None = None
        self._auth_lock = asyncio.Lock()
        self._http: aiohttp.ClientSession | None = None
        self._connections: dict[str, _Connection] = {}
        self._streams: set[EventStream] = set()
        self._next_id = 1000
        self._closed = False
        self._revoked = False
        self._close_lock = asyncio.Lock()

    @staticmethod
    def _validate_timeout(timeout: float) -> None:
        if not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("timeout must be finite and positive")

    @staticmethod
    def _validate_origin(url: str) -> None:
        parsed = urlsplit(url)
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            raise ValueError("Use an http:// or https:// origin")
        if parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("Origins cannot include credentials, query strings, or fragments")
        if parsed.path not in ("", "/"):
            raise ValueError("Origins cannot include a path")

    def _check_open(self) -> None:
        if self._closed:
            raise ClientClosed("Client is closed")
        if self._revoked:
            raise AuthorizationError(
                "Session was revoked; create a new client with a valid session"
            )

    @property
    def authorization(self) -> Authorization | None:
        """Current authorization, or None before bootstrap."""
        return self._authorization

    @property
    def session(self) -> str:
        """Session for explicit persistence by the caller; treat it as a secret."""
        return self._session

    def _http_session(self) -> aiohttp.ClientSession:
        self._check_open()
        if self._http is None:
            connector = aiohttp.TCPConnector(ssl=self._ssl_context or True)
            self._http = aiohttp.ClientSession(connector=connector)
        return self._http

    async def authorize(self, *, refresh: bool = False) -> Authorization:
        """Bootstrap or refresh a guest/account ticket via GET /authorize."""
        try:
            return await self._authorize(refresh=refresh)
        except TimeoutError:
            raise RequestTimeout("HTTP authorization timed out") from None

    async def _authorize(self, *, refresh: bool) -> Authorization:
        async with asyncio.timeout(self._timeout):
            async with self._auth_lock:
                self._check_open()
                current = self._authorization
                if (
                    current
                    and not refresh
                    and current.ticket_expires_at > time.time() * 1000 + 10000
                ):
                    return current
                try:
                    async with self._http_session().get(
                        self._base_url + "/authorize",
                        params={"session": self._session},
                    ) as response:
                        response.raise_for_status()
                        data = await response.json()
                    if not isinstance(data, dict) or data.get("ban") or data.get("deleteRequest"):
                        raise ValueError("Authorization unavailable")
                    for key in ("session", "ticket"):
                        if not isinstance(data.get(key), str) or not data[key]:
                            raise ValueError("Missing secret")
                    for key in ("userId", "sessionId", "ticketExpiresAt"):
                        if type(data.get(key)) is not int:
                            raise ValueError("Missing identity")
                    if not isinstance(data.get("user"), dict):
                        raise ValueError("Missing user")
                    self._authorization = Authorization(
                        data["userId"],
                        data["sessionId"],
                        data["session"],
                        data["ticket"],
                        data["ticketExpiresAt"],
                        data["user"],
                    )
                    self._session = data["session"]
                    return self._authorization
                except (aiohttp.ClientError, ValueError, KeyError):
                    # HTTP exception URLs can contain session secrets.
                    raise AuthorizationError(
                        "HTTP authorization failed or returned invalid data"
                    ) from None

    def _server(self, role: str, server: str | None) -> str:
        if server is not None:
            return server
        if role in self._servers:
            return self._servers[role]
        if role == "game":
            raise ServerRequired("Pass server= from game metadata for game-role APIs")
        auth = self._authorization
        if auth is None:
            raise AuthorizationError("Authorize before resolving a shard")
        if role == "main":
            return f"main{1 + auth.user_id % 10}"
        if role == "hint":
            return f"hint{1 + auth.user_id % 4}"
        if role == "chat":
            return "chat1"
        if role == "watcher":
            return "watcher1"
        raise ValueError(f"Unknown role: {role}")

    def _server_url(self, server: str) -> str:
        if "://" in server:
            self._validate_origin(server)
            return server.rstrip("/")
        if not re.fullmatch(r"[a-z0-9-]+", server):
            raise ValueError("Invalid shard name")
        return f"https://{server}.minesweeper.online"

    def _fail_pending(self, connection: _Connection, error: WomError) -> None:
        for future in tuple(connection.pending.values()):
            if not future.done():
                future.set_exception(error)

    def _publish(self, event: Event) -> None:
        for stream in tuple(self._streams):
            stream._publish(event)

    def _make_connection(self, server: str) -> _Connection:
        sio = socketio.AsyncClient(
            http_session=self._http_session(),
            reconnection=True,
            reconnection_delay=1,
            reconnection_delay_max=5,
            logger=False,
            engineio_logger=False,
        )
        connection = _Connection(server, sio)

        async def authorized(data: Any) -> None:
            auth = self._authorization
            if self._closed:
                await sio.disconnect()
                return
            if not isinstance(data, dict) or not auth or data.get("sessionId") != auth.session_id:
                connection.failure = AuthorizationError("Invalid WebSocket authorization")
                connection.ready.set()
                return
            if isinstance(data, dict) and auth and data.get("sessionId") == auth.session_id:
                if isinstance(data.get("ticket"), str) and type(data.get("ticketExpiresAt")) is int:
                    if data["ticketExpiresAt"] >= auth.ticket_expires_at:
                        self._authorization = replace(
                            auth,
                            ticket=data["ticket"],
                            ticket_expires_at=data["ticketExpiresAt"],
                        )
            connection.failure = None
            connection.ready.set()

        async def disconnected(*args: Any) -> None:
            connection.ready.clear()
            self._fail_pending(connection, ConnectionError(f"Disconnected from {server}"))
            self._publish(Event("disconnect", [], server))

        async def response(data: Any) -> None:
            if (
                not isinstance(data, list)
                or len(data) != 3
                or (data[0] is not None and type(data[0]) is not int)
                or not isinstance(data[1], str)
                or not isinstance(data[2], list)
            ):
                self._fail_pending(connection, ProtocolError("Malformed response frame"))
                return
            request_id, name, params = data
            future = connection.pending.get(request_id or 0)
            if name == "ApiEvent":
                if future and not future.done():
                    if len(params) != 1:
                        future.set_exception(ProtocolError("ApiEvent must have exactly one result"))
                    else:
                        future.set_result(cast(JsonValue, params[0]))
            elif name == "SkipEvent":
                if future and not future.done():
                    future.set_exception(ProtocolError("Server skipped the request"))
            self._publish(Event(name, params, server, request_id or 0))

        async def server_error(data: Any) -> None:
            connection.failure = ServerError("Server reported server_error")
            connection.ready.set()
            self._fail_pending(connection, connection.failure)
            self._publish(Event("server_error", [data], server))

        async def revoked(data: Any) -> None:
            self._revoked = True
            error = AuthorizationError("Session was revoked")
            for other in tuple(self._connections.values()):
                other.failure = error
                other.ready.set()
                self._fail_pending(other, error)
            self._publish(Event("session_revoked", [data], server))
            for stream in tuple(self._streams):
                stream._finish(error)
            # Disconnecting the socket from its receive handler is supported by Socket.IO.
            await sio.disconnect()

        sio.on("authorized", handler=authorized)
        sio.on("disconnect", handler=disconnected)
        sio.on("response", handler=response)
        sio.on("server_error", handler=server_error)
        sio.on("session_revoked", handler=revoked)
        return connection

    async def _connect(self, server: str) -> _Connection:
        self._check_open()
        self._server_url(server)
        connection = self._connections.get(server)
        if connection is None:
            connection = self._make_connection(server)
            self._connections[server] = connection
        async with connection.lock:
            self._check_open()
            if not connection.socket.connected and not connection.started:
                connection.ready.clear()
                connection.failure = None

                async def auth_payload() -> dict[str, str]:
                    auth = await self.authorize()
                    return {"ticket": auth.ticket, "session": auth.session}

                try:
                    await connection.socket.connect(
                        self._server_url(server),
                        auth=auth_payload,
                        socketio_path="mine-websocket",
                        transports=self._transports,
                        wait_timeout=self._timeout,
                    )
                    connection.started = True
                except asyncio.CancelledError:
                    await connection.socket.disconnect()
                    raise
                except Exception:
                    await connection.socket.disconnect()
                    raise ConnectionError(f"Could not connect to {server}") from None
            await connection.ready.wait()
            self._check_open()
            if connection.failure:
                raise connection.failure
            return connection

    async def connect(self, *, role: str = "main", server: str | None = None) -> None:
        """Authorize and wait for the site's authorized event on a shard."""
        try:
            async with asyncio.timeout(self._timeout):
                await self.authorize()
                await self._connect(self._server(role, server))
        except TimeoutError:
            raise RequestTimeout("Connection authorization timed out") from None

    @staticmethod
    def _payload(payload: Mapping[str, JsonValue] | None, params: Payload) -> Payload | None:
        if payload is not None and not isinstance(payload, Mapping):
            raise TypeError("payload must be a mapping or None")
        if payload is None and not params:
            return None
        result = dict(payload or {})
        if result.keys() & params.keys():
            raise ValueError("A field was supplied in both payload and keyword arguments")
        result.update(params)
        if any(not isinstance(key, str) for key in result):
            raise TypeError("Payload field names must be strings")
        # Reject non-JSON objects and NaN locally, before opening a connection.
        json.dumps(result, allow_nan=False)
        return result

    async def _emit(
        self,
        connection: _Connection,
        controller: str,
        payload: Payload | None,
        request_id: int,
    ) -> None:
        async with connection.send_lock:
            delay = connection.last_sent + self._interval - asyncio.get_running_loop().time()
            if delay > 0:
                await asyncio.sleep(delay)
            self._check_open()
            if not connection.ready.is_set() or not connection.socket.connected:
                raise ConnectionError(f"Disconnected from {connection.server}")
            await connection.socket.emit(
                "request", [controller, payload, request_id, self._version]
            )
            connection.last_sent = asyncio.get_running_loop().time()

    async def request(
        self,
        controller: str,
        payload: Mapping[str, JsonValue] | None = None,
        *,
        server: str | None = None,
        timeout: float | None = None,
        **params: JsonValue,
    ) -> JsonValue:
        """Call a controller and await its correlated ApiEvent result.

        New controller names can be called with an explicit server. Domain pushes
        remain available through subscriptions. A timeout or disconnect does not
        imply that the server did not execute the action.
        """
        self._check_open()
        duration = self._timeout if timeout is None else timeout
        self._validate_timeout(duration)
        body = self._payload(payload, params)
        spec = APIS.get(controller)
        if spec is None and server is None:
            raise ServerRequired("Unknown controllers need an explicit server")
        connection = None
        future: asyncio.Future[JsonValue] | None = None
        request_id = 0
        try:
            async with asyncio.timeout(duration):
                await self.authorize()
                connection = await self._connect(
                    self._server(spec.role if spec else "main", server)
                )
                self._next_id += 1
                request_id = self._next_id
                future = asyncio.get_running_loop().create_future()
                connection.pending[request_id] = future
                await self._emit(connection, controller, body, request_id)
                return await future
        except TimeoutError:
            raise RequestTimeout(f"{controller} exceeded its request deadline") from None
        finally:
            if connection:
                connection.pending.pop(request_id, None)
            if future is not None:
                # Retrieve disconnect errors even when cancellation happened during emit.
                if future.done() and not future.cancelled():
                    future.exception()
                elif not future.done():
                    future.cancel()

    async def send(
        self,
        controller: str,
        payload: Mapping[str, JsonValue] | None = None,
        *,
        server: str | None = None,
        **params: JsonValue,
    ) -> None:
        """Send without requesting an ApiEvent reply (callback ID 0).

        Subscribe first for controllers that communicate through pushes only.
        """
        self._check_open()
        body = self._payload(payload, params)
        spec = APIS.get(controller)
        if spec is None and server is None:
            raise ServerRequired("Unknown controllers need an explicit server")
        try:
            async with asyncio.timeout(self._timeout):
                await self.authorize()
                connection = await self._connect(
                    self._server(spec.role if spec else "main", server)
                )
                await self._emit(connection, controller, body, 0)
        except TimeoutError:
            raise RequestTimeout(f"{controller} exceeded its send deadline") from None

    def subscribe(self, *names: str, max_queue_size: int = 100) -> EventStream:
        """Subscribe immediately; no names selects all events. Does not connect."""
        self._check_open()
        stream = EventStream(names, max_queue_size, self._streams.discard)
        self._streams.add(stream)
        return stream

    async def get_game(self, game_id: int, *, timeout: float | None = None) -> list[JsonValue]:
        """Fetch the InitGameEvent argument list for a public game.

        Argument 0 is game metadata; subsequent arguments contain board and replay
        data. The full server payload is preserved. Subscribe before EnterGameWS
        so the push cannot be missed. Concurrent calls filter by game ID.
        """
        duration = self._timeout if timeout is None else timeout
        self._validate_timeout(duration)
        try:
            async with asyncio.timeout(duration):
                async with self.subscribe("InitGameEvent", "GameNotFoundEvent") as events:
                    await self.enter_game(gameId=game_id, timeout=duration)
                    async for event in events:
                        if event.name == "GameNotFoundEvent":
                            # Not-found pushes are not reliably correlated to requests.
                            continue
                        if event.params and isinstance(event.params[0], dict):
                            if event.params[0].get("id") == game_id:
                                return event.params
        except TimeoutError:
            raise RequestTimeout(f"Game {game_id} did not provide a snapshot") from None
        raise ClientClosed("Client closed while waiting for a game snapshot")

    async def ping(self, *, server: str | None = None) -> float:
        """Call the shard's Socket.IO p event; return round-trip seconds."""
        try:
            async with asyncio.timeout(self._timeout):
                await self.authorize()
                connection = await self._connect(self._server("main", server))
                start = asyncio.get_running_loop().time()
                async with connection.send_lock:
                    await connection.socket.call("p", timeout=self._timeout)
                return asyncio.get_running_loop().time() - start
        except (TimeoutError, socketio.exceptions.TimeoutError):
            raise RequestTimeout("Ping timed out") from None

    async def ping_http(self, *, server: str | None = None) -> str:
        """GET the shard's /ping endpoint and return its text (normally OK)."""
        try:
            async with asyncio.timeout(self._timeout):
                await self.authorize()
                target = self._server_url(self._server("main", server))
                async with self._http_session().get(target + "/ping") as response:
                    response.raise_for_status()
                    return await response.text()
        except TimeoutError:
            raise RequestTimeout("HTTP ping timed out") from None
        except aiohttp.ClientError:
            raise ConnectionError("HTTP ping failed") from None

    async def close(self) -> None:
        """Fail outstanding requests and release every socket, session and stream."""
        async with self._close_lock:
            if self._closed:
                return
            self._closed = True
            for connection in self._connections.values():
                connection.failure = ClientClosed("Client closed")
                connection.ready.set()
                self._fail_pending(connection, connection.failure)
            for stream in tuple(self._streams):
                stream._finish()
            try:
                # Engine.IO's public abort option avoids waiting for a pending
                # long poll. Closing our shared HTTP session then releases the
                # readers, and wait() joins their background tasks.
                await asyncio.gather(
                    *(c.socket.eio.disconnect(abort=True) for c in self._connections.values())
                )
            finally:
                if self._http is not None:
                    await self._http.close()
                await asyncio.gather(*(c.socket.shutdown() for c in self._connections.values()))
                await asyncio.gather(*(c.socket.eio.wait() for c in self._connections.values()))

    async def __aenter__(self) -> WomClient:
        self._check_open()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()
