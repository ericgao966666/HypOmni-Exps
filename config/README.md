# 本机配置

`servers.example.json` 是可同步模板，`servers.local.json` 是被 Git 忽略的本机配置。当前机器登记为 `server-a`；另一台为 `server-b`，具体路径尚未确认，保持 null。

另一台服务器 clone 后，若本机配置尚不存在，复制模板：

```bash
cp -n config/servers.example.json config/servers.local.json
```

将 `current_server` 改为实际别名，填写实际存在且已获授权的工作区和项目路径。不要复用本机路径作为远端已确认路径，不在配置中存放密码、Token、Cookie、私钥或代理认证信息。

该配置是路径登记表，不会自动连接服务器、挂载存储或改写链接。内部结果快照不依赖这些路径；查看原始日志和模型才需要对应服务器的数据。
