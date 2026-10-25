# 20261023T063408-server-b-train-hyp_cone_d32_s50_R1-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 按用户要求暂停；2026-10-23T06:51:50.459985+00:00（UTC），保留第1轮断点 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；外部seed50-only包装入口 |
| 执行范围 | [仅seed50与指定单卡布局](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/execution_scope.json) |
| 协议与数据 | [历史封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)，种子和指定布局以新执行范围覆盖；MSRVTT 7427/500/884 |
| 条件 | hyp_cone / 32D / seed50 / R1 / joint / 30轮 / global batch64 / world size1 |
| 布局变化 | 该条件尚未开始时由原计划world size2改为1；全局batch样本顺序不变，实际随机流可能受rank数影响 |
| 资源 | PID2847813；GPU2，与VAST的对应rank共享；file rendezvous |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__hyp_cone_d32_s50_R1__joint.log` |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/hyp_cone_d32_s50_R1/joint` |
| 证据 | [实际优化步](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/progress.json) |

从既定共同初始化开始；64D已选定R1。用户明确取消多seed，此条件只运行seed50；不改变global batch或训练轮数。未做GPU测速。

2026-10-23T06:51:50.459985+00:00：用户要求先完成64D，本条件暂停，完整第1轮checkpoint保留。后续仍以world size1恢复。
