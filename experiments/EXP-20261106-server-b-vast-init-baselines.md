# 共同VAST初始化与固定15轮（无早停）下的原生基线比较

[返回实验总览](../README.md) · EXP-20261106-server-b-vast-init-baselines · 方案核对：2026-11-06 UTC；原版结果核对：2026-11-08 21:08；重跑暂停核对：2026-11-08 23:30；产物复核与文档更新：2026-11-10，Asia/Shanghai

**原固定15轮的三方法及15项测试已完成；保留全部逐轮模型的重跑版已按用户要求暂时停止，尚无新正式结果。** 在固定视听交集、验证选模的单seed测试中，MSRVTT双向平均ITM R@1为GRAM44.06%、VAST43.55%、PMRL40.21%；GRAM比VAST高0.51pp。VAST在VAST test、VATEX和ActivityNet上较高，GRAM在MSRVTT和DiDeMo上较高；单seed不能据此声称稳定优势。逐轮评估使用VAST验证集，五数据集正式测试仅评估每种方法验证选出的一个主checkpoint。

11-10只读复核原版三份训练完成状态、15项测试完成标记/结果及两份汇总CSV，结果口径与下表一致。keepall队列文件仍记载11-08的`paused_by_user`、无自动重启；此次仅重读持久化记录，未重新核实server2进程。该重跑按最后已核实状态记为暂停，不能因本次文档更新而改成运行中或完成。

固定协议与原发布版安装见[完整操作指南](../operations/OPS-20261106-native-baselines-fixed15.md)。本次保留全部模型的重跑使用单独封存代码，具体启动以本地keepall运行记录为准；原发布版仍有模型裁剪。实验卡记录科学问题与结果口径，实际服务器别名、PID、路径和启停过程在目标端本地run中记录。

## 研究问题与关键设置

研究问题：消除GRAM/PMRL各自已训练权重的起点差异，并对齐head适配与联合训练阶段后，三种方法在同一VAST划分及固定五数据集上的检索表现有何不同？与当前测地线实验对照时，哪些差异仍来自目标、head结构或ITM设计？

| 影响结果解读的设置 | 本轮口径 |
| --- | --- |
| 初始化 | 三方法均使用VAST `model_step_204994.pt`；公共编码器、兼容投影头和ITM沿用该权重，Adam从零开始 |
| 数据与划分 | VAST train/val/test 82608/2048/2051，按源视频隔离；固定manifest、caption和样本顺序，不在目标端重划分 |
| 外部测试 | MSRVTT 884、VATEX 1224（12240 queries）、ActivityNet 3987、DiDeMo 995；固定视听交集，保留全部指定caption |
| 输入 | 2个中点视频帧、1个确定性音频窗、40个文本token、无字幕、512D |
| 预算与种子 | seed50、global batch256、每轮322步；5轮head/1610步＋10轮joint/3220步，总4830步，固定15轮、无早停 |
| head阶段 | VAST更新t/va头和温度；GRAM更新t/v/a头和温度；PMRL更新t/v/a头，tau1/tau2固定；编码器和ITM冻结 |
| 联合阶段 | 承接head及Adam状态，解冻有效视觉/音频/共享BERT、ITM及相关输入投影；使用原生对齐目标＋0.1倍原生ITM |
| 目标差异 | VAST为T–VA对比；GRAM为Gram体积对比；PMRL为谱内＋全局batch谱间损失，tau1=.05、tau2=.1 |
| 选模与测试 | 完成固定15轮后，在epoch6–15中按验证ITM R@1、ITC R@1、较早epoch选主模型；不看测试成绩选模 |
| 指标 | T↔VA双向ITC R@1/5/10、候选R@32、自身Top32上的纯ITM重排；漏召回计miss，不融合分数 |

研究协议与完整超参数见[固定代码提交中的protocol](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/1070647727351499089ada891d1136eff208bde3/portable_baselines/protocol.json)。验证每轮进行ITC，epoch0/5及每个联合epoch6–15进行ITM。学习率保留旧日程前15轮，不压缩cosine；没有基于指标的早停。详见[共同协议](details/PROTOCOL-20261106-fixed15-no-early-stop.md)。

