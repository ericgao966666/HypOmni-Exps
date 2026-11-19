# 正初始化和严格配对起点下的HoPA蒸馏收益

[返回实验总览](../README.md) · EXP-20261111-server-a-hopa-positive-distill · 本地结果核对与文档更新：2026-11-12，Asia/Shanghai

<!-- HOPA-POSITIVE-DISTILL-START -->
正初始化蒸馏小试：`complete`，核对2026-11-11T16:00:43+08:00。 验证R@1固定LR：HoPA 4.076%，联合LoRS 3.688%，Random-HoPA 2.306%；一个蒸馏seed、三个配对新head，尚无test。

本地运行：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_distill/20261111T145619-server-a-positive-distill-v1`；控制与日志：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/positive_init_distill/runs/20261111T145619-server-a-positive-distill-v1`。
<!-- HOPA-POSITIVE-DISTILL-END -->

## 谱近似机制的后续诊断

2026-11-18T00:01:56+08:00完成：5个正随机专家在固定1024训练probe上的E从0.2632±0.0005降至0.0757±0.0003，同checkpoint validation R@1从0.125±0.053%提高到20.229±0.220%。初始化ρ0.3166反而低于末态0.4262，公共正坐标及分数尺度变化影响解释，不能据此建立ρ与实际E的全程单调关系。

原source seed20的回放补采已完成，outer0/500/1000/1950、inner15实际batch的Mean/P95依次为0.0820/0.1441、0.0736/0.1274、0.0736/0.1328、0.0764/0.1750。单源seed，后续Gram非负不再保证（该四点非负实例100%/100%/96%/88%）；其他inner及同head全100诊断保留。原初态、四个500步checkpoint及最终优化器/RNG均与原运行数值完全一致，无原数据修改。

追加outer1500的同口径恢复读出于2026-11-18T00:11:15+08:00完成：inner15 Mean/P95为0.0721/0.1616，Gram非负实例68%。原第1501次rollout抽到专家103的更新0起点；通过已测500/1000的8状态精确复现验证，无外层更新。

专家中间状态于2026-11-18T00:43:15+08:00补齐约每5个epoch网格：5专家×8新节点，固定原1024训练probe、无重训；新增验证检索与历史记录最大差异0。实际epoch-equivalent=update/71，完整表另存`positive_init_20261117T2325/expert_epoch_grid_20261118T0040/RESULTS.md`，不将近邻保存点改标成整数epoch。

另于2026-11-18T01:48:20+08:00完成outer600/1200/1800实际rollout补测，inner15 Mean/P95为0.0782/0.1740、0.0654/0.1467、0.0687/0.1569；原专家起点分别0/0/2250，inner0见完整表。保持单source seed20，完整回放与原artifact、优化器及RNG精确相等，详细结果位于`positive_init_20261117T2325/outer_grid_20261118T0120/RESULTS.md`。

完整结果与限制见[谱理论实验卡](EXP-20261107-server-a-hopa-spectral-theory.md)，本地报告为`HoPA-Rebuttal/theorem3_states_20261117/positive_init_20261117T2325/runs/attempt03/report/RESULTS.md`。本轮只补实测误差及机制联系，不宣称近似误差下降导致了检索改善；没有逐outer新学生检索。

## 研究问题与关键设置

上一轮[正余弦小试](EXP-20261111-server-a-pmrl-positive-init.md)显示无pairwise warm-up的PMRL真实CE可以学好Full，但还没有检验WBCE、learned S/LR及蒸馏。本轮采用仅正初始化后自由训练，保持新head和原生HoPA目标，并将初始化状态严格配对。

| 设置 | 本轮口径 |
|---|---|
| 数据 | MSRVTT Full7127 / 验证800；Random和合成集N100；不读test |
| 正初始化 | 同一1025D head参数化，b=1.05；之后自由学习，无InfoNCE warm-up |
| 初态bank | 显式保存全部参数和buffer，逐次加载校验SHA256；每个paired seed逐字一致，不只依赖RNGseed |
| 专家 | 每方法5个head起点100–104，3000更新；两方法同seed同初态；旧专家不复用 |
| 内循环 | 对应专家片段起点精确加载，包括当时b；原生plain SGD，16步匹配150真实更新；不重置中途b |
| 蒸馏 | 一个source seed20，HoPA/联合三对LoRS各2000外层；同100条真实tuple初始化，rank10、alpha1，无额外调参 |
| 最终学生 | 三个未见head seeds1000–1002；Full/Random/HoPA/LoRS同seed加载同一初态，动量均从空状态开始 |
| 学习率读出 | 固定三分支LR.03为控制；另保留artifact learned-LR。两种读出分开，均使用各方法的S |
| 训练与选择 | 学生3000更新/batch100/SGD .9/.0005，tau=.1；验证R@1+R@5选同一节点并保留末态 |

