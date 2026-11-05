# MERU对数映射：L2几乎保持检索，余弦明显下降

[返回实验总览](../README.md) · `EXP-20261102-server-a-meru-logmap` · 归档核对：2026-11-05T08:39:54.407550+00:00

同一官方MERU权重、零训练读出替换中，logmap-L2的六项mean recall为34.427%，原生双曲为34.367%（+0.060pp，配对区间跨0）；logmap-cosine降至32.520%。这支持当前checkpoint上L2读出接近，不证明负曲率在一般任务中无用。

## 研究问题与关键设置

COCO val2017全5000图/25014caption，官方ViT-B/16权重冻结，FP64评分，候选索引稳定打破并列。2000次配对图像簇bootstrap、固定gallery；事前诊断容忍度±0.5pp。没有重新训练或选checkpoint。

## 主要结果

| 分数 | I→T R@1 | T→I R@1 | 六项mean recall |
|---|---|---|---|
| hyperbolic | <ins>19.700</ins> | **14.500** | <ins>34.367</ins> |
| logmap_l2 | **19.800** | <ins>14.496</ins> | **34.427** |
| logmap_cosine | 17.780 | 13.536 | 32.520 |


## 解释、局限与下一步

mean recall为双向R@1/5/10六项均值。区间只覆盖query图像抽样，不含训练种子或gallery变化；半径范围和距离失真仅作事后机制描述。需要跨checkpoint和任务后才能推广。

## 结果报告

[完整指标与诊断](../summaries/recent-20261105/meru_logmap.md)

## 来源与复核范围

- 本地 `workspace/meru-width-coco/experiments/meru_logmap_retrieval_20261102/results/results.json`；SHA-256：`a65540af3f054f0133b8764484d55821fae82a475ed5fe71deb00885de740143`。

这里只读取并归档已有结果，没有重新训练或重新计算模型指标。完整数据、源码版本和运行细节留在上述来源及本地快照。
