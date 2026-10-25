# PMRL ITM：GPU 4–7 启动记录

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-a-pmrl-itm-alignment](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261021T170458-server-a-itm-start-seed50 |
| 服务器 | server-a |
| 状态与核对时间 | 已停止：四种单卡 smoke 均通过，四卡阶段被原空闲门槛阻止；2026-10-21 17:14 核对，Asia/Shanghai；正式训练未开始 |
| 开始 / 结束时间 | 2026-10-21 17:04:58 +08:00 / 尚未结束 |
| 代码仓库 / 基底 commit | PMRL-ITM；基底 `a230347a072a46cdcb97eb30f4a5cdcf6f2119db` |
| 含未提交改动 | 是；实际运行以源码快照为准 |
| 实际运行源码快照 | 输出目录 `source/e55de36ae08aba99587c71fe72827cffdea7a4b827442bf5d74bf1d88b698fc3/`；该 SHA-256 是快照文件哈希映射的聚合值 |
| 协议与配置 | 输出根目录 `protocol.json`、`frozen_data/manifest.json`，各 job 的 `config.json` / `job.json` |
| 数据版本与划分 | VAST accepted 86,707 条，SHA-256 `ce83a1b91fce11aed08cdc0080f96f466a668b245ad769610622b9c05a8aa5d9`；派生清单在冻结数据快照中 |
| 条件 | 严格 TVA；首轮四种评分 seed 50；正式训练四卡 × 16，全局 batch 64，一 epoch；开发集规则决定后续 seeds 42/123 |
| 资源 | 指定物理 GPU 4,5,6,7；单卡 smoke/校准/评测使用 GPU 4；四卡阶段要求 4–7 全部空闲 |
| 启动命令与资源记录 | [启动清单](../../../PMRL-ITM/artifacts/launches/20261021T170458-server-a-itm-start-seed50.json)；调度进程 PID 543885；端口由每个 job 单独检查、记录 |
| 原始结果目录 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/itm-alignment-v1` |
| 调度日志 | [启动日志](../../../PMRL-ITM/artifacts/launches/20261021T170458-server-a-itm-start-seed50.log) |
| 可同步结果快照 | 尚无正式结果 |
| 完成或失败证据 | 以各 job 的 `worker_complete.json`、训练 `run_complete.json` 与日志核实；当前仅创建协议/源码/数据快照 |

## 指标与解释

本次用户明确授权在 GPU 4–7 开始。启动前 GPU 4、6 空闲，GPU 5、7 各有约 17 GiB 的在用计算进程，因此先执行 GPU 4 的单卡检查。未停止现有进程；若四卡阶段仍不满足空闲条件，入口将退出而非抢占或常驻等待。

Smoke 与正式训练分开记录，不将 smoke 完成当作正式结果。正式结果使用一个 epoch 的最后 checkpoint，在四个固定下游视听交集上零样本评测。

## 运行变更

- 2026-10-21 17:04:58：启动已验证源码版本的完整串行入口，命令为项目 `.venv/bin/python -u -m itm_experiment.suite run --gpus 4,5,6,7 --output /data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/itm-alignment-v1`。当前处于启动检查阶段。
- 随后四种评分单卡 smoke 均完成两次有效更新；GPU 5 仍有在用进程，原空闲检查拒绝启动四卡阶段，调度进程已退出。不是模型训练失败，没有结束其他进程。
- 用户补充“只要不会爆显存就直接开始”，转入独立显存测量与共享门槛验证。旧源码快照和日志保留，不覆盖为新运行版本。
