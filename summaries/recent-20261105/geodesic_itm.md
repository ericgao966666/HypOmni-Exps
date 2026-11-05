# 测地线λ=.2主干的几何输入ITM对照

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_itm_geometry_20261103/REPORT.md`；SHA-256：`02de41c7d93b66ab10b9714b6e5396b5d2cf1d870a411ef7ffbd56bd1c467bb7`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

已完成并核验 15 个2000步运行。只使用末轮，缺失条件不视为完成。

当前λ=.2、曲率/温度可学习的测地线主干冻结；所有条件均使用同一均匀负例，只改变残差输入。D0复用旧均匀ITM权重，重新评估同一测地线Top32候选；其他条件从原始VAST matcher初始化。候选漏召回保留在分母。

| 运行 | R@1 | R@5 | R@10 | 候选R@32 |
|---|---|---|---|---|
| D0_s50 | 49.9268 | 70.8008 | 77.2949 | **84.1553** |
| D0_s51 | 49.5361 | 70.6543 | 76.8799 | **84.1553** |
| D0_s52 | **50.2197** | 70.6787 | 77.2217 | **84.1553** |
| D1_s50 | 50.0000 | 70.8252 | <ins>77.3193</ins> | **84.1553** |
| D1_s51 | 49.5850 | 70.7031 | 76.9531 | **84.1553** |
| D1_s52 | 50.0000 | 70.7031 | 77.1973 | **84.1553** |
| D2_s50 | 49.9756 | 70.7520 | **77.3438** | **84.1553** |
| D2_s51 | 49.5117 | 70.6787 | 76.9775 | **84.1553** |
| D2_s52 | <ins>50.1953</ins> | 70.7764 | 77.2461 | **84.1553** |
| D3_s50 | 50.0244 | <ins>70.8496</ins> | <ins>77.3193</ins> | **84.1553** |
| D3_s51 | 49.6338 | 70.7275 | 77.0508 | **84.1553** |
| D3_s52 | **50.2197** | 70.8252 | 77.1973 | **84.1553** |
| D4_s50 | 49.9756 | **70.8740** | **77.3438** | **84.1553** |
| D4_s51 | 49.5850 | 70.7275 | 77.0264 | **84.1553** |
| D4_s52 | <ins>50.1953</ins> | 70.7764 | 77.1973 | **84.1553** |

三seed选择：D0；候选为D3，新的D0标准差0.3430pp，门槛0.6859pp。

完整配对差值：`/data0/xiaobo.xia/yuxuan.gao/geodesic_itm_geometry_20261103/SELECTION_LOCK.json`。

## 锁定后的外部结果

- D0_s50 / msrvtt: 双向R@1=45.9842%
- D0_s50 / vatex: 双向R@1=78.8317%
- D0_s51 / msrvtt: 双向R@1=46.8326%
- D0_s51 / vatex: 双向R@1=78.8113%
- D0_s52 / msrvtt: 双向R@1=46.1538%
- D0_s52 / vatex: 双向R@1=78.9624%

D1为空特征容量对照；D2为仅距离；D3为完整双曲几何；D4将距离与外角改为切空间欧氏算子，保留相同半张角和径向坐标，不代表完整欧氏训练。半径干预属于推理敏感性检查，不替代训练消融。异源负例不是人工标注语义非蕴含。

协议与实现（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_itm_geometry_20261103/README.md`） · CPU检查（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_itm_geometry_20261103/cpu_tests.json`） · GPU检查（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_itm_geometry_20261103/gpu_tests.json`） · 运行状态（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_itm_geometry_20261103/logs/status.json`）
