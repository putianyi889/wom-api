from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field

import pytest_asyncio
import socketio
from aiohttp import web

from wom_api import WomClient


@dataclass
class LocalServer:
    sio: socketio.AsyncServer
    url: str = ""
    received: asyncio.Queue = field(default_factory=asyncio.Queue)
    auth_sessions: list[str] = field(default_factory=list)
    socket_auths: list[dict] = field(default_factory=list)
    connected: asyncio.Queue = field(default_factory=asyncio.Queue)
    auth_ready: asyncio.Event = field(default_factory=asyncio.Event)
    reject_http: bool = False
    expiry_ms: int = 3600000
    http_ready: asyncio.Event = field(default_factory=asyncio.Event)
    http_requested: asyncio.Event = field(default_factory=asyncio.Event)
    authorization_data: object = None
    socket_authorization_data: object = None
    omit_socket_authorization: bool = False

    def client(self, **kwargs) -> WomClient:
        return WomClient(
            base_url=self.url,
            servers={role: self.url for role in ("main", "chat", "hint", "watcher")},
            timeout=2,
            min_request_interval=0,
            **kwargs,
        )


@pytest_asyncio.fixture
async def local_server():
    sio = socketio.AsyncServer(async_mode="aiohttp")
    server = LocalServer(sio)
    server.auth_ready.set()
    server.http_ready.set()
    app = web.Application()
    sio.attach(app, socketio_path="mine-websocket")

    async def authorize(request):
        server.auth_sessions.append(request.query.get("session", ""))
        server.http_requested.set()
        await server.http_ready.wait()
        if server.reject_http:
            return web.json_response({"error": "rejected"}, status=403)
        if server.authorization_data is not None:
            return web.json_response(server.authorization_data)
        return web.json_response(
            {
                "session": "private-session",
                "ticket": f"private-ticket-{len(server.auth_sessions)}",
                "userId": 123,
                "sessionId": 456,
                "ticketExpiresAt": int(time.time() * 1000) + server.expiry_ms,
                "user": {"id": 123},
            }
        )

    async def ping(request):
        return web.Response(text="OK")

    app.router.add_get("/authorize", authorize)
    app.router.add_get("/ping", ping)

    @sio.event
    async def connect(sid, environ, auth):
        server.socket_auths.append(auth)
        await server.auth_ready.wait()
        if server.omit_socket_authorization:
            server.connected.put_nowait(sid)
            return
        if server.socket_authorization_data is not None:
            await sio.emit("authorized", server.socket_authorization_data, to=sid)
            server.connected.put_nowait(sid)
            return
        await sio.emit(
            "authorized",
            {
                "sessionId": 456,
                "ticket": "rotated-ticket",
                "ticketExpiresAt": int(time.time() * 1000) + 3600000,
            },
            to=sid,
        )
        server.connected.put_nowait(sid)

    @sio.on("request")
    async def request(sid, data):
        server.received.put_nowait((sid, data))
        controller, payload, callback, version = data
        if payload and payload.get("query") == "hold":
            return
        if controller == "EnterGameWS":
            await sio.emit(
                "response",
                [
                    None,
                    "InitGameEvent",
                    [
                        {"id": payload["gameId"], "server": "game1"},
                        {"t": [0, 1, 10]},
                        [[0, 0, 0, 0]],
                    ],
                ],
                to=sid,
            )
            result = {}
        elif controller == "SearchUserWS":
            result = {"result": [{"id": 7, "username": payload["query"]}]}
        else:
            result = {"echo": payload, "controller": controller}
        if callback:
            await sio.emit("response", [callback, "ApiEvent", [result]], to=sid)

    @sio.on("p")
    async def socket_ping(sid):
        return "OK"

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 0)
    await site.start()
    port = site._server.sockets[0].getsockname()[1]
    server.url = f"http://127.0.0.1:{port}"
    try:
        yield server
    finally:
        server.auth_ready.set()
        server.http_ready.set()
        for sid in list(sio.manager.get_participants("/", None)):
            await sio.disconnect(sid[0])
        for engine_sid in list(sio.eio.sockets):
            await sio.eio.disconnect(engine_sid)
        await sio.shutdown()
        await runner.cleanup()
