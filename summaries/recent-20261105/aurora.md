# AURORA controlled reproduction

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`dataset_root/aurora_reproduction_20261101/REPORT.md`；SHA-256：`2d4c88b1d17a5fa90c89aec966c98a6a002be2b640afd031424c3ff9ea19dd63`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

Completed evaluations: 11/11. Single seed 50.

| Phase | Arm | COCO mean R@1 | Score |
|---|---|---:|---|
| finetune | meru | 1.022 | distance |
| finetune | meru_boxes | 1.104 | distance |
| finetune | hycoclip | 1.026 | distance |
| finetune | aurora | 23.661 | cosine |
| finetune | aurora_no_hec | **23.729** | cosine |
| finetune | aurora_no_norm | 23.677 | cosine |
| finetune | aurora_nce | 22.965 | cosine |
| finetune | aurora_linear_norm | <ins>23.683</ins> | cosine |
| scratch | meru | <ins>0.268</ins> | distance |
| scratch | hycoclip | 0.204 | distance |
| scratch | aurora | **0.412** | cosine |

Missing:

No missing results are imputed. Fine-tuning and scratch results are separate comparisons.
Geometry, radial order and task performance are separate claims. Bootstrap intervals measure image sampling only, not training-seed robustness.

微调与从头训练分别排名；各模型保留原生读出，数值比较不单独识别曲率贡献。
