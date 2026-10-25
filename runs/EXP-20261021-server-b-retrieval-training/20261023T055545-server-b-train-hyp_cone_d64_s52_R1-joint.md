# 20261023T055545-server-b-train-hyp_cone_d64_s52_R1-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 已按用户要求停止；2026-10-23T06:36:13.810302+00:00（UTC），保留第4轮断点 |
| 实际源码 | 封存快照 `Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021`；摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动 |
| 运行时覆盖 | [指定同卡许可与包装器哈希](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-overlay-seed52/runtime_policy.json)，复用数据盘40GiB写入保护 |
| 选择依据 | [seed50四候选验证结果](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-early-selected/selection.json)，R1按原规则锁定 |
| 数据与配置 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；MSRVTT 7427/500/884 |
| 条件 | 双曲有锥 / 64D / seed52 / R1 / joint / 30轮 / global batch64 / 单卡 / λ=.1 |
| 资源 | PID456697；GPU1，与VAST PID856070的一个rank共享；file rendezvous |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/hyp_cone_d64_s52_R1/joint` |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__hyp_cone_d64_s52_R1__joint.log` |
| 运行证据 | [实际优化步与GPU分配](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-overlay-seed52/progress.json) |

启动命令：

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/overlay_seed52_20261023/train_overlay.py --method hyp_cone --dimension 64 --seed 52 --recipe R1 --stage joint --devices 1
```

用户明确要求直接叠加，不做GPU性能试跑。CPU调度/资源检查12项通过。模型从既定共同初始化开始，训练预算与选模规则不变；后续复核阶段复用此条件。VAST和seed51原进程保持运行。

2026-10-23T06:36:13.810302+00:00：用户取消多seed，已停止此进程，保存到第4轮的检查点与历史结果保留。见[取消记录](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/cancelled_multiseed.json)。
