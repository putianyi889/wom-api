from __future__ import annotations

import asyncio

import pytest

from wom_api import (
    APIS,
    PROTOCOL_VERSION,
    AuthorizationError,
    ClientClosed,
    ConnectionError,
    Event,
    EventOverflow,
    ProtocolError,
    RequestTimeout,
    ServerError,
    ServerRequired,
    WomClient,
)


async def test_real_socket_round_trip_and_ticket_rotation(local_server):
    async with local_server.client(session="existing-session") as client:
        result = await client.search_user(query="Alice", isFinal=False)
        assert result == {"result": [{"id": 7, "username": "Alice"}]}
        sid, frame = await local_server.received.get()
        assert frame == [
            "SearchUserWS",
            {"query": "Alice", "isFinal": False},
            1001,
            PROTOCOL_VERSION,
        ]
        assert local_server.auth_sessions == ["existing-session"]
        assert local_server.socket_auths[0] == {
            "ticket": "private-ticket-1",
            "session": "private-session",
        }
        assert client.authorization.ticket == "rotated-ticket"
        assert "private-session" not in repr(client.authorization)
        assert "rotated-ticket" not in repr(client.authorization)
        assert await client.ping() >= 0
        assert await client.ping_http() == "OK"
    assert client._http.closed
    assert not next(iter(client._connections.values())).socket.connected


async def test_concurrent_requests_are_correlated_out_of_order(local_server):
    async with local_server.client() as client:
        first = asyncio.create_task(client.search_user(query="hold"))
        sid, first_frame = await local_server.received.get()
        second = await client.get_user_info(userId=7)
        assert second["echo"] == {"userId": 7}
        assert not first.done()
        await local_server.sio.emit(
            "response", [first_frame[2], "ApiEvent", [{"first": True}]], to=sid
        )
        assert await first == {"first": True}
        assert not next(iter(client._connections.values())).pending


async def test_snapshot_push_arrives_before_ack_and_concurrent_games(local_server):
    async with local_server.client() as client:
        first, second = await asyncio.gather(client.get_game(42), client.get_game(43))
        assert first == [{"id": 42, "server": "game1"}, {"t": [0, 1, 10]}, [[0, 0, 0, 0]]]
        assert second[0]["id"] == 43
        assert not client._streams


async def test_timeout_and_late_reply_do_not_pollute_next_request(local_server):
    async with local_server.client() as client:
        with pytest.raises(RequestTimeout):
            await client.search_user(query="hold", timeout=0.2)
        sid, frame = await local_server.received.get()
        assert not next(iter(client._connections.values())).pending
        await local_server.sio.emit("response", [frame[2], "ApiEvent", [{"late": True}]], to=sid)
        result = await client.get_user_info(userId=8)
        assert result["echo"]["userId"] == 8


async def test_cancellation_releases_pending_and_subscription(local_server):
    async with local_server.client() as client:
        task = asyncio.create_task(client.search_user(query="hold"))
        await local_server.received.get()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert not next(iter(client._connections.values())).pending
        async with client.subscribe("InitGameEvent") as events:
            assert events in client._streams
        assert not client._streams


@pytest.mark.parametrize(
    "event,params,exception",
    [
        ("response", ["malformed"], ProtocolError),
        ("response", [1001, "ApiEvent", []], ProtocolError),
        ("response", [1001, "SkipEvent", []], ProtocolError),
        ("server_error", ["error"], ServerError),
        ("session_revoked", {"sessionId": 456, "reason": 2}, AuthorizationError),
    ],
)
async def test_errors_complete_outstanding_requests(local_server, event, params, exception):
    async with local_server.client() as client:
        task = asyncio.create_task(client.search_user(query="hold"))
        sid, frame = await local_server.received.get()
        await local_server.sio.emit(event, params, to=sid)
        with pytest.raises(exception):
            await asyncio.wait_for(task, 1)


async def test_disconnect_fails_pending_without_replaying(local_server):
    async with local_server.client() as client:
        task = asyncio.create_task(client.search_user(query="hold"))
        sid, frame = await local_server.received.get()
        await local_server.sio.disconnect(sid)
        with pytest.raises(ConnectionError):
            await asyncio.wait_for(task, 1)
        assert local_server.received.empty()


async def test_close_unblocks_requests_and_streams_and_is_idempotent(local_server):
    client = local_server.client()
    task = asyncio.create_task(client.search_user(query="hold"))
    await local_server.received.get()
    stream = client.subscribe()
    waiting = asyncio.create_task(anext(stream))
    await client.close()
    with pytest.raises(ClientClosed):
        await task
    with pytest.raises(StopAsyncIteration):
        await waiting
    await client.close()
    with pytest.raises(ClientClosed):
        await client.get_user_info(userId=7)


async def test_event_stream_filters_and_reports_overflow(local_server):
    async with local_server.client() as client:
        stream = client.subscribe("NewMessageEvent", max_queue_size=1)
        client._publish(Event("OtherEvent", [], "chat1"))
        client._publish(Event("NewMessageEvent", [1], "chat1"))
        client._publish(Event("NewMessageEvent", [2], "chat1"))
        with pytest.raises(EventOverflow):
            await anext(stream)
        assert not client._streams
        with pytest.raises(StopAsyncIteration):
            await anext(stream)


async def test_notify_and_unknown_controller_escape_hatch(local_server):
    async with local_server.client() as client:
        await client.send("TrackViewWS", id=7, type=1)
        sid, frame = await local_server.received.get()
        assert frame[2] == 0
        result = await client.request("FutureWS", {"field": "value"}, server=local_server.url)
        assert result["echo"] == {"field": "value"}


