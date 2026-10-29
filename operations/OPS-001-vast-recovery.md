# VAST 150k 媒体恢复

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 / 类型 | OPS-001 / 数据准备 |
| 项目 | VAST27M-download |
| 状态 | 仅有历史running快照；当前源服务器状态无法在本机核实 |
| 进度快照时间 | 2026-10-20 15:44:33，Asia/Shanghai |
| 最后核对 | 2026-10-20 |

## 目的与范围

恢复 VAST-150k 缺失视频及音频配对，为后续实验增加可用训练数据。项目也包含 VAST-27M 下载工具，但以下计数仅属于 VAST-150k 恢复任务。

## 最近快照

| 指标 | 数量 |
|---|---:|
| 总标注 | 150,154 |
| 可用配对 | 93,986 |
| 仍缺失 | 56,168 |
| 本次恢复进程新增 | 200 |

“本次新增”不是本周新增。快照来自进度文件，进程与数字可能在此后变化；manifest 定时刷新可能稍落后于进度计数。

## 位置

- [下载器说明](../../VAST27M-download/README.md)
- [最新进度](</data-nfs/xiaoboxia/YuxuanGao/datasets/vast150k_recovery/bulk-20261009/state/progress.json>)
- [规范数据目录](</data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/vast150k/>)
- [可用性报告](</data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/vast150k/availability_report.json>)
- [恢复日志](../../VAST27M-download/logs/recover-vast150k-20261009.log)

## 对实验的影响

已经冻结的实验继续使用自己的 manifest 和哈希；不因下载新增而默默更换训练集。新实验需要明确记录新 cohort。不可访问、删除或私有来源仍可能缺失，不能将一轮恢复结束当作完整数据集恢复。

本卡不保存 Cookie、代理认证材料或带凭据的命令。

## 变更记录

- 2026-10-17 至 20：继续分批恢复，过程记录见原项目。
- 2026-10-20：补录上述时间点快照。

## 2026-10-28归档核对

本机配置没有VAST27M-download项目映射，历史源服务器 `/data-nfs/` 不在本机可用路径内。本轮保留10月20日历史计数，不推断仍在下载或已经完成；未连接未授权服务器。需源服务器提供新的进度/终态快照后才能更新。
