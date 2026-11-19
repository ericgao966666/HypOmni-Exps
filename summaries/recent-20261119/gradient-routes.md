# 梯度路由对照的固定轮次外部评测

[返回实验卡](../../experiments/EXP-20261110-server-b-geodesic-gradient-routes.md) · 源报告核对 2026-11-11 10:18 UTC · 文档更新 2026-11-19

三组共享第 5 轮起点。`joint` 复用历史正常联合训练，`frozen` 冻结主干，`stop_cone` 阻断 cone 损失到主干的梯度。固定外部读出轮次为 7 和 10。数据集此前已查看，以下为探索性测试。

### 第 7 轮 · msrvtt

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>32.353</ins> | <ins>45.362</ins> |
| frozen | 29.129 | 40.781 |
| stop_cone | **32.466** | **45.701** |

### 第 7 轮 · vatex

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>61.736</ins> | <ins>78.717</ins> |
| frozen | 54.918 | **78.844** |
| stop_cone | **61.830** | 78.644 |

### 第 7 轮 · activitynet

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>23.689</ins> | **39.102** |
| frozen | 20.241 | 37.309 |
| stop_cone | **23.790** | <ins>38.901</ins> |

### 第 7 轮 · didemo

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>21.256</ins> | <ins>41.709</ins> |
| frozen | 20.151 | 36.281 |
| stop_cone | **21.709** | **41.759** |

### 第 10 轮 · msrvtt

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>31.052</ins> | **44.231** |
| frozen | 30.600 | 41.120 |
| stop_cone | **31.165** | <ins>43.948</ins> |

### 第 10 轮 · vatex

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>60.384</ins> | <ins>78.064</ins> |
| frozen | 57.075 | **78.962** |
| stop_cone | **60.531** | 78.051 |

### 第 10 轮 · activitynet

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | <ins>21.859</ins> | **37.986** |
| frozen | 21.232 | <ins>37.710</ins> |
| stop_cone | **22.022** | 37.597 |

### 第 10 轮 · didemo

| 条件 | ITC R@1 (%) | ITM R@1 (%) |
| --- | --- | --- |
| joint | 19.196 | <ins>38.643</ins> |
| frozen | **20.704** | 36.683 |
| stop_cone | <ins>19.749</ins> | **39.246** |

本地 `workspace/Hyperbolic-Omnimodal/code/experiments/geodesic_gradient_routes_20261110/REPORT.md`，SHA-256 `a73cf13e25c3324c019fe563e3177c1155b9cdb7477b93b98fa575772820ff0a`。 完整逐轮验证、各子集半径与标准差见本地源报告和同目录 `validation.csv`。
