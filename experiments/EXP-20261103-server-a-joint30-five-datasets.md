# 四方法 30 轮与五数据集：PMRL 外部均值最高，角度组在 MSRVTT 领先

[返回实验总览](../README.md) · `EXP-20261103-server-a-joint30-five-datasets` · 结果文件核对及文档更新 2026-11-19 UTC

四方法均已完成 30 轮训练和 **20/20** 项固定末轮测试。PMRL 的外部四集平均 ITM R@1 为 **48.605%**，比 GRAM 高 **0.433pp**。MSRVTT 上角度组为 **41.007%**，比该集次高的测地线组高 **1.358pp**。本比较为单 seed，各方法沿用各自原生预训练和 ITM 采样配方。

## 研究问题与关键设置

四方法目标预算均为VAST train82608、seed50、global batch256、30epoch/9660更新，T↔VA。测试可用视听交集：VAST2051、MSRVTT884、VATEX1224、ActivityNet3987、DiDeMo995视频；VATEX保留12240条caption。固定2帧/1窗/40token，ITM Top32，漏召回计未命中。

## 固定第 30 轮 ITM R@1 (%)

| 方法 | VAST | MSRVTT | VATEX | ActivityNet | DiDeMo | 外部四集平均 |
| --- | --- | --- | --- | --- | --- | --- |
| 测地线 | 47.489 | <ins>39.649</ins> | 70.576 | 29.621 | 29.296 | 42.286 |
| 角度 | 48.367 | **41.007** | 72.561 | 32.029 | 31.960 | 44.389 |
| PMRL | **51.999** | 37.613 | **78.734** | **39.478** | **38.593** | **48.605** |
| GRAM | <ins>48.415</ins> | 39.593 | <ins>77.610</ins> | <ins>37.748</ins> | <ins>37.739</ins> | <ins>48.172</ins> |

PMRL 在 VAST 和除 MSRVTT 外的三个外部集取得最高 ITM R@1。GRAM 的外部均值接近 PMRL，二者均高于这批设置下的两组自有方法。

## 解释与局限

可用媒体交集和输入预算与论文标准测试不同。PMRL/GRAM 使用原生 1:2 三组 CE 和采样，自有方法使用 1:1 均匀负例。末轮追加训练步数匹配，各自原生初始化、计算量和采样仍有差异。测地线训练遇到非有限梯度，从第 7,084 步检查点恢复同批次与随机状态并降低 AMP scale，未跳过数据。共同 VAST 起点的[固定 15 轮对照](EXP-20261106-server-b-vast-init-baselines.md)单独解读。

## 完整结果与来源

[20 项 R@1/5/10 与候选池结果](../summaries/recent-20261119/joint30.md) · [早期 15 项归档快照](../summaries/recent-20261105/joint30.md)

本地 `workspace/Hyperbolic-Omnimodal/code/experiments/joint30_five_datasets_20261103/REPORT.md`，SHA-256 `bfa18be8c2de7b34003e7cf7c356b151b2b081a02ff663810d7c38417df5aaba`。 逐方法、逐数据集评测和完成记录位于本地 `dataset_root/joint30_five_datasets_20261103/evaluation/`。本次核对 20 份结果文件哈希，未重跑实验。
