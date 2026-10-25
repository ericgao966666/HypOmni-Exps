# server2 剩余矩阵续跑：20261023T231135-server2-itm-remaining-resume

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM 对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261023T231135-server2-itm-remaining-resume |
| 服务器 | server2，114.214.255.126，独立于历史server-b |
| 状态与核对时间 | 失败；2026-10-24 15:00，Asia/Shanghai；现场确认控制器及torchrun已退出 |
| 开始 / 结束 | 20261023 231135 / 2026-10-23 23:54:59；Asia/Shanghai |
| 代码仓库与快照 | PMRL a230347a072a46cdcb97eb30f4a5cdcf6f2119db基础上未提交实现；实际冻结训练源码SHA-256 `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750` |
| 控制器部署 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/deployments/1f3a26e8592ab599293d3a9c9169f95e0480b017bd940f5f0bf609f16a0f2fb2`；不可变目录内文件哈希单独记录 |
| 训练配置 | 原`train/legacy_va/seed-50/config.json`；恢复合同配置SHA-256 `777f0455abaa8158e9e5f05422bc34a612915b97ff08aaee84c6f026e8651bc4` |
| 数据与条件 | 冻结86,706条严格TVA，SHA-256 `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384`；seed50，GPU4–7，每卡16，全局64，1354batch/epoch |
| 实际训练 | legacy_va从400恢复至920；累计920次有效更新、0 AMP跳步 |
| 启动与资源 | `ops/expctl.py migrate --target server2 --remaining --gpus 4,5,6,7`；控制器PID 3619969；torchrun/端口/进程身份见对应job与启动清单 |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50`；保留原输出，使用共享checkpoint |
| 控制器日志 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/portable/logs/20261023T231135-server2-itm-remaining-resume.log` |
| 完成或失败证据 | rank2 DataLoader超时600秒；完整checkpoint900保留；没有worker_complete或正式检索结果 |

模型训练源码、初始化、原始配置、样本名单及batch均保持原协议。目标复用已有PMRL虚拟环境；Python3.9→3.10 checkpoint及RNG加载验证通过。新checkpoint、缓存及日志均写NFS，源SSD备份未删除。媒体覆盖仍只启用已验证的md6F6VbYjeE.7无损修复。

跨机验收证据在`portable/validation/`：`acl_probe.json`、`all-inputs-readable.json`、`python39_to310_recovery.json`及`server2-real-resume.json`。900步模型/优化器/训练状态文件从源服务器复核SHA-256全部一致，四rank恢复状态完整。

这是续跑与基础设施验收记录，不是完整训练结果。尚未产生开发集或测试集指标；TV仍保留400步，其余两种方法未开始。两次失败均在同一读取位置，正在CPU诊断，不能据此判断模型收益或收敛。
