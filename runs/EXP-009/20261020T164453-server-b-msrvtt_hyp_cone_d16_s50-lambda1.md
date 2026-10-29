# 双曲有锥 / 16D / 1.0

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-009](../../experiments/EXP-009-lowdim-finetune.md) |
| run ID | `20261020T164453-server-b-msrvtt_hyp_cone_d16_s50-lambda1` |
| 服务器 / 状态 | server-b / COMPLETE；核对于 2026-10-20T17:57:38.608924+00:00 |
| 开始时间 | 2026-10-20T16:44:53.005978+00:00 |
| 完成标记时间 | 2026-10-20T17:34:49.688870+00:00；DONE 文件修改时间 |
| 代码仓库 / 基础版本 | Hyperbolic-Omnimodal / lowdim-handoff-20261019 / `8457b8e615837203f48d3c11957ae8777811a827` |
| 含未提交改动 | 是；基础 commit 不等于实际运行源码 |
| 实际源码 | SHA-256 `aee691955eed83bda82c6bda3e42f7b848c6215336f2610f75758ce494678339`；[文件哈希清单](../../results/EXP-009/2026-10-20-server-b/provenance/source_manifest_lambda1.json) |
| 协议 | SHA-256 `47cf29f89c44847062a41d10ebffee9ce09354a4757fae77076b904c781df058`；[原始协议](../../results/EXP-009/2026-10-20-server-b/provenance/protocol_lambda1.json) |
| 数据 | MSRVTT train/val/test=7427/500/884；[固定数据证据](../../results/EXP-009/2026-10-20-server-b/provenance/msrvtt_ready.json) |
| 条件 | seed50；维度 16；λ=1.0；world size=2；全局 batch64 |
| 实际预算 | 10 epochs，1160 steps，测试候选 884；无早停 |
| 选模 | 验证六方向 macro R@1 选 best，epoch0 允许；本组选中 epoch 7 |
| PID / GPU / 端口 | 2972669 / 1, 2 / file rendezvous |
| 原始结果 | `dataset_root:lowdim_entailment16_lambda1_20261020/runs/msrvtt_hyp_cone_d16_s50`；本机路径见忽略的 servers.local.json |
| 执行政策 | Direct lambda ablation at user request; no new CPU/GPU READY |
| 完成证据 | DONE SHA-256 `19d1591a2b0b666b9ab96d2d296f99e48df10833d0407f94e670e759c31eb0fc`；test_metrics SHA-256 `106c498cf47067c222f3ca753ba29d7905f0e0f7b7f6a9e0dd76ddda06e1c9cd` |
| 结果与启动命令 | [43 组指标](../../results/EXP-009/2026-10-20-server-b/metrics_43.json)、[完整运行清单](../../results/EXP-009/2026-10-20-server-b/provenance/run_provenance.json) |

这些是验证选模后的测试结果，指标为六方向，不是旧冻结头阶段的十二方向。训练种子只有 50；world size 与 GPU 布局不代表新增种子。
