# 共同VAST初始化与固定15轮（无早停）下的原生基线比较

[返回实验总览](../README.md) · EXP-20261106-server-b-vast-init-baselines · 方案核对：2026-11-06 UTC；文档更新：2026-11-06

**尚无本轮正式结果。** 本实验将VAST、GRAM、PMRL的预训练起点统一为同一份VAST checkpoint，并统一为5轮对齐head适配＋10轮联合训练，用于比较不同原生对齐目标在共同起点和阶段预算下的检索表现。迁移代码已发布，目标服务器的完整预检、三组训练和15项测试仍待运行；源端功能检查不构成性能结论。

新服务器可直接按[完整操作指南](../operations/OPS-20261106-native-baselines-fixed15.md)执行。实验卡只记录科学问题与结果口径；实际服务器别名、PID、路径和启停过程在目标端本地run中记录。

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

最初5+25代码提交 `ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2` 与[旧操作指南](../operations/OPS-20261106-native-baselines-5plus25.md)保留。用户在观察测地线验证退化后明确要求固定15轮、不要早停；本卡当前方案同步该修订。目标端是否已启动旧版未核验，旧任务不自动切换，新版必须使用新目录和新输出。

## 主要结果

尚无目标服务器的正式训练或测试结果，因此暂无方法排名和性能差值。待三组完成固定15轮预算、验证选定主模型的15项测试齐全后回填；CPU/GPU功能检查、发布成功和训练启动均不填作研究结果。

## 解释与局限

- 与[此前30轮四方法实验](EXP-20261103-server-a-joint30-five-datasets.md)相比，本轮同时改变GRAM/PMRL初始化与阶段安排，不能把新旧差值解释为单一因素效应。
- 当前测地线模型有新初始化的七子集几何head，并做过额外head超参数搜索；原生基线的head结构与搜索预算不同。共同VAST主干初始化和相同4830步不能等同于所有参数起点或总计算量完全一致。
- 三个原生基线保留1正2负的原生ITM采样；当前几何方法使用1:1均匀异来源负例，ITM设计仍存在差异。
- 原生基线没有原生entailment cone，不把几何锥指标强加给它们。检索与几何结论分别解释。
- 单seed不能估计训练种子不确定性；固定视听交集与简化输入不等于论文完整榜单协议。VAST保留划分只保证不参加本轮追加训练，不能保证作者历史预训练未见过这些媒体。
- 默认每方法4卡；目标GPU布局、精度和环境需要在本地run中记录并重新预检，不保证跨硬件逐位相同。

## 下一步判断

按操作指南在目标服务器校验固定输入与共同初始化，完成目标GPU/global256预检，再进行三方法固定5+10训练与验证选模后的测试。获得同口径结果后比较共同初始化下各目标的表现，并单列与几何方法的剩余可比性限制。

## 完整结果与来源

- [新服务器完整操作指南](../operations/OPS-20261106-native-baselines-fixed15.md)
- [代码固定提交](https://github.com/ericgao966666/Hyperbolic-Omnimodal/tree/1070647727351499089ada891d1136eff208bde3/portable_baselines)；分支 `native-baselines-vast-init-fixed15-20261106`。
- [固定manifest索引](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/1070647727351499089ada891d1136eff208bde3/portable_baselines/manifests/index.json)、[源端实际验证边界](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/1070647727351499089ada891d1136eff208bde3/portable_baselines/TESTING.md)。完整哈希清单在代码包中。
- 目标端本地：`<output_root>/reports/REPORT.md`、`<output_root>/reports/validation.csv`、`<output_root>/reports/tests.csv`、`<output_root>/runs/`与`<output_root>/evaluation/`。尚未声明这些产物已经产生。
- 实验仓库本地run记录：`runs/EXP-20261106-server-b-vast-init-baselines/`；目标执行服务器以实际run字段为准，不从建卡编号推断。
