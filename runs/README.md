# 单次运行目录

新运行在 `runs/<实验编号>/<唯一run-id>.md` 建档，使用 [run 模板](../templates/run.md)。

每台服务器写自己的 run 文件；同一实验的主要结论汇总到 `experiments/` 对应卡片。这样两台机器可分别补充记录，减少同时改一张大表的冲突。

历史首批实验保留原项目的运行清单链接，不补造未知的开始时间、commit 或 PID。已有运行记录用于追溯，不表示训练当前仍在运行。

- [server-b 64D方案与扩维运行](EXP-20261021-server-b-retrieval-training/README.md)：2026-10-25核对，14/20选定条件测试完成，训练中断。

- [server2 PMRL数据扩充配对运行](EXP-20261026-server2-pmrl-data-scale/20261026T153907-server2-data-scale-seed50.md)：2026-10-26已完成两组训练与8项测试，正式结果已手工回填。

## 运行历史与来源审计

详细过程与结果正文分开维护。重写前的运行历史保留在以下入口，结论以链接的当前实验卡为准。

- [PMRL–ITM历史](EXP-20261021-server-a-pmrl-itm-alignment/history-before-results-rewrite-20261026.md) · [当前结果](../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md)。
- [64D及扩维历史](EXP-20261021-server-b-retrieval-training/history-before-results-rewrite-20261026.md) · [当前结果](../experiments/EXP-20261021-server-b-retrieval-training.md)。
- [EXP-004来源审计](../experiments/details/EXP-004-provenance.md) · [EXP-006来源审计](../experiments/details/EXP-006-provenance.md)。
512D MERU式scale、曲率与温度的17组预训练见[运行索引](EXP-20261026-server-b-meru512-scale/README.md)：全部完成30轮，进程已退出，未微调MSRVTT。
64D优先训练方案的新队列见[运行索引](EXP-20261021-server-b-retrieval-training/README.md)。启动修复、当前PID/GPU及自动后续阶段的记录位置已注明。
历史首批实验保留原项目的运行清单链接，不补造未知的开始时间、commit 或 PID。EXP-009 已补记 server-b 的43次完成训练及一次GRAM 16D失败重跑，见[运行索引](EXP-009/README.md)。
单变量蕴含实验58组见[运行索引](EXP-20261026-server-b-entailment-singlefactor/README.md)：56完成、2失败，登记进程已退出。
C0温度与曲率65组见[运行索引](EXP-20261027-server-b-c0-temperature-curvature/README.md)：65完成、0失败，全部登记进程退出。
C0温度与曲率新增λ=.2的13组，合计78条件；[运行索引](EXP-20261027-server-b-c0-temperature-curvature/README.md)保留原65组并追加本轮记录。
λ=.3联合学习补充已完成：[运行记录](EXP-20261027-server-b-c0-temperature-curvature/20261028T122522-server-b-C0_l03__L_c1t1-seed50.md)；C0累计79条件完成。

## 2026-10-28补录

- [EXP-008](../experiments/EXP-008-region-geometry.md)：结果、边界与精简来源已归档。
- [EXP-20261026-server-b-itm-geometry-diagnostics](../experiments/EXP-20261026-server-b-itm-geometry-diagnostics.md)：结果、边界与精简来源已归档。
- [EXP-20261027-server-b-itm-native-baseline](../experiments/EXP-20261027-server-b-itm-native-baseline.md)：结果、边界与精简来源已归档。
- [EXP-20261027-server-b-itm-author-baselines](../experiments/EXP-20261027-server-b-itm-author-baselines.md)：结果、边界与精简来源已归档。
