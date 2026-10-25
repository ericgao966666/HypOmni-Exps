# GPU 4–7 四卡启动

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM 评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261022T134902-server-a-itm-four-gpu-seed50 |
| 服务器 | server-a |
| 状态与核对时间 | 已失败；2026-10-22 15:21，Asia/Shanghai 核实；15:18:34 rank3 DataLoader 120秒超时，退出码1；最后858个batch、857次有效更新、1次AMP跳步 |
| 开始时间 | 2026-10-22 13:49:02 +08:00 |
| 代码与未提交改动 | PMRL-ITM，基底 a230347a；有未提交改动，运行以快照为准 |
| 实际源码 | `source/51553a812eeed9db9ae8b584541f0c229041e96701077afcecbc3fc8971c353d/`，SHA-256 为快照文件哈希映射的聚合值 |
| 调度脚本 SHA-256 | `4af6172bba5dea06af50606b3195df0a9a59605603923aed6439adc1558e86b2` |
| 数据与训练协议 | 冻结 VAST 86,707 条；严格 TVA；四卡 × 16，全局 batch 64；每组一 epoch；先 seed 50，开发集规则决定复验 |
| GPU 与显存策略 | 物理 4,5,6,7；启动前全部空闲，每卡 15 MiB；allocator 上限 40 GiB，另留至少 2 GiB 空闲门槛；关闭 autocast 权重缓存，使用 cudaMallocAsync |
| PID / 端口 | 调度 PID 217291；当前 torchrun PID252945、rank0 PID252991、端口52571；各子任务详见 job.json |
| 启动清单 | [完整命令与资源记录](../../../PMRL-ITM/artifacts/launches/20261022T134902-server-a-itm-four-gpu-seed50.json) |
| 调度日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261022T134902-server-a-itm-four-gpu-seed50.log) |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T134902-server-a-itm-four-gpu-seed50` |
| 正式结果 | 已进入正式训练，尚未完成 epoch 或下游评测；目前没有检索结果 |

## 证据与执行顺序

复用 10-21 四种评分各两次有效更新的单卡 smoke，以及 batch16 / cudaMallocAsync / 29 GiB 上限下四次有效更新的容量测试。启动脚本已核对完成标记、初始化权重哈希和相关源码；当前四卡均空闲，采用更宽的 40 GiB 进程上限。

依次执行四种评分的四卡 smoke（每卡 batch16），随后单卡温度校准、四组 seed50 的一 epoch 正式训练和下游评测、按预定开发集门槛复验。遇到错误或资源不足退出，不结束其他任务。

源代码和数据冻结快照、输入指纹、各 job 的命令/PID/GPU/端口/日志均保留在输出目录。W&B 禁用，无外部上传。

## 运行变更

- 13:49:02：用户再次授权启动，核实 GPU4–7 全部空闲后启动调度 PID 217291。当天已 fetch 核对实验记录仓库；未提交、未推送。
- 14:00 核对：legacy_va、tv、mean_tv_ta、sigma_max 四卡 smoke 全部完成，各两次有效 optimizer 更新，无 AMP 跳步及 OOM。四卡 local batch 均为 16；开始推进温度校准。此处不是正式训练结果。
- 14:04:32：温度校准完成。四种评分温度依次为 0.0283203125、0.02900681198693153、0.02053525026457146、0.018836490894898；完整熵与误差在输出目录 `calibration/temperatures.json`。
- 14:05:38：正式 `train/legacy_va/seed-50` 进程启动；`epoch_budget.json` 确认 world_size=4、global_batch=64、epoch=1、batches=1354、smoke=false。
- 14:09 核对：`updates.jsonl` 已记录 22 次有效更新、零 AMP 跳步；四卡显存约 33,345–33,569 MiB / 49,140 MiB，无 OOM。后续由既定调度继续；本记录只代表核对时状态。

当前训练日志：[`train/legacy_va/seed-50/launcher.log`](/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T134902-server-a-itm-four-gpu-seed50/train/legacy_va/seed-50/launcher.log)。进度以 `heartbeat.json`、`updates.jsonl` 及各 job.json 为准。

- 15:18:34：rank3 DataLoader 等待120秒超时，torchrun随后结束其余rank，调度15:18:36退出；未发生OOM。最后heartbeat=858，无epoch末checkpoint，不能半epoch续训。原计划接管前即检测到进程退出，未发送停止信号。
- 15:25：改为[双队列完整重试](20261022T152509-server-a-itm-parallel-retry-seed50.md)，保留本目录所有失败证据；复用已完成的smoke和校准。
