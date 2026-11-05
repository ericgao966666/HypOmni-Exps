# λ=.2：两组独立半径分布图与梯度符号

> 本页是用于 GitHub 阅读的 Markdown 报告，保留原报告的数值、结论与局限。分层整理日期：2026-11-05；实验核对时间沿用原文。
> 原文仅存本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/README.md`；原文 SHA-256：`e8a07a959a5963284fd634d43a9049ffa9b6c404d7745b109aab73da83335335`。数据、图件和运行记录的访问方式见[本地证据说明](../../../LOCAL_ARTIFACTS.md)。

两图使用同一坐标范围；每个头2048条验证样本，真实512D特征重算测地半径r，第30轮、seed50。小提琴显示密度，白色箱体为IQR，黑线为中位数，须线为P5–P95。半径是正数，灰色虚线标注模型允许范围.21–4。

## 固定c=1、τ=.035

固定参数半径分布（图件仅存本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/radius_fixed_tau0035_c1_lambda02.png`）

PDF（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/radius_fixed_tau0035_c1_lambda02.pdf`）

## 联合学习c和τ

初始c=1、τ=.07；末轮c=.617123、τ=.043651。

联合学习半径分布（图件仅存本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/radius_learned_c_tau_lambda02.png`）

PDF（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/radius_learned_c_tau_lambda02.pdf`）

全部14个头的数值统计（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/radius_statistics.csv`） · 图版来源和哈希（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/provenance.json`）

## 为什么梯度图有负数

梯度轨迹图中的cosine是两项损失梯度的夹角余弦，取值可在[-1,1]；负值表示它们在该参数组上的局部方向存在冲突。梯度范数及λ加权范数比例必须非负，已核对本轮13组所有保存的相关记录均非负。

统一物理半径缩放诊断令r→a r，在a=1处测dL/da，保持方向、c和τ不变。负值表示增大a会局部降低损失，对应梯度下降的扩张方向；正值对应收缩方向。它是局部诊断，不是实际AdamW对全部模型参数的更新，也不表示半径或损失为负。

| 设置 | 对比损失dL/da | λ·蕴含损失dL/da | 总dL/da | 投影梯度余弦 | 径向头梯度余弦 |

| --- | ---: | ---: | ---: | ---: | ---: |

| 固定c、τ | -0.228007 | +0.204472 | -0.023535 | -0.080581 | -0.778675 |

| 联合学习c、τ | -0.203541 | +0.189634 | -0.013907 | -0.111320 | -0.836278 |

以上梯度来自固定256条训练probe的第30轮副本，和用于半径分布的2048条验证样本是不同读出。原始末轮梯度数值（本地：`results/EXP-20261027-server-b-c0-temperature-curvature/2026-10-27-lambda02-radius-focus/gradient_endpoints.csv`）。

本次仅新增图表和说明；读取原有检查点，无新增训练。旧图和旧结果快照保留。
