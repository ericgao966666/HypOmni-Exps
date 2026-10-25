# 20261022T062336-server-b-train-hyp_cone_d64_s52_R0-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 运行中，2026-10-22T06:25:03.327169+00:00（UTC）；完成以原始DONE记录为准 |
| 实际源码 | 独立快照 `Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021`；摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动 |
| 数据与协议 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；MSRVTT 7427/500/884；VAST 82608/2048/2051 |
| 条件 | hyp_cone / 64D / seed52 / R0 / joint / 10 epochs / global batch 64 |
| 资源 | PID 3513130；GPU 6；file rendezvous |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__hyp_cone_d64_s52_R0__joint.log` |
| 原始输出 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/hyp_cone_d64_s52_R0/joint` |

启动命令：

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/retrieval_train.py --method hyp_cone --dimension 64 --seed 52 --recipe R0 --stage joint --devices 6
```

按验证集选checkpoint；测试不参与筛选。R0 seed51/52对照从既定共同初始化开始，提前调度不改变预算。PMRL warmup不受本次接管重启。
