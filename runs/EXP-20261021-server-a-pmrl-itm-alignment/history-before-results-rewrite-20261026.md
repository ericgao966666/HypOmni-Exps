# 历史实验卡与运行记录归档

[查看当前结果与结论](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md)

这是重写前实验卡的历史副本（来源提交 `f6bc095ede09af4ae0b4118ab92cd480e1a56456`）。其中“当前”“运行中”等描述均指原记录时点；仅调整相对链接，不作为实时状态。主卡今后只更新结果、解释和影响可比性的协议变化。

---

# PMRL：对齐空间评分能否改善 ITM

[返回实验总览](../../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-20261021-server-a-pmrl-itm-alignment |
| 项目与研究方向 | PMRL-ITM；严格 TVA 的负样本采样、检索候选与 ITM 重排 |
| 状态 | 已完成：4组seed50训练、4项开发集及16项测试；19:05结束，原始汇总与权威快照已生成 |
| 实验日期 | 2026-10-22 正式启动 |
| 最后核对时间 | 2026-10-24 21:39，Asia/Shanghai |
| 前序实验 | [EXP-001 历史零样本基线](../../experiments/EXP-001-zero-shot-baselines.md)，仅作不同协议参考 |

## 要回答的问题

保留 PMRL 的谱损失、编码器和 VA token ITM，将负样本采样与候选评分从融合投影 `T–VA` 改为 TV 余弦、TV/TA 均值或最大奇异值，是否能把对齐收益转化为更好的最终检索？若共同候选评分下的 ITM 表现没有重复改善，则不支持采样机制收益；候选改善与采样改善分开报告。当前单seed结果未支持≥0.5pp的独立采样收益；开发集选定融合在测试中退化，见下方最终结果。

## 实验协议

| 项目 | 约定 |
|---|---|
| 训练数据 | 当前过滤版86,706条；从原accepted 86,707条仅剔除`hU6PCGt2CuQ.20`；严格TVA去字幕；当前训练清单SHA-256 `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384`，原清单与排除证据保留 |
| 初始化 | 同一 VAST 官方 `model_step_204994.pt`；SHA-256 `9005d283ea0de99549efbedeb7d21c8e25bea8fa41c0f6570296b0e7a055a6c5` |
| 训练范围 | 端到端；谱损失 T/V/A；ITM 文本与完整 VA token；无下游微调 |
| 训练预算 | 每组一个 DataLoader epoch；4 GPU × 16，全局 batch 64，512 维；当前 1,354 个 batch，按原 drop_last 消费 86,656 条目槽位；不固定 1,360 步 |
| 超参数 | 主 LR 2e-5，视觉 LR 5e-7，AdamW，WD 0.01，warmup 0.1，tau1 0.05，tau2 0.1，ITM 权重 0.1 |
| 基线与变量 | legacy_va、tv、mean_tv_ta、sigma_max；采样评分与候选评分独立；新增评分温度在初始化的固定 VAST 批次上匹配负例分布熵后冻结 |
| 开发集 | MSRVTT 官方 train 中固定 hash 选择 1,000 个可用视听视频，每视频第一条 caption；与官方 test ID 不重叠；不参与梯度更新 |
| 测试 | MSRVTT 884、DiDeMo 995、ActivityNet 3,987、VATEX 1,224 个本机固定视听交集；严格 TVA、第一条 caption |
| 选模与选参 | 固定 epoch 末轮 checkpoint；评分/融合/采样只按开发集选择，测试前锁定 |
| 主指标 | 四数据集 × 双向 R@1 等权平均，%；Top-50 ITM；附 Stage-1、Top-20/100、候选覆盖率、候选内 conditional R@1 |
| 种子与阶段 | 当前按用户要求仅seed50，四个方法条件；不再追加42/123。原多seed规划保留为历史，当前执行预算以输出目录execution_policy.json为准 |
| 判定标准 | 当前为固定seed50的同协议方法对比，报告百分点差及条件于该训练种子的配对视频bootstrap；不估计训练种子标准差，原三种子判据不再用于本轮 |

完整协议、接口、测试及手动启动方式见 项目说明（原服务器本机路径：`../../PMRL-ITM/ITM_EXPERIMENT.md`）。源码基于 PMRL `a230347a072a46cdcb97eb30f4a5cdcf6f2119db` 的独立本地 checkout；实现改动尚未提交。启动时保存实际源码快照与哈希，不能用基底 commit 代替运行源码版本。

## 运行与证据

| run ID / 版本 | 条件与种子 | 状态 | 配置、源码与运行清单 | 结果与 checkpoint |
|---|---|---|---|---|
| implementation-v1 | 四种评分；规划 seeds 50/42/123 | CPU 验证；GPU 未启动 | 配置（原服务器本机路径：`../../PMRL-ITM/config/itm/`）、冻结数据清单（原服务器本机路径：`../../PMRL-ITM/assets/itm/manifest.json`）、测试（原服务器本机路径：`../../PMRL-ITM/tests/itm/`） | 无正式结果 |
| 20261021T170458-server-a-itm-start-seed50 | 用户指定 GPU 4–7；首轮 seed 50 | 已停止；四种单卡 smoke 通过，四卡被旧空闲门槛阻止 | [运行记录](20261021T170458-server-a-itm-start-seed50.md) | 无正式结果 |
| 20261022T134902-server-a-itm-four-gpu-seed50 | GPU 4–7；四卡 batch16；先 seed50 | smoke、校准完成；基线858个batch后DataLoader超时失败 | [运行记录](20261022T134902-server-a-itm-four-gpu-seed50.md) | 尚无检索结果 |
| 20261022T152509-server-a-itm-parallel-retry-seed50 | 4–7基线，0–3 TV；每卡16；seed50 | 两组各14次有效更新，无OOM；全新目录完整重试 | [运行记录](20261022T152509-server-a-itm-parallel-retry-seed50.md) | 尚无检索结果 |
| 20261022T161545-server-a-itm-recovery-v2-seed50 | 保留在跑的基线/TV；后续组恢复v2 | 上层调度已交接；基线610、TV527个batch | [运行记录](20261022T161545-server-a-itm-recovery-v2-seed50.md) | 恢复验证通过，尚无正式检索结果 |
| 20261022T170008-server-a-itm-filtered-recovery-seed50 | 四种方法统一86,706条过滤版；全新训练+百步保存 | 两组step100完整checkpoint已核实，基线144、TV106个batch | [运行记录](20261022T170008-server-a-itm-filtered-recovery-seed50.md) | 尚无正式结果 |
| 20261022T213041-server-a-itm-media-repair-resume-gpu0-3 | 同86,706条清单；单视频解码修复；从400步恢复 | GPU0–3显存不足，CPU侧控制器等待中 | [运行记录](20261022T213041-server-a-itm-media-repair-resume-gpu0-3.md) | 尚未恢复GPU训练，无正式检索结果 |
| 20261023T191223-server-a-itm-tv-resume400-gpu0-3 | 仅TV/seed50，从400步恢复；GPU0–3 | 用户选择等待容量，尚未启动GPU训练 | [运行记录](20261023T191223-server-a-itm-tv-resume400-gpu0-3.md) | 无新增正式结果 |
| 20261023T231135-server2-itm-remaining-resume | server2 GPU4–7；全剩余矩阵，基线从400步恢复 | 基线达到920；23:54:59 DataLoader超时 | [运行记录](20261023T231135-server2-itm-remaining-resume.md) | 500–900新增checkpoint已核验；无正式检索指标 |
| 20261023T235851-server2-itm-remaining-resume | 基线从900步恢复；协议不变 | 10-24 00:19:21同位置超时失败 | [运行记录](20261023T235851-server2-itm-remaining-resume.md) | 920次累计有效更新、零AMP跳步；完整checkpoint900保留 |
| 20261024T150526-server2-itm-remaining-resume | server2 GPU4–7；两视频无损覆盖，从900续跑 | 基线训练与开发集完成，TV900完整保存后交接 | [运行记录](20261024T150526-server2-itm-remaining-resume.md) | 1353有效更新、1 AMP跳步；完整末轮checkpoint1354，无测试指标 |
| 20261024T162513-server2-itm-remaining-resume | GPU4–7；TV从900恢复，主矩阵作业锁 | 已完成；19:05全部矩阵结束 | [运行记录](20261024T162513-server2-itm-remaining-resume.md) | 4组训练及16项测试均完成 |
| 20261024T162616-server2-itm-parallel-sigma_max | GPU0–3；首次并行尝试 | 启动前出现新进程，预检拒绝；未创建训练worker | [运行记录](20261024T162616-server2-itm-parallel-sigma_max.md) | 不计作已开始训练，不终止其他进程 |
| 20261024T163220-server2-itm-parallel-sigma_max | GPU0–3；sigma_max/seed50，从同一初始化开始 | 已完成1354批训练与开发集 | [运行记录](20261024T163220-server2-itm-parallel-sigma_max.md) | 训练及开发集独立运行；主队列随后复用，避免重复训练 |
| 20261024T175222-server2-itm-eval-pool-seed50 | 两台服务器单卡任务池；仍仅seed50 | 已完成16项测试；server1仅CPU等待、结束后已停止 | [运行总记录](20261024T175222-server2-itm-eval-pool-seed50.md) | 指标在18:22开发集锁定后发布；19:05完成 |

原始输出根目录：`/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/itm-alignment-v1`。17:04:58 启动串行入口，调度 PID 543885；每个 job 保存配置、命令、PID、GPU、端口、日志、输入指纹和完成状态。启动时 GPU 5、7 仍有其他任务，四卡阶段须重新确认空闲；未创建常驻 GPU 等待进程。

上述为 10-21 历史启动，进程已退出。后续容量探针中，原生分配器在 29 GiB 上限下两次因碎片 OOM；关闭权重缓存并使用 cudaMallocAsync 后完成单卡 batch16 四次有效更新。计划中的物理显存压测命令因自动审批服务额度耗尽未执行，正式训练没有启动，夜间没有本实验后台训练。

**当前继续使用的输出根目录**：`/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50`。10-23用户进一步授权迁移到114.214.255.126（固定别名server2）并完成全部剩余矩阵。源端TV等待器627326已按身份核实后停止；server2主队列使用GPU4–7，并行sigma_max槽位使用GPU0–3。训练源码与86,706条清单不变。基线和TV原step400完整checkpoint已复制到共享NFS并逐文件校验，原SSD副本保留；所有新增大型输出写NFS。主队列权威状态为`portable_state.json`，并行槽位为`portable_parallel_sigma_max.json`；旧`single_job_resume_state.json`仅为历史等待状态。

跨机执行SOP与命令见REMOTE_RUNBOOK.md（原服务器本机路径：`../../PMRL-ITM/REMOTE_RUNBOOK.md`），管理入口为ops/expctl.py（原服务器本机路径：`../../PMRL-ITM/ops/expctl.py`）。两端UID不同，通过限定范围的原生NFS ACL解决；跨UID文件操作、原子文件继承和共享锁已验证，server2全清单189,592个输入路径读取通过。Python3.9→3.10恢复状态核对通过，复用目标已有环境，未修改共享系统配置。

## 结果

**当前权威版本：[2026-10-24 单seed最终快照](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)**。四组训练、4个开发集和16个测试任务的退出状态、完成标记、样本口径均已核对；全流程于19:05:32完成。仅seed50，42/123已按用户要求取消，不把原三seed确认标记视为当前预算缺失。

统一TV候选、Top-50；各数据集为T→VA/VA→T双向R@1平均，总列对四数据集等权，单位%。本表为纯ITM（α=0），最优加粗、次优下划线。

| 训练方法 | MSRVTT | DiDeMo | ActivityNet | VATEX | 平均R@1 | 相对同候选基线 Δpp |
|---|---:|---:|---:|---:|---:|---:|
| legacy_va | 49.6041 | 51.2060 | **52.6712** | 76.8382 | 57.5799 | +0.0000 |
| tv | 49.6606 | 51.2563 | 52.1946 | 77.0425 | 57.5385 | -0.0414 |
| mean_tv_ta | <ins>50.8484</ins> | **51.7085** | 52.1821 | **77.3693** | **58.0271** | **+0.4472** |
| sigma_max | **50.9615** | <ins>51.5578</ins> | <ins>52.2699</ins> | <ins>77.1650</ins> | <ins>57.9886</ins> | <ins>+0.4087</ins> |

开发集事前选定的采样是`sigma_max`；其共同候选纯ITM增益为+0.4087pp。测试观察到的mean_tv_ta最高（+0.4472pp），不据此替换预选方案。两者均不足0.5pp。开发集选出的α=1在四组上均低于纯ITM；sigma_max融合均值51.4771%，较同口径融合基线51.6185%低0.1414pp。

[融合完整对比及口径解释](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)、[原始结果JSON](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/results.json)、[原始CSV](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/results.csv)、[逐任务完整指标](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/metrics)、[完成核验与哈希](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/verification.json)。原始输出未改写。单seed不估计训练种子标准差，bootstrap条件于本seed。

### 历史运行快照（以下不是当前状态）

**10-24 15:00历史核对**：当时尚无正式检索指标。server2首次续跑从400步推进至920/1354（约68%），跨过此前472步的媒体阻塞；500、600至900完整checkpoint持续保存。最新checkpoint900包含模型、优化器与四rank状态，已从源服务器核对三个payload的SHA-256全部一致。两次server2运行均在920附近因rank2 DataLoader等待600秒失败，日志未显示OOM；14:57现场确认旧控制器和torchrun均不存在、GPU4–7空闲。当时进行CPU有界重放定位；后续恢复与训练完成见下面15:46更新。

TV仍有step400恢复点；mean_tv_ta和sigma_max尚未开始。后续继续沿用基线→TV→其余两组、开发集选择、四数据集测试及条件种子复验协议。

**10-24 15:46更新**：精确定位rank2第922批`cLeZEBIFYHo.21`的`[173,340]`抽帧请求；原视频在最小复现中20秒超时，独立无损副本通过相同请求、全356帧及64次额外抽帧。FFmpeg逐帧YUV420P哈希与原视频完全一致，BT.709保留；新版本覆盖清单同时保留先前md6的355帧修复。训练清单与源码快照未变。server2从900恢复后已跨越卡点并于15:38完成全部1354批，实际1353次有效更新、1次AMP跳步；末轮checkpoint与训练完成标记均存在。当前`eval/legacy_va/seed-50/dev`处于ITM阶段，尚无正式四测试集结果。完整基线训练预算完成，不等于四组实验或评测已完成。


**10-24 16:40当前核对**：当前冻结版计划四组seed50，已启动三组训练。legacy_va完成1354批及1000样本开发集，末轮1353次有效更新、1次AMP跳步；TV为1000/1354（73.9%），在GPU4–7运行；sigma_max为156/1354（11.5%），在GPU0–3运行并已写入完整step100 checkpoint；mean_tv_ta尚未启动。四测试集尚未开始，按用户新要求仅seed50，42/123复验取消，当前不能判断方法收益。旧失败、重试与迁移属于同一研究问题的运行历史，不增加方法条件数。

10-24并行调度验证9项通过，包括真实跨进程作业锁互斥、显存余量及已有PID检查。源端实测两个控制器锁与两个job锁均由远端持有。主队列在TV900完整保存点交接，原始训练配置和数据不变；新增sigma_max使用29GiB分配预算及8GiB启动余量，batch16/卡不变。当前主队列沿用同样的资源预算。候选锁已按基线开发集选择为`tv`，最终采样方案及融合权重仍需全部开发集结果。

**同学任务影响核查的范围与限制**：已核对停止目标为本任务控制器4095490及其独立训练进程组192158；未发现向观察到的其他GPU PID发送停止信号的操作。16:26的0–3启动被新进程检查拒绝，未创建训练worker；其后若干小显存PID退出的原因未知。GPU2原有进程仍在，后续观察保存在项目`artifacts/launches/server2-peer-impact-review-20261024.json`。无权限查看系统OOM日志，也未获得同学退出日志，不能由这些观察证明其任务未受显存或算力竞争影响；同卡共用可能影响速度。没有读取同学的实验文件或终止其进程。

实现时验证：20 项新测试及 1 项原训练流程回归测试通过；包含两个 CPU/Gloo 进程的真实 gather / 梯度验证。17 个 Python 文件 AST 与四个配置 JSON 检查通过，Git diff whitespace 检查通过；初始化 checkpoint 哈希一致。源码及数据快照已在临时目录中独立导入并验证写入路径，临时快照已清理。详情与日志哈希见 验证记录（原服务器本机路径：`../../PMRL-ITM/artifacts/implementation_verification.json`）。随后已通过真实编码器的单卡 smoke 和容量探针；四卡检查仍是正式运行前的必要关卡。

评测范围是本轮冻结的视听交集，并非各数据集完整官方测试集。严格 TVA、第一条 caption 和媒体覆盖率均须随结果披露，不与旧 TVAS / 其他数据口径混合排名。

## 图表与解读

本轮以[最终汇总表](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)与[完整交叉报告](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/REPORT.md)为权威展示。原始完整指标、候选覆盖、方向细分和配对bootstrap均在快照内，另一台服务器及仓库网页无需挂载NFS即可读取。

## 结论与下一步

用户指定的单seed预算已完成。共同候选下采样收益较小，融合存在跨数据集退化；本轮不支持把改法描述为稳定、达到实用门槛的采样提升。后续若继续研究，应优先在开发集分析融合泛化，不用这批测试指标重新调参。当前没有启动新实验或追加seed。

## 变更记录

| 日期 | 事件 | 原因与影响 |
|---|---|---|
| 2026-10-21 | 建卡、实现严格 TVA 评分消融并冻结数据 | 按用户要求，每组 VAST150k 训练一个 epoch；用户选择届时手动启动，不设置等待任务。编辑前已 fetch，HEAD 与 origin/main 一致；保留已有 README / OPS-001 未提交改动，本次不提交或推送。 |
| 2026-10-21 17:04:58 | 用户授权在 GPU 4–7 开始，启动串行入口 | GPU 4、6 空闲，5、7 占用；先进行单卡检查，四卡阶段保留空闲门槛，不干扰已有任务。已再次 fetch 核对远端。 |
| 2026-10-22 13:49:02 | 用户再次要求启动，四卡均已空闲 | 启动新的输出目录与调度 PID217291；40GiB上限、cudaMallocAsync、正式 batch 不变，复用已核验单卡证据。 |
| 2026-10-22 14:09 | 核实正式训练已推进 | 四卡 smoke 和温度校准完成；legacy_va/seed50 已22次有效更新，零AMP跳步，无OOM；其余组尚未正式训练。 |
| 2026-10-22 15:25 | 用户授权增加GPU0–3并行组；旧基线在交接前自行超时退出 | 新目录完整重试：4–7基线、0–3 TV，batch不变；延长DataLoader等待上限，双队列固定归属；无停止信号，无覆盖失败记录。 |
| 2026-10-22 15:36 | 核实两组正式训练均已14次有效更新 | GPU0–3 TV新增组与GPU4–7基线重试均运行，0 AMP跳步，无OOM；每卡16、全局64、一epoch不变；无正式检索结果。 |
| 2026-10-22 16:19 | 用户要求优先保住训练进度，完成恢复v2并交接后续队列 | 25项ITM+1项pipeline+4项调度检查及真实双GPU AMP/NCCL中断恢复通过；当前两组未重启，仍使用v1末轮保存，后续组启用百步checkpoint。 |
| 2026-10-22 17:03 | 用户授权剔除卡住样本并全组重启 | 现场定位`hU6PCGt2CuQ.20`；新版本86,706条，仅移出训练清单；新队列106833，全部启用每100batch保存，待实际首份checkpoint确认。 |
| 2026-10-22 17:14:46 | 两组首份完整PMRL百步checkpoint均提交成功 | 核对模型/优化器/4rank状态与源、数据哈希；保存后基线144、TV106个batch，继续训练。 |
| 2026-10-22 21:36 | 用户要求查明问题并在GPU0–3继续 | 复现md6视频Decord读帧异常，独立无损修复且保留BT.709；数据清单不变、400步checkpoint保留；串行控制器413723等待容量，未恢复GPU训练。 |
| 2026-10-23 19:15 | 用户只要求一组实验并选择等待GPU0–3容量释放 | 新控制器627326，仅TV/seed50从400步恢复；原29GiB上限，增加启动余量与当前大显存进程结束检查；尚未启动GPU训练。 |
| 2026-10-23 23:11 至10-24 00:19 | server2接管全部剩余矩阵；基线400→920，900完整保存，两次同位置超时 | 原数据/源码/配置不变；源等待器退出；最新状态为失败待修复，尚无正式指标。 |
| 2026-10-24 15:05至15:46 | 修复第二个精确抽帧阻塞并从900恢复；基线训练完成、开发集评测中 | 两视频版本化无损覆盖；1354批、1353有效更新、1 AMP跳步；原清单/源码/配置不变。 |
| 2026-10-24 16:00 | 基线开发集完成，控制器已自动续跑TV，当前520批 | 500步新checkpoint已提交；基线1354完整保留。工作区工具配置与训练环境分别管理，未中断实验。 |
| 2026-10-24 16:40 | 按用户要求启用两组四卡并行并核查任务影响 | TV从完整900恢复于4–7，sigma_max在0–3已有真实更新及step100；首个并行尝试被预检拦截；未发现误停证据，其他任务退出原因仍待日志核查。 |

2026-10-24 16:42补充核对：两组仍为running，TV 1055/1354、sigma_max 225/1354；完整TV1000与sigma_max100 checkpoint的payload大小、训练源码合同及四rank状态已从源服务器核验。GPU2原有进程仍存在，早先10秒采样CPU计数持续增长；其他任务退出原因仍未取得日志确认。

**2026-10-24 16:52单seed范围变更**：用户明确只需一个seed。本轮仅保留seed50，当前两组训练不重启。输出目录新增execution_policy.json；已运行的旧控制器由不使用GPU的seed_policy_guard在selection产生后将promoted置空，原选择另存selection.before-single-seed.json，候选和融合选择不变；后续运维部署直接读取该策略，避免追加42/123。新增种子策略检查通过，运维检查共10项。按当前2–3秒/batch、1000样本开发集约10分钟和当前串行测试排程估算，余下训练约1.5–2小时，全流程约6–8小时；是假设不中断的时间估计，不是完成状态。

**2026-10-24 18:08并行评测更新**：legacy_va、TV和sigma_max的训练及开发集均完成，最后mean_tv_ta约1302/1354。按用户要求利用空闲卡，server2的0–3实际运行四个单卡测试缓存job；server1的0–3当前每卡约20–22GiB占用且计算繁忙，建立CPU容量等待槽位，满足29GiB预算+8GiB余量并连续检查后接力；server2的5–7在训练释放后接入同池。各job跨机独占，主矩阵稍后复用，不重复训练或评测。

所有候选、特征和ITM缓存计算调用原冻结函数；发布指标前须等全局selection并核对候选及融合参数与开发集预锁一致。源服务器旧FFmpeg2.8.6不用于新任务，两端统一NFS内7.0.2；同一MP3输出PCM字节哈希一致。运维12项检查、实际特征进度、跨机互斥和selection前指标暂缓检查通过。预计算不等于正式测试完成；单seed不变。

**2026-10-24 18:16核对**：mean_tv_ta已完成1354批并进入开发集，四组单seed训练全部完成。server2 GPU0–3、5–7共七条测试缓存/评测任务运行，GPU4用于最后一组开发集；server1 GPU0–3占用已升至约22–26GiB，四条接力槽位在CPU等容量。共有11条独立评测槽位，13项运维检查通过。第一轮扩展曾因扫描正在原子重命名的临时缓存文件被拦截，已跳过瞬时临时文件并成功重试；未重启现有模型作业。当前没有把缓存、等待状态当成完整测试结果。

**2026-10-24 21:39最终同步核对**：当前权威结果为[2026-10-24-final-seed50](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)。全矩阵19:05完成；7条server2评测槽位已正常结束。server1四条未占GPU的容量等待器已在最终整理时按身份核验后停止，未执行额外训练或评测。保留上方历史中断、修复及单seed预算变更记录。
