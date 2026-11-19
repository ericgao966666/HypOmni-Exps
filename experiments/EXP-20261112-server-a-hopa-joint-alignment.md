# MSR-VTT联合对齐：补齐pairwise学生后评测多模态查询

<!-- SELECTED-STUDENT-SPECTRAL-20261117-START -->
## 最佳合成集训练后的谱残差：三seed复核

**已完成，核对2026-11-17 20:46:49 +0800。真实test上Random的平均ρ最低，3-pair次之，HoPA最高，三个seed逐一均为该顺序。** 3-pair在自己的distilled data上ρ很低，但真实test上没有保持同样程度的谱集中。因此，本轮不支持“HoPA训练出的evaluation model谱残差最低”；较小ρ也不等于较好的语义检索。

MSR-VTT、N100、source seeds0/1/2；复用各方法历史最佳外层合成checkpoint对应的固定epoch20学生，未重新训练或按ρ选模。HoPA的outer分别为600/400/800，3-pair为1800/1800/2000；Random为同seed初始化抽取的100条真实tuple、outer0，不存在蒸馏或最佳外层checkpoint。

| 方法 | 同一真实test 884条：平均ρ↓ | 各自训练数据100条：平均ρ↓ |
|---|---:|---:|
| Random | **0.456403 ± 0.003095** | 0.446965 ± 0.003194 |
| 共享3-pair | <ins>0.463577 ± 0.006380</ins> | **0.071439 ± 0.003070** |
| HoPA | 0.484212 ± 0.003233 | <ins>0.424437 ± 0.016161</ins> |

ρ=1−σ₁²/3，每条实例使用归一化的V/T/A表示；先取seed内实例均值，再对三个source seed求均值±样本标准差（ddof=1）。训练数据列在方法间输入不同，仅作各自训练内拟合描述，不能替代共同test比较。反向共线同样可能ρ=0，谱集中本身不保证模态同向或语义正确。

9个test模型重新前向后，与原保存表示逐元素一致，历史ρ差异为0。8个训练集重新前向，完整token与无损压缩读出误差均为0；HoPA seed0使用原选中模型/合成集的已验证SHA-256表示，原合成权重仍在远端。所有读出通过Gram特征值/SVD及秩1、反向共线、正交解析核验。图和逐seed数值保留于本地报告。

外层仍沿用历史test六方向R@1+R@5选优；每source一个学生，专家池固定，学生目标和RNG沿用各方法原生规则，Random使用HoPA学习器。不能把增加seed或本次重复读出解释成独立测试，也不能将差异单独归因于distilled data。

本地报告、图、CSV/JSON、输入哈希、源码快照与日志：`HoPA-Rebuttal/joint_alignment_eval/spectral_readout_20261117/results_v1/`；执行器`measure.py`位于其上级。源结果核对与文档编辑均为2026-11-17；无新训练、无GPU占用、无原结果覆盖。Git fetch连接失败，远端记录状态尚未核实，未提交或上传。
<!-- SELECTED-STUDENT-SPECTRAL-20261117-END -->

## 11-17三seed扩充

<!-- JOINT-THREE-SEED-START -->
**complete**，核对：2026-11-17 19:01:26 +0800。三个source seed固定20轮、平均双查询R@1（%）：hopa 29.613±0.549；shared3pair 25.855±0.022；random 26.332±0.480。±为跨蒸馏/采样seed的样本SD，外层历史test选择限制保留。
<!-- JOINT-THREE-SEED-END -->

**11-17归一化fusion核验：** 显式使用`q=(t+a)/‖t+a‖`后，10组保存表示×3个联合查询方向×884条test的Hit@1/5/10全部不变；HoPA双查询R@1仍为29.613±0.549%，T+A→V为44.382±0.285%，较Frozen高3.092±0.285pp。归一化只给同一查询的全部候选分数乘同一个正数，检索排序与原等权余弦分数融合等价。它支持多模态查询效用，不新增不可分解高阶交互的证据；ρ与历史test选模限制不变。CPU复评核对2026-11-17 19:45:24 +0800，原结果逐seed回放通过；FP32/FP64少量非前10正确候选名次受浮点近似并列影响，Recall无变化。报告、完整表及来源核验：本地`HoPA-Rebuttal/joint_alignment_eval/analysis/20261117T194415-normalized-sum/REPORT.md`与`results.json`；执行器`audit_normalized_sum.py`，未重训。远端Git状态尚未核实（本轮fetch连接失败）。

