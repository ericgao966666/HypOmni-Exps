# 随机ImageBind投影头能否形成可学习且不饱和的HoPA设置

[返回实验总览](../README.md) · EXP-20261110-server-a-hopa-random-head · 正式结果完成：2026-11-11 00:57:01 +0800；本地结果核对与文档更新：2026-11-12

**完整N100实验已有正式test结果：HoPA比匹配Random提高9.310pp，但比联合LoRS低1.702pp，未达到预设的优于LoRS门槛。** 五个独立蒸馏seed，不能将每seed三个学生head当成15个独立蒸馏重复。下方CPU小试和GPU校准均为历史阶段，不能替代完整终测。

<!-- RANDOM-HEAD-FULL-STATUS-START -->
完整随机head实验状态：`complete`，核对2026-11-11T00:57:01+08:00。 测试六方向R@1：HoPA 12.472%、联合LoRS 14.174%；HoPA−LoRS -1.702pp，五个独立蒸馏seed。

本地完整运行：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/random_head_full/20261110T215841-server-a-random-head-4gpu-v3`；控制与日志：`/home/xiaobo.xia/YuxuanGao/HoPA-Rebuttal/random_head_full/runs/20261110T215841-server-a-random-head-4gpu-v3`。
<!-- RANDOM-HEAD-FULL-STATUS-END -->


## 完整实验：锁定后884条测试结果

MSRVTT训练7127/验证800/测试884，冻结ImageBind trunk、随机投影头；合成N100。专家和学生3000更新，HoPA采用验证锁定的300步warm-up配方；每方法20条专家。HoPA/联合LoRS各5个蒸馏seed20–24，外层固定2000更新，每份数据3个未见学生head1000–1002。所有参数及学生checkpoint按800条验证集R@1+R@5锁定后才读取test；没有按test选模。

测试六方向平均Recall（%）。先对同蒸馏seed的三个head求均值，再计算五个seed的样本SD。相同N100的三条件按列排名；两种Random学习器在本轮得到相同数值。

| 条件 | R@1 ↑ | R@5 ↑ | R@10 ↑ |
|---|---:|---:|---:|
| 匹配Random | 3.162 ± 0.225 | 10.840 ± 0.469 | 17.353 ± 0.604 |
| HoPA | <ins>12.472 ± 0.338</ins> | <ins>32.015 ± 0.309</ins> | <ins>43.435 ± 0.600</ins> |
| 联合LoRS | **14.174 ± 0.239** | **35.889 ± 0.341** | **47.998 ± 0.280** |

配对HoPA−LoRS为−1.702±0.216pp，95% t区间[−1.970, −1.434]pp；HoPA−Random为+9.310±0.329pp，区间[8.901, 9.719]pp，均以5个独立蒸馏seed为单位。匹配HoPA学习器Full为18.037±0.190% R@1，Full−Random差距恢复约62.59%；Full的±为三个head初始化的SD，不是蒸馏seed间SD；Full与压缩条件的数据预算不同，单独作参照。

data-only控制去掉learned S/LR后，HoPA/联合LoRS/Random R@1为9.947±0.351% / 11.324±0.121% / 2.919±0.201%，仍未反转HoPA低于LoRS的排序。完整固定末态、逐head结果和Holm校正在机器汇总中。结论限于冻结ImageBind及本轮配方，不推断其他backbone、LanguageBind或从头端到端训练。

本地权威结果：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/random_head_full/20261110T215841-server-a-random-head-4gpu-v3/gpu_pipeline/REPORT.md`及`summary.json`；选择锁为同目录`evaluation_lock.json`，完成标记为`finished.json`。`summary.json` SHA-256：`c8e2e4b8457cba0ca5d7066a1aadd7f95f1e2100d9187cbf8ad04d8f8f6b196f`。代码与源码清单在`HoPA-Rebuttal/random_head_full/`及其控制run目录。

## 历史GPU校准：进入蒸馏的门槛

结果核对：2026-11-10 22:39 +0800。65项GPU校准运行完成，锁定warm-up结束点300、HoPA学习率0.03；前150更新为三对InfoNCE，150–300线性过渡，之后使用HoPA目标，总预算3000更新。联合pair专家学习率0.01，Random两种学习器均经验证选择0.03。

三个独立确认head seeds10/11/12、800条验证、六方向平均R@1（%）如下；标准差为这三个确认运行的样本SD，不是蒸馏seed方差。均按验证Avg R@1+R@5选择同一节点。

| Full学习路径 | 验证Avg R@1 ↑ |
|---|---:|
| 强InfoNCE参考 | **21.132 ± 0.240** |
| HoPA真实CE专家路径 | <ins>20.778 ± 0.073</ins> |
| HoPA合成WBCE学生路径，S=I | 20.562 ± 0.237 |
| 联合pair的WBCE学生路径，S=I | 17.639 ± 0.154 |

经过学习率搜索的Random100在HoPA匹配学生路径上为**3.042 ± 0.199%**，Full−Random为**17.521pp**，Random/Full约14.79%。两条HoPA Full路径分别达到强InfoNCE参考的98.32%和97.31%，确认运行中最大末态退化0.417pp，满足事前Full质量及稳定性门槛。联合pair路径的Full−Random为14.597pp，也通过不饱和门槛。

