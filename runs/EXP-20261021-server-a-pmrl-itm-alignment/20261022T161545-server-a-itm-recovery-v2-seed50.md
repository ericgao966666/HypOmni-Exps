# 周期性 checkpoint 与恢复 v2：保持现有训练，升级后续队列

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM 评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261022T161545-server-a-itm-recovery-v2-seed50 |
| 服务器 | server-a |
| 状态与核对时间 | 已接管后续队列；2026-10-22 16:19，Asia/Shanghai；继承基线610/1354个batch、TV 527/1354个batch，训练进程未重启 |
| 开始 / 交接 | 16:15:45新控制器启动；16:15:59完成交接 |
| 基底 / 未提交改动 | PMRL-ITM，a230347a；实现未提交，运行以冻结源码为准 |
| 后续组源码 SHA-256 | `731c3aba4b93709ae2c02c7e92c2439db596510f23222de4d00f9c047acba4a4` |
| 继承训练源码 | `51553a812eeed9db9ae8b584541f0c229041e96701077afcecbc3fc8971c353d`；baseline/TV seed50仍为v1 |
| 新调度 SHA-256 | `dac783c145f3a39cd0fc1a546959d72b405357977279c4d99f88cad1293a1bb0` |
| 训练协议 | 冻结VAST 86,707条，严格TVA；每卡16，全局64，一个epoch=1354个batch；模型/损失/评分/数据未改 |
| 恢复策略 | 后续训练每100个batch及末轮保存，保留最近2份完整checkpoint；原命令追加`--resume-failed`恢复，默认不无限自动重试 |
| checkpoint落盘 | 工作区本地`PMRL-ITM/artifacts/checkpoints/<根路径哈希>/<job>/`；NFS输出的ckpt软链接指向此处；不自动跨机归档 |
| PID / GPU | 新控制器502092；原控制器91859已退出；保留torchrun114052（4–7）和114057（0–3），各自进程启动时间未变 |
| 后续分组 | 4–7：mean_tv_ta；0–3：sigma_max；条件触发的42/123复验也使用v2 |
| 启动清单 | [命令、进程与继承关系](../../../PMRL-ITM/artifacts/launches/20261022T161545-server-a-itm-recovery-v2-seed50.json) |
| 调度日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261022T161545-server-a-itm-recovery-v2-seed50.log) |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T161545-server-a-itm-recovery-v2-seed50` |
| 验证证据 | [测试清单与日志哈希](../../../PMRL-ITM/artifacts/checkpoint_recovery_verification.json) |
| 正式结果 | 尚无完成epoch或检索结果；恢复测试不代表方法收益 |

## 保留进度与版本边界

用户要求优先实现周期性保存，不继续投入大量精力定位随机解码超时。此次只替换上层控制器：验证父子PID、启动时间、命令、SIGTERM默认行为和独立session后，终止旧控制器；未向训练进程发送信号。新控制器等待两组现有训练完成，并用完成标记、完整checkpoint和四rank结束记录核实结果。旧训练目录和源码保持原样，完成后在新输出建立引用。

已运行的基线/TV使用加载后的v1源码，**仍然只有epoch末保存**，无法通过改磁盘代码给进程热加保存。后续组使用新快照；升级仅涉及pipeline、checkpoint读写和调度/worker配置，模型、数据、评分源码哈希与原版本相同。沿用原smoke和温度校准，新增恢复功能单独验证。中途checkpoint只作故障恢复，正式选模依然是epoch末模型。

## 恢复语义与验证

保存模型、优化器、AMP scaler、每个rank的Python/NumPy/Torch/CUDA随机状态、数据位置与累计有效更新/AMP跳步。恢复核对源码、配置、训练清单和加载器结构。完整标记最后提交；保存失败不清理上一份，截断文件不会作为最新可恢复checkpoint。

恢复重建相同种子的DataLoader并重读已消费数据前缀，不重复模型更新；在预取下一批前恢复主进程随机状态。因此可能仍有CPU/媒体重读等待，但无需重新训练整个epoch。旧日志和计数归档到各job的attempts目录，保留失败证据。

实际验证：25项ITM测试、1项原pipeline回归、4项双队列调度测试通过。真实双GPU（物理4、5）NCCL与AMP小模型，第5步中断，从第3步恢复到第8步，最终参数、优化器和样本与连续训练一致；测试使用512MiB allocator上限/进程，已结束并清理测试进程与临时数据。测试覆盖半写入、截断、保留两份、输入变化拒绝恢复及PID重叠保护。尚未验证完整PMRL模型100步时的大checkpoint写入耗时，不能把小模型验证冒充正式训练完成。

## 运行变更

- 16:15:59：旧控制器91859退出，两个原torchrun独立session保持运行；新控制器502092接管。
- 16:19：核实两个原torchrun PID和启动时间未变，基线610、TV527个batch；后续v2队列等待现有组完成。
- 编辑前fetch成功，HEAD与origin/main一致；保留已有OPS-001等改动，未提交或推送。

- 后续状态：旧基线16:40:14在batch858超时失败；旧TV也在同位置停顿并按用户授权停止，未完成任何epoch，旧组没有可恢复checkpoint。本控制器已退出；已转入[过滤清单后的全组重启](20261022T170008-server-a-itm-filtered-recovery-seed50.md)。
