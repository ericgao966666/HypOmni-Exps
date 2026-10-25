# 20261023T034825-server-b-train-vast_d64_s50_R3-frozen

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 运行中；2026-10-23T03:50:48.088951+00:00（UTC），已验证第25轮实际参数更新 |
| 源码 | 独立封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原代码仓库含未提交改动 |
| 运行时覆盖 | [40GiB资源策略与包装器哈希](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-disk40/runtime_policy.json)；只覆盖检查点磁盘保护，不改变训练算法 |
| 协议与数据 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；VAST train/val/test=82608/2048/2051 |
| 条件 | VAST，64D，seed50，R3 frozen，30轮，global batch256，world size4 |
| 恢复 | 从第24轮step7728的last.pt恢复优化器、scaler、四rank RNG；未保存的第25轮重跑 |
| 资源 | PID856070；GPU1/2/3/4；file rendezvous |
| 原始输出 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/vast_d64_s50_R3/frozen` |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__vast_d64_s50_R3__frozen.log` |
| 证据 | [启动与优化步](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-disk40/progress.json) |

启动命令：

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/disk40_20261023/train_disk40.py --method vast --dimension 64 --seed 50 --recipe R3 --stage frozen --devices 1,2,3,4
```

前次同条件运行因数据盘低于80GiB暂停。用户将保护线调整为40GiB后恢复，不重置已保存的训练进度。最终测试未开始。
