# 官方权重与本地模型的冻结迁移评测

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-004 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成 |
| 实验日期 / 最后核对 | 2026-10-16 至 17 / 2026-10-21 |
| 前序 / 后续 | [子集机制](EXP-003-subset-mechanisms.md) / [迁移诊断](EXP-005-transfer-diagnostics.md)、[MSRVTT 微调](EXP-006-msrvtt-finetune.md) |

## 要回答的问题

官方 VAST、GRAM、PMRL checkpoint 与本地层级模型，在相同输入和检索协议下，各自擅长哪些方向？优势能否迁移到其他数据集？

## 协议

EXP-004 本身只进行已有模型的冻结推理，不使用测试集选模或 ITM。官方三种模型使用原生头与余弦打分；Ours 来自 EXP-003 在 VAST 上完成的 9 对、λ=0.1、seed50 头部训练，使用负测地距离。四种模型的训练历史不同。

VAST 为 2,048 样本；MSRVTT 为音视频齐全的 884 条交集，不是完整 1K。AudioCaps 为可用的 704 条，Clotho 为 1,045 条；音频任务保留每条五个 caption，音频到文本按任一正例最优排名计算。

**Checkpoint 来源更正：当前 VAST 和 MSRVTT 两张表中的 Ours 并非同一个 checkpoint。** 2026-10-21 核对保存的测试命令、特征来源、指标和 checkpoint 元数据后确认：VAST 使用主训练第 30 轮 `last.pt`，MSRVTT 使用第 22 轮 `best.pt`。下面保留原始分数，并明确区分两者。

## 训练细节与模型来源

### 四种方法的来源