这是2026-11-10的配方校准证据，支持该随机head设置可学习且有明显数据量差距；校准本身不作为蒸馏收益证据。当时22:39完成26/40条专家，尚未进入正式蒸馏；随后完整结果已完成并列于上方。

来源：本地完整运行`gpu_pipeline/calibration/decision.json`、`gate_progress.json`及逐条件`result.json`，均位于上述完整run的`gpu_pipeline/`目录。

### 单卡叠加进程的资源诊断

2026-11-10在GPU2对当前HoPA head训练进行1/2/3进程小试及反序复核。单进程总吞吐29.286/28.933 updates/s；双进程总吞吐19.631/19.740 updates/s；三进程19.663 updates/s。双/三进程使总吞吐下降约32–33%，所以维持GPU2/4/5/6各一个worker。只临时暂停本任务派发和GPU2 worker，现已恢复；所有已完成专家及当前任务均保留，没有修改训练配方。

该微测不含验证与NFS保存，权重丢弃；不是论文效率比较，也不代表蒸馏回放阶段的最佳并发。可能涉及小算子、同步和上下文切换开销，未用profiler定位。完整协议与原始计时见本地`HoPA-Rebuttal/random_head_full/resource_trials/STACKING_REPORT.md`。

## 第一轮CPU小试（历史结果，保留）

[返回实验总览](../README.md) · EXP-20261110-server-a-hopa-random-head · 结果核对：2026-11-10 16:23，Asia/Shanghai；文档更新：2026-11-10

**六条件单seed小试已完成，随机head设置确实出现明显Full−Random差距，但短warm-up尚未把PMRL训练到强Full基线水平。** 800条独立验证、六方向平均R@1：纯PMRL Full/Random为4.750/0.312%，三对InfoNCE为20.917/3.521%，warm-up→PMRL为13.250/3.604%。对应差距4.438、17.396、9.646pp。warm-up比纯PMRL Full提高8.500pp，仍低于InfoNCE 7.667pp。

纯PMRL Full有66.50%的配对余弦为负；事后仅用共同训练100条确定全局模态符号，不重新训练、不用验证挑符号，可使同一Full checkpoint的R@1从4.750提高到11.917%，支持方向歧义解释部分低分，但仍未消除全部差距。该校正是额外诊断，不能替换原主结果。用户明确不做LanguageBind；没有生成蒸馏数据或专家池，也没有评测test。

## 研究问题与关键设置

| 设置 | 本轮口径 |
|---|---|
| 数据与划分 | 原MSRVTT共同清单7927 train / 884 test；train按视频ID、seed20261110划800验证，Full=7127；test只核对ID互斥，不读取特征或评测 |
| 数据条件 | Full7127与其中seed0采样的Random100；相同Random100还作为共同训练probe |
| 初始化 | 冻结ImageBind trunk，三模态原生Linear独立随机初始化，LayerNorm1/0，postprocessor默认scale；无预训练head；输出1024D，3151873可训练参数 |
| 目标 | 原始raw-SVD谱CE＋proxy实例CE；三对双向InfoNCE均值；前75步pairwise、后75步线性转PMRL、余1350步纯PMRL |
| 训练预算 | 六条件，单head seed0，batch100、各1500更新；SGD .01、momentum .9、wd .0005、tau1/tau2 .1；无LR衰减/梯度裁剪 |
| 执行设备 | GPU均占用后，在正式训练前明确切换为两线程CPU，所有条件相同设备；纯FP32，不作效率对比 |
| 配对控制 | 相同head状态、同数据条件的batch序列哈希一致；Full与Random等更新，不等epoch；各自数据内warm-up |
| 选模 | 固定验证节点，按六方向Avg R@1+R@5选择同一正更新节点，并列最早；另报固定1500；test不参与 |
| 指标 | 六方向R@1/5/10算术均值（%），Full−Random为百分点；paired row正例，分数并列按索引稳定排序；监测余弦符号、谱间隙、残差和梯度 |

## 主要结果

下表为验证集六方向平均Recall（%），每次训练按Avg R@1+R@5选同一正更新节点；单seed，无标准差。排名只在同一训练数据条件的三个目标间比较。

| 数据 | 目标 | 所选更新 | R@1 ↑ | R@5 ↑ | R@10 ↑ |
|---|---|---:|---:|---:|---:|
| Full7127 | PMRL | 1500 | 4.750 | 12.083 | 16.000 |
| Full7127 | 三对InfoNCE均值 | 1500 | **20.917** | **44.438** | **57.000** |
| Full7127 | warm-up→PMRL | 1500 | <ins>13.250</ins> | <ins>34.167</ins> | <ins>47.021</ins> |
| Random100 | PMRL | 1300 | 0.312 | 1.250 | 2.146 |
| Random100 | 三对InfoNCE均值 | 300 | <ins>3.521</ins> | **11.792** | <ins>18.292</ins> |
| Random100 | warm-up→PMRL | 300 | **3.604** | <ins>11.646</ins> | **18.458** |

