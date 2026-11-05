# λ=0.3：曲率与温度联合学习的匹配实验

> 本页是用于 GitHub 阅读的 Markdown 报告，保留原报告的数值、结论与局限。分层整理日期：2026-11-05；实验核对时间沿用原文。
> 原文仅存本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/REPORT.md`；原文 SHA-256：`1b5ed75d9bdee064e9a77bbfb9409c85f66a02dd4f4df2df3e7c342de452810b`。数据、图件和运行记录的访问方式见[本地证据说明](../../../LOCAL_ARTIFACTS.md)。

已完成30轮、9660步；512D、seed50、VAST验证2048条、六方向macro。只改变λ，与0.2/0.5保持相同初始化、数据顺序及训练算法。主结果固定epoch30；没有微调或测试集评估。

| λ | R@1↑ | R@5↑ | R@10↑ | 平均超锥角↓ | 严格合法满足率↑ | 最终c | 最终τ |
|---|---|---|---|---|---|---|---|
| 0.2 | **18.750** | **37.288** | **46.737** | 70.801 | **0.000** | 0.617123 | 0.043651 |
| 0.3 | <ins>18.107</ins> | <ins>36.353</ins> | <ins>45.931</ins> | <ins>52.064</ins> | **0.000** | 0.617120 | 0.043542 |
| 0.5 | 16.960 | 34.945 | 44.263 | **33.931** | **0.000** | 0.617219 | 0.043423 |

λ=.2→.3：R@1变化 -0.643 个百分点，平均超锥角变化 -18.737°。
λ=.3→.5：R@1变化 -1.147 个百分点，平均超锥角变化 -18.133°。

超锥角降低不等于严格蕴含成立；仅单seed验证结果，不表示统计显著性或测试收益。

核验通过：45个产物哈希；完整30轮历史；末轮/最佳检索/最佳满足率三组保存特征重算检索、九边几何、r/u/q及精确rank；检查选模与进程退出。

机器结果（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/comparison.json`） · CSV（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/comparison.csv`） · 核验（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/audit.json`） · 运行记录（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-28-lambda03-results/launch.json`）

远端状态未核实：git fetch被自动审批拒绝。本次仅本地归档，无commit/push/upload。
