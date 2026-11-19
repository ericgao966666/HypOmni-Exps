# HoPA Table 3 跨架构实验完整报告

<!-- Q3-SOURCE5-STUDENT5-START -->
## 五源×五学生seed扩充 按用户要求停止，保留已有结果；五源完整结果未完成。

Table3五源×五学生扩充stopped，核对2026-11-15T14:34:38.430889+08:00：60/100条，新增24/64条，复用36条。 当前平衡子集为3源×5学生；LanguageBind/OmniBind的D−R R@1分别+0.0422±0.1445/-0.0061±0.1844pp。

| 模型 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| languagebind | random | <ins>5.4883 ± 0.0551</ins> | **21.5611 ± 0.3060** | **32.5367 ± 0.5120** |
| languagebind | distilled | **5.5306 ± 0.0952** | <ins>21.3694 ± 0.1082</ins> | <ins>32.1906 ± 0.2792</ins> |
| omnibind | random | **12.8972 ± 0.0432** | **35.3617 ± 0.0418** | **48.6011 ± 0.1214** |
| omnibind | distilled | <ins>12.8911 ± 0.1741</ins> | <ins>35.3156 ± 0.0270</ins> | <ins>48.5572 ± 0.0766</ins> |

固定20轮；每源先平均5个学生，再统计源间样本SD；新增独立源seed4/5各200步。Random与Distilled使用同样重建流程，主结果包含全部学生重复。源数据仍按历史v1的ImageBind候选曲线选择，与此前迁移数据一致；包含源test选择，不冒充温度修正版或独立留出测试。

本地明细：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/student_repeats/20261115T040224-server-a-source5-student5/REPORT.md`、`summary.json`；summary SHA-256：`74c261fc8956bd296b748b49f7026bbc19186040213efce33852ae603cb5cbd0`。此前3×3结果保留为历史版本。
<!-- Q3-SOURCE5-STUDENT5-END -->

[实验主卡](../../experiments/EXP-20261107-server-a-hopa-cross-architecture.md) · [实验总览](../../README.md) · [Rebuttal目录](../rebuttal-20261112/README.md)

初次整理：2026-11-13；新增dense head结果核对：2026-11-14T00:26:27.996235+08:00。范围包括2026年8—9月的协议恢复材料及截至本次核对的Table 3补充实验。各实验实际完成时间分别保留。

**此前head/router及全量微调结果尚未支持三架构上的稳定蒸馏优势；新增OmniBind dense head结果另列。** 三源seed、100轮data-only迁移中，Distilled−Random的R@1为ImageBind −0.0250pp、LanguageBind +0.0972pp、OmniBind +0.0778pp；LanguageBind全量微调3e-6的差值为+0.0750±0.2241pp，其Distilled绝对R@1比匹配head对照低0.0583pp。11月13日修正ImageBind原生WBCE温度后，原生配对R@1差值仍为−0.0611±0.3369pp。

**当前版本边界：** 最新权威的“原生ImageBind评测”是11月13日温度修正版；现有三架构data-only迁移、LanguageBind插值及全量微调仍使用旧版源数据选择。修正使seed1选中数据从step150变为step100，seed2/3仍为step200；新seed1数据尚未用于下游复评。两类结果回答不同问题，不能将原生修正分数直接填入data-only迁移表。

阅读顺序：[实验清单](#实验清单与版本) → [协议与统计](#统一评测协议与统计口径) → [三架构配对](#三源seed配对迁移) → [LanguageBind训练范围](#languagebind训练范围与学习率) → [温度修正](#imagebind原生评测与温度修正) → [历史诊断](#历史协议恢复与容量诊断) → [方差](#样本方差汇总) → [证据](#证据来源与可复核范围)。

<!-- Q3-OMNI-DENSE20-START -->
## OmniBind当前数据的dense head20轮对照

OmniBind dense head20轮对照已完成，核对2026-11-14T00:26:27.996235+08:00。三源seed固定20轮Random/Distilled R@1为12.9028%/12.9861%；配对D−R +0.0833±0.1734pp；Distilled相对Frozen +0.2444pp。

| 固定20轮设置 | R@1 | R@5 | R@10 |
|---|---:|---:|---:|
| Frozen | 12.7417 | 35.0583 | 48.2167 |
| router random | 12.3528 ± 0.0728 | 34.6306 ± 0.0474 | 47.9583 ± 0.0833 |
| router distilled | 12.3806 ± 0.1417 | 34.5611 ± 0.0096 | 47.8806 ± 0.1468 |
| dense random | <ins>12.9028 ± 0.0173</ins> | **35.3500 ± 0.1500** | <ins>48.5250 ± 0.2126</ins> |
| dense distilled | **12.9861 ± 0.1564** | <ins>35.2028 ± 0.1875</ins> | **48.5806 ± 0.0867** |

三源seed均值±样本SD，ddof=1；Frozen为固定读数。Dense使Random与Distilled的三项均值均超过Frozen，但D−R在R@1/R@10为正、R@5为负，且R@1主要由seed1推动，未显示一致的蒸馏优势。

| Dense数据 | Var R@1 | Var R@5 | Var R@10 |
|---|---:|---:|---:|
| random | 0.000301 | 0.022500 | 0.045208 |
| distilled | 0.024468 | 0.035162 | 0.007523 |

方差单位pp²。新编码的seed1 router控制逐轮复现原控制结果；EVA视觉/文本各4个历史参考样本输出最大误差为0，完整验证见final_verification.json。

使用当前OmniBind原有源数据选择step150/200/200及对应Random；不是温度修正后的seed1 step100。冻结全部encoder、expert projector、router和BN统计，训练三个1536×1536 identity dense映射（7,077,888参数）。SGD LR=.01、momentum=.9、wd=.0005，batch64，tau1/tau2=.1/.2；主报固定20轮，每轮曲线及测试峰值另作诊断。seed2/3原缓存复用，seed1同源媒体本地重编码并补两次router20匹配控制；三个源seed固定学生seed1，不新增源蒸馏。

本地完整报告与曲线：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/dense_head/20261113T232025-server-a-omnibind-dense20/REPORT.md`、`curves.png`；机器结果与方差：`summary.json`；源码与输入身份见该目录清单。 本节summary.json的SHA-256：`0abf94e852b15bafc5636419dbf86f4c28c961b1857bc2f02edde41507d3b10f`。

