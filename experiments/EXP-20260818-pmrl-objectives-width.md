# PMRL 早期目标与宽度：低维表现随初始化和协议改变

[返回实验总览](../README.md) · `EXP-20260818-pmrl-objectives-width` · 原结果 2026-08-02 至 08-18 · 文档更新 2026-11-19

早期 VAST 训练的四集 TV 检索中，text-anchor 双曲谱目标的直接 R@10 为 **68.1750%**，比同评测的 VAST 高 **0.2375pp**。加 entailment 的配置最高 Top-20 R@10 为 **75.0500%**，比 PMRL 高 **0.2250pp**，该配置还用了梯度累积。8D 直接训练有单 seed 正信号，严格配对的 64D post-head 比较则回落。

## 研究问题与关键设置

VAST 初始化，先比较对齐目标、半径读出和 Top-20 ITM，再分别测试直接低维训练和从 512D checkpoint 扩展低维 head。目标表是四集 TV R@10 的历史可比读出，ITM 开关和 entailment 配方随行注明。更晚的三 seed 零样本和基线协议详见 [EXP-001](EXP-001-zero-shot-baselines.md)。

| 配置 | 直接检索 R@10 | Top-20 R@10 |
| --- | --- | --- |
| VAST（同 TV 评测） | <ins>67.9375</ins> | 73.3000 |
| PMRL（同 TV 评测） | 67.2875 | 74.8250 |
| 欧氏 spectral tuple + ITM | 66.2375 | 74.8500 |
| 双曲 direction-radius spectral + ITM | 66.0500 | 74.9125 |
| 双曲 text-anchor + ITM | **68.1750** | <ins>74.9875</ins> |
| 双曲 text-anchor + entailment + ITM | 67.6125 | **75.0500** |

## 主要结果与局限

- 在冻结特征方向反事实中，保留学习半径的 TV R@10 为 49.9188%，把半径固定为模态均值后为 49.1375%，打乱样本半径为 48.0750%。全量训练后固定半径的差值缩小到 −0.0625pp，说明短程读出不能直接外推。
- VAST→MSRVTT 的单 seed Direct 8D 实验中，六项 R@1/5/10 均值为欧氏 28.0167%、双曲无 entailment 30.6000%、双曲加 entailment 30.9500%。同一双曲 checkpoint 固定半径读出为 31.1000%。冻结 ImageBind 的独立 D8 test 差值为 +0.87pp，验证集未复现。
- 08-17 的旧欧氏项是 eigengap 类比。08-18 采用原版 PMRL 配对 checkpoint 后，固定 entailment=.2 的两个双曲方法在 D64 分别落后各自欧氏组 1.89/1.38pp。MERU/CLIP 的 COCO 五轮低维对照同时改变骨干和预训练，适用于压缩比较。

## 结果来源

本地 `workspace/PMRL/LOSS_DESIGN_FORMAL_RESULTS.md`，SHA-256 `df47440862acc07c5b45d3ca0b42b001e65b80908eaa4e9ca5bd494c3aa89407`。

本地 `workspace/PMRL/HYPERBOLIC_GEOMETRY_UTILIZATION_RESULTS.md`，SHA-256 `7e8f11ed2dbc32ae08cb3db4ea2ba69e4c5c4546602e34ce9fdbcbfc35617cdf`。

本地 `workspace/PMRL/TEXT_ANCHOR_SPECTRAL_EXPERIMENT_SUMMARY.md`，SHA-256 `6bb1f97935ae7535b297b18a8558f22390415e55ec0a0c7b3d3a5a56db48854b`。

本地 `workspace/PMRL/HYPERBOLIC_WIDTH_EXPERIMENT_SUMMARY.md`，SHA-256 `adf7b947a94eab55eb277b825cd487cc21279cf992ab447a142ff20a56a255eb`。

本地 `workspace/PMRL/LATEST_LOW_DIMENSION_EXPERIMENT_20260818.md`，SHA-256 `4ce281168a1ce0b1bb4f37d6b4b27e8e787f740d9fe21c7d59f9b667d4aa8a70`。

本地 `workspace/PMRL/MAIN_ZERO_SHOT_EXPERIMENT_SUMMARY_20260818.md`，SHA-256 `3015b3e7d64fb8c5940c52d0e51658ac0a0527b712b367639e126e9035e4f101`。
