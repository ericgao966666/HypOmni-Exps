# 总结文档同步

本仓库维护 `main`，远端为 [ericgao966666/HypOmni-Exps](https://github.com/ericgao966666/HypOmni-Exps)。自 2026-11-05 起，当前版本只同步总结性 Markdown 和 `.gitignore`、`.gitattributes`、`.editorconfig` 三个必要配置文件。

## 同步内容

| 同步到 GitHub | 保留在本地 |
|---|---|
| 总览、实验主卡、研究协议、关键对比表和周报 | 原始 CSV / JSON / JSONL、逐轮与逐样本结果 |
| `summaries/` 中筛选后的 Markdown 报告 | `results/` 中的原始报告、图件、核验清单 |
| 模板、维护规则和本地文件访问说明 | `runs/` 下的实际运行记录、运维历史 |
| 报告的原文相对路径与 SHA-256 | 模型、数据集、特征、日志、凭据、本机配置 |

`results/README.md` 和 `runs/README.md` 只说明本地材料的用途。`.gitignore` 默认忽略文件，只明确允许已审核的文档路径；文件扩展名是 Markdown 并不自动获得上传资格。新增报告需检查内容并加入允许清单，不使用 `git add -f` 绕过规则。

详细位置、原文与阅读版的关系见 [LOCAL_ARTIFACTS.md](LOCAL_ARTIFACTS.md)。现有 Git 历史保留，旧提交中的详细数据仍可访问；本次不是历史清理。

## 另一台已有服务器第一次更新

本次提交将从 Git 索引移除大量文件。当前整理机器使用 `git rm --cached` 保留了工作区文件，但另一台机器普通快进拉取时，Git 会删除那里仍被跟踪的对应文件。必须先备份，不能直接 pull。

1. 在该机器已授权的个人工作区内确认仓库真实路径，检查 `git status --short --branch`。保留所有未提交工作和未跟踪结果；有改动或分叉时先核对合并方案，不自动 reset、clean 或覆盖。
2. 执行 `git fetch origin`，只更新远端引用。用 `git diff --name-only --diff-filter=D --no-renames HEAD..origin/main` 列出本次将删除的跟踪路径；此时本地原文件尚未被删除。
3. 将这些文件连同本地独有结果备份到该机器已授权的独立目录，保留路径结构并记录、复核 SHA-256。不要仅依赖另一台服务器上的备份；不要上传备份。
4. 确认可快进且不会覆盖本地工作后，执行 `git merge --ff-only origin/main`。然后从本机备份将被移除的详细文件恢复到原位置，**仅恢复缺失的本地材料，不覆盖已存在文件或新的总结文档**。
5. 复核恢复文件的 SHA-256，并用 `git check-ignore -- <文件>` 确认它们已被忽略；保留备份，检查 `git status --short --branch`。不要重新 add 详细结果。

上述步骤需在每台服务器各自执行。本次 GitHub 发布不会自动替其他服务器备份、拉取或恢复数据。

## 新机器接入

在已授权的工作区执行：

```bash
git clone https://github.com/ericgao966666/HypOmni-Exps.git
cd HypOmni-Exps
```

新 clone 的当前文件树只有总结文档，没有本地详细材料。具体路径配置见 [config/README.md](config/README.md)。如需跨服务器取得详细材料，必须另行确认来源、目标和传输范围。

每台机器的 Git 设置只放在仓库级配置：

```bash
git config --local pull.ff only
git config --local push.default simple
git config --local fetch.prune true
git config --local core.autocrlf false
git config --local user.useConfigOnly true
```

提交前另行设置本仓库的 `user.name` 和 `user.email`；不修改共享账号的全局身份，不借用共享凭据。Git 提交身份与 GitHub 登录权限分别管理。

## 日常更新与发布

1. 开始修改前检查 Git 状态并 fetch；无本地改动且可快进时先同步。获取失败应明确说明远端状态未核实。
2. 原始输出和 run 记录留在本地。将关键数字、对照协议、负结果与局限写入实验主卡；需要报告时在 `summaries/` 创建阅读版，注明原文位置、SHA-256 和真实实验核对时间。
3. 更新总览与报告索引，只给发布文档建立可点击相对链接。数据和图件使用带“本地”说明的代码格式路径，不嵌入线上缺失图片。
4. 获授权后只暂存确认过的文档和允许清单改动。检查暂存文件类型、链接、结果数字和本地证据完整性；不盲目 `git add .`。
5. 发布前再次 fetch 并比对远端，合并其他服务器的新工作；不强推。使用 GitHub API 时，以核实的头提交作为 `expected_sha` 并发检查。
6. 发布后核对 GitHub 头提交、本地分支和剩余改动。只读咨询不触发提交或同步；这里没有自动提交、推送或后台监控服务。
