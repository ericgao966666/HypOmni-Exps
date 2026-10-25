# 20261023T064848-server-b-train-gram_d64_s50_R3-frozen

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 运行中；2026-10-23T06:51:50.459985+00:00（UTC），已验证真实优化步 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；沿用seed50训练入口与磁盘40GiB包装器 |
| 条件 | GRAM / 64D / seed50 / R3 frozen / 30轮 / global batch256 / world size4 |
| 恢复 | 第16轮step5152；optimizer/scaler及四rank RNG恢复，未保存的第17轮重跑 |
| 数据与协议 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；VAST 82608/2048/2051；执行范围仅seed50 |
| 资源 | PID3798136；GPU3/4/5/6，暂与旧VAST在GPU3/4共享；file rendezvous |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__gram_d64_s50_R3__frozen.log` |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/gram_d64_s50_R3/frozen` |
| 证据 | [实际更新及当前布局](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-priority64-gpu3to6/progress.json) |

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/seed50_only_20261023/train_seed50.py --method gram --dimension 64 --seed 50 --recipe R3 --stage frozen --devices 3,4,5,6
```

此前因数据盘80GiB保护暂停；用户将保护线降至40GiB并要求GPU3–6优先续跑64D后恢复。训练参数不变。
