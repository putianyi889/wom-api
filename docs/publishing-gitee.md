# Gitee 发布

Gitee 仓库为 [putianyi889/wom-api](https://gitee.com/putianyi889/wom-api)。
**Publish Gitee Release** 工作流将选定 GitHub Release 的 wheel、源码包和 HTML
文档 ZIP 上传到 Gitee；直接使用原始附件，并核对 GitHub 提供的 SHA256。
当前 GitHub 的 `v0.1.0` 可以通过此流程发布，不需要重新构建或移动已有标签。

## 首次配置

1. 将 [GitHub 仓库](https://github.com/putianyi889/wom-api) 导入 Gitee，或创建
   空仓库后推送代码和发布标签。Gitee 标签必须指向与 GitHub 相同的提交。
2. 在 Gitee 的[私人令牌设置](https://gitee.com/personal_access_tokens)创建令牌，
   授予仓库 API 访问权限（`projects`），令牌所属用户也需有目标仓库的发布权限。
3. 在 [GitHub Actions Secrets 设置](https://github.com/putianyi889/wom-api/settings/secrets/actions)
   添加仓库 Secret，名称为 `GITEE_TOKEN`，值为 Gitee 令牌。
4. 将新增的工作流提交并推送到 GitHub 默认分支 `main`。

令牌只放在 Secret 或本地环境变量中，不放进 Git remote URL、发布参数或源码。
GitHub 内置的 `GITHUB_TOKEN` 用于读取 GitHub 附件，不能替代 Gitee 令牌。

## 发布现有版本

在 GitHub Actions 中选择 **Publish Gitee Release**，点击 **Run workflow**：

| 参数 | 当前版本的值 | 含义 |
| --- | --- | --- |
| `tag` | `v0.1.0` | 已发布的 GitHub Release 标签 |
| `repository` | `putianyi889/wom-api` | Gitee 仓库，已作为默认值 |

也可以使用已登录的 GitHub CLI：

```sh
gh workflow run publish-gitee.yml --ref main -f tag=v0.1.0 -f repository=putianyi889/wom-api
```

工作流先确认令牌已配置，下载 GitHub 发行版元数据和三个原始附件，再检查附件名称、
大小、SHA256、源发行版是否公开发布，以及 Gitee 标签的提交是否一致。全部检查通过后，
创建 Gitee Release 并逐个上传三个附件，保留源发行版标题、说明和预发布标记。
工作流读取当前工作流所在提交中的发布工具，因此可以同步早于该工具的旧版本。

普通 push、tag push 和 GitHub Release 创建不会自动运行此工作流。GitHub 发布流程
继续独立使用。Gitee 发布流程只创建发行版和上传附件，代码与标签由 Git 同步：

```sh
# 首次添加；OWNER 替换为实际 Gitee 用户名或组织路径。
git remote add gitee https://gitee.com/OWNER/wom-api.git
git push gitee main
git push gitee v0.1.0
```

如果已经添加 `gitee` remote，直接执行 push。无需强制推送或镜像覆盖目标仓库。
后续版本先按开发指南发布 GitHub Release，再推送对应 Gitee 标签并手动同步发行版。

## 本地发布

安装项目后，使用 GitHub CLI 准备元数据和附件。以下命令用于 PowerShell，
发布令牌应提前通过本地环境变量 `GITEE_TOKEN` 配置：

```powershell
# 使用新的空目录，避免混入其他版本的文件。
gh api repos/putianyi889/wom-api/releases/tags/v0.1.0 | Set-Content -Encoding UTF8 release.json
gh release download v0.1.0 --repo putianyi889/wom-api --dir gitee-dist
$releaseCommit = git rev-parse 'v0.1.0^{commit}'
python tools/publish_gitee.py --repo putianyi889/wom-api --tag v0.1.0 --commit $releaseCommit --manifest release.json --dist gitee-dist
```

这里显式使用 UTF-8，避免 PowerShell 5.1 默认重定向产生 UTF-16 文件。
发布工具也支持带 BOM 的 UTF-8 文件。

## 安装

`v0.1.0` 已发布到 [Gitee 发行版页面](https://gitee.com/putianyi889/wom-api/releases/tag/v0.1.0)。
推荐从页面下载 wheel 后安装：

```sh
python -m pip install ./wom_api-0.1.0-py3-none-any.whl
```

2026-10-14 的验证中，三个附件均可匿名下载，SHA256 与 GitHub 原始附件完全一致；
下载后的 wheel 可安装并导入 `wom_api`。但 pip 直接访问同一 Gitee wheel URL 返回
HTTP 403，在沙箱外复核也相同。不要将直接 URL 安装作为已验证的默认方案。
需要在 `requirements.txt` 中引用在线 wheel 时，目前可使用已验证的 GitHub URL。

Gitee 的附件下载链接由服务端返回。本版本的地址为：

```text
https://gitee.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl
```

其他版本请从发行版页面复制实际地址。
也可以使用已经同步的 Git 标签（要求本机安装 Git）：

```sh
python -m pip install "wom-api @ git+https://gitee.com/putianyi889/wom-api.git@v0.1.0"
```

依赖仍从 pip 配置的包源安装。Git 标签安装命令给出了可用语法，本次没有执行
Gitee Git 克隆安装；私有仓库或 Gitee 的访问限制可能要求登录。

## 失败处理和验证范围

已有同名 Gitee Release 会使流程失败，避免覆盖已发布版本。HTTP 错误、无效响应、
重定向、连接失败和超时也会使流程失败，不输出令牌、完整请求 URL 或响应正文。
每个请求有 180 秒超时，整个工作流有 15 分钟上限。

Gitee 创建发行版与上传附件不是原子操作。上传失败可能留下包含部分附件的发行版，
工作流不会自动删除或重试。先检查 Gitee 页面；补齐附件可使用页面操作。如果决定
删除这个未完成的发行版后重新运行，应保留版本标签并确认删除的是未完成的发布。

自动测试使用本地 aiohttp HTTP 服务，覆盖三个附件的 multipart 上传、标签分页、
提交一致性、文件校验、认证错误、失败停止和凭据不跟随重定向。
`v0.1.0` 的真实上传已通过 [发布工作流](https://github.com/putianyi889/wom-api/actions/runs/38521685750)
完成，三个公开附件的下载与校验、下载后 wheel 的安装与导入均已通过；直接 URL
安装的限制见上文。方案比较和 API 依据见[调查报告](research/gitee/README.md)。
