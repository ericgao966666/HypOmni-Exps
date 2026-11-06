# 实验总览

这里统一记录研究问题、实验状态、主要结论和结果位置。通常一个研究问题对应一张实验卡；同一问题的种子、消融、失败重试和续跑放在卡内。历史基线与方法探索可按章节汇总，如 EXP-001。GitHub 保留实验结论、关键结果表与 Markdown 报告；原始配置、详细数据、图件、日志和 checkpoint 留在本地。阅读版报告位于 `summaries/`，原始快照仍在本地 `results/`。

首批整理范围：2026-10-13 至 2026-10-20；现已补入 2026 年 8–10 月的零样本基线与方法探索，EXP-001 已同步 server-b 的 2026-10-15 版完整报告。历史归档核对：2026-10-28；近期补录核对：2026-11-05（覆盖10-28至11-05已有产物）；各结果实际发生时间以卡内证据为准。其他更早实验尚未系统补录；交接到其他服务器的任务，只记录当前能核实的交接状态。

本目录是独立 Git 仓库，分支为 `main`，远端为 [ericgao966666/HypOmni-Exps](https://github.com/ericgao966666/HypOmni-Exps)。两台服务器的使用方式见[同步说明](SYNC.md)，维护规则见 [AGENTS.md](AGENTS.md)。本地内容是否已经推送，以 Git 分支状态和远端提交记录为准。

快捷入口：[新服务器5+25操作指南](operations/OPS-20261106-native-baselines-5plus25.md) · [结果报告](summaries/README.md) · [本地证据与图件](LOCAL_ARTIFACTS.md) · [运行记录说明](runs/README.md) · [本机路径配置](config/README.md)

同步范围于 **2026-11-05** 调整为总结文档；这次整理没有重新运行实验，也没有更新各实验原有的结果核对日期。数据与图件不再出现在当前 GitHub 文件树，旧提交历史保留。两台服务器首次更新的本地文件保护步骤见 [SYNC.md](SYNC.md)。

## 当前关注

- **共同VAST初始化的5+25基线待目标端运行**：[实验卡](experiments/EXP-20261106-server-b-vast-init-baselines.md)统一VAST/GRAM/PMRL的预训练起点与阶段预算；[按步骤操作](operations/OPS-20261106-native-baselines-5plus25.md)。尚无本轮正式性能结果。
- **近期实验已补录**：[近期索引](summaries/recent-20261105/README.md)按研究问题汇总角度、K/合法域、ITM、AURORA及官方权重诊断，完整数据继续只存本地。
- **最新端到端比较仍缺GRAM**：[30轮与五数据集](experiments/EXP-20261103-server-a-joint30-five-datasets.md)完成15/20项；MSRVTT角度ITM R@1为41.007%，测地线39.649%、PMRL37.613%，不代表完整四方法排名。
- **K扫描的检索回升可重复，完整合法层级仍失败**：[测地线与下界](experiments/EXP-20261103-server-a-geodesic-domain.md)中K=.3→.5三seed配对R@1 +0.564±0.125pp；动态合法域由参数化保证，不能当作层级学习成功。
- **角度和GP的证据分开**：[角度最小消融](experiments/EXP-20261101-server-a-angular-alignment.md)A0比距离带锥高0.220pp，但比角度无蕴含仅高0.008pp；[GP替代](experiments/EXP-20261102-server-a-gromov-alignment.md)的最佳直接增益区间跨0。
- **图文重建与零训练审计已补齐**：[AURORA/CLIP](experiments/EXP-20261101-server-a-aurora-reconstruction.md)为23.661%/23.037% COCO双向R@1；[官方锥审计](experiments/EXP-20261029-server-a-official-cone-audit.md)区分表观与合法满足；[MERU对数映射](experiments/EXP-20261102-server-a-meru-logmap.md)不与训练消融混用。

- **ITM探索完成并锁定C0**：[原生ITM](experiments/EXP-20261027-server-b-itm-native-baseline.md)：验证三seed 49.8128%±0.4189pp，hard下降5.5583pp；锁定后外部MSRVTT/VATEX可用子集46.2104%/79.1571%。[几何诊断](experiments/EXP-20261026-server-b-itm-geometry-diagnostics.md)与[作者权重补测](experiments/EXP-20261027-server-b-itm-author-baselines.md)分卡记录，避免混淆协议。

- **VAST扩充收益有限**：[PMRL数据量对照](experiments/EXP-20261026-server2-pmrl-data-scale.md)：数据+21.5%，Top-50平均R@1仅+0.36pp，直接检索−0.10pp；单seed且主指标样本区间跨0。
- **低维双曲优势不稳定**：[64D与扩维检索](experiments/EXP-20261021-server-b-retrieval-training.md)：64D双曲R@1 22.13%，比欧氏高0.32pp；32/128/512D欧氏更好，严格包含率仍0%。已完成14/20个选定条件，VAST/PMRL扩维缺失。
- **PMRL–ITM采样收益较小，融合退化**：[四数据集单seed对照](experiments/EXP-20261021-server-a-pmrl-itm-alignment.md)：事前预选sigma_max的共同候选纯ITM增益+0.4087pp，未达0.5pp门槛；开发集选定融合在测试中下降。

- **C0温度与曲率补充已完成**：[EXP-20261027-server-b-c0-temperature-curvature](experiments/EXP-20261027-server-b-c0-temperature-curvature.md)，原65组＋λ=.2新增13组＋λ=.3新增1组＋[λ=.25新增1组](summaries/recent-20261105/lambda025.md)；[λ=.1/.2/.5匹配结果](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-results/LAMBDA_COMPARISON.md)；[两组独立半径图](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/README.md)；[与最初C0的锥角对比](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-cone-angles-original/README.md)；[真实样本庞加莱图](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-poincare-examples/README.md)。
- **单变量蕴含实验已完成**：[EXP-20261026-server-b-entailment-singlefactor](experiments/EXP-20261026-server-b-entailment-singlefactor.md)，56/58完成、2失败；[完整Markdown报告](summaries/EXP-20261026-server-b-entailment-singlefactor/2026-10-26-results/REPORT.md)，全量验证与128条训练诊断分开呈现。
- **512D新对照已完成**：[MERU式scale、曲率与温度](experiments/EXP-20261026-server-b-meru512-scale.md)：17/17组完成30轮、0失败；[完整报告](summaries/EXP-20261026-server-b-meru512-scale/2026-10-26-results/REPORT_WITH_RADII.md)。仅VAST头部预训练及验证，结果固定顺序展示，未微调MSRVTT。
- **本轮双曲几何可视化已完成**：[R0/R1/R2/R3匹配验证集对照](summaries/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/README.md)：R3径向分层明显，严格锥满足率仍为0%。 [R0/R3新版图](summaries/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/README.md)已将baseline半径面板改为独立纵轴。
- **64D五方法最终测试已补齐**：[EXP-20261021-server-b-retrieval-training](experiments/EXP-20261021-server-b-retrieval-training.md)，[完整测试报告](summaries/EXP-20261021-server-b-retrieval-training/2026-10-27-five-method-tests/README.md)包含PMRL、R0增量、验证候选及六方向明细。仅seed50；扩维仍为14/20选定条件有结果，另有2个R0对照。 [同方案对比与半径分布](summaries/EXP-20261021-server-b-retrieval-training/2026-10-27-matched-recipes/README.md)已补充。
- **已观察到的收益**：[MSRVTT 端到端微调](experiments/EXP-006-msrvtt-finetune.md)六方向平均 R@1 达到 24.87%，超过本轮最强基线 VAST 3.88 个百分点，主要来自视频与音频方向。
- **尚未解决的问题**：[子集层级机制](experiments/EXP-003-subset-mechanisms.md)与[几何对照](experiments/EXP-007-coco-geometry.md)仍未证明严格层级包含的成功；[音频迁移](experiments/EXP-005-transfer-diagnostics.md)随头部训练下降。
- **低维实验已完成**：[EXP-009](experiments/EXP-009-lowdim-finetune.md)已核实42组MSRVTT主实验及1组强锥约束消融；六维度双曲有锥仍无严格包含。与旧512D相比，本轮没有额外VAST子集头预训练。
- **区域实验回填完成**：[区域层级实验](experiments/EXP-008-region-geometry.md)已完成20个冻结＋4个seed0联合阶段；8个联合阶段延期，正式test未开始。

## 实验目录

| 编号 / 简称 | 研究问题 | 项目 | 最近实验记录 | 状态 | 当前判断 |
|---|---|---|---|---|---|
| 共同VAST起点5+25基线 | [共同初始化下比较VAST/GRAM/PMRL](experiments/EXP-20261106-server-b-vast-init-baselines.md) | Hyperbolic-Omnimodal | 11-06方案核对 | 已交接，目标端待运行 | 尚无正式结果；[操作指南](operations/OPS-20261106-native-baselines-5plus25.md) |
| 锥训练参数 | [锥训练参数：改善局部满足仍未形成完整层级](experiments/EXP-20261029-server-a-cone-parameters.md) | Hyperbolic-Omnimodal | 10-29；11-05核对 | 已完成 | K=.3合法满足12.869%，检索−0.684pp |
| 原C0几何控制 | [原C0几何控制：双曲无锥略优，锥约束有检索代价](experiments/EXP-20261030-server-a-c0-geometry.md) | Hyperbolic-Omnimodal | 10-30；11-05核对 | 已完成 | 512D无锥双曲R@1 19.019%，欧氏18.783% |
| R3固定曲率 | [R3固定曲率：64D验证候选小幅提高，尚无新测试](experiments/EXP-20261029-server-a-r3-curvature.md) | Hyperbolic-Omnimodal | 10-29；11-05核对 | 已完成 | 固定c=.3/τ=.035：MSRVTT验证28.467% |
| ARGENT/AURORA组件 | [ARGENT/AURORA组件：角度检索提高，样本特异层级未证实](experiments/EXP-20261030-server-a-argent-components.md) | Hyperbolic-Omnimodal | 10-30；11-05核对 | 已完成 | S主读出19.173%，相对B0 +0.423pp |
| 角度对齐 | [角度对齐：减轻蕴含的检索代价，完整合法层级仍失败](experiments/EXP-20261101-server-a-angular-alignment.md) | Hyperbolic-Omnimodal | 11-01；11-05核对 | 已完成 | A0 18.970%，相对距离带锥+0.220pp |
| 测地线K与半径下界 | [测地线K与半径下界：检索回升可重复，合法域仍是瓶颈](experiments/EXP-20261103-server-a-geodesic-domain.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | K=.3→.5三seed回升+0.564±0.125pp |
| Gromov product | [Gromov product：46组探索未找到可信的替代收益](experiments/EXP-20261102-server-a-gromov-alignment.md) | Hyperbolic-Omnimodal | 11-02；11-05核对 | 已完成 | GP_E仅+0.024pp，区间跨0 |
| ITM几何输入 | [ITM几何输入：两套三seed门槛均保留原均匀基线](experiments/EXP-20261103-server-a-itm-geometry.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | I2/D3均未过门槛，锁定I0/D0 |
| 模态组合锥与理想根 | [模态组合锥与理想根：18条件均未通过预设双目标](experiments/EXP-20261103-server-a-cone-root.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | 18/18完成，均未过双目标门槛 |
| 四方法30轮与五数据集 | [四方法30轮与五数据集：已完成15/20项，GRAM仍缺](experiments/EXP-20261103-server-a-joint30-five-datasets.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 部分完成：15/20测试 | 15/20项；MSRVTT角度ITM 41.007%，GRAM缺失 |
| 官方锥审计 | [官方锥审计：高表观满足掩盖定义域问题](experiments/EXP-20261029-server-a-official-cone-audit.md) | meru-width-coco | 10-29；11-05核对 | 已完成 | 表观98–100%，合法覆盖0–1.371% |
| AURORA受控重建 | [AURORA受控重建：检索收益未证明HEC独立贡献](experiments/EXP-20261101-server-a-aurora-reconstruction.md) | meru-width-coco | 11-01；11-05核对 | 已完成 | AURORA23.661%，CLIP23.037%；去HEC23.729% |
| MERU对数映射 | [MERU对数映射：L2几乎保持检索，余弦明显下降](experiments/EXP-20261102-server-a-meru-logmap.md) | meru-width-coco | 11-02；11-05核对 | 已完成 | logmap-L2 mean recall34.427%，原生34.367% |
| ITM原生基线 | [来源/多任务/hard探索](experiments/EXP-20261027-server-b-itm-native-baseline.md) | Hyperbolic-Omnimodal | 10-28 | C0锁定与外部评测完成 | 新变体未超过C0，音频方向弱 |
| ITM几何诊断 | [几何探针与早期结构](experiments/EXP-20261026-server-b-itm-geometry-diagnostics.md) | Hyperbolic-Omnimodal | 10-26～27 | 诊断与4组早期C0完成 | 高AUROC不能替代困难候选重排 |
| ITM作者补测 | [VAST/GRAM/PMRL](experiments/EXP-20261027-server-b-itm-author-baselines.md) | Hyperbolic-Omnimodal | 10-27 | 0步作者权重验证完成 | 共同池PMRL/GRAM 50.02/49.32%，非等训练预算 |
| EXP-20261027-server-b-c0-temperature-curvature | [C0温度与曲率](experiments/EXP-20261027-server-b-c0-temperature-curvature.md) | Hyperbolic-Omnimodal | 10-28 | 80条件完成 | λ=.25补录，匹配配置比较 |
| EXP-20261026-server-b-entailment-singlefactor | [单变量蕴含满足与检索取舍](experiments/EXP-20261026-server-b-entailment-singlefactor.md) | Hyperbolic-Omnimodal | 10-26 | 56/58完成，2失败 | 22全量＋36训练诊断，seed50 |
| EXP-20261026-server-b-meru512-scale | [512D的scale初始化、曲率与温度](experiments/EXP-20261026-server-b-meru512-scale.md) | Hyperbolic-Omnimodal | 10-26 | 17/17组完成30轮，0失败 | 已展示全部结果，未微调 |
| EXP-001 | [历史零样本基线与方法探索](experiments/EXP-001-zero-shot-baselines.md) | PMRL-minimal-hyperbolic / Hyperbolic-Omnimodal | 08–10；报告 10-15；同步 10-20 | 历史评估、MERU 配对及 HyperGRAM pure 探索完成；Parent 仅验证 | 历史视频 Top-50 均值持平，音频 direct 下降；已补 MERU、纯双曲与调参，按协议分组 |
| EXP-002 | [子集配对数量与约束强度](experiments/EXP-002-subset-pilot.md) | Hyperbolic-Omnimodal | 10-16 | 初版停止；后续消融完成 | 9 对弱约束检索较好，未解决严格包含；已附四张几何审计图 |
| EXP-003 | [温度与训练机制能否兼顾检索和层级](experiments/EXP-003-subset-mechanisms.md) | Hyperbolic-Omnimodal | 10-16 | 已完成 | 57 次正式运行，未通过双目标验收 |
| EXP-004 | [官方权重与本地模型的冻结迁移能力](experiments/EXP-004-frozen-transfer.md) | Hyperbolic-Omnimodal | 10-16 至 10-17；10-21 核对 | 已完成 | VAST视听方向强，音频文本跨域退化；两组Ours checkpoint不同 |
| EXP-005 | [音频迁移下降发生在哪个阶段](experiments/EXP-005-transfer-diagnostics.md) | Hyperbolic-Omnimodal | 10-17 | 已完成探索性诊断 | 第一轮已下降，多种目标均受影响 |
| EXP-006 | [统一微调预算下的 MSRVTT 表现](experiments/EXP-006-msrvtt-finetune.md) | Hyperbolic-Omnimodal | 10-17 | 已完成含续跑 | Ours R@1 24.87%，高于VAST 3.88pp；严格包含仍失败 |
| EXP-007 | [负曲率是否带来额外层级能力](experiments/EXP-007-coco-geometry.md) | meru-width-coco | 10-17 | 已完成并修正读出 | 小幅检索收益，无明确层级优势 |
| EXP-008 | [区域监督几何](experiments/EXP-008-region-geometry.md) | meru-width-coco | 10-20结果；10-28核对 | 24/32阶段完成；test未开始 | seed0联合dev R@5双曲高4.37/0.72pp，尚无完整几何结论 |
| PMRL–ITM 对齐 | [PMRL 对齐评分能否改善 ITM](experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) | PMRL-ITM | 10-24 19:05完成；10-24 21:39核对 | 已完成4组单seed训练、开发集与16项测试 | 共同候选采样增益约+0.41～0.45pp；融合测试退化；[最终结果](summaries/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md) |
| 64D检索方案 | [64D优先训练方案](experiments/EXP-20261021-server-b-retrieval-training.md) | Hyperbolic-Omnimodal | 10-25 | 64D全完成；14/20测试，扩维已中断 | 单seed；64D双曲略优，其他三维度欧氏更好；严格包含仍0% |
| PMRL 数据扩充 | [扩充VAST是否改善单轮检索](experiments/EXP-20261026-server2-pmrl-data-scale.md) | PMRL-minimal-hyperbolic / server2 | 10-26 20:01完成；20:18核对 | 已完成2组单seed训练与8项测试 | Top-50 R@1 59.07→59.44%（+0.36pp），direct −0.10pp；主区间跨0，稳定收益未证实 |
| EXP-009 | [低维空间是否放大几何差异](experiments/EXP-009-lowdim-finetune.md) · [五方法展示](summaries/EXP-009/2026-10-20-server-b-five-methods/README.md) | Hyperbolic-Omnimodal | 10-19 至 10-20 | MSRVTT 42组主实验＋1组λ消融全部完成；ActivityNet未训练 | 新初始化流程下，六维度有锥均未严格包含；λ=1改善16D R@1约1pp |

“已完成”指卡内声明的运行与评估完成，不代表假设成立，也不代表证明收敛。运行预算、验证集结果、测试集结果分别记录。

## 数据与基础设施

| 编号 | 工作 | 状态 | 对实验的影响 |
|---|---|---|---|
| OPS-001 | [VAST 150k 缺失媒体恢复](operations/OPS-001-vast-recovery.md) | 仅有10-20历史进度，本机无源目录 | 无法确认当前恢复进程；已冻结实验不能自动换用新 manifest |

## 周度回顾

- [2026 年 10 月 13 至 20 日](weekly/2026-10-13_2026-10-20.md)

## 如何维护

1. **开始新实验**：从[模板](templates/experiment.md)建卡；保留已有 EXP 编号，跨服务器新增时使用 `EXP-YYYYMMDD-server-a-名称` 等含服务器别名的唯一编号，避免双方取到同一个序号。写清问题、基线、唯一变量、数据划分、选择规则和预算，再更新目录。
2. **开始运行**：按 [run 模板](templates/run.md)新增独立记录，补上精确 run ID、服务器、协议与配置、源码版本或快照、输出目录，以及记录命令/PID/GPU/日志的运行清单。不要把凭据或带凭据的命令复制进卡片。
3. **运行变化**：失败、重试、续跑和交接写入 `runs/`，主卡不追加普通进度播报。数据、预算、目标或选模变化影响结果解释时，在主卡概括并链接完整版本证据。
4. **有新结果**：按[实验模板](templates/experiment.md)更新开头结论、关键数字、Markdown 比较表和局限，不以运行完成代替研究判断。负结果保留在总结中；完整指标、图件、来源审计与旧过程保留本地并注明位置。
5. **周度整理**：按请求或本次实验工作需要更新周报，链接实验卡，避免维护多份完整结果表。这里没有后台自动监控或定时更新任务；详细运行记录仅在各自产生它们的服务器保留。

总览中，已有短编号可直接展示；使用长编号的新实验展示简短名称，完整唯一编号保留在实验卡、文件名及运行关联中。

新实验可用状态：计划中、准备中、运行中、已停止、失败待修复、已完成、已交接。运行中状态必须带最后核对时间；历史停止原因不能被新状态覆盖。

数字以本地机器结果为依据，原始快照通过本地来源清单与 SHA-256 对应原始文件；GitHub 阅读版注明原文位置与哈希。卡片负责解释和定位；若修正评测，标明当前权威版本并保留本地旧版本。六方向与十二方向平均、验证与测试、固定末轮与验证最优 checkpoint、样本 bootstrap 与训练种子不确定性不得混用。

历史源服务器路径（包括 `/data-nfs/`）只用于溯源，不代表本机可访问；本机数据目录为 `/data0/xiaobo.xia/yuxuan.gao`。线上优先读取 `summaries/` 中的报告；复核详细证据时读取本地快照，不自动迁移或重写其他服务器路径。

## 2026-10-28补充

λ=.3、c/τ联合学习已完成30轮；C0累计79条件完成。[三组λ匹配报告](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/REPORT.md)，仅seed50验证；本轮纳入统一同步。
