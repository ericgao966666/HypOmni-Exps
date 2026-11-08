# MSRVTT：VAST子集head预训练是否帮助目标域微调

[返回实验总览](../README.md) · EXP-20261107-server-b-msrvtt-head-init · 方案确认：2026-11-07 UTC；执行准备核对：2026-11-08 UTC

**尚无正式结果，待验证。** 比较原始VAST加新双曲head直接微调，与原始VAST加VAST-150k第5轮head迁移微调。两种初始化分别覆盖K=0.1、0.2、0.5，共6组；目标域预算统一为2轮head＋8轮联合，不早停。计划先同步，随后在server-b启动；发布计划不代表训练已经启动。

## 研究问题与关键设置

已有VAST子集训练的外部曲线提示联合训练后期迁移退化，但不能把原因单独归于head。新实验隔离head初始化，检验其对MSRVTT检索和严格锥包含的影响。

| 设置 | 本轮口径 |
|---|---|
| 数据 | MSRVTT train/val/test=7427/500/884，ID互斥；884视听齐全测试视频，与上一轮相同，不是完整MSRVTT-1K |
| 初始化 | fresh：原始VAST＋固定seed50新head；vast_head5：同一VAST＋对应K的VAST第5轮head，仅继承模型参数 |
| 几何 | 512D，测地线对齐，λ=0.2，曲率和温度可学习，沿用物理半径参数化 |
| K/η/α | 0.1/0.7/0.05；0.2/0.7/0；0.5/1.0/0；每K两种初始化参数相同，不重新搜索 |
| 预算 | seed50，全局batch64，4卡/组；116步/轮，2+8轮，共1160次MSRVTT更新，无指标早停 |
| 评测 | epoch0及每轮完整验证；T↔VA双向等权ITC/ITM、候选R@32及严格几何；own-Top32纯ITM重排 |
| 选模 | 仅MSRVTT验证集选检索主模型与双目标辅助模型，允许epoch0；全部6组固定预算完成并锁定后读取正式测试 |
| 测试 | MSRVTT及VAST/VATEX/ActivityNet/DiDeMo；MSRVTT额外epoch0/2/10诊断 |

完整训练、选模、保存及资源规则见[研究协议](details/PROTOCOL-20261107-msrvtt-head-init.md)。现有三份迁移head和初始投影哈希已核验。旧VAST固定15轮队列在2026-11-07已完成；本轮不恢复或修改旧训练。

## 主要结果

尚无正式结果。完成后按K列出两种初始化的验证选定epoch、MSRVTT及外部集ITC/ITM和几何指标，报告同K差值。缺失结果不填零。

## 解释与限制

- 比较的是相同MSRVTT预算下的初始化效果；迁移组额外经历1610次VAST head更新，总训练预算不相等。
- η/α来自既有VAST验证选择，跨K比较是成套参数比较，不能归因于K单一变量。
- 只有seed50；样本bootstrap不能替代多训练种子，不将差值表述为稳定提升。
- MSRVTT域内改善不代表跨数据集泛化改善；外部测试不用于重新调参或选轮次。
- 双目标合格仅表示通过本协议相对门槛，不代表全部九边建立合法层级。
- 同VAST起点的原生VAST/GRAM/PMRL为后续对照，本机本轮只启动6组双曲实验。

## 本地证据与执行入口

源代码：`<WORKSPACE>/Hyperbolic-Omnimodal/code/experiments/msrvtt_geodesic_2plus8_20261107/`；输入、协议、checkpoint与结果：`<DATA_ROOT>/msrvtt_geodesic_2plus8_20261107/`。确切源码以封存的源码快照和SHA-256为准，不能用当前仓库HEAD冒充执行版本。

运行记录存本地`runs/EXP-20261107-server-b-msrvtt-head-init/`。PID、设备、空间清理、重试和资源暂停不放入结果表。原始CSV/JSON与曲线只存本地，GitHub同步本卡及研究协议。
