# 本机路径配置

`config/servers.local.json` 是被 Git 忽略的本机配置。它只登记各服务器已确认的路径，不会连接远端、挂载磁盘或同步详细结果；GitHub 阅读版不依赖此文件。

新机器可在本地创建该文件，按下面结构填写实际服务器别名与已获授权的路径。已有配置继续使用，不覆盖。原 `servers.example.json` 只在旧机器本地保留，新 clone 使用这里的示例。

```json
{
  "schema_version": 1,
  "current_server": "server-a",
  "servers": {
    "server-a": {
      "workspace_root": null,
      "dataset_root": null,
      "projects": {
        "Hyperbolic-Omnimodal": null,
        "meru-width-coco": null,
        "VAST27M-download": null
      }
    },
    "server-b": {
      "workspace_root": null,
      "dataset_root": null,
      "projects": {
        "Hyperbolic-Omnimodal": null,
        "meru-width-coco": null,
        "VAST27M-download": null
      }
    }
  }
}
```

`server-a` / `server-b` 是稳定别名；不能把另一台机器的未知位置照抄为当前路径。未确认的路径保留 `null`。不在此文件或公开文档中存放密码、Token、Cookie、私钥或代理认证信息。

详细结果访问方式见 [LOCAL_ARTIFACTS.md](../LOCAL_ARTIFACTS.md)，同步规则见 [SYNC.md](../SYNC.md)。
