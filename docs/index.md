# wom-api

An async Python client for the data protocol used by
[Minesweeper Online](https://minesweeper.online/). The package has an explicit
method for every controller found in the reviewed public frontend, plus HTTP
authorization, connection management, event streams, and public game snapshots.

Python 3.11+ is required. Distribution name: `wom-api`; import name: `wom_api`.
Packages are distributed through GitHub Releases; pip can install the wheel URL
or a fixed Git tag. See the quick start for installation commands.
This is an independent project. The browser protocol is undocumented by the
website and may change; the research report records the exact bundle and scope.

```{toctree}
:maxdepth: 2

quickstart
quickstart-zh
connections
endpoints
reference
research/README
development
publishing-gitee
research/gitee/README
```