本节为新增分支，来源独立于文末前版44项整理清单。
<!-- Q3-OMNI-DENSE20-END -->

<!-- Q3-LB-OMNI-STUDENT3-START -->
## LanguageBind与OmniBind每源三学生seed

LanguageBind head与OmniBind dense的三源×三学生seed评测完成，核对2026-11-14T03:43:22.279439+08:00。固定20轮配对D−R R@1：LanguageBind +0.0602±0.1287pp，OmniBind +0.0241±0.2294pp。

| 模型 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| languagebind | random | <ins>5.4602 ± 0.0806</ins> | **21.5667 ± 0.3170** | **32.5148 ± 0.5961** |
| languagebind | distilled | **5.5204 ± 0.0902** | <ins>21.3352 ± 0.2165</ins> | <ins>32.2046 ± 0.2657</ins> |
| omnibind | random | <ins>12.9000 ± 0.0626</ins> | **35.3796 ± 0.0449** | **48.6083 ± 0.1405** |
| omnibind | distilled | **12.9241 ± 0.2042** | <ins>35.2981 ± 0.0385</ins> | <ins>48.5556 ± 0.0846</ins> |

每个模型3个源seed，各自Random/Distilled分别运行学生seed1/2/3；每项固定20轮、80次更新。先在每个源seed内平均3次学生结果，再统计3个源均值的均值±样本SD；每源学生SD、实际方差及九次运行的描述性SD另列。九次运行不是九个独立源蒸馏seed。输入、预训练或identity初始化固定，每个学生重新初始化，seed改变训练shuffle。源数据沿用step150/200/200，源选择仍含历史test信息；ImageBind未在本次追加学生seed。

