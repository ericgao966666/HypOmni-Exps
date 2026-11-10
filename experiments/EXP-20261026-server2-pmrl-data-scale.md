# VAST 数据规模扩大后，PMRL 的单轮检索表现如何变化？

[返回实验总览](../README.md) · EXP-20261026-server2-pmrl-data-scale · 当前轮已完成；结果核对：2026-11-03 21:41；归档产物复核与文档更新：2026-11-10，Asia/Shanghai

**当前数据组相对上一轮，Top-50 ITM八方向平均R@1提高 0.0644 个百分点。** 训练集由105,369条增至120,688条，均从同一官方VAST初始化、seed50、各一个epoch；平均R@1为 59.4365% → 59.5009%。95%配对样本bootstrap差值区间 [-0.4286, +0.5224] pp。差值的条件样本区间包含0。

Stage-1 direct均值为 45.4669% → 45.4737%，变化 +0.0069 pp。

11-10复核已有`summary.md`与`verification.json`：当前组1885次更新完成、0次AMP跳步，四集评测来源齐全；未重跑训练或评测。周度整理前，此轮结果仅在本地卡片中，远端`ee98a3e`仍为10-26两组结果；本次发布纳入三组完整对照。

## 研究问题与关键设置

| 设置 | 当前口径 |
|---|---|
| 数据规模 | 86,706 / 105,369 / 120,688条；前两组复用10-26完成结果，本轮只新训2026-11-03冻结数据组 |
| 执行位置 | server1（server-a），GPU 0,1,2,3；环境差异见协议与运行记录 |
| 方法与初始化 | 原版PMRL、512维、`ret%tv%ta`；同一VAST权重及初始化头部指纹；模型/损失/优化器/训练循环保持原字节 |
| 预算 | seed50，各一个真实DataLoader epoch；全局batch64，四卡×16，无梯度累积；当前组1885个batch |
| 选模与评测 | 固定末轮、无下游微调；首条caption；TV候选及原模态Top-50 ITM |
| 测试成员 | MSR-VTT 884、DiDeMo 995、ActivityNet 3987、VATEX 1224 |
| 不确定性 | 2000次按视频ID配对、分数据集抽样；固定模型和候选库，不估计训练种子方差 |

## 主要结果

### Top-50 ITM

各数据集为双向R@1均值，单位%；总列为八方向等权平均。

| 训练集 | MSR-VTT | DiDeMo | ActivityNet | VATEX | 八方向平均 |
|---|---:|---:|---:|---:|---:|
| old：86,706条 | 53.90 | 52.11 | 52.91 | <ins>77.37</ins> | 59.07 |
| previous：105,369条 | <ins>54.41</ins> | <ins>52.76</ins> | <ins>53.16</ins> | **77.41** | <ins>59.44</ins> |
| current：120,688条 | **54.64** | **52.86** | **53.17** | 77.33 | **59.50** |

当前组相对105,369条：ΔR@1 +0.0644 pp，配对样本bootstrap 95%区间 [-0.4286, +0.5224] pp。

当前组相对86,706条：ΔR@1 +0.4279 pp，配对样本bootstrap 95%区间 [-0.0262, +0.8906] pp。

### Stage-1 direct

各数据集为双向R@1均值，单位%；总列为八方向等权平均。

| 训练集 | MSR-VTT | DiDeMo | ActivityNet | VATEX | 八方向平均 |
|---|---:|---:|---:|---:|---:|
| old：86,706条 | <ins>43.16</ins> | **35.53** | 37.47 | 66.09 | **45.56** |
| previous：105,369条 | **43.33** | 34.47 | <ins>37.48</ins> | <ins>66.58</ins> | <ins>45.47</ins> |
| current：120,688条 | 42.25 | <ins>34.82</ins> | **37.79** | **67.03** | <ins>45.47</ins> |

当前组相对105,369条：ΔR@1 +0.0069 pp，配对样本bootstrap 95%区间 [-0.3701, +0.4222] pp。

当前组相对86,706条：ΔR@1 -0.0889 pp，配对样本bootstrap 95%区间 [-0.5129, +0.3132] pp。


## 解释与局限

这是各训练一轮的实际表现比较：新增数据同时增加更新次数，恢复媒体的来源/编码也可能不同，不能单独归因于纯数据量。只有seed50，不能证明跨种子稳定收益。两个历史组为已完成同协议结果的明确复用；没有把smoke或旧1360步历史主表混入当前对照。
当前组运行于server1（server-a）/Python3.9.23，已完成的两个对照运行于server2/Python3.10.12；PyTorch、CUDA及其余已核对框架版本一致。跨服务器和Python小版本差异仍需作为比较限制披露。

## 下一步判断

结合逐数据集、双向结果和条件样本区间判断变化方向与幅度。多seed或等步数对照需另行确认，本轮不自动扩展预算。

## 完整结果与来源

- 本轮完整对比（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-11-03-server-a-current-seed50/summary.md`） · R@1/5/10 CSV（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-11-03-server-a-current-seed50/results.csv`） · JSON（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-11-03-server-a-current-seed50/results.json`）
- 协议（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-11-03-server-a-current-seed50/protocol.json`） · 完成核验（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-11-03-server-a-current-seed50/verification.json`）
- 10-26完整结果（本地：`results/EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/summary.md`）
- 当前运行记录（本地：`runs/EXP-20261026-server2-pmrl-data-scale/20261103-server-a-current-data-seed50.md`）
