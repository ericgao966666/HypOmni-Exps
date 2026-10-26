# EXP-004：训练预算与checkpoint来源审计

[返回实验结论](../EXP-004-frozen-transfer.md)

本页保存详细结果或来源审计；2026-10-26从原实验卡整理，原始指标与图表未改写。

## 训练细节与模型来源

### 四种方法的来源

| 模型 | 本次使用的来源 | 本地训练范围 |
|---|---|---|
| VAST | 官方发布的 `model_step_204994.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| GRAM | 官方发布的 `gram_model_step_459.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| PMRL | 官方发布的 `pmrl_base.pt` | 本轮直接推理，没有按 Ours 的预算重新训练 |
| Ours | VAST 官方编码器，加上 `minimal9_B1_standard_s50` 的子集头 | 在本地 VAST 划分上训练头部，VAST/MSRVTT 评测使用的具体版本见下表 |

本页不能描述为“四种方法都在相同 VAST 数据上统一训练 30 轮”。以下训练轮数和 steps 仅描述 Ours 的本地头部训练，不包含任何官方预训练成本。

### Ours 的数据与训练范围

- VAST 按来源视频分组划分：训练 **82,611** 条，验证 **2,048** 条，测试 **2,048** 条；同一来源视频不跨这些划分。
- 全局 batch 为 **256**，使用 `drop_last`，每轮处理 322 个完整 batch，即 **322 次梯度更新**。不足一个 batch 的 179 条不进入该轮更新。
- 共享 warmup 冻结骨干、继承的头和全部半径参数，只训练三个新增方向头 TV、TA、TVA；主训练在固定 pooled 特征上训练全部子集方向头和半径参数。**两个阶段都没有更新编码器。**
- 主训练使用 512 维表示、seed50、9 对对比目标及 λ=0.1 的九条锥约束；未在 MSRVTT 上继续训练。本页后续的 MSRVTT 端到端微调属于独立的 [EXP-006](../EXP-006-msrvtt-finetune.md)。

数据划分和基础设置见 [base_protocol.json](../../results/EXP-004/2026-10-21/training/base_protocol.json)，主训练的实际运行约定见 [main_experiment.json](../../results/EXP-004/2026-10-21/training/main_experiment.json) 和 [main_config.json](../../results/EXP-004/2026-10-21/training/main_config.json)。基础协议中也保留了其他阶段的参数；本次是否执行、执行多久，以相应完成记录为准。

### 实际训练预算

| 阶段 | Epochs | 梯度更新 steps | 阶段完成记录 |
|---|---:|---:|---|
| 共享 warmup | 8 | 2,576 | [warmup_done.json](../../results/EXP-004/2026-10-21/training/warmup_done.json) |
| 后续头部主训练 | 30 | 9,660 | [main_done.json](../../results/EXP-004/2026-10-21/training/main_done.json) |
| 本地训练任务合计 | 38 | 12,236 | 两阶段相加，不包含官方 VAST 预训练 |

主训练从共享 warmup 的第 8 轮 `last.pt` 开始，输入文件哈希与运行记录一致。主训练的 epoch/step 从该阶段重新计数；这里的“主训练第 22 轮”不包含前面的 8 轮 warmup。

### VAST 和 MSRVTT 实际评测的 checkpoint

| 评测数据 | Ours checkpoint | 主训练 epoch | 主训练 step | 来源依据 |
|---|---|---:|---:|---|
| VAST 测试集，2,048 条 | `last.pt` | 30 | 9,660 | [测试命令](../../results/EXP-004/2026-10-21/training/vast_test_launcher.json)、[头部测试指标](../../results/EXP-004/2026-10-21/training/vast_head_test_metrics.json)、[六方向评测结果](../../results/EXP-004/2026-10-21/training/vast_ours_metrics.json) |
| MSRVTT 测试集，884 条 | `best.pt` | 22 | 7,084 | [评测记录及 checkpoint 哈希](../../results/EXP-004/2026-10-21/training/msrvtt_ours_metrics.json)、[checkpoint 审计](../../results/EXP-004/2026-10-21/training/checkpoint_audit.json) |

`best.pt` 由 VAST 验证集的十二方向 macro R@1 选择，第 22 轮达到 29.50846%；主训练仍实际跑满 30 轮。逐轮的 epoch、step 和验证分数见[验证摘要](../../results/EXP-004/2026-10-21/training/main_validation_summary.json)。两份 checkpoint 的 epoch、step 和 SHA-256 已从本地文件核对，未上传模型权重。

VAST 原汇总中的 `selection` 字段写着 `validation-selected checkpoint`，但其 `source_features` 指向使用 `last.pt` 生成的测试特征；对应测试命令也明确指定 `last.pt`，且六方向分数与该次测试记录一致。因此本页以这条实际来源链更正描述，保留[原汇总快照](../../results/EXP-004/2026-10-21/training/vast_comparison_report.json)供追溯。MSRVTT 记录的 checkpoint 哈希则与第 22 轮 `best.pt` 一致。

这些结果可分别解读，但不能当作严格同 checkpoint 的跨数据集对比；若需要这种比较，应统一 checkpoint 后重新评测。本次只补充来源审计，没有改动分数或重跑评测。


## 变更记录

- 2026-10-16 至 17：依次完成 VAST、MSRVTT、AudioCaps 和 Clotho 评测。
- 2026-10-20：补录；与 EXP-003 的十二方向结果分开记录。
- 2026-10-20：展开 VAST 与 MSRVTT 六方向及 macro 的 R@1/5/10，补入 VAST 中位排名，数值由原 CSV 生成。
- 2026-10-20：增加关联 EXP-006 的 MSRVTT 十轮微调曲线、PDF 和选模汇总，明确与本页冻结评测结果的区别。
- 2026-10-20：按用户要求补齐全部三组已有曲线，追加 VAST 头部训练和跨数据集迁移曲线；保留各自来源及指标口径。
- 2026-10-20：按列标记最优与次优值，处理并列和 MedR 的反向排序；原始数字未改变。
- 2026-10-20：按用户要求移除本页关联训练曲线整节；其他实验文档及图表文件保留。
- 2026-10-21：补充模型来源、数据划分、训练范围、8 轮 warmup 与 30 轮主训练预算；纠正“VAST 与 MSRVTT 使用同一个验证最优 checkpoint”的描述，明确 VAST 使用第 30 轮 `last.pt`、MSRVTT 使用第 22 轮 `best.pt`，原结果保留。
