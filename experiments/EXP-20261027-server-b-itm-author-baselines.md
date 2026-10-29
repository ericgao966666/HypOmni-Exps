# 作者权重ITM补测：共同候选下PMRL与GRAM接近

[返回总览](../README.md) · `EXP-20261027-server-b-itm-author-baselines` · 原结果：2026-10-27；归档核对：2026-10-28T12:41:34.660651+00:00

**同一双曲ITC候选池上，PMRL与GRAM双向R@1为50.0244%和49.3164%，VAST为31.5918%。** 原生候选下则为49.4629%、46.7041%、25.4395%。固定候选控制了召回差异，但各方法仍使用各自编码器与matcher，不能解释成只替换matcher的消融。

## 协议与主要结果

作者权重、0步本轮追加训练；共同2,048条VAST验证、2帧视频、1音频窗、40 token、无字幕、512D、top32。原生评分分别遵循各自模型；共同候选由当前冻结双曲ITC产生，双向R@32均84.2773%。

| 方法 | 原生候选ITM双向R@1 (%) | 共同候选ITM双向R@1 (%) |
|---|---:|---:|
| VAST | 25.4395 | 31.5918 |
| GRAM | <ins>46.7041</ins> | <ins>49.3164</ins> |
| PMRL | **49.4629** | **50.0244** |

[原始完整报告](../results/EXP-20261027-server-b-itm-author-baselines/2026-10-28-archive/REPORT.md) · [VAST结果](../results/EXP-20261027-server-b-itm-author-baselines/2026-10-28-archive/vast/results.json) · [GRAM结果](../results/EXP-20261027-server-b-itm-author-baselines/2026-10-28-archive/gram/results.json) · [PMRL结果](../results/EXP-20261027-server-b-itm-author-baselines/2026-10-28-archive/pmrl/results.json)。各方法protocol包含模型来源与哈希，DONE及数值等价检查保留在[快照](../results/EXP-20261027-server-b-itm-author-baselines/2026-10-28-archive/)和[运行记录](../runs/EXP-20261027-server-b-itm-author-baselines/README.md)。

## 比较边界

这不是论文配置的完整复现，也不是追加训练预算匹配实验。当前双曲ITC头先前训练过30轮，后续ITM又有额外更新；不能直接拿本表证明新ITM优于PMRL。验证保留只保证不参与本轮增量训练，不能保证作者预训练从未见过这些视频。本补测没有使用MSRVTT/VATEX测试性能选模。
