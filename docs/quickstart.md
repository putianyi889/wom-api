# Quick start

Install a published GitHub Release wheel, choosing the desired version:

```sh
python -m pip install "https://github.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl"
```

Or install a fixed Git tag; this requires Git on your machine:

```sh
python -m pip install "wom-api @ git+https://github.com/putianyi889/wom-api.git@v0.1.0"
```

The same direct reference works in your application's `requirements.txt`:

```text
wom-api @ https://github.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl
```

These URLs work after the matching tag or release is published. The wheel
contains the package; its dependencies still use pip's configured package
index. Use a versioned asset or a full Git commit hash for a reproducible
dependency, rather than following a moving branch.

The Gitee mirror also supports a fixed Git tag:

```sh
python -m pip install "wom-api @ git+https://gitee.com/putianyi889/wom-api.git@v0.1.0"
```

Gitee `v0.1.0` is published. Download its wheel and install the local file with
`python -m pip install ./wom_api-0.1.0-py3-none-any.whl`. Direct pip access to
the Gitee URL returned HTTP 403 in validation; local installation passed.
See the [Gitee publishing guide](publishing-gitee.md).

For this checkout:

```sh
python -m pip install -e .
```

```python
import asyncio
from wom_api import WomClient


async def main():
    async with WomClient() as client:
        profile = await client.get_user_info(userId=1)
        print(profile["user"])
        players = await client.search_user(query="player name", isFinal=False)
        print(players["result"])


asyncio.run(main())
```

The client creates an anonymous session automatically. To access your account's
data, supply the value of `localStorage['_session']` from your own browser on
minesweeper.online as `WomClient(session=...)`. Treat it as a credential. The
library does not read browser storage or save sessions to disk. `client.session`
lets you explicitly persist a new guest session for reuse.

All 236 controller methods are async. Pass a dictionary or keyword arguments
with the website's original camelCase field names. JSON responses retain their
original structure, integers, nulls, and timestamp strings. Responses are not
converted into guessed models.

```python
profile = await client.get_user_detail_data({"userId": 1, "popupRandId": None})
# Equivalent:
profile = await client.get_user_detail_data(userId=1, popupRandId=None)
```

The [endpoint catalogue](endpoints.md) lists each method, controller, role,
observed input shapes and response fields. These are browser observations rather
than complete required-field schemas. Account-only requests and administrator
requests still require the website's permissions.

Each resolved shape also has request/response field type tables, including
nested paths such as `user.username` and `result[].id`. Types use Python notation
and include their evidence. A field marked `JsonValue` / `unresolved` has no
reliable concrete type yet. Nullable values and omitted fields are different;
the type tables do not assert requiredness.

## Rankings and other tables

The browser's table controllers share an envelope. `dataType=1` requests the
count, `2` requests your position, and `3` requests rows. `url` is the page path
that will be echoed back; `params` contains page-specific filters. For example,
the beginner all-time time ranking:

```python
await client.authorize()
ranking = await client.fetch_user_stat_table(
    {
        "url": "/ranking",
        "dataType": 3,
        "limit": 10,
        "offset": 0,
        "params": {
            "userId": client.authorization.user_id,
            "season": 0,
            "country": "",
            "sortBy": "timePoints",
            "brLevel": 1,
        },
    }
)
print(ranking["rows"])
```

Change `limit` and `offset` explicitly to request another page. A season uses the
website's season identifier, rather than an ISO date. The catalogue includes
observed nested table parameter names and default sort keys.

## Board and replay data

```python
snapshot = await client.get_game(6646633208)
metadata = snapshot[0]
board = snapshot[1]
print(metadata["server"], metadata["sizeX"], metadata["sizeY"])
```

`get_game()` returns the **entire argument list** of the matching `InitGameEvent`.
It subscribes before sending `EnterGameWS`, so an early push is not missed.
Subsequent arguments contain the board and replay payloads. The actual structure
depends on the game; inspect it rather than assuming a fixed record schema.
`enter_game()` alone returns its API acknowledgement, which can be `{}`.

## Inspect and extend the API

```python
from wom_api import APIS, EVENT_NAMES

print(APIS["GetUserInfoWS"])
print(EVENT_NAMES)
result = await client.request("GetUserInfoWS", {"userId": 1})
# A new controller that isn't in the reviewed catalogue requires its shard:
result = await client.request("NewControllerWS", {"field": 1}, server="main2")
```

Pass wire fields called `payload`, `server`, or `timeout` inside the dictionary
because those names are reserved by Python method signatures.

## Account transitions

`sign_in()`, `use_auth_code()`, and `terminate_session()` are exposed like the
other controllers. They can close or revoke sessions. They do not silently
replace the client's account or guess the meaning of the returned JSON. After
a successful account transition, close the client and construct another one
with the session returned by the website. No password is needed when reusing
your own browser session.
