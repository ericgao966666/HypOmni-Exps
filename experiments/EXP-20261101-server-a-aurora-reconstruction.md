# AURORA受控重建：检索收益未证明HEC独立贡献

[返回实验总览](../README.md) · `EXP-20261101-server-a-aurora-reconstruction` · 归档核对：2026-11-05T08:39:54.407550+00:00

11/11主条件评测完成，另补直接微调CLIP。COCO双向R@1：AURORA23.661%、CLIP23.037%，差值+0.624pp；去HEC的AURORA为23.729%，不支持这轮HEC带来额外检索收益。

## 研究问题与关键设置

独立公式重建，非未公开作者代码。GRIT100k/5k/5k；ViT-B微调8组共用本地CLIP初始权重、batch768/1300步，ViT-S从头3组5000步，seed50。COCO5000图/25014caption，原生读出分别报告。CLIP补充同预算但只有整图caption监督。

## 主要结果

| 微调方案 | COCO双向R@1 (%) | 原生分数 |
|---|---|---|
| clip | 23.037 | cosine |
| meru | 1.022 | distance |
| meru_boxes | 1.104 | distance |
| hycoclip | 1.026 | distance |
| aurora | 23.661 | cosine |
| aurora_no_hec | **23.729** | cosine |
| aurora_no_norm | 23.677 | cosine |
| aurora_nce | 22.965 | cosine |
| aurora_linear_norm | <ins>23.683</ins> | cosine |

零追加更新的初始CLIP为17.856%，作为参考单列，不参加同预算排名。主指标是I→T与T→I micro R@1的均值。

从头阶段必须单列：MERU0.268%、HyCoCLIP0.204%、AURORA0.412%，不与微调表混排。

## 解释、局限与下一步

CLIP减AURORA的图像配对bootstrap区间为[−1.160,−0.116]pp，只反映样本抽样，不代表训练seed稳健性。区域监督、原生损失、读出和重建细节不同，不能将差值单独归因于负曲率。MERU/HyCoCLIP在本轮短预算下表现很低，不等于官方模型能力。BF16编码器/FP32几何、共同PIL预处理、权重衰减分组和reduction歧义均按源码协议保留。

## 结果报告

[11条件报告](../summaries/recent-20261105/aurora.md) · [CLIP直接微调补充](../summaries/recent-20261105/clip.md)

## 来源与复核范围

- 本地 `dataset_root/aurora_reproduction_20261101/summary.json`；SHA-256：`3b8e05fd7a94a544b1d95a71d5674b27fb552f28423ac0fa913352a1110b1884`。
- 本地 `dataset_root/aurora_clip_finetune_20261101/comparison.json`；SHA-256：`c231cd86fa23c423a129c6916bf3cc867d7b80f3b77086105baf5b29d2b1d0bf`。

这里只读取并归档已有结果，没有重新训练或重新计算模型指标。完整数据、源码版本和运行细节留在上述来源及本地快照。
