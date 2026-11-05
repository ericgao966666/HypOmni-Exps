# K、eta、alpha 训练对照结果

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/REPORT.md`；SHA-256：`b745117dfd3eb0b5db44841ef2c92eb9b8901d7eba1d290f615c433e2f567a5d`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

8/8组完成30轮（每组9660步）；VAST验证2048、512D、seed50、λ=.2、曲率和温度可学习。主表固定末轮，不使用测试集。

本轮发现：在统一 K_eval=.3 下，训练 K=.3 将合法满足率从 0 提高到 12.869%，R@1 从 18.750% 降至 18.066%（−0.684 pp），但合法覆盖降到 74.859%。此时循环错配合法入锥率为 0.022%，每个视频九边全部合法满足率仍为 0；不能宣布完整层次结构已学成。

alpha=.05/.1 将平均外向夹角从 79.679° 降至 77.634°/75.684°，R@1 分别为 18.726%/18.612%。统一 K_eval=.5 下，合法满足率从 4.427% 升至 9.863%/16.075%，合法覆盖仍有 96.343%/92.676%。这提供了较温和取舍的单seed证据，但在 K_eval≤.3 下二者仍为0。

eta=.7 使夹角更大、K_eval=.5下的合法满足率更低，未支持“缩窄训练阈值必然改善几何”的假设；eta=1.2 有一定改善。eta=.7+alpha=.1 的组合也没有优于单独alpha=.1的角度与K_eval=.5满足率。所有条件在原 K_eval=.1 下仍为0，径向顺序均为100%，说明这一轮主要差别在角度与合法域，而不是简单的半径先后关系。

| 条件 | R@1 % | 外向夹角 ° | S@K=.1 % | S@K=.3 % | S@K=.5 % | 合法覆盖@K=.5 % | 错配S@K=.5 % | 径向顺序 % |
|---|---|---|---|---|---|---|---|---|
| baseline | <ins>18.750</ins> | 79.679 | **0.000** | <ins>0.000</ins> | 4.427 | 98.503 | 0.016 | **100.000** |
| K02 | 18.481 | 76.773 | **0.000** | <ins>0.000</ins> | 6.033 | 33.333 | **0.000** | **100.000** |
| K03 | 18.066 | **73.327** | **0.000** | **12.869** | **24.056** | 24.365 | 0.168 | **100.000** |
| eta07 | **18.856** | 80.564 | **0.000** | <ins>0.000</ins> | 0.282 | **99.978** | **0.000** | **100.000** |
| eta12 | 18.734 | 79.111 | **0.000** | <ins>0.000</ins> | 11.252 | 89.334 | 0.054 | **100.000** |
| alpha005 | 18.726 | 77.634 | **0.000** | <ins>0.000</ins> | 9.863 | 96.343 | 0.033 | **100.000** |
| alpha01 | 18.612 | <ins>75.684</ins> | **0.000** | <ins>0.000</ins> | <ins>16.075</ins> | 92.676 | 0.081 | **100.000** |
| eta07_alpha01 | 18.701 | 76.395 | **0.000** | <ins>0.000</ins> | 4.829 | <ins>99.750</ins> | <ins>0.005</ins> | **100.000** |

S均为双方处于对应K合法域且入锥的边数/全部9N；所有行使用相同K_eval和eta_eval=1比较。径向顺序为子节点比父节点更远的比例。错配是循环错配控制，并非语义负标签。

共同K下的合法满足率和覆盖率（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/K_matrix.png`）
PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/K_matrix.pdf`） · 完整阈值CSV（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/extended.csv`）

检索、夹角与径向顺序（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/geometry_retrieval.png`）
PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/geometry_retrieval.pdf`） · 主结果CSV（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/results.csv`）

## 解释边界

- 增大训练K与仅增大评估K通过同列比较区分；不同K列之间的变化属于读出阈值效应。
- 固定K下的合法满足率、错配率、覆盖率及检索必须一起看；角度变小不保证严格入锥。
- alpha在锥外也增大角度压力。没有合适的匹配权重消融时，不能把提升全归因于入锥后梯度。
- 单seed与多配置探索不支持统计显著性、稳定泛化或测试集收益结论。

## 复核

新旧基线R@1均为18.750%，平均夹角差约0.000107°，但权重不逐位相同（最大参数绝对差0.001013）；本轮所有归因使用新训练的共同基线。详见基线数值比较（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/baseline_comparison.json`）。

audit.json（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/audit.json`） 包含末轮产物哈希、保存特征重算检索和全部训练协议内K读出，以及新旧基线权重比较；tests.json（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/tests.json`）为6项CPU检查。8组真实数据GPU smoke通过，全部正式训练进程退出情况见logs/launches.json（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/logs/launches.json`）。

完整协议与复现说明（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/README.md`） · 扩展读出来源（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/cone_training_20261029/analysis/extended.json`）
