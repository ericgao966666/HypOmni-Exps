# GRAM / 128D / 原生目标

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-009](../../experiments/EXP-009-lowdim-finetune.md) |
| run ID | `20261020T072330-server-b-msrvtt_gram_d128_s50` |
| 服务器 / 状态 | server-b / COMPLETE；核对于 2026-10-20T17:57:38.608924+00:00 |
| 开始时间 | 2026-10-20T07:23:30.154721+00:00 |
| 完成标记时间 | 2026-10-20T08:48:45.920680+00:00；DONE 文件修改时间 |
| 代码仓库 / 基础版本 | Hyperbolic-Omnimodal / lowdim-handoff-20261019 / `8457b8e615837203f48d3c11957ae8777811a827` |
| 含未提交改动 | 是；基础 commit 不等于实际运行源码 |
| 实际源码 | SHA-256 `e24df6d86f3db18859ac0190ce1132931ed8ae440b89cb959938685de23cc88e`；[文件哈希清单](../../results/EXP-009/2026-10-20-server-b/provenance/source_manifest_main28.json) |
| 协议 | SHA-256 `4091fdd6497d328cc64b5408ecc9f3a96f4598f4e119e5f13535c34224223660`；[原始协议](../../results/EXP-009/2026-10-20-server-b/provenance/protocol_main28.json) |
| 数据 | MSRVTT train/val/test=7427/500/884；[固定数据证据](../../results/EXP-009/2026-10-20-server-b/provenance/msrvtt_ready.json) |
| 条件 | seed50；维度 128；λ=原生目标；world size=2；全局 batch64 |
| 实际预算 | 10 epochs，1160 steps，测试候选 884；无早停 |
| 选模 | 验证六方向 macro R@1 选 best，epoch0 允许；本组选中 epoch 8 |
| PID / GPU / 端口 | 2650145 / 4, 5 / file rendezvous |
| 原始结果 | `dataset_root:lowdim_finetune_20261019/runs/msrvtt_gram_d128_s50`；本机路径见忽略的 servers.local.json |
| 执行政策 | CPU and scoped GPU gates passed |
| 完成证据 | DONE SHA-256 `10d61de1d4d3f91c2cd19cd3f556ae1c6f9c5c220c2aff974ac82f87844a4270`；test_metrics SHA-256 `524a58c679678745dd9def216c535a281564596fd7374eca2f9e9c5b3544aaa1` |
| 结果与启动命令 | [43 组指标](../../results/EXP-009/2026-10-20-server-b/metrics_43.json)、[完整运行清单](../../results/EXP-009/2026-10-20-server-b/provenance/run_provenance.json) |

这些是验证选模后的测试结果，指标为六方向，不是旧冻结头阶段的十二方向。训练种子只有 50；world size 与 GPU 布局不代表新增种子。
