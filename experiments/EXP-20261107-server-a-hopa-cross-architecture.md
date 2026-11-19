# HoPA Table 3：跨架构转移协议与随机性

<!-- Q3-SOURCE5-STUDENT5-START -->
Table3五源×五学生扩充stopped，核对2026-11-15T14:34:38.430889+08:00：60/100条，新增24/64条，复用36条。 当前平衡子集为3源×5学生；LanguageBind/OmniBind的D−R R@1分别+0.0422±0.1445/-0.0061±0.1844pp。 按用户要求停止，保留已有结果；五源完整结果未完成。

| 模型 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| languagebind | random | <ins>5.4883 ± 0.0551</ins> | **21.5611 ± 0.3060** | **32.5367 ± 0.5120** |
| languagebind | distilled | **5.5306 ± 0.0952** | <ins>21.3694 ± 0.1082</ins> | <ins>32.1906 ± 0.2792</ins> |
| omnibind | random | **12.8972 ± 0.0432** | **35.3617 ± 0.0418** | **48.6011 ± 0.1214** |
| omnibind | distilled | <ins>12.8911 ± 0.1741</ins> | <ins>35.3156 ± 0.0270</ins> | <ins>48.5572 ± 0.0766</ins> |

固定20轮；每源先平均5个学生，再统计源间样本SD；新增独立源seed4/5各200步。Random与Distilled使用同样重建流程，主结果包含全部学生重复。源数据仍按历史v1的ImageBind候选曲线选择，与此前迁移数据一致；包含源test选择，不冒充温度修正版或独立留出测试。

本地明细：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/student_repeats/20261115T040224-server-a-source5-student5/REPORT.md`、`summary.json`；summary SHA-256：`74c261fc8956bd296b748b49f7026bbc19186040213efce33852ae603cb5cbd0`。此前3×3结果保留为历史版本。
<!-- Q3-SOURCE5-STUDENT5-END -->

<!-- Q3-LB-OMNI-STUDENT3-START -->
LanguageBind head与OmniBind dense的三源×三学生seed评测完成，核对2026-11-14T03:43:22.279439+08:00。固定20轮配对D−R R@1：LanguageBind +0.0602±0.1287pp，OmniBind +0.0241±0.2294pp。

| 模型 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| languagebind | random | <ins>5.4602 ± 0.0806</ins> | **21.5667 ± 0.3170** | **32.5148 ± 0.5961** |
| languagebind | distilled | **5.5204 ± 0.0902** | <ins>21.3352 ± 0.2165</ins> | <ins>32.2046 ± 0.2657</ins> |
| omnibind | random | <ins>12.9000 ± 0.0626</ins> | **35.3796 ± 0.0449** | **48.6083 ± 0.1405** |
| omnibind | distilled | **12.9241 ± 0.2042** | <ins>35.2981 ± 0.0385</ins> | <ins>48.5556 ± 0.0846</ins> |

每个模型3个源seed，各自Random/Distilled分别运行学生seed1/2/3；每项固定20轮、80次更新。先在每个源seed内平均3次学生结果，再统计3个源均值的均值±样本SD；每源学生SD、实际方差及九次运行的描述性SD另列。九次运行不是九个独立源蒸馏seed。输入、预训练或identity初始化固定，每个学生重新初始化，seed改变训练shuffle。源数据沿用step150/200/200，源选择仍含历史test信息；ImageBind未在本次追加学生seed。

本地完整结果：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/student_repeats/20261114T031921-server-a-lb-omni-student3/REPORT.md`、`summary.json`；各源学生结果、复用清单和两项seed1一致性重放在同目录。 summary.json SHA-256：`d37b72a83c6f8065d960ca8c7c701de78123c6edf3040f854bca8f53d5e37dfa`。
<!-- Q3-LB-OMNI-STUDENT3-END -->

<!-- Q3-OMNI-DENSE20-START -->
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
<!-- Q3-OMNI-DENSE20-END -->

[Table 3全部实验总报告](../summaries/EXP-20261107-server-a-hopa-cross-architecture/TABLE3_COMPLETE_REPORT.md)统一汇总历史协议恢复、三架构多seed、LanguageBind head与全量微调、两个LR、输入适配、OmniBind容量消融，以及11-13原生温度修正；含均值、标准差、方差、版本边界和原始证据。整理核对：2026-11-13。

