# PMRL 重建对照：323 步收益主要来自防坍缩正则

[返回实验总览](../README.md) · `EXP-20260826-pmrl-reconstruction` · 原结果 2026-08 至 09 · 文档更新 2026-11-19

VAST 同起点、固定预算下，SCRR full 在 323 步比 PMRL Stage-1 高 **0.6222pp**，仅用方差/协方差正则比 SCRR full 高 **1.6402pp**。重建项在 136 步有小幅正差，323 步方向反转；仅重建的检索性能随训练显著下降。

## 研究问题与关键设置

SCRR 用谱共识瓶颈重建，控制相同 VAST 初始化、训练 82,717 clips、固定 holdout 4,329 clips、seed50、global batch64。Stage-1 仅用纯余弦检索，在 MSR-VTT 的 884 个可用样本上报告双向 R@1 (%)。不同更新预算按列分别排名。

| 目标 | 136 步 R@1 | 323 步 R@1 |
| --- | --- | --- |
| PMRL Stage-1 | 45.1358 | 44.4004 |
| SCRR full | **46.4367** | 45.0226 |
| 方差/协方差正则 | <ins>46.2104</ins> | **46.6628** |
| 仅重建 | 19.6833 | 5.4299 |
| MSE + direct uniformity | — | <ins>45.8710</ins> |
| 仅 direct uniformity | — | <ins>45.8710</ins> |

## 输入重建、方向诊断与后续证据

- 固定 encoder 的 decoder 筛选使用 512D 全局谱 proxy 和 VAST holdout。统一 d8-w512 的三 seed macro normalized MSE 为 0.872069 ± 0.000176，模态专用为 0.874274 ± 0.006497。2/4/8 帧均过视频门控，按预设规则选 8 帧；文本 MSE 没有达到 0.95 门槛。
- SVD/eigh 的原始方向符号可翻转。定向后的正锥成员率在 PMRL 特征缓存为 99.3%，冻结 VAST holdout 为 79.4%。高离散合成例（85°）仅 13.1%，低共识时符号定向不足以恢复可靠轴。
- SIGReg 的 CPU 可行性审计中，未经缩放的单元球为 102.158，乘 √512 后为 1.105，接近 Gaussian 对照 1.103。该结果影响标准化选择；encoder 输入预热、六臂和 SIGReg 训练方案还缺本机可核对的正式结果表，阶段验收按方案记录区分。

## 结果来源

本地 `workspace/PMRL-Reconstruction/MECHANISM_136_REPORT.md`，SHA-256 `3586bdee6f510f464aff238920edb8a2e38dc1b80a8771ebff1026b631290b31`。

本地 `workspace/PMRL-Reconstruction/SCRR_DESIGN_AND_RESULTS.md`，SHA-256 `78d0b9553b458ff43d2a951ba58e439b9965abdf6b0e81c75d4857ab0eddc2e5`。

本地 `workspace/PMRL-Reconstruction/decoder_selection_global_proxy_vast_20260820_v1_REPORT.md`，SHA-256 `4bcc9b382cc21c9213f24890f62fcf8783eabd200657ea36c97fbfe960bccbae`。

本地 `workspace/PMRL-Reconstruction/svd_proxy_orientation_20260826_REPORT.md`，SHA-256 `638d31244ccddd56c7ab5514512ff0e7c8d5738dcd67254e33237316a8c43487`。

本地 `workspace/PMRL-Reconstruction/research/sigreg_20260908/README.md`，SHA-256 `5b5d4bf264c8b9957f0a9cadebfe9932a2f39530ee83dcc3812895bd7c34bda5`。

本地 `workspace/PMRL-Reconstruction/INPUT_WARMUP_EXPERIMENT.md`，SHA-256 `877a02c45432776be74838c7cf0d17340d03292f29f7342f8cba815c82824566`。

本地 `workspace/PMRL-Reconstruction/SIMPLE_INPUT_PMRL_EXPERIMENT.md`，SHA-256 `4df23f8c499a0d1afdd2b4f767dbe7c91842fa484ccb18c8aafb6294addb633b`。

本地 `workspace/PMRL-Reconstruction/SIGREG_INPUT_EXPERIMENT.md`，SHA-256 `9b2a18d7168499d36deea92acd2e96ac58667795a8b2551c6de07197c086bc42`。
