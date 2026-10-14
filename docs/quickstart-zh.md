# 中文入门

`wom-api` 是 minesweeper.online 的非官方异步 Python 数据客户端，要求 Python 3.11+。
包通过 GitHub Releases 分发。发布后可以直接安装 wheel，并选择需要的版本：

```sh
python -m pip install "https://github.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl"
```

也可以安装固定的 Git 标签，这种方式需要本机安装 Git：

```sh
python -m pip install "wom-api @ git+https://github.com/putianyi889/wom-api.git@v0.1.0"
```

应用项目的 `requirements.txt` 可以直接引用发布文件：

```text
wom-api @ https://github.com/putianyi889/wom-api/releases/download/v0.1.0/wom_api-0.1.0-py3-none-any.whl
```

以上地址在对应标签或 Release 发布后可用。该包从 GitHub 下载，其依赖仍由 pip
从配置的包源安装。建议固定版本 URL 或完整 commit hash，以便复现安装。
在本地仓库内开发时，执行 `python -m pip install -e .`。

Gitee 镜像仓库也支持固定 Git 标签安装：

```sh
python -m pip install "wom-api @ git+https://gitee.com/putianyi889/wom-api.git@v0.1.0"
```

Gitee Release 发布后，可从发行版页面复制 wheel 附件地址直接安装。
配置、发布和验证步骤见 [Gitee 发布指南](publishing-gitee.md)。

```python
import asyncio
from wom_api import WomClient


async def main():
    async with WomClient() as client:
        profile = await client.get_user_info(userId=1)
        print(profile["user"])
        results = await client.search_user(query="玩家昵称", isFinal=False)
        print(results["result"])


asyncio.run(main())
```

不传 session 时自动建立匿名会话。需要自己的账户数据时，传入浏览器中该站点的
`localStorage['_session']`：`WomClient(session=...)`。这是账户凭据，请自行保管。
库不会读取浏览器，也不会把 session 写入磁盘；可以通过 `client.session` 自行保存并复用。

当前前端版本的 236 个 WebSocket 请求类均有 Python 方法。参数保留网站原有的
camelCase 名称，可以用关键字参数或字典传入。返回值保持原始 JSON 结构；时间戳、
空值和未解析字段不会被擅自转换。`payload`、`server`、`timeout` 是方法保留参数，
同名网站字段需要放在字典中。

完整的[入口清单](endpoints.md)记录每个 controller 的方法名、服务器角色、已观察的
请求字段和响应字段；字段清单并不是完整的服务器校验规则。账户接口和管理员接口
仍然需要相应权限。研究范围、版本证据及验证限制见[调查报告](research/README.md)。

入口清单也包含 **Request / Response 字段类型表**，使用 Python 类型写法。例如
`get_user_info` 的请求字段 `userId` 为 `int`；返回值中 `user.id` 为 `int`、
`user.country` 为 `str`、`user.username` 已观察到 `str | None`。嵌套数组字段使用
`result[].id` 这样的路径。

类型表的 `Evidence` 列注明来源：`frontend syntax` 来自前端字面量或显式类型转换，
`live sample` 来自成功的公开请求/响应样本，`unresolved` 表示尚不能确定具体类型，
以 `JsonValue` 表示。类型不是完整的服务器约束；只观察到 `None` 也不代表只允许空值，
更不代表字段可以省略。日期字符串保留为 `str`。

获取棋盘和回放时使用 `await client.get_game(game_id)`。该方法会先订阅
`InitGameEvent`，再发送 `EnterGameWS`，返回匹配游戏的完整事件参数列表：首项为
游戏元数据，后续项包含棋盘、操作历史等。只调用 `enter_game()` 可能只收到空确认。

排行榜等分页接口使用 `url`、`dataType`、`params`、`limit`、`offset` 作为外层参数。
`dataType=1` 请求总数，`2` 请求当前玩家名次，`3` 请求数据行。实际例子见
[Quick start](quickstart.md) 和 [examples/public_data.py](../examples/public_data.py)。

连接在首次请求时自动建立。可以调用 `connect()` 提前连接，使用 `subscribe()`
订阅推送，用异步上下文管理器释放所有连接。主服务器和提示服务器按用户 ID 分片；
游戏服务器须通过 `server=` 明确指定。库不会自动重发已经发送的请求。

文档采用 Sphinx + MyST Markdown + Furo，入口清单与 Python 方法由同一份经过审核的
元数据生成。开发和发布命令见[开发指南](development.md)。
