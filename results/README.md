# 可同步结果快照

这里保存从原项目人工筛选的轻量结果，便于另一台服务器或仓库网页直接阅读。首批快照版本为 `2026-10-20`，是采集日期，不是实验运行日期。

| 实验 | 快照目录 |
|---|---|
| PMRL数据扩充：86,706→105,369条，单seed两组完整结果 | [结果报告](EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/summary.md) · [完整指标](EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/results.csv) · [完成核验](EXP-20261026-server2-pmrl-data-scale/2026-10-26-final-seed50/verification.json) |
| 64D完整、扩维部分完成；训练中断 | [最新测试表与证据](EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/README.md) · [此前验证集几何](EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/README.md) |
| 512D MERU式scale、曲率与温度：17组全部完成30轮 | [完整报告](EXP-20261026-server-b-meru512-scale/2026-10-26-results/REPORT_WITH_RADII.md) · [末轮CSV](EXP-20261026-server-b-meru512-scale/2026-10-26-results/final_epoch.csv) · [最佳CSV](EXP-20261026-server-b-meru512-scale/2026-10-26-results/best_validation.csv) · [图件PDF](EXP-20261026-server-b-meru512-scale/2026-10-26-results/diagnostics.pdf) · [实现证据](EXP-20261026-server-b-meru512-scale/2026-10-26-implementation/) |
| 64D同方案比较及R1/R3半径分布 | [补充报告](EXP-20261021-server-b-retrieval-training/2026-10-27-matched-recipes/README.md) · [半径图](EXP-20261021-server-b-retrieval-training/2026-10-27-matched-recipes/radius_R1_R3.png) · [验证表CSV](EXP-20261021-server-b-retrieval-training/2026-10-27-matched-recipes/validation_recipes.csv) |
| 64D五方法最终测试：含PMRL、R0增量与验证选模 | [完整报告](EXP-20261021-server-b-retrieval-training/2026-10-27-five-method-tests/README.md) · [主表CSV](EXP-20261021-server-b-retrieval-training/2026-10-27-five-method-tests/retrieval_64d.csv) · [实现与协议](EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/) · [并行接管与进度](EXP-20261021-server-b-retrieval-training/2026-10-21-parallel-screen/) |
| 历史零样本基线与方法探索 | [当前完整报告](EXP-001/2026-10-20-server-b/zero_shot/ZERO_SHOT_COMPLETE_RESULTS.md) · [旧版报告](EXP-001/2026-10-20/zero_shot/ZERO_SHOT_COMPLETE_RESULTS.md) · [协议与零样本结果](EXP-001/2026-10-20/zero_shot/) · [Parent 消融结果](EXP-001/2026-10-20/) |
| 子集初版后续消融与四张几何审计主图 | [EXP-002](EXP-002/2026-10-20/) · [图与数值](EXP-002/2026-10-20/figures/) |
| 子集机制、种子复核与头部训练曲线 | [EXP-003](EXP-003/2026-10-20/) · [训练曲线](EXP-003/2026-10-20/paired_training_curves.png) |
| 冻结模型迁移与训练来源 | [EXP-004 评测结果](EXP-004/2026-10-20/) · [10-21 训练及 checkpoint 审计](EXP-004/2026-10-21/training/) |
| 迁移退化诊断与逐轮曲线 | [EXP-005](EXP-005/2026-10-20/) · [迁移曲线](EXP-005/2026-10-20/transfer_curves.png) |
| MSRVTT 微调、训练曲线与关键分析图 | [EXP-006](EXP-006/2026-10-20/) · [训练对比图](EXP-006/2026-10-20/training_comparison.png) · [微调前来源记录](EXP-006/2026-10-20/provenance/) |
| 欧氏双曲几何对照 v2 | [EXP-007](EXP-007/2026-10-20/) |
| PMRL–ITM 对齐：单seed训练与完整四测试集 | [最终汇总](EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md) · [原始JSON](EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/results.json) · [完成与来源核验](EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/verification.json) |
| MSRVTT 六维度主结果、强锥约束消融与可视化 | [EXP-009](EXP-009/2026-10-20-server-b/) · [五方法展示版](EXP-009/2026-10-20-server-b-five-methods/README.md) · [42组CSV](EXP-009/2026-10-20-server-b/retrieval_42.csv) · [完整方向表](EXP-009/2026-10-20-server-b/directional_results.md) · [几何PDF](EXP-009/2026-10-20-server-b/geometry/all_widths_geometry_report.pdf) |

