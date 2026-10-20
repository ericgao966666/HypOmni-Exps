# 多模态低维端到端几何对照

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-009 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已交接；目标服务器后续状态待核实 |
| 最近记录 / 最后核对 | 2026-10-19 / 2026-10-20 |
| 前序 | [MSRVTT 微调](EXP-006-msrvtt-finetune.md)、[几何对照](EXP-007-coco-geometry.md) |

## 要回答的问题

在 8/32/128/512 维和统一训练预算下，原生多模态方法、欧氏子集模型与双曲子集模型表现如何？锥约束与几何是否有可分离的贡献？

## 协议

MSRVTT 与 ActivityNet 两个数据集，7 种方法：原生 VAST/GRAM/PMRL，以及 hyp_cone、hyp_none、euc_cone、euc_none。四种维度，seed50，共 56 次运行。所有方法端到端训练 10 轮，全局 batch64，验证六方向 macro R@1 选模并包含 epoch0。

降维基仅用训练集拟合；D512 为新训练的对照，不复用 EXP-006 结果。四个子集分支共享初始化并使用 9 对对比目标。ActivityNet 使用本地检索评估 split，不声称使用隐藏挑战测试集。

解码前预计 train/val/test 数量：MSRVTT 7,427/500/884；ActivityNet 7,580/500/3,987。最终 cohort 必须以完成解码后的 READY manifest 为准。

## 当前进展与位置

- 实现与部分 CPU 验证已完成，源端缓存和验证流程为交接而停止。
- 当前交接只传源码与轻量标注，目标服务器重建缓存并继续验证。
- 尚未核实任何正式运行的有效 DONE 标记；没有可报告的训练成绩。

| 内容 | 位置 |
|---|---|
| 完整协议与入口 | [LOWDIM_README.md](../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/LOWDIM_README.md) |
| 当前交接方案 | [LOWDIM_SERVER_HANDOFF.md](../../Hyperbolic-Omnimodal/experiments/subset_hierarchy/LOWDIM_SERVER_HANDOFF.md) |
| 源端停止记录 | [stopped_for_handoff.json](../../Hyperbolic-Omnimodal/logs/lowdim_finetune_20261019/stopped_for_handoff.json) |
| CPU 验证与缓存日志 | [日志目录](../../Hyperbolic-Omnimodal/logs/lowdim_finetune_20261019/) |
| suite | [lowdim_finetune_20261019](</data-nfs/xiaoboxia/YuxuanGao/lowdim_finetune_20261019/>) |

## 下一步与变更

下一步核实目标服务器数据就绪、验证与正式队列状态，再回填结果；56 是计划运行数，不是完成数。

- 2026-10-19：按交接决定停止源端工作，保留代码和标注交接。
- 2026-10-20：补录，远端训练结果待核实。