<!-- Q3-WBCE-TEMPERATURE-V2-START -->
原生WBCE温度修正复评已完成15/15，核对2026-11-13T18:10:05.219778+08:00。三源seed、各自重新选定checkpoint后，Random/Distilled测试六方向R@1为12.7083%/12.6472%；配对D−R为-0.0611±0.3369pp。

| 数据 | R@1 | R@5 | R@10 |
|---|---:|---:|---:|
| random | **12.7083 ± 0.1746** | **33.9333 ± 0.3392** | <ins>45.4389 ± 0.1491</ins> |
| distilled | <ins>12.6472 ± 0.2417</ins> | <ins>33.9194 ± 0.0459</ins> | **45.5611 ± 0.1780** |

选中checkpoint发生变化的源seed：1。目标架构与LanguageBind全量微调结果仍是旧数据选择版本，未在本轮自动重跑。

本轮把WBCE输入从proxy Gram改为proxy Gram/0.2，并显式传入tau1=.1、tau2=.2，与既有源蒸馏内层一致。复用源seed1/2/3的0/50/100/150/200节点及全部优化V/T/A、S和三条LR；源蒸馏未重跑。学生固定seed1、100轮、每5轮按test R@1+R@5选同一epoch；外层从50/100/150/200选优，保留测试选模限制。旧版18项data-only迁移与原生曲线完整保留；这次原生结果不直接替代data-only表格。

