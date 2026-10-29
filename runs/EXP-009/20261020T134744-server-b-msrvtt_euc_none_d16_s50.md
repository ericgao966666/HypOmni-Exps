# 欧氏无锥 / 16D / 0.0

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-009](../../experiments/EXP-009-lowdim-finetune.md) |
| run ID | `20261020T134744-server-b-msrvtt_euc_none_d16_s50` |
| 服务器 / 状态 | server-b / COMPLETE；核对于 2026-10-20T17:57:38.608924+00:00 |
| 开始时间 | 2026-10-20T13:47:44.680764+00:00 |
| 完成标记时间 | 2026-10-20T14:47:13.089361+00:00；DONE 文件修改时间 |
| 代码仓库 / 基础版本 | Hyperbolic-Omnimodal / lowdim-handoff-20261019 / `8457b8e615837203f48d3c11957ae8777811a827` |
| 含未提交改动 | 是；基础 commit 不等于实际运行源码 |
| 实际源码 | SHA-256 `afcf7b5ce2517b4e8c885cd2227c97f80ae2f5ffdd6ccfedd08bd3d19ca61bb7`；[文件哈希清单](../../results/EXP-009/2026-10-20-server-b/provenance/source_manifest_d16.json) |
| 协议 | SHA-256 `a342971ece1f2134b6ca413dd6c339c5676776052f8ede558f2f5957d8727677`；[原始协议](../../results/EXP-009/2026-10-20-server-b/provenance/protocol_d16.json) |
| 数据 | MSRVTT train/val/test=7427/500/884；[固定数据证据](../../results/EXP-009/2026-10-20-server-b/provenance/msrvtt_ready.json) |
| 条件 | seed50；维度 16；λ=0.0；world size=2；全局 batch64 |
| 实际预算 | 10 epochs，1160 steps，测试候选 884；无早停 |
| 选模 | 验证六方向 macro R@1 选 best，epoch0 允许；本组选中 epoch 7 |
| PID / GPU / 端口 | 2868174 / 1, 3 / file rendezvous |
| 原始结果 | `dataset_root:lowdim_finetune_16d_20261020/runs/msrvtt_euc_none_d16_s50`；本机路径见忽略的 servers.local.json |
| 执行政策 | CPU and scoped GPU gates passed |
| 完成证据 | DONE SHA-256 `3d3f98a01aa119e3fc0afd554f8688508396e16ae5cc4ee74aed83e630b6890f`；test_metrics SHA-256 `da86e264761e17c98005e020b3c73c530c3a3d950846deb4176d4db9e3382112` |
| 结果与启动命令 | [43 组指标](../../results/EXP-009/2026-10-20-server-b/metrics_43.json)、[完整运行清单](../../results/EXP-009/2026-10-20-server-b/provenance/run_provenance.json) |

这些是验证选模后的测试结果，指标为六方向，不是旧冻结头阶段的十二方向。训练种子只有 50；world size 与 GPU 布局不代表新增种子。
