# 训练释放后接力的单卡评测槽位

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T181021-server2-itm-parallel-eval-server2-gpu5 |
| 服务器 / GPU | server2 / 5 |
| 状态与核对时间 | 已完成；2026-10-24 21:39 Asia/Shanghai |
| 控制器身份 | PID 1362363；启动时间及boot ID在原始状态 |
| 当前job | eval/tv/seed-50/vatex |
| 训练源码 | `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；冻结实现，不重训或增加seed |
| 实际运维部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/590da21f697413bd3af32fbde9fc9b6af5677847f524b08a4e9fed6aee50dc54`；包内code_manifest.json记录各文件哈希 |
| 资源策略 | 等待训练释放后领取任务；29GiB预算+8GiB余量；共享job锁互斥 |
| 输出状态 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50/portable_parallel_eval-server2-gpu5.json` |
| 原始日志 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/logs/20261024T181021-server2-itm-parallel-eval-server2-gpu5.log` |
| 验证 | 13项运维检查；真实特征缓存进度、跨机锁及两端音频PCM一致性验证 |

本槽位继续seed50四测试集的同一任务池。先预计算缓存，最终开发集选择锁定后才发布测试指标；主控制器复用结果。所有大文件仍在NFS，不停止其他进程。

历史状态快照：running；2026-10-24 18:16 Asia/Shanghai。

最终核对：已完成。本run属于同一四方法、seed50矩阵，完整结果见[权威快照](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)。原始日志、源码快照与模型仍在项目/NFS。
