# 原生 VAST ITM 基线探索 v2

截至2026年10月27日19:30 UTC的全部ITM探索、三seed基线与负例实验进展，见[ITM探索实验综合报告](REPORT.md)。该报告为静态快照；实时状态以运行目录为准。

实现用户确认的冻结阶段计划。沿用原ITC、原始token缓存和固定候选；仅训练独立的VAST matcher副本。任务为TV、TA、TVA；没有VA入口、几何特征、几何损失或联合训练。旧`itm_hierarchy`及旧结果不修改。

## 模型与比较规则

- TVA直接保留原实现；TV只接收V条件，TA只接收A条件，三者共享BERT和匹配头。无新增query和独立head。
- 每步96个tuple、正负各48，所有任务使用同一批tuple。TVA曝光始终96；局部任务各增加96视图，故总视图为96/192/288，成本分开报告。
- C0损失为平衡BCE；多任务尺度对照M0为0.5L_TVA。M-TV/M-TA分别加0.5L_TV/0.5L_TA；M-Both加0.25L_TV+0.25L_TA。每项内部正负平衡。
- 所有训练从相同VAST预训练matcher初始化，阶段父节点仅表示配置关系，不继承已训练权重。ITC和共享缓存只读。
- 原生C0使用受控的50%正例/50%均匀122负例，并非作者VAST全部训练配方的复现。
- 推理只用TVA logit，同一top32候选；正例不在池内仍计未命中。TV/TA只用于辅助训练和诊断，不混合推理分数。

## 自动阶段

1. **A校准**：新跑LR1e-5、3e-5，seed50，2000步；经原生等价检查后复用旧LR1e-4曲线。按R@1、R@5、较早步数、较小LR锁定公共LR与N_A。保留全部500步评测点checkpoint。
2. **C0噪声**：选定seed50 checkpoint只做完整验证/诊断，seed51/52从原始初始化训练到同一N_A，计算样本标准差sigma_A。
3. **B来源配额**：N-t负例112/121/122/123为1/6、1/6、1/2、1/6；N-u各1/4。其他设置不变。
4. **C局部监督**：在较优混合配额上分别运行M0、M-TV、M-TA、M-Both，固定TVA样本量，记录额外计算。
5. **D难负**：分别对C0、M0、较优非空辅助配置加入rho0.5，组成局部监督与难负的配对比较；123保持均匀。112使用干净TV→A、121使用TA→V、122使用VA→T。温度沿用冻结ITC。
6. **E配对复核**：筛选最有希望的候选及直接前驱/祖先补seed51/52；若为多任务+难负组合，同时补困难单任务对照以识别交互。平均增益须大于2sigma_A且3个配对差值均正；否则保留更简单的前驱/C0。
7. **F锁定测试**：写入SELECTION_LOCK后才能提取外部特征与评测C0、选定方案及必要对照的三个seed。MSRVTT884视频；VATEX1224视频、全部12240caption。使用共同冻结VAST编码器及ITC候选；不做PMRL优劣结论。

所有方法结束时报告VAST六个不重叠检索方向和uniform/hard来源诊断，不能把单seed筛选最高分称作稳健改进。语义审查仍未完成，不报告假负例率，不用模型改标签。

## 验证和运行

现有项目环境：`../../.venv/bin/python`。数据及检查点目录：`/data0/xiaobo.xia/yuxuan.gao/itm_native_baseline_20261027_v2`。

- `tests_cpu.py`：损失/梯度与完整批次一致、TVA曝光量、选模与配对规则。
- `tests_integration.py`：真实多caption输入索引、冻结头与VAST模块隔离、未锁定时禁止测试、PID出生时间核验。
- `tests_graph.py`：只在临时合成夹具中验证完整阶段图及阴性结果保留C0，不产生真实训练/测试结果。
- `check_gpu.py --device 0`：真实三步TVA逐位等价、TV/TA与原生通路一致、排除模态不影响输出/梯度、hard教师距离一致、三任务+hard磁盘恢复逐位一致。
- `seal.py`：运行CPU检查，核实GPU证据、旧C0来源、缓存与划分，封存源码。封存后不修改相关源码；变更使用新版本。
- `schedule.py --execute --max-active 8`：启动整个有依赖的实验图；阶段内并行，初版每卡至多一个本研究worker。优先低利用率、空闲显存充足的卡，不操作其他人的任务。
- 同配置恢复需先确认原worker已退出，再显式使用`--resume-failed`。在世worker按PID、出生时间、完整命令核对后继续观察，不因等待超时重启。

