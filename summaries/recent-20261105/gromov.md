# Gromov product 对齐：可行性排序、实验与结论

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/REPORT.md`；SHA-256：`90ff9600fa5c8052dc324bf2fb964db78d0f2d302ca4f2f13700b44830713edf`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

**41组预设主实验＋5组后续校准均已完成并独立重算，无失败。当前没有发现同时明确优于匹配角度baseline的GP替代方案，建议保留现有角度方案作为主baseline。**

本轮匹配ANG基线R@1=18.970%，原锥合法入锥/全部=21.598%，困难错配截断包含=8.409%。最高直接替代对齐分数是GP_E，R@1=18.994%，相对ANG仅+0.024pp，验证视频配对bootstrap区间[-0.252, +0.317]pp。

全套最高R@1为HIER_REL_E：19.043%，相对ANG+0.073pp，区间[-0.139, +0.309]pp。它仍用角度对齐，只替换层级损失；预设GP层级满足率为0.000%，不能把这个小幅检索差值称为学到了更好的祖先包含。

以上区间是同一验证集上的视频级配对bootstrap，不是训练种子置信区间，也未消除多配置选择偏差。所有实验都是冻结VAST特征、512D七子集头部、seed50、batch256、30轮9660步；没有测试集调参。

实验前可行性排序与公式（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/PLAN.md`） · 完整协议（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/README.md`） · 46组CSV（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/all_results.csv`） · 主实验审计（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/audit.json`） · 校准审计（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/calibration/audit.json`）

## 先验排序与实测判断

| 先验顺序 | 路线 | 实测判断 | 当前处理 |
|---|---|---|---|
| 0 | 零训练GP诊断 | 直接给旧checkpoint换GP读出没有带来现成收益 | 作为机制诊断，不算新训练结果 |
| 1 | 原始GP | 实现最直接；对距离控制有小幅变化，但未超过角度基线的可信波动范围，原锥合法包含仍为0 | 保留简单对照，不替换baseline |
| 2 | 上行/下行插值、退火 | 大体接近距离控制；文本方向假设没有稳定收益 | 不优先扩大参数网格 |
| 3 | 归一化GP | 默认尺度下R@1约16.3%；温度校准恢复到18.65–18.74%，仍未同时改善检索和选择性 | 必须控制尺度，当前不推荐直接替换 |
| 4 | 角度＋GP层级 | 检索保住，但相对GP95%覆盖目标几乎未满足；同权重原锥对照揭示几何取舍 | 先解决目标/多父可行性，不宣布层级成功 |
| 5 | EMA负样本降权 | 真正降权比例极低，未见明确基准收益 | 需要更可信的语义/一对多信号，而非盲目降低阈值 |
| 6 | 边界GP/Busemann | 可训练，但主检索未优于角度；固定父查询排序本来就与角度等价 | 当前优先级低 |

## 直接分数与保留原锥的路线

所有行保持原锥λ=.2、K_train=K_eval=.1，除GP_NORM显式加范数项及AUX_GP加辅助项。UP/BR只在三对可比较子集上定向，其余对用负距离；UP_TEXT/BOUND/NEG额外采用文本方向假设。H/E成对列出。

| 路线 | H R@1 | E R@1 | H合法入锥/全部% | E合法入锥/全部% | H困难错配% | E困难错配% |
|---|---|---|---|---|---|---|
| DIST | 18.758 | 18.970 | 0.000 | 0.000 | 0.000 | 0.000 |
| GP | <ins>18.864</ins> | **18.994** | 0.000 | 0.000 | 0.000 | 0.000 |
| UP | 18.807 | 18.905 | 0.000 | 0.000 | 0.000 | 0.000 |
| BR25 | 18.766 | <ins>18.978</ins> | 0.000 | 0.000 | 0.000 | 0.000 |
| BR50 | 18.791 | 18.945 | 0.000 | 0.000 | 0.000 | 0.000 |
| BR_ANNEAL | 18.758 | 18.945 | 0.000 | 0.000 | 0.000 | 0.000 |
| MIN | 16.284 | 16.333 | <ins>30.290</ins> | <ins>21.918</ins> | 20.692 | 4.932 |
| COV | 16.366 | 16.349 | **30.523** | **26.850** | 21.077 | 3.993 |
| GP_NORM | 18.620 | 18.612 | 0.000 | 0.000 | 0.000 | 0.000 |
| UP_TEXT | 18.660 | 18.856 | 0.000 | 0.000 | 0.000 | 0.000 |
| BOUND_GP | 18.579 | 18.709 | 0.000 | 0.000 | 0.000 | 0.000 |
| BOUND_UP | 18.660 | 18.888 | 0.000 | 0.000 | 0.000 | 0.000 |
| AUX_GP | **18.896** | 18.937 | 22.635 | 21.555 | 17.459 | 17.296 |
| NEG8 | 18.636 | 18.864 | 0.000 | 0.000 | 0.000 | 0.000 |
| NEG9 | 18.620 | 18.864 | 0.000 | 0.000 | 0.000 | 0.000 |

直接路线对照（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/core_routes.png`）

PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/core_routes.pdf`）。E只把GP/距离项改为物理切空间欧氏距离；这些原锥组仍保留双曲锥监督，因此不是完整欧氏模型。多数GP路线的E对照持平或更好，本轮没有GP对齐项独特依赖负曲率的证据。

## 归一化分数的温度校准

初始r均为1时，G/min(r_a,r_b)的距离系数是2G的一半。主实验后仅把初始τ从.07改为.035，其他设置和预算不变；这些是事后诊断性补充，不冒充最初41组。

