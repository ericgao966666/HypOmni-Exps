# MSRVTT 端到端微调与几何分析

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-006 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成；含补足预算的后续实验 |
| 实验日期 / 最后核对 | 2026-10-17 / 2026-10-20 |
| 前序 / 后续 | [冻结迁移](EXP-004-frozen-transfer.md) / [低维对照](EXP-009-lowdim-finetune.md) |

## 要回答的问题

VAST、GRAM、PMRL 与我们的方法，在同一 MSRVTT 输入协议和微调预算下表现如何？检索提升是否伴随严格包含关系？

## 协议与版本

四种方法端到端微调，按验证集六方向 macro R@1 选 checkpoint，包含 epoch 0。测试为相同的 884 个音视频齐全的视频，不是完整 MSRVTT-1K。输出均为 512 维。完整协议、优化器和初始化说明见[项目实验文档](../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/README.md)和[运行目录](../../Hyperbolic-Omnimodal/outputs/msrvtt_finetune_20261017/)。

| 版本 | 运行情况 | 位置 |
|---|---|---|
| 初始早停 | VAST/GRAM/PMRL 分别完成 9/4/6 轮，Ours 10 轮 | [历史归档](../../Hyperbolic-Omnimodal/outputs/msrvtt_finetune_20261017/early_stopped_20261017/) |
| 当前完整预算 | 原状态恢复，四者均完成 10 轮、1,160 次更新，无跳步；仍由验证集选模 | 顶层 comparison.csv / comparison.json |

补足预算是在看过初始测试结果后提出的后续实验，不能写成全新预注册测试。

## 微调前的结果从哪里来

“微调前”指**尚未在本轮 MSRVTT 训练集上更新参数时，起始 checkpoint 在 MSRVTT 测试集上的表现**。它沿用 [EXP-004 的 MSRVTT 冻结评测](EXP-004-frozen-transfer.md)，与“微调后”使用相同的 884 个测试视频、caption 和六个检索方向。

| 模型 | 本轮微调的起始权重 | 微调前的原始评测 |
|---|---|---|
| VAST | 官方发布的 `model_step_204994.pt` | [VAST metrics](../results/EXP-006/2026-10-20/provenance/vast_before_metrics.json) |
| GRAM | 官方发布的 `gram_model_step_459.pt` | [GRAM metrics](../results/EXP-006/2026-10-20/provenance/gram_before_metrics.json) |
| PMRL | 官方发布的 `pmrl_base.pt` | [PMRL metrics](../results/EXP-006/2026-10-20/provenance/pmrl_before_metrics.json) |
| Ours | VAST 官方骨干，加上此前在 VAST 上训练、按验证集选定的 `minimal9_B1_standard_s50/best.pt` 子集头，9 对、λ=0.1、seed50 | [Ours metrics](../results/EXP-006/2026-10-20/provenance/ours_before_metrics.json) |

因此，“微调前”模型已经有预训练经历，Ours 还已经完成此前的子集头训练；这里衡量的是随后在 MSRVTT 上端到端微调带来的变化。四种方法的预训练历史不同，不能把前后比较解释为相同初始模型下仅改变损失的因果消融。

在结果整理代码中，`report_msrvtt_finetune.py` 从 `outputs/msrvtt_author_unimodal_20261016/<model>/metrics.json` 读取 `before`，从本轮各方法的 `test_metrics.json` 读取 `after`。本次已核对：微调前的全部 84 个 Recall 值与 EXP-004 及原始评测文件一致，测试 manifest 的 SHA-256 也一致；四组初始化路径与之前评测的 checkpoint 路径相符。依据见[本轮协议](../results/EXP-006/2026-10-20/provenance/finetune_protocol.json)和加载记录：[VAST](../results/EXP-006/2026-10-20/provenance/vast_load_audit.json)、[GRAM](../results/EXP-006/2026-10-20/provenance/gram_load_audit.json)、[PMRL](../results/EXP-006/2026-10-20/provenance/pmrl_load_audit.json)、[Ours](../results/EXP-006/2026-10-20/provenance/ours_load_audit.json)。

**训练曲线的 epoch 0 与表格“微调前”使用不同数据划分。** 曲线是 500 个验证视频的分数，用于选模；表格是 884 个测试视频的分数。例如 VAST 的表格微调前 macro R@1 为 18.10%，而曲线 epoch 0 为 22.10%。四组初始验证结果见 [VAST](../results/EXP-006/2026-10-20/provenance/vast_epoch0_validation.json)、[GRAM](../results/EXP-006/2026-10-20/provenance/gram_epoch0_validation.json)、[PMRL](../results/EXP-006/2026-10-20/provenance/pmrl_epoch0_validation.json)、[Ours](../results/EXP-006/2026-10-20/provenance/ours_epoch0_validation.json)。

