# 20261028T123204-server-b-r3-d64-lambda02-learnct-seed50

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 / 核对时间 | server-b / 2026-10-28T12:33:53.254107+00:00 UTC |
| 状态 | 已启动R3串行队列，warmup；不是完成结果 |
| 开始 | 2026-10-28T12:32:04.027346+00:00 |
| 条件 | hyp_cone；64D；seed50；λ=.2；c/τ均可学习 |
| 预算 | VAST warmup8 + frozen30 + MSRVTT joint10；batch256/256/64 |
| 数据 | VAST 82608/2048；MSRVTT 7427/500；复用既有划分与缓存 |
| 代码 | 父版本HEAD参照8457b8e615837203f48d3c11957ae8777811a827；含已有未提交改动，以封存hash为准 |
| 实际源码摘要 | `521cc681042ed9cf64e6779504d713f7380ab3c22caa46c3464a85921ba05872` |
| 协议SHA256 | `d7e3be5efad6d8369c768f01b7711ce303d02fd2a721c5ea1f86a5fbbe8c4808` |
| 调度PID / GPU / 端口 | 3072388 / 2 / 无，文件rendezvous |
| 运行清单 | workspace_root/Hyperbolic-Omnimodal/code/outputs/r3_64d_learned_ct_lambda02_20261028/logs/launches.jsonl |
| 原始输出 | dataset_root/r3_64d_learned_ct_lambda02_20261028 |
| 准备快照 | [协议、测试与启动](../../results/EXP-20261021-server-b-retrieval-training/2026-10-28-r3-learnct-implementation/README.md) |

按各阶段验证R@1选模（warmup传末轮），最终比较同R3的500视频六方向验证指标。旧欧氏温度固定，因此不能解释为纯曲率消融；单seed。未自动新增测试集推理。

本次8项CPU测试通过，旧源码、输入缓存和基线检查点hash通过核验。状态以本机logs/status.json为准。

远端状态尚未核实：本轮fetch被自动审批拒绝；未提交或推送。

归档复核 2026-10-28T12:44:18.320406+00:00：状态文件报告frozen阶段running（历史warmup已推进）；[精确快照](../../results/EXP-20261021-server-b-retrieval-training/2026-10-28-status-audit/r3_learnct_status.json)。这里只采集状态文件，不把它当作持续监控或完成证明；此前fetch受阻说明作为历史保留，本轮统一核实远端并发布。
