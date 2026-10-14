# wom-api

Async Python client for [Minesweeper Online](https://minesweeper.online/), distributed
through GitHub Releases. Python 3.11+. This is an independent, unofficial
project using the website's browser protocol.

- **236 explicit API methods**, extracted from reviewed frontend version 1036.
- Anonymous or existing-session authorization and Socket.IO connection management.
- Concurrent requests, per-shard pacing, deadlines, cancellation and cleanup.
- Event subscriptions and public game board/replay snapshots.
- Typed package, Sphinx documentation, offline protocol tests and publishing workflow.

Install this checkout:

```sh
python -m pip install -e .
```

After a GitHub Release is published, install its wheel directly:

```sh
python -m pip install "https://github.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl"
```

You can also install a fixed Git tag:

```sh
python -m pip install "wom-api @ git+https://github.com/putianyi889/wom-api.git@v0.1.0"
```

Git installs require Git on your machine. The package's runtime dependencies
are installed normally by pip. The installation URLs become usable after the
matching tag or release has been published to the repository.

```python
import asyncio
from wom_api import WomClient


async def main():
    async with WomClient() as client:
        profile = await client.get_user_info(userId=1)
        print(profile["user"])


asyncio.run(main())
```

Pass your browser's `localStorage['_session']` value as `WomClient(session=...)`
for your account data. Parameter names retain their original camelCase spelling.
Returns are raw JSON; administrator and account endpoints retain server-side
permission requirements. The reviewed bundle is not an official stable API.

Read the [quick start](docs/quickstart.md), [中文入门](docs/quickstart-zh.md),
[complete API catalogue](docs/endpoints.md),
[connection and event guide](docs/connections.md), and
[protocol investigation](docs/research/README.md). The catalogue states which
field shapes were observed and which remain unresolved; production validation
covers public reads rather than every authenticated/action controller.
Request/response type tables include nested fields, nullable values and the
evidence behind each concrete type; unresolved types are explicitly marked.

Build the searchable HTML documentation:

```sh
python -m pip install -e ".[docs]"
python -m sphinx -W -b html docs docs/_build/html
```

Open `docs/_build/html/index.html`. For tests, protocol updates, wheel/sdist
builds and GitHub Releases, see the [development guide](docs/development.md).

The [Gitee mirror](https://gitee.com/putianyi889/wom-api) supports Git tag
installation. A separate manual workflow can copy a GitHub Release and its
three verified assets to Gitee; see the [Gitee publishing guide](docs/publishing-gitee.md).

