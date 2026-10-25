# 单卡测试缓存/评测槽位：eval-server2-gpu1

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T175723-server2-itm-parallel-eval-server2-gpu1 |
| 服务器 | server2；地址114.214.255.126 |
| 计划GPU | 1；等待状态不表示已经占用GPU |
| 状态与核对时间 | 已完成；2026-10-24 21:39 Asia/Shanghai |
| 当前作业 | eval/tv/seed-50/activitynet；特征/ITM进度3808 |
| 控制器身份 | PID 1148002；start ticks 156544513；boot ID在原始状态文件中 |
| 实际训练源码 | 冻结SHA-256 `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；基于PMRL a230347a072a46cdcb97eb30f4a5cdcf6f2119db的未提交实现 |
| 实际运维部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/4ff71fb62a739919eb672fa266aa7eb425c963908f792321e1d99560848c97df`；文件哈希见code_manifest.json |
| 数据与范围 | seed50；已冻结的四测试集TVA交集；不新增训练或seed，不改变模型末轮checkpoint |
| 协议 | 先锁定已完成模型的开发集候选/融合参数；预计算特征与ITM分数；全局开发集选择锁定后才输出测试指标 |
| 内存与权限 | 29GiB分配预算、8GiB启动余量；已有PID只用于资源检查，不发送停止信号 |
| 权威状态 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50/portable_parallel_eval-server2-gpu1.json` |
| 控制器日志 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/logs/20261024T175723-server2-itm-parallel-eval-server2-gpu1.log` |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50`；canonical eval子目录沿用原矩阵，`.ops_job.lock`保证跨机独占 |

特征提取、候选构建、ITM分数计算和指标汇总复用冻结实现。任务池优先ActivityNet，完成后领取其他未完成job；模型训练/开发集未完成时跳过该模型。主队列后来遇到相同job将等待并复用结果。缓存不等于正式评测完成。

server1检测时0–3已占约20–22GiB且计算繁忙，因此先以CPU等待容量；资源满足并连续检查通过后才启动GPUworker。server2的5–7等待当前四卡训练释放。所有大文件在共享NFS，系统盘只保留少量IPC。

历史状态快照：running；2026-10-24 18:08 Asia/Shanghai。

最终核对：已完成。本run属于同一四方法、seed50矩阵，完整结果见[权威快照](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)。原始日志、源码快照与模型仍在项目/NFS。
