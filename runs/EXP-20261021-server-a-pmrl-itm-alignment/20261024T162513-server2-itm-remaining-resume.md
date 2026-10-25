# server2双队列：主矩阵从TV900恢复

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T162513-server2-itm-remaining-resume |
| 服务器与GPU | server2，114.214.255.126；GPU 4,5,6,7 |
| 状态与核对时间 | 已完成；2026-10-24 21:39 Asia/Shanghai |
| 实际进度 | 1000/1354个batch；有效更新998，AMP跳步2 |
| 训练源码 | 冻结SHA-256 `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；未提交实现，不以基底commit代替运行源码 |
| 运维部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/0ceb10be929b052f649650ebc82dc5296c433b2575e19db2804f194c6bcb2539`；包内文件哈希固定 |
| 数据 | 86,706条严格TVA，训练manifest SHA-256 `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384` |
| 条件 | seed50，512维，每卡16，全局64，一个epoch=1354batch；百步保存 |
| 配置文件SHA-256 | `664cedd060e40796113ffdcbad63cc1d8a834fa3126c2712b7add19b71ae59a5`；路径`/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50/train/tv/seed-50/config.json` |
| 控制器与worker | 控制器PID 373143；torchrun PID 373433；端口 40605；start ticks/boot ID保存在原始状态与job清单 |
| 资源预算 | 29GiB分配预算+8GiB启动余量；已有进程PID仅作共用检查列表，不执行停止 |
| 媒体覆盖 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/media_repairs/20261024T145826-cLeZEBIFYHo21-lossless/overlay_manifest.json`；两处已核验无损修复 |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 控制器日志 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/logs/20261024T162513-server2-itm-remaining-resume.log` |
| 当前结果 | TV从完整900恢复；基线已完成并复用；随后mean_tv_ta及原协议后续流程 |

两个控制器各有独立交接token及控制器锁；全部训练/评测job有独占锁。主队列遇到并行job时等待并复用，选参与测试统一由主队列完成。相同目标重复启动返回当前活动任务，不新增第二组worker。所有大型checkpoint、日志和缓存继续写NFS。

验证：9项运维检查通过；源端真实跨机锁探测显示矩阵锁、并行控制器锁及两个job锁均被远端持有。实时状态与步数保存在`portable_state.json` / `portable_parallel_sigma_max.json`和各job的`updates.jsonl`。

对其他任务的影响核查尚不能证明零影响：已核对本任务停止信号的目标，GPU2原有进程仍在；无系统OOM日志权限、未取得同学退出日志。同卡运行共享显存及算力，不提供隔离保证。

历史状态快照：运行中；2026-10-24 16:40 Asia/Shanghai。

最终核对：已完成。本run属于同一四方法、seed50矩阵，完整结果见[权威快照](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)。原始日志、源码快照与模型仍在项目/NFS。