## 当前结果

### 平均表现与选模概览

六方向测试平均 R@1，单位 %：

微调前、完整预算后分别在各自列内比较，R@1 越高越好；**加粗**为最优，<ins>下划线</ins>为次优。选中 epoch 是配置记录，不参与排名。

| 模型 | 微调前 | 完整预算后 | 选中 epoch |
|---|---:|---:|---:|
| VAST | 18.10 | <ins>20.98</ins> | 6 |
| GRAM | 17.91 | 19.74 | 10 |
| PMRL | **19.97** | 20.70 | 8 |
| Ours，9 对 λ=0.1 | <ins>19.19</ins> | **24.87** | 10 |

Ours 相对 VAST 的 macro 提升 3.88 pp，条件样本 bootstrap 区间 [2.70, 5.09] pp。候选库和 checkpoint 固定，区间不是训练种子不确定性。视频→音频与音频→视频分别提升 15.61 和 14.37 pp；文本视频方向仍偏向 VAST。

几何测量中八类边半径顺序正确率 100%，A→TA 为 99.77%，但九类边的严格锥满足率均为 0%。平均 exterior angle 为 30.19°–146.08°，平均 aperture 仅 1.79°–2.91°，显示径向顺序与角度包含没有共同学成。

完整结果按微调阶段分别列出，T/V/A 分别表示文本/视频/音频。R@1、R@5、R@10 越高越好，MedR（中位排名）越低越好；各表各列按展示精度标记最优和次优。Recall 来自[原始 CSV](../results/EXP-006/2026-10-20/comparison.csv)，MedR 来自[原始 JSON](../results/EXP-006/2026-10-20/comparison.json)。

### 微调后完整结果

四种方法均完成十轮预算，使用验证集选定的 checkpoint，在同一 884 视频测试集上评估；不是强制使用最后一轮。

#### R@1

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | **45.14** | **45.25** | <ins>10.52</ins> | <ins>10.41</ins> | 7.47 | 7.13 | <ins>20.98</ins> |
| GRAM | <ins>43.89</ins> | **45.25** | 8.26 | 5.32 | 7.47 | 8.26 | 19.74 |
| PMRL | 36.43 | 36.99 | 8.37 | 8.37 | <ins>18.10</ins> | <ins>15.95</ins> | 20.70 |
| Ours | 39.59 | <ins>42.19</ins> | **10.75** | **12.10** | **23.08** | **21.49** | **24.87** |

#### R@5

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | **71.38** | **71.72** | **30.54** | **29.98** | 20.59 | 20.14 | 40.72 |
| GRAM | <ins>71.27</ins> | <ins>70.81</ins> | 22.51 | 18.33 | 21.72 | 20.48 | 37.52 |
| PMRL | 66.52 | 65.16 | 25.79 | 24.55 | <ins>40.84</ins> | <ins>40.27</ins> | <ins>43.85</ins> |
| Ours | 66.97 | 67.53 | <ins>28.28</ins> | <ins>27.15</ins> | **49.21** | **47.74** | **47.81** |

#### R@10

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | <ins>80.77</ins> | **81.00** | **41.63** | **41.06** | 29.07 | 28.17 | 50.28 |
| GRAM | **81.00** | <ins>80.88</ins> | 33.60 | 26.02 | 31.67 | 27.15 | 46.72 |
| PMRL | 75.57 | 76.47 | 36.65 | 36.54 | <ins>52.49</ins> | <ins>50.57</ins> | <ins>54.71</ins> |
| Ours | 77.49 | 78.28 | <ins>40.16</ins> | <ins>40.05</ins> | **61.43** | **59.95** | **59.56** |

#### 中位排名 MedR

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V |
|---|---:|---:|---:|---:|---:|---:|
| VAST | **2** | **2** | **16** | **17** | 37 | 51 |
| GRAM | **2** | **2** | 27 | 40 | 34 | 45 |
| PMRL | <ins>3</ins> | <ins>3</ins> | 21 | <ins>21</ins> | <ins>9</ins> | <ins>10</ins> |
| Ours | **2** | **2** | <ins>18</ins> | **17** | **6** | **6** |

