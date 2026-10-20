# Parent 构造与蕴含约束消融

[返回实验总览](../README.md)

| 字段 | 内容 |
|---|---|
| 编号 | EXP-001 |
| 项目 | Hyperbolic-Omnimodal |
| 状态 | 已完成验证；无本轮测试集结果 |
| 实验日期 / 最后核对 | 2026-10-14 / 2026-10-20 |
| 后续 | [子集层级初版](EXP-002-subset-pilot.md) |

## 要回答的问题

固定本机 M 配置后，Perron、Text、SVD parent 是否相对 E0 改善检索，并形成有效锥包含？

## 协议与运行

512 维，seed 50，四组各 1,360 步；Perron/Text/SVD 的约束权重为 0.1。主比较是 Perron 对本机 E0。八卡全局 batch 64。本轮属于独立探索，不与服务器 A 的结果直接配对。

精确设置与运行清单见[执行方案](../../Hyperbolic-Omnimodal/experiments/next_steps/SERVER_B_EXECUTION_20261014.md)和[运行目录](../../Hyperbolic-Omnimodal/outputs/server_b_20261014/)。

## 结果

以下均为 holdout R@1，单位 %；ITC 为 Stage-1，ITM 为重排。

| 条件 | ITC | ITM | 音频 |
|---|---:|---:|---:|
| E0 | 41.95 | 54.30 | 4.75 |
| Perron λ=0.1 | 41.70 | 54.45 | 4.70 |
| Text λ=0.1 | 41.80 | 54.60 | 4.80 |
| SVD λ=0.1 | 42.05 | 54.40 | 4.75 |

带蕴含约束的三组锥满足率均为 0%。原始[汇总表](../results/EXP-001/2026-10-20/summary.md)、[结构化结果](../results/EXP-001/2026-10-20/summary.json)、[完成状态](../../Hyperbolic-Omnimodal/outputs/server_b_20261014/controller_status.json)。

## 结论与下一步

检索差异很小，未观察到明确的 parent 构造收益或严格包含成功。单种子验证结果不足以支持稳定优势；测试栏为空，不能当作测试结果。后续转向显式子集关系，见 EXP-002。

## 变更记录

- 2026-10-14：首个 smoke 因 allocator cap 失败；第二个 attempt 调整资源上限后通过，正式四组完成。失败记录保留。
- 2026-10-20：根据现存执行文档与结果补录实验卡。
