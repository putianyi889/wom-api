# Gitee release publishing investigation

Reviewed on 2026-10-14. The project already uses GitHub CLI for GitHub Releases
and aiohttp for HTTP. Gitee publishing reuses both, and mirrors the existing
wheel, sdist and documentation instead of rebuilding a released version.

## Existing solutions considered

- [trustedinster/sync-release-gitee v1.3](https://github.com/trustedinster/sync-release-gitee/tree/v1.3):
  the reviewed [sync_releases.py](https://github.com/trustedinster/sync-release-gitee/blob/v1.3/sync_releases.py)
  disables TLS verification (`verify=False` and a global unverified context).
  In `upload_release_assets`, the actual upload occurs after the file iteration,
  so a multi-file batch uploads only its final file. It also synchronizes all
  releases rather than the one version selected by this project.
- [nICEnnnnnnnLee/action-gitee-release v2.0.0](https://github.com/nICEnnnnnnnLee/action-gitee-release/tree/v2.0.0):
  its [publisher](https://github.com/nICEnnnnnnnLee/action-gitee-release/blob/v2.0.0/gitee_release.py)
  supports individual multipart uploads and retains default TLS verification.
  Its HTTP calls have no explicit timeout; the create path does not preflight
  tag commit identity or existing releases. Its retry decorator retries raised
  exceptions, while unsuccessful HTTP responses return `(False, message)`.
  Those HTTP failures therefore do not receive the advertised upload retries.

Neither reviewed version meets this project's selected-version and validation
requirements directly. `tools/publish_gitee.py` is a small adapter over the
existing aiohttp dependency; it adds no SDK, transport implementation or runtime
API to `wom_api`. GitHub downloads remain handled by the
[official GitHub CLI](https://cli.github.com/manual/gh_release_download).

## Official API evidence

The [Gitee API documentation](https://gitee.com/api/v5/swagger) serves Swagger
JSON at [doc_json](https://gitee.com/api/v5/doc_json). The downloaded document
version was `5.4.93`. The
[Gitee SDK reference](https://gitee.com/sdk/gitee5j/blob/main/docs/RepositoriesApi.md)
also describes release and attachment operations.

| Operation | Path below `https://gitee.com/api/v5` | Used fields |
| --- | --- | --- |
| List tags | `GET /repos/{owner}/{repo}/tags` | `access_token`, `page`, `per_page` |
| Find release | `GET /repos/{owner}/{repo}/releases/tags/{tag}` | `access_token` |
| Create release | `POST /repos/{owner}/{repo}/releases` | form fields `access_token`, `tag_name`, `name`, `body`, `target_commitish`, `prerelease` |
| Upload attachment | `POST /repos/{owner}/{repo}/releases/{release_id}/attach_files` | multipart fields `access_token`, `file` |

Create returns a Release object with integer `id`. Upload returns an AttachFile
object with `name`, `size` and `browser_download_url`. Requests retain TLS
verification and refuse redirects. GET uses the documented query authentication;
POST uses form authentication. Error output omits URLs, credentials and response
bodies. Only a 404 during release lookup means the release does not exist.

The official Tag schema declares `commit` as a string; a live anonymous request
to `putianyi889/wom-api/tags` returned a `commit` object with `sha` on this date.
Both representations are accepted and checked against a full source commit SHA.
The imported `v0.1.0` matched GitHub commit
`823c3b0c9c7f6477fafd3767a5ad037320cd48ee`.

## Validation limits

Local HTTP tests exercise real form encoding, all three uploads and failure
handling. Anonymous Gitee tag access succeeded for this repository. The
[live workflow](https://github.com/putianyi889/wom-api/actions/runs/38521685750)
created release ID `1204673` and uploaded all three `v0.1.0` assets. Anonymous
downloads with curl succeeded and all SHA256 digests matched GitHub. Installing
the downloaded wheel into a separate target directory with existing runtime
dependencies, then importing `wom_api` from that directory, confirmed `0.1.0`.

Direct pip installation from the Gitee wheel URL returned HTTP 403 both inside
and outside the sandbox, even though curl downloaded the same URL successfully.
The cause of that client-dependent response is unconfirmed. The documented
default is downloading the wheel first and installing the local file. Gitee
Git clone installation was not exercised. No quota or universal anonymous
download guarantee is inferred from these API schemas.
See the [publishing guide](../../publishing-gitee.md) for operational steps.