| 路线 | τ=.07 R@1 | τ=.035 R@1 | 校准后合法入锥/全部% | 校准后困难错配% |
|---|---|---|---|---|
| MIN_H | 16.284 | 18.652 | <ins>21.734</ins> | 23.768 |
| MIN_E | 16.333 | <ins>18.717</ins> | 16.574 | 25.570 |
| COV_H | **16.366** | 18.685 | **22.624** | 23.644 |
| COV_E | <ins>16.349</ins> | **18.742** | 14.247 | 28.874 |

温度校准（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/normalization_calibration.png`）

PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/normalization_calibration.pdf`）。默认尺度下的损失不能全部归咎于归一化思想；校准恢复了大部分检索，但错误包含仍明显高于ANG，未形成更好的联合取舍。

## GP层级目标与径向顺序控制

| 条件 | R@1 | 主层级判据满足% | 主判据困难错配满足% | 辅助原锥合法入锥/全部% | 辅助原锥困难错配% |
|---|---|---|---|---|---|
| ANG | 18.970 | 61.138 | 8.409 | 21.598 | 8.409 |
| ANG5 | 18.807 | 79.454 | 15.061 | **31.679** | 15.061 |
| ORDER | 18.880 | 100.000 | 99.989 | 0.000 | 0.000 |
| HIER_ABS_H | 18.970 | 1.845 | 0.000 | 1.904 | 1.226 |
| HIER_ABS_E | 18.970 | 2.941 | 0.000 | 0.000 | 0.000 |
| HIER_REL_H | 18.978 | 0.000 | 0.000 | 10.341 | 5.425 |
| HIER_REL_E | **19.043** | 0.000 | 0.000 | 0.239 | 0.011 |
| HIER_REL5_H | 18.978 | 0.000 | 0.000 | <ins>29.682</ins> | 23.470 |
| HIER_REL5_E | <ins>19.010</ins> | 0.005 | 0.000 | 5.442 | 0.228 |
| AUX_GP_H | 18.896 | 67.990 | 17.459 | 22.635 | 17.459 |
| AUX_GP_E | 18.937 | 66.857 | 17.296 | 21.555 | 17.296 |

“主层级判据满足”采用各自的主训练约束，定义不同，不作跨行直接排名。AUX_GP的主判据是原锥，GP辅助项的满足情况另见约束分量表，不能把原锥满足率当作两个目标同时满足。替换原锥的GP组，其原锥列只是辅助诊断；完整平坦E组的该列是在c=1的Lorentz提升上计算，不能作为其原生几何成功指标。

相对GP组的径向margin几乎100%满足，但平均未覆盖比例仍为.155–.223，目标是≤.05；这不是仅有浮点误差的边界问题。ORDER单靠类型层次可达到100%自身满足，同时困难错配满足也接近100%，说明原始径向顺序本身缺乏配对选择性。详见约束分量（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/gp_constraint_components.csv`）。

同权重对照：HIER_REL5_H的R@1=18.978%，高于ANG5的18.807%，但辅助原锥合法包含较低、困难错配更高，且自身严格GP目标仍未满足；不能称作全面改进。

精确GP上行=0要求父节点位于原点到子节点的根路径。多父节点都满足精确祖先关系时，它们必须共享该路径，这比一般子集偏序更强。ε=.05即使在欧氏极限也只允许单父根角约25.84°；多父布局可能没有共同可行的子方向。固定末轮父节点的可行性诊断（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/GP_FEASIBILITY.md`）显示，这个问题在本轮相对GP组很普遍。它不是整个子集图不可嵌入的证明；旋转方向、改变容差或改变关系模型都可能改变结论。

## EMA降权是否真正生效

| 条件 | 降权候选对次数 | 预热后全部负对中的比例% | 相对UP_TEXT的ΔR@1 pp |
|---|---|---|---|
| NEG8_H | 7,829 | 0.00017243147 | <ins>-0.024</ins> |
| NEG9_H | 1 | 2.2024712e-08 | -0.041 |
| NEG8_E | 560,393 | 0.012342494 | **+0.008** |
| NEG9_E | 1,685 | 3.7111639e-05 | **+0.008** |

分母为预热后45.4035亿个批内负配对出现次数，不是独立样本数。NEG9_H全程仅降权1次；本轮不能据此证明“修正假负样本”有效，也不能否定有语义依据的多正样本训练。几何教师输出不是人工语义真值。

## 机制诊断与完整数据

- 零训练重读出、GP缺口与四点δ（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/ZERO_TRAINING.md`）：历史FP16特征，仅作诊断。
- 六方向与三种读出（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/directions.csv`）：原生分数、角度、测地线；不事后挑选最优读出替换预设主结果。
- H/E配对（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/metric_pairs.csv`） · 额外文本方向假设（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/text_order_assumptions.csv`） · 负样本触发统计（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/negative_activity.csv`）。
- 主实验样本区间（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/paired_bootstrap.csv`） · 补充样本区间（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/calibration/paired_bootstrap.csv`）。

δ是同一224点集合、同一20000四元组的抽样最大值，并除以该集合直径。对同一组点同时计算双曲与切空间距离，较小相对δ本身不证明语义树或独特曲率收益。没有额外构造WordNet/CIFAR文本树，因此外部语义层级泛化仍未验证。

建议保留现有角度＋原锥方案作为baseline。若继续GP研究，优先明确多父关系所需的容差/关系定义，以及真实的一对多监督；当前证据不足以支持仅凭“共享祖先”解释就直接替换检索分数。

原41组自动报告（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/REPORT.main41-generated-20261102.md`） · 主实验CSV（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/results.csv`） · 校准CSV（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/calibration/results.csv`） · 后处理来源（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/gromov_alignment_20261102/analysis/postprocess_provenance.json`）
