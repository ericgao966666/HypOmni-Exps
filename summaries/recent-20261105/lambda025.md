# λ=0.25：曲率与温度联合学习的匹配实验

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/Hyperbolic-Omnimodal/code/outputs/c0_temperature_curvature_lambda025_20261028/analysis/REPORT.md`；SHA-256：`e997597fc916340a528e06386f834fd0c1b18260fa4dce67543d3496efb14de4`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

已完成30轮、9660步；512D、seed50、VAST验证2048条、六方向macro。只改变λ，与0.2/0.3/0.5保持相同初始化、数据顺序及训练算法。主结果固定epoch30；没有微调或测试集评估。

| λ | R@1↑ | R@5↑ | R@10↑ | 平均超锥角↓ | 严格合法满足率↑ | 最终c | 最终τ |
|---|---|---|---|---|---|---|---|
| 0.2 | **18.750** | **37.288** | **46.737** | 70.801 | **0.000** | 0.617123 | 0.043651 |
| 0.25 | <ins>18.457</ins> | <ins>36.833</ins> | <ins>46.411</ins> | 60.022 | **0.000** | 0.617099 | 0.043588 |
| 0.3 | 18.107 | 36.353 | 45.931 | 52.064 | **0.000** | 0.617120 | 0.043542 |
| 0.5 | 16.960 | 34.945 | 44.263 | 33.931 | **0.000** | 0.617219 | 0.043423 |

λ=.2→.25：R@1变化 -0.293 个百分点，平均超锥角变化 -10.779°。
λ=.25→.3：R@1变化 -0.350 个百分点，平均超锥角变化 -7.958°。

超锥角降低不等于严格蕴含成立；仅单seed验证结果，不表示统计显著性或测试收益。

核验通过：45个产物哈希；完整30轮历史；末轮/最佳检索/最佳满足率三组保存特征重算检索、九边几何、r/u/q及精确rank；检查选模与进程退出。

机器结果（本地 `workspace/Hyperbolic-Omnimodal/code/outputs/c0_temperature_curvature_lambda025_20261028/analysis/comparison.json`） · CSV（本地 `workspace/Hyperbolic-Omnimodal/code/outputs/c0_temperature_curvature_lambda025_20261028/analysis/comparison.csv`） · 核验（本地 `workspace/Hyperbolic-Omnimodal/code/outputs/c0_temperature_curvature_lambda025_20261028/verification/audit.json`） · 运行记录（本地 `workspace/Hyperbolic-Omnimodal/code/outputs/c0_temperature_curvature_lambda025_20261028/logs/launch.json`）

原实验当时仅独立本地归档，未提交或上传；本页与实验索引在本次近期结果补录中发布。
