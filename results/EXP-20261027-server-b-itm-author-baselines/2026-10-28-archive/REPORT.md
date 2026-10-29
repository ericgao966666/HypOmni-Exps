# VAST、GRAM、PMRL：共同VAST验证集补测

本次均使用作者权重，0步本轮追加训练。相同2048条VAST验证样本、2帧视频、1音频窗、40token文本、无字幕、512D、top32。
各方法使用自己的编码器与匹配器。FP16编码、raw AV token转FP16、BF16匹配、FP32排序。模型权重与来源均有SHA256。

## 1. 各方法原生评分与候选池

VAST/PMRL主检索使用各自原生T–VA投影点积；GRAM使用负的三模态Gram体积。原生候选上的ITM包含候选漏召回。

| 模型 | ITC t→va R@1 | ITC va→t R@1 | ITC平均R@1 | ITM t→va R@1 | ITM va→t R@1 | ITM平均R@1 | 候选R@32均值 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| VAST | 14.5020 | 8.8379 | 11.6699 | 30.0781 | 20.8008 | 25.4395 | 48.7793 |
| GRAM | 25.0488 | 21.4355 | 23.2422 | 47.3633 | 46.0449 | 46.7041 | 70.8496 |
| PMRL | 33.5449 | 35.1562 | 34.3506 | 49.7070 | 49.2188 | 49.4629 | 80.9082 |

## 2. 相同双曲ITC候选池的重排

此处复用当前冻结双曲ITC的候选，双向候选召回均84.2773%。它控制了候选差异，但编码器与matcher都仍属于各自模型，因此不是只替换matcher的消融。

| 模型 | t→va R@1 | va→t R@1 | 双向平均R@1 | 平均R@5 | 平均R@10 |
| --- | ---: | ---: | ---: | ---: | ---: |
| VAST | 35.9863 | 27.1973 | 31.5918 | 54.7607 | 67.2119 |
| GRAM | 49.8047 | 48.8281 | 49.3164 | 70.2881 | 76.7822 |
| PMRL | 50.4395 | 49.6094 | 50.0244 | 70.3613 | 76.9043 |

## 解释边界

- 本次是统一评测协议下的现有作者权重参考，不是三种方法各自论文配置的完整复现，也不是追加训练预算匹配的实验。
- 当前双曲ITC头此前训练30轮；我们的ITM又有额外更新。原ITC-only37.16%不是原始VAST作者权重的ITC成绩。
- VAST保留划分只保证不参与本轮增量训练，不能保证各作者预训练从未使用这些视频。
- 未读取MSRVTT/VATEX测试性能，未更改当前ITM v2训练或选模规则。
- VAST共同池结果需复现此前零步参照；各方法matcher与自身原生通路的数值等价检查均通过。

## 原始记录

- VAST：checkpoint SHA256 `9005d283ea0de99549efbedeb7d21c8e25bea8fa41c0f6570296b0e7a055a6c5`；结果位于数据目录`/data0/xiaobo.xia/yuxuan.gao/itm_author_baselines_20261027/vast`，包含protocol、原生特征、pair logits、DONE及进度记录。
- GRAM：checkpoint SHA256 `070c4b25a12f0a2861ced77d9bbe871e649f9be5b390e680e6049114a51b99d5`；结果位于数据目录`/data0/xiaobo.xia/yuxuan.gao/itm_author_baselines_20261027/gram`，包含protocol、原生特征、pair logits、DONE及进度记录。
- PMRL：checkpoint SHA256 `78ab07cf45f9465fcd1cb0a01b7c32ec83a467e642338a67bd6079bdb21b8836`；结果位于数据目录`/data0/xiaobo.xia/yuxuan.gao/itm_author_baselines_20261027/pmrl`，包含protocol、原生特征、pair logits、DONE及进度记录。

## 当前C0的上下文参考

原生C0、LR1e-5、seed50、1500步在同一共同候选池的双向平均R@1为 **49.6338%**。这比先前500步的48.2666%有所提高，数值上接近GRAM的49.3164%和PMRL的50.0244%。但C0有额外训练，且仍需多seed复核；不能将这些单次差值解释为最终方法优劣。详见current_c0_context.json。
