# Q5补充：HoPA Q100与各pair LoRS Q50的预算对照准备

## 2026-11-15执行版本：N50合成与学生预算曲线

<!-- N50-BUDGET-START -->
**complete**，核对：2026-11-15 15:06:39 +0800。三对N50和声明的学生预算评测已结束；单seed，所有预算点保留。 固定20步双查询R@1：HoPA 27.338%，LoRS50 31.825%；独立LoRS合计训练GPU时间0.467s，HoPA为2.054s。 存在共卡计算，耗时仅作执行记录，不用于公平效率结论。

|每模型更新|方法|单查询R@1↑|双查询R@1↑|双查询R@5↑|合计学生GPU秒↓|总优化更新|
|---:|---|---:|---:|---:|---:|---:|
|0|hopa|**20.362**|**27.866**|**52.187**|0.000|0|
|0|independent_lors50|**20.362**|**27.866**|**52.187**|0.000|0|
|1|hopa|<ins>20.004</ins>|<ins>26.961</ins>|<ins>52.225</ins>|1.241|1|
|1|independent_lors50|**21.022**|**28.582**|**54.223**|0.037|3|
|5|hopa|<ins>16.667</ins>|<ins>21.833</ins>|<ins>43.552</ins>|1.423|5|
|5|independent_lors50|**21.833**|**32.466**|**58.861**|0.130|15|
|10|hopa|<ins>16.139</ins>|<ins>20.701</ins>|<ins>42.232</ins>|1.638|10|
|10|independent_lors50|**19.608**|**30.807**|**57.051**|0.243|30|
|20|hopa|<ins>20.173</ins>|<ins>27.338</ins>|<ins>51.961</ins>|2.054|20|
|20|independent_lors50|**20.720**|**31.825**|**57.655**|0.467|60|
|40|hopa|**21.456**|<ins>31.259</ins>|<ins>56.637</ins>|2.876|40|
|40|independent_lors50|<ins>20.814</ins>|**32.127**|**59.314**|0.847|120|
|80|hopa|<ins>20.419</ins>|<ins>31.523</ins>|<ins>56.071</ins>|4.512|80|
|80|independent_lors50|**21.361**|**32.843**|**59.314**|1.518|240|

完整逐方向与成本见本地analysis/REPORT.md；不按最高测试值选预算。
<!-- N50-BUDGET-END -->

用户授权自主完成合成及不同下游预算比较。本机与已定位server2目录均未找到已完成的N50产物，本轮三个pair新合成；不以旧准备材料冒充已完成实验。既有20×10epoch配对专家核验后复用，HoPA参考使用同一theory_selected运行的outer2000末态，不使用测试选中的600步。

11-15资源修正：最初完全独占准入使队列等待约8小时43分钟，未启动任何N50 worker。最终改为有显存余量即可在GPU6/7运行：每合成进程allocator上限17GiB，额外计2GiB运行时和8GiB余量；学生上限12GiB、同卡串行。此前N100已测最大allocated为15.49GiB，先以N50数值预检验证容量。已有任务不终止。共卡耗时只作执行记录，不能作为公平效率结果；训练和预算协议不变，原独占与中间20GiB门槛版本均归档。

合成阶段每对Q50、seed0、2000实际更新，内层16/batch25、rank10/alpha1、特征LR100、相似度LR10、初始学生LR.01/meta1e-4。关闭学生评测，按固定预算保存初态、每200步及末态，不用test选择合成集。代码中N=100仅代表原生配方，q=50是实际数据规模。

学生统一预训练初始化和seed1000，固定batch128，一条轨迹保存0/1/5/10/20/40/80更新。N≤100时每epoch一个更新；LoRS保留原20epoch调度（milestone11、gamma.1及原生ep0 scheduler调用），HoPA无scheduler，调度不随预算端点改变。所有预算点完整报告，不用测试最高点决定训练时长。报告单/双查询R@1/5/10及三对LoRS合计学生CUDA-event时间与优化墙钟时间；同卡串行、评测与I/O单列，不把每模型相同步数称为等总计算。

当前仅一个蒸馏seed，测试集有历史使用，不称全新确认或多seed稳定性。合成参数近似匹配HoPA Q100，实际数量在完成后逐张量计算。HoPA旧源执行过周期评测的事实保留；本轮不重新蒸馏HoPA。

