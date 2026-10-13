# Development and publishing

## Setup and checks

```sh
python -m venv .venv
# Activate .venv, then:
python -m pip install -e ".[dev,docs,research]"
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy
python tools/generate.py --check
python -m sphinx -W --keep-going -b html docs docs/_build/html
python -m build
python -m twine check dist/*.whl dist/*.tar.gz
```

On PowerShell you can use `.\.venv\Scripts\python.exe` directly. This is a Python
project and has no JavaScript application, ESLint configuration or Cypress
suite. The pytest suite uses a local aiohttp/Socket.IO server and never accesses
minesweeper.online. CI checks Python 3.11–3.14; Linux and Windows are included.

The separate live smoke script only runs when explicitly invoked:

```sh
python examples/live_check.py --game-id 6646633208
# For environments requiring the system certificate store:
python -m pip install -e ".[system-certs]"
python examples/live_check.py --system-certs --game-id 6646633208
```

It checks public profile, ranks, a three-row ranking, ping and optionally a game
snapshot. `WOM_SESSION` optionally supplies your session without placing it in
command-line arguments. The script prints structural checks rather than tokens.

## Update the reviewed API

1. Read the homepage's current application script URL.
2. Download that `index-NNNN.js` to an ignored `.research-index.js` file.
3. Parse it without executing it:

   ```sh
   python tools/discover.py .research-index.js --version NNNN
   ```

4. Review `src/wom_api/api_catalog.json`, including roles, controller names,
   inferred table fields, source hash and any method-name collisions. The
   extractor refuses syntax errors and empty catalogues. It supports the
   reviewed bundle's class shapes; new obfuscation or changed table factories
   require an extractor update and tests.
5. Run `python tools/generate.py`. This writes explicit controller methods and
   the endpoint reference, including field type tables, from the same catalogue.
   It uses Ruff's formatter and requires the `dev` and `research` extras.
6. Verify all checks, public live reads, and protocol envelopes. Update the
   research report's version and evidence. Avoid committing downloaded bundles
   or session credentials.

`discover.py --check` compares a local bundle against the reviewed catalogue.
CI uses `generate.py --check` offline, so a site deployment cannot unexpectedly
break an otherwise reproducible build.

For the current reviewed bundle, reproduce the catalogue with its type evidence:

```sh
python tools/discover.py .research-index.js --version 1036 --observations docs/research/type-observations.json --check
```

To refresh public request/response type observations explicitly:

```sh
python tools/observe_types.py --system-certs
python tools/discover.py .research-index.js --version 1036 --observations docs/research/type-observations.json
python tools/generate.py
```

Omit `--system-certs` when the default TLS configuration works. The collector
uses only public reads, stores JSON type schemas rather than original scalar
values, and removes sample-derived required-field constraints. An optional
`WOM_SESSION` reuses an existing session. Review the observation diff before
updating the catalogue. After a frontend version change, collect matching new
observations; previous version/hash evidence is intentionally rejected.

## Release

The initial version is `0.1.0`. Update `pyproject.toml` and `wom_api.__version__`
together before a new release. The wheel includes the typed package, reviewed
JSON catalogue, and license. The sdist also includes tests, research tooling,
examples and documentation. Builds use Hatchling and standard PEP 517 tooling.

```sh
python -m build
python -m twine check dist/*.whl dist/*.tar.gz
```

Twine is used here for offline distribution metadata validation. Releases are
uploaded to GitHub through the GitHub CLI.

### Publish a GitHub Release

1. Create or choose your GitHub repository, configure `origin`, and push this
   project. The publish workflow must be present on the repository's default
   branch so it can be manually dispatched.
2. Ensure `pyproject.toml` and `wom_api.__version__` contain the intended version,
   then create and push a matching tag:

   ```sh
   git tag -a v0.1.0 -m "wom-api 0.1.0"
   git push origin v0.1.0
   ```

3. In GitHub Actions, run **Publish GitHub Release** with `tag=v0.1.0`. The
   workflow checks out `refs/tags/v0.1.0`, verifies that the tag matches the
   package version, and runs tests, lint, type checks, documentation and
   distribution validation.
4. On success, it creates a GitHub Release containing the wheel, source archive,
   and `wom_api-0.1.0-docs.zip` with the searchable HTML documentation. Extract
   the documentation ZIP and open `index.html`. Release notes are generated
   through GitHub's Release Notes API.

The workflow uses the built-in `GITHUB_TOKEN` with `contents: write` in the
release job. No PyPI publisher, PyPI token or additional third-party upload
action is required. The tag must already exist remotely; the CLI uses
[`--verify-tag`](https://cli.github.com/manual/gh_release_create) to check this.
Regular pushes and tag pushes alone do not publish a release. A repeated run
for an existing release fails rather than replacing its assets.

Users install a specific wheel URL or Git tag as shown in the
[quick start](quickstart.md), using the
[putianyi889/wom-api repository](https://github.com/putianyi889/wom-api).
Distribution filenames use `wom_api`; the Python import
name remains `wom_api` and the project name remains `wom-api`.

Documentation uses Sphinx + MyST Markdown + Furo. Open
`docs/_build/html/index.html` after building locally. `.readthedocs.yaml` is
provided for hosting; connect the repository to Read the Docs to publish it.
The release workflow includes a versioned HTML documentation archive. Read the
Docs hosting can be configured separately.
