# PMRL / 64D / 原生目标

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-009](../../experiments/EXP-009-lowdim-finetune.md) |
| run ID | `20261020T152851-server-b-msrvtt_pmrl_d64_s50` |
| 服务器 / 状态 | server-b / COMPLETE；核对于 2026-10-20T17:57:38.608924+00:00 |
| 开始时间 | 2026-10-20T15:28:51.113906+00:00 |
| 完成标记时间 | 2026-10-20T16:56:11.998405+00:00；DONE 文件修改时间 |
| 代码仓库 / 基础版本 | Hyperbolic-Omnimodal / lowdim-handoff-20261019 / `8457b8e615837203f48d3c11957ae8777811a827` |
| 含未提交改动 | 是；基础 commit 不等于实际运行源码 |
| 实际源码 | SHA-256 `9c741b6108c7b5fa75cca4565faa4ae9c11aeb3fa3ff1ff7dd29090630b00543`；[文件哈希清单](../../results/EXP-009/2026-10-20-server-b/provenance/source_manifest_d64.json) |
| 协议 | SHA-256 `9f6e462b5aaf6753362820a962db5d078ef3b17311af35d8ada341c8a9a51f4b`；[原始协议](../../results/EXP-009/2026-10-20-server-b/provenance/protocol_d64.json) |
| 数据 | MSRVTT train/val/test=7427/500/884；[固定数据证据](../../results/EXP-009/2026-10-20-server-b/provenance/msrvtt_ready.json) |
| 条件 | seed50；维度 64；λ=原生目标；world size=1；全局 batch64 |
| 实际预算 | 10 epochs，1160 steps，测试候选 884；无早停 |
| 选模 | 验证六方向 macro R@1 选 best，epoch0 允许；本组选中 epoch 6 |
| PID / GPU / 端口 | 2933797 / 3 / file rendezvous |
| 原始结果 | `dataset_root:lowdim_finetune_64d_20261020/runs/msrvtt_pmrl_d64_s50`；本机路径见忽略的 servers.local.json |
| 执行政策 | Direct training at user request; no completed D64 GPU gate |
| 完成证据 | DONE SHA-256 `a7c03acad770403d7af103bfadb238112af67531bc34d06dadf55fa9a0c67b9a`；test_metrics SHA-256 `25f29b306c26a9115cc66cf9d1be0b4890d7fb47dbb41249f97b36a55afc493d` |
| 结果与启动命令 | [43 组指标](../../results/EXP-009/2026-10-20-server-b/metrics_43.json)、[完整运行清单](../../results/EXP-009/2026-10-20-server-b/provenance/run_provenance.json) |

这些是验证选模后的测试结果，指标为六方向，不是旧冻结头阶段的十二方向。训练种子只有 50；world size 与 GPU 布局不代表新增种子。
