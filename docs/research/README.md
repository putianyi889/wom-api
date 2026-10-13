# Protocol investigation

Reviewed on **2026-10-13**. This report explains the evidence, alternatives and
limits behind the implementation. No official API specification was found.
The scope is the application's public browser bundle, rather than unobservable
server routes or APIs for other versions of the site.

## Primary evidence

- [Site homepage](https://minesweeper.online/): identifies `index-1036.js` and
  `vendor-1036.js`; starts `GET /authorize?session=...` from browser storage.
- [Application bundle](https://minesweeper.online/js/index-1036.js): 236 controller
  classes, their roles and flags, connection auth, routing, request/response
  envelopes and event definitions. Its exact SHA-256 is recorded in the shipped
  `wom_api/api_catalog.json` and exposed as `wom_api.catalog.SOURCE_SHA256`.
- [Vendor bundle](https://minesweeper.online/js/vendor-1036.js): Engine.IO protocol
  revision 4 and a Socket.IO implementation with the v3/v4 namespace handshake.
- [python-socketio compatibility table](https://python-socketio.readthedocs.io/en/latest/intro.html#version-compatibility):
  Python 5.x supports JS Socket.IO 3.x/4.x and Engine.IO 4. This is the mature
  transport implementation used by the package.

The extractor uses Tree-sitter's JavaScript parser. It reads syntax trees without
executing downloaded JavaScript. It collects class declarations, request object
shapes, literal values, destructured callback result fields, event names and the
inherited generic table factory. It deliberately does not guess a complete
request or response schema. Derived metadata is checked in; the full website
bundles and authorization secrets are excluded from distributions.

## Field type evidence

The endpoint catalogue now includes Python field type tables for requests and
responses, including nested object/array paths and nullable unions. It keeps
three evidence categories separate:

- **Frontend syntax:** literals and explicit numeric/boolean/string operations
  in the reviewed JavaScript. Dynamic identifiers and arbitrary helper calls
  remain unresolved rather than being typed from a field's name.
- **Live sample:** successful public request/response values converted to type
  schemas. Only the schemas are retained; no original scalar values or session
  credentials are stored in the observation file.
- **Unresolved:** a field name is known, but its concrete type is not. Its table
  entry uses `JsonValue` until reliable evidence is available.

The tooling reuses [GenSON](https://github.com/wolverdude/genson/) to merge
observations into JSON type schemas. The renderer uses Python notation for the
[JSON Schema primitive types](https://json-schema.org/understanding-json-schema/reference/type).
JSON numbers are shown as `int | float`; integral observations use `int`.
Dates/times transported as strings remain `str`.

The reviewed [type-only observations](type-observations.json) cover
`GetUserInfoWS`, `GetUserDetailDataWS`, `GetRanksTableWS`, `SearchUserWS` and
`FetchUserStatTableWS`. Two public player profiles expose both named and unnamed
players; table count, position and rows are sampled separately. Observations
record the frontend version, bundle hash, collection time and sample counts.
They do not assert exhaustive unions, required fields or server validation
rules. In particular, a null-only sample means **only null has been observed**,
not that null is the only possible value. Null and omitted properties differ.

`tools/observe_types.py` performs opt-in public reads and stores type schemas.
`discover.py --observations ...` merges them only when the version and source
hash match the reviewed bundle. `generate.py` renders the stored metadata
offline. Authenticated writes and administrator APIs have not been sampled.

## Existing solutions

[tonyd33/mso-api](https://github.com/tonyd33/mso-api) was examined through its
[repository listing](https://api.github.com/repos/tonyd33/mso-api/contents).
Its historical [author's protocol investigation](https://tangled.org/tonyd.tngl.sh/blog/blob/c02ba8caf0ae6f99da938b84f9c185bdaae92fbc/content/posts/reverse-engineering-minesweeper-online-to-electrocute-myself-and-more.md)
describes the older `authKey` handshake, Engine.IO 3 and obfuscated game
operations. Those details do not match the live 1036 frontend. The repository
contains a TypeScript application rather than a current complete Python data
package. No implementation code was copied.

Other search results named “minesweeper online API” targeted unrelated
Minesweeper applications or screen-based game automation. They did not provide
the current site's full data API. Hand-written polling/WebSocket frames would
duplicate Socket.IO, so the library uses `python-socketio` and `aiohttp` instead.

## Authorization and topology

HTTP `GET /authorize?session=<existing-or-empty>` returns session, ticket,
sessionId, ticketExpiresAt, userId, user and other bootstrap metadata. Empty
session creates a guest. The current socket auth payload is `{ticket, session}`,
**not** the historical URL query with authKey and userId. The socket must receive
the `authorized` event before API requests can be sent.

`authorized` contains a rotated ticket, sessionId and expiry. `session_revoked`
indicates an unusable session. Tickets are refreshed through HTTP or accepted
from socket authorization. The package keeps secrets out of object repr and
HTTP error messages and does not enable packet logging.

| Browser role | Default production shard | Controllers |
| --- | --- | ---: |
| main | `main{1 + userId % 10}` | 208 |
| chat | `chat1` | 13 |
| game | selected game server | 9 |
| watcher | `watcher1` | 5 |
| hint | `hint{1 + userId % 4}` | 1 |

Requests use the Socket.IO event `request` with this JSON array:

```text
[controllerName, requestObjectOrNull, callbackIdOrZero, 1036]
```

Replies use `response`:

```text
[callbackIdOrNull, eventName, argumentList]
```

`ApiEvent` wraps one callback result. `SkipEvent` discards a callback in the
browser; the Python client exposes it as `ProtocolError` so callers do not hang.
Named domain events drive the browser UI and often have no callback ID.
The catalogue records 46 named event classes. Additional future names can still
be consumed through subscriptions.

The browser normally paces non-game requests at 125ms and marks some controllers
as skipping that limit. The package applies a configurable per-shard minimum
interval to all requests. This is pacing, not a claim about the server's actual
quota or permission rules.

## HTTP and other surfaces

`authorize()` covers the bootstrap HTTP endpoint. The frontend also probes
`GET https://<shard>.minesweeper.online/ping` and sends the Socket.IO `p` event
with an acknowledgement; the client exposes these as `ping_http()` and `ping()`.
HTML pages, images, translations, third-party billing redirects and static
downloads are not counted as data controllers. They do not establish an
additional HTTP JSON API in this reviewed bundle.

The 236-controller count includes account changes, purchases, gameplay, chat and
35 administrator operations visible in the bundle. They have entry points for
completeness; server authorization still applies. Their presence does not imply
that guest access is possible. The library itself does not execute those actions
during authorization or connection.

## Verification and limits

The live anonymous connection verified the `authorized` ticket rotation and:

| Request | Verified result |
| --- | --- |
| `GetUserInfoWS` | Correlated `ApiEvent`, result with matching `user.id` |
| `GetRanksTableWS` | `ApiEvent` with `ranksCount` |
| `FetchUserStatTableWS` | Three beginner time-ranking rows in a correlated `ApiEvent` |
| `EnterGameWS` on completed game 6646633208 | `InitGameEvent` before the API acknowledgement, plus `GameResultEvent` |
| Socket.IO `p` | Acknowledged round trip |
| HTTP `/ping` | `OK` response from the main shard |

`EnterGameWS` acknowledges with `{}` after pushing the board/replay. This is why
`get_game()` subscribes first and returns the matching full event argument list.

Only public reads are exercised live. The package does not claim that every
controller was tested against the website. Authenticated account data, game
actions, purchases, chat writes and administrator requests require appropriate
accounts and have not been executed. Local protocol tests exercise connection
lifecycle and dispatch without calling those production actions. Socket.IO
heartbeats and framing remain the upstream library's responsibility.

The initial local verification used Windows and Python 3.14.6: 272 tests passed,
including real local WebSocket and polling round trips, concurrent callback
correlation, cancellation, deadlines, ticket rotation, bounded event streams
and transport cleanup. Ruff, strict mypy, Sphinx's warning-as-error build,
wheel/sdist creation and Twine metadata checks passed. A separate virtual
environment installed the wheel and imported all 236 entries and bundled type
and catalogue resources. The other Python versions in CI have not been run
locally, and no remote workflow or PyPI upload was executed.

The frontend contains a requestSchema property on its base API class but no
concrete schemas on these controllers. Input/output shapes and types derived from
usage are partial observations; some are dynamic and are explicitly unresolved.
Client-side validation consequently checks JSON encoding and duplicate fields,
rather than inventing field requirements.

When the frontend changes, fetch the new public bundle and review catalogue
diffs. Follow [the update procedure](../development.md). A hard-coded version
is intentional: silent discovery on import or connect would introduce network
side effects and could change the contract without review.
