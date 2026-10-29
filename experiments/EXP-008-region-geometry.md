# 区域层级几何：seed0联合训练有检索收益，完整测试尚未解锁

[返回总览](../README.md) · `EXP-008` · 实际阶段完成：2026-10-20；本机证据重新核对：2026-10-28T12:41:34.660651+00:00

**HyCoCLIP原生目标的seed0联合训练，双曲/欧氏dev双向平均R@5为45.80%/41.43%（+4.37pp）；UNCHA为46.17%/45.45%（+0.72pp）。** 这些是固定5000步的开发集末轮结果，不能据此断言层级优势或正式测试胜出。原先“只交接、尚无本机正式结果”的状态已过时。

## 关键设置与结果

GRIT子集100,000/5,000/5,000图像，512D、global batch256；原协议20个冻结阶段＋12个联合阶段，各5000步。保留source-server特征并经哈希验证，联合阶段从相应冻结结果接续。原生目标与matched目标不能混排；以下仅比较相同native目标、seed0、entailment weight=.2的联合末轮。

| 几何 | HyCoCLIP dev平均R@5 (%) | UNCHA dev平均R@5 (%) |
|---|---:|---:|
| 欧氏 | <ins>41.43</ins> | <ins>45.45</ins> |
| 双曲 | **45.80** | **46.17** |

matched冻结目标seed0下，HyCoCLIP双曲/欧氏为37.19%/37.11%，UNCHA为37.89%/37.92%，差异很小。native冻结目标与matched目标表现不同，不能把native检索增益全部归因于空间曲率。

[24阶段末轮完整数值](../results/EXP-008/2026-10-28-server-b-audit/stage_summary.json) · [协议](../results/EXP-008/2026-10-28-server-b-audit/protocol.json) · [条件清单](../results/EXP-008/2026-10-28-server-b-audit/arms.json) · [各阶段证据](../results/EXP-008/2026-10-28-server-b-audit/arms/)。末轮提取保留源JSONL哈希，完整日志和权重留在数据目录。

## 当前完成范围

核实20个冻结阶段和4个seed0联合阶段均为5000步完成，共24/32阶段；seed1/2的8个联合阶段延期，**不是seed1/2所有训练都未做**。聚合状态为selected_seeds_complete，full_experiment_complete=false，test_evaluation_started=false。原测试门槛仍要求全32阶段完成；本次未启动训练或测试。

[选择种子完成标记](../results/EXP-008/2026-10-28-server-b-audit/selected_seeds_complete.json) · [聚合状态](../results/EXP-008/2026-10-28-server-b-audit/pipeline_status.json) · [运行索引](../runs/EXP-008/README.md)。尚缺跨seed联合结果、正式测试和完整几何判定，不能声称整个实验结束或已经证明严格层级包含。

原迁移和停止历史完整保留在[交接附录](../runs/EXP-008/history-handoff-before-audit-20261028.md)。后续先确认是否继续延期条件，再按原门槛统一测试；本次仅补录已存在证据。
