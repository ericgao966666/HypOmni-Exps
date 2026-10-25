# server2 无损修复后从900续跑

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T150526-server2-itm-remaining-resume |
| 服务器 | server2，114.214.255.126；GPU4–7 |
| 状态与核对时间 | 2026-10-24 15:46 Asia/Shanghai；基线训练完成，开发集ITM评测运行中 |
| 启动 / 训练完成 | 15:05 / 15:38；当前控制器4095490继续管理后续矩阵 |
| 实际训练源码 | SHA-256 `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；训练核心保持冻结源码 |
| 运维源码部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/4e1a5eaad1ab8bc9eee4908bb2781503f33a41967e99ccf6cc8ed733803fc778` |
| 数据版本 | 86,706条严格TVA；训练SHA-256 `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384` |
| 模式与预算 | legacy_va / seed50；4×16，全局64；1354batch一个epoch；原始配置与恢复合同不变 |
| 修复清单 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/media_repairs/20261024T145826-cLeZEBIFYHo21-lossless/overlay_manifest.json`；原视频保留，md6(355帧)+cLeZ(356帧)版本化无损覆盖 |
| 结果 | 1354批，1353次有效更新，1次AMP跳步；正式测试指标待完成 |
| 输出根目录 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 完成证据 | `train/legacy_va/seed-50/run_complete.json`、`worker_complete.json`、完整`checkpoint_step_1354.complete.json`与哈希审计 |

精确诊断及前后对比在`portable/diagnostics/window-920/`。原cLeZ视频首次请求`[173,340]`挂起，20秒超时；无损副本同请求、全帧与额外抽帧通过，原始与修复视频的FFmpeg解码YUV帧序列哈希完全相同。CPU元信息重放复查rank2从卡点到1354批正常结束，仅作诊断证据；真实GPU训练完成标记才用于训练验收。

启动命令：`ops/expctl.py migrate --target server2 --remaining --gpus 4,5,6,7`。从共享900步恢复，未重训已完成更新。目标上所有大型checkpoint、缓存和日志在NFS。后续按原协议继续TV、mean_tv_ta、sigma_max与开发集选参，测试前锁定；目前不能判断方法收益。

16:00核对：基线开发集已完成，控制器自动进入TV/seed50，从400恢复到520批并提交500步新checkpoint。其他两组及正式测试尚未完成；工具环境同步期间未停止本实验。

2026-10-24 16:40核对：该控制器已于16:20:48在TV完整step900保存后停止，按用户要求交接至支持并行作业锁的新主控制器。该轮已完成基线训练与1000样本开发集；TV900时898次有效更新、2次AMP跳步。停止信号指向已核验的自有控制器及其独立torchrun进程组；旧源和失败记录保留。
