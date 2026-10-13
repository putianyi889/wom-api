# Connections, deadlines and events

The library uses `python-socketio` 5.x for Socket.IO 4 / Engine.IO 4. The website
uses `/mine-websocket` and sends `{ticket, session}` as the Socket.IO auth body.
HTTP `/authorize` creates or resumes a session. Authorization tickets expire;
the client refreshes an expired ticket before a new connection and accepts
rotated tickets from the `authorized` event. TLS verification remains enabled.

## Protocol field types

The Socket.IO `request` event carries a four-element array:

| Index | Field | Python type | Meaning |
| --- | --- | --- | --- |
| 0 | controller | `str` | Controller name, e.g. `GetUserInfoWS` |
| 1 | payload | `dict[str, JsonValue]` or `None` | Request fields; endpoint-specific types appear in the catalogue |
| 2 | callback ID | `int` | Positive request identifier, or 0 for `send()` |
| 3 | frontend version | `int` | Reviewed protocol version |

The Socket.IO `response` event carries a three-element array:

| Index | Field | Python type | Meaning |
| --- | --- | --- | --- |
| 0 | callback ID | `int` or `None` | Correlation identifier; absent on many pushes |
| 1 | event name | `str` | `ApiEvent`, `InitGameEvent`, or another event |
| 2 | arguments | `list[JsonValue]` | Original event arguments; `ApiEvent` wraps one result |

The returned `ApiEvent` result has endpoint-specific field types in the
[catalogue](endpoints.md). `InitGameEvent` and other pushes have different
argument layouts and are not the API acknowledgement's response object.

## Lifecycle

```python
async with WomClient(session=existing_session) as client:
    await client.connect()  # optional; requests connect lazily
    data = await client.get_user_info(userId=1)
```

One Socket.IO client is maintained per server. The default routing matches the
reviewed frontend: `main{1 + userId % 10}`, `hint{1 + userId % 4}`, `chat1`, and
`watcher1`. Game requests require `server=` from game metadata. You can override
roles with `servers={"main": "main1"}` or supply a complete HTTP origin for a
test server. Use each `WomClient` within one asyncio event loop.

`close()` is idempotent and permanently closes the client. It stops reconnection,
closes the HTTP session and sockets, ends streams and fails outstanding calls.
It aborts pending long polls and waits for transport background tasks to finish.
The client does not play a new game or initialize chat when connecting.

## Concurrent calls and pacing

```python
profiles = await asyncio.gather(
    client.get_user_info(userId=1),
    client.get_user_info(userId=2),
)
```

Each request has its own callback ID. Responses may arrive in any order. Sends
are serialized per shard and paced by `min_request_interval` (default 0.125s,
matching the frontend's ordinary request pacing). Requests do not queue until
infinity: their total deadline includes authorization, connection, pacing and
response. You can supply a per-request `timeout=` in seconds. The client never
skips its pacing based on an endpoint's `skipRateLimit` flag; the recorded flag
describes the browser, and is not a request to increase load.

Transport interruptions can trigger Socket.IO's reconnection. In-flight calls
fail immediately on disconnect. They are **never replayed**, including reads,
because a timeout or disconnect cannot prove that a server action did not run.
Reconnection reuses or refreshes authorization. If the server explicitly closes
the Socket.IO namespace, it may not reconnect automatically; use a new client.
Session revocation requires a new valid session and client.

## Subscriptions

```python
async with client.subscribe("InitGameEvent", "GameResultEvent") as events:
    await client.send("EnterGameWS", gameId=6646633208)
    async for event in events:
        print(event.name, event.server, event.params)
        if event.name == "InitGameEvent":
            break
```

Subscriptions register immediately, before awaiting the context manager. They
do not establish connections by themselves. With no names, a subscription
receives every response event, including unknown future event names, plus
`disconnect`, `server_error`, and `session_revoked`. `Event.params` retains the
original argument list. `request_id=0` means the server supplied no callback ID.

The default buffer holds 100 events. If a consumer falls behind, the stream
fails with `EventOverflow` and unsubscribes. This does not silently lose data
or block the socket reader. Choose a larger `max_queue_size` if needed.
Exiting the context manager discards buffered events and ends the stream.

Controller methods wait for a correlated `ApiEvent`, returning its single JSON
result. Push-only interactions can use `send()` (callback ID 0) and a
subscription. Domain pushes may have no correlation ID, so a matching event
cannot automatically be assigned to every arbitrary request.

## Errors

| Exception | Meaning |
| --- | --- |
| `AuthorizationError` | HTTP bootstrap failed, socket identity invalid, or session revoked |
| `ConnectionError` | Cannot connect, or disconnected while requests were pending |
| `RequestTimeout` | Total request/connection deadline exceeded |
| `ProtocolError` | Malformed response or explicit `SkipEvent` |
| `ServerError` | Explicit Socket.IO `server_error` event |
| `ServerRequired` | Game or unknown controller lacks explicit routing |
| `ClientClosed` | Client is permanently closed |
| `EventOverflow` | Subscription buffer filled |

Domain rejection events such as `TooManyRequestsEvent`, `OldVersionEvent`, or
`GameNotFoundEvent` remain available in subscriptions. Their callback/correlation
behavior is not guaranteed across controllers. A request can consequently fail
with a skip or deadline rather than a structured HTTP-like status. Handle and
inspect the original events when you need controller-specific diagnostics.

## System certificate stores

Some Windows environments require the system trust store rather than Python's
default SSL certificate configuration. If default verification fails, install
the optional `system-certs` extra and explicitly provide a verified context:

```python
import ssl
import truststore

context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client = WomClient(ssl_context=context)
```

Both HTTP authorization and WebSocket connections use that context.
