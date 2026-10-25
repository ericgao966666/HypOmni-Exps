# 20261024T081258-server-b-train-pmrl_d64_s50_R3-frozen

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 运行中；2026-10-24T08:16:46.953317+00:00（UTC），已确认第9轮实际更新 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；资源控制在外部覆盖 |
| 条件 | PMRL / 64D / seed50 / R3 frozen / 30轮 / global batch256 / world size4 |
| 恢复 | 第8轮step2576的last.pt；原优化器/scaler及四rank RNG恢复，未保存的第9轮重跑 |
| 资源 | PID1649042，GPU1/2/6/7；GRAM原进程1639066在GPU5并行；file rendezvous |
| 数据与协议 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)，当前仅seed50 |
| 原始输出 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/pmrl_d64_s50_R3/frozen` |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__pmrl_d64_s50_R3__frozen.log` |
| 证据 | [实际优化步与资源](../../results/EXP-20261021-server-b-retrieval-training/2026-10-24-pmrl-recovery/progress.json) |

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/seed50_only_20261023/train_seed50.py --method pmrl --dimension 64 --seed 50 --recipe R3 --stage frozen --devices 1,2,6,7
```

此前16:09启动显存准入失败，原失败记录保留。用户要求立即并行恢复，本次重新排队；未更改模型、数据、训练轮数和全局batch。