本地完整结果：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/student_repeats/20261114T031921-server-a-lb-omni-student3/REPORT.md`、`summary.json`；各源学生结果、复用清单和两项seed1一致性重放在同目录。 summary.json SHA-256：`d37b72a83c6f8065d960ca8c7c701de78123c6edf3040f854bca8f53d5e37dfa`。

本节为新增重复实验。其余历史章节中的“固定学生seed1”仍指旧版，不与这里的3×3统计混用。
<!-- Q3-LB-OMNI-STUDENT3-END -->

## 实验清单与版本

| 工作或实验 | 实际覆盖 | 当前用途与状态 |
| --- | --- | --- |
| 投稿Table 3协议审计 | 三架构；历史checkpoint、输入接口、训练参数与指标 | 历史Distilled产物及官方OmniBind旧evaluator未找回；不能按新Random的波动给旧单值补标准差 |
| 历史zero-shot与直接真实样本对照 | 三架构；200条同索引真实样本；单seed | 已完成；直接原始媒体属于real-data coreset，不含重建损失 |
| 共享媒体重建与保真度 | 200条初始化数据；三架构单seed；视频、音频与文本审计 | 已完成；视频近似保真，音频恢复有损 |
| OmniBind视频协议恢复 | Large的8种取帧/聚合候选，另有Base与UniBind诊断 | 已完成；五帧方案参考论文值选择，非独立历史复现 |
| OmniBind可训练参数消融 | 11种post-router配置，另有官方router-only | 已完成；单seed，post-router消融为同CPU runner比较 |
| 固定数据上的学生seed重复 | 三架构×5学生seed＝15次，100轮，仅Random | 已完成；估计学生训练波动 |
| 新raw-space源蒸馏 | 3个独立源seed，各200外层更新，Q200 | 已完成；新生成产物，不是找回历史投稿checkpoint |
| 原生ImageBind节点诊断旧版 | 3源seed×0/50/100/150/200＝15节点，100轮 | 已完成；用于旧源数据选择；旧稀疏读出及重试单独保留 |
| 三架构data-only配对迁移 | 3源seed×Random/Distilled×3架构＝18次，100轮 | 11月10日齐全；使用旧原生选模的150/200/200 |
| LanguageBind直接插值适配 | 源seed1，新增Random/Distilled两次100轮 | 11月9日完成；媒体重建对照复用，不重复计运行 |
| LanguageBind全量微调学习率探索 | 源seed1，1e-5/3e-6×两种数据＝4次；另2次head20 | 11月10日完成；学习率触发使用test信息 |
| LanguageBind固定3e-6多源复核 | 新增源seed2/3的4次full及4次head20；复用seed1 | 11月11日00:18完成；合计8次唯一full运行、6次唯一head20运行 |
| ImageBind温度修正复评 | 同15节点、每节点100轮；源蒸馏未重跑 | 11月13日18:10完成15/15，无失败；最新原生版本 |
| 实现与资源预检 | 数值等价、输入身份、显存、梯度检查点、GPU准入 | 辅助验证；不作为新增性能实验或独立seed |

上述分支存在数据、对照与seed1结果复用，不相加成一个“独立实验数”。原计划90次迁移学生训练已在执行前收缩为18次；原脚本2000更新上限也不能替代本轮实际200更新预算。原生15节点是候选数据的评测，不是15个独立蒸馏seed。

## 统一评测协议与统计口径

数据为VGGSound-S锁定的10,000条训练池和2,000条测试实例；每份Random或Distilled有200个视频、文本、音频triplet。文本使用类别名，测试中有307个不同类别名；重复文本保留为不同候选行，只有同实例对应行是正例。每个R@K先对V↔T、V↔A、T↔A六方向作算术平均。

| 对象 | 训练参数 | 固定部分或输入 |
| --- | --- | --- |
| ImageBind head/postprocess | 3,151,873 | preprocessor与trunk冻结；原生head是预训练参数，不是新建identity MLP |
| LanguageBind projection | 2,162,688 | 三模态encoder冻结；视频/音频/文本原生projection |
| OmniBind Large router | 2,914,347 | expert encoder、expert projector和point router冻结 |
| LanguageBind full | 839,301,376 | 全部视频、文本、音频encoder与projector更新；不是LoRA |

源蒸馏优化预处理视频帧、音频fbank、ImageBind文本trunk token，以及软相似度S和三条学习率。**原生ImageBind评测**直接消费这些优化对象；**data-only迁移**先共享重建为媒体/文本，再由目标自身encoder编码，只迁移数据、不转移源S/LR/head。LanguageBind全量微调仍使用这套重建数据，只扩大目标可训练参数范围。源端“full ImageBind前向”不意味着源backbone权重参与训练。

本轮新源蒸馏使用Q200、200外层更新、16内层步、内层batch20；复用20条历史专家轨迹。已记录的专家池每条有11个快照，最初两个相同，对应9次实际epoch更新；expert_epochs=2表示快照索引跨度，从索引0出发仅跨一次实际更新。本轮没有重新生成专家，也不把200步预算称作收敛证明。

100轮实验每5轮评测，在5/10/…/100中按测试集Avg R@1+Avg R@5选同一epoch，三项Recall取同一轮；epoch0单列zero-shot，固定末轮另列。20轮实验相应在5/10/15/20中选择。源数据先完成200更新，再在50/100/150/200中按原生ImageBind选定一份，所有目标共用；step0只作Random。两级选择都使用test信息，不能称独立验证或无偏留出测试。

报告格式为均值±样本标准差，Recall单位%，差值与标准差单位pp。样本方差为 `s² = Σ(xᵢ−μ)²/(n−1)`，单位pp²，另表给出。单seed的标准差和方差不可估计，不填0。五学生seed统计条件于同一份固定数据；三源seed统计条件于固定学生seed1，两者不混合。对比表仅在说明的可比组内标记最高均值为粗体、第二个不同值为下划线；并列按展示精度处理，标记不表示显著性。

## 三源seed配对迁移

这是现有完整的18项data-only迁移结果。三个源seed均生成200更新的源产物，旧原生选模分别锁定step150/200/200；Random使用各自step0初始化。每架构、每条件各3个源seed，学生seed均为1，训练100轮。标记仅比较同架构的Random与Distilled。

| 架构 | 数据 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- |
| ImageBind | random | **12.7222 ± 0.0631** | **33.7333 ± 0.2210** | <ins>45.3000 ± 0.3586</ins> |
| ImageBind | distilled | <ins>12.6972 ± 0.0774</ins> | <ins>33.5889 ± 0.2536</ins> | **45.3722 ± 0.0994** |
| LanguageBind | random | <ins>5.5944 ± 0.1473</ins> | **22.1472 ± 0.2913** | **33.0333 ± 0.3825** |
| LanguageBind | distilled | **5.6917 ± 0.1083** | <ins>21.4806 ± 0.4004</ins> | <ins>32.4722 ± 0.4301</ins> |
| OmniBind | random | <ins>12.6556 ± 0.0127</ins> | <ins>34.9472 ± 0.0376</ins> | <ins>48.0583 ± 0.3000</ins> |
| OmniBind | distilled | **12.7333 ± 0.1010** | **35.0028 ± 0.0376** | **48.0861 ± 0.1072** |

| 架构 | D−R的R@1 | D−R的R@5 | D−R的R@10 |
| --- | --- | --- | --- |
| ImageBind | -0.0250 ± 0.1377 | -0.1444 ± 0.0867 | +0.0722 ± 0.3432 |
| LanguageBind | +0.0972 ± 0.2496 | -0.6667 ± 0.4691 | -0.5611 ± 0.2983 |
| OmniBind | +0.0778 ± 0.0891 | +0.0556 ± 0.0376 | +0.0278 ± 0.3892 |

ImageBind和LanguageBind没有在三项Recall上形成一致收益；OmniBind三个均值略高，但样本仅三个源seed，不能仅依据均值或排名宣称稳定优势。新温度修正改变seed1的源选择，因此这张表保留为**旧数据选择版本**，而非修正后的最终跨架构表。来源：`HoPA-Rebuttal/cross_arch/artifacts/paired_source_seed_summary.json`。

## LanguageBind训练范围与学习率

### 单源seed的20轮学习率探索

固定源seed1、学生seed1、旧选中step150；全量训练的backbone LR先用1e-5，达到预设效果不足条件后追加3e-6，projector LR始终0.01。使用SGD、momentum=.9、weight decay=.0005、有效batch64、微批4。训练与测试输入预处理固定，更新后的encoder输出重新计算；head20对照采用同一输入视图。

| 数据 | 训练设置 | 选中epoch | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- | --- |
| random | 仅head | 15 | <ins>5.5833</ins> | 21.0833 | **31.9500** |
| random | 全量 LR1e-5 | 5 | **5.6000** | <ins>21.1000</ins> | 31.5083 |
| random | 全量 LR3e-6 | 15 | 5.4250 | **21.2000** | <ins>31.8917</ins> |
| distilled | 仅head | 5 | **5.7333** | <ins>21.3083</ins> | <ins>31.8667</ins> |
| distilled | 全量 LR1e-5 | 5 | 5.4583 | **21.4667** | **31.9500** |
| distilled | 全量 LR3e-6 | 5 | <ins>5.6417</ins> | 21.2000 | 31.8583 |

本表只在同数据条件的三种训练设置之间排名。单seed无可报告的跨seed方差。D−R的R@1依次为head20 +0.1500pp、full1e-5 −0.1417pp、full3e-6 +0.2167pp。full3e-6的配对差值较高，并不意味着其Distilled绝对成绩超过head20。

### 固定3e-6的三源seed复核

固定上一阶段选出的3e-6，不继续调参；新增source2/3的4次全量运行和4次head20对照，复用source1。新增运行启用经全部参数梯度一致性检查的原生gradient checkpointing，保持微批4、有效batch64、目标与预算。结果为三源seed均值±样本SD；同训练范围内比较Random与Distilled。

| 训练范围 | 数据 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- |
| 仅head20 | random | <ins>5.6361 ± 0.0987</ins> | **21.4056 ± 0.3093** | **32.4028 ± 0.3971** |
| 仅head20 | distilled | **5.6417 ± 0.0821** | <ins>21.3889 ± 0.2396</ins> | <ins>31.8528 ± 0.4876</ins> |
| 全量3e-6 20轮 | random | <ins>5.5083 ± 0.1970</ins> | **21.5528 ± 0.3058** | **32.2444 ± 0.3870** |
| 全量3e-6 20轮 | distilled | **5.5833 ± 0.0507** | <ins>21.3472 ± 0.1355</ins> | <ins>31.9750 ± 0.3087</ins> |

| 比较 | R@1差值 | R@5差值 | R@10差值 |
| --- | --- | --- | --- |
| head20 D−R | +0.0056 ± 0.1655 | -0.0167 ± 0.2302 | -0.5500 ± 0.5865 |
| full3e-6 D−R | +0.0750 ± 0.2241 | -0.2056 ± 0.1811 | -0.2694 ± 0.5673 |
| Distilled的full−head | -0.0583 ± 0.0333 | -0.0417 ± 0.1922 | +0.1222 ± 0.2261 |

| 源seed | head20 D−R R@1 | full3e-6 D−R R@1 | Distilled full−head R@1 |
| --- | --- | --- | --- |
| 1 | +0.1500 | +0.2167 | -0.0917 |
| 2 | +0.0417 | +0.1917 | -0.0583 |
| 3 | -0.1750 | -0.1833 | -0.0250 |

source1参与过学习率选择；仅看新增source2/3，full3e-6的D−R为+0.0042±0.2652pp。全量微调没有显示稳定收益，三个源seed的Distilled绝对R@1均低于匹配head20。全量训练共8次唯一运行：1e-5的seed1两次，加3e-6的seed1/2/3六次；1e-5尚无多源seed结果。

### 固定末轮对照

下表保留第20轮读出，不与所选epoch结果混合；仅在同训练范围内排名。

| 训练范围 | 数据 | 末轮R@1 | 末轮R@5 | 末轮R@10 |
| --- | --- | --- | --- | --- |
| 仅head20 | random | **5.5528 ± 0.2092** | **21.4389 ± 0.2584** | **32.3889 ± 0.4208** |
| 仅head20 | distilled | <ins>5.4944 ± 0.0756</ins> | <ins>21.4056 ± 0.2208</ins> | <ins>32.2111 ± 0.1905</ins> |
| 全量3e-6 20轮 | random | <ins>5.4139 ± 0.1435</ins> | **21.5194 ± 0.2726** | **32.5083 ± 0.4524** |
| 全量3e-6 20轮 | distilled | **5.4556 ± 0.0173** | <ins>21.3111 ± 0.1420</ins> | <ins>32.1111 ± 0.2870</ins> |

来源：`full_finetune/20261110T1525-languagebind-seed1/summary.json`与`full_finetune/20261110T2053-languagebind-three-seed-lr3e6/summary.json`，相对路径前缀均为`HoPA-Rebuttal/cross_arch/`。这两批使用旧源数据选择，不能解释为已经用新step100复核。

## LanguageBind输入适配小试

11月9日的单seed探索复用Q200、源seed1的step150与同初始化Random，只将训练视频/fbank改为直接插值到LanguageBind尺寸。媒体重建对照来自18项主评测，仅新增direct两项100轮训练。文本、测试特征、初始化及loss保持原对照；音频resize近似、视频时间适配及绕过随机翻转同时变化，因此不能把变化全部归因于避免Griffin–Lim。

| 数据 | 输入适配 | 选中epoch | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- | --- |
| random | media | 35 | **5.6667** | <ins>21.9667</ins> | **32.8083** |
| random | direct | 50 | <ins>5.6583</ins> | **22.0250** | <ins>32.7000</ins> |
| distilled | media | 60 | **5.6917** | <ins>21.8417</ins> | <ins>32.5750</ins> |
| distilled | direct | 30 | <ins>5.6500</ins> | **22.0500** | **32.7000** |

同条件两种适配之间排名。direct下D−R为−0.0083/+0.0250/0.0000pp，基本没有观察到蒸馏优势；没有以这次单seed探索替换主适配协议。OmniBind未做对应直接插值实验。来源：`HoPA-Rebuttal/cross_arch/adapter_trials/20261109T2202-languagebind-direct-seed1/comparison.json`。

## ImageBind原生评测与温度修正

### 不一致及修正内容

源蒸馏内层使用`WBCE(G / 0.2, S)`，其中`G = u₁u₁ᵀ`；旧原生模型的WBCE分支使用`WBCE(G, S)`，且评测入口没有把CLI的tau1/tau2传入模型。11月13日修正入口参数传递，并在WBCE分支仅应用一次tau2，使其与已生成源数据时的内层目标一致。原有S、三条学习率、数据、采样器、optimizer和100轮预算保持；没有重新蒸馏。

12项CPU检查与GPU6/7的损失及梯度一致性检查通过；之后在独立版本中复评全部15节点，18:10完成。每worker上限18GiB、每卡最多2worker，最大allocated14.7323GiB、reserved17.6523GiB；共卡时间不作为论文效率证据。

### 修正前后按各版本选择数据

| 评测版本 | 数据 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- |
| 旧原生 | random | **12.8528 ± 0.1119** | <ins>33.5861 ± 0.2407</ins> | <ins>45.2194 ± 0.3979</ins> |
| 旧原生 | distilled | <ins>12.7500 ± 0.0961</ins> | **33.8028 ± 0.2237** | **45.6167 ± 0.2268** |
| 温度修正原生 | random | **12.7083 ± 0.1746** | **33.9333 ± 0.3392** | <ins>45.4389 ± 0.1491</ins> |
| 温度修正原生 | distilled | <ins>12.6472 ± 0.2417</ins> | <ins>33.9194 ± 0.0459</ins> | **45.5611 ± 0.1780** |

| 评测版本 | D−R R@1 | D−R R@5 | D−R R@10 |
| --- | --- | --- | --- |
| 旧原生 | -0.1028 ± 0.1838 | +0.2167 ± 0.0433 | +0.3972 ± 0.2936 |
| 温度修正原生 | -0.0611 ± 0.3369 | -0.0139 ± 0.3849 | +0.1222 ± 0.2375 |

| 源seed | 旧选中外层step | 新选中外层step | 新学生epoch | 新D−R R@1 |
| --- | --- | --- | --- | --- |
| 1 | 150 | 100 | 70 | +0.1417 |
| 2 | 200 | 200 | 35 | -0.4500 |
| 3 | 200 | 200 | 55 | +0.1250 |

温度不一致是实在的实现问题，但修正没有恢复稳定的R@1优势。新旧汇总同时包含源数据选择变化；为区分两者，下面固定为旧版150/200/200三份Distilled，只改变原生评测实现。

| 修正评测但固定旧数据 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- |
| random | **12.7083 ± 0.1746** | **33.9333 ± 0.3392** | **45.4389 ± 0.1491** |
| distilled | <ins>12.6250 ± 0.2088</ins> | <ins>33.9028 ± 0.0747</ins> | <ins>45.4000 ± 0.2155</ins> |

### 全部15个节点的新旧读出

每个单元格按R@1 / R@5 / R@10排列。旧、新各自按同源seed的五个节点分别标记各指标最优/次优；最佳epoch也各自按R@1+R@5选择。step0为Random，不参与Distilled外层选择。

| 源seed | 外层step | 旧epoch | 旧R@1 / R@5 / R@10 | 新epoch | 新R@1 / R@5 / R@10 |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 20 | **12.9333** / 33.7333 / 45.5917 | 85 | 12.7500 / **34.3250** / <ins>45.5667</ins> |
| 1 | 50 | 10 | 12.6917 / 33.6333 / 45.2417 | 35 | 12.4000 / 33.5500 / 45.2917 |
| 1 | 100 | 10 | <ins>12.8917</ins> / 33.6833 / <ins>45.7750</ins> | 70 | **12.8917** / <ins>33.8667</ins> / **45.6917** |
| 1 | 150 | 20 | 12.7833 / **33.9750** / 45.6500 | 95 | <ins>12.8250</ins> / 33.8167 / 45.2083 |
| 1 | 200 | 15 | 12.6583 / <ins>33.8667</ins> / **45.8000** | 80 | 12.7000 / 33.6500 / 44.9583 |
| 2 | 0 | 10 | <ins>12.7250</ins> / 33.3083 / 44.8000 | 60 | **12.8583** / <ins>33.7333</ins> / **45.4750** |
| 2 | 50 | 10 | 12.4833 / 33.2167 / 45.0500 | 90 | 12.3833 / 33.5667 / 44.7833 |
| 2 | 100 | 10 | 12.6833 / 33.2500 / <ins>45.1917</ins> | 60 | <ins>12.6917</ins> / 33.4250 / 45.1083 |
| 2 | 150 | 15 | 12.6583 / **33.6750** / 44.9917 | 80 | 12.5000 / 33.2917 / 44.7833 |
| 2 | 200 | 15 | **12.8250** / <ins>33.5500</ins> / **45.3750** | 35 | 12.4083 / **33.9417** / <ins>45.3583</ins> |
| 3 | 0 | 15 | <ins>12.9000</ins> / <ins>33.7167</ins> / 45.2667 | 55 | 12.5167 / <ins>33.7417</ins> / 45.2750 |
| 3 | 50 | 15 | **12.9250** / 33.5083 / <ins>45.3750</ins> | 75 | **12.8000** / 33.6583 / <ins>45.3167</ins> |
| 3 | 100 | 15 | 12.7167 / 33.6000 / 45.3417 | 95 | 12.6083 / 33.3917 / 45.0750 |
| 3 | 150 | 25 | 12.4750 / 33.2667 / 44.9083 | 65 | 12.1500 / 33.1333 / 44.5417 |
| 3 | 200 | 10 | 12.6417 / **33.8833** / **45.8250** | 55 | <ins>12.6417</ins> / **33.9500** / **45.6333** |

旧原生15节点之外，另有8份只含稀疏评测的旧读出被排除；完整周期结果才进入主统计。旧目录`runs/native-checkpoint-eval-v1/`与新目录`runs/20261113T173102-server-a-native-wbce-temperature-v2/`均保留，前缀为`HoPA-Rebuttal/cross_arch/`。新结果按测试选模，不能与独立validation选模结果等同。

## 固定数据上的五学生seed实验

这一批固定同一份Q200重建初始化Random与预训练权重，仅改变学生minibatch顺序，三个架构各5次、各100轮。它回答训练随机性，不回答独立蒸馏数据的随机性。当前主读出为test-selected best；固定100轮作为后期退化诊断。跨架构行不作性能排名。

| 架构 | 读出 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- |
| ImageBind | 测试选epoch | 12.8083 ± 0.0835 | 34.0600 ± 0.1020 | 45.6000 ± 0.0775 |
| ImageBind | 固定100轮 | 12.7483 ± 0.0686 | 34.0583 ± 0.1082 | 45.6333 ± 0.0876 |
| LanguageBind | 测试选epoch | 5.7467 ± 0.0855 | 21.7567 ± 0.1837 | 32.6967 ± 0.1432 |
| LanguageBind | 固定100轮 | 5.4750 ± 0.0764 | 21.1850 ± 0.1447 | 32.3733 ± 0.1583 |
| OmniBind | 测试选epoch | 12.7767 ± 0.1310 | 34.9633 ± 0.2186 | 48.1800 ± 0.0830 |
| OmniBind | 固定100轮 | 12.4533 ± 0.1422 | 34.6267 ± 0.2592 | 47.8050 ± 0.1475 |

OmniBind固定末轮12.4533/34.6267/47.8050低于本批zero-shot12.7417/35.0583/48.2167，负结果保留。历史Distilled checkpoint缺失，不能把本批Random标准差加到论文Distilled单值上。来源：`HoPA-Rebuttal/cross_arch/artifacts/student_seed_summary.json`。

## 历史协议恢复与容量诊断

下列为8—9月历史产物及11月协议审计所追溯的分支。旧文档曾使用Table 4编号；最终投稿PDF对应Table 3。历史材料中“validation”实际调用test，“新建identity head”等概括也不适用于所有架构；本报告以已核查的实际可训练参数和测试选模说明为准。历史论文单值不能替代后来新生成数据的配对结果，也不能给当前负结果提供缺失的方差。

### 投稿表中的历史参考

| 模型 | 投稿设置 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- |
| ImageBind | w/o Distilled | 12.25 | 32.87 | 44.32 |
| ImageBind | w/ Random | <ins>12.83</ins> | <ins>33.89</ins> | <ins>45.57</ins> |
| ImageBind | w/ Distilled | **13.15** | **35.33** | **47.34** |
| LanguageBind | w/o Distilled | 4.91 | 19.94 | 29.56 |
| LanguageBind | w/ Random | <ins>5.87</ins> | <ins>21.76</ins> | <ins>32.67</ins> |
| LanguageBind | w/ Distilled | **5.93** | **22.11** | **33.32** |
| OmniBind | w/o Distilled | <ins>12.92</ins> | 34.88 | 48.03 |
| OmniBind | w/ Random | 12.75 | <ins>34.93</ins> | <ins>48.28</ins> |
| OmniBind | w/ Distilled | **13.13** | **35.63** | **48.87** |

数值来自本地投稿PDF第8页，原表未报告方差。此处排名只复述同模型论文行的数值次序，不补作“同一实现已复现”的证据。原Distilled产物和官方OmniBind旧evaluator未恢复；后补Random存在重建与可训练模块差异。

### 真实媒体与重建初始化对照

| 架构或训练模块 | 数据设置 | epoch | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- | --- |
| ImageBind | zero-shot | 0 | 12.4250 | 32.6417 | 44.4083 |
| ImageBind | 直接同索引真实媒体 | 100 | <ins>12.6333</ins> | **34.2667** | **45.8333** |
| ImageBind | 重建初始化媒体 | 50 | **12.8250** | <ins>33.8917</ins> | <ins>45.5667</ins> |
| LanguageBind | zero-shot | 0 | 4.9417 | 19.8583 | 29.5333 |
| LanguageBind | 直接同索引真实媒体 | 70 | **6.2750** | **23.3917** | **34.8250** |
| LanguageBind | 重建初始化媒体 | 55 | <ins>5.8667</ins> | <ins>21.7583</ins> | <ins>32.6750</ins> |
| OmniBind dense heads | zero-shot | 0 | 12.6250 | 34.9250 | 48.2500 |
| OmniBind dense heads | 直接同索引真实媒体 | 90 | **13.2500** | <ins>36.3583</ins> | **49.4917** |
| OmniBind dense heads | 重建初始化媒体 | 100 | <ins>13.0917</ins> | **36.3667** | <ins>49.3083</ins> |

这批均为seed1；OmniBind直接真实媒体的cache-only repeat逐方向和所选epoch一致，但不是独立seed。推定初始化来自`RandomState(1).permutation(10000)[:200]`，没有找回原历史checkpoint来证明逐样本身份。直接真实媒体保留的信息多于重建媒体，不能用其分数作为重建匹配Random。OmniBind本表是7.08M dense heads，不能混入后来的官方router-only统计。

| 模态 | 重建前后平均余弦 | 平均绝对误差 |
| --- | --- | --- |
| 视频 | 0.999993 | 0.002578 |
| 音频 | 0.801176 | 0.249152 |

在200条初始化样本上，文本nearest-caption恢复为对应类别名200/200，视频无损封装往返的uint8误差为0；音频用固定mel伪逆与32次确定性Griffin–Lim恢复，缺少相位，因此有损。视频/音频的上述余弦与误差是输入重建审计，不能当作独立检索seed统计。

### OmniBind视频取帧协议恢复

| Large视频策略 | R@1 | R@5 | R@10 | 对论文三指标最大误差pp |
| --- | --- | --- | --- | --- |
| 首帧 | 11.2083 | 32.4083 | 45.2500 | 2.7800 |
| 四分之一帧 | 11.4667 | 33.0750 | 46.1167 | 1.9133 |
| 中间帧 | 11.5917 | 33.6667 | 46.6083 | 1.4217 |
| 四分之三帧 | 11.1917 | 32.8250 | 45.4167 | 2.6133 |
| 末帧 | 10.8333 | 32.0750 | 44.6333 | 3.3967 |
| 首中末三帧均值 | <ins>12.2833</ins> | 34.3083 | <ins>47.7000</ins> | <ins>0.6367</ins> |
| 四分之一中间四分之三均值 | 12.2667 | <ins>34.7250</ins> | <ins>47.7000</ins> | 0.6533 |
| 均匀五帧均值 | **12.6250** | **34.9250** | **48.2500** | **0.2950** |

五帧位置为0、0.25、0.5、0.75、1，各帧先独立经过expert/router，再平均并L2归一化。其最大误差约0.295pp，通过历史0.35pp恢复门槛；选择参考了论文数字，属于target-informed protocol recovery。不能将接近论文值当作独立确认历史实现。

历史三帧候选存在摘要与机器结果不一致：上表采用现存`video_protocol_recovery.json`，首中末三帧为12.2833/34.3083/47.7000，与旧综合报告一致；另一份`CROSS_ARCH_SAME_INIT.md`曾摘录为12.37/34.33/47.71。两份来源均保留，本次没有重跑来解释差异；五帧结果12.6250/34.9250/48.2500及恢复门槛结论一致。

| 单seed诊断 | R@1 | R@5 | R@10 | 解释 |
| --- | --- | --- | --- | --- |
| OmniBind Base中间帧 zero-shot | 11.9667 | 33.4833 | 46.6583 | 不同模型；未复现Large论文协议 |
| released-code UniBind zero-shot | 12.6250 | 33.2750 | 44.6500 | UniBind不是官方OmniBind |
| OmniBind Large中间帧 Random | 12.2500 | 34.8333 | 47.9167 | epoch75；保留未通过zero-shot恢复门槛的诊断 |
| released-code UniBind Random | 13.1750 | 34.2083 | 45.7333 | epoch60；实现诊断，不填OmniBind行 |
| LanguageBind old-style初始化输入 | 5.7167 | 22.2917 | 32.8000 | epoch65；mode字段虽写distilled_data，实际输入为初始化诊断 |

本表不同模型/协议回答不同问题，不跨行排名。历史released evaluator加载PointBind/UniBind，不能据此认定论文OmniBind行一定误标；官方旧evaluator缺失，结论限于当前可核查代码。

### OmniBind投影参数消融与官方router

11种post-router配置共享重建Random、官方OmniBind Large缓存、seed1、SGD和100轮预算，仅改变可训练参数化，全部使用同一CPU runner。以下仅在这11项内排名；不把另一CUDA dense结果或论文历史Distilled混入排序。

| 可训练参数化 | 参数量 | epoch | R@1 | R@5 | R@10 |
| --- | --- | --- | --- | --- | --- |
| Dense V T A | 7077888 | 85 | <ins>13.1333</ins> | **36.2167** | **49.4833** |
| Dense V T | 4718592 | 100 | **13.1667** | <ins>35.9417</ins> | <ins>49.2083</ins> |
| Dense V A | 4718592 | 95 | 13.0583 | 35.6917 | 48.9417 |
| Dense T A | 4718592 | 95 | 13.1083 | 35.6250 | 49.0333 |
| Dense V | 2359296 | 95 | 13.0167 | 35.6333 | 48.6250 |
| Dense T | 2359296 | 90 | 13.0833 | 35.4667 | 48.7167 |
| Dense A | 2359296 | 20 | 12.8833 | 35.2667 | 48.1333 |
| Residual low-rank341 | 3142656 | 70 | 13.0500 | 35.6083 | 48.8250 |
| Residual low-rank316 | 2912256 | 75 | 12.8583 | 35.6083 | 48.7917 |
| Residual low-rank192 | 1769472 | 45 | 13.0333 | 35.4833 | 48.4833 |
| Diagonal V T A | 4608 | 25 | 12.7917 | 35.2083 | 48.2417 |

| 官方router单seed阶段 | R@1 | R@5 | R@10 |
| --- | --- | --- | --- |
| zero-shot | <ins>12.7167</ins> | **35.0333** | <ins>48.2000</ins> |
| router-only epoch10 | **12.7500** | <ins>34.9333</ins> | **48.2750** |

官方V/T/A router共2,914,347参数；expert encoder/projector及point router冻结。rank341只是接近released UniBind投影参数预算的控制，rank316接近官方router参数预算，两者都不实现输入相关路由。容量改变会影响Random分数，但不能因某设置更接近论文而认定找回历史协议。官方router单seed结果也不能与后来的三源seed均值混用。

## 样本方差汇总

下表为前述多seed主读出的样本方差，单位pp²，使用未舍入的原始结果计算。方差描述波动，不按“性能最优”排名。1e-5全量、历史协议恢复、容量消融、直接插值等单seed实验没有可估计的跨seed方差。

| 实验与统计口径 | 数据 | Var R@1 | Var R@5 | Var R@10 |
| --- | --- | --- | --- | --- |
| ImageBind head100 3源seed | random | 0.003981 | 0.048819 | 0.128611 |
| ImageBind head100 3源seed | distilled | 0.005995 | 0.064329 | 0.009884 |
| LanguageBind head100 3源seed | random | 0.021690 | 0.084884 | 0.146319 |
| LanguageBind head100 3源seed | distilled | 0.011736 | 0.160301 | 0.185023 |
| OmniBind router100 3源seed | random | 0.000162 | 0.001412 | 0.090000 |
| OmniBind router100 3源seed | distilled | 0.010208 | 0.001412 | 0.011481 |
| LanguageBind 仅head20 3源seed | random | 0.009745 | 0.095648 | 0.157662 |
| LanguageBind 仅head20 3源seed | distilled | 0.006736 | 0.057384 | 0.237801 |
| LanguageBind 全量3e-6 20轮 3源seed | random | 0.038819 | 0.093495 | 0.149745 |
| LanguageBind 全量3e-6 20轮 3源seed | distilled | 0.002569 | 0.018356 | 0.095278 |
| 旧原生 3源seed | random | 0.012523 | 0.057940 | 0.158356 |
| 旧原生 3源seed | distilled | 0.009236 | 0.050023 | 0.051458 |
| 温度修正原生 3源seed | random | 0.030486 | 0.115069 | 0.022245 |
| 温度修正原生 3源seed | distilled | 0.058426 | 0.002106 | 0.031690 |
| ImageBind 固定Random 5学生seed 测试选epoch | random | 0.006979 | 0.010396 | 0.006007 |
| ImageBind 固定Random 5学生seed 固定100轮 | random | 0.004701 | 0.011701 | 0.007674 |
| LanguageBind 固定Random 5学生seed 测试选epoch | random | 0.007312 | 0.033729 | 0.020507 |
| LanguageBind 固定Random 5学生seed 固定100轮 | random | 0.005833 | 0.020951 | 0.025049 |
| OmniBind 固定Random 5学生seed 测试选epoch | random | 0.017167 | 0.047799 | 0.006896 |
| OmniBind 固定Random 5学生seed 固定100轮 | random | 0.020229 | 0.067201 | 0.021757 |

## 目前结论与待补项目

1. **已经完成：** 三架构15项固定Random学生重复、3个源蒸馏seed、18项配对迁移、LanguageBind两项直接插值、8项唯一全量微调及6项head20、原生旧版与修正版各15节点，以及历史输入协议/参数容量诊断。
2. **没有显示稳定收益：** 当前LanguageBind head迁移和全量微调；ImageBind修正后原生R@1；OmniBind虽平均略高，仍只具三个源seed的有限证据。不能以历史论文单值或选出的某个好seed替代当前配对均值。
3. **新数据选择尚未传播：** 若更新为温度修正后的统一Table 3，seed1需要用step100重新导出并评测三架构Distilled；LanguageBind的20轮head/full对照也需明确是否沿用旧step150或切换新数据。Random以及seed2/3在输入身份、目标训练协议一致时可核验复用。当前尚未执行这些下游更新。
4. **未覆盖的设置：** OmniBind全量微调、LanguageBind 1e-5多源seed、以LanguageBind或OmniBind为源backbone重新蒸馏；它们不能由已有目标迁移结果代替。
5. **剩余解释限制：** 历史产物缺失、音频重建有损、源/学生两级test选择、三个源seed固定一个学生seed，以及200外层更新不等于收敛证明。温度修正排除了一个确定实现差异，没有证明它是性能差距的全部原因。

## 证据来源与可复核范围

报告以机器结果与已保存源码/协议为依据。以下为主要汇总和历史原文；原始数据、checkpoint、日志、图件保留在项目或授权NFS中，不复制进实验记录仓库。路径以工作区为基准，NFS路径另行写明。

- **三源seed迁移**：`HoPA-Rebuttal/cross_arch/artifacts/paired_source_seed_summary.json`；SHA-256：`ba4aeaaab008a341efcc7615afd12a56f1addad1b482321ba923c4622547bf07`。

- **五学生seed**：`HoPA-Rebuttal/cross_arch/artifacts/student_seed_summary.json`；SHA-256：`8e42979620ab0d102d2f569db8137503e80c6b52474f54e2d47bb2bcc16e4bcd`。

- **LanguageBind学习率探索**：`HoPA-Rebuttal/cross_arch/full_finetune/20261110T1525-languagebind-seed1/summary.json`；SHA-256：`434af5e3dffe388385626a3698907fb3be228c37ea2de498b2c70b71aa9a0fe1`。

- **LanguageBind三源复核**：`HoPA-Rebuttal/cross_arch/full_finetune/20261110T2053-languagebind-three-seed-lr3e6/summary.json`；SHA-256：`e7ee33aa455b2afe813de25c43b64bdf07599fcdcb71ad6eda7a72e4449e7c2b`。

- **输入插值**：`HoPA-Rebuttal/cross_arch/adapter_trials/20261109T2202-languagebind-direct-seed1/comparison.json`；SHA-256：`403e07c4c328661f87a31e45d585dddd9a007234b6692c1b795693dae89945de`。

- **旧原生15节点**：`HoPA-Rebuttal/cross_arch/runs/native-checkpoint-eval-v1/summary.json`；SHA-256：`c8cbb671e769e824078a035bcc11febf885613a2975f7e50e47f3a498edc55ab`。

- **修正原生15节点**：`HoPA-Rebuttal/cross_arch/runs/20261113T173102-server-a-native-wbce-temperature-v2/summary.json`；SHA-256：`fa6b1142f19f1148955ff31befae4bc9da63e91180435fa45cb68868cb647f9c`。

- **投稿PDF**：`HoPA-Rebuttal/263_Omnimodal_Dataset_Distilla.pdf`；SHA-256：`7f81692e86ade2e293792c083ff604c692034318a76fae3c5db95e3122e37744`。

- **历史综合报告**：`HoPA-666f966/CROSS_ARCH_EXPERIMENTS_SUMMARY.md`；SHA-256：`eddf630fed800b6d941ab4b79b52e38227ca76713c52c401e790ee5fb6501922`。

- **历史初始化与视频恢复**：`HoPA-666f966/CROSS_ARCH_SAME_INIT.md`；SHA-256：`1d8e828037186fed57e3ffa927128699fe5dc44b41deb9dc8dc011d8f9b0148a`。

- **历史重建审计**：`HoPA-666f966/RECONSTRUCTED_RAW_CROSS_ARCH.md`；SHA-256：`f5865ed8d869e392067664ec177a98881a77686ba9dd6ae694716ce4523405a4`。

- **历史OmniBind容量审计**：`HoPA-666f966/OMNIBIND_PARAMETER_ABLATION.md`；SHA-256：`6206814877bba695a53cd230717cb46a125da39db3f95b6a8f2ea20a7964bb89`。

- **实际接口与身份审计**：`HoPA-Rebuttal/cross_arch/docs/PROTOCOL_AUDIT.md`；SHA-256：`acb7bd6ddc187cc2cda13fcc590fdfd782d88a29326bb42c476c9b69705c3ac1`。

历史NFS证据目录：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/cross_arch_same_init/`与`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/cross_arch_reconstructed_raw/`；其中包含视频恢复候选、重建保真度、11项参数消融及router结果。原始证据只读使用，本次整理没有新增训练、复评或外部上传。

前版整理来源清单（44个文件及各自SHA-256；新增实验来源见对应小节）保存于本地`HypOmni-Exps/runs/table3-consolidation-20261113T194008/source_manifest.json`，清单SHA-256：`fff7ddeaa513198cffe73540cea62de8db927454264499a659ca8660a65f39ad`。正文是综合报告，不冒充任一原始报告的逐字副本。远端状态未核实，本次未commit或push。
