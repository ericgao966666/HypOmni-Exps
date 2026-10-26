# EXP-006：微调预算、初始化和结果来源

[返回实验结论](../EXP-006-msrvtt-finetune.md)

本页保存详细结果或来源审计；2026-10-26从原实验卡整理，原始指标与图表未改写。

## 协议与版本

四种方法端到端微调，按验证集六方向 macro R@1 选 checkpoint，包含 epoch 0。测试为相同的 884 个音视频齐全的视频，不是完整 MSRVTT-1K。输出均为 512 维。完整协议、优化器和初始化说明见项目实验文档（原服务器本机路径：`../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/README.md`）和运行目录（原服务器本机路径：`../../Hyperbolic-Omnimodal/outputs/msrvtt_finetune_20261017/`）。

| 版本 | 运行情况 | 位置 |
|---|---|---|
| 初始早停 | VAST/GRAM/PMRL 分别完成 9/4/6 轮，Ours 10 轮 | 历史归档（原服务器本机路径：`../../Hyperbolic-Omnimodal/outputs/msrvtt_finetune_20261017/early_stopped_20261017/`） |
| 当前完整预算 | 原状态恢复，四者均完成 10 轮、1,160 次更新，无跳步；仍由验证集选模 | 顶层 comparison.csv / comparison.json |

补足预算是在看过初始测试结果后提出的后续实验，不能写成全新预注册测试。

## 微调前的结果从哪里来

“微调前”指**尚未在本轮 MSRVTT 训练集上更新参数时，起始 checkpoint 在 MSRVTT 测试集上的表现**。它沿用 [EXP-004 的 MSRVTT 冻结评测](../EXP-004-frozen-transfer.md)，与“微调后”使用相同的 884 个测试视频、caption 和六个检索方向。

| 模型 | 本轮微调的起始权重 | 微调前的原始评测 |
|---|---|---|
| VAST | 官方发布的 `model_step_204994.pt` | [VAST metrics](../../results/EXP-006/2026-10-20/provenance/vast_before_metrics.json) |
| GRAM | 官方发布的 `gram_model_step_459.pt` | [GRAM metrics](../../results/EXP-006/2026-10-20/provenance/gram_before_metrics.json) |
| PMRL | 官方发布的 `pmrl_base.pt` | [PMRL metrics](../../results/EXP-006/2026-10-20/provenance/pmrl_before_metrics.json) |
| Ours | VAST 官方骨干，加上此前在 VAST 上训练、按验证集选定的 `minimal9_B1_standard_s50/best.pt` 子集头，9 对、λ=0.1、seed50 | [Ours metrics](../../results/EXP-006/2026-10-20/provenance/ours_before_metrics.json) |

因此，“微调前”模型已经有预训练经历，Ours 还已经完成此前的子集头训练；这里衡量的是随后在 MSRVTT 上端到端微调带来的变化。四种方法的预训练历史不同，不能把前后比较解释为相同初始模型下仅改变损失的因果消融。

在结果整理代码中，`report_msrvtt_finetune.py` 从 `outputs/msrvtt_author_unimodal_20261016/<model>/metrics.json` 读取 `before`，从本轮各方法的 `test_metrics.json` 读取 `after`。本次已核对：微调前的全部 84 个 Recall 值与 EXP-004 及原始评测文件一致，测试 manifest 的 SHA-256 也一致；四组初始化路径与之前评测的 checkpoint 路径相符。依据见[本轮协议](../../results/EXP-006/2026-10-20/provenance/finetune_protocol.json)和加载记录：[VAST](../../results/EXP-006/2026-10-20/provenance/vast_load_audit.json)、[GRAM](../../results/EXP-006/2026-10-20/provenance/gram_load_audit.json)、[PMRL](../../results/EXP-006/2026-10-20/provenance/pmrl_load_audit.json)、[Ours](../../results/EXP-006/2026-10-20/provenance/ours_load_audit.json)。

**训练曲线的 epoch 0 与表格“微调前”使用不同数据划分。** 曲线是 500 个验证视频的分数，用于选模；表格是 884 个测试视频的分数。例如 VAST 的表格微调前 macro R@1 为 18.10%，而曲线 epoch 0 为 22.10%。四组初始验证结果见 [VAST](../../results/EXP-006/2026-10-20/provenance/vast_epoch0_validation.json)、[GRAM](../../results/EXP-006/2026-10-20/provenance/gram_epoch0_validation.json)、[PMRL](../../results/EXP-006/2026-10-20/provenance/pmrl_epoch0_validation.json)、[Ours](../../results/EXP-006/2026-10-20/provenance/ours_epoch0_validation.json)。


## 变更记录

- 2026-10-17：初始早停结果保存，随后补足统一十轮预算并重算报告与 bootstrap。
- 2026-10-20：补录；当前主表使用完整预算版本。
- 2026-10-20：补入已有训练对比 PNG/PDF 与机器可读汇总，供本页和 EXP-004 共用。
- 2026-10-20：展开微调前后全部六方向 R@1/5/10 与 MedR，补充起始 checkpoint、冻结评测及 epoch 0 验证来源说明；原始数值不变。
