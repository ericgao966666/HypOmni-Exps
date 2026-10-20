# 两台服务器同步

本仓库独立维护实验记录，默认分支为 `main`。日志同步不要求切换实验代码仓库分支。

## 当前状态

2026-10-20 已初始化本地 Git 仓库并配置同步选项。用户指定远端为 `https://github.com/ericgao966666/HypOmni-Exps.git`，同步分支为 `main`。首次检查时仓库为公开状态，后续可见性以 GitHub 设置为准。上传与同步状态以本地分支状态和远端提交记录为准。

## 每台服务器的本地设置

在本仓库根目录运行以下命令。它们只修改当前仓库 `.git/config`；这些设置不会通过 clone 自动继承，需要每台服务器各配置一次。

```bash
git config --local pull.ff only
git config --local push.default simple
git config --local fetch.prune true
git config --local core.autocrlf false
git config --local user.useConfigOnly true
```

当前源服务器的本仓库提交署名为 `ericgao966666 / ericgao96.cn@gmail.com`，与本次同步使用的 GitHub 连接账号一致，仅设置在本仓库。Git 提交署名与 GitHub 登录授权分别管理：前者记录提交作者，后者决定远端读写权限，更换连接账号不会自动修改本地署名。

另一台服务器首次提交前配置自己的姓名和邮箱，仅使用 `git config --local user.name` / `git config --local user.email`。`user.useConfigOnly` 防止 Git 自动猜测身份，但不会屏蔽已有全局身份，所以仍需设置本地值。仓库级 Git 配置不会随 clone 同步。

从 [servers.example.json](config/servers.example.json) 创建忽略的本机路径配置，见[配置说明](config/README.md)。当前机器记为 server-a，目标机器记为 server-b；首次落地后固定别名。

## 另一台服务器接入

首次上传已完成。在另一台服务器获授权的工作区根目录执行：

```bash
git clone https://github.com/ericgao966666/HypOmni-Exps.git
cd HypOmni-Exps
```

公开仓库允许匿名读取；提交推送需要该仓库的写入权限及本机授权的认证方式。不要借用共享账号中其他人的凭据，也不要把本机配置或认证材料加入提交。

完成上述本地配置即可查看总览与结果快照。把以下约定加入该机器适用的工作区规则：实验工作开始前读取 `HypOmni-Exps/README.md`，更新实验时遵守日志仓库的 `AGENTS.md`。仓库内部规则不会自动作用于其外部的代码仓库。

## 日常协作

1. 更新前看 `git status`，在工作区干净时执行 `git pull --ff-only`。已有未提交改动时先检查并保留，不自动 reset、stash 或清理。
2. 新增本服务器的唯一 run 记录，再更新关联实验卡与总览。精简结果按日期或明确版本放在 `results/`，注明来源与哈希。
3. 获得提交授权后，明确列出要加入的文件，检查暂存差异，再 commit 和 push。Agent 不因为本流程存在就获得上传授权。
4. 若拉取或推送提示分叉，停止自动同步，检查双方变更并合并。不得强推覆盖另一台机器记录。多人同时改同一卡片时，可使用短期分支审阅合并。

## 文件范围

| 同步到日志仓库 | 留在原项目或本机 |
|---|---|
| 实验卡、周报、模板、仓库内维护规则 | `.git/config` 与本机路径配置 |
| 精简指标 CSV/JSON、精选分析图 | checkpoint、数据集、特征缓存 |
| 来源清单、代码 commit 或源码快照标识 | 完整日志、源码大包、凭据 |

首批主要结果已经复制为仓库内相对链接。剩余 `../../Hyperbolic-Omnimodal/` 等链接用于源项目协议和原始产物，仅在相应目录存在时可打开。Markdown/JSON 中记载的源路径不会通过 Git 自动同步其指向的文件。

这里没有后台监控、自动提交、自动拉取或自动推送服务。
