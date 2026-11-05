# 2026-10-28至11-05近期实验补录

归档核对：2026-11-05T08:39:54.407550+00:00。只读取已有结果；未启动、停止或修改训练。详细数据、模型、图件和运行记录仍只存本地。

| 研究问题 | 当前结论 | 范围 |
|---|---|---|
| [锥训练参数：改善局部满足仍未形成完整层级](../../experiments/EXP-20261029-server-a-cone-parameters.md) | K=.3合法满足12.869%，检索−0.684pp | 已完成 |
| [原C0几何控制：双曲无锥略优，锥约束有检索代价](../../experiments/EXP-20261030-server-a-c0-geometry.md) | 512D无锥双曲R@1 19.019%，欧氏18.783% | 已完成 |
| [R3固定曲率：64D验证候选小幅提高，尚无新测试](../../experiments/EXP-20261029-server-a-r3-curvature.md) | 固定c=.3/τ=.035：MSRVTT验证28.467% | 已完成 |
| [ARGENT/AURORA组件：角度检索提高，样本特异层级未证实](../../experiments/EXP-20261030-server-a-argent-components.md) | S主读出19.173%，相对B0 +0.423pp | 已完成 |
| [角度对齐：减轻蕴含的检索代价，完整合法层级仍失败](../../experiments/EXP-20261101-server-a-angular-alignment.md) | A0 18.970%，相对距离带锥+0.220pp | 已完成 |
| [测地线K与半径下界：检索回升可重复，合法域仍是瓶颈](../../experiments/EXP-20261103-server-a-geodesic-domain.md) | K=.3→.5三seed回升+0.564±0.125pp | 已完成 |
| [Gromov product：46组探索未找到可信的替代收益](../../experiments/EXP-20261102-server-a-gromov-alignment.md) | GP_E仅+0.024pp，区间跨0 | 已完成 |
| [ITM几何输入：两套三seed门槛均保留原均匀基线](../../experiments/EXP-20261103-server-a-itm-geometry.md) | I2/D3均未过门槛，锁定I0/D0 | 已完成 |
| [模态组合锥与理想根：18条件均未通过预设双目标](../../experiments/EXP-20261103-server-a-cone-root.md) | 18/18完成，均未过双目标门槛 | 已完成 |
| [四方法30轮与五数据集：已完成15/20项，GRAM仍缺](../../experiments/EXP-20261103-server-a-joint30-five-datasets.md) | 15/20项；MSRVTT角度ITM 41.007%，GRAM缺失 | 部分完成：15/20测试 |
| [官方锥审计：高表观满足掩盖定义域问题](../../experiments/EXP-20261029-server-a-official-cone-audit.md) | 表观98–100%，合法覆盖0–1.371% | 已完成 |
| [AURORA受控重建：检索收益未证明HEC独立贡献](../../experiments/EXP-20261101-server-a-aurora-reconstruction.md) | AURORA23.661%，CLIP23.037%；去HEC23.729% | 已完成 |
| [MERU对数映射：L2几乎保持检索，余弦明显下降](../../experiments/EXP-20261102-server-a-meru-logmap.md) | logmap-L2 mean recall34.427%，原生34.367% | 已完成 |

## 报告入口

- [K、eta、alpha 训练对照结果](cone_training.md)
- [ARGENT / AURORA 组件对照结果](argent.md)
- [角度对齐、原始 entailment 与范数正则](angular.md)
- [测地线／角度 InfoNCE：entailment weight × K](angle_grid.md)
- [测地线 InfoNCE：entailment weight × K 补齐结果](geodesic_grid.md)
- [补充：λ = 0.2 的测地线 K 扫描与分层几何](geodesic_single.md)
- [补充：λ = 0.2 测地线 K 扫描，统一实现三 seed 重跑](geodesic_seeds.md)
- [补充：更大 K 的三 seed 实验（λ = 0.2，测地线）](large_k.md)
- [补充：K = 0.5、λ = 0.2 的 eta × alpha 三 seed 扫描](eta_alpha.md)
- [补充：λ = 0.2 的角度 K 扫描与分层几何（单 seed）](angular_k.md)
- [补充：随 K 与曲率变化的半径下界，三 seed 对照](domain_floor.md)
- [补充：K = 0.5 取消固定0.21半径下界，三 seed 对照](no_floor.md)
- [Gromov product 对齐：可行性排序、实验与结论](gromov.md)
- [角度候选下的ITM实验](angle_itm.md)
- [测地线λ=.2主干的几何输入ITM对照](geodesic_itm.md)
- [模态组合锥与理想根实验](cone_root.md)
- [四方法30epoch训练与五数据集测试](joint30.md)
- [官方 HyCoCLIP / UNCHA checkpoint 锥蕴含审计](official_cone.md)
- [AURORA controlled reproduction](aurora.md)
- [CLIP 直接微调补充比较](clip.md)
- [λ=0.25：曲率与温度联合学习的匹配实验](lambda025.md)
- [C0欧氏/双曲控制](c0_geometry.md)
- [R3曲率与维度](r3_curvature.md)
- [MERU对数映射](meru_logmap.md)

## 本地来源清单

本次来源逐文件快照及SHA-256清单：本地 `results/recent-20261105/manifest.json`。活跃实验仅记录捕获时状态；GRAM五项缺失保留。具体访问方式见[本地证据说明](../../LOCAL_ARTIFACTS.md)。
