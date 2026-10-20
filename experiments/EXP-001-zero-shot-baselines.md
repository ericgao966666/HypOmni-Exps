# 历史零样本基线与方法探索

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-001 |
| 项目 | PMRL-minimal-hyperbolic；末节为 Hyperbolic-Omnimodal 的历史 Parent 消融 |
| 状态 | 已同步历史零样本、MERU 配对与 HyperGRAM 纯双曲结果；Parent 消融仅完成验证评估 |
| 原零样本报告更新 / 本次同步 | 2026-10-15 / 2026-10-20（UTC） |
| 本次来源 | server-b：`PMRL-minimal-hyperbolic/docs/ZERO_SHOT_COMPLETE_RESULTS.md` |
| Parent 消融日期 | 2026-10-14 |
| 关联实验 | [子集层级初版](EXP-002-subset-pilot.md)、[后来的官方权重冻结迁移](EXP-004-frozen-transfer.md) |

本页汇总早期 baseline、hyperbolic spectral PMRL 及尚未取得全面收益的方法探索。第 1–9 节纳入本机 `ZERO_SHOT_COMPLETE_RESULTS.md` 的完整结果表格，原 EXP-001 的 Parent 消融保留在[文档末尾](#historical-parent)，没有另设实验编号。

## 阅读口径

- 本页零样本部分的 **Ours 是早期 hyperbolic spectral PMRL**，不是 EXP-002 之后的七子集层级模型。这里的本地训练 baseline 也不同于 EXP-004 的官方发布权重直接推理，不能混为同一组对照。
- Video–text 分别保留 Top-50 ITM、Top-20 ITM 与 Stage-1 direct；audio–text 主表采用无 ITM 的 direct retrieval，旧 Top-50 表单独保留。
- 按原始未舍入均值计算，历史三 seed 音频 direct 四方向 Ours 为 19.175%，PMRL 为 23.3333%，相差约 **−4.16 pp**。原报告的 **−0.61 pp 只对应旧音频 Top-50 协议**；本页保留这一口径修正，原表数字不变。
- 原实验协议明确披露 Ours 曾使用四个视频测试集调参，因此这些结果不能描述为未触碰测试集的泛化验证。外部方法采用各自官方实现和原生设置，属于方法参考，不是对 PMRL 的单变量消融。
- 新增 MERU 为单 seed 50 配对实验；HyperGRAM pure 使用 TVA/TVAS 联合候选，调参结果为单 seed、评测集选参。它们不与历史三 seed 结果合并统计或重排前三名。
- 第 2.5 节的 9 月 Mean/SVD parent 与文末 10 月 14 日的 Parent holdout 消融属于不同实验，不合并。

[当前完整报告快照](../results/EXP-001/2026-10-20-server-b/zero_shot/ZERO_SHOT_COMPLETE_RESULTS.md) · [旧版报告（2026-09-01）](../results/EXP-001/2026-10-20/zero_shot/ZERO_SHOT_COMPLETE_RESULTS.md) · [历史执行协议说明](../results/EXP-001/2026-10-20/zero_shot/MAIN_RESULT_PROTOCOL.md) · [历史机器可读协议](../results/EXP-001/2026-10-20/zero_shot/protocol.json) · [来源及哈希](../results/manifest.json)

快速定位：[视频 Top-50](#video-top50) · [视频 Top-20](#video-top20) · [视频 Stage-1](#video-stage1) · [Stage-1 汇总](#stage1-summary) · [音频 direct](#audio-direct) · [MERU 配对](#meru-paired) · [HyperGRAM pure](#hypergram-pure) · [HyperGRAM 调参](#hypergram-tuning) · [历史 Parent 消融](#historical-parent)

原报告更新时间：2026-10-15；本次只同步已有记录，未重跑实验。完整快照逐字节保存，报告中的服务器路径和未收录辅助文档仍为原始来源记录，不代表可跨服务器访问。实验卡保留现有仓库内证据链接；新增章节的原始路径以代码形式列出。第 5 节结论限定为历史三 seed 实验，新增结果按各节协议解释。

本文档汇总当前已经完成的 video–text 和 audio–text zero-shot retrieval
实验。所有表格均报告 Recall@1（R@1，%）。Video–text 分别报告最终
Stage-1 checkpoint 的 Top-50 ITM rerank、Top-20 ITM rerank 和纯 Stage-1；
新增的 audio–text 主表只使用 Stage-1 direct retrieval，明确不运行 ITM。

MERU-style 单 seed 配对实验已列入视频 Top-50、视频 Stage-1 和音频 Stage-1 总表；详细比较口径见第 7 节。

## 1. 实验范围与完成情况

### 1.1 方法

- VAST
- GRAM
- PMRL
- HyperGRAM（hybrid）
- HyperGRAM（pure hyperbolic；目前完成视频 Stage-1／Top-50）
- TRIANGLE
- MERU all-pair（无 entailment / Text parent；单 seed 50）
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
- MERU all-pair 两个版本仅完成 seed 50，采用第 7 节的配对协议；不混入历史三 seed 均值、标准差或前三名标记。Top-20 尚未评测。
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

HyperGRAM pure hyperbolic 已完成 seeds 42、50、123 的四视频数据集 Stage-1 和 Top-50；Top-20 与音频评测尚未运行，下表统一标为“未评测”，不参与统计或排名。

<a id="video-top50"></a>

## 2. Video–text zero-shot 结果

本节主表为 Top-50 ITM 重排结果，每个数据集按 `T→V / V→T` 排列。除 VAST 和 MERU all-pair 外，数值均为三次实验的
`mean ± sample std`。所有主结果表统一使用：**第一名粗体**、<u>第二名下划线</u>、
*第三名斜体*；并列结果使用相同标记。

| 方法 | Seeds | MSR-VTT T→V / V→T | DiDeMo T→V / V→T | ActivityNet T→V / V→T | VATEX T→V / V→T |
|---|---:|---:|---:|---:|---:|
| VAST | 1 | 49.80 / 49.50 | 48.60 / 48.10 | 51.30 / 49.00 | 76.20 / 72.80 |
| GRAM | 3 | 54.37 ± 0.51 / 51.23 ± 0.45 | 51.40 ± 0.87 / 48.40 ± 0.44 | 53.80 ± 0.17 / 47.67 ± 0.76 | 77.37 ± 0.71 / 73.43 ± 0.45 |
| PMRL | 3 | 55.40 ± 0.44 / 52.37 ± 0.55 | *54.17 ± 0.32* / 51.67 ± 0.46 | <u>56.20 ± 0.17</u> / 50.27 ± 0.42 | *79.57 ± 0.50* / 74.67 ± 0.40 |
| PMRL (`tau1=0.1`) | 3 | <u>55.67 ± 0.55</u> / 51.83 ± 0.45 | <u>54.40 ± 0.30</u> / 51.83 ± 0.40 | **56.40 ± 0.17** / 49.93 ± 0.60 | **79.77 ± 0.21** / *74.83 ± 0.32* |
| PMRL (`tau1=0.07`) | 3 | 55.47 ± 0.31 / 52.20 ± 0.56 | **54.70 ± 0.20** / *51.93 ± 0.23* | <u>56.20 ± 0.10</u> / 50.17 ± 0.58 | <u>79.73 ± 0.35</u> / **75.10 ± 0.26** |
| HyperGRAM (hybrid) | 3 | 55.50 ± 0.61 / <u>52.67 ± 0.12</u> | 51.80 ± 0.82 / 50.30 ± 0.40 | 54.27 ± 0.31 / 48.53 ± 0.15 | 78.60 ± 0.61 / <u>75.07 ± 0.61</u> |
| HyperGRAM (pure hyperbolic)† | 3 | 45.43 ± 2.90 / 51.17 ± 0.21 | 47.97 ± 0.21 / 48.80 ± 0.26 | 49.30 ± 0.82 / 48.37 ± 0.71 | 56.00 ± 15.89 / 74.33 ± 0.31 |
| TRIANGLE | 3 | 49.67 ± 0.49 / 50.30 ± 0.35 | 46.87 ± 0.15 / 49.13 ± 1.31 | 49.63 ± 1.06 / 49.07 ± 0.67 | 77.23 ± 0.38 / 72.90 ± 0.46 |
| Ours (`entailment=0`) | 3 | 55.10 ± 0.66 / *52.53 ± 0.51* | 53.77 ± 0.06 / 51.80 ± 0.10 | 55.83 ± 0.25 / **51.07 ± 0.06** | 79.30 ± 0.30 / 74.33 ± 0.45 |
| **Ours** | 3 | 55.27 ± 0.46 / <u>52.67 ± 0.60</u> | 53.77 ± 0.29 / **52.17 ± 0.15** | 55.93 ± 0.12 / <u>51.03 ± 0.06</u> | 79.40 ± 0.20 / 74.07 ± 0.47 |
| Ours (`entailment=0.2`) | 3 | 55.33 ± 0.40 / **52.80 ± 0.53** | 53.83 ± 0.06 / <u>52.03 ± 0.21</u> | 55.97 ± 0.06 / *51.00 ± 0.00* | 79.30 ± 0.36 / 74.17 ± 0.42 |
| Ours (`entailment=0.3`) | 3 | **55.70 ± 0.30** / <u>52.67 ± 0.47</u> | 54.10 ± 0.62 / *51.93 ± 0.15* | *56.03 ± 0.12* / 50.97 ± 0.15 | 79.37 ± 0.31 / 74.17 ± 0.23 |
| Ours (`entailment=0.5`) | 3 | *55.53 ± 0.45* / <u>52.67 ± 0.21</u> | 54.10 ± 0.30 / 51.37 ± 0.40 | 55.77 ± 0.15 / 50.73 ± 0.12 | 78.73 ± 0.15 / 73.97 ± 0.12 |
| MERU all-pair，无 entailment‡ | 1 | 55.3 / 53.2 | 54.5 / 52.1 | 55.7 / 50.0 | 79.4 / 75.0 |
| MERU all-pair，Text parent‡ | 1 | 54.8 / 52.0 | 54.0 / 51.3 | 55.8 / 50.0 | 79.1 / 73.8 |

† HyperGRAM pure hyperbolic 使用 2026-10-10 的当前媒体与 first-caption manifests，以及官方 TVA/TVAS 联合候选；该行按 **T→D / D→T** 理解，D 是视频实例的联合模态候选。与历史行并列供方法级参考，不视作仅几何变化的配对实验，也不纳入前三名格式标记。原 HyperGRAM 行为 hybrid。协议、逐 seed 结果和来源见第 8 节。

‡ MERU all-pair 为 2026-09-29 的 seed-50 结果，使用旧方向—半径映射、三对测地 InfoNCE，并保留 0.1 ITM；Text parent 另加 0.1 entailment（T→V、T→A）。Stage-1 为 TV-only 候选，ITM 按评测任务可使用音频/字幕。与历史三 seed 行并列供参考，不纳入前三名标记；同协议 PMRL/双曲谱对照见第 7 节。

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
| PMRL | 3 | <u>55.53 ± 0.45</u> / *51.97 ± 0.51* | 53.07 ± 0.40 / <u>51.10 ± 0.44</u> | *55.67 ± 0.06* / 50.00 ± 0.10 | <u>79.67 ± 0.57</u> / *74.53 ± 0.45* |
| PMRL (`tau1=0.1`) | 3 | *55.47 ± 0.47* / 51.57 ± 0.35 | 52.37 ± 0.29 / 49.90 ± 0.62 | 55.17 ± 0.21 / 48.93 ± 0.45 | **79.70 ± 0.20** / <u>74.70 ± 0.46</u> |
| PMRL (`tau1=0.07`) | 3 | **55.60 ± 0.17** / 51.83 ± 0.75 | 52.53 ± 0.06 / **51.30 ± 0.10** | 55.37 ± 0.12 / 49.60 ± 0.53 | <u>79.67 ± 0.38</u> / **74.93 ± 0.23** |
| HyperGRAM (hybrid) | 3 | 54.93 ± 1.16 / 51.80 ± 0.46 | 48.90 ± 0.75 / 47.03 ± 0.25 | 53.17 ± 0.23 / 45.80 ± 0.36 | 77.73 ± 0.49 / 74.20 ± 0.92 |
| HyperGRAM (pure hyperbolic)† | — | 未评测 | 未评测 | 未评测 | 未评测 |
| TRIANGLE | 3 | 47.03 ± 0.85 / 50.20 ± 0.69 | 40.87 ± 0.32 / 47.67 ± 0.60 | 44.73 ± 0.81 / 48.27 ± 0.58 | 73.87 ± 0.15 / 72.83 ± 0.51 |
| Ours (`entailment=0`) | 3 | 54.90 ± 0.79 / 51.83 ± 0.25 | <u>53.27 ± 0.21</u> / 50.53 ± 0.15 | 55.53 ± 0.25 / **50.67 ± 0.06** | 79.13 ± 0.25 / 74.30 ± 0.46 |
| **Ours** (`entailment=0.1`) | 3 | 54.97 ± 0.64 / <u>52.10 ± 0.44</u> | *53.20 ± 0.26* / *51.00 ± 0.10* | 55.57 ± 0.12 / <u>50.63 ± 0.12</u> | *79.23 ± 0.21* / 74.03 ± 0.32 |
| Ours (`entailment=0.2`) | 3 | 55.23 ± 0.40 / **52.27 ± 0.15** | 53.10 ± 0.26 / 50.77 ± 0.23 | <u>55.73 ± 0.15</u> / *50.47 ± 0.06* | 79.17 ± 0.35 / 74.17 ± 0.35 |
| Ours (`entailment=0.3`) | 3 | *55.47 ± 0.49* / 51.93 ± 0.29 | **53.30 ± 0.46** / 50.53 ± 0.21 | **55.83 ± 0.15** / *50.47 ± 0.12* | 79.03 ± 0.21 / 74.17 ± 0.23 |
| Ours (`entailment=0.5`) | 3 | 55.00 ± 0.26 / 51.80 ± 0.35 | 53.00 ± 0.10 / 49.30 ± 0.70 | 55.00 ± 0.20 / 50.03 ± 0.21 | 78.40 ± 0.20 / 73.87 ± 0.06 |

当前写入 12/12 个已有完整方法/配置结果行，另列 HyperGRAM pure hyperbolic 未评测占位行；只有全部协议 seeds 完成的数值行参与汇总。
<!-- VIDEO_TOP20_TABLE_END -->

† HyperGRAM pure hyperbolic 尚无本表对应的评测结果；“未评测”不是零分，Seeds 列的“—”表示尚无完成该评测的 seed，不代表未训练。

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
| PMRL | 3 | 43.50 ± 0.26 / 42.13 ± 0.90 | *35.77 ± 0.65* / 35.47 ± 0.45 | 40.83 ± 0.06 / *35.03 ± 0.46* | 68.97 ± 0.23 / 65.10 ± 0.66 |
| PMRL (`tau1=0.1`) | 3 | 41.00 ± 0.40 / 38.27 ± 0.46 | 28.77 ± 0.40 / 28.20 ± 0.26 | 35.03 ± 0.21 / 31.07 ± 0.23 | 62.57 ± 0.23 / 58.00 ± 0.30 |
| PMRL (`tau1=0.07`) | 3 | 42.17 ± 0.12 / 40.97 ± 0.59 | 32.83 ± 0.42 / 32.53 ± 0.65 | 38.40 ± 0.10 / 33.37 ± 0.06 | 66.40 ± 0.17 / 62.33 ± 0.06 |
| HyperGRAM (hybrid) | 3 | 38.93 ± 0.81 / 37.30 ± 0.56 | 25.87 ± 0.95 / 25.80 ± 0.17 | 31.40 ± 0.61 / 24.77 ± 0.46 | 57.93 ± 0.61 / 53.63 ± 0.15 |
| HyperGRAM (pure hyperbolic)† | 3 | 17.17 ± 0.78 / 34.50 ± 0.62 | 20.00 ± 1.55 / 26.23 ± 0.31 | 18.27 ± 0.59 / 26.13 ± 0.31 | 20.10 ± 6.51 / 52.93 ± 0.71 |
| TRIANGLE | 3 | 25.90 ± 1.00 / 40.00 ± 0.30 | 15.80 ± 0.66 / 31.70 ± 0.46 | 17.23 ± 0.31 / 32.87 ± 0.42 | 39.40 ± 0.61 / 64.27 ± 0.31 |
| Ours (`entailment=0`) | 3 | 43.77 ± 0.49 / <u>42.57 ± 0.21</u> | 35.57 ± 0.38 / *35.73 ± 0.15* | 41.17 ± 0.55 / **35.33 ± 0.35** | **69.87 ± 0.21** / **66.47 ± 0.25** |
| **Ours** (`entailment=0.1`) | 3 | *43.80 ± 0.62* / **42.70 ± 0.46** | *35.77 ± 0.42* / <u>35.80 ± 0.17</u> | *41.37 ± 0.51* / <u>35.27 ± 0.29</u> | <u>69.53 ± 0.23</u> / <u>66.20 ± 0.36</u> |
| Ours (`entailment=0.2`) | 3 | **44.17 ± 0.31** / *42.40 ± 0.53* | **36.03 ± 0.42** / **35.93 ± 0.57** | **41.50 ± 0.80** / **35.33 ± 0.21** | *69.27 ± 0.23* / *65.67 ± 0.61* |
| Ours (`entailment=0.3`) | 3 | <u>43.83 ± 0.15</u> / 41.40 ± 0.30 | <u>35.83 ± 0.51</u> / 35.30 ± 0.17 | <u>41.40 ± 0.50</u> / 34.90 ± 0.20 | 68.80 ± 0.20 / 65.17 ± 0.40 |
| Ours (`entailment=0.5`) | 3 | 43.07 ± 0.12 / 38.47 ± 0.45 | 35.13 ± 1.08 / 31.17 ± 0.38 | 37.47 ± 0.40 / 32.70 ± 0.10 | 65.00 ± 0.52 / 61.87 ± 0.38 |
| MERU all-pair，无 entailment‡ | 1 | 39.9 / 34.5 | 27.8 / 25.9 | 33.8 / 30.3 | 61.5 / 55.6 |
| MERU all-pair，Text parent‡ | 1 | 39.8 / 33.9 | 27.3 / 25.5 | 33.1 / 29.9 | 59.6 / 54.8 |
<!-- VIDEO_STAGE1_DIRECT_TABLE_END -->

† 本行取官方纯双曲候选生成分数（ITM 重排前）；使用 TVA/TVAS 联合候选，按 T→D / D→T 理解。评测口径差异同 Top-50 主表脚注，仅作方法级参考，不纳入前三名标记。

‡ MERU 两行为单 seed 结果，协议与第 2 节主表脚注及第 7 节一致，不参与历史三 seed 排名。

<a id="stage1-summary"></a>

### 2.5 Stage-1 跨方法汇总

以下为四个视频数据集（MSR-VTT、DiDeMo、ActivityNet、VATEX）、两个方向的 R@1 等权平均（%），不是 R@1/5/10 的平均。评测时不运行 ITM，但部分方法训练时包含 ITM 辅助损失。

| 实验组 | 方法 | Seeds | Stage-1 平均 R@1 |
|---|---|---:|---:|
| 历史 baseline | VAST | 1 | 35.04 |
| 历史 baseline | GRAM | 3 | 33.46 |
| 历史 baseline | HyperGRAM hybrid | 3 | 36.95 |
| 外部 baseline（2026-10-10 协议） | HyperGRAM pure hyperbolic | 3 | 26.92 |
| 历史 baseline | TRIANGLE | 3 | 33.40 |
| 9 月配对实验 | PMRL matched | 1 | 46.03 |
| 9 月配对实验 | 双曲谱，无 entailment | 1 | 46.13 |
| 9 月配对实验 | 双曲谱，Text parent | 1 | 46.14 |
| 9 月配对实验 | 双曲谱，Mean parent（α=1） | 1 | 46.00 |
| 9 月配对实验 | 双曲谱，SVD learned-radius parent | 1 | 45.96 |
| 9 月配对实验 | MERU all-pair，无 entailment | 1 | 38.66 |
| 9 月配对实验 | MERU all-pair，Text parent | 1 | 37.99 |

外部 baseline 均值由第 2.4 节已显示的八个方向均值计算，再四舍五入至两位小数，不推算跨方向标准差。各方法采用原生候选评分；HyperGRAM pure 使用 TVA/TVAS 联合候选及更新后的媒体协议。9 月配对组为 seed 50、匹配训练预算、TV-only Stage-1 候选；PMRL matched 不是第 2.4 节历史 PMRL 三 seed 行。不同实验组仅作参考，不将整表视为严格配对排名。

PMRL、双曲谱 E0/ET 与 MERU 的来源为第 7.2 节；Mean/SVD 来源为 实验回顾第 9 节（源项目 `PMRL-minimal-hyperbolic/docs/HYPERBOLIC_EXPERIMENT_REVIEW_20261013.md#9-当前512维-parent-完整对照`，未收录快照）。配对组中 PMRL/双曲谱的 Stage-1 均值约为 46，MERU all-pair 约为 38；加入 Text entailment 没有改善本轮 MERU 的直接检索。

PMRL 相对无 entailment MERU 的 Stage-1 优势为 7.3625 个百分点，但 Top-50 ITM 后仅为 0.1750 个百分点。这说明直接检索优势没有等幅反映到最终重排结果；尚不能认定 ITM 未充分利用表征，需进一步比较 Stage-1 R@50 与不同候选数 K 下的重排结果。

<a id="audio-direct"></a>

## 3. Audio–text Stage-1 direct retrieval（无 ITM）

AudioCaps 与 ClothoV2 均统一为纯 `ret%ta`。评估器在输出原生 Stage-1
相似度的双向指标后立即返回，不构造也不运行 ITM reranker。AudioCaps 不再使用
旧实验中的 `ret%tva` 视频–音频联合候选。

<!-- AUDIO_STAGE1_DIRECT_TABLE_START -->
| 方法 | Seeds | AudioCaps T→A / A→T | ClothoV2 T→A / A→T |
|---|---:|---:|---:|
| VAST | 1 | <u>30.80</u> / **31.80** | <u>15.40</u> / <u>14.00</u> |
| GRAM | 3 | 22.37 ± 0.86 / 22.43 ± 1.37 | 13.30 ± 0.69 / 10.23 ± 0.85 |
| PMRL | 3 | **31.37 ± 0.93** / <u>31.10 ± 0.30</u> | **16.10 ± 0.30** / **14.77 ± 0.12** |
| HyperGRAM (hybrid) | 3 | 24.30 ± 0.61 / 23.50 ± 1.84 | 13.60 ± 0.30 / 10.63 ± 0.81 |
| HyperGRAM (pure hyperbolic)† | — | 未评测 | 未评测 |
| TRIANGLE | 3 | 23.70 ± 0.70 / *27.77 ± 0.86* | 14.57 ± 0.61 / *12.70 ± 0.87* |
| **Ours** | 3 | *27.53 ± 0.90* / 23.83 ± 0.57 | *14.83 ± 0.72* / 10.50 ± 0.17 |
| MERU all-pair，无 entailment‡ | 1 | 21.7 / 26.0 | 12.7 / 13.9 |
| MERU all-pair，Text parent‡ | 1 | 20.2 / 25.9 | 12.0 / 13.0 |
<!-- AUDIO_STAGE1_DIRECT_TABLE_END -->

‡ MERU 音频结果为第 7.3 节的 seed-50 纯 `ret%ta`、first-caption 评测：AudioCaps 704/729 条可用音频，ClothoV2 1045/1045 条，不运行 ITM。保留原始一位小数；不与历史三 seed 行合并统计或参与前三名标记。

这里的 PMRL、Ours、GRAM、HyperGRAM 与 TRIANGLE 均已完成 seed 42、50、123，
报告 `mean ± sample std`。VAST 使用官方发布 checkpoint，因此报告一次确定性
评估结果，不能据此估计随机方差。表内没有使用部分运行结果。

† HyperGRAM pure hyperbolic 尚无本表对应的评测结果；“未评测”不是零分，Seeds 列的“—”表示尚无完成该评测的 seed，不代表未训练。

## 4. 历史 Audio–text Top-50 结果（旧协议，不作为新主表）

本节保留此前结果以便追溯，但 AudioCaps 使用的是 `ret%tva` 且包含 Top-50
ITM，因此不能解释为纯 audio–text Stage-1 direct retrieval。

表中每个数据集按 `T→A / A→T` 排列。除 VAST 外，数值均为三次实验的
`mean ± sample std`，排名标记沿用第一名粗体、第二名下划线、第三名斜体。

| 方法 | Seeds | AudioCaps T→A / A→T | ClothoV2 T→A / A→T |
|---|---:|---:|---:|
| VAST | 1 | <u>33.20</u> / <u>33.50</u> | 14.70 / 14.50 |
| GRAM | 3 | 32.03 ± 1.05 / *33.43 ± 0.40* | 16.50 ± 0.53 / <u>15.63 ± 0.86</u> |
| PMRL | 3 | *32.83 ± 0.93* / 32.13 ± 0.91 | **17.20 ± 0.46** / *15.50 ± 0.62* |
| HyperGRAM (hybrid) | 3 | **34.70 ± 1.61** / **36.10 ± 0.35** | *16.83 ± 0.81* / 15.30 ± 0.26 |
| HyperGRAM (pure hyperbolic)† | — | 未评测 | 未评测 |
| TRIANGLE | 3 | 30.00 ± 0.78 / 32.30 ± 0.79 | <u>16.93 ± 0.76</u> / **15.77 ± 0.67** |
| **Ours** | 3 | 31.67 ± 1.15 / 31.77 ± 0.25 | <u>16.93 ± 0.51</u> / 14.87 ± 0.76 |

† HyperGRAM pure hyperbolic 尚无本表对应的评测结果；“未评测”不是零分，Seeds 列的“—”表示尚无完成该评测的 seed，不代表未训练。

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

## 5. 总体结论（历史三 seed 实验）

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
6. 历史三 seed 报告中，finetune 主实验仍需独立完成，不能由本页
   zero-shot 结果推断。之后的 MSRVTT 子集模型微调另见 [EXP-006](EXP-006-msrvtt-finetune.md)，
   模型与协议不同，不合并进本页的历史主表。

## 6. 原始结果与汇总文件

历史主输出目录（保留源服务器路径；本机不存在 `/data-nfs`，不据此推断迁移位置）：

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

<a id="meru-paired"></a>

## 7. MERU-style 三模态 baseline（2026-09-29，单 seed 配对实验）

本节为新增 seed-50 实验，独立于第 2–3 节的历史三 seed 主表；不替换历史均值、标准差或排名。
第 5 节结论仍对应历史实验，本轮结论见 7.5。两组已于 2026-09-29 09:33 UTC
（北京时间 17:33）全部完成。

### 7.1 方法与比较口径

- MERU-style 将 TV、TA、VA 三对的双向 InfoNCE 等权平均，相似度为负 Lorentz
  测地距离，温度固定 0.07，使用支持梯度回传的 global-batch negatives。
- `meru_allpair_no_ent`：all-pair InfoNCE + 0.1 ITM。
- `meru_allpair_text_parent`：all-pair InfoNCE + 0.1 entailment + 0.1 ITM；
  entailment 仅为 T→V、T→A 锥违例的平均。两组均关闭双曲谱目标。
- 这是沿用当前 backbone 和方向—半径映射的 MERU-style 多模态适配，不是官方 MERU 完整复现。
- 本节视频对照统一 VAST 初始化、86707 条训练样本、seed 50、global batch 64、
  1360 次有效 optimizer 更新及最终 checkpoint，保持相同视频评测与 Top-50 ITM 协议。
- PMRL 为匹配预算的原始目标对照；其 inter negatives 为 rank-local 16，
  双曲谱与 MERU-style 使用 global 64。目标、温度等也存在差异，不能单独归因于几何。
- 音频对照统一纯 `ret%ta`、Stage-1、固定每段音频的首条 caption，不使用视觉或 ITM；
  AudioCaps 使用可用的 704/729 条音频，ClothoV2 使用 1045/1045 条。
  不是官方五 caption 评测，不与历史音频主表直接合并。

### 7.2 Video–text 逐数据集结果

均为 R@1（%），每格按 T→V / V→T 排列。

| 方法 | 阶段 | MSR-VTT | DiDeMo | ActivityNet | VATEX | 八方向均值 |
|---|---|---:|---:|---:|---:|---:|
| PMRL matched | Stage-1 | 43.6 / 42.1 | 35.6 / 36.1 | 40.8 / 35.8 | 68.0 / 66.2 | 46.0250 |
| 双曲谱，无 entailment | Stage-1 | 43.8 / 42.0 | 34.6 / 35.3 | 41.3 / 34.9 | 70.3 / 66.8 | 46.1250 |
| 双曲谱，text-parent | Stage-1 | 43.1 / 41.6 | 35.0 / 35.6 | 41.7 / 35.2 | 70.3 / 66.6 | 46.1375 |
| MERU-style，无 entailment | Stage-1 | 39.9 / 34.5 | 27.8 / 25.9 | 33.8 / 30.3 | 61.5 / 55.6 | 38.6625 |
| MERU-style，text-parent | Stage-1 | 39.8 / 33.9 | 27.3 / 25.5 | 33.1 / 29.9 | 59.6 / 54.8 | 37.9875 |
| PMRL matched | Top-50 ITM | 56.6 / 52.8 | 53.8 / 52.2 | 55.8 / 50.3 | 80.1 / 75.0 | 59.5750 |
| 双曲谱，无 entailment | Top-50 ITM | 56.9 / 53.3 | 53.6 / 51.2 | 56.0 / 50.4 | 79.2 / 74.8 | 59.4250 |
| 双曲谱，text-parent | Top-50 ITM | 57.2 / 53.5 | 53.4 / 51.2 | 55.7 / 50.6 | 79.0 / 75.2 | 59.4750 |
| MERU-style，无 entailment | Top-50 ITM | 55.3 / 53.2 | 54.5 / 52.1 | 55.7 / 50.0 | 79.4 / 75.0 | 59.4000 |
| MERU-style，text-parent | Top-50 ITM | 54.8 / 52.0 | 54.0 / 51.3 | 55.8 / 50.0 | 79.1 / 73.8 | 58.8500 |

八方向均值是四个数据集、两个方向的 R@1 等权平均，不是按样本量加权，也不是 R@1/5/10 的均值。

### 7.3 Audio–text Stage-1 结果

均为 R@1（%），每格按 T→A / A→T 排列。

| 方法 | AudioCaps | ClothoV2 |
|---|---:|---:|
| PMRL matched | 28.84 / 29.69 | 15.60 / 13.88 |
| 双曲谱，无 entailment | 27.27 / 26.42 | 13.40 / 11.10 |
| 双曲谱，text-parent | 27.41 / 23.15 | 14.26 / 10.43 |
| MERU-style，无 entailment | 21.7 / 26.0 | 12.7 / 13.9 |
| MERU-style，text-parent | 20.2 / 25.9 | 12.0 / 13.0 |

对照组沿用逐查询汇总的两位小数；MERU-style 沿用原生指标的一位小数，不补造精度。

### 7.4 几何诊断

使用固定 4096 个 VAST 样本；半径为平均测地半径，违例单位为 rad。

| MERU-style 设置 | T 半径 | V 半径 | A 半径 | T→V 平均违例 | T→A 平均违例 | T→V / T→A 锥满足率 |
|---|---:|---:|---:|---:|---:|---:|
| 无 entailment | 1.150901 | 1.193815 | 1.128711 | 2.125345 | 2.253816 | 0% / 0% |
| text-parent | 0.997881 | 1.286802 | 1.187121 | 1.861250 | 2.037403 | 0% / 0% |

Entailment 改变了径向位置并降低平均锥违例，但诊断样本上仍无满足锥约束的配对。
半径排序不等于锥包含，更不能单凭这些统计认定学到了语义层级。

### 7.5 本轮结论与限制

1. 直接视频检索中，双曲谱相对 MERU-style 的八方向平均 R@1：无 entailment 时
   高 7.4625 个百分点，text-parent 时高 8.1500 个百分点；两种设置下均为八个方向全部更高。
2. Top-50 ITM 后差距明显缩小：无 entailment 时双曲谱仅高 0.0250 个百分点，
   text-parent 时高 0.6250 个百分点。本轮最明确的观察是第一阶段检索优势，不能据此声称最终重排全面领先。
3. MERU-style 加入 entailment 后，视频 Stage-1 均值下降 0.6750 个百分点，
   ITM 均值下降 0.5500 个百分点；音频四个方向 R@1 也均下降。
4. 音频上 MERU-style 相对双曲谱 text-parent 的 T→A 更弱、A→T 更强，
   没有形成跨方向的全面改善，整体也未超过 PMRL matched。
5. 当前仅 seed 50、固定温度和预算，未估计训练随机方差，也未对 MERU-style 做超参数搜索。
   这些结果支持当前配置下的比较，不足以证明谱方法普遍优于 MERU 或建立统计显著性。

### 7.6 本轮结果来源

- MERU-style 完整 R@1/5/10 与几何报告：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/meru_multimodal_pairwise_20260929/REPORT.md`
- MERU-style 协议：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/meru_multimodal_pairwise_20260929/protocol.json`
- 同预算视频对照报告：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/entailment_ablation_20260928/REPORT.md`
- 同协议音频对照报告：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/audio_text_eval_20260929_side/REPORT.md`
- MERU-style 方法说明（源项目 `PMRL-minimal-hyperbolic/docs/MERU_MULTIMODAL_PAIRWISE_BASELINE.md`，未收录快照）

<!-- HYPERGRAM_PURE_20261010_START -->
<a id="hypergram-pure"></a>

## 8. HyperGRAM 纯 hyperbolic 官方代码复现（2026-10-10）

使用官方提交 `fd6e89b1733c48a75835c0bd7ae23b150490d01c`，`geometry_mode=hyperbolic`；不混入 Euclidean 分支。
VAST 86,707 条 accepted 标注、TVAS 原生训练、batch128、学习率5e-5、一 epoch（677次计划更新），seeds50/42/123。
采用当前媒体和 first-caption 评测 manifests。候选是官方原生 TVA/TVAS 联合候选；与第7节 video-only 的配对模型属于方法级参考，不能单独归因几何。前部汇总表以†行并列展示，保留协议差异说明，不重算历史结果。
保留官方模型、损失、体积与检索计算；环境/运行适配和实际AMP更新数见协议及逐rank审计。纯双曲指表征对齐分支，Top-50仍使用官方ITM。
运行协议：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/hypergram_pure_official_20261010/protocol.json` · 实时状态：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/hypergram_pure_official_20261010/status.json`

### 8.1 原生 Stage-1 R@1

每格为 T→D / D→T（%，D为对应视频实例的联合模态候选）。

| 方法 / seed | MSR-VTT | DiDeMo | ActivityNet | VATEX |
|---|---:|---:|---:|---:|
| HyperGRAM-pure / 50 | 17.4 / 34.3 | 18.4 / 26.5 | 17.6 / 25.8 | 23.4 / 52.3 |
| HyperGRAM-pure / 42 | 16.3 / 35.2 | 20.1 / 26.3 | 18.7 / 26.2 | 12.6 / 52.8 |
| HyperGRAM-pure / 123 | 17.8 / 34.0 | 21.5 / 25.9 | 18.5 / 26.4 | 24.3 / 53.7 |
| HyperGRAM-pure / 三seed均值±样本标准差 | 17.17 ± 0.78 / 34.50 ± 0.62 | 20.00 ± 1.55 / 26.23 ± 0.31 | 18.27 ± 0.59 / 26.13 ± 0.31 | 20.10 ± 6.51 / 52.93 ± 0.71 |

### 8.2 Top-50 ITM R@1

每格为 T→D / D→T（%，D为对应视频实例的联合模态候选）。

| 方法 / seed | MSR-VTT | DiDeMo | ActivityNet | VATEX |
|---|---:|---:|---:|---:|
| HyperGRAM-pure / 50 | 46.8 / 51.0 | 48.2 / 48.9 | 49.5 / 48.5 | 64.0 / 74.4 |
| HyperGRAM-pure / 42 | 42.1 / 51.4 | 47.8 / 48.5 | 50.0 / 49.0 | 37.7 / 74.6 |
| HyperGRAM-pure / 123 | 47.4 / 51.1 | 47.9 / 49.0 | 48.4 / 47.6 | 66.3 / 74.0 |
| HyperGRAM-pure / 三seed均值±样本标准差 | 45.43 ± 2.90 / 51.17 ± 0.21 | 47.97 ± 0.21 / 48.80 ± 0.26 | 49.30 ± 0.82 / 48.37 ± 0.71 | 56.00 ± 15.89 / 74.33 ± 0.31 |

<!-- HYPERGRAM_PURE_20261010_END -->

<!-- HYPERGRAM_TUNING_20261012_START -->
<a id="hypergram-tuning"></a>

## 9. HyperGRAM 纯双曲参数探索（2026-10-12）

保持官方实现与原生检索口径不变；seed50，分阶段调参，各组从相同 VAST 初始化重训。原始三seed基线保留在第8节。
依次比较主学习率、固定曲率、温度参数学习率、ITM权重和训练长度，最多9组新训练。以前一阶段最佳配置为下一阶段起点；主指标为四数据集八方向 Top-50 R@1，Stage-1用于同分比较。
**这是使用评测集选参的单seed探索，不能视作独立测试集的无偏结果，也不能代表三seed提升。** 曲率梯度和裁剪等官方实现均未修复；只调整原生配置。
协议：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/hypergram_tuning_20261012/protocol.json` · 实时状态：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/hypergram_tuning_20261012/status.json` · 全部结果：`/data0/xiaobo.xia/yuxuan.gao/PMRL/outputs/hypergram_tuning_20261012/results.json`

| 配置 | 状态 | 主LR | 曲率 | 温度LR | ITM权重 | Epoch | Stage-1 R@1 | Top-50 R@1 | ΔTop-50 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline | complete | 5e-05 | 1 | 5e-05 | 0.1 | 1 | 26.9625 | 53.9125 | +0.0000 |
| c0p3 | complete | 1e-05 | 0.3 | 1e-05 | 0.1 | 1 | 16.2000 | 40.8875 | -13.0250 |
| c2 | complete | 1e-05 | 2 | 1e-05 | 0.1 | 1 | 28.6250 | 55.9250 | +2.0125 |
| epochs2 | complete | 1e-05 | 2 | 1e-05 | 0.2 | 2 | 26.5750 | 54.6000 | +0.6875 |
| itm0p05 | complete | 1e-05 | 2 | 1e-05 | 0.05 | 1 | 28.5375 | 56.0125 | +2.1000 |
| itm0p2 | complete | 1e-05 | 2 | 1e-05 | 0.2 | 1 | 28.5125 | 56.1250 | +2.2125 |
| lr1e5 | complete | 1e-05 | 1 | 1e-05 | 0.1 | 1 | 27.0000 | 54.2875 | +0.3750 |
| lr2e5 | complete | 2e-05 | 1 | 2e-05 | 0.1 | 1 | 22.4125 | 50.5625 | -3.3500 |
| temp_lr1e5 | complete | 1e-05 | 2 | 1e-05 | 0.1 | 1 | 28.5000 | 55.9875 | +2.0750 |
| temp_lr5e6 | complete | 1e-05 | 2 | 5e-06 | 0.1 | 1 | 28.0125 | 55.5625 | +1.6500 |

### 分阶段选择记录

- learning_rate：选择 `lr1e5`；已完成候选 baseline, lr2e5, lr1e5。
- curvature_fixed：选择 `c2`；已完成候选 lr1e5, c0p3, c2。
- temperature_lr：选择 `temp_lr1e5`；已完成候选 c2, temp_lr1e5, temp_lr5e6。
- itm_weight：选择 `itm0p2`；已完成候选 temp_lr1e5, itm0p05, itm0p2。
- epochs：选择 `itm0p2`；已完成候选 itm0p2, epochs2。

### baseline 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 17.4 / 34.3 | 46.8 / 51.0 |
| didemo | 18.4 / 26.5 | 48.2 / 48.9 |
| activitynet | 17.6 / 25.8 | 49.5 / 48.5 |
| vatex | 23.4 / 52.3 | 64.0 / 74.4 |

### c0p3 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 0.9 / 30.4 | 24.4 / 51.0 |
| didemo | 0.7 / 25.8 | 30.1 / 49.3 |
| activitynet | 0.6 / 25.4 | 12.1 / 48.7 |
| vatex | 1.8 / 44.0 | 38.6 / 72.9 |

### c2 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 20.2 / 37.8 | 49.4 / 52.6 |
| didemo | 16.9 / 30.4 | 49.4 / 50.4 |
| activitynet | 15.1 / 29.5 | 47.8 / 50.0 |
| vatex | 21.3 / 57.8 | 72.3 / 75.5 |

### epochs2 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 18.0 / 35.9 | 47.3 / 53.6 |
| didemo | 16.0 / 26.0 | 48.3 / 49.6 |
| activitynet | 13.6 / 25.2 | 45.7 / 48.9 |
| vatex | 23.8 / 54.1 | 67.6 / 75.8 |

### itm0p05 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 20.2 / 37.3 | 50.2 / 52.0 |
| didemo | 17.0 / 30.8 | 49.5 / 50.7 |
| activitynet | 15.0 / 29.7 | 48.0 / 50.0 |
| vatex | 20.8 / 57.5 | 72.0 / 75.7 |

### itm0p2 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 19.6 / 38.0 | 50.0 / 52.7 |
| didemo | 16.0 / 29.8 | 49.8 / 50.9 |
| activitynet | 15.0 / 29.5 | 47.7 / 50.1 |
| vatex | 22.0 / 58.2 | 72.0 / 75.8 |

### lr1e5 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 16.4 / 37.0 | 47.9 / 52.9 |
| didemo | 14.1 / 28.9 | 45.6 / 51.3 |
| activitynet | 13.6 / 28.1 | 44.7 / 50.5 |
| vatex | 22.3 / 55.6 | 66.2 / 75.2 |

### lr2e5 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 9.6 / 32.7 | 39.1 / 52.9 |
| didemo | 12.1 / 26.4 | 43.2 / 50.5 |
| activitynet | 6.4 / 25.7 | 35.2 / 49.2 |
| vatex | 13.9 / 52.5 | 59.7 / 74.7 |

### temp_lr1e5 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 19.9 / 37.6 | 50.0 / 52.1 |
| didemo | 16.6 / 30.5 | 49.3 / 50.6 |
| activitynet | 15.0 / 29.6 | 47.9 / 50.1 |
| vatex | 21.2 / 57.6 | 72.3 / 75.6 |

### temp_lr5e6 分数据集 R@1

每格为原生 T→D / D→T，D为TVA/TVAS联合模态候选。

| 数据集 | Stage-1 | Top-50 |
|---|---:|---:|
| msrvtt | 18.1 / 37.4 | 48.8 / 52.4 |
| didemo | 16.2 / 30.2 | 48.6 / 50.8 |
| activitynet | 14.8 / 29.3 | 47.3 / 50.1 |
| vatex | 20.3 / 57.8 | 71.1 / 75.4 |
<!-- HYPERGRAM_TUNING_20261012_END -->

<a id="7-历史-parent-消融"></a>
<a id="historical-parent"></a>

## 10. 历史 Parent 消融

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
| E0 | 41.95 | 54.30 | 4.75 |
| Perron λ=0.1 | 41.70 | 54.45 | 4.70 |
| Text λ=0.1 | 41.80 | 54.60 | 4.80 |
| SVD λ=0.1 | 42.05 | 54.40 | 4.75 |

带蕴含约束的三组锥满足率均为 0%。原始[汇总表](../results/EXP-001/2026-10-20/summary.md)、[结构化结果](../results/EXP-001/2026-10-20/summary.json)、[完成状态](../../Hyperbolic-Omnimodal/outputs/server_b_20261014/controller_status.json)。

### 结论与下一步

检索差异很小，未观察到明确的 parent 构造收益或严格包含成功。单种子验证结果不足以支持稳定优势；测试栏为空，不能当作测试结果。后续转向显式子集关系，见 EXP-002。

### 变更记录

- 2026-10-14：首个 smoke 因 allocator cap 失败；第二个 attempt 调整资源上限后通过，正式四组完成。失败记录保留。
- 2026-10-20：根据现存执行文档与结果补录实验卡。
- 2026-10-20：按用户要求移入零样本基线汇总页末尾；原结果和来源链接完整保留。

## 本次同步记录

- 2026-10-20（UTC）：从 server-b 的 2026-10-15 版零样本报告同步全部表格，新增 MERU 配对、HyperGRAM pure 三 seed 复现、单 seed 调参与 Stage-1 汇总。
- 保留旧快照与历史 Parent 消融；保留音频 direct / 旧 Top-50 的结论区分。源报告未修改，没有把旧 JSON 冒充新增实验的机器结果。
- 新快照版本为 `2026-10-20-server-b`；采集时间与 SHA-256 见来源清单。源报告中的辅助报告、协议和状态文件未在本次额外采集，运行状态只代表报告所记录的时点。