资源：单worker显存上限24GiB、启动空闲至少48GiB、运行空闲低于12GiB停止自身；磁盘保护40GiB，调度还预留每个活动worker6GiB检查点预算，写检查点串行且预留原子写入空间。每worker CPU2线程。不开启同卡双任务，除非后续实测吞吐和资源余量支持并另行记录。

`logs/status.json`、`logs/launches.jsonl`和各run的runtime/progress/failures记录真实PID、命令、GPU和时间。FAILED不自动删掉，DONE需要核对配置、更新数和结果hash。最后输出`reports/results.json`、`reports/REPORT.md`、`reports/figures.pdf`及PNG。状态以实际运行文件和进程为准，本README不表示各阶段已完成。

## 实施核对与运行记录（2026-10-27）

9项CPU检查和真实GPU检查通过：原生TVA连续3次更新的参数逐位一致，TV/TA通路与原生实现一致、无不可见模态依赖；三任务+hard的磁盘恢复后参数逐位一致，峰值预留显存6.240GiB。

最终封存入口为`maintenance/seal_study.py`，它调用组件检查并将缓存、候选、诊断文件的哈希纳入持续核验；`seal.py`为内部组件步骤。

已启动LR1e-5与LR3e-5校准，worker PID分别1100674（GPU0）、1100675（GPU5）。启动阶段发现并修复了`/proc`命令行短暂为空的控制器竞态：只替换协调器，训练worker未停止、未重跑。新增真实子进程回归检查通过，数值组件再次GPU验证通过。差异仅为控制器/恢复元数据与回归测试，模型、损失、采样、预算和训练循环不变；审计材料位于`maintenance/controller_fix_01/`，旧源码和就绪证据保留。

新协调器PID1120314已成功接管同一批worker；当前阶段为A_calibration。静态PID仅记录当时核对，实时状态以数据目录`logs/status.json`、各run的progress与真实进程为准。

### 长任务会话修复与恢复（后续更新）

第一次接管后，旧执行会话关闭时两个worker也意外终止，均无Python模型异常日志。已通过实际PID消失及检查点读取确认：最后完整提交为step400，之前观察到的step500仍在验证，尚未提交。中断时间范围和重算记录保存在各run的`interruptions.jsonl`、`interruption_time_bounds.json`，不能把首次尝试成本省略。

已用8秒独立进程验证跨工具调用存活；控制器与worker现在使用独立session/process group、独立日志和DEVNULL输入。正式启动入口改为：

```bash
PYTHONNOUSERSITE=1 ../../.venv/bin/python -B maintenance/launch_study.py --max-active 8
# 仅在核实旧worker终止且检查点有效后，显式恢复：
PYTHONNOUSERSITE=1 ../../.venv/bin/python -B maintenance/launch_study.py --max-active 8 --resume-failed
```

当前协调器PID1149239，恢复worker PID1149293、1149294，从step400恢复同一配置。已观察到恢复后step420的loss和梯度范数与中断前完全一致。当前PID仅作核对记录，实时情况查看`current_coordinator.json`和数据目录`logs/status.json`。

两次修复仅涉及控制器启动/接管和恢复身份元数据，数值组件及训练更新循环未改变；兼容性审计和旧版本保存在`maintenance/controller_fix_01/`与`controller_fix_02/`。source seal显式记录兼容旧worker版本，不允许改变数据、学习率、任务、预算或采样后继续原run。旧实验和其他人的进程未操作。
