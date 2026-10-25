# 剔除卡住样本，按百步 checkpoint 从头重启

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM 评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261022T170008-server-a-itm-filtered-recovery-seed50 |
| 服务器 | server-a |
| 状态与核对时间 | 正式训练运行中；2026-10-22 17:14:46，Asia/Shanghai；基线144、TV106个batch，两组均完成step100完整checkpoint并继续训练 |
| 开始时间 | 2026-10-22 17:00:08 +08:00 |
| 基底 / 未提交改动 | PMRL-ITM，a230347a；实现未提交 |
| 源码 SHA-256 | `e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750` |
| 调度 SHA-256 | `5a19ff9b6bb72d18aff04efd73357311245abd3eae7ac602e0c5219dd7d846de` |
| 新训练清单 | 86,706条；原86,707条仅剔除`hU6PCGt2CuQ.20`，原媒体未删除 |
| 训练清单 SHA-256 | `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384` |
| 版本manifest SHA-256 | `915cec39509b4a9449a4623e89053c677c406ceffb27b30f7683595934f3b0c3` |
| 数据版本 | `assets/itm-cohort-20261022-drop-hU6PCGt2CuQ20`；父manifest与排除证据在版本manifest中 |
| 其他数据 | 校准2048条、开发集和四个测试集内容哈希不变；复用原校准温度 |
| 训练条件 | 严格TVA；每卡16、全局64；一epoch仍为1,354个batch；先seed50；四种方法统一新清单 |
| 保存与恢复 | 每100个batch及末轮保存；本地SSD保留最近两份完整checkpoint；原命令追加`--resume-failed`继续 |
| GPU / PID / 端口 | 4–7基线torchrun114766、端口59015；0–3 TV torchrun114769、端口58223；控制器106833；后续mean_tv_ta/sigma_max沿用对应队列 |
| 启动清单 | [命令与资源](../../../PMRL-ITM/artifacts/launches/20261022T170008-server-a-itm-filtered-recovery-seed50.json) |
| 调度日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261022T170008-server-a-itm-filtered-recovery-seed50.log) |
| 输出根目录 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 正式结果 | 尚无完整epoch或检索结果 |

## 剔除依据与范围

基线两次在batch858后发生rank3 DataLoader超时（120秒、600秒），TV也在同一位置停顿。16:50–16:53现场检查，TV的rank3 PID114197下的数据worker PID117439持续占用CPU，打开的视频为`hU6PCGt2CuQ.20.mp4`；对应原清单索引32359、rank3采样偏移13748，位于停顿后的预取范围。用户授权去掉导致问题的样本并重新开始实验。

仅从派生训练清单删除这一条记录。原视频/音频、原86,707条清单、失败输出与日志均保留。12组孤立随机帧对能够解码，未复现训练时的完整decoder状态，因此记录为“现场定位的卡住样本”，不宣称该文件在所有解码方式下均损坏，也不把局部检查当作全数据解码认证。证据：[卡住进程与打开文件](../../../PMRL-ITM/artifacts/launches/stalled-worker-evidence.json)、[有限帧对检查](../../../PMRL-ITM/artifacts/launches/stalled-clip-reproduction.json)。

旧TV进程经PID、启动时间、完整命令和进程组核对后，于16:54附近收到本任务SIGTERM停止；仅影响本实验进程组。旧调度和训练均已退出，未触碰其他任务。准确停止时刻见[停止记录](../../../PMRL-ITM/artifacts/launches/stop_stalled_tv.json)。

## 实施与验证

新增版本化assets入口，Runner的配置、协议和冻结数据都使用指定清单，恢复校验绑定新清单哈希。模型、损失、采样评分、batch与训练预算没有变化。新运行不继承旧v1的训练进度，四种方法都从同一初始化checkpoint重新开始。

27项ITM检查通过，包含新清单确实被配置/冻结快照使用、旧清单保持原样及篡改后拒绝运行；4项双队列调度检查通过。百步恢复逻辑沿用已通过真实双GPU AMP/NCCL中断恢复测试的实现。17:14:46已核实两组完整PMRL模型的第100步checkpoint实际落盘，保存后训练继续推进；不是仅凭单元测试判断。

尚无检索指标。最终指标仍按冻结开发/测试口径、双向四数据集等权平均报告；本轮训练口径为86,706条，与旧86,707条运行分开标注。

## 首份完整 checkpoint 核实

17:14:46核对：基线已到144个batch，TV已到106个batch，均有`checkpoint_step_100.complete.json`。每组文件大小：模型5,587,045,722字节（约5.20GiB）、优化器9,940,697,931字节（约9.26GiB）、训练状态73,575字节。三份文件均与complete标记声明的大小一致；training_state版本2包含4个rank，各rank有效更新与AMP跳步之和均为100，源码与冻结训练清单哈希相符。两组在保存点均100次有效更新、0次AMP跳步。

实际目录为本地 `PMRL-ITM/artifacts/checkpoints/255789d006930558/train/<mode>/seed-50/`，NFS job/ckpt软链接已核实。保存完成后两组继续执行，排除了仅生成临时文件或卡在保存同步点的情况。保留最近两份的策略会在后续完整保存后清理更老版本，历史验证信息保留在[百步保存证据](../../../PMRL-ITM/artifacts/launches/20261022T170008-server-a-itm-filtered-recovery-seed50-checkpoint-verification.json)。

本次验证没有中断新训练来强制恢复；恢复数值一致性由此前CPU和真实双GPU小模型演练验证。本轮首份大checkpoint已实际完成，完整epoch和检索结果仍待运行。

- 后续失败：基线17:43:30、TV17:56:11均在472个batch后超时；两组300/400步checkpoint完整。本次保存机制保住400步进度，后续按[媒体修复后的GPU0–3续训记录](20261022T213041-server-a-itm-media-repair-resume-gpu0-3.md)推进；截至21:36因显存不足等待，尚未恢复。
