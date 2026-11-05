# MERU零训练对数映射检索

> 归档核对：2026-11-05T08:39:54.407550+00:00；本页由本地机器结果汇总，来源位置及SHA-256见文末。未重跑实验。

| 分数 | I→T R@1 | T→I R@1 | 六项mean recall |
|---|---|---|---|
| hyperbolic | <ins>19.700</ins> | **14.500** | 34.367 |
| logmap_l2 | **19.800** | <ins>14.496</ins> | 34.427 |
| logmap_cosine | 17.780 | 13.536 | 32.520 |

同一官方MERU ViT-B/16、COCO val2017全候选池、FP64评分；六项是双向R@1/5/10的均值，不能与双向R@1均值混用。

logmap-L2减原生双曲mean recall为+0.060002pp，图像簇配对bootstrap区间[−0.001996,+0.116668]pp；所有六项区间均处于事前±0.5pp诊断容忍度内。这不是通用几何等价定理。logmap-cosine为−1.847611pp，区间[−2.083014,−1.620961]pp。

正配对和随机配对的双曲距离相对logmap-L2距离超出均值约0.555%/0.533%；仅为事后描述，不用于选模型或指标。完整top10复核通过。

## 来源与复核范围

- 本地 `workspace/meru-width-coco/experiments/meru_logmap_retrieval_20261102/results/results.json`；SHA-256：`a65540af3f054f0133b8764484d55821fae82a475ed5fe71deb00885de740143`。
- 本地 `workspace/meru-width-coco/experiments/meru_logmap_retrieval_20261102/results/verification_geometry.json`；SHA-256：`9f4d712e9abd88518d5477d452d2e5c77050f288378470257baad5766ad0b665`。

这里只读取并归档已有结果，没有重新训练或重新计算模型指标。完整数据、源码版本和运行细节留在上述来源及本地快照。
