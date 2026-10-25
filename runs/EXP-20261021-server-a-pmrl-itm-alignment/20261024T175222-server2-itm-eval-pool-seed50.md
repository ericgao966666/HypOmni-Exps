# 跨服务器单卡评测池

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T175222-server2-itm-eval-pool-seed50；子运行ID逐槽位登记 |
| 状态与核对时间 | 2026-10-24 18:08 Asia/Shanghai；server2四条缓存实际运行，server1四条容量等待，server2其余槽位训练后接力 |
| 科研范围 | 四方法、仅seed50、原四测试集；不扩展实验问题 |
| 数学实现 | 冻结源码e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750；运维包装仅分开缓存与发布阶段 |
| 全局选择 | 最后一组mean_tv_ta训练1302/1354；最终候选、融合和方法选择仍只用开发集 |
| 验证 | 13项运维检查通过；跨机作业锁实测互斥；全局selection前metrics.json未发布；同一MP3在Py3.9/3.10两端PCM SHA-256完全一致 |

| 主机 | GPU | 状态 | 当前job | 特征/ITM进度 |
|---|---|---|---|---|
| server1 / server-a | 0 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 1 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 2 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 3 | waiting_for_capacity | 等待容量/任务 | — |
| server2 | 0 | running | eval/legacy_va/seed-50/activitynet | 3808 |
| server2 | 1 | running | eval/tv/seed-50/activitynet | 3808 |
| server2 | 2 | running | eval/sigma_max/seed-50/activitynet | 3808 |
| server2 | 3 | running | eval/legacy_va/seed-50/vatex | 1208 |

原始状态在`/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50`的`portable_parallel_eval-*.json`。数据、缓存、日志和模型不复制到实验日志仓库；全部大型新增输出仍在NFS。旧串行ETA不适用于当前并行排程，完成时间需按实际缓存/ITM速度更新。

主控制器与每条GPU槽位有独立状态和启动身份；同一个训练/评测job受共享独占锁保护。不得为了填满GPU而终止其他任务；server1容量不足时只等待。当前没有把等待器或缓存完成记作正式测试结果。

## 子运行记录

- [20261024T180015-server-a-itm-parallel-eval-server-a-gpu0](20261024T180015-server-a-itm-parallel-eval-server-a-gpu0.md)
- [20261024T180024-server-a-itm-parallel-eval-server-a-gpu1](20261024T180024-server-a-itm-parallel-eval-server-a-gpu1.md)
- [20261024T180033-server-a-itm-parallel-eval-server-a-gpu2](20261024T180033-server-a-itm-parallel-eval-server-a-gpu2.md)
- [20261024T180041-server-a-itm-parallel-eval-server-a-gpu3](20261024T180041-server-a-itm-parallel-eval-server-a-gpu3.md)
- [20261024T175222-server2-itm-parallel-eval-server2-gpu0](20261024T175222-server2-itm-parallel-eval-server2-gpu0.md)
- [20261024T175723-server2-itm-parallel-eval-server2-gpu1](20261024T175723-server2-itm-parallel-eval-server2-gpu1.md)
- [20261024T175800-server2-itm-parallel-eval-server2-gpu2](20261024T175800-server2-itm-parallel-eval-server2-gpu2.md)
- [20261024T175836-server2-itm-parallel-eval-server2-gpu3](20261024T175836-server2-itm-parallel-eval-server2-gpu3.md)

## 2026-10-24 18:16核对

四组seed50训练均已完成；最后mean_tv_ta正在开发集评测。server2七条单卡测试缓存/评测任务实际运行，GPU4处理mean_tv_ta开发集；server1四条CPU容量等待槽位。server1当前0–3每卡已用约22–26GiB、算力繁忙，不满足37GiB启动余量要求，因此没有将等待器记作GPU运行。

| 主机 | GPU | 状态 | 当前job | 特征/ITM进度 |
|---|---|---|---|---|
| server1 / server-a | 0 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 1 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 2 | waiting_for_capacity | 等待容量/任务 | — |
| server1 / server-a | 3 | waiting_for_capacity | 等待容量/任务 | — |
| server2 | 0 | running | eval/legacy_va/seed-50/activitynet | 1120 |
| server2 | 1 | running | eval/tv/seed-50/activitynet | 984 |
| server2 | 2 | running | eval/sigma_max/seed-50/activitynet | 888 |
| server2 | 3 | running | eval/legacy_va/seed-50/vatex | 968 |
| server2 | 5 | running | eval/tv/seed-50/vatex | 1008 |
| server2 | 6 | running | eval/sigma_max/seed-50/vatex | 1008 |
| server2 | 7 | running | eval/legacy_va/seed-50/didemo | 144 |

追加子记录：

- [20261024T181021-server2-itm-parallel-eval-server2-gpu5](20261024T181021-server2-itm-parallel-eval-server2-gpu5.md)
- [20261024T181033-server2-itm-parallel-eval-server2-gpu6](20261024T181033-server2-itm-parallel-eval-server2-gpu6.md)
- [20261024T181051-server2-itm-parallel-eval-server2-gpu7](20261024T181051-server2-itm-parallel-eval-server2-gpu7.md)
