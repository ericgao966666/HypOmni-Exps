# PMRL Parent 消融：代理父节点的小幅检索差值缺少层级支持

[返回实验总览](../README.md) · `EXP-20260929-pmrl-parent-proxies` · 原结果 2026-09-28 至 09-30 · 文档更新 2026-11-19

VAST 配对预算下，学习半径的 SVD parent 与同预算 PMRL 的 Top-50 八方向平均 R@1 分别为 **59.5875%** 和 **59.5750%**。各代理相对 Text parent 的差值很小。冻结类别探针上，AudioCaps 的祖先 F1 仍低于 PMRL，三个双曲组在两个数据集的正例锥满足率均为 0。

## 研究问题与关键设置

共同 VAST 初始权重、86,707 条、seed50、global batch64、1,360 次有效更新，使用末轮权重。下面为 MSR-VTT、DiDeMo、ActivityNet、VATEX 的 T→V/V→T R@1 等权平均 (%)。Mean/ SVD 是切空间均值或首奇异向量构造；谱目标保留 Text anchor，代理仅用于 parent 约束。

| Parent | 直接检索 R@1 | Top-50 R@1 |
| --- | --- | --- |
| PMRL matched | 46.0250 | <ins>59.5750</ins> |
| 无 entailment | <ins>46.1250</ins> | 59.4250 |
| Text | **46.1375** | 59.4750 |
| Mean α=0.5 | 46.0875 | 59.5125 |
| Mean α=1 | 46.0000 | 59.3375 |
| SVD + mean radius | 46.0750 | 59.4625 |
| SVD + learned radius | 45.9625 | **59.5875** |

## 低维、分类和纯音频

- 64D 同维度无锥组 Top-50 为 58.4000%，Mean parent 为 58.6125%。16D 无锥 46.2500%，Text parent 46.4250%。PCA 只由 VAST train 拟合，各组单 seed。原报告的 bootstrap 衡量查询抽样，未覆盖训练种子。
- 冻结类别探针中，MSR-VTT Text-parent mAP 为 35.73%，PMRL 为 32.72%。AudioCaps→AudioSet 祖先 F1@1 最高为 PMRL 的 39.66%，双曲三个组为 34.51–35.26%。严格正例锥满足为 0%，Text-parent 的部分半径排序优势没有转化为包含。
- 纯音频直检使用四份 seed50 的第 1,360 步权重，AudioCaps 704、Clotho 1,045，首条 caption、无 ITM。AudioCaps 上 PMRL 和 Text-parent 的 T→A/A→T R@1 为 28.84/29.69% 和 27.41/23.15%。Clotho 为 15.60/13.88% 和 14.26/10.43%。

## 结果来源

本地 `workspace/PMRL-minimal-hyperbolic/docs/PROXY_PARENT_RESULTS_20260929.md`，SHA-256 `4843cade1b9c61f8046887019383c06d3883985f159498d3a8023712d3b608a2`。

本地 `workspace/PMRL-minimal-hyperbolic/docs/CATEGORY_HIERARCHY_RESULTS_20260929.md`，SHA-256 `0a70b38fd96e1313cf9ea48dbed3f9b972ac8671cbcb79957c311c8512595ff6`。

本地 `dataset_root/PMRL/outputs/entailment_ablation_20260928/REPORT.md`，SHA-256 `d3528b45bf45f09bde88ed99144ffa458a0ef924ddfb3ab022b44174d49a28fa`。

本地 `dataset_root/PMRL/outputs/parent_alpha1_20260929/REPORT.md`，SHA-256 `d5ed6dffd470e158f0152bcdc31a667bd6c267524cbd9ca704d75b3e8bbd3a4c`。

本地 `dataset_root/PMRL/outputs/svd_parent_20260929/REPORT.md`，SHA-256 `44f6690c095ec2de3c0d385799a0b5262b7bdbb9a61dbbf3049fb66e94cc4c7a`。

本地 `dataset_root/PMRL/outputs/lowdim_parent_20260929/FINAL_REPORT.md`，SHA-256 `ce56a10410414d8ff3dab357c1cd806e68f33dc76ae87b337a295fd4467cafdc`。

本地 `dataset_root/PMRL/outputs/audio_text_eval_20260929_side/REPORT.md`，SHA-256 `b3f33a200b4d23faad6a76f839140ccd63ec830bd3cb234efc97ba734f9f2857`。
