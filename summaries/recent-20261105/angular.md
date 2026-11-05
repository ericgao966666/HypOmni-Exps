# 角度对齐、原始 entailment 与范数正则

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/REPORT.md`；SHA-256：`67a62f4087754d6caed2e1a46c5e7d645f76af4ecf16ed54d3f61b3d88714922`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

A0边界稳定续跑与A2R数值对照均完成固定30轮/9660步。去掉范数正则的角度+蕴含组 A0，六方向角度检索 R@1=18.970%，相对距离 baseline D2 变化 +0.220pp；相对角度无蕴含 N0 变化 +0.008pp。

A0 的 MERU 截断入锥率为 61.263%，合法域覆盖 43.793%，合法且入锥/全部对为 21.663%。九边同时成立：截断口径 3.271%，合法口径 0.000%。

本轮支持的判断是：角度对齐减轻了加入蕴含监督时的检索代价，并改善部分包含关系。距离对齐下增加蕴含使R@1下降0.269pp，角度下仅变化+0.008pp；没有证据表明蕴含监督进一步提高了角度检索。取消范数正则后R@1基本不变，但合法且入锥/全部对提高6.548pp、截断入锥提高10.493pp。困难错配的截断入锥也从4.595%升至8.436%，故需同时看正负选择性，不能只看正样本成功率。完整九边层级尚未学好。

冻结 VAST 编码器、七子集512D头部，seed50，train82608/val2048，batch256；同一初始化、数据顺序、优化器和训练预算。所有结果为固定末轮，单seed验证集探索，不构成稳定泛化提升。A0在原实现第4502步出现asin端点NaN后，以前向不变的端点反向稳定实现继续到9660步；A2R用同一稳定实现从头重训。N0来自本次原实现实验，D0/D2/D2R来自同协议历史实验；均逐项核验并从末轮特征重算。原始失败记录保留，A0不得标为原数值实现的成功运行。

数值对照已完成：稳定实现A2R与旧A的所有末轮参数逐位相同（最大绝对差0），检索、几何、曲率和温度指标也逐位相同。核验记录（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/final_verification.json`）。

| 条件 | 主检索R@1 | R@5 | R@10 | 截断入锥% | 合法覆盖% | 合法域内入锥% | 合法且入锥/全部% |
|---|---|---|---|---|---|---|---|
| D0 距离，无蕴含 | **19.019** | 37.630 | 46.777 | 0.000 | **100.000** | 0.000 | 0.000 |
| D2 距离，λ=.2 | 18.750 | 37.288 | 46.737 | 0.000 | **100.000** | 0.000 | 0.000 |
| N0 角度，无蕴含 | 18.962 | 38.013 | **47.266** | 0.000 | **100.000** | 0.000 | 0.000 |
| A0 角度，λ=.2 | <ins>18.970</ins> | <ins>38.045</ins> | <ins>47.152</ins> | **61.263** | <ins>43.793</ins> | **49.467** | **21.663** |
| D2R 距离，λ=.2，正则.05 | 18.327 | 37.069 | 46.745 | 0.000 | **100.000** | 0.000 | 0.000 |
| A2R 角度，λ=.2，正则.05 | 18.962 | **38.053** | 47.127 | <ins>50.770</ins> | 42.860 | <ins>35.266</ins> | <ins>15.115</ins> |

距离组主检索使用负双曲距离，角度组使用空间方向余弦；两种统一读出均在 CSV 中。训练仍为九对双向 InfoNCE；原锥 entailment 为九边平均，K=.1，启用时λ=.2。所有组 c/τ 开启学习；无径向监督时 c/半径并不因此获得有意义的学习信号。

检索和包含率（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/analysis/retrieval_geometry.png`）

PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/analysis/retrieval_geometry.pdf`）。包含率图的分母均为全部18432对；蓝色为合法且入锥，橙色为只在截断扩展下入锥。

## 能分离的因素