### 微调前完整结果

这组分数复用 EXP-004 的起始 checkpoint 冻结评测，仅在本页展开对照；没有再次训练或按测试分数选模。

#### R@1

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | **43.67** | **41.74** | 6.56 | **6.45** | 4.64 | 5.54 | 18.10 |
| GRAM | 41.97 | 36.31 | <ins>7.35</ins> | <ins>6.00</ins> | 8.37 | 7.47 | 17.91 |
| PMRL | <ins>42.99</ins> | <ins>41.52</ins> | **7.81** | **6.45** | <ins>11.20</ins> | <ins>9.84</ins> | **19.97** |
| Ours | 36.76 | 35.52 | 5.77 | 5.43 | **15.95** | **15.72** | <ins>19.19</ins> |

#### R@5

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | <ins>68.33</ins> | <ins>65.27</ins> | 16.86 | 15.95 | 13.46 | 14.93 | 32.47 |
| GRAM | <ins>68.33</ins> | 63.69 | <ins>17.65</ins> | <ins>16.40</ins> | 24.89 | 21.04 | 35.33 |
| PMRL | **68.67** | **66.40** | **20.14** | **19.12** | <ins>28.62</ins> | <ins>27.26</ins> | **38.37** |
| Ours | 61.65 | 59.28 | 16.06 | 14.82 | **37.22** | **35.86** | <ins>37.48</ins> |

#### R@10

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | 76.70 | <ins>75.90</ins> | 23.19 | 24.21 | 20.02 | 20.81 | 40.14 |
| GRAM | <ins>78.17</ins> | 72.85 | <ins>24.77</ins> | <ins>24.66</ins> | 32.47 | 28.39 | 43.55 |
| PMRL | **78.51** | **76.92** | **29.75** | **26.02** | <ins>38.24</ins> | <ins>37.10</ins> | **47.76** |
| Ours | 71.15 | 69.23 | 23.87 | 23.19 | **47.40** | **47.17** | <ins>47.00</ins> |

#### 中位排名 MedR

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V |
|---|---:|---:|---:|---:|---:|---:|
| VAST | **2** | **2** | 69 | 67 | 99 | 92 |
| GRAM | **2** | **2** | <ins>41</ins> | 56 | 37 | 42 |
| PMRL | **2** | **2** | **33** | **39** | <ins>21</ins> | <ins>24</ins> |
| Ours | <ins>3</ins> | <ins>3</ins> | 63 | <ins>51</ins> | **13** | **14** |

## 训练曲线

![MSRVTT 四模型验证集平均 R@1 训练曲线和微调前后测试表现](../results/EXP-006/2026-10-20/training_comparison.png)

[打开原图](../results/EXP-006/2026-10-20/training_comparison.png) · [下载矢量 PDF](../results/EXP-006/2026-10-20/training_comparison.pdf) · [选模与结果汇总](../results/EXP-006/2026-10-20/comparison.json)

左图是 500 个验证视频上随 epoch 变化的六方向 macro R@1，黑圈为验证选中的 checkpoint；右图是相同 884 个测试视频上微调前后的 macro R@1。图版对应四种方法均完成十轮预算后的结果。各模型的绝对训练 loss 不在这张图中。

## 结果位置

- [最终结果表](../results/EXP-006/2026-10-20/comparison.csv)
- [检索与训练分析 PDF](../results/EXP-006/2026-10-20/analysis_figures.pdf)
- [几何分析 PDF](../results/EXP-006/2026-10-20/hyperbolic_geometry_report.pdf)
- [几何数值](../results/EXP-006/2026-10-20/geometry_summary.json)

## 结论与下一步

本轮域内微调检索收益明确，主要来自视频音频方向；这是单种子结果，不证明锥损失的独立贡献或跨域能力。严格包含仍失败。低维实验 EXP-009 将加入欧氏/双曲、有锥/无锥成对控制，但其结果尚未产生。

## 变更记录

- 2026-10-17：初始早停结果保存，随后补足统一十轮预算并重算报告与 bootstrap。
- 2026-10-20：补录；当前主表使用完整预算版本。
- 2026-10-20：补入已有训练对比 PNG/PDF 与机器可读汇总，供本页和 EXP-004 共用。
- 2026-10-20：展开微调前后全部六方向 R@1/5/10 与 MedR，补充起始 checkpoint、冻结评测及 epoch 0 验证来源说明；原始数值不变。
