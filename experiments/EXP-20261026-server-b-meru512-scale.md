# 512D VAST：MERU式scale、曲率与温度对照

[返回实验总览](../README.md)

## 结果与完成状态

2026-10-26T14:43:59 UTC：17/17组全部完成30轮，每组9660次更新，合计164220次；0组失败。训练及协调器进程均已退出，没有MSRVTT微调或测试集评估。

[完整图文报告](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/REPORT_WITH_RADII.md) · [末轮CSV](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/final_epoch.csv) · [最佳轮次CSV](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/best_validation.csv) · [完整JSON](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/results.json) · [图件PDF](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/diagnostics.pdf)。

Markdown明细：[逐方向检索](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/DIRECTIONS.md) · [逐边几何与错配](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/GEOMETRY.md) · [scale与半径](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/PARAMETERS.md)。

半径分布补充：[初始化、末轮、最佳轮次的完整分布](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/RADIUS_DISTRIBUTIONS.md) · [分位数统计CSV](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/radius_distribution_statistics.csv) · [五页PDF](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/radius_distributions.pdf)。此前参数表和热力图只有均值，本补充展示每子集全部2048个验证视频的分布。

![第30轮原空间半径分布](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/radius_distribution_final.png)

小提琴为密度估计，箱体为P25–P75，须为P05–P95，黑横线为中位数，黑菱形为均值；末轮与最佳轮次图使用共同纵轴。补充报告另有无量纲半径sqrt(c)×r与q分布，区分不同曲率的尺度。分位范围是视频间差异，不是置信区间或跨seed不确定性。

以下为VAST验证集2048视频、第30轮、六方向macro R@1（%）。按本次用户明确要求只展示原始数值，不添加方法排名标记或优劣判断；完整CSV保留数值精度。

| 初始scale倍数 | M00：均固定 | M01：学温度 | M10：学曲率 | M11：两者均学 |
|---:|---:|---:|---:|---:|
| 0.5 | 11.93 | 12.49 | 11.93 | 12.54 |
| 1 | 14.58 | 14.95 | 14.58 | 14.97 |
| 2 | 15.67 | 15.80 | 15.79 | 15.95 |
| 4 | 15.75 | 16.02 | 15.83 | 16.26 |

C0独立半径头末轮macro R@1为18.66%。17组末轮父节点合法域覆盖均为100%，官方截断满足率与合法域满足率均为0%，九条边全部合法且满足率均为0%。逐方向和逐边数值见[方向CSV](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/directions.csv)与[边CSV](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/edges.csv)。

![训练与验证曲线](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/training_curves.png)

每行一个初始scale倍数；左为验证R@1，中为训练对比损失，右为未加权锥损失；均为512D、seed50。C0参考曲线在各行重复展示。

![原空间外角与开角](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/native_cone_angles.png)

本图使用各组验证检索最佳checkpoint，标题注明实际轮次；与上方末轮表分开读取。每组固定同一48个验证视频、九条边，坐标为原空间FP32外角与半开角，未用二维投影判定包含。

## 实验协议

| 项目 | 设置 |
|---|---|
| 编号 | EXP-20261026-server-b-meru512-scale |
| 数据 | VAST固定划分：82608训练、2048验证；复用84656条冻结pooled缓存 |
| 维度／种子 | 512D／seed50 |
| 条件 | C0；M00/M01/M10/M11 × 初始scale倍数0.5/1/2/4，共17组 |
| 参数化 | C0独立半径头，初始r=1；M组使用未归一化投影、每子集可学习scale和指数映射 |
| 共同初始化 | 投影无bias，标准差1/sqrt(input_dim)，共用CPU seed50权重；M组a=gamma/sqrt(512) |
| 曲率／温度 | M00均固定；M01仅温度可学习；M10仅曲率可学习；M11均可学习；初值1与0.07 |
| 目标 | 原九组对比pair、九条锥边；K=.1，锥权重=.1 |
| 预算 | 每组30轮、batch256、9660次更新；17组合计164220次更新 |
| 优化 | AdamW(.9,.98)，LR1e-4，483步warmup后cosine，wd=.01，clip=2；标量/bias无wd |
| 精度 | 投影AMP FP16；几何、损失、验证FP32；TF32关闭；官方原始epsilon=1e-8 |
| 数值失败 | 该条件停止并保留失败位置，不更改公式、精度或跳步继续 |
| 读出 | 30轮末轮主表；验证macro R@1最佳附表，同分R@5、较早轮，含epoch0 |
| 范围 | 仅VAST冻结头部训练及验证；不微调MSRVTT、不使用测试集 |