| 模型 | 本次使用的来源 | 本地训练范围 |
|---|---|---|
| VAST | 官方发布的 `model_step_204994.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| GRAM | 官方发布的 `gram_model_step_459.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| PMRL | 官方发布的 `pmrl_base.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| Ours | VAST 官方编码器，加上 `minimal9_B1_standard_s50` 的子集头 | 在本地 VAST 划分上训练头部，VAST/MSRVTT 评测使用的具体版本见下表 |

本页不能描述为“四种方法都在相同 VAST 数据上统一训练 30 轮”。以下训练轮数和 steps 仅描述 Ours 的本地头部训练，不包含任何官方预训练成本。

### Ours 的数据与训练范围

- VAST 按来源视频分组划分：训练 **82,611** 条，验证 **2,048** 条，测试 **2,048** 条；同一来源视频不跨这些划分。
- 全局 batch 为 **256**，使用 `drop_last`，每轮处理 322 个完整 batch，即 **322 次梯度更新**。不足一个 batch 的 179 条不进入该轮更新。
- 共享 warmup 冻结骨干、继承的头和全部半径参数，只训练三个新增方向头 TV、TA、TVA；主训练在固定 pooled 特征上训练全部子集方向头和半径参数。**两个阶段都没有更新编码器。**
- 主训练使用 512 维表示、seed50、9 对对比目标及 λ=0.1 的九条锥约束；未在 MSRVTT 上继续训练。本页后续的 MSRVTT 端到端微调属于独立的 [EXP-006](EXP-006-msrvtt-finetune.md)。

数据划分和基础设置见 [base_protocol.json](../results/EXP-004/2026-10-21/training/base_protocol.json)，主训练的实际运行约定见 [main_experiment.json](../results/EXP-004/2026-10-21/training/main_experiment.json) 和 [main_config.json](../results/EXP-004/2026-10-21/training/main_config.json)。基础协议中也保留了其他阶段的参数；本次是否执行、执行多久，以相应完成记录为准。

### 实际训练预算

| 阶段 | Epochs | 梯度更新 steps | 阶段完成记录 |
|---|---:|---:|---|
| 共享 warmup | 8 | 2,576 | [warmup_done.json](../results/EXP-004/2026-10-21/training/warmup_done.json) |
| 后续头部主训练 | 30 | 9,660 | [main_done.json](../results/EXP-004/2026-10-21/training/main_done.json) |
| 本地训练任务合计 | 38 | 12,236 | 两阶段相加，不包含官方 VAST 预训练 |

主训练从共享 warmup 的第 8 轮 `last.pt` 开始，输入文件哈希与运行记录一致。主训练的 epoch/step 从该阶段重新计数；这里的“主训练第 22 轮”不包含前面的 8 轮 warmup。

### VAST 和 MSRVTT 实际评测的 checkpoint

| 评测数据 | Ours checkpoint | 主训练 epoch | 主训练 step | 来源依据 |
|---|---|---:|---:|---|
| VAST 测试集，2,048 条 | `last.pt` | 30 | 9,660 | [测试命令](../results/EXP-004/2026-10-21/training/vast_test_launcher.json)、[头部测试指标](../results/EXP-004/2026-10-21/training/vast_head_test_metrics.json)、[六方向评测结果](../results/EXP-004/2026-10-21/training/vast_ours_metrics.json) |
| MSRVTT 测试集，884 条 | `best.pt` | 22 | 7,084 | [评测记录及 checkpoint 哈希](../results/EXP-004/2026-10-21/training/msrvtt_ours_metrics.json)、[checkpoint 审计](../results/EXP-004/2026-10-21/training/checkpoint_audit.json) |

`best.pt` 由 VAST 验证集的十二方向 macro R@1 选择，第 22 轮达到 29.50846%；主训练仍实际跑满 30 轮。逐轮的 epoch、step 和验证分数见[验证摘要](../results/EXP-004/2026-10-21/training/main_validation_summary.json)。两份 checkpoint 的 epoch、step 和 SHA-256 已从本地文件核对，未上传模型权重。

VAST 原汇总中的 `selection` 字段写着 `validation-selected checkpoint`，但其 `source_features` 指向使用 `last.pt` 生成的测试特征；对应测试命令也明确指定 `last.pt`，且六方向分数与该次测试记录一致。因此本页以这条实际来源链更正描述，保留[原汇总快照](../results/EXP-004/2026-10-21/training/vast_comparison_report.json)供追溯。MSRVTT 记录的 checkpoint 哈希则与第 22 轮 `best.pt` 一致。

这些结果可分别解读，但不能当作严格同 checkpoint 的跨数据集对比；若需要这种比较，应统一 checkpoint 后重新评测。本次只补充来源审计，没有改动分数或重跑评测。

## 结果

表内各指标列的**最优值加粗**，<ins>次优值加下划线</ins>；显示精度下的并列值同样标记。Recall 越高越好，MedR 越低越好；音频表中两个方向分别排名。

### 六方向平均概览

| 模型 | VAST 六方向平均 R@1 % | MSRVTT 六方向平均 R@1 % |
|---|---:|---:|
| VAST | 8.46 | 18.10 |
| GRAM | 12.80 | 17.91 |
| PMRL | <ins>18.33</ins> | **19.97** |
| Ours | **20.52** | <ins>19.19</ins> |

T 表示文本，V 表示视频，A 表示音频。Recall 指标单位均为 %，展示到小数点后两位；CSV 保留原始精度。Macro 为六个方向的算术平均。以下是冻结 checkpoint 的完整检索读数。

### VAST 测试样本集，2,048 条

[下载完整 CSV](../results/EXP-004/2026-10-20/vast_comparison.csv)

#### R@1

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | 27.88 | 13.33 | 2.15 | 2.29 | 2.73 | 2.39 | 8.46 |
| GRAM | 35.21 | 22.75 | 5.62 | 4.20 | 5.03 | 4.00 | 12.80 |
| PMRL | **40.72** | **40.33** | <ins>6.69</ins> | **6.84** | <ins>7.76</ins> | <ins>7.67</ins> | <ins>18.33</ins> |
| Ours | <ins>36.72</ins> | <ins>36.43</ins> | **6.88** | <ins>6.54</ins> | **18.51** | **18.02** | **20.52** |

#### R@5

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | 47.51 | 33.06 | 6.49 | 5.81 | 8.98 | 6.45 | 18.05 |
| GRAM | 57.13 | 42.97 | 14.79 | 11.04 | 13.92 | 12.55 | 25.40 |
| PMRL | **63.57** | **63.38** | <ins>18.12</ins> | <ins>17.04</ins> | <ins>20.31</ins> | <ins>20.51</ins> | <ins>33.82</ins> |
| Ours | <ins>59.77</ins> | <ins>59.81</ins> | **18.95** | **18.80** | **40.33** | **40.04** | **39.62** |

#### R@10

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V | Macro |
|---|---:|---:|---:|---:|---:|---:|---:|
| VAST | 55.62 | 45.02 | 10.30 | 8.64 | 12.50 | 9.33 | 23.57 |
| GRAM | 66.21 | 52.20 | 20.61 | 16.06 | 21.00 | 19.14 | 32.54 |
| PMRL | **71.58** | **71.92** | <ins>25.44</ins> | <ins>24.27</ins> | <ins>29.49</ins> | <ins>29.74</ins> | <ins>42.07</ins> |
| Ours | <ins>68.60</ins> | <ins>69.43</ins> | **27.29** | **26.61** | **50.78** | **51.03** | **48.96** |

#### 中位排名 MedR

数值越低越好；不计算跨方向的平均中位排名。

| 模型 | T→V | V→T | T→A | A→T | V→A | A→V |
|---|---:|---:|---:|---:|---:|---:|
| VAST | 7 | 14 | 408 | 368 | 311 | 320 |
| GRAM | <ins>3</ins> | 9 | 83 | 118 | 75 | 90 |
| PMRL | **2** | **2** | <ins>55</ins> | <ins>59</ins> | <ins>32</ins> | <ins>35</ins> |
| Ours | <ins>3</ins> | <ins>3</ins> | **42** | **43** | **10** | **10** |

### MSRVTT 音视频交集，884 条

[下载完整 CSV](../results/EXP-004/2026-10-20/msrvtt_comparison.csv)

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

本次 MSRVTT 汇总 CSV 未提供 MedR，页面仅展示已保存的 Recall 指标。

### AudioCaps 与 Clotho

| 模型 | AudioCaps T→A / A→T R@1 % | Clotho T→A / A→T R@1 % |
|---|---|---|
| VAST | **32.05** / **42.05** | <ins>16.13</ins> / **20.00** |
| GRAM | 30.28 / 36.08 | 14.45 / 15.79 |
| PMRL | <ins>31.99</ins> / <ins>41.19</ins> | **16.94** / <ins>18.18</ins> |
| Ours | 9.80 / 20.17 | 4.75 / 7.08 |

## 结果文件

结果与每组的审计文件分别位于：

- [VAST 对比 CSV](../results/EXP-004/2026-10-20/vast_comparison.csv)
- [MSRVTT 对比 CSV](../results/EXP-004/2026-10-20/msrvtt_comparison.csv)
- [AudioCaps 与 Clotho 对比 CSV](../results/EXP-004/2026-10-20/audio_comparison.csv)
- [协议与 checkpoint 来源说明](../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/README.md)
- [2026-10-21 训练预算及 checkpoint 来源审计](../results/EXP-004/2026-10-21/training/checkpoint_audit.json)

## 结论与下一步

我们的视频与音频方向较强，文本相关方向的优势不足，音频文本跨域迁移明显下降。VAST 与我们共享冻结 encoder 输出，因此差异位于头部学习和打分阶段，但这不能单独识别锥损失的因果贡献。

VAST cohort 可能与官方预训练数据重叠，不能称为认证零样本；各模型训练史不同，不能称为匹配训练对照。AudioCaps 后续发现一条与训练源重叠，去重诊断见 EXP-005。

## 变更记录

- 2026-10-16 至 17：依次完成 VAST、MSRVTT、AudioCaps 和 Clotho 评测。
- 2026-10-20：补录；与 EXP-003 的十二方向结果分开记录。
- 2026-10-20：展开 VAST 与 MSRVTT 六方向及 macro 的 R@1/5/10，补入 VAST 中位排名，数值由原 CSV 生成。
- 2026-10-20：增加关联 EXP-006 的 MSRVTT 十轮微调曲线、PDF 和选模汇总，明确与本页冻结评测结果的区别。
- 2026-10-20：按用户要求补齐全部三组已有曲线，追加 VAST 头部训练和跨数据集迁移曲线；保留各自来源及指标口径。
- 2026-10-20：按列标记最优与次优值，处理并列和 MedR 的反向排序；原始数字未改变。
- 2026-10-20：按用户要求移除本页关联训练曲线整节；其他实验文档及图表文件保留。
- 2026-10-21：补充模型来源、数据划分、训练范围、8 轮 warmup 与 30 轮主训练预算；纠正“VAST 与 MSRVTT 使用同一个验证最优 checkpoint”的描述，明确 VAST 使用第 30 轮 `last.pt`、MSRVTT 使用第 22 轮 `best.pt`，原结果保留。
