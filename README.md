# 实验总览

<!-- THREE-PAIR-PAIRED-EXPERT-A100-START -->
- [HoPA统一选优与单学生对照](experiments/EXP-20261117-server-a-hopa-three-pair-lm.md)：四方法统一修正专家配对，沿用联合查询表的选优规则及单学生：三seed平均R@1为3-pair 17.075±0.443%；L_M + 3-pair 17.019±0.264%；5L_M + 3-pair 17.094±0.175%；HoPA 21.512±0.019%。
<!-- THREE-PAIR-PAIRED-EXPERT-A100-END -->

<!-- THREE-PAIR-SELECTED-COMPARISON-START -->
- [HoPA统一选优与单学生对照](experiments/EXP-20261117-server-a-hopa-three-pair-lm.md)：**失败待恢复GPU，六组均未进行训练更新**，核对2026-11-18 05:14:53 +0800。GPU0–7均显示GPU requires reset，PyTorch CUDA初始化失败；需要管理员恢复GPU/CUDA。六个worker、控制器及缓存进程均已退出，约57.1GiB RAM已释放。配置、专家池、旧结果和失败证据保留，尚无完整选优横评结果。
<!-- THREE-PAIR-SELECTED-COMPARISON-END -->

<!-- THREE-PAIR-LM5-THREE-SEED-START -->
- [HoPA λ5共享target三seed](experiments/EXP-20261117-server-a-hopa-three-pair-lm.md)：固定λM=5、共享1组target，三蒸馏seed的Avg.R@1/5/10为17.182 ± 0.151/39.585 ± 0.637/51.251 ± 0.364%；相对各seed匹配Random的R@1差为-2.420 ± 0.264pp。每seed先平均五学生，±为跨三个蒸馏seed的样本SD。
<!-- THREE-PAIR-LM5-THREE-SEED-END -->

<!-- THREE-PAIR-SHARED-WEIGHT-START -->
- [HoPA共享target与固定权重](experiments/EXP-20261117-server-a-hopa-three-pair-lm.md)：共享同一target、蒸馏seed0固定2000步/学生20轮：λM=5的Avg.R@1为17.195%，λM=10为16.629%，差值-0.566pp。各数值平均5个学生；只有一个蒸馏seed，不报告跨蒸馏seed SD。
<!-- THREE-PAIR-SHARED-WEIGHT-END -->

