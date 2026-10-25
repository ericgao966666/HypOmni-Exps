# 20261023T070240-server-b-train-pmrl_d64_s50_R3-warmup

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 运行中；2026-10-23T07:05:41.961669+00:00（UTC），第6轮真实更新已确认 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；沿用seed50/磁盘40GiB训练包装器 |
| 条件 | PMRL / 64D / seed50 / R3 warmup / 8轮 / global batch256 / world size4 |
| 恢复 | 第5轮step1610，恢复optimizer/scaler及四rank RNG；旧未保存第6轮重跑 |
| 资源 | PID1290393；GPU1/2/6/7；与VAST共享1/2、与GRAM共享6；file rendezvous |
| 数据与协议 | [历史封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)，VAST 82608/2048/2051；当前仅seed50 |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/pmrl_d64_s50_R3/warmup` |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__pmrl_d64_s50_R3__warmup.log` |
| 证据 | [GPU分配和优化步](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-pmrl-gpu1267/progress.json) |

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/seed50_only_20261023/train_seed50.py --method pmrl --dimension 64 --seed 50 --recipe R3 --stage warmup --devices 1,2,6,7
```

用户要求新增指定四卡组；既有VAST、GRAM原进程保留，未做测速。之前PMRL停滞根因尚未确诊，此次从完整断点恢复。
