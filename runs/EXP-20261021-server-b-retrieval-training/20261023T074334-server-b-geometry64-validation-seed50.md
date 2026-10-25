# 20261023T074334-server-b-geometry64-validation-seed50

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 类型与服务器 | 事后验证集几何分析，server-b；没有新增模型训练 |
| 状态与核对时间 | 已完成；2026-10-23T07:57:10.139145+00:00（UTC） |
| 模型 | 双曲有锥64D、seed50、R0/R1/R2/R3；各方案按检索选出的checkpoint，epoch5/26/9/7 |
| 数据 | 相同500个验证视频；投影固定48视频×7子集336点；未读取最终测试特征 |
| 算法 | 复用作者HoroPCA500步、CO-SNE1000步，投影seed50；完整参数和原作者commit见[来源](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/provenance.json) |
| 分析代码 | `Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/analysis/geometry_validation_20261023/analyze_recipes.py`；SHA256 `a79e43e64a546be7c222ea10efcd1fc8096375dae685ce0b52c78d9ab10152d0` |
| R0提取 | PID2280859，GPU7，16GiB上限；实际峰值5.709GiB，500样本指标复算误差0；进程已退出 |
| 投影计算 | PID2757553，CPU2线程，已退出 |
| 原始特征 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/analysis/geometry_validation_20261023`仅存R0补提取；R1–R3复用训练输出 |
| 日志 | 分析目录的 `extraction.log`、`projection.log` |
| 结果 | [图文总览](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/README.md) · [四页PDF](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-geometry-validation/geometry_validation_report.pdf) |

R3呈明显径向分层：单/双/三模态均值约1.265/1.679/3.168；R1/R2仍主要接近半径1。所有方案原空间严格锥满足率仍0%。颜色表示子集类型，不是语义类别；二维投影不能代替原空间约束检验。正式训练任务未修改或重启。
