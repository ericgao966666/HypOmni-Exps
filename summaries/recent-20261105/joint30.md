# 四方法30epoch训练与五数据集测试

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/experiments/joint30_five_datasets_20261103/REPORT.md`；SHA-256：`fb1326c1e55f65c791addd82481f9c4bfa30cc1a2df10864ce4f6d3bf2f3c19d`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

完成正式评测 15/20 项。尚缺 5 项；未完成结果不填充。

所有模型seed50、VAST同一82608条训练数据、全局batch256、固定第30轮；主任务T↔VA。原生预训练权重与ITM采样配方不同，仅匹配追加训练预算。所有caption保留，Top32漏召回计未命中。当前媒体交集和2帧/1窗/40token统一协议不是标准全量榜单。

## vast

| 方法 | 视频 | Caption | ITC R@1 | ITC R@5 | ITC R@10 | ITM R@1 | ITM R@5 | ITM R@10 | 候选R@32 |
|---|---|---|---|---|---|---|---|---|---|
| geodesic | 2051 | 2051 | 26.499 | 50.049 | 59.824 | 47.489 | 64.651 | 70.185 | 75.280 |
| angular | 2051 | 2051 | <ins>29.937</ins> | <ins>53.754</ins> | <ins>63.335</ins> | <ins>48.367</ins> | <ins>66.431</ins> | <ins>72.647</ins> | <ins>77.791</ins> |
| pmrl | 2051 | 2051 | **39.322** | **61.238** | **68.966** | **51.999** | **70.502** | **76.694** | **81.643** |

## msrvtt

| 方法 | 视频 | Caption | ITC R@1 | ITC R@5 | ITC R@10 | ITM R@1 | ITM R@5 | ITM R@10 | 候选R@32 |
|---|---|---|---|---|---|---|---|---|---|
| geodesic | 884 | 884 | 17.590 | 41.629 | 52.998 | <ins>39.649</ins> | <ins>59.785</ins> | 67.138 | 72.398 |
| angular | 884 | 884 | <ins>21.663</ins> | <ins>47.172</ins> | <ins>58.710</ins> | **41.007** | **61.991** | <ins>69.061</ins> | <ins>74.548</ins> |
| pmrl | 884 | 884 | **37.274** | **62.048** | **71.210** | 37.613 | **61.991** | **72.398** | **82.862** |

## vatex

| 方法 | 视频 | Caption | ITC R@1 | ITC R@5 | ITC R@10 | ITM R@1 | ITM R@5 | ITM R@10 | 候选R@32 |
|---|---|---|---|---|---|---|---|---|---|
| geodesic | 1224 | 12240 | 37.504 | 67.169 | 77.422 | 70.576 | 86.940 | 89.571 | 90.629 |
| angular | 1224 | 12240 | <ins>43.889</ins> | <ins>74.020</ins> | <ins>83.603</ins> | <ins>72.561</ins> | <ins>89.751</ins> | <ins>92.602</ins> | <ins>93.603</ins> |
| pmrl | 1224 | 12240 | **67.373** | **91.042** | **95.380** | **78.734** | **95.078** | **97.300** | **98.382** |

## activitynet

| 方法 | 视频 | Caption | ITC R@1 | ITC R@5 | ITC R@10 | ITM R@1 | ITM R@5 | ITM R@10 | 候选R@32 |
|---|---|---|---|---|---|---|---|---|---|
| geodesic | 3987 | 3987 | 10.622 | 27.013 | 37.284 | 29.621 | 47.517 | 53.474 | 56.396 |
| angular | 3987 | 3987 | <ins>13.381</ins> | <ins>33.271</ins> | <ins>44.507</ins> | <ins>32.029</ins> | <ins>52.772</ins> | <ins>60.045</ins> | <ins>64.936</ins> |
| pmrl | 3987 | 3987 | **26.486** | **53.712** | **65.927** | **39.478** | **65.676** | **74.893** | **83.559** |

## didemo

| 方法 | 视频 | Caption | ITC R@1 | ITC R@5 | ITC R@10 | ITM R@1 | ITM R@5 | ITM R@10 | 候选R@32 |
|---|---|---|---|---|---|---|---|---|---|
| geodesic | 995 | 995 | 8.945 | 24.523 | 33.819 | 29.296 | 45.226 | 49.598 | 53.015 |
| angular | 995 | 995 | <ins>12.010</ins> | <ins>30.402</ins> | <ins>41.055</ins> | <ins>31.960</ins> | <ins>49.799</ins> | <ins>55.377</ins> | <ins>59.899</ins> |
| pmrl | 995 | 995 | **27.990** | **54.322** | **64.020** | **38.593** | **60.503** | **69.397** | **76.935** |


方案与解释边界（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/joint30_five_datasets_20261103/PLAN.md`） · 运行状态（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/joint30_five_datasets_20261103/status.json`） · 数据规模（本地 `workspace/Hyperbolic-Omnimodal/code/experiments/joint30_five_datasets_20261103/input_summary.json`）
