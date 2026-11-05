# 角度候选下的ITM实验

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/angle_itm_20261102/REPORT.md`；SHA-256：`3996c130e1ddb5d45facec8043a786d0d363c3a2e555070e53df1f3ea4471a3e`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

已完成并核验 12 个2000步运行。只使用末轮，缺失条件不视为完成。

当前角度主干冻结；变化发生于ITM负例采样或残差输入。I0复用旧均匀ITM权重，重新评估同一角度Top32候选；其他条件从原始VAST matcher初始化。候选漏召回保留在分母。

| 运行 | R@1 | R@5 | R@10 | 候选R@32 |
|---|---|---|---|---|
| I0_s50 | 50.0488 | 71.1426 | 77.6611 | **84.5703** |
| I0_s51 | 49.4385 | 70.8008 | 77.3926 | **84.5703** |
| I0_s52 | 50.3174 | 70.9473 | 77.5146 | **84.5703** |
| I1_s50 | 50.8545 | 70.9717 | 77.6855 | **84.5703** |
| I1_s51 | 49.2920 | <ins>71.1914</ins> | 77.3926 | **84.5703** |
| I1_s52 | **51.1719** | **71.5820** | 77.6855 | **84.5703** |
| I2_s50 | <ins>51.0254</ins> | 71.1182 | <ins>77.8320</ins> | **84.5703** |
| I2_s51 | 49.6582 | 70.7031 | 77.5635 | **84.5703** |
| I2_s52 | <ins>51.0254</ins> | 71.0938 | **78.0518** | **84.5703** |
| I3_s50 | 50.9277 | 70.9717 | 77.7344 | **84.5703** |
| I4_s50 | 50.8057 | 71.0205 | 77.7344 | **84.5703** |
| I5_s50 | 50.8789 | 70.9961 | 77.7588 | **84.5703** |

三seed选择：I0；候选为I2，新的I0标准差0.4504pp，门槛0.9008pp。

完整配对差值：`/data0/xiaobo.xia/yuxuan.gao/angle_itm_20261102/SELECTION_LOCK.json`。

## 锁定后的外部结果

- I0_s50 / msrvtt: 双向R@1=45.8145%
- I0_s50 / vatex: 双向R@1=79.4281%
- I0_s51 / msrvtt: 双向R@1=46.4367%
- I0_s51 / vatex: 双向R@1=79.4771%
- I0_s52 / msrvtt: 双向R@1=45.9842%
- I0_s52 / vatex: 双向R@1=79.5425%

I3是额外角度输入/容量对照；I4是双曲几何；I5仅替换外角算子，保留半张角和半径，不代表完整欧氏训练。半径干预属于推理敏感性检查，不替代训练消融。异源负例不是人工标注语义非蕴含。

协议与实现（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angle_itm_20261102/README.md`） · CPU检查（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angle_itm_20261102/cpu_tests.json`） · GPU检查（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angle_itm_20261102/gpu_tests.json`） · 运行状态（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/angle_itm_20261102/logs/status.json`）
