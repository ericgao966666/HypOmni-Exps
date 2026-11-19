# MSRVTT：迁移 VAST 子集 head 提高目标域检索

[返回实验总览](../README.md) · `EXP-20261107-server-b-msrvtt-head-init` · 源报告核对 2026-11-09 05:26 UTC · 文档更新及结果文件核对 2026-11-19 UTC

六组都完成 2+8 轮。MSRVTT 验证集选定的检索主模型在 884 个测试视频上，VAST head 迁移组相对同 K 直接微调组的双向 **ITC R@1 提高 10.463–11.538pp，ITM R@1 提高 1.357–1.923pp**。迁移组在另外四个评测集上也均高于同 K 对照。这是三个设置上的一致方向，来自同一训练 seed；迁移组另有 1,610 步 VAST head 预训练。

## 研究问题与关键设置

已有VAST子集训练的外部曲线提示联合训练后期迁移退化，但不能把原因单独归于head。新实验隔离head初始化，检验其对MSRVTT检索和严格锥包含的影响。

| 设置 | 本轮口径 |
|---|---|
| 数据 | MSRVTT train/val/test=7427/500/884，ID互斥；884视听齐全测试视频，与上一轮相同，不是完整MSRVTT-1K |
| 初始化 | fresh：原始VAST＋固定seed50新head；vast_head5：同一VAST＋对应K的VAST第5轮head，仅继承模型参数 |
| 几何 | 512D，测地线对齐，λ=0.2，曲率和温度可学习，沿用物理半径参数化 |
| K/η/α | 0.1/0.7/0.05；0.2/0.7/0；0.5/1.0/0；每K两种初始化参数相同，不重新搜索 |
| 预算 | seed50，全局batch64，4卡/组；116步/轮，2+8轮，共1160次MSRVTT更新，无指标早停 |
| 评测 | epoch0及每轮完整验证；T↔VA双向等权ITC/ITM、候选R@32及严格几何；own-Top32纯ITM重排 |
| 选模 | 仅MSRVTT验证集选检索主模型与双目标辅助模型，允许epoch0；全部6组固定预算完成并锁定后读取正式测试 |
| 测试 | MSRVTT及VAST/VATEX/ActivityNet/DiDeMo；MSRVTT额外epoch0/2/10诊断 |

完整训练、选模、保存及资源规则见[研究协议](details/PROTOCOL-20261107-msrvtt-head-init.md)。现有三份迁移head和初始投影哈希已核验。旧VAST固定15轮队列在2026-11-07已完成；本轮不恢复或修改旧训练。

## MSRVTT 正式测试，检索主模型 R@1 (%)

| 初始化 | K | 选定轮次 | ITC R@1 | ITM R@1 |
| --- | --- | --- | --- | --- |
| 新 head | 0.1 | 8 | 26.980 | 46.267 |
| 新 head | 0.2 | 7 | 27.093 | 45.928 |
| 新 head | 0.5 | 8 | 26.867 | 46.324 |
| VAST head 第 5 轮 | 0.1 | 9 | 37.443 | **47.851** |
| VAST head 第 5 轮 | 0.2 | 8 | <ins>37.613</ins> | **47.851** |
| VAST head 第 5 轮 | 0.5 | 8 | **38.405** | <ins>47.681</ins> |

K=0.5 的迁移组在 MSRVTT 上取得最高 ITC R@1（38.405%），K=0.1 和 0.2 的迁移组并列最高 ITM R@1（47.851%）。表中的 K 对应各自固定 η/α 配方，无法单独估计 K 的效应。外部评测、双目标辅助模型与固定轮次读出见完整报告。[两轮组合初始化小试](EXP-20261110-server-b-msrvtt-composed-head-init.md)采用另一初始化方案。

## 完整结果与来源

[完整测试与固定轮次诊断](../summaries/recent-20261119/msrvtt-head-init.md)

本地 `workspace/Hyperbolic-Omnimodal/code/experiments/msrvtt_geodesic_2plus8_20261107/REPORT.md`，SHA-256 `9f16fcab11a4311062255353d0e17ad8ef5795c2676ef64a679b476d4e244f3c`。 五集两种选模角色的 **60/60** 份本地评测文件通过完成记录哈希核对，目录为 `dataset_root/msrvtt_geodesic_2plus8_20261107/evaluation/`。本次核对未重新训练或评估。
