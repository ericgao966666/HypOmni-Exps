# 20261023T043728-server-b-train-hyp_cone_d64_s51_R1-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 已按用户要求停止；2026-10-23T06:36:13.810302+00:00（UTC），保留第16轮断点 |
| 实际源码 | 封存快照 `Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021`；摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动 |
| 运行时策略 | 沿用[磁盘40GiB包装器](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-disk40/runtime_policy.json)，GPU准入<45GiB |
| 选择依据 | [双曲方法四候选验证记录](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-early-selected/selection.json)，R1按原规则最高，不使用测试集 |
| 条件 | 双曲有锥 / 64D / seed51 / R1 / MSRVTT joint / 30 epochs / global batch64 / 单卡 |
| 数据与配置 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；MSRVTT 7427/500/884；λ=.1，既定共同初始化 |
| 资源 | PID3904627，GPU6，file rendezvous |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__hyp_cone_d64_s51_R1__joint.log` |
| 原始结果目录 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/hyp_cone_d64_s51_R1/joint` |

启动命令：

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/disk40_20261023/train_disk40.py --method hyp_cone --dimension 64 --seed 51 --recipe R1 --stage joint --devices 6
```

本条件属于原计划三种子复核，仅提前调度；不从seed50微调权重继续训练。后续统一复核阶段复用其完成记录，不重复运行。VAST原进程856070未重启。

2026-10-23T04:39:27.592407+00:00：已确认实际优化步，详见[运行证据](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-early-selected/progress.json)。

2026-10-23T06:36:13.810302+00:00：用户取消多seed，已停止此进程，保存到第16轮的检查点与历史结果保留。见[取消记录](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/cancelled_multiseed.json)。
