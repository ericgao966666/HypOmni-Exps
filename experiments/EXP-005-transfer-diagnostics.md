# 音频迁移退化的训练与打分诊断

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-005 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成探索性诊断 |
| 实验日期 / 最后核对 | 2026-10-17 / 2026-10-20 |
| 前序 | [冻结迁移](EXP-004-frozen-transfer.md) |

## 要回答的问题

音频迁移下降是否只出现在训练后期、是否只由锥损失引起，以及半径与评分函数是否参与退化？

## 协议与运行

冻结 encoder，重放原始 seed50 头部轨迹，记录 epoch 0/1/2/3/5/10/15/20/30。epoch 0 是原共享 warmup 的末状态。增加 PMRL spectral、cosine3、cosine9 和 hyperbolic0 对照；测试轨迹用于探索，不用于重新选最佳模型。

精确重放协议：[early transfer protocol](../../Hyperbolic-Omnimodal/outputs/early_transfer_20261017/protocol.json)。训练目标对照、源码快照及运行清单：[objective controls](../../Hyperbolic-Omnimodal/outputs/vast_objective_controls_20261017/)。

## 结果

原轨迹 AudioCaps R@1，单位 %：

| 轮数 | T→A | A→T |
|---|---:|---:|
| 0 | 32.05 | 42.05 |
| 1 | 23.98 | 31.39 |
| 10 | 12.64 | 23.44 |
| 30 | 9.12 | 18.32 |

各对照在 epoch 30 的 AudioCaps R@1：

| 目标 | T→A | A→T |
|---|---:|---:|
| PMRL spectral | 10.28 | 13.49 |
| cosine3 | 15.54 | 20.88 |
| cosine9 | 16.28 | 21.73 |
| hyperbolic0，无锥约束 | 2.78 | 0.28 |
| ours，λ=0.1 | 9.12 | 18.32 |

同一 hyperbolic0 权重改用方向余弦后，AudioCaps 为 14.80 / 13.35%，明显高于其测地距离分数，但仍低于初始水平。方向余弦仅是诊断读出，不替换双曲模型的正式检索结果。

原始证据：[轨迹 CSV](../results/EXP-005/2026-10-20/early_transfer.csv)、[目标对照 CSV](../results/EXP-005/2026-10-20/objective_controls.csv)、[同权重评分消融](../results/EXP-005/2026-10-20/same_weights_scoring_ablation.json)。

## 随训练轮数变化的迁移曲线

![五种冻结编码器头部训练目标在四个数据集上的逐轮迁移曲线](../results/EXP-005/2026-10-20/transfer_curves.png)

[打开原图](../results/EXP-005/2026-10-20/transfer_curves.png) · [下载矢量 PDF](../results/EXP-005/2026-10-20/transfer_curves.pdf) · [逐轮数值 JSON](../results/EXP-005/2026-10-20/comparison.json)

横轴是共享 warmup 后的训练 epoch。VAST 验证与 MSRVTT 迁移面板使用六方向 macro R@1；AudioCaps 和 Clotho 面板使用双向平均 R@1，样本数分别为 704 和 1,045。这张图展示五种目标的探索性轨迹，不将跨域测试曲线用于选模。

## 结论与局限

退化从第一轮已经出现，多种目标均有下降；不能归因于仅仅训练太久或仅仅锥损失。评分消融支持半径/打分参与结果变化，但没有单独确定所有机制的因果贡献。

[数据审计](../../Hyperbolic-Omnimodal/outputs/vast_objective_controls_20261017/data_audit.json)发现 AudioCaps 一条源视频重叠，另有 703 条去重子集评估；上表保留 704 条原 cohort 以比较轨迹。两套数据口径不能混算。诊断中的 MSRVTT epoch 0 macro 为 18.081%，与 EXP-004 独立推理的 18.100% 略有差异，引用时保留各自原始结果。

## 下一步

可考虑在固定数据与预算下检查保持初始文本音频能力的训练目标；该建议尚未立项或启动。

## 变更记录

- 2026-10-17：完成时长轨迹、四种额外目标对照及同权重评分诊断。
- 2026-10-20：补录；区分探索性测试曲线与验证选模。
- 2026-10-20：补入原始迁移曲线 PNG/PDF 和逐轮 JSON，供本页及 EXP-004 共用。
