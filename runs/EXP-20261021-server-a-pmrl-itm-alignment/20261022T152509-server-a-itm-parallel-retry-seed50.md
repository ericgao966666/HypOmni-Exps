# 四卡双队列：基线重试与 TV 新增组

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM 评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261022T152509-server-a-itm-parallel-retry-seed50 |
| 服务器 | server-a |
| 状态与核对时间 | 两组正式训练运行中；2026-10-22 15:36，Asia/Shanghai；基线与TV均已14/1,354次有效更新，AMP跳步0，无OOM |
| 代码仓库 / 基底 | PMRL-ITM；a230347a；包含未提交实现 |
| 实际训练源码 | `51553a812eeed9db9ae8b584541f0c229041e96701077afcecbc3fc8971c353d`；新输出下source目录 |
| 调度脚本 SHA-256 | `8c309a7ddd79ad29a3cfe6188f5e8db21cf9ea5ccc4412a3e839fb1d2f027b23` |
| 数据与协议 | VAST accepted 86,707条；严格TVA，沿用冻结manifest；每卡16，全局64，一epoch=1,354个batch；seed50先行 |
| 两条队列 | GPU4–7：legacy_va→mean_tv_ta；GPU0–3：tv→sigma_max；固定归属，避免重复训练 |
| 显存与加载 | cudaMallocAsync；4–7上限40GiB，0–3上限29GiB；启动门槛额外预留2GiB；关闭autocast权重缓存；DataLoader timeout 120→600秒 |
| PID / 端口 | 调度91859；基线torchrun114052、端口43163；TV torchrun114057、端口53681；各rank详见job日志 |
| 启动清单 | [命令、环境和资源](../../../PMRL-ITM/artifacts/launches/20261022T152509-server-a-itm-parallel-retry-seed50.json) |
| 调度日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261022T152509-server-a-itm-parallel-retry-seed50.log) |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T152509-server-a-itm-parallel-retry-seed50` |
| 正式结果 | 尚无完成epoch、checkpoint或检索结果 |

## 前序失败与重试依据

[前序运行](20261022T134902-server-a-itm-four-gpu-seed50.md)在15:18:34发生rank3 DataLoader 120秒超时，最后858个batch，857次有效更新和1次AMP跳步，无中途checkpoint。原接管脚本在进程身份检查处退出，未发送停止信号。此次使用新目录，从相同初始化权重重跑完整epoch；原失败证据保留。

检查rank3的采样偏移13712–13775共64个候选样本，每个检查8个视频位置与音频加载。第一轮90秒总预算检查到偏移13757时结束，第二轮覆盖剩余19个并通过，单个最大3.97秒；这是局部诊断，没有重现训练随机帧/完整DataLoader时序，不能据此排除解码挂起或确认NFS为根因。日志在项目 `artifacts/launches/timeout-batch-probe*.log`。

复用前序四种四卡smoke和2,048条样本温度校准，启动时核对源码、batch与完成状态。冻结训练源码、初始化、数据和学习超参数不变；DataLoader等待上限统一改为600秒，是运行容错调整，尚未证明根因已解决。0–3上的其他进程占用上升，最终采用已通过单卡batch16容量探针的29GiB上限；15:36已通过两组各14次有效更新的实际运行检查，当前无OOM；不能据此保证全epoch不会再遇到读取问题。

## 选择规则与验证

采样训练不依赖候选评分C*，允许并行；所有seed50开发集结果齐备后才按原规则锁定C*、融合权重与复验组，再运行测试和必要的42/123种子。两队列各自唯一拥有对应采样组；一条失败后不再启动新任务，另一条已运行任务允许完成以保留进度。

双队列调度测试4项通过：PID身份、完整epoch/四rank/checkpoint证据、固定归属及开发集选择顺序、超时调整保持batch/优化器不变。没有新增训练收益结论；最终结果仍需完整epoch与评测。编辑前已fetch，HEAD与origin/main一致，未提交或推送。

## 实际启动核实

- 15:25:09启动调度后，初始化校验和快照复制受NFS延迟影响；进程曾处于NFS RPC等待，写入持续推进，15:30完成快照。存储延迟是可见现象，不足以确定前序超时根因。
- 15:32两条队列通过连续显存检查后启动torchrun；15:34开始正式训练。
- 15:36核实基线与TV各14个batch、14次有效optimizer更新、0次AMP跳步；两者epoch_budget均为world_size=4、global_batch=64、batches=1354、smoke=false。两者日志无OOM或Python traceback。
- GPU0–3总显存占用41,647–43,107 MiB / 49,140 MiB，含其他任务，最少约5.9GiB剩余；GPU4–7占用33,057–33,633 MiB。allocator预算不等同于含CUDA/NCCL的总物理占用。
- 前序失败记录、训练源码快照、温度与数据版本保留。当前尚无末轮checkpoint或正式检索指标；任务继续后台运行，无需用户进一步操作。

- 16:15:59：仅上层控制器91859交接给502092，原torchrun114052/114057未中断。后续队列由[恢复v2运行记录](20261022T161545-server-a-itm-recovery-v2-seed50.md)维护；当前两组继续旧源码，仍无中途checkpoint。16:19核实基线610、TV527个batch。