完整实现与命令见[本机README](../../Hyperbolic-Omnimodal/code/outputs/meru512_scale_pretrain_20261026/README.md)。

## 来源与验证

官方MERU版本`6d4430055f58354539f68668175135256f99d47f`；未修改的lorentz.py SHA256为`bd02210a14a4ca84c9eb24e7aad9b07ad42df5369d68124cf44d5ae07ba496f1`，未使用本地边界补丁。

本轮封存源码摘要：`e55adfdb597052cd0866f9c2aed661737c9096eb00c018cd8fb2396edb2ca5a4`。代码仓库基础HEAD为`8457b8e615837203f48d3c11957ae8777811a827`，但实际执行版本由独立源码哈希清单确定。

21项CPU/报告检查通过，包括共同初始化、参数更新、曲率梯度、官方非有限边界、恢复优化器和RNG、45GiB准入边界、最多16任务与缺失末轮读出。没有GPU profiling或独立试训；GPU检查发生在正式首批更新。

[可同步实现证据](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-implementation/)包含协议、21项检查、4096个训练样本的初始化审计、官方来源、源码清单和启动快照；哈希已登记到结果manifest。

## 运行与位置

- 协调器PID：1863665；启动于2026-10-26T14:27:34.543987 UTC。
- GPU0–7可用，每卡最多两个本轮任务。第一个真实更新后重新检查总占用≤45GiB、空闲≥48GiB才叠加第二个。
- 每进程40GiB上限，运行GPU余量8GiB，数据盘余量40GiB及检查点写入保护；只管理本轮已登记PID。
- 原始权重和结果：`/data0/xiaobo.xia/yuxuan.gao/meru512_scale_pretrain_20261026`。
- 命令、PID、GPU、日志与恢复事件：[本机日志目录](../../Hyperbolic-Omnimodal/code/outputs/meru512_scale_pretrain_20261026/logs/)。
- [单次运行索引](../runs/EXP-20261026-server-b-meru512-scale/README.md)。

以上PID为历史记录，均已退出。实际最大并发为16、每卡最多两组；最后一组M11_g4于14:35:10 UTC自动启动在GPU1。用户提出将剩余任务放在最低显存GPU后，在核对和安排叠加期间，该组已由原调度器启动，因此没有重复启动或迁移。每组PyTorch保留显存峰值为0.166–0.176GiB，不含全部CUDA上下文开销。[完成核验](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/completion_summary.json)与[运行审计](../results/EXP-20261026-server-b-meru512-scale/2026-10-26-results/run_audit.json)记录预算、哈希、实际dtype、准入与进程退出检查。

本机已成功fetch公开origin/main至`9cfce9f`；原工作区存在未提交改动及未合并的远端更新，本次保留原有内容，仅登记新实验。没有commit、push或上传。

## 结果口径与后续

合法域覆盖、官方截断满足率、合法对内满足率、合法且满足/全部配对分别展示。错配视频仅为配对控制，不当作人工非蕴含标签；仅一个训练seed。C0与M组的径向初始化不同，比较包含参数化与初始化影响。

本轮结束后只交付结果和权重。MSRVTT微调需用户后续明确要求，不自动创建任务。

## 变更记录

| 时间（UTC） | 事件 |
|---|---|
| 2026-10-26 14:27 | 封存源码并启动17组30轮VAST头部预训练 |
| 2026-10-26 14:28 | 16组真实更新确认，每卡两组，1组排队 |
| 2026-10-26 14:35 | 最后一组M11_g4自动启动在GPU1，17组全部已启动 |
| 2026-10-26 14:43 | 全部完成30轮；21项前置检查及全部运行结果核验通过，结果归档，未启动微调 |
| 2026-10-26 | 按用户要求新增纯Markdown主报告及三份明细，主入口统一改为Markdown；原始数值未变 |
| 2026-10-26 | 补充51份已存验证特征的半径分布、1071行统计和五页图件；新报告保留原结果表，旧均值版仍归档 |
