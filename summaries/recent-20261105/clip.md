# CLIP 直接微调补充比较

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`dataset_root/aurora_clip_finetune_20261101/REPORT.md`；SHA-256：`b59f2074b1982e641bb2e06cf377ba806b4ef7a63c2b2611ad1242e039ef0a80`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

标准整图-caption、余弦双向InfoNCE；相同初始化、seed50、batch768、1300步。CLIP无区域监督，不能单独将差异归因于几何。

| 方法 | COCO双向R@1均值 | 原生读出 |
|---|---:|---|
| clip | 23.037 | cosine |
| clip_initial | 17.856 | cosine |
| meru | 1.022 | distance |
| meru_boxes | 1.104 | distance |
| hycoclip | 1.026 | distance |
| aurora | 23.661 | cosine |
| aurora_no_hec | **23.729** | cosine |
| aurora_no_norm | 23.677 | cosine |
| aurora_nce | 22.965 | cosine |
| aurora_linear_norm | <ins>23.683</ins> | cosine |

开发集相同1000图：CLIP微调双向R@1=48.10%。此项不用于选参。

缺失结果保持缺失；欧氏CLIP不计算或伪造曲率、RAOC等双曲指标。置信区间仅为样本不确定性。

排名仅在相同训练阶段内比较；clip_initial是零追加更新的参考，不参加同预算排名。
