# Rebuttal实验目录与记录核对

**当前目录覆盖10个研究问题。** 新增[MSR-VTT联合对齐](../../experiments/EXP-20261112-server-a-hopa-joint-alignment.md)直接回应**Area Chair 48NW W2**及**Reviewer o82E W2 / Q4前半段**。原九项结果保留原核对快照；本次补充reviewer映射不代表重新核验实验状态。

[返回实验总览](../../README.md) · 文档整理与本地产物核对：2026-11-12，Asia/Shanghai

Table 3已于11-13另行整理为[一份完整实验报告](../EXP-20261107-server-a-hopa-cross-architecture/TABLE3_COMPLETE_REPORT.md)，覆盖本页跨架构分支、历史OmniBind协议/容量诊断，以及最新原生WBCE温度修正；其他研究问题仍按下方各自快照日期解读。

首次核对时已有**9张相关研究主卡**，随后新增联合对齐卡，共10个研究问题。多数实验已经记录。缺口是`q5_equal`只有代码/来源材料、缺少文字记录，以及N500联合调参、随机head完整实验、正初始化蒸馏的最终结果没有完整回填。现已补齐上述记录，并将原先分散在主卡、子目录和结果报告中的分支列在下方。

范围为本机`HoPA-Rebuttal/`及其明确关联的授权数据目录、现有实验卡和本地远端镜像。没有重新训练或评测，没有连接远端核实其后续执行，也没有将其他协议结果补作缺失实验。尚无本地产物、仅存在于未提供讨论中的计划不属于已核实覆盖范围。结果发生时间与本次文档日期分开列；本页是核对快照，后续状态以对应主卡及原始记录为准。

## 编号口径与审稿来源

依据本地保存的2026-11-12 13:50 OpenReview更新快照，按意见内容逐项对应；**W=Critical Weakness，Q=Question for Authors**。wyrt原文直接使用W1–W3/Q1–Q3；o82E的两段weakness按“First/Second”记作W1/W2、问题按原编号1–6记作Q1–Q6；AC 48NW按其编号列表记W1/W2/Q1。AC是Area Chair，不另造reviewer ID。

| 审稿人/编号 | 该意见的主要要求 | 更新快照页码 |
|---|---|---|
| wyrt W1 / Q1 | rank-1丢失的互补/模态特有信息，rank-2取舍 | 第3页 |
| wyrt W2 / Q2 | 非负性、谱残差、leading eigengap在训练中是否成立，以及近简并稳定性 | 第3页 |
| wyrt W3 / Q3 | 冻结设置之外的可靠迁移；Table3输入/空间适配及多次运行方差 | 第3页 |
| o82E W1 / Q1 | 饱和和Random接近Full；训练更多网络或扩大性能差距；跨架构及更换源backbone | 第4–5页 |
| o82E W2 / Q2 | 同一批实例改变k=2/3/4，报告性能、时间、显存、合成参数，并解释IMU方向 | 第4–5页 |
| o82E Q3 | 真实/合成表示负Gram比例、ρ和γ分布 | 第5页 |
| o82E W2 / Q4 | 前半段要求多模态联合使用任务；后半段追问Table9调参及是否包含L_M | 第4–6页 |
| o82E Q5 | 总存储/合成参数/计算预算匹配，以及时间和峰值显存 | 第6页 |
| AC 48NW W2 | 测试集联合对齐度量或多模态query，补足只有pairwise指标的缺陷 | 第2页 |

“**衍生诊断/衍生验证**”表示围绕该意见开展的后续方法探索，不表示审稿人原文要求了正初始化、持续约束或SVD/mock等具体设计。“补证/关联”也不等于完整回答：关系保真度与加权proxy没有独立解决wyrt W1/Q1的模态特有信息或rank-2问题；更换LanguageBind/OmniBind作为**源**backbone尚未由当前目标迁移实验覆盖。o82E W2/Q6、AC W1中的创新性定位，以及AC Q1的去L_M跨数据集相反趋势，也不能仅凭这些实验标为已回应完毕。

