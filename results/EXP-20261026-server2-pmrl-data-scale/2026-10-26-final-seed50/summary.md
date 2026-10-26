# PMRL 数据扩充前后：seed50、各一个epoch

两组均在 server2 GPU 4–7 重新训练，使用末轮 checkpoint。R@1 单位为%，Δ为百分点。

| 阶段 | 数据集 | 方向 | 旧数据 R@1 | 新数据 R@1 | Δpp |
|---|---|---|---:|---:|---:|
| direct | msrvtt | t2v | **44.23** | <ins>43.78</ins> | -0.45 |
| direct | msrvtt | v2t | <ins>42.08</ins> | **42.87** | +0.79 |
| direct | didemo | t2v | **34.37** | <ins>33.47</ins> | -0.90 |
| direct | didemo | v2t | **36.68** | <ins>35.48</ins> | -1.21 |
| direct | activitynet | t2v | <ins>39.98</ins> | **40.01** | +0.03 |
| direct | activitynet | v2t | **34.96** | **34.96** | +0.00 |
| direct | vatex | t2v | <ins>68.14</ins> | **68.87** | +0.74 |
| direct | vatex | v2t | <ins>64.05</ins> | **64.30** | +0.25 |
| itm_top50 | msrvtt | t2v | <ins>55.09</ins> | **55.20** | +0.11 |
| itm_top50 | msrvtt | v2t | <ins>52.71</ins> | **53.62** | +0.90 |
| itm_top50 | didemo | t2v | **53.47** | <ins>52.86</ins> | -0.60 |
| itm_top50 | didemo | v2t | <ins>50.75</ins> | **52.66** | +1.91 |
| itm_top50 | activitynet | t2v | **55.93** | <ins>55.91</ins> | -0.03 |
| itm_top50 | activitynet | v2t | <ins>49.89</ins> | **50.41** | +0.53 |
| itm_top50 | vatex | t2v | **79.90** | <ins>79.33</ins> | -0.57 |
| itm_top50 | vatex | v2t | <ins>74.84</ins> | **75.49** | +0.65 |

direct 八方向平均：旧组 45.5626，新组 45.4669，Δ -0.0957 pp；配对样本 bootstrap 95% 区间 [-0.4827, +0.2740] pp。

itm_top50 八方向平均：旧组 59.0730，新组 59.4365，Δ +0.3635 pp；配对样本 bootstrap 95% 区间 [-0.0872, +0.8112] pp。

样本量及 batch 数：{"old": {"samples": 86706, "manifest_path": "/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/assets/old.json", "sha256": "a38cec1508131b4479788f8907971abd9efff91db3a7004e13f1cea86e350d95", "batches": 1354}, "expanded": {"samples": 105369, "manifest_path": "/data-nfs/xiaoboxia/YuxuanGao/PMRL/outputs/data-scale-20261026/assets/expanded.json", "sha256": "25fe529dc0b6d820591a04586c82c2175813fdee46f6a985c1282dc70a6a387e", "batches": 1646}}

单seed不能估计训练随机性。新组数据量和训练步数同时增加；新增媒体来源及编码也有差异。Bootstrap 固定模型和候选库，不代表多seed置信区间。

[完整指标](results.csv) · [机器结果](results.json)
