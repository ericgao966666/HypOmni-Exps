# 20261023T110614-server-b-train-vast_d64_s50_R3-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 已启动；2026-10-23T11:08:02.746392+00:00（UTC）；完成以DONE记录为准 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；沿用seed50/磁盘40GiB包装器 |
| 条件 | VAST / 64D / seed50 / R3 joint / MSRVTT10轮 / global batch64 / world size1 |
| 前置阶段 | VAST R3 warmup8轮及冻结30轮均已完成；继承冻结阶段最佳适配参数 |
| 数据与协议 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)，MSRVTT 7427/500/884；当前仅seed50 |
| 资源 | PID1913822；GPU7，与PMRL四卡任务的一个rank共享；file rendezvous |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__vast_d64_s50_R3__joint.log` |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/vast_d64_s50_R3/joint` |

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/seed50_only_20261023/train_seed50.py --method vast --dimension 64 --seed 50 --recipe R3 --stage joint --devices 7
```

用户明确要求GPU7单卡微调；保留GRAM3798136和PMRL1465285原进程，资源保护及每卡最多两个本任务rank保持。没有GPU测速。

2026-10-23T11:08:33.309227+00:00已核验正式优化步，详见[启动后证据](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-vast-joint-gpu7/progress.json)。