本地来源：`HoPA-Rebuttal/Omnimodal Dataset Distillation via High-Order Proxy Alignment_OpenReview-update.pdf`（6页；打印时间2026-11-12 13:50；包含AC 11-11意见及wyrt/o82E审稿）。SHA-256：`86a51a378eda51a7e8499b15b2226f50769a31131ecd9588c963a203016414df`。仅引用已保存快照，未核实线上后续更新；PDF不随本目录发布。

## 十个研究问题与审稿意见对应

| 研究问题及独立记录 | 针对的 reviewer / Weakness / Question | 已核实的结果范围 | 当前判断/缺口 |
|---|---|---|---|
| [谱条件、关系保真度与稳定性](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md) | **wyrt W2 / Q2；o82E Q3**：非负性、谱残差、eigengap及稳定性；**wyrt W1 / Q1**的关系损失补证 | 11-09选中状态与三项补测；含历史v3 | 条件并非处处满足；加权proxy相关0.905889未达0.93示例门槛；单seed |
| [Table3跨架构迁移](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md) | **wyrt W3 / Q3；o82E W1 / Q1**：跨架构输入接口、运行方差及冻结网络范围 | 15项Random学生重复、18项三源seed配对、适配和全量微调补充 | 配对结果已有；历史投稿Distilled原产物仍缺；test参与选择 |
| [Q5预算、效率与显存](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md) | **o82E Q5**：总合成参数/存储、等预算/等计算、总耗时与峰值显存 | 原生N100小试、硬件计时、SVD替换、六方法显存 | 旧v1–v4结论撤回；不同时间窗口/硬件/性能口径不可混用；等预算独立分支待核实 |
| [Table9 N500联合3-pair调参](../../experiments/EXP-20261108-server-a-hopa-joint-tuning.md) | **o82E W2 / Q4后半段**：Table9的pairwise变体是否充分调参、是否包含L_M | 11-09 13:29完成7/7配置；11-12回填 | 最优20.2489% R@1，低于配对Random20.7014%；单seed、test-selected |
| [N25/50/100低tuple预算](../../experiments/EXP-20261108-server-a-hopa-low-budget.md) | **o82E W1 / Q1**：减小预算能否扩大Random与Full差距，减轻饱和 | 11-09本地server2镜像9/9条件 | 三seed；低预算增益未稳定扩大，固定末态负结果保留 |
| [随机head可学习性与完整蒸馏](../../experiments/EXP-20261110-server-a-hopa-random-head.md) | **o82E W1 / Q1**：构造较不饱和设置并检验真实蒸馏收益；仍非更换源backbone | CPU小试、GPU校准、11-11完整五seed终测 | HoPA/联合LoRS测试R@1为12.472/14.174%；已补正式结果正文 |
| [PMRL正余弦初始化](../../experiments/EXP-20261111-server-a-pmrl-positive-init.md) | **衍生诊断：wyrt W2 / Q2、o82E Q3**的非负前提；同时服务**o82E W1 / Q1**的随机head可学习性 | 11-11八条件单seed验证小试 | 仅正初始化Full20.292%，普通随机2.208%；本分支无蒸馏/test |
| [正初始化且严格配对的蒸馏](../../experiments/EXP-20261111-server-a-hopa-positive-distill.md) | **衍生验证：o82E W1 / Q1**的低饱和蒸馏；关联**wyrt W2 / Q2、o82E Q3**的正初始化前提 | 11-11固定LR与learned-LR结果；11-12完整回填 | 固定LR HoPA/LoRS验证4.076/3.688%；一个蒸馏seed、三个学生head，无test |
| [模态数量与共享/独立LoRS](../../experiments/EXP-20261111-server-a-hopa-modality-scaling.md) | **o82E W2 / Q2**：同实例k=2/3/4扩展性与IMU方向；**Q5**的成本核算补充 | 四组合三seedtest与独占成本；11-12 validation复核 | 共享tuple三模态补充尚在执行；不能把两类LoRS或validation/test混为一组 |
| [MSR-VTT联合对齐与多模态查询](../../experiments/EXP-20261112-server-a-hopa-joint-alignment.md) | **AC 48NW W2；o82E W2 / Q4前半段**：测试集联合几何与多模态查询 | 11-12学生选优版、11-13固定20轮版均完成 | 固定20轮HoPA/共享3-pair双查询R@1为30.053/25.867%，ρ为0.484814/0.464067；外层历史test选择保留 |