## 主要结果

**正初始化下HoPA高于联合LoRS及匹配Random，但当前只有一个蒸馏seed、验证集结果。** 固定LR的HoPA−LoRS为+0.389pp；learned-LR为+1.417pp。Full与合成集仍有明显差距，不能当作完整恢复Full或跨蒸馏seed稳定提升。

800条validation、六方向Recall均值（%）；±仅为三个配对未见学生head的样本SD。固定LR与learned-LR分别在两种蒸馏方法内排名，不混排为一套方法。

### 固定三分支LR=0.03

| 方法 | 验证选优R@1 ↑ | R@5 ↑ | R@10 ↑ | 固定3000步R@1 ↑ |
|---|---:|---:|---:|---:|
| HoPA | **4.076 ± 0.170** | **13.910 ± 0.469** | **22.444 ± 0.595** | **3.076 ± 0.094** |
| 联合LoRS | <ins>3.688 ± 0.116</ins> | <ins>12.347 ± 0.280</ins> | <ins>20.375 ± 0.137</ins> | <ins>2.083 ± 0.055</ins> |

### 使用各自产物的learned LR

| 方法 | 验证选优R@1 ↑ | R@5 ↑ | R@10 ↑ | 固定3000步R@1 ↑ |
|---|---:|---:|---:|---:|
| HoPA | **5.097 ± 0.142** | **16.722 ± 0.167** | **25.924 ± 0.335** | **3.618 ± 0.187** |
| 联合LoRS | <ins>3.681 ± 0.084</ins> | <ins>12.715 ± 0.060</ins> | <ins>20.542 ± 0.369</ins> | <ins>2.639 ± 0.048</ins> |

匹配参照（验证选优）：Full-HoPA 19.972±0.223%、Random-HoPA 2.306±0.136%；Full-pair 17.444±0.251%、Random-pair 2.444±0.142%。固定3000步时Random-HoPA/Random-pair降至1.792±0.091% / 1.521±0.146%；合成集的末态下降也已保留。Full数据量不同，不能与N100压缩方法混作同预算排名。

### 历史WBCE门槛校准

2026-11-11 15:06 +0800核对：**当时WBCE门槛已通过，进入配对专家生成；最终合成集结果现已补齐于上方。** 同一个bank0、相同3000更新预算下，真实CE Full验证R@1为20.292%，WBCE Full为19.812%，WBCE Random100为2.500%。WBCE达到真实CE的97.64%，Full−Random为17.313pp，末态退化0pp。三项运行的完整初始化哈希均匹配同一bank状态，实际三分支LR均为0.03。

入门规则保持不变：WBCE Full≥同bank真实CE Full的90%、末态退化≤1pp、Full−Random≥5pp、Random≤Full80%；不通过则停止。以上是head seed0的验证校准，不是蒸馏收益，也不是独立测试结果。

## 解释与局限

- 只保证专家/最终学生在第0步采用正初始化；内循环中途的b由专家轨迹决定，不能人为重置为1.05。
- 模型初态与最终学生的空动量状态严格配对，但专家的momentum SGD和原生内循环plain SGD仍不同，明确保留这项算法差异。
- WBCE、S的无约束低秩参数化和原近似回放不变；固定LR读出不能冒充完整learned-LR方法，二者都报告。
- 一个蒸馏seed、三个学生head；SD只反映学生初始化波动，不能声称多蒸馏seed稳定性。验证探索不能代替独立测试。

## 下一步判断

门槛和单seed成对验证均已完成。现有结果支持进一步核对独立蒸馏seed，且必须分别保留固定LR与learned-LR读出；暂不能推断test泛化。是否扩展仍待下一轮研究决策，本次不新增训练。

## 完整结果与来源

本地入口`HoPA-Rebuttal/positive_init_distill/README.md`；协议、源码哈希、bank与起点audit、日志、PID/GPU位于该项目的控制目录及`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_distill/`运行根目录。旧小试与旧完整实验只读保留。

