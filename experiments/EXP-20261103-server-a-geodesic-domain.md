# 测地线K与半径下界：检索回升可重复，合法域仍是瓶颈

[返回实验总览](../README.md) · `EXP-20261103-server-a-geodesic-domain` · 归档核对：2026-11-05T08:39:54.407550+00:00

统一实现三seed重跑中，K=.3→.5的R@1在3/3个seed回升，配对差值+0.564±0.125pp；K=.5合法覆盖却只有33.133±0.009%，九边同时合法满足为0%。动态下界能保证合法域，但不自动产生层级。

## 研究问题与关键设置

VAST 冻结编码器、512D 七子集头部，train82608/validation2048，batch256，固定30轮/9660次更新；只比较验证集，不使用测试集选型。λ=.2、K_train=K_eval。seed50/51/52；±为seed间样本标准差ddof=1，区别于单seed节点分布标准差。五K新训15组，大K新增9组，eta×alpha新增24组，动态下界新增21组，取消.21新增3组，复用基准不重复计为新训练。

## 主要结果

| K | R@1 (%) | 合法覆盖 (%) | 合法入锥/全部 (%) | 九边同时合法 (%) |
|---|---|---|---|---|
| 0.05 | **18.685±0.115** | **100.000±0.000** | 0.000±0.000 | **0.000±0.000** |
| 0.1 | 18.631±0.118 | **100.000±0.000** | 0.000±0.000 | **0.000±0.000** |
| 0.2 | 18.487±0.147 | **100.000±0.000** | 0.000±0.000 | **0.000±0.000** |
| 0.3 | 18.091±0.029 | <ins>74.964±0.064</ins> | **12.844±0.138** | **0.000±0.000** |
| 0.5 | <ins>18.655±0.115</ins> | 33.133±0.009 | <ins>10.026±0.123</ins> | **0.000±0.000** |

K=.7相对K=.5配对R@1 +0.179±0.094pp；eta=1.2/alpha=.1相对同seed基准的R@1 +0.084±0.093pp，但合法入锥−9.493±0.150pp。动态下界K=.7、q裕量0.1%相对初始化匹配固定下界：合法入锥+3.948±0.142pp、R@1−0.160±0.167pp。取消.21下界：R@1−0.008±0.000pp、合法入锥−0.403±0.066pp；实际训练没有r<.21的节点。

## 解释、局限与下一步

截断90°不是合法原锥；大K组起点可处于域外。动态下界K=.7三组统一r_init=1.3，不能与旧r_init=1的差异全归因于下界。下界同时改变参数化梯度。三seed是重复性检查，未证明测试集泛化或统计显著。

## 结果报告

[五K三seed](../summaries/recent-20261105/geodesic_seeds.md) · [大K三seed](../summaries/recent-20261105/large_k.md) · [eta×alpha三seed](../summaries/recent-20261105/eta_alpha.md) · [动态下界](../summaries/recent-20261105/domain_floor.md) · [取消固定下界](../summaries/recent-20261105/no_floor.md) · [历史单seed](../summaries/recent-20261105/geodesic_single.md) · [λ×K网格](../summaries/recent-20261105/geodesic_grid.md)

## 来源与复核范围

- 本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_lambda02_3seed_20261103/summary.csv`；SHA-256：`e8d34b794424efdb4835cb335d8461a44f9f07b0a2236918e280d92450e16fd1`。
- 本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_domain_floor_3seed_20261103/summary.csv`；SHA-256：`f7c45bdf1ed5e7b8b2fd9bdf6ab6493218d2265d5769862603da897b8ae9364b`。
- 本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_k05_no_floor_3seed_20261103/summary.csv`；SHA-256：`f952d8649a2fb62ae4c8fc0822460562934d79c766a534beea3045d1e04b0575`。

这里只读取并归档已有结果，没有重新训练或重新计算模型指标。完整数据、源码版本和运行细节留在上述来源及本地快照。