## 协议修订

最初5+25代码提交 `ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2` 与[旧操作指南](../operations/OPS-20261106-native-baselines-5plus25.md)保留。用户在观察测地线验证退化后明确要求固定15轮、不要早停；本卡当前方案同步该修订。本机旧5+25运行曾继续到第24/25轮，现已停止并保留历史。新版采用独立代码与输出，各方法仅继承经验证等价的前8轮状态，后续旧轮更新不混入新版。GRAM/PMRL已完成；11-08用户允许VAST在server2继续，同样使用独立输出。

11-08用户进一步要求永久保留每轮checkpoint并在server2重跑三方法。重跑版采用独立代码和输出，从各自第8轮末2576步的完整模型/Adam/AMP/四rank RNG恢复，重新执行第9–15轮/2254次更新；前5轮head快照和第6–8轮模型从经核验的归档导入。联合epoch6–15的模型全部保留，`last.pt`仍为滚动完整恢复点且末轮不删除。目标、数据、seed50、global256、学习率前缀、15轮预算和验证选模规则不变；每个方法完成后自动核对旧版保留模型与新模型的逐tensor差异，并在新目录执行主模型五集测试。旧版结果继续独立保存，重跑不作为独立seed或额外训练预算的性能对照，也不事先声明逐位重现。 用户随后要求让出server2资源，重跑队列与当前训练已安全暂停，完整恢复点和已生成模型均保留；后续等待明确恢复指令。

## 主要结果

以下是原固定15轮三方法的正式测试，指标为T↔VA双向平均纯ITM R@1（%，越高越好）；使用各自Top32候选、漏召回计miss、不融合ITC分数。完成15轮后仅按验证ITM、ITC和较早epoch选择主模型。排名不代表统计显著性，保留全部checkpoint的重跑结果尚未混入本表。

| 方法 | 验证选定epoch | VAST test | MSRVTT | VATEX | ActivityNet | DiDeMo |
|---|---:|---:|---:|---:|---:|---:|
| VAST | 11 | **53.34** | <ins>43.55</ins> | **80.76** | **40.77** | <ins>41.31</ins> |
| GRAM | 11 | <ins>52.71</ins> | **44.06** | 79.96 | <ins>40.54</ins> | **42.01** |
| PMRL | 12 | 52.32 | 40.21 | <ins>80.22</ins> | 40.46 | 39.85 |

固定测试规模：VAST2051、MSRVTT884、VATEX1224视频/12240查询、ActivityNet3987、DiDeMo995；不是论文完整标准测试集。三方法均已完成4830步及各五项测试；GRAM/PMRL于11-07 17:11前后完成，VAST于11-08 20:40完成（Asia/Shanghai）。

完整ITC/ITM及R@1/5/10原始结果分别保留在本地`native_baselines_fixed15_seed50_20261107/`（GRAM/PMRL）和`native_baselines_fixed15_vast_seed50_20261108/`（VAST）的`evaluation/`与`reports/tests.csv`下，路径相对本机数据根。15份测试完成标记、结果JSON哈希和验证选定checkpoint身份已核对；单seed不估计训练种子方差。

## checkpoint验证与测试覆盖

训练期间使用固定VAST **val 2048条**评估和选模；正式VAST **test 2051条**与四个外部测试集分开。每轮有ITC验证，epoch0/5及联合epoch6–15有ITM验证。完成15轮后，仅将验证选出的主checkpoint用于VAST test、MSRVTT、VATEX、ActivityNet、DiDeMo；其他checkpoint不逐一执行这五项测试，末轮15和ITC最佳模型也不自动追加测试。

| 方法 | 新fixed15输出中的完整ITC＋ITM验证 | 五数据集正式测试使用的checkpoint | 已完成测试 |
|---|---|---|---|
| GRAM | epoch6–15，每轮VAST val 2048条 | epoch11，验证选定 | VAST test＋四个外部集，5/5 |
| PMRL | epoch6–15，每轮VAST val 2048条 | epoch12，验证选定 | VAST test＋四个外部集，5/5 |
| VAST | epoch6–15，每轮VAST val 2048条 | epoch11，验证选定 | VAST test＋四个外部集，5/5 |

