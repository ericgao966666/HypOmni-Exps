# 20261023T060415-server-b-train-euc_none_d64_s51_R1-joint

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-20261021-server-b-retrieval-training](../../experiments/EXP-20261021-server-b-retrieval-training.md) |
| 服务器 | server-b |
| 状态与核对时间 | 已按用户要求停止；2026-10-23T06:36:13.810302+00:00（UTC），保留第3轮断点 |
| 实际源码 | 封存摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`；原仓库含未提交改动；沿用40GiB写入保护包装器 |
| 选择依据 | [欧氏四候选验证选模](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-gpu5-euc/selection.json)，R1按原规则锁定 |
| 协议与数据 | [封存协议](../../results/EXP-20261021-server-b-retrieval-training/2026-10-21-implementation/protocol_summary.json)；MSRVTT 7427/500/884 |
| 条件 | 欧氏无锥 / 64D / seed51 / R1 / joint / 30轮 / global batch64 / 单卡 |
| 资源 | PID960332；GPU5；file rendezvous |
| 原始结果 | `/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021/runs/euc_none_d64_s51_R1/joint` |
| 日志 | `/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__euc_none_d64_s51_R1__joint.log` |

```bash
/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/disk40_20261023/train_disk40.py --method euc_none --dimension 64 --seed 51 --recipe R1 --stage joint --devices 5
```

用户要求GPU5增加一个实验，因此提前这个既定复核条件。训练从共同初始化开始，后续统一复核阶段复用结果，不重复训练。现有三个工作进程未重启。

2026-10-23T06:05:53.727138+00:00已验证真实优化步，见[运行证据](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-gpu5-euc/progress.json)。

2026-10-23T06:36:13.810302+00:00：用户取消多seed，已停止此进程，保存到第3轮的检查点与历史结果保留。见[取消记录](../../results/EXP-20261021-server-b-retrieval-training/2026-10-23-seed50-only/cancelled_multiseed.json)。
