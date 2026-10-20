# 官方权重与本地模型的冻结迁移评测

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-004 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成 |
| 实验日期 / 最后核对 | 2026-10-16 至 17 / 2026-10-20 |
| 前序 / 后续 | [子集机制](EXP-003-subset-mechanisms.md) / [迁移诊断](EXP-005-transfer-diagnostics.md)、[MSRVTT 微调](EXP-006-msrvtt-finetune.md) |

## 要回答的问题

官方 VAST、GRAM、PMRL checkpoint 与本地层级模型，在相同输入和检索协议下，各自擅长哪些方向？优势能否迁移到其他数据集？

## 协议

不在目标数据集训练或选 checkpoint，不使用 ITM。官方三种模型使用原生头与余弦打分；本地模型使用 EXP-003 的 9 对 λ=0.1 seed50 参考和负测地距离。训练历史不同。

VAST 为 2,048 样本；MSRVTT 为音视频齐全的 884 条交集，不是完整 1K。AudioCaps 为可用的 704 条，Clotho 为 1,045 条；音频任务保留每条五个 caption，音频到文本按任一正例最优排名计算。

## 结果

| 模型 | VAST 六方向平均 R@1 % | MSRVTT 六方向平均 R@1 % |
|---|---:|---:|
| VAST | 8.46 | 18.10 |
| GRAM | 12.80 | 17.91 |
| PMRL | 18.33 | 19.97 |
| Ours | 20.52 | 19.19 |

| 模型 | AudioCaps T→A / A→T R@1 % | Clotho T→A / A→T R@1 % |
|---|---|---|
| VAST | 32.05 / 42.05 | 16.13 / 20.00 |
| GRAM | 30.28 / 36.08 | 14.45 / 15.79 |
| PMRL | 31.99 / 41.19 | 16.94 / 18.18 |
| Ours | 9.80 / 20.17 | 4.75 / 7.08 |

结果与每组的审计文件分别位于：

- [VAST 对比 CSV](../results/EXP-004/2026-10-20/vast_comparison.csv)
- [MSRVTT 对比 CSV](../results/EXP-004/2026-10-20/msrvtt_comparison.csv)
- [AudioCaps 与 Clotho 对比 CSV](../results/EXP-004/2026-10-20/audio_comparison.csv)
- [协议与 checkpoint 来源说明](../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/README.md)

## 结论与下一步

我们的视频与音频方向较强，文本相关方向的优势不足，音频文本跨域迁移明显下降。VAST 与我们共享冻结 encoder 输出，因此差异位于头部学习和打分阶段，但这不能单独识别锥损失的因果贡献。

VAST cohort 可能与官方预训练数据重叠，不能称为认证零样本；各模型训练史不同，不能称为匹配训练对照。AudioCaps 后续发现一条与训练源重叠，去重诊断见 EXP-005。

## 变更记录

- 2026-10-16 至 17：依次完成 VAST、MSRVTT、AudioCaps 和 Clotho 评测。
- 2026-10-20：补录；与 EXP-003 的十二方向结果分开记录。