[manifest.json](manifest.json) 保存来源服务器别名、原始相对路径、采集时间、文件大小及 SHA-256。`source_root` 未填写或为 `workspace` 时，原始路径相对源工作区；为 `dataset_root` 时，相对源机器的数据根目录，具体路径见本机配置。原始产物按字节复制，保留原有 CSV 换行；显示预览或元数据摘录以 `derivation` 记录生成方法及源文件哈希，多源审计在其中列出全部输入来源。所有条目的 `sha256` 均校验所保存文件本身。历史 JSON 中的绝对路径是来源记录，不能假设另一台机器可直接访问。

修正结果时新增快照版本，并修改实验卡的当前链接，保留旧版。原始文件中提到但未纳入本仓库的辅助文件仍在源服务器；实验卡会注明本仓库可直接查看的主要证据。

EXP-001 的 `2026-10-20-server-b` 为本次同步的独立版本，来源文档更新于 2026-10-15，补充 MERU 与 HyperGRAM pure 等结果；旧 `2026-10-20` 快照及 JSON 保留。新报告逐字节复制，辅助文档链接与服务器绝对路径属于原始来源记录，未额外采集其目标文件；可跨服务器阅读的结果与协议区分见[实验卡](../experiments/EXP-001-zero-shot-baselines.md)。

EXP-009 的 `2026-10-20-server-b` 来自交接接收端 server-b：42组主结果及1组λ消融，只有训练seed50。原始CSV/JSON及已有图按字节复制；后生成的汇总、曲线与来源清单在manifest中标明derivation。没有复制模型、特征数组、数据集或完整日志。

EXP-009 的 `2026-10-20-server-b-five-methods` 为同一实验的五方法展示视图：主结果30组，另含λ=1.0消融1组；原七方法完整记录不变。只对保留方法重新排名和绘图；仅含双曲有锥的几何及权重图原样复用。

- [2026-10-22 独立R0种子对照提前调度](EXP-20261021-server-b-retrieval-training/2026-10-22-early-controls/controller_manifest.json)：5项CPU检查、保留PMRL原进程的[接管记录](EXP-20261021-server-b-retrieval-training/2026-10-22-early-controls/handover.json)。

- [2026-10-23 数据盘40GiB策略](./EXP-20261021-server-b-retrieval-training/2026-10-23-disk40/runtime_policy.json)：调度与写入保护统一覆盖，8项检查通过；[停滞恢复记录](./EXP-20261021-server-b-retrieval-training/2026-10-23-disk40/recovery.json)。

- [2026-10-23 双曲R1独立选模与提前复核](./EXP-20261021-server-b-retrieval-training/2026-10-23-early-selected/selection.json)：候选齐全后按原规则锁定，提前seed51；[调度器检查](./EXP-20261021-server-b-retrieval-training/2026-10-23-early-selected/controller_manifest.json)。

- [2026-10-23 指定seed52同卡叠加](./EXP-20261021-server-b-retrieval-training/2026-10-23-overlay-seed52/runtime_policy.json)：只对一个既定实验授权，与VAST同卡；[无中断接管](./EXP-20261021-server-b-retrieval-training/2026-10-23-overlay-seed52/handover.json)。

- [2026-10-23 GPU5欧氏R1复核](./EXP-20261021-server-b-retrieval-training/2026-10-23-gpu5-euc/selection.json)：原规则独立选模，固定GPU5，6项调度检查通过。

