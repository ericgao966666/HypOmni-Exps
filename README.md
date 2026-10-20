# 实验总览

这里统一记录研究问题、实验状态、主要结论和结果位置。通常一个研究问题对应一张实验卡；同一问题的种子、消融、失败重试和续跑放在卡内。历史基线与方法探索可按章节汇总，如 EXP-001。原始配置、日志和 checkpoint 保留在项目输出目录，主要结果表与精选分析图另存为本仓库可同步快照。

首批整理范围：2026-10-13 至 2026-10-20；现已补入 2026 年 8–9 月的零样本基线与方法探索。最后核对：2026-10-20，Asia/Shanghai。其他更早实验尚未系统补录；交接到其他服务器的任务，只记录当前能核实的交接状态。

本目录是独立 Git 仓库，分支为 `main`，远端为 [ericgao966666/HypOmni-Exps](https://github.com/ericgao966666/HypOmni-Exps)。两台服务器的使用方式见[同步说明](SYNC.md)，维护规则见 [AGENTS.md](AGENTS.md)。本地内容是否已经推送，以 Git 分支状态和远端提交记录为准。

快捷入口：[可同步结果](results/README.md) · [单次运行记录](runs/README.md) · [本机路径配置](config/README.md)

## 当前关注

- **已观察到的收益**：[MSRVTT 端到端微调](experiments/EXP-006-msrvtt-finetune.md)六方向平均 R@1 达到 24.87%，超过本轮最强基线 VAST 3.88 个百分点，主要来自视频与音频方向。
- **尚未解决的问题**：[子集层级机制](experiments/EXP-003-subset-mechanisms.md)与[几何对照](experiments/EXP-007-coco-geometry.md)仍未证明严格层级包含的成功；[音频迁移](experiments/EXP-005-transfer-diagnostics.md)随头部训练下降。
- **等待结果回填**：[区域层级实验](experiments/EXP-008-region-geometry.md)与[低维端到端实验](experiments/EXP-009-lowdim-finetune.md)已交接，目标服务器后续训练状态待核实。

## 实验目录

| 编号 | 研究问题 | 项目 | 最近实验记录 | 状态 | 当前判断 |
|---|---|---|---|---|---|
| EXP-001 | [历史零样本基线与方法探索](experiments/EXP-001-zero-shot-baselines.md) | PMRL-minimal-hyperbolic / Hyperbolic-Omnimodal | 08–09；10-14 | 历史评估完成；Parent 仅验证 | 视频 Top-50 均值持平，音频 direct 下降；旧 Parent 消融置于文末 |
| EXP-002 | [子集配对数量与约束强度](experiments/EXP-002-subset-pilot.md) | Hyperbolic-Omnimodal | 10-16 | 初版停止；后续消融完成 | 9 对弱约束检索较好，未解决严格包含；已附四张几何审计图 |
| EXP-003 | [温度与训练机制能否兼顾检索和层级](experiments/EXP-003-subset-mechanisms.md) | Hyperbolic-Omnimodal | 10-16 | 已完成 | 57 次正式运行，未通过双目标验收 |
| EXP-004 | [官方权重与本地模型的冻结迁移能力](experiments/EXP-004-frozen-transfer.md) | Hyperbolic-Omnimodal | 10-16 至 10-17 | 已完成 | 视频音频较强，音频文本迁移较弱 |
| EXP-005 | [音频迁移下降发生在哪个阶段](experiments/EXP-005-transfer-diagnostics.md) | Hyperbolic-Omnimodal | 10-17 | 已完成探索性诊断 | 第一轮已下降，多种目标均受影响 |
| EXP-006 | [统一微调预算下的 MSRVTT 表现](experiments/EXP-006-msrvtt-finetune.md) | Hyperbolic-Omnimodal | 10-17 | 已完成含续跑 | Ours 24.87%，领先 VAST 3.88 pp |
| EXP-007 | [负曲率是否带来额外层级能力](experiments/EXP-007-coco-geometry.md) | meru-width-coco | 10-17 | 已完成并修正读出 | 小幅检索收益，无明确层级优势 |
| EXP-008 | [区域监督下的欧氏与双曲对照](experiments/EXP-008-region-geometry.md) | meru-width-coco | 10-19 | 已交接；目标状态待核实 | 数据准备完成，尚无本机正式结果 |
| EXP-009 | [低维空间是否放大几何差异](experiments/EXP-009-lowdim-finetune.md) | Hyperbolic-Omnimodal | 10-19 | 已交接；目标状态待核实 | 56 次运行协议完成，尚无正式结果 |

“已完成”指卡内声明的运行与评估完成，不代表假设成立，也不代表证明收敛。运行预算、验证集结果、测试集结果分别记录。

## 数据与基础设施

| 编号 | 工作 | 状态 | 对实验的影响 |
|---|---|---|---|
| OPS-001 | [VAST 150k 缺失媒体恢复](operations/OPS-001-vast-recovery.md) | 最近进度文件报告运行中 | 可用样本仍在增加；已冻结实验不能自动换用新 manifest |

## 周度回顾

- [2026 年 10 月 13 至 20 日](weekly/2026-10-13_2026-10-20.md)

## 如何维护

1. **开始新实验**：从[模板](templates/experiment.md)建卡；保留已有 EXP 编号，跨服务器新增时使用 `EXP-YYYYMMDD-server-a-名称` 等含服务器别名的唯一编号，避免双方取到同一个序号。写清问题、基线、唯一变量、数据划分、选择规则和预算，再更新目录。
2. **开始运行**：按 [run 模板](templates/run.md)新增独立记录，补上精确 run ID、服务器、协议与配置、源码版本或快照、输出目录，以及记录命令/PID/GPU/日志的运行清单。不要把凭据或带凭据的命令复制进卡片。
3. **运行变化**：在同一卡片追加失败、重试、续跑和交接记录。修改数据、目标函数或评测协议时登记新版本；若研究问题也改变，另建关联卡片。
4. **结束实验**：核对完成标记和结果表，写主要指标、结论、局限、下一步；状态与目录同步更新。负结果同样保留。
5. **周度整理**：按请求或本次实验工作需要更新周报，链接实验卡，避免维护多份完整结果表。这里没有后台自动监控或定时更新任务。

新实验可用状态：计划中、准备中、运行中、已停止、失败待修复、已完成、已交接。运行中状态必须带最后核对时间；历史停止原因不能被新状态覆盖。

数字以链接的机器结果为依据，本仓库快照通过来源清单与 SHA-256 对应原始文件。卡片负责解释和定位；若修正评测，标明当前权威版本并保留旧版本。六方向与十二方向平均、验证与测试、固定末轮与验证最优 checkpoint、样本 bootstrap 与训练种子不确定性不得混用。

当前多个 `outputs/` 目录是指向 `/data-nfs/xiaoboxia/YuxuanGao/local-storage-20261019/` 的符号链接，目录存在不表示结果仍存于本机磁盘。迁移路径时同步检查卡片链接。
