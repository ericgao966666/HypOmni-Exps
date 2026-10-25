# sigma_max首次并行尝试：预检拒绝

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T162616-server2-itm-parallel-sigma_max |
| 服务器 | server2，GPU0–3 |
| 状态 | 16:26:43启动前检查失败；未创建训练torchrun或产生模型更新 |
| 原因 | GPU0出现未列入当次已观察PID列表的新进程；控制器按规则拒绝启动 |
| 控制器 | PID 376599，已退出；该PID是CPU控制器 |
| 源码与协议 | `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；四卡×16、86,706条，协议未变 |
| 运维部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/0ceb10be929b052f649650ebc82dc5296c433b2575e19db2804f194c6bcb2539` |
| 原始日志 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/logs/20261024T162616-server2-itm-parallel-sigma_max.log` |

未结束或修改检测到的进程。后续核实0/1/3空闲、GPU2原进程仍在且余量足够，使用新run ID `20261024T163220-server2-itm-parallel-sigma_max`启动。该失败只计启动尝试，不计已开始的正式训练。