各行研究问题、数据和协议不同，不进行跨行指标排名。已有EXP编号保留；同一问题的种子、重试和续跑留在原卡。

## 分支与补充实验逐项检索

### 谱条件与关系测量

| 分支 | 针对的 reviewer / Weakness / Question | 记录入口 | 原始证据位置（本地，HoPA-Rebuttal下） |
|---|---|---|---|
| v3固定末轮谱统计/梯度稳定性 | wyrt **W2 / Q2**；o82E **Q3** | [主卡历史与边界](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md#历史结果与边界) | `results/spectral_theory/RESULTS_v3_fixed_final.md`；与新选模协议分开 |
| 原生检索选中状态的谱条件 | wyrt **W2 / Q2**；o82E **Q3** | [当前协议和结果](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md) | `theory_selected/migration_server2/status/20261109T003257-server2-spectral-selected-native/formal/RESULTS.md` |
| 全量跨实例关系保真度 | wyrt **W1 / Q1**关系损失补证；wyrt **W2 / Q2**、o82E **Q3**的条件/误差解释 | [直接测量](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md#跨实例关系保真度新增直接测量) | `results/spectral_theory/fidelity_selected_20261109/analysis_v1/RESULTS.md` |
| 同100条配对与负Gram/u₁分解 | wyrt **W2 / Q2**；o82E **Q3** | [配对诊断](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md#负gram分解与同100条配对) | `results/spectral_theory/paired_initial_selected_20261109/analysis_v1/RESULTS.md` |
| 投影系数加权proxy | **衍生诊断**：wyrt **W1 / Q1、W2 / Q2**；o82E **Q3**，不替代原方法或rank-2消融 | [加权补测](../../experiments/EXP-20261107-server-a-hopa-spectral-theory.md#投影系数加权补测) | `results/spectral_theory/weighted_proxy_selected_20261109/RESULTS.md` |

两个谱问题的已有回复页保留于本地`HoPA-Rebuttal/reviewers/README.md`：wyrt W2/Q2及o82E Q3使用共同谱证据，不能计作两个独立实验；其他实验的对应关系见本页各表。

### 跨架构与目标训练范围

| 分支 | 针对的 reviewer / Weakness / Question | 记录入口 | 原始证据位置（本地，HoPA-Rebuttal/cross_arch下） |
|---|---|---|---|
| 投稿Table3协议审计和15项Random重复 | wyrt **W3 / Q3**；o82E **W1 / Q1** | [主卡设置/主要结果](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md#主要结果) | `docs/PROTOCOL_AUDIT.md`、`docs/STUDENT_SEED_RESULTS.md` |
| 三独立源seed、18项配对迁移 | wyrt **W3 / Q3**（独立蒸馏方差）；o82E **Q1**（迁移协议） | [当前重建结果](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md) | `docs/PAIRED_SOURCE_RESULTS.md`、`artifacts/paired_source_seed_summary.json` |
| 源节点0/50/100/150/200原生选择诊断 | 为wyrt **W3 / Q3**、o82E **Q1**提供源数据选择审计，非额外独立迁移证据 | [保存节点诊断](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md#保存节点的原生诊断) | `runs/native-checkpoint-eval-v1/RESULTS.md`；属于源选择证据，不另计目标迁移重复 |
| LanguageBind直接插值适配 | wyrt **W3 / Q3**；o82E **Q1**（异构输入/特征空间如何适配） | [单seed输入适配](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md#输入插值适配小试languagebind) | `adapter_trials/20261109T2202-languagebind-direct-seed1/REPORT.md` |
| LanguageBind全量微调及固定3e-6三seed复核 | wyrt **W3**；o82E **W1 / Q1**（训练更多网络、检验冻结设置限制） | [单seed小试](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md#languagebind全量微调20轮小试) · [三seed复核](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md#固定3e-6的三源seed全量微调复核) | `full_finetune/20261110T1525-languagebind-seed1/REPORT.md`；`full_finetune/20261110T2053-languagebind-three-seed-lr3e6/REPORT.md` |

### 预算、硬件成本与显存

| 分支 | 针对的 reviewer / Weakness / Question | 记录入口 | 原始证据位置（本地，HoPA-Rebuttal下） |
|---|---|---|---|
| 原生N100：同名义N、等参数、等时间 | o82E **Q5** | [原生小试](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md#n100单seed阶段读出) | `q5_native/runs/20261108-native-v5d-pilot/analysis/REPORT.md`；旧`q5_budget` v1–v4结论已撤回 |
| Q100 HoPA/各pair Q50 LoRS独立队列准备 | o82E **Q5**（总预算匹配，执行待核实） | [本次新补独立记录](../../experiments/details/EXP-20261107-server-a-hopa-budget-efficiency-equal-budget.md) | `q5_equal/README.md`、`performance_queue.py`、`scientific_manifest.json`；没有本地运行结果，远端未核实 |
| server2完整成本/A100短程硬件测量 | o82E **Q5**（时间口径与硬件条件） | [硬件读数](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md#当前硬件计时结果) | `q5_hardware/RESULTS.md`、`q5_hardware/control/*_status.json`；11-09镜像快照不代表远端当前进度 |
| A100 GPU5空闲复测 | o82E **Q5**（独占条件下效率复核） | [独占短测](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md#a100-gpu5空闲复测) | `q5_hardware/repeats/20261109T160403-a100-gpu5-exclusive-repeat/REPORT.md` |
| SVD/mock替换开销诊断 | **衍生诊断**：o82E **Q5**（SVD对效率差异的贡献） | [三seed短测](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md#svd替换计时诊断2026-11-12) | `q5_svd_diagnostic/runs/20261112-server-a-svd-mock-v2/REPORT.md` |
| 六方法完整进程峰值显存 | o82E **Q5**（peak memory） | [100步及稳定性读数](../../experiments/EXP-20261107-server-a-hopa-budget-efficiency.md#msr-vtt-q100六方法完整进程峰值显存) | `q5_peak_memory/runs/20261112T152715-server-a-gpu7-memory100-seed0/REPORT.md`；MTT-VL/TESLA为仓库适配版 |

A100迁移、显存容量预检、原生数值对齐及单卡叠进程微测是运行/诊断材料；已在各父卡及本地运行记录中关联，不把迁移或预检通过当作科研结果。

### 低预算、初始化与模态规模

| 分支 | 针对的 reviewer / Weakness / Question | 独立主卡/小节 | 本地原始结果入口 |
|---|---|---|---|
| N500联合3-pair七配置 | o82E **W2 / Q4后半段**（调参与L_M组成） | [完整调参结果](../../experiments/EXP-20261108-server-a-hopa-joint-tuning.md) | `HoPA-Rebuttal/q4_tuning/runs/20261109T000033-server-a-n500-test-selected/{REPORT.md,results.json,finished.json}` |
| N25/50/100三seed配对 | o82E **W1 / Q1**（低饱和设置） | [低预算实验](../../experiments/EXP-20261108-server-a-hopa-low-budget.md) | `HoPA-Rebuttal/low_budget/migration_server2/status/20261108T230026-server2-msrvtt-low-budget/REPORT.md` |
| 随机head CPU小试及符号诊断 | o82E **W1 / Q1**；符号解释关联wyrt **W2 / Q2**、o82E **Q3** | [历史小试](../../experiments/EXP-20261110-server-a-hopa-random-head.md#第一轮cpu小试历史结果保留) | `HoPA-Rebuttal/random_head_pilot/results/20261110-v1-cpu/REPORT.md`及`polarity_diagnostic/REPORT.md` |
| 随机head完整五seed蒸馏/test | o82E **W1 / Q1**（Full−Random差距和多seed收益） | [完整终测](../../experiments/EXP-20261110-server-a-hopa-random-head.md#完整实验锁定后884条测试结果) | 数据盘`random_head_full/20261110T215841-server-a-random-head-4gpu-v3/gpu_pipeline/{REPORT.md,summary.json}` |
| 仅正初始化/持续正约束八条件 | **衍生诊断**：wyrt **W2 / Q2**、o82E **Q3**；服务o82E **W1 / Q1** | [PMRL正初始化](../../experiments/EXP-20261111-server-a-pmrl-positive-init.md) | `HoPA-Rebuttal/positive_init_pilot/results/20261111T115501-server-a-positive-init-v1/REPORT.md` |
| 正初始化、严格配对、固定/learned LR蒸馏 | **衍生验证**：o82E **W1 / Q1**；关联wyrt **W2 / Q2**、o82E **Q3** | [完整验证读数](../../experiments/EXP-20261111-server-a-hopa-positive-distill.md) | 数据盘`positive_init_distill/20261111T145619-server-a-positive-distill-v1/{REPORT.md,summary.json}` |
| VT/VTA/VTI/VTAI与独立pair LoRS | o82E **W2 / Q2**（固定实例的模态数量与IMU方向）；**Q5**成本补充 | [四组合test与成本](../../experiments/EXP-20261111-server-a-hopa-modality-scaling.md) | 数据盘`q2_scaling/20261111-four-subsets-v1/analysis/REPORT.md` |
| 203实例validation读出复核 | o82E **Q2**（Table8/IMU结果解释与评估口径复核） | [冻结学生复核](../../experiments/EXP-20261111-server-a-hopa-modality-scaling.md#203实例-validation-复核2026-11-12) | 同run的`analysis/validation_20261112T151811_v1/REPORT.md`；不重新选模 |
| 共享tuple LoRS补充 | o82E **W2 / Q2**（与Table8同结构对照）；**Q5**（共享/独立预算核算） | [共享对照协议](../../experiments/EXP-20261111-server-a-hopa-modality-scaling.md#共享tuple-lors补充对照2026-11-12) | 数据盘`q2_scaling/20261112-shared-tuples-gpu7-v2/`；本次读取17:03:53的progress为`running / cost_exclusive`，未见完整最终报告 |
| MSR-VTT测试集联合几何/多模态query | **AC 48NW W2；o82E W2 / Q4前半段** | [联合对齐实验](../../experiments/EXP-20261112-server-a-hopa-joint-alignment.md) | `HoPA-Rebuttal/joint_alignment_eval/`；原run下`fixed_epoch20_v1/`为最新固定20轮读出，`analysis/`保留学生选优版 |

“数据盘”前缀为本机授权的`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/`，不是可随Git同步的附件。低预算、谱选中状态和部分硬件结果来自本地已有server2镜像；本次没有远端实时核验。

## 核对与维护

三张回填卡依据原始`summary.json`/`results.json`与`finished.json`核对，源码/数据/日志路径在各卡中；结果JSON的SHA-256同时写在对应卡末。`q5_equal`的99项已有冻结文件哈希一致，记录本身不宣称运行完成。编辑前文档与本次来源哈希保存在本地`runs/rebuttal-record-audit-20261112T1705/`，历史结果、失败和撤回材料均保留。

后续新问题仍按实验模板建卡；同一问题的新seed、失败重试、选模修正和续跑更新原卡及本目录，避免产生两份相互冲突的权威结果。`git fetch origin`连接失败，远端状态尚未核实；本次没有commit、push或上传。
