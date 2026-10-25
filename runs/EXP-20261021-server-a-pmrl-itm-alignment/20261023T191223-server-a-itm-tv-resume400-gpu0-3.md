# GPU0–3：仅续跑TV / seed50

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261023T191223-server-a-itm-tv-resume400-gpu0-3 |
| 服务器 | server-a |
| 状态与核对时间 | 等待容量；2026-10-23 19:15，Asia/Shanghai；尚未启动GPU训练 |
| 控制器开始时间 | 2026-10-23 19:12:23 +08:00 |
| PID | 等待控制器627326；尚无新torchrun PID或端口 |
| 本次范围 | 仅TV/seed50续训与该组开发集评测，完成后退出；不启动其他方法或追加种子 |
| 恢复点 | step400；旧训练最远472/1354个batch，400步完整checkpoint与四rank状态保留 |
| GPU | 物理0,1,2,3 |
| batch与保存 | 每卡16、全局64；每100batch及末轮保存，保留最近两份 |
| 显存策略 | 原TV allocator上限29GiB不变，额外预留8GiB，要求每卡至少37GiB空闲并通过三次稳定检查 |
| 等待策略 | 用户明确选择等待GPU0–3释放；同时等本次已观察到的大显存进程退出，PID+启动时间核验；最多12小时，不向占用进程发信号 |
| 源码 | 基底a230347a，含未提交实现；实际冻结源码`e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`，没有修改训练数学或恢复合同 |
| 单组调度 SHA-256 | `6e9322d140f3e24fba428a05a1b4ec2b9e9f70d7086c97dff61f9631e64d2c3d` |
| 数据版本 | 86,706条过滤清单不变；继续使用已验证的md6F6VbYjeE.7媒体修复副本 |
| 启动清单 | [命令与资源](../../../PMRL-ITM/artifacts/launches/20261023T191223-server-a-itm-tv-resume400-gpu0-3.json) |
| 调度日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261023T191223-server-a-itm-tv-resume400-gpu0-3.log) |
| 输出根目录 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 当前状态文件 | `single_job_resume_state.json`；旧serial/parallel状态均属于历史队列 |
| 正式结果 | 尚未恢复GPU训练，无新增更新或评测指标 |

## 本次启动核查

最初检查GPU0–3占用约9–10GiB/卡；启动前复查时，另一组进程由约1.3GiB/卡增长至约24GiB/卡，使总占用升至约32–34GiB/卡。容量检查阻止了立即启动，未创建新的训练进程，也未修改旧checkpoint或归档旧attempt。用户随后明确选择等待容量释放。

为避免只看到对方任务初始化阶段的低显存就启动，新等待入口除检查空闲显存外，还等待本次已观察到的大显存进程结束；只读取PID与启动时间作身份核对，不终止或查看这些进程的配置。等待CPU控制器不分配GPU训练内存。

本次选择TV原29GiB上限配置，未复用前次基线40GiB配置。增加的预留仅改变启动准入，不改变模型、batch、学习率、数据或checkpoint。恢复配置、源码和训练清单与400步保存的合同一致。已有媒体修复验证及checkpoint恢复验证沿用；本次新增单组入口的语法及阻塞进程身份识别检查通过。不能将等待队列启动称为训练已经恢复。

## 运行变更

- 19:12:23：建立仅TV/seed50的等待控制器627326。
- 19:15：状态waiting_for_capacity；等待进程418849、418851、418852、418853结束及显存稳定达标，尚无新GPU训练。
- 旧21:30串行控制器曾于10-22 23:33恢复基线，23:39发生CUDA OOM后退出；本次不是该旧队列仍在等待。
- 编辑前fetch成功，保留其他README/OPS-001改动，未提交或推送。