<!-- SELECTED-STUDENT-SPECTRAL-20261117-OVERVIEW-START -->
- **最佳合成集训练后的谱残差**：[三seed、固定epoch20复核](experiments/EXP-20261112-server-a-hopa-joint-alignment.md#最佳合成集训练后的谱残差三seed复核)：11-17 20:46完成。共同884条test的平均ρ：Random **0.456403±0.003095**、3-pair <ins>0.463577±0.006380</ins>、HoPA 0.484212±0.003233；三个seed顺序一致。各自100条训练数据的ρ为0.446965/0.071439/0.424437（同顺序），训练内谱集中不能替代真实test表现。历史test外层选模限制保留。
<!-- SELECTED-STUDENT-SPECTRAL-20261117-OVERVIEW-END -->

<!-- THREE-PAIR-LM-N100-START -->
- [HoPA N100 3-pair＋L_M](experiments/EXP-20261117-server-a-hopa-three-pair-lm.md)：固定外层2000/学生20轮：3-pair＋L_M Avg.R@1 17.113 ± 0.532%，3-pair 17.037 ± 0.681%；配对差值 +0.075±0.217pp。±为三个蒸馏seed的样本SD，先在每seed内平均五个学生。
<!-- THREE-PAIR-LM-N100-END -->

<!-- JOINT-THREE-SEED-OVERVIEW-START -->
- [HoPA联合查询三seed扩充](experiments/EXP-20261112-server-a-hopa-joint-alignment.md)：**complete**，核对：2026-11-17 19:01:26 +0800。三个source seed固定20轮、平均双查询R@1（%）：hopa 29.613±0.549；shared3pair 25.855±0.022；random 26.332±0.480。±为跨蒸馏/采样seed的样本SD，外层历史test选择限制保留。
<!-- JOINT-THREE-SEED-OVERVIEW-END -->

- **归一化fusion核验**：[联合查询实验](experiments/EXP-20261112-server-a-hopa-joint-alignment.md)，11-17 19:45完成。显式归一化查询和与原等权分数融合的R@1/5/10全部相同；HoPA T+A→V为44.382±0.285%，较Frozen +3.092±0.285pp。支持组合查询效用，不新增不可分解高阶交互证据。

<!-- MEAN-PROXY-20261117-OVERVIEW-START -->
- **HoPA均值proxy对照完成**：[谱理论实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：267个同表示离线状态已测。outer600/inner15平均E为谱0.1119、单位均值0.1081；后者在151/204个合成状态更低。不能据此声称谱proxy直接近似普遍更准；未做替换proxy后的重训。
<!-- MEAN-PROXY-20261117-OVERVIEW-END -->

<!-- POSITIVE-FIDELITY-20261117-OVERVIEW-START -->
- **正随机初始化近似质量补测完成**：[谱理论实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：5专家平均E从0.2632到0.0757，validation R@1从0.125%到20.229%；单source seed20的outer0/500/1000/1950实际rollout已补采，原checkpoint复现通过。机制联系不作因果或跨source seed结论。 新增outer1500恢复读出：inner15平均E0.0721、P950.1616，非负实例68%，原采样和已测节点一致性核验通过。
- **正初始化专家约5epoch网格补齐**：5专家、40次新增读出，验证检索精确复现；实际4.23至40.14epoch平均E从0.0898±0.0006降至0.0763±0.0002，完整表含初始与42.25epoch末态。[实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)。
<!-- POSITIVE-OUTER-GRID-20261118-OVERVIEW-START -->
- **正初始化outer600/1200/1800补测完成**：[谱理论实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：inner15 Mean/P95为0.0782/0.1740、0.0654/0.1467、0.0687/0.1569；inner0另报。原artifact/optimizer/RNG及旧读出完全复现，已存每100步快照。单source seed20。
<!-- POSITIVE-OUTER-GRID-20261118-OVERVIEW-END -->
<!-- POSITIVE-FIDELITY-20261117-OVERVIEW-END -->

<!-- MULTISEED-E-20261117-OVERVIEW-START -->
- **HoPA实际近似误差三seed完成**：[谱理论实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：11-17核对612个actual rollout状态，seed0完全复现旧单seed。inner15下outer600平均E为0.1183±0.0109、outer1950为0.1295±0.0150；8个指定outer点及完整逐seed表图齐全，±为跨3蒸馏seed的样本SD。未重训，仅谱proxy。
<!-- MULTISEED-E-20261117-OVERVIEW-END -->

<!-- THEOREM3-STATES-20261117-OVERVIEW-START -->
- **HoPA训练状态直接近似误差完成**：[谱理论实验卡](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：11-17完成80个专家状态及204个实际合成内循环状态。专家epoch10平均E为0.0672±0.0002；合成各状态均值0.0670–0.2765、P95为0.1137–0.5149，存在波动，谱界保守。原表checkpoint已明确，英文回复和完整表图齐全。
<!-- THEOREM3-STATES-20261117-OVERVIEW-END -->

<!-- N50-BUDGET-OVERVIEW-START -->
- **独立LoRS N50与训练预算曲线**：[结果与协议](experiments/details/EXP-20261107-server-a-hopa-budget-efficiency-equal-budget.md)：**complete**，核对：2026-11-15 15:06:39 +0800。三对N50和声明的学生预算评测已结束；单seed，所有预算点保留。 固定20步双查询R@1：HoPA 27.338%，LoRS50 31.825%；独立LoRS合计训练GPU时间0.467s，HoPA为2.054s。 存在共卡计算，耗时仅作执行记录，不用于公平效率结论。
<!-- N50-BUDGET-OVERVIEW-END -->

- **HoPA 去 L_M 方向分解**：[实验卡](experiments/EXP-20261114-server-a-hopa-lm-directional.md) · [固定末轮均值/方差与全部方向](summaries/EXP-20261114-server-a-hopa-lm-directional/2026-11-15-fixed-final/REPORT.md)：24/24完成；去L_M规模差MSR−1.212±0.252pp、VGG+0.581±0.808pp，VGG仅2/3seed上涨。
- **HoPA 去 L_M 解读限制**：固定末轮与选优口径的VGG趋势符号不同；稿件/manifest的VGG样本量及lr_lr记载待核对，DiDeMo/pairwise机制未由本轮验证。

- **MSR-VTT AC W2联合评测**：[联合对齐实验](experiments/EXP-20261112-server-a-hopa-joint-alignment.md)：11-13固定学生20轮已完成，双查询R@1为HoPA30.053%、共享3-pair25.867%、独立LoRS32.541%；HoPA/共享3-pair的ρ为0.484814/0.464067。保留旧学生选优结果；合成集仍沿用历史test外层选择，非完全独立测试。

这里统一记录研究问题、实验状态、主要结论和结果位置。通常一个研究问题对应一张实验卡；同一问题的种子、消融、失败重试和续跑放在卡内。历史基线与方法探索可按章节汇总，如 EXP-001。GitHub 保留实验结论、关键结果表与 Markdown 报告；原始配置、详细数据、图件、日志和 checkpoint 留在本地。阅读版报告位于 `summaries/`，原始快照仍在本地 `results/`。

首批整理范围为 2026-10-13 至 10-20。已有历史基线见 EXP-001；11-19 补录早期 PMRL、重建、BaryBind 与冻结特征诊断，并用本机评测产物更新近期实验。核对范围为本机工作区、授权数据目录及已有 GitHub 记录，其他服务器独有产物仍以各自可核实的源记录为准。

[11-19 补录索引](summaries/recent-20261119/README.md)收录新报告和历史实验入口。[11-03 至 11-10 周报](weekly/2026-11-03_2026-11-10.md)保留当周记录状态，四方法固定末轮和 MSRVTT head 初始化以对应实验卡的完整结果为准。

本目录是独立 Git 仓库，分支为 `main`，远端为 [ericgao966666/HypOmni-Exps](https://github.com/ericgao966666/HypOmni-Exps)。两台服务器的使用方式见[同步说明](SYNC.md)，维护规则见 [AGENTS.md](AGENTS.md)。本地内容是否已经推送，以 Git 分支状态和远端提交记录为准。

快捷入口：[新服务器固定15轮操作指南](operations/OPS-20261106-native-baselines-fixed15.md) · [结果报告](summaries/README.md) · [本地证据与图件](LOCAL_ARTIFACTS.md) · [运行记录说明](runs/README.md) · [本机路径配置](config/README.md)

同步范围于 **2026-11-05** 调整为总结文档；这次整理没有重新运行实验，也没有更新各实验原有的结果核对日期。数据与图件不再出现在当前 GitHub 文件树，旧提交历史保留。两台服务器首次更新的本地文件保护步骤见 [SYNC.md](SYNC.md)。

**Rebuttal专用检索入口：** [10个研究问题、reviewer对应与各补充实验](summaries/rebuttal-20261112/README.md)。11-12已补等预算队列说明，并将N500调参、随机head完整终测、正初始化蒸馏的最终结果回填原卡；原协议与失败历史保留。

## 当前关注

<!-- Q3-SOURCE5-STUDENT5-START -->
- **Table3五源×五学生扩充**：Table3五源×五学生扩充stopped，核对2026-11-15T14:34:38.430889+08:00：60/100条，新增24/64条，复用36条。 当前平衡子集为3源×5学生；LanguageBind/OmniBind的D−R R@1分别+0.0422±0.1445/-0.0061±0.1844pp。 [实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)。 按用户要求停止，保留已有结果；五源完整结果未完成。
<!-- Q3-SOURCE5-STUDENT5-END -->

<!-- Q3-LB-OMNI-STUDENT3-START -->
- **Table 3学生seed重复**：LanguageBind head与OmniBind dense的三源×三学生seed评测完成，核对2026-11-14T03:43:22.279439+08:00。固定20轮配对D−R R@1：LanguageBind +0.0602±0.1287pp，OmniBind +0.0241±0.2294pp。 [实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)。
<!-- Q3-LB-OMNI-STUDENT3-END -->

<!-- Q3-OMNI-DENSE20-START -->
- **OmniBind dense head对照**：OmniBind dense head20轮对照已完成，核对2026-11-14T00:26:27.996235+08:00。三源seed固定20轮Random/Distilled R@1为12.9028%/12.9861%；配对D−R +0.0833±0.1734pp；Distilled相对Frozen +0.2444pp。 [实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)。
<!-- Q3-OMNI-DENSE20-END -->

<!-- Q3-WBCE-TEMPERATURE-V2-START -->
- **ImageBind原生评测温度修正**：原生WBCE温度修正复评已完成15/15，核对2026-11-13T18:10:05.219778+08:00。三源seed、各自重新选定checkpoint后，Random/Distilled测试六方向R@1为12.7083%/12.6472%；配对D−R为-0.0611±0.3369pp。 [实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)。
<!-- Q3-WBCE-TEMPERATURE-V2-END -->

<!-- Q5-LIFETIME-MEMORY-OVERVIEW-START -->
- **六方法Q100完整进程显存**：GPU7单卡串行，已完成14/14个测量进程；100步并检查末段稳定性，必要时300步，含初始化与最终保存。MTT-VL/TESLA为仓库适配版。[结果卡](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)。
<!-- Q5-LIFETIME-MEMORY-OVERVIEW-END -->

<!-- HOPA-POSITIVE-DISTILL-START -->
[正初始化蒸馏小试](experiments/EXP-20261111-server-a-hopa-positive-distill.md)：11-11完成，11-12补齐结果。验证R@1固定LR：HoPA/联合LoRS为4.076/3.688%；learned-LR为5.097/3.681%。一个蒸馏seed、三个配对新head，无test。
<!-- HOPA-POSITIVE-DISTILL-END -->

<!-- PMRL-POSITIVE-INIT-START -->
- **PMRL正余弦前提小试完成**：[初始化与持续约束](experiments/EXP-20261111-server-a-pmrl-positive-init.md)：无pairwise warm-up，Full验证R@1从普通随机2.208%提高到仅正初始化20.292%、持续正约束20.229%；InfoNCE参照21.458%。8/8、单seed，持续条件负余弦始终0；没有WBCE/蒸馏/test结论。
<!-- PMRL-POSITIVE-INIT-END -->

<!-- RANDOM-HEAD-FULL-STATUS-START -->
完整随机head实验状态：`complete`，核对2026-11-11T00:57:01+08:00。 测试六方向R@1：HoPA 12.472%、联合LoRS 14.174%；HoPA−LoRS -1.702pp，五个独立蒸馏seed。
<!-- RANDOM-HEAD-FULL-STATUS-END -->

<!-- HOPA-RANDOM-HEAD-START -->
- **HoPA随机head完整结果已回填**：[完整终测与历史小试](experiments/EXP-20261110-server-a-hopa-random-head.md)：11-11完成五个独立蒸馏seed；HoPA比Random高9.310pp、比联合LoRS低1.702pp。学生只按800条validation选模，终测884条；CPU小试、GPU校准和资源微测保留为历史。
<!-- HOPA-RANDOM-HEAD-END -->

<!-- Q5-SVD-DIAGNOSTIC-OVERVIEW-START -->
- **HoPA SVD替换计时完成**：[预算与效率实验卡](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)：三个seed扣除专家读取后SVD/mock为0.836/0.569秒/步，减少32.0%，未显示高于旧表39.1%的占比；seed0三对LoRS总时间比从1.271到1.882，当前短测不能单独解释历史退化。11-12核验，原始读取耗时另列。
<!-- Q5-SVD-DIAGNOSTIC-OVERVIEW-END -->

<!-- Q5-A100-EXCLUSIVE-OVERVIEW-START -->
- **A100 GPU5空闲复测完成**：HoPA 155.91s、LoRS三对 241.96s，时间比 1.552；旧短测时间比 1.442。同seed、100测量步，不作多seed结论。[实验卡](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)。
<!-- Q5-A100-EXCLUSIVE-OVERVIEW-END -->

<!-- Q5-A100-COST-START -->
- **HoPA Q5硬件与成本**：短程硬件结果已部分产出，server2完整对照仍在执行；两端关闭学生evaluation，A100共卡限制及结果见[实验卡](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)。
<!-- Q5-A100-COST-END -->

<!-- Q5-A100-MIGRATION-START -->
- **HoPA Q5 A100 迁移**：已传输并通过目标机全量 SHA-256 校验；沿用相同原生代码、MSRVTT 划分、缓存与 80 条专家。已配置传输后纯成本复测，迁移完成不代表测量完成。[实验卡](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)。
<!-- Q5-A100-MIGRATION-END -->

- **HoPA Table 9七组调参已完成**：[MSR-VTT N500联合3-pair](experiments/EXP-20261108-server-a-hopa-joint-tuning.md)：11-09完成、11-12回填；最优conservative测试R@1为20.2489%，较原配置+2.6018pp，但低于配对Random0.4525pp。单seed、test参与选参；固定末态退化保留。

- **HoPA Table 3协议与方差**：[跨架构转移](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)：三源seed主配对18/18完成，固定学生seed1；Distilled−Random平均R@1为imagebind -0.0250pp；languagebind +0.0972pp；omnibind +0.0778pp。完整源seed SD及局限见卡；单seed插值小试另列。
- **Table 3完整实验汇总**：[同一份总报告](summaries/EXP-20261107-server-a-hopa-cross-architecture/TABLE3_COMPLETE_REPORT.md)覆盖历史协议恢复、head/router、多LR全量微调及11-13温度修正；均值、标准差和方差分口径报告。修正后seed1改选step100，下游结果尚未补测。
- **LanguageBind全量微调小试**：[跨架构实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)：预设20轮单seed对照已完成；各设置的Distilled−Random R@1为matched_head20 +0.1500pp；bb1e-5 -0.1417pp；bb3e-6 +0.2167pp。测试驱动的学习率探索，与原三源seed主表分开报告。
- **LanguageBind 3e-6三源seed复核**：[跨架构实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)：6/6配对全量结果与匹配head对照齐全；full的D−R R@1为+0.0750±0.2241pp，Distilled绝对R@1相对head变化-0.0583pp。source2/3新增复核另列，保持测试选模限制。

- **HoPA Q5原生验证通过，优先N100单seed**：[预算与效率](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md)：专家仍为四目标各20条，专家并发上限提高；完成单seed完整对照后评估再扩展。旧v4结论已撤回。

<!-- SPECTRAL-SERVER2-OVERVIEW-START -->
- **HoPA理论条件与配对证据**：[谱变化、负Gram与关系保真](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：合成proxy投影系数加权后Spearman0.8195→0.9059，未达0.93示例门槛，解释获部分支持；同100条阶段ρ下降83/100，固定head后48/100，u₁异号13/100。 当前8.33%对应run的训练采样曲线已补齐，25条minibatch轨迹与100条选中head参考分别标注。 旧v3图已提供指定五节点及六节点版，原均值/SD不变；全点及其他版本保留，口径见实验卡。
- **共享3-pair合成几何补图**：[固定20轮学生读出](experiments/EXP-20261112-server-a-hopa-joint-alignment.md)：每200步共11节点负Gram均0%，合成ρ从0.5513到0.0736；单seed、读出口径与旧HoPA inner16图不同，不作直接方法排名。
<!-- HOPA-FIXED20-OVERVIEW-START -->
- **HoPA固定20轮曲线已补齐**：[每200步全11点读出](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：单seed合成ρ 0.4495→0.4142，与3-pair统一学生训练轮数；各自训练协议的差异仍保留。
<!-- HOPA-FIXED20-OVERVIEW-END -->
- **谱统计主表对齐图**：[状态与checkpoint读出](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：Real初始化与Synthetic选中学生的head不同；600步8.33%已在原生读出曲线上对齐，不能写same fixed heads。
<!-- HOPA-MULTISEED100-OVERVIEW-START -->
- **三seed固定20轮谱曲线已完成**：[21点及指定五节点图](experiments/EXP-20261107-server-a-hopa-spectral-theory.md)：末态ρ 0.413850±0.007898，负Gram 10.555556±7.603605%；独立蒸馏seed0/1/2。
<!-- HOPA-MULTISEED100-OVERVIEW-END -->
<!-- SPECTRAL-SERVER2-OVERVIEW-END -->

- **组合初始化保住VAST起点，两轮检索优于随机，cone仍为0**：[实验卡](experiments/EXP-20261110-server-b-msrvtt-composed-head-init.md)在884视频探索性test上两轮ITC/ITM R@1为37.048%/41.629%，随机对照19.457%/39.536%；组合初态ITC为36.086%。仅单seed短head阶段，不能单独归因三个额外组合head或外推完整微调收益。

- **MSRVTT head 迁移提高检索**。[六组完整测试](experiments/EXP-20261107-server-b-msrvtt-head-init.md)中，VAST 第 5 轮 head 迁移相对同 K 直接微调，在 MSRVTT 的 ITC R@1 提高 10.463–11.538pp、ITM 提高 1.357–1.923pp。迁移组另有 1,610 步 VAST 训练，来自单 seed。

- **VAST全轮次180点已测齐，外部高点在联合第1–2轮**：[完整曲线结论](experiments/EXP-20261106-server-b-geodesic-fixed15.md)中三K四集平均ITM在总epoch6–7最高约51.10–51.22%，到epoch15降低3.50–3.91pp；head第1–5轮仍持续改善，不能把联合后期退化直接归于warmup过长。
- **共同VAST初始化的三方法结果齐全，保留全部模型的重跑已暂停**：[实验卡](experiments/EXP-20261106-server-b-vast-init-baselines.md)原固定15轮及15项测试已完成；MSRVTT ITM R@1为GRAM44.06%、VAST43.55%、PMRL40.21%。按11-08要求在server2独立重跑并永久保留逐轮模型，现因用户需使用GPU而暂停；完整断点及原结果保留，等待明确恢复。原版结果核对21:08、暂停核对23:30（Asia/Shanghai），重跑尚无新正式结果。
- **近期实验已补录**：[近期索引](summaries/recent-20261105/README.md)按研究问题汇总角度、K/合法域、ITM、AURORA及官方权重诊断，完整数据继续只存本地。
- **四方法 30 轮的五集结果已齐**。[固定末轮测试](experiments/EXP-20261103-server-a-joint30-five-datasets.md)共 20/20 项，PMRL 外部四集 ITM R@1 均值 48.605%，GRAM 为 48.172%。MSRVTT 的最高值来自角度组 41.007%。
- **K扫描的检索回升可重复，完整合法层级仍失败**：[测地线与下界](experiments/EXP-20261103-server-a-geodesic-domain.md)中K=.3→.5三seed配对R@1 +0.564±0.125pp；动态合法域由参数化保证，不能当作层级学习成功。
- **角度和GP的证据分开**：[角度最小消融](experiments/EXP-20261101-server-a-angular-alignment.md)A0比距离带锥高0.220pp，但比角度无蕴含仅高0.008pp；[GP替代](experiments/EXP-20261102-server-a-gromov-alignment.md)的最佳直接增益区间跨0。
- **图文重建与零训练审计已补齐**：[AURORA/CLIP](experiments/EXP-20261101-server-a-aurora-reconstruction.md)为23.661%/23.037% COCO双向R@1；[官方锥审计](experiments/EXP-20261029-server-a-official-cone-audit.md)区分表观与合法满足；[MERU对数映射](experiments/EXP-20261102-server-a-meru-logmap.md)不与训练消融混用。

- **ITM探索完成并锁定C0**：[原生ITM](experiments/EXP-20261027-server-b-itm-native-baseline.md)：验证三seed 49.8128%±0.4189pp，hard下降5.5583pp；锁定后外部MSRVTT/VATEX可用子集46.2104%/79.1571%。[几何诊断](experiments/EXP-20261026-server-b-itm-geometry-diagnostics.md)与[作者权重补测](experiments/EXP-20261027-server-b-itm-author-baselines.md)分卡记录，避免混淆协议。

- **VAST数据规模对照**：[实验记录](experiments/EXP-20261026-server2-pmrl-data-scale.md)：当前120,688条相对105,369条：Top-50 +0.0644pp，direct +0.0069pp；单seed。
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

<!-- HOPA-LOW-BUDGET-START -->
**HoPA低tuple预算**：[N25/50/100配对曲线](experiments/EXP-20261108-server-a-hopa-low-budget.md)：已迁移server2，完成9/9个条件，3蒸馏seed；仅HoPA–Random、按显存容量并发、排除GPU4，原生test选模与固定末态同时报告。核对11-09 03:33（Asia/Shanghai），结论以完整三seed结果为准。
<!-- HOPA-LOW-BUDGET-END -->


<!-- HOPA-Q2-STATUS-START -->
**HoPA模态数量**：[四组合结果](experiments/EXP-20261111-server-a-hopa-modality-scaling.md)：test四模态HoPA/独立LoRS为2.887/2.827%；11-12 validation复核为6.418/7.512%，90组预测与已有记录一致。两种评估口径分别保留，原Table8的LoRS为共享四元组版本。
<!-- HOPA-Q2-STATUS-END -->


<!-- HOPA-Q2-SHARED-START -->
共享LoRS已完成，核对2026-11-12 18:36:04 +0800。四组合三seed、validation/test与独占成本均齐全；结论及数值见实验卡共享对照章节。
<!-- HOPA-Q2-SHARED-END -->


<!-- HOPA-Q2-SVD-START -->
**Ego4D Lemma2模态权重**：[实验卡](experiments/EXP-20261111-server-a-hopa-modality-scaling.md)：已按论文u₁重报固定专家probe，IMU平均系数0.2965→0.2106，始终较小且13%–28%为负；只统一整体符号，原u₁²能量份额留作辅助。离线诊断非因果证明，核对2026-11-14。
<!-- HOPA-Q2-SVD-END -->

## 实验目录

| 编号 / 简称 | 研究问题 | 项目 | 最近实验记录 | 状态 | 当前判断 |
|---|---|---|---|---|---|
| HoPA谱条件与关系 | [选中状态、配对与加权诊断](experiments/EXP-20261107-server-a-hopa-spectral-theory.md) | HoPA-Rebuttal | 11-09结果；11-12记录核对 | 主结果及三项补测已有记录 | 非负前提非全满足；加权proxy相关0.905889，单seed |
| HoPA跨架构 | [三源seed迁移与全量微调](experiments/EXP-20261107-server-a-hopa-cross-architecture.md) | HoPA-Rebuttal | 11-10至11-11结果 | 18项配对完成；补充适配/全量微调齐全 | 三架构R@1配对差值−0.0250/+0.0972/+0.0778pp；test-informed |
| HoPA预算与效率 | [原生预算、硬件、SVD和显存](experiments/EXP-20261107-server-a-hopa-budget-efficiency.md) | HoPA-Rebuttal | 11-12诊断结果 | 原生单seed及诊断有结果；等预算队列执行待核实 | 旧v1–v4撤回；SVD替换扣读取省32.0%；不同协议分开 |
| HoPA N500调参 | [联合3-pair七配置](experiments/EXP-20261108-server-a-hopa-joint-tuning.md) | HoPA-Rebuttal | 11-09完成；11-12回填 | 7/7完成，单seed | 最优R@1 20.2489%，配对Random20.7014%，未超过Random |
| HoPA低tuple预算 | [N25/50/100三个seed](experiments/EXP-20261108-server-a-hopa-low-budget.md) | HoPA-Rebuttal | 11-09完成镜像 | 9/9完成，已保留两种选模口径 | 低预算收益未稳定扩大；固定末态负结果保留 |
| HoPA正初始化蒸馏 | [严格配对起点与两种LR读出](experiments/EXP-20261111-server-a-hopa-positive-distill.md) | HoPA-Rebuttal | 11-11完成；11-12回填 | 单蒸馏seed、三学生head验证完成 | 固定LR HoPA/LoRS4.076/3.688%；learned-LR5.097/3.681%；无test |
| HoPA模态数量 | [四组合、验证复核与共享LoRS](experiments/EXP-20261111-server-a-hopa-modality-scaling.md) | HoPA-Rebuttal | 11-11至11-12 | 独立pair完成；共享tuple补充未齐 | 四模态test HoPA/独立LoRS2.887/2.827%；validation不能混报 |
| PMRL正余弦初值 | [预设非负前提是否能冷启动](experiments/EXP-20261111-server-a-pmrl-positive-init.md) | HoPA-Rebuttal | 11-11 12:08完成 | 8条件单seed小试完成 | 无warm-up的Full约20.2%，随机2.2%；尚无新蒸馏 |
| HoPA随机head | [可学习性与完整五seed蒸馏](experiments/EXP-20261110-server-a-hopa-random-head.md) | HoPA-Rebuttal | 11-11完成；11-12回填 | 完整终测完成，历史小试保留 | test HoPA12.472%、联合LoRS14.174%；HoPA−Random +9.310pp |
| 测地线梯度路由 | [半径学习与主干更新](experiments/EXP-20261110-server-b-geodesic-gradient-routes.md) | Hyperbolic-Omnimodal | 11-11 | 两个续训条件完成 | 第 10 轮验证 ITM R@1，冻结 32.202%，正常联合 50.879%，阻断 cone 51.050% |
| HoPA 去 L_M | [去 L_M 方向消融](experiments/EXP-20261114-server-a-hopa-lm-directional.md) | HoPA | 11-14 至 15 | 双数据集三 seed 主实验 24/24，另有 VGGSound-S 两 seed 配对快照 | 固定末轮去 L_M 的 N100→N500 变化：MSRVTT −1.212±0.252pp，VGGSound-S +0.581±0.808pp |
| LanguageBind 正初始化 | [严格配对 CE/WBCE 与独立 LoRS](experiments/EXP-20261114-server-b-languagebind-positive.md) | LanguageBind | 11-14 至 15 | 两组补实验已完成，验证集 | 独立 LoRS 固定 LR R@1 3.201%，HoPA 学习 LR 3.611% |
| 早期 PMRL 目标与宽度 | [谱目标、半径、直接压缩与后接低维 head](experiments/EXP-20260818-pmrl-objectives-width.md) | PMRL | 08-02 至 18 | 历史对照已归档 | 8D 有单 seed 正信号；严格配对 64D post-head 双曲回落 |
| PMRL 重建与正则 | [SCRR、decoder 筛选与 proxy 方向](experiments/EXP-20260826-pmrl-reconstruction.md) | PMRL-Reconstruction | 08–09 | 核心对照及诊断完成 | 323 步仅正则 46.6628%，full 45.0226% |
| Parent 代理 | [均值、SVD、低维及类别探针](experiments/EXP-20260929-pmrl-parent-proxies.md) | PMRL | 09-28 至 30 | 固定预算对照完成 | Top-50 R@1 差值很小；类别正例严格锥满足为 0 |
| Lorentz 全模态 | [映射、谱共识及曲率](experiments/EXP-20260929-pmrl-lorentz-omnimodal.md) | PMRL | 09-29 至 30 | 探索与三 seed 确认完成 | 新的完整曲率组 Top-50 58.7833%，对照 59.5333% |
| BaryBind 复现 | [预算匹配 PMRL 与 WB 软势修订](experiments/EXP-20261009-barybind-reproduction.md) | BaryBind | 10-09 至 10 | 四集结果已归档 | 末态 MSR-VTT T→V/V→T 相对 PMRL +1.584/+0.566pp |
| 谱 proxy 与残差 | [冻结 VAST 的 MSR-VTT 校准诊断](experiments/EXP-20261012-msrvtt-spectral-proxy-dependence.md) | PMRL-Reconstruction | 10-12 | 已完成，当前保留完成记录 | 完整 proxy 5/9，留一 proxy 9/9 |
| VAST 树假设 | [冻结特征 D1–D4](experiments/EXP-20261013-vast-tree-assumption.md) | VAST | 10-13 | D1–D4 完成 | 全局树未过阈值，视觉与音频局部嵌套有信号 |
| 多模态证据顺序 | [两轮合成、切空间与 AudioCaps 门控](experiments/EXP-20261015-multimodal-order-diagnostics.md) | PMRL-minimal-hyperbolic | 10-15 | 诊断完成，E3 未启动 | 合成 Lorentz O4 的子集内部 ρ 为 0.219，音频验证未过门槛 |
| MSRVTT head 初始化 | [直接微调与 VAST head 迁移](experiments/EXP-20261107-server-b-msrvtt-head-init.md) | Hyperbolic-Omnimodal | 11-09 源报告，11-19 文件核对 | 六组训练与五集测试完成 | 同 K 迁移组的 MSRVTT ITM 提高 1.357–1.923pp |
| VAST组合head初始化 | [保留检索起点与两轮冷启动对照](experiments/EXP-20261110-server-b-msrvtt-composed-head-init.md) | Hyperbolic-Omnimodal | 11-10源端记录 | 两条件两轮小试完成 | 组合/随机ITM41.629%/39.536%；单seed探索性test，严格cone仍为0% |
| 测地线固定15轮 | [固定15轮结果与完整外部曲线](experiments/EXP-20261106-server-b-geodesic-fixed15.md) | Hyperbolic-Omnimodal | 11-10最终核验 | 权重恢复及180点补评完成 | 外部高点在总epoch6–7；head前5轮持续改善，后期joint退化 |
| 共同VAST起点固定15轮基线 | [共同初始化下比较VAST/GRAM/PMRL](experiments/EXP-20261106-server-b-vast-init-baselines.md) | Hyperbolic-Omnimodal | 11-08 21:08结果/23:30暂停核对，Asia/Shanghai | 原版三方法/15项测试完成；keepall重跑按用户要求暂停，完整断点保留 | MSRVTT ITM R@1：GRAM44.06%、VAST43.55%、PMRL40.21%；重跑尚无新正式结果 |
| 锥训练参数 | [锥训练参数：改善局部满足仍未形成完整层级](experiments/EXP-20261029-server-a-cone-parameters.md) | Hyperbolic-Omnimodal | 10-29；11-05核对 | 已完成 | K=.3合法满足12.869%，检索−0.684pp |
| 原C0几何控制 | [原C0几何控制：双曲无锥略优，锥约束有检索代价](experiments/EXP-20261030-server-a-c0-geometry.md) | Hyperbolic-Omnimodal | 10-30；11-05核对 | 已完成 | 512D无锥双曲R@1 19.019%，欧氏18.783% |
| R3固定曲率 | [R3固定曲率：64D验证候选小幅提高，尚无新测试](experiments/EXP-20261029-server-a-r3-curvature.md) | Hyperbolic-Omnimodal | 10-29；11-05核对 | 已完成 | 固定c=.3/τ=.035：MSRVTT验证28.467% |
| ARGENT/AURORA组件 | [ARGENT/AURORA组件：角度检索提高，样本特异层级未证实](experiments/EXP-20261030-server-a-argent-components.md) | Hyperbolic-Omnimodal | 10-30；11-05核对 | 已完成 | S主读出19.173%，相对B0 +0.423pp |
| 角度对齐 | [角度对齐：减轻蕴含的检索代价，完整合法层级仍失败](experiments/EXP-20261101-server-a-angular-alignment.md) | Hyperbolic-Omnimodal | 11-01；11-05核对 | 已完成 | A0 18.970%，相对距离带锥+0.220pp |
| 测地线K与半径下界 | [测地线K与半径下界：检索回升可重复，合法域仍是瓶颈](experiments/EXP-20261103-server-a-geodesic-domain.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | K=.3→.5三seed回升+0.564±0.125pp |
| Gromov product | [Gromov product：46组探索未找到可信的替代收益](experiments/EXP-20261102-server-a-gromov-alignment.md) | Hyperbolic-Omnimodal | 11-02；11-05核对 | 已完成 | GP_E仅+0.024pp，区间跨0 |
| ITM几何输入 | [ITM几何输入：两套三seed门槛均保留原均匀基线](experiments/EXP-20261103-server-a-itm-geometry.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | I2/D3均未过门槛，锁定I0/D0 |
| 模态组合锥与理想根 | [模态组合锥与理想根：18条件均未通过预设双目标](experiments/EXP-20261103-server-a-cone-root.md) | Hyperbolic-Omnimodal | 11-03；11-05核对 | 已完成 | 18/18完成，均未过双目标门槛 |
| 四方法 30 轮与五数据集 | [同预算固定末轮](experiments/EXP-20261103-server-a-joint30-five-datasets.md) | Hyperbolic-Omnimodal | 11-05 源报告，11-19 文件核对 | 20/20 正式测试 | PMRL 外部均值 48.605%，角度在 MSRVTT 最高 41.007% |
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
| PMRL 数据扩充 | [扩充VAST是否改善单轮检索](experiments/EXP-20261026-server2-pmrl-data-scale.md) | PMRL-minimal-hyperbolic / server1 | 2026-11-03 21:41，Asia/Shanghai | 三组同协议结果齐全，当前轮完成 | 当前120,688条相对105,369条：Top-50 +0.0644pp，direct +0.0069pp |
| EXP-009 | [低维空间是否放大几何差异](experiments/EXP-009-lowdim-finetune.md) · [五方法展示](summaries/EXP-009/2026-10-20-server-b-five-methods/README.md) | Hyperbolic-Omnimodal | 10-19 至 10-20 | MSRVTT 42组主实验＋1组λ消融全部完成；ActivityNet未训练 | 新初始化流程下，六维度有锥均未严格包含；λ=1改善16D R@1约1pp |

“已完成”指卡内声明的运行与评估完成，不代表假设成立，也不代表证明收敛。运行预算、验证集结果、测试集结果分别记录。

## 数据与基础设施

| 编号 | 工作 | 状态 | 对实验的影响 |
|---|---|---|---|
| OPS-001 | [VAST 150k 缺失媒体恢复](operations/OPS-001-vast-recovery.md) | 11-19 00:07源下载重启后已新增5条，保持单并发；server3复制状态仅有11-13续传历史，本次未核验 | 源可用144,568对；复制原固定快照135,798对及最终补传计划保留，远端当前状态待复核，冻结实验manifest保留 |

## 周度回顾

- [2026 年 11 月 03 至 10 日：双曲多模态实验与记录缺口](weekly/2026-11-03_2026-11-10.md)
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

历史源服务器路径只用于溯源，不代表本机可访问；各机器的实际数据目录仅在本地忽略配置中登记。线上优先读取 `summaries/` 中的报告；复核详细证据时读取本地快照，不自动迁移或重写其他服务器路径。

## 2026-10-28补充

λ=.3、c/τ联合学习已完成30轮；C0累计79条件完成。[三组λ匹配报告](summaries/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/REPORT.md)，仅seed50验证；本轮纳入统一同步。

<!-- LB-POSITIVE-START -->
完整单seed续跑已完成。固定LR验证R@1：HoPA 3.125±0.430%，联合LoRS 2.431±0.087%，配对均值差+0.694pp。 learned-LR验证R@1：HoPA 3.611±0.345%，联合LoRS 2.382±0.167%，配对均值差+1.229pp。 SD仅为三个学生head的波动，无test。 [实验卡](experiments/EXP-20261111-server-a-hopa-positive-distill.md)。
<!-- LB-POSITIVE-END -->

<!-- Q3-LB-POSITIVE-START -->
Table3 LanguageBind初始化小试完成。固定3000更新：pretrained D−R R@1 +0.050±0.102pp；neutral D−R R@1 -0.156±0.285pp；positive_free D−R R@1 -0.164±0.121pp。 [实验卡](experiments/EXP-20261107-server-a-hopa-cross-architecture.md)。
<!-- Q3-LB-POSITIVE-END -->

<!-- IB-INDEPENDENT-START -->
ImageBind正初始化独立pairwise补实验已完成。fixed_lr_0.03: HoPA 4.076%，独立LoRS 4.326%，HoPA−独立 -0.250pp；learned_lr: HoPA 5.097%，独立LoRS 4.507%，HoPA−独立 +0.590pp。 [实验卡](experiments/EXP-20261111-server-a-hopa-positive-distill.md)。
<!-- IB-INDEPENDENT-END -->

<!-- LB-INDEPENDENT-START -->
LanguageBind正初始化独立pairwise补实验已完成。fixed_lr_0.03：HoPA 3.125±0.430%，独立LoRS 3.201±0.024%，差值-0.076pp；learned_lr：HoPA 3.611±0.345%，独立LoRS 3.236±0.052%，差值+0.375pp。 [实验卡](experiments/EXP-20261111-server-a-hopa-positive-distill.md)。
<!-- LB-INDEPENDENT-END -->
