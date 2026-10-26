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
