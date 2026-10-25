# 20261024T212155-server-b-train-hyp_cone_d512_s50_R1-joint

- 实验：[64D训练方案比较](../../experiments/EXP-20261021-server-b-retrieval-training.md)。
- 服务器：server-b；核对时间：2026-10-25T07:22:03.941622+00:00（UTC）。
- 状态：已完成对应条件；重试历史以原始启动清单为准。
- 条件：hyp_cone_d512_s50_R1 / joint；seed50；global batch 64。
- 运行源码：封存快照摘要 `5c50f53951e21a6350d78ea3b11526e9f5c02abac483909907161375fe420337`，包含未提交实现；不能以当前Git HEAD代替。
- 数据：joint使用MSRVTT 7427/500/884；warmup/frozen使用封存VAST划分。测试为884候选、六方向macro，验证选模。
- 命令：`/home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/.venv/bin/python -u -B /home/xiaobo.xia/YuxuanGao/Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/control/seed50_only_20261023/train_seed50.py --method hyp_cone --dimension 512 --seed 50 --recipe R1 --stage joint --devices 4,7`。
- PID：657535；GPU：4,7；端口：文件rendezvous。
- 原始日志：server-b工作区相对路径 `Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/code/logs/lowdim_retrieval_20261021/train__hyp_cone_d512_s50_R1__joint.log`。
- [本次结果与运行观察](../../results/EXP-20261021-server-b-retrieval-training/2026-10-25-current-results/README.md)。