本地当前修正版本：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/cross_arch/runs/20261113T173102-server-a-native-wbce-temperature-v2`，完整报告`REPORT.md`、逐节点与方差`summary.json`、迁移影响`transfer_followup.json`。
<!-- Q3-WBCE-TEMPERATURE-V2-END -->

[返回实验总览](../README.md) · EXP-20261107-server-a-hopa-cross-architecture · 结果核对：2026-11-07 21:43:09 Asia/Shanghai；文档更新：2026-11-09

已确认最终投稿 Table 3 混合了历史 Distilled 数字和本机补充的 reconstructed-initialization Random 对照。原 Distilled checkpoint 及官方 OmniBind 历史 evaluator 未找回，**尚不能补齐同协议 Distilled 多 seed 方差**。现有 LanguageBind 对照完成 5 个学生 seed：主报告按用户要求采用测试最佳epoch，R@1 **5.7467±0.0855pp**；原固定第100轮 **5.4750±0.0764pp** 保留作审计，两种规则不混合。原表 Distilled−Random 的 0.06pp 差值没有由本轮证明显著。

<!-- Q3-SEED1-RECOVERY-START -->
当前统一重建结果核对：2026-11-10 14:40 +0800。三个独立源seed的18/18项Random/Distilled配对评测已完成；每源固定目标学生seed1。下表为测试六方向Recall均值±源seed间样本SD（ddof=1，单位百分点）。每次训练的三个指标取同一按R@1+R@5选中的epoch，源数据和学生epoch均使用test信息，不能称独立留出测试。

| 架构 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| imagebind | random | **12.7222 ± 0.0631** | **33.7333 ± 0.2210** | <ins>45.3000 ± 0.3586</ins> |
| imagebind | distilled | <ins>12.6972 ± 0.0774</ins> | <ins>33.5889 ± 0.2536</ins> | **45.3722 ± 0.0994** |
| languagebind | random | <ins>5.5944 ± 0.1473</ins> | **22.1472 ± 0.2913** | **33.0333 ± 0.3825** |
| languagebind | distilled | **5.6917 ± 0.1083** | <ins>21.4806 ± 0.4004</ins> | <ins>32.4722 ± 0.4301</ins> |
| omnibind | random | <ins>12.6556 ± 0.0127</ins> | <ins>34.9472 ± 0.0376</ins> | <ins>48.0583 ± 0.3000</ins> |
| omnibind | distilled | **12.7333 ± 0.1010** | **35.0028 ± 0.0376** | **48.0861 ± 0.1072** |

标记只在同架构两条件内比较，不代表统计显著性。成对Distilled−Random的R@1均值±样本SD：imagebind -0.0250±0.1377pp；languagebind +0.0972±0.2496pp；omnibind +0.0778±0.0891pp。

三源seed均完成200个源更新后，各自在50/100/150/200中按原生ImageBind曲线锁定数据；不依据目标架构结果重新选数据。原固定数据15次学生seed重复及输入插值两项小试单独保留，不混入本表。

完整结果：本地`HoPA-Rebuttal/cross_arch/docs/PAIRED_SOURCE_RESULTS.md`与`artifacts/paired_source_seed_summary.json`；GPU2续评记录：本地`runs/EXP-20261107-server-a-hopa-cross-architecture/20261110T1355-server-a-seed3-gpu2.md`。
<!-- Q3-SEED1-RECOVERY-END -->

## 研究问题与关键设置

| 影响结果解读的设置 | 本轮口径 |
|---|---|
| 数据与划分 | VGGSound-S 10,000 train / 2,000 test；按有效CSV前缀；测试含307个不同类别名，重复文本保留为独立行 |
| 正例与指标 | 仅同实例行为正例；六方向 R@1/5/10 算术平均；百分比 |
| Random 数据 | 固定 seed1 初始化的200条重建媒体；同一 manifest、文件hash和样本顺序 |
| 目标训练 | ImageBind native heads+postprocess；LanguageBind native projections；OmniBind Large V/T/A routers |
| 预算与随机性 | 各架构5个学生seed（1–5）、100epochs、batch64；固定数据和预训练初始化，改变batch顺序 |
| 选模 | 11-08用户指定主报test-selected best：每5轮按六方向Avg R@1+Avg R@5选择，同一epoch报告R@1/5/10；epoch0另列，固定末轮作审计 |
| 不确定性 | 先每seed平均六方向，再统计seed间样本SD/方差，ddof=1；不是独立蒸馏seed的SD |

## 主要结果

三架构的5个学生seed均已完成，主报最佳epoch的mean±sample SD：ImageBind **12.8083±0.0835 / 34.0600±0.1020 / 45.6000±0.0775**，LanguageBind **5.7467±0.0855 / 21.7567±0.1837 / 32.6967±0.1432**，OmniBind **12.7767±0.1310 / 34.9633±0.2186 / 48.1800±0.0830**。每个run的三指标来自同一所选epoch，统计的是固定数据上的学生训练波动，不是三源蒸馏seed方差。

原固定末轮数据保留：ImageBind 12.7483/34.0583/45.6333、LanguageBind 5.4750/21.1850/32.3733、OmniBind 12.4533/34.6267/47.8050；完整SD在本地报告。OmniBind末轮低于zero-shot12.7417/35.0583/48.2167的负结果没有删除。选择规则是在部分诊断结果出现后按用户指示调整，主报告明确为test-selected best，不能称为独立留出测试。

## 解释与局限

- 跨架构专用源实现优化视频预处理帧、音频fbank和文本trunk hidden states，不是把ImageBind最终embedding直接连接到不同目标head。
- LanguageBind旧入口做视频/音频输入布局转换；文本使用初始化样本原caption，没有直接转移优化后的text hidden states。其原生projection有2,162,688参数，并非注释所说的identity MLP。
- 后补Random使用共同媒体导出，音频为mel伪逆加Griffin–Lim近似；不能证明与历史Distilled导出完全同口径。
- OmniBind Random对应2,914,347参数的router-only；7,077,888参数dense heads为另一个敏感性实验。五帧协议曾参考论文zero-shot恢复，不能称为独立历史复现。
- ImageBind评测实际tau1/tau2=0.1/0.1（CLI值未传入）；LanguageBind/OmniBind为0.1/0.2。旧评测以测试集选轮次；不能称为validation selection。
- 历史Distilled缺失，不使用Random的SD给旧Distilled单值填“±”，也不把目标学生seed当作独立蒸馏seed。

## 下一步判断

已有20条VGGSound-S专家轨迹与native head参数形状匹配。新的独立源蒸馏计划为Q200、seeds1/2/3、16内层步；源脚本上限2,000更新、历史评测路径指向第200步，新方案固定200更新、三源seed，后续18次配对学生评测；完整Q200单步预检通过（457.07秒，peak allocated14.903GiB，三模态及相似度均有有限非零更新）。预检不是正式结果。用户已明确批准固定200更新、三源seed；2026-11-08进一步确认将后续配对学生训练从90次缩至18次，每项固定学生seed1；该新版于2026-11-07 21:41 Asia/Shanghai开始运行；11-08按用户指示将seed3提前到GPU4，与GPU5/6上的seed1/2并行，科学协议及18次评测预算不变。历史审批暂停及解除情况留在运行记录。三个目标原生编码入口各四样本验证也已通过；当前三个独立源seed的18项配对结果已齐全，均值、样本SD和配对差值见上方当前结果。根据用户最新要求，每源seed完成200更新后，在50/100/150/200完整原生ImageBind曲线中按最佳score选定一份数据；Random为该seed相同初始化的第0步。三个目标共用这一选择，不依据LanguageBind/OmniBind结果重新挑数据。完整替换表使用同一导出与训练口径配对Random/Distilled，按固定学生seed1统计三个独立源seed的均值、样本SD和成对差值；不再估计每份数据内的学生训练方差。本次收缩发生在新配对评测开始前，原15次Random学生重复结果保留。

## 保存节点的原生诊断

2026-11-08用户新增授权在源蒸馏继续运行时，共卡评测0/50/100/150/200节点，每个节点仅固定学生seed1，最多15次原生ImageBind诊断。读取所有优化的三模态张量、软相似度S和三条学习率，只训练原生head/postprocess；不改写原学生loss、采样器或优化器更新。每5轮评测并选最佳score，与18次data-only跨架构评测分开，源优化预算仍200更新，但这些原生曲线现在用于按统一规则选择迁移数据。原生诊断已改为完整周期最佳epoch口径：seed1初始化checkpoint有完整曲线，最佳epoch20为12.9333/33.7333/45.5917，相对第100轮12.2250/33.1250/44.7417存在后期退化。另8份只有0/100读出的旧结果保留并重新评测学生，不冒充最优；源蒸馏不重启。完整新结果尚未齐全，不据此声称所有蒸馏集必然过拟合。明细和曲线在本地`HoPA-Rebuttal/cross_arch/runs/native-checkpoint-eval-v1/RESULTS.md`。共卡时间不作为效率证据。

## 完整结果与来源

本地：`HoPA-Rebuttal/cross_arch/docs/PROTOCOL_AUDIT.md`（逐架构代码证据及英文草稿）、`docs/STUDENT_SEED_RESULTS.md`（完整均值/SD/方差/逐seed表）、`artifacts/student_seed_summary.json`（机器汇总）、`source_manifest.json`（原代码哈希）、`configs/raw_rebuild.json`、`artifacts/*.json`（数据身份、模型参数与buffer兼容性）。

权威对照路径：ImageBind `runs/student-seeds-v2/imagebind/`；LanguageBind `runs/student-seeds-v1/languagebind/`；OmniBind `runs/student-seeds-v2/omnibind/`，均相对于上述本地目录。v1 ImageBind/OmniBind保留作数值对齐诊断。详细命令/PID/GPU及失败重试只记本地 `runs/EXP-20261107-server-a-hopa-cross-architecture/`。

## 当前目标架构安排

LanguageBind与OmniBind各评选中的最佳数据及对应初始化Random，三源seed各一次，共12项；另保留相同重建流程的ImageBind6项，全部仍18项。目标encoder冻结，只训练原生projection/router，学生epoch仍按test最佳；原生源端选优用了S/LR，目标保持data-only，二者不混作同口径分数。每源四候选齐全后写入锁定清单再进入任何目标编码。截至11-08 23:39，source1已锁定第150步（源学生最佳epoch20、score46.7583），source2已锁定第200步（源学生最佳epoch15、score46.375），两者进入共享媒体重建/目标评测流水线；source3尚缺优化候选，目标架构结果仍未齐全。选择规则是在部分源曲线观察后更新，应明确test-informed source selection及test-selected target epoch。

<!-- Q3-DIRECT-ADAPTER-START -->
## 输入插值适配小试：LanguageBind

核对：2026-11-09 22:19 +0800。复用seed1的Q200与锁定step150，不重新蒸馏；视频/fbank直接插值到LanguageBind输入尺寸，绕过媒体导出和音频相位重建，目标内部patch embedding与Transformer保留。文本特征、测试特征、初始化、loss和学生训练预算保持原对照。

两项100轮评测计算共3.19分钟。Distilled的R@1/R@5/R@10从5.6917/21.8417/32.5750变为5.6500/22.0500/32.7000；新Random为5.6583/22.0250/32.7000，因而新Distilled−Random仅−0.0083/+0.0250/0.0000pp。R@5/R@10较旧Distilled回升，但与新Random几乎持平，当前不支持以这次单seed小试替换主适配协议。

| 条件 | 输入适配 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| Random | 媒体重建 | **5.6667** | <ins>21.9667</ins> | **32.8083** |
| Random | 直接插值 | <ins>5.6583</ins> | **22.0250** | <ins>32.7000</ins> |
| Distilled | 媒体重建 | **5.6917** | <ins>21.8417</ins> | <ins>32.5750</ins> |
| Distilled | 直接插值 | <ins>5.6500</ins> | **22.0500** | **32.7000** |

仅在同一条件的两种适配之间标记最优/次优。均为测试六方向均值（%），按R@1+R@5选同一最佳epoch，非独立validation。音频时轴拉伸和视频随机翻转旁路也是变化，不能把效果单独归因于避免Griffin–Lim。单源seed、固定学生seed1；本次两项不混入18项主评测。OmniBind异构音频专家尚未实施此直接插值试验。

本地完整报告与校验：`HoPA-Rebuttal/cross_arch/adapter_trials/20261109T2202-languagebind-direct-seed1/REPORT.md`、`comparison.json`、`verification.json`；运行与源码清单位于本地`runs/EXP-20261107-server-a-hopa-cross-architecture/20261109T2202-server-b-languagebind-direct-seed1.md`。
<!-- Q3-DIRECT-ADAPTER-END -->

<!-- Q3-LB-FULLFT-START -->
## LanguageBind全量微调20轮小试

核对：2026-11-10 18:24 +0800。固定源seed1、学生seed1，Q200的重建Random与源step150 Distilled。V/T/A编码器和projector共839,301,376参数全部更新，有效batch64；SGD momentum=.9、weight decay=.0005，head LR=.01。预设backbone LR=1e-5，满足既定效果不足/退化条件才追加3e-6；不扩展其他seed。

为使可训练范围比较公平，重跑相同固定预处理输入/测试视图下的20轮head-only对照。所有更新后的测试编码器输出重新计算；仅输入张量可缓存。与旧100轮Table3是不同预算和预处理随机性固定口径，不直接拼表。

| 条件 | 训练范围/LR | R@1 | R@5 | R@10 | 最佳epoch |
|---|---|---:|---:|---:|---:|
| random | matched_head20 | <ins>5.5833</ins> | 21.0833 | **31.9500** | 15 |
| random | bb1e-5 | **5.6000** | <ins>21.1000</ins> | 31.5083 | 5 |
| random | bb3e-6 | 5.4250 | **21.2000** | <ins>31.8917</ins> | 15 |
| distilled | matched_head20 | **5.7333** | <ins>21.3083</ins> | <ins>31.8667</ins> | 5 |
| distilled | bb1e-5 | 5.4583 | **21.4667** | **31.9500** | 5 |
| distilled | bb3e-6 | <ins>5.6417</ins> | 21.2000 | 31.8583 | 5 |

仅在同条件不同训练设置之间标记最优/次优。读出为test六方向均值（%），在5/10/15/20轮按R@1+R@5选同一轮。固定末轮与所有负结果另存；学习率触发也使用test，因此是探索性单seed结果，不能称无偏验证或跨seed稳定提升。

配对Distilled−Random的R@1均值：matched_head20 +0.1500pp；bb1e-5 -0.1417pp；bb3e-6 +0.2167pp。

完整报告与参数/梯度/显存/输入身份：本地`HoPA-Rebuttal/cross_arch/full_finetune/20261110T1525-languagebind-seed1/REPORT.md`、`summary.json`、`preflight.json`、`protocol.json`。运行记录：本地`runs/EXP-20261107-server-a-hopa-cross-architecture/20261110T1525-server-a-languagebind-fullft.md`。
<!-- Q3-LB-FULLFT-END -->

<!-- Q3-LB-FULLFT-THREE-SEED-START -->
## 固定3e-6的三源seed全量微调复核

核对：2026-11-11 00:18 +0800。三源seed的配对结果已齐：full3e-6的Distilled−Random R@1为+0.0750±0.2241pp，匹配head-only为+0.0056±0.1655pp。Full的Distilled绝对R@1相对head变化为-0.0583±0.0333pp；同时报告绝对值与配对差值，避免把Random下降误解为Distilled提升。

固定学生seed1、20epochs、有效batch64、微批4，SGD momentum=.9、weight decay=.0005、head LR=.01、backbone LR=3e-6。source1复用先前结果；source2/3为新增复核，输入、模型初始化与选模口径相同。新增运行启用通过全部参数梯度一致性检查的原生梯度检查点，属于显存优化，不改变训练预算或损失。

| 训练范围 | 数据 | R@1 | R@5 | R@10 |
|---|---|---:|---:|---:|
| head | random | <ins>5.6361 ± 0.0987</ins> | **21.4056 ± 0.3093** | **32.4028 ± 0.3971** |
| head | distilled | **5.6417 ± 0.0821** | <ins>21.3889 ± 0.2396</ins> | <ins>31.8528 ± 0.4876</ins> |
| full3e-6 | random | <ins>5.5083 ± 0.1970</ins> | **21.5528 ± 0.3058** | **32.2444 ± 0.3870** |
| full3e-6 | distilled | **5.5833 ± 0.0507** | <ins>21.3472 ± 0.1355</ins> | <ins>31.9750 ± 0.3087</ins> |

表为三源seed均值±样本SD（ddof=1）；只在同训练范围内比较Random与Distilled。LR曾使用source1结果选择，故另报source2/3：full3e-6的配对R@1为+0.0042±0.2652pp。它们没有参与LR选择，但共用test与测试选模，不能称独立留出测试。

完整逐seed、固定末轮、R@5/R@10及绝对成绩变化见本地`HoPA-Rebuttal/cross_arch/full_finetune/20261110T2053-languagebind-three-seed-lr3e6/REPORT.md`和`summary.json`。本次只新增4个全量运行及4个匹配head对照，不增加LR搜索。模型与新缓存位于授权NFS，控制与日志留工作区。共卡耗时不作独占效率结论。
<!-- Q3-LB-FULLFT-THREE-SEED-END -->

<!-- Q3-LB-POSITIVE-START -->
## LanguageBind冻结编码器、head初始化对照

Table3 LanguageBind初始化小试完成。固定3000更新：pretrained D−R R@1 +0.050±0.102pp；neutral D−R R@1 -0.156±0.285pp；positive_free D−R R@1 -0.164±0.121pp。

| 初始化 | Random R@1 | Distilled R@1 | D−R (pp) | Full R@1 |
|---|---:|---:|---:|---:|
| pretrained | **5.022 ± 0.121** | **5.072 ± 0.054** | **0.050 ± 0.102** | **8.311 ± 0.065** |
| neutral | 0.631 ± 0.161 | 0.475 ± 0.126 | <ins>-0.156 ± 0.285</ins> | 2.083 ± 0.147 |
| positive_free | <ins>1.742 ± 0.022</ins> | <ins>1.578 ± 0.128</ins> | -0.164 ± 0.121 | <ins>7.750 ± 0.042</ins> |

VGGSound-S源seed1/旧step150，Random与Distilled各200条、Full10000条、评测2000条；三种初始化×三个head，共27项。±为head样本SD，非源seed波动。固定3000主报，固定80（压缩组旧20轮）另报；没有目标test选模，但源数据保留历史test-informed选择，结果属探索性。Full是真实原始媒体参照，与压缩组重建媒体保真度不同。

核对：2026-11-15T03:26:25+08:00。完整报告`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/table3_languagebind_positive/20261115-source1-step150/a100_results/REPORT.md`、`summary.json`；远端模型与原始输出`/home/xiaobo.xia/YuxuanGao/Table3-LanguageBind-Positive-20261115/results`。原Table3及其他实验不覆盖。
<!-- Q3-LB-POSITIVE-END -->
