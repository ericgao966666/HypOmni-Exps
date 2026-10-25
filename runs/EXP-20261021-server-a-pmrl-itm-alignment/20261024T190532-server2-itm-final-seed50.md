# PMRL–ITM 单seed完成记录

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL–ITM对齐](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261024T190532-server2-itm-final-seed50（矩阵完成事件，非新增训练） |
| 服务器 | server2；单卡评测池与主控制器协作完成 |
| 状态与核对时间 | 已完成；2026-10-24 21:39 Asia/Shanghai |
| 完成时间 | 2026-10-24 19:05:32 Asia/Shanghai |
| 实际训练源码 | 冻结SHA-256 `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750`；训练实现未提交 |
| 条件 | 四种采样、仅seed50；4×16、1354batch/epoch；末轮checkpoint固定 |
| 数据 | 严格TVA，86,706训练条目；测试样本884/995/3987/1224 |
| 完成证据 | 4份训练run_complete与worker_complete；4个开发集、16个测试job exit0+指标+worker_complete |
| 原始输出 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 可同步结果 | [最终快照](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/summary.md)；[核验JSON](../../results/EXP-20261021-server-a-pmrl-itm-alignment/2026-10-24-final-seed50/verification.json) |
| 预算范围 | 用户取消42/123；单seed执行策略已生效，非三seed确认实验 |

开发集预选sigma_max，TV候选、Top50纯ITM下测试均值57.9886%，较共同候选基线+0.4087pp；测试观察的mean_tv_ta为58.0271%，不据此重选。开发集融合α1在测试退化。原始结果与负结果均保留，无训练种子方差估计。

server1没有执行这些16项测试；其CPU容量等待槽位已在本次完成整理时核验身份后停止。server2正常结束并释放本任务GPU资源。未终止其他任务。
