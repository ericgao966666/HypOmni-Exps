# R3固定曲率：64D验证候选小幅提高，尚无新测试

[返回实验总览](../README.md) · `EXP-20261029-server-a-r3-curvature` · 归档核对：2026-11-05T08:39:54.407550+00:00

固定c=.3、τ=.035的64D R3候选在MSRVTT验证R@1达到28.467%，比历史欧氏28.267%高0.200pp；联合学习c/τ的λ=.2候选为28.100%。这轮没有新增测试集结果。

## 研究问题与关键设置

R3为VAST热身8轮＋头部30轮，再按事前VAST验证规则锁定两组、MSRVTT微调10轮。train7427/validation500、batch64、seed50；FP32头部/FP64几何。17个头部条件涵盖固定c/τ网格和32/64/128/512D，但只有两个64D固定候选进入微调。

## 主要结果

| 64D MSRVTT验证候选 | 选中epoch | R@1 | R@5 | R@10 |
|---|---|---|---|---|
| historical R3 euc_none | 9 | <ins>28.267</ins> | **55.300** | 65.800 |
| historical R3 hyp_cone | 7 | 28.100 | <ins>55.100</ins> | <ins>65.933</ins> |
| lambda .2, learned c/tau R3 hyp_cone | 7 | 28.100 | 54.867 | 65.900 |
| fixed_c0.3_t0.035 | 7 | **28.467** | 54.967 | **66.033** |
| fixed_c0.3_t0.07 | 9 | 27.800 | 54.967 | 65.800 |


## 解释、局限与下一步

所有列来自MSRVTT验证最优checkpoint，选中epoch已列明。不同温度、λ及学习开关使其成为配方比较，不能把0.200pp全部归因于曲率；头部筛选也可能漏掉微调后反超的配置。历史扩维测试缺口仍保留在原[64D检索卡](EXP-20261021-server-b-retrieval-training.md)。

## 结果报告

[17条件头部与微调报告](../summaries/recent-20261105/r3_curvature.md)

## 来源与复核范围

- 本地 `workspace/Hyperbolic-Omnimodal/code/outputs/r3_64d_learned_ct_lambda02_20261028/comparison.json`；SHA-256：`c77f8c518a48573b96a519da1081b80728665cd4e481def2c7ab2aeb83560766`。
- 本地 `workspace/Hyperbolic-Omnimodal/code/outputs/r3_curvature_dimension_20261029/comparison.json`；SHA-256：`7fe7c4db98836d5e0fc88fbec5f0833f731ffa4bdff1d35d39692e404e19d4df`。

这里只读取并归档已有结果，没有重新训练或重新计算模型指标。完整数据、源码版本和运行细节留在上述来源及本地快照。