用户授权GPU0/1/4/5，各最多一个本任务worker。沿用原N100、2000更新、20条专家池和原生训练；每200步、每5学生epoch按单查询R@1+R@5选择合成集，再读取选中合成集对应epoch20模型。不得把新增seed改成固定outer2000后与原600/1800选中数据混为同协议。

HoPA保留原生source-seeded随机状态；3-pair沿用student_seed1000及评测隔离；每个source仅一个学生。Random为相同source的100条初始化真实tuple，使用HoPA学生目标，读outer0/epoch20；Frozen保持原固定权重。三seed结果将报告源seed间sample SD，而非方向、样本或shuffle的SD。专家池固定，单独说明其随机性没有重新采样。test外层选择限制仍保留，不把增加seed解释成消除选模偏差。

每个新任务先执行同GPU三步保存器数值对齐；旧seed0模型及预测只读校验。所有正式任务完成后统一输出单查询/联合查询、三种方向、打乱控制、ρ及mean±SD。代码：`HoPA-Rebuttal/joint_alignment_eval/seed_extension_20261117/`；运行：数据盘`HoPA/runs/joint_alignment_eval/20261117T172617-server-a-three-seeds/`，进度progress.json、最终analysis/REPORT.md。

**11-15后续预算实验：** [独立LoRS各N50与学生训练预算](details/EXP-20261107-server-a-hopa-budget-efficiency-equal-budget.md)，固定外层2000并报告全部预设学生预算点。它属于预算研究的新执行分支，不替换下方已有N100结果。

[返回实验总览](../README.md) · EXP-20261112-server-a-hopa-joint-alignment · 最新核对：2026-11-13，Asia/Shanghai

<!-- JOINT-STATUS-START -->
**固定学生epoch20版本已完成。** 同一批历史选中合成集上，双查询R@1：HoPA30.053%、共享3-pair25.867%、独立LoRS32.541%；HoPA比共享3-pair高4.186pp，但其ρ为0.484814，仍高于共享3-pair的0.464067。固定训练时长改变了检索排名，没有使HoPA的谱残差领先。外层合成集仍有历史test选模，不能称完全无测试选择。
<!-- JOINT-STATUS-END -->

回应AC W2：在真实测试样本测联合几何，并比较多模态查询检索。两类pairwise学生已补齐；本次按用户要求统一固定学生epoch20。历史N500和随机head结果不替代本轮。

## 既有seed0读出：固定学生epoch20

**只改变学生epoch，不重新选择合成数据。** HoPA使用outer600，共享3-pair使用outer1800，独立VT/VA/AT使用outer1600/2000/2000。Frozen为未训练参考。Random原epoch20未保存，本次用已核实的同100条初始化样本、原生PMRL学生函数与学习率恢复20轮；全部18项指标与历史epoch20日志一致。

884条真实test，单蒸馏seed，Recall单位%。独立LoRS聚合数据和模型预算更大，不计算跨独立模型的三模态ρ。

| 方法 | 单查询R@1↑ | 双查询R@1↑ | 双查询R@5↑ | 平均ρ↓ |
|---|---:|---:|---:|---:|
| 独立LoRS | **22.134** | **32.541** | **59.615** | — |
| HoPA | <ins>21.210</ins> | <ins>30.053</ins> | <ins>56.674</ins> | 0.484814 |
| Frozen | 20.362 | 27.866 | 52.187 | 0.505017 |
| Random | 20.513 | 26.885 | 51.621 | **0.459841** |
| 共享3-pair | 17.496 | 25.867 | 52.489 | <ins>0.464067</ins> |

HoPA−共享3-pair双查询R@1为+4.186pp，视频ID配对bootstrap95%区间[2.300,6.146]pp；HoPA−独立LoRS为−2.489pp，区间[−4.148,−0.753]pp。区间固定模型和gallery，不表示多seed稳定性。共享3-pair从学生epoch5改为20后，单查询R@1下降4.506pp、双查询R@1下降5.882pp，ρ增加0.012416；HoPA原本就是epoch20，因此本次数字完全不变。

该版本消除学生epoch的测试选择，仍保留外层checkpoint的历史选择；而且是在查看旧测试结果后提出的协议检查，应与旧结果同时报告。不能把固定20轮带来的排名反转当作完全独立的确认。ρ与检索没有单调对应，较小ρ不能单独证明语义检索更优。

本地权威报告：原run下`fixed_epoch20_v1/REPORT.md`，完整JSON/CSV、分布图、20组打乱及2000次bootstrap同目录；输入锁定`evaluation_lock.json`，验证`validation_summary.json`。HoPA/Random原生回放通过；共享3-pair原生GPU回放18项通过同一1e-5pp门槛，统一CPU读出的V→A R@5与历史GPU相差一个样本（0.1131pp，六方向平均0.0189pp），明确保留此数值差异。