**固定1500更新敏感性：** Full三组不变；Random三组R@1分别0.354、3.521、3.417%，Full−Random分别4.396、17.396、9.833pp。因此较大数据差距不只来自验证选优。完整固定末态R@5/R@10保留于本地报告。

Random100的InfoNCE、warm-up在所选节点的共同训练100条probe R@1分别99.500%、99.333%，验证仅3.521%、3.604%；训练probe候选数100，不与800验证直接比较绝对数值，但它表明Random已能拟合自己的训练数据。Full相同probe为78.667%、44.167%；此时Full泛化更好，不能以训练集召回单独排名。

### 方向诊断：事后分析，不替换主表

每个原有checkpoint只用共同训练100条选择四种相对符号中平均匹配余弦最高者；固定video=+1。先保存符号决定，再读验证输出；校正后不重选checkpoint、不读test。下表仅在同一行比较前后。

| 条件 | 符号video/text/audio | 原R@1 | 校正后R@1 | Δpp |
|---|---|---:|---:|---:|
| Full PMRL，1500步 | + / − / + | <ins>4.750</ins> | **11.917** | +7.167 |
| Random PMRL，原选优1300步 | + / − / − | <ins>0.312</ins> | **1.521** | +1.208 |

其余四条件都选择(+,+,+)，检索不变；Random PMRL固定1500步为0.354→1.583%。完整六条件及两个读出见独立`polarity_diagnostic`报告。PMRL Full校正后仍低于InfoNCE 9.000pp，因此方向问题不是完整解释。

曲线在本地`HoPA-Rebuttal/random_head_pilot/results/20261110-v1-cpu/learning_curves.png`与同名PDF：Full侧显示warm-up消除大部分负余弦但检索增长慢于InfoNCE；Random侧显示训练早期达到验证平台，固定末态没有改变数据差距判断。没有多seed误差带。

## 解释与局限

- 单一SGD配方和初始化，尚不足以判断某个loss从随机初始化原则上不可学习。Full曲线仍上升，1500更新不代表收敛。warm-up是新增训练规则，原PMRL/InfoNCE与全部末态均保留。
- 全局符号诊断是在观察PMRL负余弦后新增的机制分析，未经独立seed验证。只用训练数据选符号，没有把验证最优符号当作合法训练规则。
- 所有六条件使用两线程CPU。CPU下原生head、full/reduced SVD目标/梯度/HVP等价检查通过；GPU因占用未完成预检。raw-SVD的符号约定及数值轨迹可能依设备改变，正式GPU蒸馏前需独立复核，不把本轮冒充GPU结果。
- Full指划出验证后剩余训练集，不能引用旧Full数值；800候选验证与历史884测试结果不可直接比较。
- backbone仍为预训练ImageBind，本实验只检验对已训练head/跨模态对齐的依赖，不声称端到端从头训练或跨源backbone鲁棒性。
- 本轮只有head训练，没有蒸馏，不能将Full−Random差距当作HoPA相对Random的收益。

## 历史小试的下一步判断（后续已执行）

保留随机head方向：单seed已显示数据不足造成的较大差距，原低预算饱和问题有所缓解。下一步优先核对其他head/子集seed，并在同一总更新预算内比较更长的pairwise启动阶段，检验PMRL Full能否接近强InfoNCE Full。暂不把当前短warm-up配方直接扩成大规模专家/蒸馏；后续必须重建对应随机head和调度的专家轨迹。该建议在后续完整实验中已按验证门槛执行，结果见上方；本次整理不追加LanguageBind或训练预算。

## 完整结果与来源

本地协议与代码：`HoPA-Rebuttal/random_head_pilot/`；派生特征缓存与训练产物：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/random_head_pilot/`；输入缓存只读复用`HoPA/runs/msrvtt/trunk_cache`。原训练清单与原生head源码来自`HoPA-Rebuttal/q5_native`。完整源码/数据哈希、PID、GPU、日志和检查结果记录于独立run目录及本地`runs/EXP-20261110-server-a-hopa-random-head/`。

本轮权威运行：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/random_head_pilot/20261110-v1-cpu/`，2026-11-10 16:19:26 +0800结束，6/6、无失败。工作区阅读副本：`HoPA-Rebuttal/random_head_pilot/results/20261110-v1-cpu/`，含主报告、CSV/JSON、原始日志副本、符号诊断及图；`archive_manifest.json`逐文件校验副本与源SHA256一致。

核验：7项CPU数值/协议检查通过；6条件均完整1500更新、共享初始head哈希、同数据条件batch序列相同、warm-up与InfoNCE前75步验证/几何完全一致、每条件18个预定节点；校正诊断重新评估原模型时与主表逐指标一致。测试特征和测试指标均未读取。

实验记录仓库已成功fetch并核对远端新增记录；本地有既有未提交改动，本次保留且不自动合并、不提交、不上传。

2026-11-12补录：原卡及当时校准进度保存在本地`runs/rebuttal-record-audit-20261112T1705/before/`；本轮仅读取已完成产物，未重新训练或评测。