上表为原fixed15输出的评测覆盖。迁移继承部分的epoch0–5验证保留在旧输出`native_baselines_5plus25_seed50_20261106/runs/<method>/validation/`：epoch0/5有ITC＋ITM，epoch1–4仅ITC。三方法epoch6–8已在各fixed15输出重新完整补评；之后的验证来自各自续训。原版曾按验证排名裁剪模型文件，所以指标齐全不等于所有权重仍在。当前重跑版用于补齐并永久保留逐轮模型；仍只对验证选出的主模型执行五集正式测试，没有自动扩展为逐checkpoint的四外部集测试。

## 解释与局限

- 与[此前30轮四方法实验](EXP-20261103-server-a-joint30-five-datasets.md)相比，本轮同时改变GRAM/PMRL初始化与阶段安排，不能把新旧差值解释为单一因素效应。
- 当前测地线模型有新初始化的七子集几何head，并做过额外head超参数搜索；原生基线的head结构与搜索预算不同。共同VAST主干初始化和相同4830步不能等同于所有参数起点或总计算量完全一致。
- 三个原生基线保留1正2负的原生ITM采样；当前几何方法使用1:1均匀异来源负例，ITM设计仍存在差异。
- 原生基线没有原生entailment cone，不把几何锥指标强加给它们。检索与几何结论分别解释。
- 单seed不能估计训练种子不确定性；固定视听交集与简化输入不等于论文完整榜单协议。VAST保留划分只保证不参加本轮追加训练，不能保证作者历史预训练未见过这些媒体。
- 默认每方法4卡；目标GPU布局、精度和环境需要在本地run中记录并重新预检，不保证跨硬件逐位相同。 server2按用户授权与现有任务共用GPU，使用42GiB上限并按空闲显存与2GiB余量自适应；运行适配和资源策略单独入档，耗时不视为同等独占条件下的速度比较。

## 下一步判断

待用户明确恢复后，从各自最新完整断点继续三方法重跑，核验全部联合epoch模型文件及SHA，核对原版保留模型与重跑模型是否逐tensor一致。随后报告新目录的验证选模与五集测试，并明确它们与原版结果的关系；不把单seed重跑当作训练种子方差估计。

## 完整结果与来源

- [新服务器完整操作指南](../operations/OPS-20261106-native-baselines-fixed15.md)
- [代码固定提交](https://github.com/ericgao966666/Hyperbolic-Omnimodal/tree/1070647727351499089ada891d1136eff208bde3/portable_baselines)；分支 `native-baselines-vast-init-fixed15-20261106`。
- [固定manifest索引](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/1070647727351499089ada891d1136eff208bde3/portable_baselines/manifests/index.json)、[源端实际验证边界](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/1070647727351499089ada891d1136eff208bde3/portable_baselines/TESTING.md)。完整哈希清单在代码包中。
- GRAM/PMRL本地输出：`native_baselines_fixed15_seed50_20261107/`（相对本机数据根），已产生`reports/REPORT.md`、`reports/validation.csv`、`reports/tests.csv`以及两方法的`runs/`与`evaluation/`结果。
- VAST独立输出：`native_baselines_fixed15_vast_seed50_20261108/`（相对本机数据根），已完成训练、epoch6–15验证及五项正式`evaluation/`测试。
- 保留全部模型的重跑输出：`native_baselines_fixed15_keepall_seed50_20261108/`（相对本机数据根）；代码从固定提交派生，封存源码、补丁和逐文件哈希位于本地`native_baselines_fixed15_keepall_20261108/`与代码目录`.local/`。重跑版独立报告`CHECKPOINT_ARCHIVE.json`与`REPLAY_AUDIT.json`。
- 当前状态入口：本地`config/native_baselines.current.local.json`。各方法运行、重跑和迁移记录位于本地`runs/EXP-20261106-server-b-vast-init-baselines/`；旧版已完成结果与新版队列分别记录。
