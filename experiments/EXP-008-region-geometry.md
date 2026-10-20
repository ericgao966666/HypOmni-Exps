# HyCoCLIP 与 UNCHA 区域层级几何对照

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-008 |
| 项目 | meru-width-coco |
| 状态 | 已交接；目标服务器后续状态待核实 |
| 最近记录 / 最后核对 | 2026-10-19 / 2026-10-20 |
| 前序 | [冻结 CLIP 几何对照](EXP-007-coco-geometry.md) |

## 要回答的问题

在包含整图、caption、区域和 phrase 的监督中，HyCoCLIP / UNCHA 的双曲版本是否比欧氏迁移版本学到更有效的层级结构？

## 已冻结的计划

GRIT 子集训练 100,000 图像、开发 5,000、测试 5,000；512 维。计划 32 次运行：12 次冻结全目标、4 次无蕴含控制、4 次合法域诊断、12 次骨干与头部联合训练。每阶段 5,000 步、全局 batch 256。三个主实验种子为 0/1/2，诊断使用 seed0。

完整[实验说明](../../meru-width-coco/REGION_GEOMETRY.md)与[源服务器配置](../../meru-width-coco/configs/width_experiment/region_geometry.json)。

## 当前证据

数据准备已完成，训练/开发/测试分别含 236,474 / 11,688 / 11,744 个区域。实现及 smoke/容量检查已做，但这些不是正式实验结果。

2026-10-19 源流水线停止用于迁移，状态明确要求不在迁移中启动训练。迁移校验记录为通过，125,312 文件，`training_started=false`。该值仅代表交接时状态。

| 内容 | 位置 |
|---|---|
| 源运行目录 | [region_geometry_v1](../../meru-width-coco/output/region_geometry_v1/) |
| 数据状态 | [data_status.json](../../meru-width-coco/output/region_geometry_v1/data_status.json) |
| 停止与交接状态 | [pipeline_status.json](../../meru-width-coco/output/region_geometry_v1/pipeline_status.json) |
| 交接说明 | [SERVER2_HANDOFF.md](../../meru-width-coco/.tmp/server2-migration-fzmlgq9d/project/SERVER2_HANDOFF.md) |
| 迁移校验 | [verification.json](../../meru-width-coco/.tmp/server2-migration-fzmlgq9d/verification.json) |
| 数据与大型缓存 | [hyco_uncha_geometry](</data-nfs/xiaoboxia/YuxuanGao/hyco_uncha_geometry/>) |

交接说明和校验记录当前位于 `.tmp`；它们仍是本次交接证据，不应当作无用临时文件清理。

## 结果与下一步

尚无本机正式结果，不能给出几何胜负。下一步是核实目标服务器上的运行状态，回填其配置、run ID 与报告路径。目标服务器的新训练或访问应遵守原授权范围；本卡不代表启动授权。

## 变更记录

- 2026-10-18 至 19：完成数据与执行准备，进行特征缓存；随后停止并迁移。
- 2026-10-20：补录，仅确认交接记录，不推断远端已训练完成。
