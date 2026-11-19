# LanguageBind 正初始化：固定与学习 LR 下的蒸馏排名不同

[返回实验总览](../README.md) · `EXP-20261114-server-b-languagebind-positive` · 结果 2026-11-14 至 15 UTC · 文档更新 2026-11-19

在 800 条 MSR-VTT 验证样本上，N=100 的独立 LoRS 在固定 LR 下比 HoPA 高 **0.076pp R@1**，而 HoPA 在可学习 LR 下比独立 LoRS 高 **0.375pp**。两种 LR 模式的 HoPA 和独立 LoRS 都高于共享 3-pair 的验证选优值。初始校准未通过 WBCE/CE 门槛。后续两组诊断均完成，证据限于验证集及一个蒸馏 seed。

## 研究问题与关键设置

采用 LanguageBind 正初始化，专家用 CE，蒸馏内循环和学生用 WBCE。蒸馏回放精确恢复专家段起点，学生从三个未见 head 初始化。后续比较把原 WBCE/CE 90% 门槛保留为诊断项。独立 LoRS 的三对各用五条 CE 专家、各蒸馏 2,000 步；每对 N=100，变量和总更新成本高于共享合成集。

## 主要结果

| 方法 | 固定 LR 验证 R@1 | 学习 LR 验证 R@1 |
| --- | --- | --- |
| HoPA | <ins>3.125 ± 0.430</ins> | **3.611 ± 0.345** |
| 共享 3-pair | 2.431 ± 0.087 | 2.382 ± 0.167 |
| 独立 pairwise LoRS | **3.201 ± 0.024** | <ins>3.236 ± 0.052</ins> |

固定 LR 的选优结果受验证选择影响。严格配对小试固定末态下，HoPA 可学习 LR 为 2.375%（随机 1.410%），共享 3-pair 的固定 LR 为 1.146%（随机 1.562%）。完整 R@5/R@10 和学习率敏感性见报告。

## 结果与来源

[校准、选优、固定末态与 LoRS 比较](../summaries/recent-20261119/languagebind-positive.md)

本地 `dataset_root/LanguageBind-Positive-20261114/continuations/ce-wbce-v2/results/REPORT.md`，SHA-256 `67cc4dfdf305561f066b0e6d9a37b548372e4dbde2e1a70c7a3a140da382f483`。

本地 `dataset_root/LanguageBind-Positive-20261114/continuations/independent-lors-v1/results/REPORT.md`，SHA-256 `50729cf2b6d60c14db257ab5c9794b22a56b66cb3d4319020a4d7a617b4c62ae`。
