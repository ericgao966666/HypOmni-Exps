# 低维检索：64D双曲略优，跨维度优势尚不稳定

[返回实验总览](../README.md) · `EXP-20261021-server-b-retrieval-training` · 结果核对：2026-10-25 07:22 UTC；文档整理：2026-10-26

**64D双曲有锥R@1为22.13%，比欧氏高0.32个百分点，比PMRL高0.34个百分点；32/128/512D均是欧氏更好。严格锥包含率仍为0%。** 五方法64D结果完整，跨维度共14/20个选定条件有最终测试，另有2个历史R0对照。

## 研究问题与关键设置

延长微调、提高头部学习率、增加VAST头部预训练，能否改善低维检索，并得到可迁移的几何优势？先在64D验证集选方案，再把方案用于32/128/512D。

| 影响解读的设置 | 本轮口径 |
|---|---|
| 方法与数据 | 双曲有锥、欧氏无锥、VAST、GRAM、PMRL；MSRVTT 7,427/500/884，沿用固定缓存及train-only PCA |
| 候选方案 | R0：旧10轮基线；R1：共同初始化重训30轮；R2：10轮，提高头部学习率；R3：VAST头部8轮warmup＋30轮冻结训练，再微调10轮 |
| 选择规则 | 每方法仅按64D seed50验证六方向macro R@1选方案；同分按R@5、较少更新和预定方案顺序；每个checkpoint也由验证集选择，包含epoch0 |
| 固定条件 | 仅seed50，联合微调全局batch64；双曲λ=.1，欧氏λ=0；测试不参与方案选择 |
| 指标与范围 | 同一MSRVTT test884、六方向macro，单位%；本轮不新增8D/16D，跨方案训练预算并不相同 |

验证选定方案为双曲/欧氏/GRAM的R1，VAST/PMRL的R3。[四候选验证表](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/validation_candidates_64d.csv)与以下测试结果分开保存。

## 主要结果

最优加粗、次优下划线；仅在同列已完成方法中排名，缺失不记零。单seed结果不代表统计显著性。

## 跨维度 R@1（%）

| 方法 | 选定方案 | 32D | 64D | 128D | 512D |
|---|---|---:|---:|---:|---:|
| 双曲有锥 | R1 | <ins>17.70</ins> | **22.13** | <ins>23.96</ins> | <ins>24.08</ins> |
| 欧氏无锥 | R1 | **18.23** | <ins>21.81</ins> | **24.62** | **24.70** |
| PMRL | R3 | 待完成 | 21.79 | 待完成 | 待完成 |
| VAST | R3 | 待完成 | 18.70 | 待完成 | 待完成 |
| GRAM | R1 | 14.48 | 16.53 | 17.78 | 19.27 |

## 64D完整测试与验证选择的checkpoint

| 方法 | 方案 | 最佳epoch | R@1 (%) | R@5 (%) | R@10 (%) |
|---|---|---:|---:|---:|---:|
| 双曲有锥 | R1 | 26 | **22.13** | <ins>45.98</ins> | <ins>57.24</ins> |
| 欧氏无锥 | R1 | 22 | <ins>21.81</ins> | **46.02** | **57.69** |
| PMRL | R3 | 8 | 21.79 | 45.70 | 56.39 |
| VAST | R3 | 9 | 18.70 | 40.63 | 50.96 |
| GRAM | R1 | 7 | 16.53 | 33.20 | 41.69 |


## 解释与局限

- 64D双曲相对自身R0提升2.4510个百分点，说明本轮方案有检索收益；相对欧氏和PMRL仅领先0.3205和0.3394个百分点。
- 32/128/512D欧氏分别领先双曲0.5279/0.6599/0.6222个百分点，当前没有稳定跨维度双曲优势。
- 不同方法通过验证选择了不同训练方案，训练预算不一致；该比较评估整套方案，不能单独识别曲率或锥约束的因果贡献。
- VAST和PMRL的32/128/512D共6个条件未完成，所以跨维度最优仍只是当前已完成结果。仅seed50，不能报告训练种子稳定性。

## 已完成双曲方案的验证集几何可视化

2026-10-23：已用同一批验证视频比较R0/R1/R2/R3的HoroPCA和CO-SNE。R3原空间单/双/三模态平均半径约1.265/1.679/3.168，R0则约0.996/1.005/1.014；仅延长微调的R1仍较接近半径1。R3两种投影均显示TVA外移，其半径相关性分别为0.863和0.979，但严格锥满足率仍为0%。数据和训练阶段同时变化，不能只归因于训练轮数。详见[完整图文与数值](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/README.md)。

![R0与R3的HoroPCA、CO-SNE及原空间半径](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/geometry_R0_vs_R3.png)

图左/中为固定48个验证视频×7子集，训练及投影seed50；右侧为全部500验证视频的原空间半径。各方案使用按检索选出的checkpoint，颜色为子集类型，灰线不代表包含成立。未使用最终测试集。[完整四页PDF](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/geometry_validation_report.pdf) · [R1/R2图](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/geometry_R1_vs_R2.png) · [原空间CSV](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/native_geometry.csv) · [保真度CSV](../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/projection_quality.csv)。


## 下一步判断与完成范围

先补齐VAST、PMRL的6个扩维条件，才能评价完整跨方法趋势；若要解释几何机制，需进一步使用匹配预算的欧氏/双曲及锥约束消融。

截至2026-10-25的运行观察，训练已中断，VAST32D warmup保留第5轮检查点，原因未确认。[运行状态证据](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/runtime_observation.json)与[历史启停记录](../runs/EXP-20261021-server-b-retrieval-training/history-before-results-rewrite-20261026.md)供恢复时查阅；本次文档重写没有重新检查或启动训练。

## 完整结果与来源

[完整结果说明](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/README.md) · [汇总CSV](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/test_macro.csv) · [六方向CSV](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/test_directions.csv) · [原始测试JSON](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/evaluations/) · [全体选择锁](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/SELECTIONS_LOCKED.json) · [R0对照](../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/baseline_r0_64d.json)。

[运行索引](../runs/EXP-20261021-server-b-retrieval-training/README.md)及历史快照保留数据、源码和检查点来源；结果依据记录中的实际运行源码快照，不以当前代码HEAD替代。
