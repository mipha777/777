| 模块                  | 功能                                     |
| ------------------- | -------------------------------------- |
| `main.py`           | 控制整个流程，调用登录 → 获取歌曲 → 获取评论              |
| `browser_cookie.py` | 用 Playwright 打开网易云音乐并登录，自动保存 cookie    |
| `encrypt.js`        | 复刻网易云音乐加密逻辑（如 `window.asrsea`）         |
| `crypto_api.py`     | 用 Python `execjs` 运行 JS，生成加密参数         |
| `music_api.py`      | 所有接口都通过它：排行榜、歌曲详情、评论接口等                |
| `comment_parser.py` | 处理分页评论，解析 JSON、判断是否有下一页                |
| `file_helper.py`    | 封装 `save_json()` / `load_json()` 等文件操作 |
| `songs.json`        | 存储排行榜歌曲（歌名、ID、歌手）                      |
| `comments/`         | 每首歌一个 JSON 评论数据文件，便于后续分析或建库            |


