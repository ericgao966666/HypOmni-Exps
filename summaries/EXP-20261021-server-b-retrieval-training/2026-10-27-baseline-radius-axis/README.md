# R0/R3 半径图：baseline 独立纵轴

> 本页是用于 GitHub 阅读的 Markdown 报告，保留原报告的数值、结论与局限。分层整理日期：2026-11-05；实验核对时间沿用原文。
> 原文仅存本地：`results/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/README.md`；原文 SHA-256：`d5385e51251bf86af6c302ef7977eeb934969b81ce24a9fbccfea3e9ef78d073`。数据、图件和运行记录的访问方式见[本地证据说明](../../../LOCAL_ARTIFACTS.md)。

2026-10-27 图版调整。复用 10-23 的全部验证特征和既有 HoroPCA/CO-SNE 投影，不重新训练或拟合投影。

右上 R0（10-epoch baseline）的半径纵轴独立放大至约 0.9835–1.0324，以显示接近 1 的分布；右下 R3 保持 0.8–3.6。上下箱体的视觉高度不可直接比较，请读取各自刻度。箱体、5%–95% 须线及所有实验数值不变。

独立 baseline 半径纵轴（图件仅存本地：`results/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/geometry_R0_vs_R3.png`）

本图 PDF（本地：`results/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/geometry_R0_vs_R3.pdf`） · [原版报告及统一纵轴图](../2026-10-23-geometry-validation/README.md) · 绘图脚本（本地：`results/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/redraw.py`） · 输入哈希与核验（本地：`results/EXP-20261021-server-b-retrieval-training/2026-10-27-baseline-radius-axis/provenance.json`）

数据：MSRVTT 验证集 500 视频，64D，训练 seed50；投影为相同的 48 视频 × 7 子集，投影 seed50。R0/R3 分别为检索选出的 epoch5/epoch7，严格锥满足率均为 0%。
