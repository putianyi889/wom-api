"""Publish the three verified assets of an existing GitHub Release to Gitee."""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

import aiohttp


class PublishError(Exception):
    """A safe-to-print publishing error (never contains HTTP credentials)."""


def validate_release(manifest: dict, directory: Path, tag: str) -> list[Path]:
    """Check all inputs before making any remote changes."""
    if not re.fullmatch(r"v\d+\.\d+\.\d+(?:(?:a|b|rc)\d+)?", tag):
        raise PublishError("Expected a version tag such as v0.1.0")
    if manifest.get("tag_name") != tag or manifest.get("draft") is not False:
        raise PublishError("Source must be a published GitHub Release with the requested tag")
    version = tag[1:]
    expected = {
        f"wom_api-{version}-py3-none-any.whl",
        f"wom_api-{version}.tar.gz",
        f"wom_api-{version}-docs.zip",
    }
    assets = manifest.get("assets", [])
    if not isinstance(assets, list) or len(assets) != 3:
        raise PublishError("Source release must contain exactly the wheel, sdist and documentation")
    if any(not isinstance(asset, dict) for asset in assets):
        raise PublishError("Invalid source asset metadata")
    if {asset.get("name") for asset in assets} != expected:
        raise PublishError("Source asset names do not match the requested version")
    paths = []
    for asset in assets:
        path = directory / asset["name"]
        if not path.is_file() or path.is_symlink() or path.stat().st_size != asset.get("size"):
            raise PublishError(f"Missing file or incorrect size: {path.name}")
        with path.open("rb") as stream:
            digest = "sha256:" + hashlib.file_digest(stream, "sha256").hexdigest()
        if asset.get("digest") != digest:
            raise PublishError(f"Missing or mismatched GitHub SHA256 digest: {path.name}")
        if asset.get("state") != "uploaded":
            raise PublishError(f"Source asset is not fully uploaded: {path.name}")
        paths.append(path)
    return paths


async def publish(
    session: aiohttp.ClientSession,
    *,
    repository: str,
    token: str,
    tag: str,
    commit: str,
    manifest: dict,
    directory: Path,
    api_url: str = "https://gitee.com/api/v5",
) -> int:
    """Verify the target tag, create one release and upload assets individually.

    ``api_url`` exists for local HTTP tests; the CLI always uses Gitee over HTTPS.
    No mutation is retried: an ambiguous failure needs remote inspection first.
    """
    paths = validate_release(manifest, directory, tag)
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise PublishError("Gitee repository must be owner/repo")
    if not token.strip():
        raise PublishError("Set GITEE_TOKEN to a Gitee token with repository access")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise PublishError("Expected the full source tag commit SHA")
    base = f"{api_url}/repos/{repository}"

    async def request(method: str, suffix: str, *, data=None, params=None, absent=False):
        # Gitee documents access_token as a query or form field. Never print
        # request URLs, response bodies or aiohttp exception text containing it.
        query = {"access_token": token, **(params or {})} if method == "GET" else None
        try:
            async with session.request(
                method, base + suffix, params=query, data=data, allow_redirects=False
            ) as response:
                if absent and response.status == 404:
                    return None
                if not 200 <= response.status < 300:
                    raise PublishError(f"Gitee {method} {suffix}: HTTP {response.status}")
                try:
                    return await response.json()
                except (ValueError, aiohttp.ContentTypeError):
                    raise PublishError("Gitee returned an invalid JSON response") from None
        except (aiohttp.ClientError, TimeoutError):
            raise PublishError(
                "Gitee connection failed or timed out; inspect the release"
            ) from None

    page = 1
    while True:
        tags = await request("GET", "/tags", params={"page": page, "per_page": 100})
        if not isinstance(tags, list) or any(not isinstance(item, dict) for item in tags):
            raise PublishError("Gitee returned an invalid tag list")
        match = next((item for item in tags if item.get("name") == tag), None)
        if match is not None:
            # Swagger describes commit as string; live Gitee tag responses also
            # use a commit object. Accept only a full SHA in either shape.
            target = match.get("commit")
            target_sha = target.get("sha") if isinstance(target, dict) else target
            if target_sha != commit:
                raise PublishError("Gitee tag commit differs from the source tag")
            break
        if len(tags) < 100:
            raise PublishError("Gitee tag is missing; push the source tag to Gitee first")
        page += 1

    existing = await request("GET", f"/releases/tags/{quote(tag, safe='')}", absent=True)
    if existing is not None:
        raise PublishError("Gitee release already exists; inspect it before uploading again")

    release = await request(
        "POST",
        "/releases",
        data={
            "access_token": token,
            "tag_name": tag,
            "target_commitish": commit,
            "name": manifest.get("name") or f"wom-api {tag}",
            "body": manifest.get("body") or f"wom-api {tag}",
            "prerelease": str(bool(manifest.get("prerelease"))).lower(),
        },
    )
    release_id = release.get("id") if isinstance(release, dict) else None
    if type(release_id) is not int or release_id <= 0:
        raise PublishError("Gitee did not return a valid release ID; inspect the release")
    print(f"Created Gitee release {release_id}; uploading {len(paths)} assets")
    for path in paths:
        with path.open("rb") as stream:
            form = aiohttp.FormData()
            form.add_field("access_token", token)
            form.add_field(
                "file", stream, filename=path.name, content_type="application/octet-stream"
            )
            asset = await request("POST", f"/releases/{release_id}/attach_files", data=form)
        if (
            not isinstance(asset, dict)
            or not asset.get("browser_download_url")
            or asset.get("name") != path.name
            or asset.get("size") != path.stat().st_size
        ):
            raise PublishError("Gitee did not confirm the upload; inspect the release")
        print(f"Uploaded {path.name}")
    print(f"Published https://gitee.com/{repository}/releases/tag/{tag}")
    return release_id


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="Gitee owner/repo")
    parser.add_argument("--tag", required=True)
    parser.add_argument("--commit", required=True, help="Full source tag commit SHA")
    parser.add_argument("--manifest", type=Path, required=True, help="GitHub Release API JSON")
    parser.add_argument("--dist", type=Path, default=Path("dist"))
    args = parser.parse_args()

    async def run() -> None:
        try:
            manifest = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
        except (OSError, ValueError):
            raise PublishError("Cannot read GitHub release manifest") from None
        if not isinstance(manifest, dict):
            raise PublishError("GitHub release manifest must be a JSON object")
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=180)) as session:
            await publish(
                session,
                repository=args.repo,
                token=os.environ.get("GITEE_TOKEN", ""),
                tag=args.tag,
                commit=args.commit,
                manifest=manifest,
                directory=args.dist,
            )

    try:
        asyncio.run(run())
    except PublishError as exc:
        print(f"Publishing failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None


if __name__ == "__main__":
    main()
