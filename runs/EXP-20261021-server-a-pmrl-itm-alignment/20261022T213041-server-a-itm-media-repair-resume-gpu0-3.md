# 媒体修复后从400步续训：GPU0–3串行队列

| 字段 | 内容 |
|---|---|
| 实验卡 | [PMRL ITM评分消融](../../experiments/EXP-20261021-server-a-pmrl-itm-alignment.md) |
| run ID | 20261022T213041-server-a-itm-media-repair-resume-gpu0-3 |
| 服务器 | server-a |
| 状态与核对时间 | 已失败退出；10-23核实：10-22 23:33基线从400步启动，23:39 CUDA OOM；TV及后续组未启动 |
| 控制器开始时间 | 21:30:41 +08:00 |
| 源码 / 未提交改动 | PMRL-ITM基底a230347a；含未提交实现；冻结源码保持`e614af4a075812a56831aff28c02ac821b9a62c6b6b7f1fad1ca1775996fd750` |
| 续训控制器 SHA-256 | `9b74929e416f28a950ffefd5857f2e1a41a285f9fe276b039e7c43b0e8691ff6` |
| 训练数据 | 仍为86,706条过滤版；训练清单SHA-256 `5f85117bb8810707fbd30755e91997c840c1f7f54fc5c8c3330d7e8f5b9f0384`；未再删除样本 |
| 恢复点 | 基线/TV均有300和400步完整checkpoint；将各从step400恢复，world4与原配置保持一致 |
| GPU与执行顺序 | 仅GPU0–3；基线seed50→TVseed50→mean_tv_ta→sigma_max→条件复验，任务串行 |
| batch / 保存 | 每卡16、全局64；每100batch及末轮保存，保留最近两份 |
| 资源等待 | 每卡至少38GiB空闲，连续三次稳定检查后启动；最多等待12小时；不抢占其他进程 |
| 显存参数 | 实测需求准入36GiB+2GiB余量；旧基线/TV配置中的allocator cap40/29GiB保持不变，新组采用36GiB |
| PID | CPU侧等待控制器413723；尚无新的torchrun PID/端口 |
| 命令与资源清单 | [启动清单](../../../PMRL-ITM/artifacts/launches/20261022T213041-server-a-itm-media-repair-resume-gpu0-3.json) |
| 控制器日志 | [日志](../../../PMRL-ITM/artifacts/launches/20261022T213041-server-a-itm-media-repair-resume-gpu0-3.log) |
| 继续使用的输出根目录 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/outputs/20261022T170008-server-a-itm-filtered-recovery-seed50` |
| 当前状态文件 | `serial_media_resume_state.json`；旧parallel_state是失败的历史状态 |
| 修复清单 | `/data-nfs/xiaoboxia/YuxuanGao/PMRL-ITM/media_repairs/20261022T212335-md6F6VbYjeE7-lossless/repair_manifest.json` |
| 验证记录 | [原片错误、修复与加载窗口检查](../../../PMRL-ITM/artifacts/launches/media-repair-resume-verification.json) |
| 正式结果 | 尚无完整epoch或检索结果；不能把等待队列或CPU检查当作GPU续训成功 |

## 失败与修复证据

过滤版基线17:43:30、TV17:56:11均在完成472个batch后由rank2报DataLoader600秒超时退出；torchrun随后清理其余rank。最新完整checkpoint400保住了此前训练进度。本次没有为恢复而修改训练样本清单或重新从初始化开始。

此前现场定位的媒体为 `md6F6VbYjeE.7.mp4`。原视频流时间戳起点−4.857933秒；Decord全帧读取明确报超过35个损坏/邻近恢复帧，FFmpeg则能解码全部355帧。独立修复副本采用全关键帧无损编码、时间戳归零，并显式保留BT.709色彩参数。源与修复副本的全部355帧YUV内容哈希逐帧相同，帧率/分辨率/帧数不变。原视频和独立音频WAV均保留，实际修复目录仅覆盖这一条视频。

源文件SHA-256：`e30c1a6c10cd0dad584e69c77245e83626e5e0f9cb0fabec37b686e2bd43288e`；最终副本SHA-256：`10289a7807a1c1d2906078522325ab9ab27bd53781ed7da72b60d96e66df9ebd`。修复通过原有PMRL_VIDEO_REPAIR_ROOT机制显式启用，写入续训清单；冻结学习源码、旧job配置、训练清单和checkpoint恢复合同未改写。后续续训必须使用本次带媒体修复清单的入口。

## 验证与当前限制

- 最终副本的355帧全帧读取、67组抽帧检查通过；原片的Decord全帧读取失败，故不声称二者Decord RGB全帧直接相等。
- 正式任务同环境的fork/4数据worker/seed50/rank2/local batch16检查加载前480批，读过问题样本所在第474批。训练最后记录472与预取阻塞位置相符。该检查仅CPU数据加载，模型更新为0。
- 两组恢复配置、源码、训练清单哈希及四rank的step400状态校验通过；前400步模型进度无需重训，但恢复仍会重读数据前缀以重建worker随机状态。
- 初次受限环境测试的进程通信受到禁止，造成队列超时；切换至训练同环境后通过。没有把该测试环境错误当作新的坏样本。
- GPU0–3当前总占用约28–31GiB/卡，只余17–20GiB，低于本任务准入。控制器等待，不降低batch，不结束其他进程。GPU4–7不在本次队列范围。

## 运行变更

- 21:30:41启动有界容量等待控制器413723。
- 21:36核实状态为waiting_for_capacity；尚无GPU训练启动，后续状态须再次核实。
- 编辑前已fetch，保留已有README/OPS-001等改动，未提交或推送。

- 10-23 19:15：旧控制器已退出。当前仅TV/seed50的等待队列见[新运行记录](20261023T191223-server-a-itm-tv-resume400-gpu0-3.md)，不得把本条历史等待状态当作仍在运行。
