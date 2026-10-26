# PMRL–ITM：采样收益较小，开发集选定融合在测试中退化

[返回实验总览](../README.md) · `EXP-20261021-server-a-pmrl-itm-alignment` · 结果核对：2026-10-24 21:39（Asia/Shanghai）；文档整理：2026-10-26

**共同TV候选、纯ITM下，开发集预选的sigma_max比基线提高0.4087个百分点；未达到原设0.5个百分点实用门槛。开发集选定的融合在四种方法上均低于纯ITM。** 四种采样方法的单seed预算及16项测试已完成。

## 研究问题与关键设置

保持PMRL编码器、谱损失与VA token ITM，改变训练负样本采样评分，判断对齐空间的变化能否改善最终检索。采样收益和候选生成收益分别比较。

| 影响解读的设置 | 本轮口径 |
|---|---|
| 对照与变量 | legacy_va、tv、mean_tv_ta、sigma_max；本页主表统一TV候选，隔离采样差异 |
| 数据与预算 | 四组均用86,706条严格TVA训练清单，seed50、512维、全局batch64、一个epoch（1,354批）；无下游微调 |
| 初始化与选模 | 同一VAST官方权重；固定epoch末轮checkpoint；采样方案、候选评分、融合参数只按1,000样本开发集选择并在测试前锁定 |
| 测试集合 | MSRVTT 884、DiDeMo 995、ActivityNet 3,987、VATEX 1,224；固定视听交集，每视频第一条caption，非完整官方测试集 |
| 主指标 | Top-50 ITM；每数据集T→VA/VA→T双向R@1平均，再对四数据集等权平均，单位% |

## 主要结果

**测试中mean_tv_ta最高不改变事前预选的sigma_max。** 以下表格分别保留纯ITM与开发集选定融合，不能跨口径混排。

## 纯ITM：TV候选，Top-50，α=0

| 训练方法 | MSRVTT | DiDeMo | ActivityNet | VATEX | 平均R@1 | 相对同候选基线 Δpp |
|---|---:|---:|---:|---:|---:|---:|
| legacy_va | 49.6041 | 51.2060 | **52.6712** | 76.8382 | 57.5799 | +0.0000 |
| tv | 49.6606 | 51.2563 | 52.1946 | 77.0425 | 57.5385 | -0.0414 |
| mean_tv_ta | <ins>50.8484</ins> | **51.7085** | 52.1821 | **77.3693** | **58.0271** | **+0.4472** |
| sigma_max | **50.9615** | <ins>51.5578</ins> | <ins>52.2699</ins> | <ins>77.1650</ins> | <ins>57.9886</ins> | <ins>+0.4087</ins> |

## 开发集选定的融合：TV候选，Top-50，α=1

| 训练方法 | MSRVTT | DiDeMo | ActivityNet | VATEX | 平均R@1 | 相对同候选基线 Δpp |
|---|---:|---:|---:|---:|---:|---:|
| legacy_va | 50.2262 | 43.8693 | 41.2591 | 71.1193 | 51.6185 | +0.0000 |
| tv | **50.8484** | **44.4221** | 41.3469 | 71.0784 | **51.9240** | **+0.3055** |
| mean_tv_ta | <ins>50.3959</ins> | <ins>44.3216</ins> | **41.4848** | <ins>71.1601</ins> | <ins>51.8406</ins> | <ins>+0.2221</ins> |
| sigma_max | 49.9434 | 43.3166 | <ins>41.4472</ins> | **71.2010** | 51.4771 | -0.1414 |

融合公式为每个查询的候选集内`z(ITM匹配概率)+α*z(TV相似度)`，标准差下限1e-6；α=0保留原ITM概率排序。TV仍负责提供Top-50候选，纯ITM不代表对全库直接运行ITM。α从开发集网格{0,0.1,0.3,1,3}选择，测试前锁定。


## 解释与局限

- 共同候选下，sigma_max和mean_tv_ta的纯ITM增益分别为+0.4087、+0.4472个百分点；TV采样为−0.0414个百分点。当前结果未支持稳定达到实用门槛的采样收益。
- 事前选定sigma_max在融合口径下为51.4771%，比融合基线51.6185%低0.1414个百分点。不能把纯ITM的增益当成实际预选融合方案的正结果。
- 相对原legacy_va候选基线的变化还包含候选生成机制，不能全部归因于训练采样。
- 原计划追加的42/123已取消，当前预算仅seed50。配对视频bootstrap条件于该训练seed，不估计训练种子方差；旧文件中的三seed未完成标记不代表当前预算缺失。
- 原accepted清单中排除一条阻塞样本后，四组统一使用86,706条冻结清单；媒体无损修复和AMP跳步等执行证据见[完成核验](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/verification.json)。这些影响数据/预算解读的事实保留，具体重启和迁移时间线见运行附录。

## 下一步判断

优先在开发集分析融合跨数据集泛化，不用这批测试结果重新选α或替换预选采样。若主张采样收益，需要另行设计独立验证；本记录不授权新实验。

## 完整结果与来源

[当前权威汇总](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md) · [原始JSON](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/results.json) · [完整交叉报告](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/REPORT.md) · [逐任务指标](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/metrics/) · [开发集选择](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/selection.json) · [单seed范围](../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/execution_policy.json)。

[运行与迁移历史](../runs/EXP-20261021-server-a-pmrl-itm-alignment/history-before-results-rewrite-20261026.md)保留原实验卡的全部启停、修复、核查和版本记录。指标、运行源码摘要和数据来源以快照核验文件为准。