## 补充：共享3-pair合成checkpoint轨迹

共享3-pair的N100/seed0运行保存了0–2000步每200步的11份合成checkpoint及对应20轮学生head。离线CPU读出全部100条合成实例后，11个节点的负非对角Gram比例均为0/600，ρ均值0.551263→0.073566，γ均值0.457905→2.637495。

这是每checkpoint对应的epoch20评测学生在合成集上的读出，只有一个蒸馏seed；没有跨seed阴影。与历史HoPA v3的inner16训练head、三个seed聚合口径不同，不能直接叠图作同口径方法比较。第0步也经过学生20轮训练，不是未训练head。 该图使用合成实例，不替换上文884条真实test的权威结果。测量对每节点保存完整token前向与压缩前向的核对，最大差异为0；outer1800的真实test嵌入也与原固定20轮结果逐项相同。

本地输出：`HoPA-Rebuttal/results/spectral_theory/shared3pair_outer_every200_20261114/RESULTS.md`及PNG/PDF、CSV、NPZ。只读原checkpoint，无新训练。核对：2026-11-14T00:59:06+08:00。

## 历史：按学生检索选优版本

2026-11-12 22:18完成的旧版本保留在`analysis/REPORT.md`：双查询R@1分别为HoPA30.053%、共享3-pair31.750%、独立LoRS33.183%。当时HoPA学生epoch20、共享3-pair epoch5、独立VT epoch5、VA/AT epoch20、Random epoch10。旧数值、权重和选模记录不覆盖。

## 共享设置与原学生选优协议（历史）

MSR-VTT固定7927 train／884 test，预训练ImageBind、冻结backbone、N100、首轮一个蒸馏seed0。HoPA共享三元组与共享3-pair各N100；独立LoRS每pair N100，聚合预算不同。共享3-pair采用三项pairwise WBCE之和，无谱loss。

原版学生最多20epoch、batch128，SGD momentum0.9、weight-decay0.0005，保留合成学习率与各方法原生调度。新增学生seed1000，每5epoch按test两两R@1+R@5选择，排除epoch0，并保留epoch20；最新读出改为上文的固定epoch20。缺失蒸馏补2000步、16内层步、batch25、rank10/alpha1；其余锁定设置见本地protocol.json。对应专家20×10epoch核验后复用。该预算匹配本轮HoPA，不冒称旧Table9脚本的逐字复现。

## 评测与解释

锁定学生后，计算884真实实例的ρ分布、负余弦和20组打乱；全部三个双模态查询与六个单查询方向；移除/打乱查询。所有检索使用等权余弦分数融合、完整候选库，报告R@1/5/10。独立pair模型不拼接为联合表示，不计算其三模态ρ。

bootstrap按视频ID配对2000次，模型和gallery固定。单seed、历史及新增学生test选模，不能称独立确认测试或多seed稳定性；VT/VA合成源曾按5次学生选择，HoPA为1次，选择历史差异保留。联合指标不参与任何选模，结果不预设HoPA领先。

## 实现与历史运行

2026-11-12用户授权GPU7并行：GPU6共享3-pair与GPU7独立AT均已完成2000更新。保留原训练流程与资源切换记录；旧版本完成证据在本地parallel_progress.json/finished.json。2026-11-13固定20轮版完成证据在fixed_epoch20_v1/finished.json。

已完成已定位本机/server2存档核验和head导入；HoPA与Random原18项单查询指标回放通过。VT/VA及两项新增基线均保留学生权重。原10项CPU检查通过，包含实际预训练head的输出/梯度一致性及原生学生epoch；固定20轮的新模型/数据锁定、原生回放及新旧不变项另行核验通过。

实现验证保留两次失败记录：学生入口缺少observer模块路径，修复后未改变训练算法；专家数据文件字节哈希因JSON缩进不同而不一致，逐字段及顺序核验7927/884条完全相同后改为语义一致性检查并保留两端原始哈希。CPU回放最初两个R@1方向各差一个样本，定位为原生top128掩码影响NumPy并列排序；复用原生规则后全部指标通过，未放宽阈值。

## 来源

本地代码：`HoPA-Rebuttal/joint_alignment_eval/`。本地运行：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/joint_alignment_eval/20261112T203706-server-a-msrvtt-n100/`；来源清单audit.json、权重校验sources/hopa/verified.json、锁定源码source_manifest.json、实时状态progress.json、运行命令jobs/*_launch.json、最终报告analysis/REPORT.md。原始产物只读保留，无提交或上传。Git fetch失败，远端实验记录状态未核实。
