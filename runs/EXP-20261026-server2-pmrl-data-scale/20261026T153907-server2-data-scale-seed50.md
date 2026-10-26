# PMRL 数据扩充配对实验：server2 / seed50

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261026-server2-pmrl-data-scale](../../experiments/EXP-20261026-server2-pmrl-data-scale.md) |
| run ID | 20261026T153907-server2-data-scale-seed50 |
| 服务器 | server2，114.214.255.126，UID1003 |
| 状态与核对时间 | 已完成2组训练及8项正式评测；最终结束20:01:32，结果核对2026-10-26 20:18，Asia/Shanghai |
| 源码 | 历史PMRL模型/评分，运维适配独立冻结；[源码清单](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/source/manifest.json)，当前SHA-256 `1df35143b7e055b502af156e679baa03649edc379edd9e4f465ee937d39d03d4`；旧版本另存source_versions |
| 含未提交改动 | 是；保留已有改动，不以HEAD冒充运行源码 |
| 数据 | 旧86,706；新105,369；原始冻结105,709；新增18,663全部校验通过，无新增解码排除；旧/新1354 / 1646个batch |
| 条件 | seed50、512维、四卡×16、每组一个DataLoader epoch、固定末轮、无下游微调 |
| GPU | server2 4–7；两组串行，启动前连续空闲检查 |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026` |
| 冻结记录 | [freeze.json](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/freeze.json) |
| 输入权限检查 | server2全量224,918个输入路径均可读；无需修改原媒体ACL；独立输出目录已配置两端UID权限并保留ACL备份 |
| 媒体校验 | 16:39:40完成；18,663/18,663通过；[完整校验报告](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/validation/media.json)及逐样本视频/音频哈希保留 |
| 实验控制器 | 历史PID2485961；运行状态记录为complete；[清单](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/controller-launch.json)；[完成状态](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/state.json) |
| 完成记录器 | 原server-a记录器日志报NFS `Stale file handle`，自动回填未完成；本次按用户要求手工归档，原故障日志和源码保持原样 |
| 正式结果 | [权威结果快照](../../results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/summary.md)；Top-50八方向均值+0.3635pp，direct −0.0957pp；单seed、主样本区间跨0 |

## 运行变更

- 15:39冻结数据。最初逐条复制链接的冻结进程614486已确认身份并停止；改用规范媒体目录与12条公共修复映射。原始媒体和历史清单未修改；本任务产生的废弃链接待精确清理。
- 实验记录仓库已fetch并快进至`bf965c8`，autostash自动恢复三份原有未提交文档改动；未提交或推送本次更改。
- 15:43新增媒体校验运行中。源级下载仍可继续，但本轮成员已固定；最终训练清单只按预先声明的解码校验剔除失败新增样本。
- 校验脚本两次修正：Decord数组长度改取实际帧轴；以减号开头的ID改为`--one=ID`传参。旧误判保存在`validation/invalid-probe-v1/`与`invalid-probe-v2-arguments/`，明确不进入排除结果；有效的已通过记录保留。修正版启动后核对2,098条、0条拒绝（仅当时快照）。
- 4项数据/预算/配对测试通过；复用恢复层的4项回归测试通过，包含真实双rank Gloo中断后样本、参数、优化器与连续训练完全一致。初次沙箱测试无法创建回环socket，已在允许回环通信的环境重跑通过；无需安装pytest。
- 15:55在server2 GPU4–7启动完整PMRL smoke，采用固定4个batch、在第2步完整保存后退出并续跑至第4步。此项通过且新增媒体校验完成后，控制器才会发布最终清单并执行正式两组训练与评测。
- 16:00首轮smoke完成4次有效更新、0 AMP跳步，但其他rank提前读取主rank完成文件导致退出码1。已归档旧源码`c0a1a98…`及完整失败证据；加入barrier和主rank检查后以新源码`1df35143…`重新从初始化验证。正式训练尚未使用旧源码。
- 16:12新版本smoke的保存、续跑、4rank状态和两次退出码均通过：从2恢复至4，累计4次有效更新、0跳步。16:20另完成64样本MSRVTT原生四卡评测，覆盖direct/Top-50、双向R@1/5/10及逐样本导出；退出码0。[实际GPU验证](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/validation/gpu_smoke.json)。这些数字是工程验收，不是正式检索结果。
- 控制器在仅CPU等待阶段重启以继承独立CUDA/Triton/扩展缓存路径；未重复已通过的smoke。大型缓存和全部checkpoint位于实验NFS目录。最初准备阶段创建的10,256个废弃链接已按[精确清单](/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/validation/abandoned-links-cleanup.json)清理，原始媒体未删除。
- 16:39完成全部新增媒体校验并发布正式协议；16:40进入旧组训练。两组均从官方VAST初始化，模型/评分/谱计算/优化器与历史项目逐字节相同，保存与恢复仅为运维适配。
- 16:51核对旧组269/1354个batch。首个100步完整恢复点已核对模型5,587,045,722字节、优化器9,943,844,257字节、四rank状态73,639字节及完成标记；当时100个batch对应99次有效更新、1次同步AMP跳步。后续按最近两份完整checkpoint保留策略轮换，不能把该进度当作完整epoch或检索结果。
- 完成记录器已启动，只有两组完整训练、8个正式评测任务均通过退出码/完成标记检查后，才复制精选结果、登记最终模型SHA-256并回填结论。64样本smoke及其指标不进入正式对比表。

## 完成核验与手工归档（2026-10-26 20:18，Asia/Shanghai）

用户要求将正式结果写入实验记录仓库。本次仅更新仓库文档和轻量结果快照，未重新运行实验或改写原始结果。远端状态已fetch核对，当前HEAD与origin/main一致；已有未提交改动保留，未commit或push。

| 条件 | batch数 | 有效更新 | AMP跳步 | 末轮checkpoint | 正式评测 |
|---|---:|---:|---:|---|---|
| 旧组86,706条 | 1354 | 1353 | 1 | `model_step_1354.pt` | 四数据集均退出码0 |
| 新组105,369条 | 1646 | 1646 | 0 | `model_step_1646.pt` | 四数据集均退出码0 |

两组初始化指纹一致；核对了两组训练与8项评测的完成标记、配置哈希和退出码。末轮模型、优化器和训练状态的大小与完成标记一致；本次文档归档未重新哈希大型模型/优化器，不能把大小检查说成完整载荷哈希校验。

48项指标已逐项与逐样本rank、原生评测日志及CSV对照；两个阶段的八方向等权均值重新计算一致。源结果JSON、CSV、Markdown及协议等按字节复制，快照SHA-256登记到总清单。64样本smoke没有纳入正式表格。

- [完成、配置、checkpoint与数值核验](../../results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/verification.json)
- [权威报告](../../results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/summary.md) · [完整JSON](../../results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/results.json) · [完整CSV](../../results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/results.csv)
- 自动回填失败仅影响记录同步，训练和评测均已完成；原`logs/recorder.log`中保留NFS错误证据。
