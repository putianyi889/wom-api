from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

import aiohttp
import pytest
import pytest_asyncio
from aiohttp import web

from tools.publish_gitee import PublishError, publish, validate_release

TAG = "v0.1.0"
COMMIT = "a" * 40
TOKEN = "private-gitee-token"


@pytest.fixture
def release_files(tmp_path):
    assets = []
    for name in (
        "wom_api-0.1.0-py3-none-any.whl",
        "wom_api-0.1.0.tar.gz",
        "wom_api-0.1.0-docs.zip",
    ):
        content = name.encode()
        (tmp_path / name).write_bytes(content)
        assets.append(
            {
                "name": name,
                "size": len(content),
                "digest": "sha256:" + hashlib.sha256(content).hexdigest(),
                "state": "uploaded",
            }
        )
    return {"tag_name": TAG, "draft": False, "name": "Release", "body": "Notes", "assets": assets}


@dataclass
class GiteeServer:
    url: str = ""
    requests: list[str] = field(default_factory=list)
    uploads: dict[str, bytes] = field(default_factory=dict)
    release: dict | None = None
    tag_sha: str = COMMIT
    tag_shape: str = "object"
    missing_tag: bool = False
    paginated: bool = False
    existing: bool = False
    status: int = 200
    upload_status: int = 201
    redirect: bool = False


@pytest_asyncio.fixture
async def gitee_server():
    server = GiteeServer()

    async def handle(request):
        server.requests.append(request.path)
        if server.redirect:
            return web.Response(status=302, headers={"Location": "/credential-leak"})
        if server.status != 200:
            # A response may echo credentials; error output must not include it.
            return web.Response(status=server.status, text=TOKEN)
        if request.method == "GET":
            assert request.query["access_token"] == TOKEN
        if request.path.endswith("/tags"):
            if server.paginated and request.query["page"] == "1":
                return web.json_response([{"name": f"other-{i}"} for i in range(100)])
            commit = server.tag_sha if server.tag_shape == "string" else {"sha": server.tag_sha}
            return web.json_response(
                [] if server.missing_tag else [{"name": TAG, "commit": commit}]
            )
        if "/releases/tags/" in request.path:
            return web.json_response({"id": 42}) if server.existing else web.Response(status=404)
        if request.path.endswith("/releases"):
            server.release = dict(await request.post())
            assert server.release.pop("access_token") == TOKEN
            return web.json_response({"id": 42}, status=201)
        if request.path.endswith("/attach_files"):
            reader = await request.multipart()
            token_part = await reader.next()
            assert token_part.name == "access_token"
            assert await token_part.text() == TOKEN
            file_part = await reader.next()
            assert file_part.name == "file"
            server.uploads[file_part.filename] = bytes(await file_part.read())
            return web.json_response(
                {
                    "browser_download_url": "https://gitee.com/download/asset",
                    "name": file_part.filename,
                    "size": len(server.uploads[file_part.filename]),
                },
                status=server.upload_status,
            )
        raise AssertionError(f"Unexpected request: {request.path}")

    app = web.Application()
    app.router.add_route("*", "/{tail:.*}", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "127.0.0.1", 0)
    await site.start()
    server.url = f"http://127.0.0.1:{site._server.sockets[0].getsockname()[1]}"
    try:
        yield server
    finally:
        await runner.cleanup()


async def run_publish(server, manifest, tmp_path, **overrides):
    kwargs = dict(
        repository="owner/wom-api",
        token=TOKEN,
        tag=TAG,
        commit=COMMIT,
        manifest=manifest,
        directory=tmp_path,
        api_url=server.url,
    )
    kwargs.update(overrides)
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=2)) as session:
        return await publish(session, **kwargs)


@pytest.mark.parametrize("tag_shape", ["string", "object"])
async def test_publishes_all_assets_and_preserves_release(
    gitee_server, release_files, tmp_path, tag_shape
):
    gitee_server.tag_shape = tag_shape
    gitee_server.paginated = True
    assert await run_publish(gitee_server, release_files, tmp_path) == 42
    assert gitee_server.release == {
        "tag_name": TAG,
        "target_commitish": COMMIT,
        "name": "Release",
        "body": "Notes",
        "prerelease": "false",
    }
    assert gitee_server.uploads == {
        asset["name"]: (tmp_path / asset["name"]).read_bytes() for asset in release_files["assets"]
    }


@pytest.mark.parametrize("problem", ["digest", "size", "missing", "draft", "tag", "extra"])
async def test_invalid_source_makes_no_requests(gitee_server, release_files, tmp_path, problem):
    if problem in {"digest", "size"}:
        release_files["assets"][0][problem] = "incorrect"
    elif problem == "missing":
        (tmp_path / release_files["assets"][0]["name"]).unlink()
    elif problem == "draft":
        release_files["draft"] = True
    elif problem == "tag":
        release_files["tag_name"] = "v9.9.9"
    else:
        release_files["assets"].append({"name": "unexpected"})
    with pytest.raises(PublishError):
        await run_publish(gitee_server, release_files, tmp_path)
    assert not gitee_server.requests


@pytest.mark.parametrize("problem", ["missing_tag", "wrong_commit", "existing"])
async def test_target_preflight_prevents_mutation(gitee_server, release_files, tmp_path, problem):
    if problem == "wrong_commit":
        gitee_server.tag_sha = "b" * 40
    else:
        setattr(gitee_server, problem, True)
    with pytest.raises(PublishError):
        await run_publish(gitee_server, release_files, tmp_path)
    assert gitee_server.release is None
    assert not gitee_server.uploads


@pytest.mark.parametrize("status", [401, 403, 429, 500])
async def test_http_error_does_not_leak_token(
    gitee_server, release_files, tmp_path, status, capsys
):
    gitee_server.status = status
    with pytest.raises(PublishError, match=f"HTTP {status}") as error:
        await run_publish(gitee_server, release_files, tmp_path)
    assert TOKEN not in str(error.value)
    assert TOKEN not in capsys.readouterr().out
    assert len(gitee_server.requests) == 1


async def test_upload_error_stops_without_retry(gitee_server, release_files, tmp_path):
    gitee_server.upload_status = 500
    with pytest.raises(PublishError, match="HTTP 500"):
        await run_publish(gitee_server, release_files, tmp_path)
    assert len(gitee_server.uploads) == 1


async def test_redirect_does_not_forward_credentials(gitee_server, release_files, tmp_path):
    gitee_server.redirect = True
    with pytest.raises(PublishError, match="HTTP 302"):
        await run_publish(gitee_server, release_files, tmp_path)
    assert len(gitee_server.requests) == 1


@pytest.mark.parametrize(
    "overrides", [{"token": ""}, {"repository": "bad/repo/path"}, {"commit": "main"}]
)
async def test_invalid_configuration_makes_no_requests(
    gitee_server, release_files, tmp_path, overrides
):
    with pytest.raises(PublishError):
        await run_publish(gitee_server, release_files, tmp_path, **overrides)
    assert not gitee_server.requests


def test_unsafe_tag_rejected(release_files, tmp_path):
    with pytest.raises(PublishError):
        validate_release(release_files, tmp_path, "../../release")
