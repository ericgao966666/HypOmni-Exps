# 冻结 MSR-VTT 的谱 proxy 与残差依赖诊断

[返回实验总览](../README.md) · `EXP-20261012-msrvtt-spectral-proxy-dependence` · 原结果 2026-10-12（保留的完成记录） · 文档更新 2026-11-19

冻结特征的校准诊断中，完整 proxy 的 9 项主检查有 **5 项**通过，leave-one-out 的 **9 项均通过**。项目完成记录指出测试复现验证。残差按谱方向投影定义，读数衡量依赖，无法据此识别特定模态语义。

## 关键设置与证据

相同 VAST 冻结特征，8,811 条音视频样本全部完成提取，按 7,127/800/884 划为拟合、验证、测试。proxy 为归一化模态矩阵的首特征方向，经模态均值定向；leave-one-out 不用目标模态计算方向。验证和测试分别完成 199 次配对置换及 199 次 Gaussian 对照。低 eigengap 和残差消失按协议剔除并计数。

| 主检查 | 通过项 |
|---|---:|
| 完整 proxy | 5/9 |
| Leave-one-out proxy | 9/9 |

完成记录保留了测试锁核验和协议，本机目前无法访问其注明的原始报告 `dataset_root/PMRL-Reconstruction/msrvtt_hypothesis_diagnostics_20261012/REPORT.md`。本卡保留完成记录支持的摘要。

## 结果来源

本地 `workspace/PMRL-Reconstruction/research/msrvtt_hypothesis_diagnostics/README.md`，SHA-256 `0a7712879dc6f73d37451e6932a1017c95c2a3bd867faaf499539db10d706226`。
