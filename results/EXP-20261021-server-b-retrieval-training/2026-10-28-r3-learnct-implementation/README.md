# 64D R3：λ=.2、可学习曲率与温度

沿用历史 R3：VAST train82608/val2048，热身8轮（batch256，lr3e-4），头部训练30轮（batch256，lr1e-4），MSRVTT train7427/val500微调10轮（batch64，头部/非视觉lr2e-5，视觉lr5e-7），seed50。

新条件从原64D共同初始化重新训练。λ=.2；c初始1、τ初始.07；两者在三个阶段均可学习并随检查点传递，采用阶段头部学习率且不做weight decay。c限制.1–10、τ≥.01，物理r限制.21–4；原R3热身仅开放TV/TA/TVA方向头，半径头冻结，此阶段额外学习c/τ。保留原FP32头部、FP64几何，未替换成前序512D诊断实验的FP16投影/FP32几何。

热身使用末轮进入头部训练；头部训练按VAST验证R@1最佳进入微调；微调按MSRVTT验证R@1最佳，均沿用原严格改善选模规则。不会使用测试集选模。本次自动输出验证比较，不自动新增测试推理。

历史R3同协议对照为欧氏无锥（验证六方向macro R@1 28.2667%，epoch9）和双曲有锥λ=.1固定c/τ（28.1000%，epoch7）。旧欧氏τ固定.07，故这是候选方案比较，不能把差异全部归因于曲率。单seed不代表稳定统计优势。

`experiment_spec.py`、`learned_geometry.py`、`train.py` 为独立增量实现；引用旧封存模型/数据代码并核验哈希。旧结果和旧源码保留。`test_experiment.py` 的8项CPU测试全部通过，覆盖c=1下旧输出/损失/梯度、一般曲率距离公式、标量梯度有限差分、物理半径/检索评估、阶段冻结/优化器、跨阶段加载、边界和实验范围。详见PREPARATION.json。

GPU2单任务，显存上限40GiB、至少8GiB余量，数据盘保护线40GiB；训练批次及调度器均检查资源。无网络端口，使用文件rendezvous。调度器自动串行执行warmup→frozen→joint，结束时核对500个验证ID并生成comparison.json。

- 启动、PID：LAUNCH.json；逐阶段：logs/launches.jsonl。
- 当前状态：logs/status.json；调度日志：logs/scheduler.log。
- 数据和权重：/data0/xiaobo.xia/yuxuan.gao/r3_64d_learned_ct_lambda02_20261028。
- 命令：项目code/.venv/bin/python -u -B schedule.py --device 2（先加载code/local_env.sh）。

远端状态尚未核实：git fetch origin被自动审批拒绝；仅本地记录，无commit/push/upload。
