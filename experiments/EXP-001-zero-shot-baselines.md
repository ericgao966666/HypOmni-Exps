# 历史零样本基线与方法探索

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-001 |
| 项目 | PMRL-minimal-hyperbolic；末节为 Hyperbolic-Omnimodal 的历史 Parent 消融 |
| 状态 | 历史零样本评估已完成；Parent 消融仅完成验证评估 |
| 原零样本报告更新 / 本次补录 | 2026-09-01 / 2026-10-20 |
| Parent 消融日期 | 2026-10-14 |
| 关联实验 | [子集层级初版](EXP-002-subset-pilot.md)、[后来的官方权重冻结迁移](EXP-004-frozen-transfer.md) |

本页汇总早期 baseline、hyperbolic spectral PMRL 及尚未取得全面收益的方法探索。主体纳入 `ZERO_SHOT_COMPLETE_RESULTS.md` 的完整表格，原 EXP-001 的 Parent 消融保留在[文档末尾](#7-历史-parent-消融)，没有另设实验编号。

## 阅读口径

- 本页前六节的 **Ours 是早期 hyperbolic spectral PMRL**，不是 EXP-002 之后的七子集层级模型。这里的本地训练 baseline 也不同于 EXP-004 的官方发布权重直接推理，不能混为同一组对照。
- Video–text 分别保留 Top-50 ITM、Top-20 ITM 与 Stage-1 direct；audio–text 主表采用无 ITM 的 direct retrieval，旧 Top-50 表单独保留。
- 按原始未舍入均值计算，音频 direct 四方向 Ours 为 19.175%，PMRL 为 23.3333%，相差约 **−4.16 pp**。原报告的 **−0.61 pp 只对应旧音频 Top-50 协议**；本页在总体结论中明确了这一区别，原表数字不变。
- 原实验协议明确披露 Ours 曾使用四个视频测试集调参，因此这些结果不能描述为未触碰测试集的泛化验证。外部方法采用各自官方实现和原生设置，属于方法参考，不是对 PMRL 的单变量消融。

[原始完整报告快照](../results/EXP-001/2026-10-20/zero_shot/ZERO_SHOT_COMPLETE_RESULTS.md) · [原始执行协议说明](../results/EXP-001/2026-10-20/zero_shot/MAIN_RESULT_PROTOCOL.md) · [机器可读协议](../results/EXP-001/2026-10-20/zero_shot/protocol.json)

快速定位：[视频 Top-50](#video-top50) · [视频 Top-20](#video-top20) · [视频 Stage-1](#video-stage1) · [音频 direct](#audio-direct) · [历史 Parent 消融](#7-历史-parent-消融)

原报告更新时间：2026-09-01。本节中的“当前”指该历史报告时点。

本文档汇总当前已经完成的 video–text 和 audio–text zero-shot retrieval
实验。所有表格均报告 Recall@1（R@1，%）。Video–text 分别报告最终
Stage-1 checkpoint 的 Top-50 ITM rerank、Top-20 ITM rerank 和纯 Stage-1；
新增的 audio–text 主表只使用 Stage-1 direct retrieval，明确不运行 ITM。

## 1. 实验范围与完成情况

### 1.1 方法

- VAST
- GRAM
- PMRL
- HyperGRAM
- TRIANGLE
- Ours（hyperbolic spectral PMRL）

### 1.2 数据集

Video–text：

- MSR-VTT
- DiDeMo
- ActivityNet
- VATEX

Audio–text：

- AudioCaps
- ClothoV2

### 1.3 Seed 与 checkpoint 约定

- PMRL、Ours、GRAM、HyperGRAM 和 TRIANGLE 均已完成 seed 42、50、123，
  表格报告三次实验的 `mean ± sample std`。
- VAST 使用官方发布的 checkpoint，本地记录为 seed 50，因此只有一个结果；
  VAST 单次结果不能用于估计随机方差。
- GRAM、HyperGRAM 和 TRIANGLE 使用各自官方 GitHub 仓库代码进行训练和评估，
  没有在 PMRL 中重新实现其模型与 loss。
- PMRL 与 Ours 使用配对配置，除目标模型结构和 hyperbolic spectral loss 外，
  数据、训练和评估协议保持一致。
- VATEX 的 VAST evaluation 已修复为与其他方法一致的数据与 caption 处理方式；
  本文中的 VAST VATEX V→T 正确结果为 `72.80`，不使用此前的异常高值。

原有 video–text 与历史 Top-50 audio–text zero-shot 组合均已完成。新增实验中，
PMRL `tau1=0.1` 与 `tau1=0.07` 的三 seed 训练与 video–text 评估、PMRL/Ours 的纯
audio–text Stage-1 direct 三 seed 评估，以及四个 external baseline 的纯
audio–text Stage-1 direct 评估均已完成。

<a id="video-top50"></a>

## 2. Video–text zero-shot Top-50 ITM 结果

表中每个数据集按 `T→V / V→T` 排列。除 VAST 外，数值均为三次实验的
`mean ± sample std`。所有方法对比表按每个数据集的各方向分别标记：**最优值加粗**、
<ins>次优值加下划线</ins>；按展示均值排名，并列使用相同标记，次优指第二个不同的值。

| 方法 | Seeds | MSR-VTT T→V / V→T | DiDeMo T→V / V→T | ActivityNet T→V / V→T | VATEX T→V / V→T |
|---|---:|---:|---:|---:|---:|
| VAST | 1 | 49.80 / 49.50 | 48.60 / 48.10 | 51.30 / 49.00 | 76.20 / 72.80 |
| GRAM | 3 | 54.37 ± 0.51 / 51.23 ± 0.45 | 51.40 ± 0.87 / 48.40 ± 0.44 | 53.80 ± 0.17 / 47.67 ± 0.76 | 77.37 ± 0.71 / 73.43 ± 0.45 |
| PMRL | 3 | 55.40 ± 0.44 / 52.37 ± 0.55 | 54.17 ± 0.32 / 51.67 ± 0.46 | <ins>56.20 ± 0.17</ins> / 50.27 ± 0.42 | 79.57 ± 0.50 / 74.67 ± 0.40 |
| PMRL (`tau1=0.1`) | 3 | <ins>55.67 ± 0.55</ins> / 51.83 ± 0.45 | <ins>54.40 ± 0.30</ins> / 51.83 ± 0.40 | **56.40 ± 0.17** / 49.93 ± 0.60 | **79.77 ± 0.21** / 74.83 ± 0.32 |
| PMRL (`tau1=0.07`) | 3 | 55.47 ± 0.31 / 52.20 ± 0.56 | **54.70 ± 0.20** / 51.93 ± 0.23 | <ins>56.20 ± 0.10</ins> / 50.17 ± 0.58 | <ins>79.73 ± 0.35</ins> / **75.10 ± 0.26** |
| HyperGRAM | 3 | 55.50 ± 0.61 / <ins>52.67 ± 0.12</ins> | 51.80 ± 0.82 / 50.30 ± 0.40 | 54.27 ± 0.31 / 48.53 ± 0.15 | 78.60 ± 0.61 / <ins>75.07 ± 0.61</ins> |
| TRIANGLE | 3 | 49.67 ± 0.49 / 50.30 ± 0.35 | 46.87 ± 0.15 / 49.13 ± 1.31 | 49.63 ± 1.06 / 49.07 ± 0.67 | 77.23 ± 0.38 / 72.90 ± 0.46 |
| Ours (`entailment=0`) | 3 | 55.10 ± 0.66 / 52.53 ± 0.51 | 53.77 ± 0.06 / 51.80 ± 0.10 | 55.83 ± 0.25 / **51.07 ± 0.06** | 79.30 ± 0.30 / 74.33 ± 0.45 |
| **Ours** | 3 | 55.27 ± 0.46 / <ins>52.67 ± 0.60</ins> | 53.77 ± 0.29 / **52.17 ± 0.15** | 55.93 ± 0.12 / <ins>51.03 ± 0.06</ins> | 79.40 ± 0.20 / 74.07 ± 0.47 |
| Ours (`entailment=0.2`) | 3 | 55.33 ± 0.40 / **52.80 ± 0.53** | 53.83 ± 0.06 / <ins>52.03 ± 0.21</ins> | 55.97 ± 0.06 / 51.00 ± 0.00 | 79.30 ± 0.36 / 74.17 ± 0.42 |
| Ours (`entailment=0.3`) | 3 | **55.70 ± 0.30** / <ins>52.67 ± 0.47</ins> | 54.10 ± 0.62 / 51.93 ± 0.15 | 56.03 ± 0.12 / 50.97 ± 0.15 | 79.37 ± 0.31 / 74.17 ± 0.23 |
| Ours (`entailment=0.5`) | 3 | 55.53 ± 0.45 / <ins>52.67 ± 0.21</ins> | 54.10 ± 0.30 / 51.37 ± 0.40 | 55.77 ± 0.15 / 50.73 ± 0.12 | 78.73 ± 0.15 / 73.97 ± 0.12 |

### 2.1 Ours 相对 PMRL 的变化

正数表示 Ours 更好，负数表示 PMRL 更好。

| 数据集 | T→V ΔR@1 | V→T ΔR@1 |
|---|---:|---:|
| MSR-VTT | -0.13 | +0.30 |
| DiDeMo | -0.40 | +0.50 |
| ActivityNet | -0.27 | +0.77 |
| VATEX | -0.17 | -0.60 |

八个 video–text 方向的简单平均 R@1：

- PMRL：59.29
- Ours：59.29
- Ours − PMRL：约 0.00

### 2.2 Video–text 结果解读

- Ours 在 MSR-VTT、DiDeMo 和 ActivityNet 的 V→T 上分别提高 0.30、0.50
  和 0.77，其中 ActivityNet V→T 的提升最明显。
- Ours 在四个数据集的 T→V 上均略低于 PMRL，差距为 0.13–0.40。
- VATEX 是当前相对较弱的一项：Ours 的 T→V 低 0.17，V→T 低 0.60。
- 综合八个方向，Ours 与 PMRL 的平均值基本完全相同。因此当前结果支持
  “部分 V→T 方向的平均值更高”，但不支持“zero-shot 全面超过 PMRL”。
- HyperGRAM 在 MSR-VTT 两个方向以及 VATEX V→T 上很强；它是除 PMRL 外
  最需要重点比较的方法。

<a id="video-top20"></a>

### 2.3 Video–text Top-20 完整 retrieval

本表与 Top-50 主表复用完全相同的 checkpoint、数据和方法原生 Stage-1 候选
分数，唯一变化是把 `itm_rerank_num` 从 50 改为 20。保存过逐样本 Top-50
分数的 PMRL/Ours 配置从同一分数包按原生 CUDA `topk` 精确重算；没有保存
逐样本分数的 official-repository baseline 和 entailment 消融则使用原 checkpoint
补做原生 Top-20 evaluation。这样不会把历史 checkpoint 或不同数据协议混入表中。

<!-- VIDEO_TOP20_TABLE_START -->
| 方法 | Seeds | MSR-VTT T→V / V→T | DiDeMo T→V / V→T | ActivityNet T→V / V→T | VATEX T→V / V→T |
|---|---:|---:|---:|---:|---:|
| VAST | 1 | 48.40 / 48.30 | 47.40 / 46.30 | 50.40 / 48.00 | 74.10 / 71.60 |
| GRAM | 3 | 53.10 ± 0.46 / 50.83 ± 0.76 | 46.30 ± 0.60 / 44.27 ± 0.81 | 51.40 ± 0.17 / 45.17 ± 0.61 | 77.03 ± 0.70 / 72.83 ± 0.51 |
| PMRL | 3 | <ins>55.53 ± 0.45</ins> / 51.97 ± 0.51 | 53.07 ± 0.40 / <ins>51.10 ± 0.44</ins> | 55.67 ± 0.06 / 50.00 ± 0.10 | <ins>79.67 ± 0.57</ins> / 74.53 ± 0.45 |
| PMRL (`tau1=0.1`) | 3 | 55.47 ± 0.47 / 51.57 ± 0.35 | 52.37 ± 0.29 / 49.90 ± 0.62 | 55.17 ± 0.21 / 48.93 ± 0.45 | **79.70 ± 0.20** / <ins>74.70 ± 0.46</ins> |
| PMRL (`tau1=0.07`) | 3 | **55.60 ± 0.17** / 51.83 ± 0.75 | 52.53 ± 0.06 / **51.30 ± 0.10** | 55.37 ± 0.12 / 49.60 ± 0.53 | <ins>79.67 ± 0.38</ins> / **74.93 ± 0.23** |
| HyperGRAM | 3 | 54.93 ± 1.16 / 51.80 ± 0.46 | 48.90 ± 0.75 / 47.03 ± 0.25 | 53.17 ± 0.23 / 45.80 ± 0.36 | 77.73 ± 0.49 / 74.20 ± 0.92 |
| TRIANGLE | 3 | 47.03 ± 0.85 / 50.20 ± 0.69 | 40.87 ± 0.32 / 47.67 ± 0.60 | 44.73 ± 0.81 / 48.27 ± 0.58 | 73.87 ± 0.15 / 72.83 ± 0.51 |
| Ours (`entailment=0`) | 3 | 54.90 ± 0.79 / 51.83 ± 0.25 | <ins>53.27 ± 0.21</ins> / 50.53 ± 0.15 | 55.53 ± 0.25 / **50.67 ± 0.06** | 79.13 ± 0.25 / 74.30 ± 0.46 |
| **Ours** (`entailment=0.1`) | 3 | 54.97 ± 0.64 / <ins>52.10 ± 0.44</ins> | 53.20 ± 0.26 / 51.00 ± 0.10 | 55.57 ± 0.12 / <ins>50.63 ± 0.12</ins> | 79.23 ± 0.21 / 74.03 ± 0.32 |
| Ours (`entailment=0.2`) | 3 | 55.23 ± 0.40 / **52.27 ± 0.15** | 53.10 ± 0.26 / 50.77 ± 0.23 | <ins>55.73 ± 0.15</ins> / 50.47 ± 0.06 | 79.17 ± 0.35 / 74.17 ± 0.35 |
| Ours (`entailment=0.3`) | 3 | 55.47 ± 0.49 / 51.93 ± 0.29 | **53.30 ± 0.46** / 50.53 ± 0.21 | **55.83 ± 0.15** / 50.47 ± 0.12 | 79.03 ± 0.21 / 74.17 ± 0.23 |
| Ours (`entailment=0.5`) | 3 | 55.00 ± 0.26 / 51.80 ± 0.35 | 53.00 ± 0.10 / 49.30 ± 0.70 | 55.00 ± 0.20 / 50.03 ± 0.21 | 78.40 ± 0.20 / 73.87 ± 0.06 |

当前写入 12/12 个完整方法/配置行；仅在该行的全部协议 seeds 完成后加入表格。
<!-- VIDEO_TOP20_TABLE_END -->

<a id="video-stage1"></a>

### 2.4 Video–text Stage-1 direct retrieval（无 ITM）

本节只使用模型原生 Stage-1 retrieval score，不构造或运行 ITM reranker。
额外 entailment weight 的行只会在 seeds 42、50、123 全部完成后写入。
对 GRAM、HyperGRAM 和 TRIANGLE，这里使用各自 Top-50 候选生成前的原生
`ret_area_forward/backard` 双向分数，而不是额外改用 cosine score。

<!-- VIDEO_STAGE1_DIRECT_TABLE_START -->
| 方法 | Seeds | MSR-VTT T→V / V→T | DiDeMo T→V / V→T | ActivityNet T→V / V→T | VATEX T→V / V→T |
|---|---:|---:|---:|---:|---:|
| VAST | 1 | 31.60 / 32.40 | 30.60 / 32.40 | 31.00 / 27.60 | 50.10 / 44.60 |
| GRAM | 3 | 34.77 ± 0.49 / 35.93 ± 0.25 | 22.97 ± 1.12 / 21.57 ± 0.21 | 26.33 ± 1.25 / 23.30 ± 0.17 | 48.53 ± 1.99 / 54.27 ± 0.70 |
| PMRL | 3 | 43.50 ± 0.26 / 42.13 ± 0.90 | 35.77 ± 0.65 / 35.47 ± 0.45 | 40.83 ± 0.06 / 35.03 ± 0.46 | 68.97 ± 0.23 / 65.10 ± 0.66 |
| PMRL (`tau1=0.1`) | 3 | 41.00 ± 0.40 / 38.27 ± 0.46 | 28.77 ± 0.40 / 28.20 ± 0.26 | 35.03 ± 0.21 / 31.07 ± 0.23 | 62.57 ± 0.23 / 58.00 ± 0.30 |
| PMRL (`tau1=0.07`) | 3 | 42.17 ± 0.12 / 40.97 ± 0.59 | 32.83 ± 0.42 / 32.53 ± 0.65 | 38.40 ± 0.10 / 33.37 ± 0.06 | 66.40 ± 0.17 / 62.33 ± 0.06 |
| HyperGRAM | 3 | 38.93 ± 0.81 / 37.30 ± 0.56 | 25.87 ± 0.95 / 25.80 ± 0.17 | 31.40 ± 0.61 / 24.77 ± 0.46 | 57.93 ± 0.61 / 53.63 ± 0.15 |
| TRIANGLE | 3 | 25.90 ± 1.00 / 40.00 ± 0.30 | 15.80 ± 0.66 / 31.70 ± 0.46 | 17.23 ± 0.31 / 32.87 ± 0.42 | 39.40 ± 0.61 / 64.27 ± 0.31 |
| Ours (`entailment=0`) | 3 | 43.77 ± 0.49 / <ins>42.57 ± 0.21</ins> | 35.57 ± 0.38 / 35.73 ± 0.15 | 41.17 ± 0.55 / **35.33 ± 0.35** | **69.87 ± 0.21** / **66.47 ± 0.25** |
| **Ours** (`entailment=0.1`) | 3 | 43.80 ± 0.62 / **42.70 ± 0.46** | 35.77 ± 0.42 / <ins>35.80 ± 0.17</ins> | 41.37 ± 0.51 / <ins>35.27 ± 0.29</ins> | <ins>69.53 ± 0.23</ins> / <ins>66.20 ± 0.36</ins> |
| Ours (`entailment=0.2`) | 3 | **44.17 ± 0.31** / 42.40 ± 0.53 | **36.03 ± 0.42** / **35.93 ± 0.57** | **41.50 ± 0.80** / **35.33 ± 0.21** | 69.27 ± 0.23 / 65.67 ± 0.61 |
| Ours (`entailment=0.3`) | 3 | <ins>43.83 ± 0.15</ins> / 41.40 ± 0.30 | <ins>35.83 ± 0.51</ins> / 35.30 ± 0.17 | <ins>41.40 ± 0.50</ins> / 34.90 ± 0.20 | 68.80 ± 0.20 / 65.17 ± 0.40 |
| Ours (`entailment=0.5`) | 3 | 43.07 ± 0.12 / 38.47 ± 0.45 | 35.13 ± 1.08 / 31.17 ± 0.38 | 37.47 ± 0.40 / 32.70 ± 0.10 | 65.00 ± 0.52 / 61.87 ± 0.38 |
<!-- VIDEO_STAGE1_DIRECT_TABLE_END -->

<a id="audio-direct"></a>

## 3. Audio–text Stage-1 direct retrieval（无 ITM）

AudioCaps 与 ClothoV2 均统一为纯 `ret%ta`。评估器在输出原生 Stage-1
相似度的双向指标后立即返回，不构造也不运行 ITM reranker。AudioCaps 不再使用
旧实验中的 `ret%tva` 视频–音频联合候选。

<!-- AUDIO_STAGE1_DIRECT_TABLE_START -->
| 方法 | Seeds | AudioCaps T→A / A→T | ClothoV2 T→A / A→T |
|---|---:|---:|---:|
| VAST | 1 | <ins>30.80</ins> / **31.80** | <ins>15.40</ins> / <ins>14.00</ins> |
| GRAM | 3 | 22.37 ± 0.86 / 22.43 ± 1.37 | 13.30 ± 0.69 / 10.23 ± 0.85 |
| PMRL | 3 | **31.37 ± 0.93** / <ins>31.10 ± 0.30</ins> | **16.10 ± 0.30** / **14.77 ± 0.12** |
| HyperGRAM | 3 | 24.30 ± 0.61 / 23.50 ± 1.84 | 13.60 ± 0.30 / 10.63 ± 0.81 |
| TRIANGLE | 3 | 23.70 ± 0.70 / 27.77 ± 0.86 | 14.57 ± 0.61 / 12.70 ± 0.87 |
| **Ours** | 3 | 27.53 ± 0.90 / 23.83 ± 0.57 | 14.83 ± 0.72 / 10.50 ± 0.17 |
<!-- AUDIO_STAGE1_DIRECT_TABLE_END -->

这里的 PMRL、Ours、GRAM、HyperGRAM 与 TRIANGLE 均已完成 seed 42、50、123，
报告 `mean ± sample std`。VAST 使用官方发布 checkpoint，因此报告一次确定性
评估结果，不能据此估计随机方差。表内没有使用部分运行结果。

## 4. 历史 Audio–text Top-50 结果（旧协议，不作为新主表）

本节保留此前结果以便追溯，但 AudioCaps 使用的是 `ret%tva` 且包含 Top-50
ITM，因此不能解释为纯 audio–text Stage-1 direct retrieval。

表中每个数据集按 `T→A / A→T` 排列。除 VAST 外，数值均为三次实验的
`mean ± sample std`，排名标记沿用最优值加粗、次优值加下划线；各方向分别排名。

| 方法 | Seeds | AudioCaps T→A / A→T | ClothoV2 T→A / A→T |
|---|---:|---:|---:|
| VAST | 1 | <ins>33.20</ins> / <ins>33.50</ins> | 14.70 / 14.50 |
| GRAM | 3 | 32.03 ± 1.05 / 33.43 ± 0.40 | 16.50 ± 0.53 / <ins>15.63 ± 0.86</ins> |
| PMRL | 3 | 32.83 ± 0.93 / 32.13 ± 0.91 | **17.20 ± 0.46** / 15.50 ± 0.62 |
| HyperGRAM | 3 | **34.70 ± 1.61** / **36.10 ± 0.35** | 16.83 ± 0.81 / 15.30 ± 0.26 |
| TRIANGLE | 3 | 30.00 ± 0.78 / 32.30 ± 0.79 | <ins>16.93 ± 0.76</ins> / **15.77 ± 0.67** |
| **Ours** | 3 | 31.67 ± 1.15 / 31.77 ± 0.25 | <ins>16.93 ± 0.51</ins> / 14.87 ± 0.76 |

### 4.1 Ours 相对 PMRL 的变化

| 数据集 | T→A ΔR@1 | A→T ΔR@1 |
|---|---:|---:|
| AudioCaps | -1.17 | -0.37 |
| ClothoV2 | -0.27 | -0.63 |

四个 audio–text 方向的简单平均 R@1：

- PMRL：24.42
- Ours：23.81
- Ours − PMRL：-0.61

### 4.2 历史 Audio–text 结果解读

- Ours 在四个 audio–text 方向上均未超过 PMRL。
- AudioCaps T→A 的下降最大，为 1.17；其余方向下降 0.27–0.63。
- HyperGRAM 在 AudioCaps 两个方向均明显最好。
- 当前 hyperbolic spectral 方法的收益更偏向部分 video-to-text retrieval，
  尚未迁移到 audio–text retrieval。

## 5. 总体结论

1. 当前 zero-shot 实验已经具备完整的多方法、多数据集和多 seed 结果，
   可以用于分析，但 Ours 尚未形成全面领先。
2. Video–text Top-50 ITM 主表中，Ours 相对 PMRL 的主要优势集中在 V→T，尤其是
   ActivityNet；T→V 则在所有数据集上小幅下降。
3. 八个 video–text Top-50 ITM 方向的平均 R@1 与 PMRL 基本相同，说明当前模块更多是
   改变了双向检索之间的性能分布，而不是提高整体平均水平。
4. 纯 audio–text Stage-1 direct 主表中，Ours 四方向平均低于 PMRL 约 4.16 pp
   （按机器结果的未舍入均值计算）。旧 Top-50 协议的差值为约 0.61 pp，
   仅适用于第 4 节。两套协议均不支持跨模态、跨数据集全面提升。
5. 论文表述应优先使用逐方向结果和统计波动，避免只选择有利数据集；同时应
   重点分析双曲 spectral loss 为什么更有利于 V→T，以及 VATEX 和音频任务
   没有受益的原因。
6. 在原报告的 2026-09-01 时点，finetune 主实验仍需独立完成，不能由本页
   zero-shot 结果推断。之后的 MSRVTT 子集模型微调另见 [EXP-006](EXP-006-msrvtt-finetune.md)，
   模型与协议不同，不合并进本页的历史主表。

## 6. 原始结果与汇总文件

主输出目录：

```text
/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/main_results_vast86707_20260823
```

汇总文件：

- PMRL/Ours video–text Markdown：
  [paired_zeroshot.md](../results/EXP-001/2026-10-20/zero_shot/paired_zeroshot.md)
- PMRL/Ours video–text JSON：
  [paired_zeroshot.json](../results/EXP-001/2026-10-20/zero_shot/paired_zeroshot.json)
- VAST/GRAM/HyperGRAM/TRIANGLE video–text JSON：
  [external_local.json](../results/EXP-001/2026-10-20/zero_shot/external_local.json)
- PMRL/Ours audio–text JSON：
  [paired_audio_zeroshot.json](../results/EXP-001/2026-10-20/zero_shot/paired_audio_zeroshot.json)
- VAST/GRAM/HyperGRAM/TRIANGLE audio–text JSON：
  [external_audio_zeroshot.json](../results/EXP-001/2026-10-20/zero_shot/external_audio_zeroshot.json)
- PMRL/Ours 纯 audio–text Stage-1 direct JSON：
  [paired_audio_stage1_direct.json](../results/EXP-001/2026-10-20/zero_shot/paired_audio_stage1_direct.json)
- VAST/GRAM/HyperGRAM/TRIANGLE 纯 audio–text Stage-1 direct JSON：
  [external_audio_stage1_direct.json](../results/EXP-001/2026-10-20/zero_shot/external_audio_stage1_direct.json)
- PMRL `tau1=0.1` 三 seed JSON：[pmrl_tau1_0p1.json](../results/EXP-001/2026-10-20/zero_shot/pmrl_tau1_0p1.json)
- PMRL `tau1=0.07` 三 seed JSON：[pmrl_tau1_0p07.json](../results/EXP-001/2026-10-20/zero_shot/pmrl_tau1_0p07.json)
- Video–text Top-20 三 seed JSON：[video_top20.json](../results/EXP-001/2026-10-20/zero_shot/video_top20.json)

逐 seed 指标位于：

```text
zeroshot/<method>/seed-<seed>/metrics.json
external/<method>/zeroshot/seed-<seed>/metrics.json
audio_zeroshot/<method>/seed-<seed>/metrics.json
external/<method>/audio_zeroshot/seed-<seed>/metrics.json
audio_stage1_direct/<method>/seed-<seed>/metrics.json
external/<method>/audio_stage1_direct/seed-<seed>/metrics.json
tau1_0p1/zeroshot/pmrl/seed-<seed>/metrics.json
tau1_0p07/zeroshot/pmrl/seed-<seed>/metrics.json
top20_cached/<method>/seed-<seed>/metrics.json
external/<method>/zeroshot_top20/seed-<seed>/metrics.json
```

Top-20 entailment 消融的逐 seed 指标位于：

```text
/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/minimal_hyperbolic_search_20260821/
eval/top20/<family>/<name>/seed-<seed>/metrics.json
```

其中 `pmrl` 和 `ours` 位于 paired 路径，VAST、GRAM、HyperGRAM 和 TRIANGLE
位于 `external/` 路径。


补充权重消融汇总：[entailment=0.2](../results/EXP-001/2026-10-20/zero_shot/ours_entailment_0p2.json)、[entailment=0.3](../results/EXP-001/2026-10-20/zero_shot/ours_entailment_0p3.json)、[entailment=0.5](../results/EXP-001/2026-10-20/zero_shot/ours_entailment_0p5.json)。原始逐 seed 文件留在源服务器；上述轻量汇总与原报告已纳入[来源及哈希清单](../results/manifest.json)。

## 7. 历史 Parent 消融

本节为原 EXP-001 内容，属于 2026-10-14 的后续探索；其 holdout 结果不加入上面的三种子零样本主表。

| 字段 | 内容 |
|---|---|
| 归属 | EXP-001 历史方法章节，原 EXP-001 主内容 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成验证；无本轮测试集结果 |
| 实验日期 / 最后核对 | 2026-10-14 / 2026-10-20 |
| 后续 | [子集层级初版](EXP-002-subset-pilot.md) |

### 要回答的问题

固定本机 M 配置后，Perron、Text、SVD parent 是否相对 E0 改善检索，并形成有效锥包含？

### 协议与运行

512 维，seed 50，四组各 1,360 步；Perron/Text/SVD 的约束权重为 0.1。主比较是 Perron 对本机 E0。八卡全局 batch 64。本轮属于独立探索，不与服务器 A 的结果直接配对。

精确设置与运行清单见[执行方案](../../Hyperbolic-Omnimodal/experiments/next_steps/SERVER_B_EXECUTION_20261014.md)和[运行目录](../../Hyperbolic-Omnimodal/outputs/server_b_20261014/)。

### 结果

以下均为 holdout R@1，单位 %；ITC 为 Stage-1，ITM 为重排。

| 条件 | ITC | ITM | 音频 |
|---|---:|---:|---:|
| E0 | <ins>41.95</ins> | 54.30 | <ins>4.75</ins> |
| Perron λ=0.1 | 41.70 | <ins>54.45</ins> | 4.70 |
| Text λ=0.1 | 41.80 | **54.60** | **4.80** |
| SVD λ=0.1 | **42.05** | 54.40 | <ins>4.75</ins> |

带蕴含约束的三组锥满足率均为 0%。原始[汇总表](../results/EXP-001/2026-10-20/summary.md)、[结构化结果](../results/EXP-001/2026-10-20/summary.json)、[完成状态](../../Hyperbolic-Omnimodal/outputs/server_b_20261014/controller_status.json)。

### 结论与下一步

检索差异很小，未观察到明确的 parent 构造收益或严格包含成功。单种子验证结果不足以支持稳定优势；测试栏为空，不能当作测试结果。后续转向显式子集关系，见 EXP-002。

### 变更记录

- 2026-10-14：首个 smoke 因 allocator cap 失败；第二个 attempt 调整资源上限后通过，正式四组完成。失败记录保留。
- 2026-10-20：根据现存执行文档与结果补录实验卡。
- 2026-10-20：按用户要求移入零样本基线汇总页末尾；原结果和来源链接完整保留。