本地代码：`HoPA-Rebuttal/q5_equal/distill_only_20261115/`；输出：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/q5_equal/20261115T051102-server-a-lors50-budget`。输入来源与哈希在sources/manifest.json，专家在expert_reuse.json，冻结代码在source_manifest.json及source_snapshot，状态在progress.json，最终报告analysis/REPORT.md。最多GPU6/7各一worker，三对完成后同卡串行训练学生。GPU等待上限24h，失败保留，不改超参数追求结果。无commit/push；git fetch失败。

下方保留11-12准备材料的历史核对，不能当作当前执行状态。

[返回主实验卡](../EXP-20261107-server-a-hopa-budget-efficiency.md) · [Rebuttal目录](../../summaries/rebuttal-20261112/README.md) · 归属EXP-20261107-server-a-hopa-budget-efficiency · 本地材料核对/文档补录：2026-11-12，Asia/Shanghai

**尚无可核实的本分支正式结果。** 本地`HoPA-Rebuttal/q5_equal/`已有独立原生代码副本、专家来源清单和有限性能队列，但未发现本分支本地`runs/`、启动记录或结果汇总；远端未核实。不能把存在代码当作已启动，也不能把主卡旧Q5结果直接填入本分支。

## 研究问题与关键设置

准备检验缩小独立pair LoRS的合成规模后，与HoPA Q100在检索性能上的差异。以下由现存`performance_queue.py`与`worker.py`读取，是代码中的计划口径，未被实际运行参数文件确认。

| 设置 | 已有代码中的口径 |
|---|---|
| 数据 | MSR-VTT，V/T/A；复用q5_native的train/test注释和冻结ImageBind缓存 |
| 合成规模 | HoPA Q100；VT、VA、AT三组LoRS各Q50。任务字段`N=100`控制配方，实际tuple数由`q`传给`num_queries`，不得将LoRS写成Q100 |
| 专家 | `input_sources.json`指定复用`q5_native/20261108-native-v5d-pilot`，不重新训练专家 |
| 预算与种子 | 单seed0、各2000外层更新、16内层步、batch25、专家跨度2、max_start5 |
| 学生 | 每次1个学生、20epoch；外层每200更新评估，沿用原生入口 |
| 选择规则 | 现有材料没有本分支独立验证划分或最终选模汇总；后续必须按实际运行产物确认，不能称validation-selected |
| 指标 | 计划读取六方向R@1/R@5/R@10；不同pair先完整汇齐再聚合，尚无数值 |
| 成本边界 | 性能队列允许共卡，并显式标记`timing_comparison_valid=false`；其耗时不得用于公平加速比 |

## 主要结果与限制

尚无正式结果。99项冻结源码/注释文件与`scientific_manifest.json`逐项SHA-256相符，仅证明本地材料身份。没有运行完成或数值对齐记录，不能宣称预检或正式实验已经通过。

Q100与三个Q50也不自动等于严格等参数：需按各模态维度、相似度矩阵参数化及学习率参数核算实际总量。“等预算”是该分支要验证的对照目标，当前不报告已实现精确参数匹配，也不冒充等蒸馏时间实验。

## 下一步判断

先找回对应执行记录；若远端实际运行过，应沿用原run ID补入，不重复立项。没有记录时保持准备/待核实状态。本次仅补文档，不启动队列、连接远端、重新蒸馏或改动输入。

## 完整来源

本地代码/来源：`HoPA-Rebuttal/q5_equal/`；原生`reference/`与`runtime/`、`worker.py`、`native_observer.py`、`validate.py`、`performance_queue.py`、`scientific_manifest.json`、`input_sources.json`。本地说明入口为同目录`README.md`。

- `performance_queue.py` SHA-256：`e6f321ae719025d7ce1333789a93ff41d1a8c55d65116fa822742c5430b118ed`。
- `worker.py` SHA-256：`c0b961a0633006665a8af957d00bfbaa8256beb7a8ef86ac49b2b2e6b55ff9bc`。
- `scientific_manifest.json` SHA-256：`1af07c6d0c38579186edefa3e2fb03799772d3287db8e82ed2b55b55dc91b6b0`。

该补充沿用预算研究主卡编号，不为同一问题重复建EXP。所有结论以本地现存材料为限；远端状态尚未核实。