权威本地报告：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_distill/20261111T145619-server-a-positive-distill-v1/REPORT.md`及`summary.json`，完成标记`finished.json`明确`test_evaluated=false`。`summary.json` SHA-256：`b3aca1fdfbb2d8130c4fc25eb43dbb8eb054c9d6bfc1349a5cdb9f3811c48674`。本次仅读取既有结果；编辑前卡片保存在本地`runs/rebuttal-record-audit-20261112T1705/before/`。

<!-- LB-POSITIVE-START -->
## LanguageBind正初始化：CE buffer→WBCE蒸馏

完整单seed续跑已完成。固定LR验证R@1：HoPA 3.125±0.430%，联合LoRS 2.431±0.087%，配对均值差+0.694pp。 learned-LR验证R@1：HoPA 3.611±0.345%，联合LoRS 2.382±0.167%，配对均值差+1.229pp。 SD仅为三个学生head的波动，无test。

历史校准：正初始化CE Full 16.229%，WBCE Full 12.458%（CE的76.8%）；旧版因90%门槛停止。观察结果后，用户明确取消此项阻塞条件，保留为诊断及历史负结果。

MSRVTT 7127/800；769D positive_free、无warm-up。每方法5条CE专家，source seed20各2000外层，三个未见head1000–1002，Full/Random和固定/learned-LR合成学生共24项。只取消WBCE/CE90%门槛，其余配方不变。

核对：2026-11-14T17:57:50+08:00。本地运行入口`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/languagebind_positive_distill/continued_ce_wbce`；远端权威产物`/home/xiaobo.xia/YuxuanGao/LanguageBind-Positive-20261114/continuations/ce-wbce-v2/results`。本地结果摘要`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/languagebind_positive_distill/20261114T161649-server-a-languagebind-positive-shared-v2-seed20/continuation_ce_wbce_v2_metadata/REPORT.md`、`summary.json`。
<!-- LB-POSITIVE-END -->

<!-- IB-INDEPENDENT-START -->
## ImageBind正初始化：独立pairwise LoRS

ImageBind正初始化独立pairwise补实验已完成。fixed_lr_0.03: HoPA 4.076%，独立LoRS 4.326%，HoPA−独立 -0.250pp；learned_lr: HoPA 5.097%，独立LoRS 4.507%，HoPA−独立 +0.590pp。

VT/VA/AT分别训练buffer、蒸馏及学生，互不共享优化变量；每对5条CE专家、N100、2000外层、16内层，3个未见head，每pair分别验证选模并另报统一步数与固定末态。单source seed20，无test。温度和预算匹配旧正初始化小试；LoRS采用主实验merged数据梯度及per-branch裁剪LR梯度。独立特征参数约为共享三模态集的两倍，不是等总参数或等总时间对照。

核对：2026-11-15T17:10:44+08:00。结果`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_independent_lors/20261115T165301-server-a-positive-independent-seed20/REPORT.md`和`summary.json`；控制与源码清单`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/positive_init_independent_lors/runs/20261115T165301-server-a-positive-independent-seed20`。旧HoPA/共享3-pair结果只读引用，历史负结果保留。
<!-- IB-INDEPENDENT-END -->

<!-- LB-INDEPENDENT-START -->
## LanguageBind正初始化：独立pairwise LoRS

LanguageBind正初始化独立pairwise补实验已完成。fixed_lr_0.03：HoPA 3.125±0.430%，独立LoRS 3.201±0.024%，差值-0.076pp；learned_lr：HoPA 3.611±0.345%，独立LoRS 3.236±0.052%，差值+0.375pp。

MSRVTT 7127/800，769D positive_free，无warm-up；VT/VA/AT各5条CE专家、N100独立合成集、2000外层/16内层，3个未见学生head，共36评估。旧HoPA/共享3-pair只读引用。同名义N每pair100，独立特征参数是共享三模态的两倍，非等总参数/时间。三pair各自验证选模，并保留共同步数和固定3000；单source seed20，SD仅学生head波动，无test。

核对：2026-11-15T17:51:32+08:00。本地入口`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/languagebind_independent_lors`；远端产物`/home/xiaobo.xia/YuxuanGao/LanguageBind-Positive-20261114/continuations/independent-lors-v1/results`。结果摘要`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/languagebind_independent_lors/20261115-pro6000-independent-seed20-v1/metadata/REPORT.md`和`summary.json`。
<!-- LB-INDEPENDENT-END -->