- [2026-10-23 仅seed50执行范围](./EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/execution_scope.json)：GPU2/3/4各一项单卡扩维；[多seed停止但保留结果](./EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/cancelled_multiseed.json)。

- [2026-10-23 64D优先、GPU3–6四卡续训](./EXP-20261021-server-b-retrieval-training/2026-10-23-priority64-gpu3to6/runtime_schedule.json)：三个扩维暂停保留断点，[GRAM真实续训](./EXP-20261021-server-b-retrieval-training/2026-10-23-priority64-gpu3to6/progress.json)。

- [2026-10-23 PMRL新增GPU1/2/6/7四卡组](./EXP-20261021-server-b-retrieval-training/2026-10-23-pmrl-gpu1267/runtime_schedule.json)：保留VAST与GRAM，seed50-only、64D优先。

- [2026-10-23 本轮双曲R0/R1/R2/R3几何可视化](./EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/README.md)：匹配验证集HoroPCA/CO-SNE、原空间半径和投影保真度；[完整PDF](./EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/geometry_validation_report.pdf)。

- [2026-10-23 VAST在GPU7单卡微调](./EXP-20261021-server-b-retrieval-training/2026-10-23-vast-joint-gpu7/runtime_schedule.json)：64D R3，seed50，10轮batch64；保留GRAM和PMRL四卡任务。

- [2026-10-24 PMRL恢复与启动显存重试](./EXP-20261021-server-b-retrieval-training/2026-10-24-pmrl-recovery/recovery_policy.json)：PMRL四卡继续第9轮，GRAM单卡并行；[实际更新](./EXP-20261021-server-b-retrieval-training/2026-10-24-pmrl-recovery/progress.json)。

- [2026-10-24 逐方法锁定后的64D测试](./EXP-20261021-server-b-retrieval-training/2026-10-24-method-tests/README.md)：4项GPU推理及2项CPU复核完成，约1分钟/模型；PMRL继续训练。

- [单变量蕴含与检索取舍：58组完整报告](./EXP-20261026-server-b-entailment-singlefactor/2026-10-26-results/REPORT.md)：22全量验证＋36训练诊断，包含70个单因素差值、梯度和半径分布。

- [C0温度与曲率：65组完整结果](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-results/REPORT.md)：65完成、0失败，117项单因素比较，r/u/q和梯度分布齐全；[实现快照](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-implementation/protocol.json)保留。

- [C0 λ=.2补充结果及λ=.1/.5匹配比较](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-results/LAMBDA_COMPARISON.md)：13/13完成、0失败；原65组及[补充实现快照](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-implementation/protocol.json)保留。

- [λ=.2固定τ=.035与联合学习的独立半径图](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/README.md)：第30轮、每头2048条验证样本；附梯度负值解释、数值及来源哈希。

- [最初C0与当前配置的锥角可视化](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-cone-angles-original/README.md)：六个末轮配置、每组18432条边；含角度总览、局部示意、真实分布与单因素对照。

- [真实样本的庞加莱圆盘比较](./EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-poincare-examples/README.md)：三个真实验证样本×三种模型×两条父子边；展示实际位置、测地线和蕴含锥，附几何保真核验。

- [λ=.2/.3/.5联合学习匹配结果](EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/REPORT.md)：新增λ=.3单组，30轮完成。

## 2026-10-28补录

- [EXP-008](../experiments/EXP-008-region-geometry.md)：结果、边界与精简来源已归档。
- [EXP-20261026-server-b-itm-geometry-diagnostics](../experiments/EXP-20261026-server-b-itm-geometry-diagnostics.md)：结果、边界与精简来源已归档。
- [EXP-20261027-server-b-itm-native-baseline](../experiments/EXP-20261027-server-b-itm-native-baseline.md)：结果、边界与精简来源已归档。
- [EXP-20261027-server-b-itm-author-baselines](../experiments/EXP-20261027-server-b-itm-author-baselines.md)：结果、边界与精简来源已归档。