- 取消正则：A0 相对 A2R 的 R@1 变化 +0.008pp；这两组只改变范数正则系数 .05→0。
- 角度下增加蕴含：A0 相对 N0 的 R@1 变化 +0.008pp。
- 距离下增加蕴含：D2 相对 D0 的 R@1 变化 -0.269pp。
- D2/A0 比较完整的训练分数和匹配检索读出变化；CSV 的交叉读出可区分仅换检索分数的影响。

## 层级和半径控制

| 条件 | 九边同时截断满足% | 九边同时合法满足% | 困难错配截断入锥% | 困难错配合法入锥/全部% | 打乱半径合法入锥/全部% | 类型中位半径合法入锥/全部% |
|---|---|---|---|---|---|---|
| D0 | 0.000 | **0.000** | **0.000** | **0.000** | 0.000 ± 0.000 | 0.000 |
| D2 | 0.000 | **0.000** | **0.000** | **0.000** | 0.000 ± 0.000 | 0.000 |
| N0 | 0.000 | **0.000** | **0.000** | **0.000** | 0.000 ± 0.000 | 0.000 |
| A0 | **3.271** | **0.000** | 8.436 | 0.515 | **19.903 ± 0.142** | **14.431** |
| D2R | 0.000 | **0.000** | **0.000** | **0.000** | 0.000 ± 0.000 | 0.000 |
| A2R | <ins>0.732</ins> | **0.000** | <ins>4.595</ins> | <ins>0.342</ins> | <ins>15.014 ± 0.147</ins> | <ins>9.028</ins> |

打乱数值是五个固定置换（50–54）的均值±标准差，不是多训练seed。每种节点类型内部独立交换测地半径，保留方向与类型内分布；类型中位半径控制进一步将每种类型的所有半径设为其中位数。

A0打乱半径后的合法入锥率为19.903±0.142%，较真实半径21.663%低约1.760pp，提示当前指标中存在一定的样本—半径对应贡献。类型中位半径替换同时会改变合法域覆盖：A0从43.793%变为33.333%，因此该列不能直接当作“径向信息贡献”的净效应；其截断入锥率反而为65.289%。完整分母及连续margin见控制表（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/controls.csv`）。

类型间径向分层本身可以表达单模态→双模态→三模态的子集偏序。打乱不降低指标，不能否定这种层级；它仅削弱“半径与具体样本的对应关系对当前指标有必要贡献”的解释。二值阈值不敏感也是可能原因，因此另保留逐边连续角度、margin 和半径统计。

节点类型的半径（图件仅存本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/analysis/radius_by_type.png`）

PDF（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/analysis/radius_by_type.pdf`）。每点为2048个验证样本的测地半径均值与类型内标准差。A0的单模态均值约.231–.249、双模态约.386–.423、三模态约3.229；A2R的三模态均值约1.033，说明范数正则主要限制了这组实验的外层径向扩张。

共同困难错配来自旧 baseline 的最近错误视频，所有模型使用相同候选；它们是选择性控制，不是人工确认的语义非蕴含标签。

## 指标定义

- 每组全部预定正偏序对 M=9×2048=18432。合法域同时检查父/子 q=sqrt(c)||x_space||≥.2。FP64 排除外角未定义的重合点。
- 截断入锥率：沿用 MERU FP32 半张角截断并判定 relu(phi-psi)≤1e-7，分母M；非法域的截断结果也计入。
- 合法覆盖率=合法对/M；合法域内入锥率=合法且入锥/合法对；合法且入锥/全部=合法且入锥/M。
- 独立 FP64 外角与截断判定同时复核，分歧数写入 audit.json；不可将截断后的包含直接当作原始合法域偏序保证。

完整结果（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/comparison.csv`） · 逐边（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/edges.csv`） · 半径（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/nodes.csv`） · 控制（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/controls.csv`） · 独立核验（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/audit.json`） · 协议与问答（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/README.md`） · 边界修复（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angular_alignment_20261101/stability/NUMERICS.md`）

模型和恢复点：`/data0/xiaobo.xia/yuxuan.gao/angular_alignment_20261101/stability`。未更新旧实验、未提交或上传。