async def test_http_rejection_does_not_expose_session(local_server):
    local_server.reject_http = True
    async with local_server.client(session="super-secret") as client:
        with pytest.raises(AuthorizationError) as caught:
            await client.authorize()
        assert "super-secret" not in str(caught.value)
        assert caught.value.__suppress_context__


async def test_expired_ticket_refresh_uses_existing_session(local_server):
    local_server.expiry_ms = -1000
    async with local_server.client() as client:
        first = await client.authorize()
        second = await client.authorize()
        assert first.ticket != second.ticket
        assert local_server.auth_sessions == ["", "private-session"]


async def test_pacing_is_within_total_deadline(local_server):
    client = WomClient(
        base_url=local_server.url,
        servers={"main": local_server.url},
        timeout=2,
        min_request_interval=10,
    )
    async with client:
        await client.get_user_info(userId=1)
        with pytest.raises(RequestTimeout):
            await client.get_user_info(userId=2, timeout=0.1)
        assert local_server.received.qsize() == 1
        assert not next(iter(client._connections.values())).pending


async def test_game_role_requires_explicit_server(local_server):
    async with local_server.client() as client:
        with pytest.raises(ServerRequired):
            await client.join_game(gameId=1)
        with pytest.raises(ServerRequired):
            await client.request("UnknownWS")
        result = await client.join_game(gameId=1, server=local_server.url)
        assert result["controller"] == "JoinGameWS"


@pytest.mark.parametrize("timeout", [0, -1, float("nan"), float("inf")])
def test_invalid_deadline(timeout):
    with pytest.raises(ValueError):
        WomClient(timeout=timeout)


async def test_invalid_payloads_fail_before_network():
    async with WomClient() as client:
        with pytest.raises(ValueError):
            await client.get_user_info({"userId": 1}, userId=2)
        with pytest.raises(TypeError):
            await client.get_user_info({"userId": object()})
        with pytest.raises(ValueError):
            await client.get_user_info(userId=float("nan"))
        assert client._http is None


def test_routing_matches_browser_sharding():
    from wom_api.types import Authorization

    client = WomClient()
    client._authorization = Authorization(123, 456, "session", "ticket", 0, {})
    assert client._server("main", None) == "main4"
    assert client._server("hint", None) == "hint4"
    assert client._server("chat", None) == "chat1"
    assert client._server("watcher", None) == "watcher1"


@pytest.mark.parametrize("data", [{}, {"ban": True}, [], {"session": "secret", "ticket": "secret"}])
async def test_malformed_http_authorization_is_rejected(local_server, data):
    local_server.authorization_data = data
    async with local_server.client() as client:
        with pytest.raises(AuthorizationError):
            await client.authorize()


async def test_http_authorization_has_public_timeout_error(local_server):
    local_server.http_ready.clear()
    client = WomClient(base_url=local_server.url, timeout=0.1)
    async with client:
        with pytest.raises(RequestTimeout):
            await client.authorize()
        assert client.authorization is None
    local_server.http_ready.set()


async def test_invalid_socket_authorization_identity(local_server):
    local_server.socket_authorization_data = {"sessionId": 999}
    async with local_server.client() as client:
        with pytest.raises(AuthorizationError):
            await client.connect()
        assert local_server.received.empty()


async def test_close_during_authorized_event_wait_unblocks_connection(local_server, monkeypatch):
    import socketio

    handshake_done = asyncio.Event()
    original_connect = socketio.AsyncClient.connect

    async def connect_and_signal(self, *args, **kwargs):
        await original_connect(self, *args, **kwargs)
        handshake_done.set()

    monkeypatch.setattr(socketio.AsyncClient, "connect", connect_and_signal)
    local_server.omit_socket_authorization = True
    client = local_server.client()
    task = asyncio.create_task(client.connect())
    await local_server.connected.get()
    await handshake_done.wait()
    await client.close()
    with pytest.raises(ClientClosed):
        await asyncio.wait_for(task, 1)


async def test_cancellation_while_waiting_for_socket_authorization(local_server):
    local_server.omit_socket_authorization = True
    async with local_server.client() as client:
        task = asyncio.create_task(client.connect())
        await local_server.connected.get()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        local_server.omit_socket_authorization = False
        # Retry starts a fresh handshake if the first connect was interrupted.
        connection = next(iter(client._connections.values()))
        if connection.started:
            sid = next(iter(local_server.sio.manager.get_participants("/", None)))[0]
            await local_server.sio.emit("authorized", {"sessionId": 456}, to=sid)
        await client.connect()


async def test_successful_sends_respect_minimum_interval(local_server):
    client = WomClient(
        base_url=local_server.url, servers={"main": local_server.url}, min_request_interval=0.025
    )
    async with client:
        await client.get_user_info(userId=1)
        connection = next(iter(client._connections.values()))
        first = connection.last_sent
        await client.get_user_info(userId=2)
        assert connection.last_sent - first >= 0.025


async def test_polling_transport_round_trip(local_server):
    async with asyncio.timeout(2):
        async with local_server.client(transports=("polling",)) as client:
            result = await client.get_user_info(userId=2)
            assert result["echo"] == {"userId": 2}
        connection = next(iter(client._connections.values()))
        assert connection.socket.eio.read_loop_task.done()
        assert not connection.socket.connected


@pytest.mark.parametrize("spec", list(APIS.values()), ids=lambda spec: spec.controller)
async def test_each_entry_point_preserves_controller_and_payload(spec):
    # Exercise dispatch without sending privileged actions to any server.
    class Recorder(WomClient):
        async def request(self, controller, payload=None, *, server=None, timeout=None, **params):
            return [controller, payload, server, timeout, params]

    client = Recorder()
    result = await getattr(client, spec.method)({"x": 1}, server="main1", timeout=5, y=True)
    assert result == [spec.controller, {"x": 1}, "main1", 5, {"y": True}]
