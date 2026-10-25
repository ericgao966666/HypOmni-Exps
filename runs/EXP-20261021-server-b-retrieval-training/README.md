# EXP-20261021-server-b-retrieval-training 运行记录

首批运行如下。后续自动队列的逐次命令、PID、GPU、日志及时间记录于本机 `launchers.jsonl`。

| run ID | 条件 | 已核对状态 |
|---|---|---|
| [20261021T044831-server-b-train-hyp_cone_d64_s50_R1-joint](20261021T044831-server-b-train-hyp_cone_d64_s50_R1-joint.md) | hyp_cone / 64D / seed50 / R1 / joint | 已启动，状态快照时间 2026-10-21T04:51:56.001370+00:00 |
| [20261021T044831-server-b-train-hyp_cone_d64_s50_R2-joint](20261021T044831-server-b-train-hyp_cone_d64_s50_R2-joint.md) | hyp_cone / 64D / seed50 / R2 / joint | 已启动，状态快照时间 2026-10-21T04:51:56.001370+00:00 |
| [20261021T044831-server-b-train-euc_none_d64_s50_R1-joint](20261021T044831-server-b-train-euc_none_d64_s50_R1-joint.md) | euc_none / 64D / seed50 / R1 / joint | 已启动，状态快照时间 2026-10-21T04:51:56.001370+00:00 |
| [20261021T044831-server-b-train-euc_none_d64_s50_R2-joint](20261021T044831-server-b-train-euc_none_d64_s50_R2-joint.md) | euc_none / 64D / seed50 / R2 / joint | 已启动，状态快照时间 2026-10-21T04:51:56.001370+00:00 |
| [20261021T044831-server-b-vast_pooled_cache](20261021T044831-server-b-vast_pooled_cache.md) | VAST frozen pooled feature extraction; deterministic inputs | 已启动，状态快照时间 2026-10-21T04:51:56.001370+00:00 |

## 2026-10-21 独立候选提前并行

原五个工作进程保留，新协调器统一调度，原生候选提前使用GPU5/6/7。

| run ID | 条件 | 核对状态 |
|---|---|---|
| [20261021T054524-server-b-train-vast_d64_s50_R1-joint](20261021T054524-server-b-train-vast_d64_s50_R1-joint.md) | vast / 64D / seed50 / R1 | 已进入正式训练 |
| [20261021T054524-server-b-train-gram_d64_s50_R1-joint](20261021T054524-server-b-train-gram_d64_s50_R1-joint.md) | gram / 64D / seed50 / R1 | 已进入正式训练 |
| [20261021T054524-server-b-train-pmrl_d64_s50_R1-joint](20261021T054524-server-b-train-pmrl_d64_s50_R1-joint.md) | pmrl / 64D / seed50 / R1 | 已进入正式训练 |

- [20261022T060839-server-b-train-pmrl_d64_s50_R3-warmup](20261022T060839-server-b-train-pmrl_d64_s50_R3-warmup.md)

- [20261022T062336-server-b-train-hyp_cone_d64_s51_R0-joint](20261022T062336-server-b-train-hyp_cone_d64_s51_R0-joint.md)

- [20261022T062336-server-b-train-hyp_cone_d64_s52_R0-joint](20261022T062336-server-b-train-hyp_cone_d64_s52_R0-joint.md)

- [20261022T062336-server-b-train-euc_none_d64_s51_R0-joint](20261022T062336-server-b-train-euc_none_d64_s51_R0-joint.md)

- [20261023T034825-server-b-train-vast_d64_s50_R3-frozen](20261023T034825-server-b-train-vast_d64_s50_R3-frozen.md)

- [20261023T043728-server-b-train-hyp_cone_d64_s51_R1-joint](20261023T043728-server-b-train-hyp_cone_d64_s51_R1-joint.md)

- [20261023T055545-server-b-train-hyp_cone_d64_s52_R1-joint](20261023T055545-server-b-train-hyp_cone_d64_s52_R1-joint.md)

- [20261023T060415-server-b-train-euc_none_d64_s51_R1-joint](20261023T060415-server-b-train-euc_none_d64_s51_R1-joint.md)

- [20261023T063408-server-b-train-hyp_cone_d32_s50_R1-joint](20261023T063408-server-b-train-hyp_cone_d32_s50_R1-joint.md)

- [20261023T063408-server-b-train-euc_none_d32_s50_R1-joint](20261023T063408-server-b-train-euc_none_d32_s50_R1-joint.md)

- [20261023T063408-server-b-train-hyp_cone_d128_s50_R1-joint](20261023T063408-server-b-train-hyp_cone_d128_s50_R1-joint.md)

- [20261023T064848-server-b-train-gram_d64_s50_R3-frozen](20261023T064848-server-b-train-gram_d64_s50_R3-frozen.md)

- [20261023T070240-server-b-train-pmrl_d64_s50_R3-warmup](20261023T070240-server-b-train-pmrl_d64_s50_R3-warmup.md)

- [20261023T074334-server-b-geometry64-validation-seed50](20261023T074334-server-b-geometry64-validation-seed50.md)

- [20261023T110614-server-b-train-vast_d64_s50_R3-joint](20261023T110614-server-b-train-vast_d64_s50_R3-joint.md)

- [20261024T081258-server-b-train-pmrl_d64_s50_R3-frozen](20261024T081258-server-b-train-pmrl_d64_s50_R3-frozen.md)

- [20261024T090647-server-b-method_test-hyp_cone_d64_s50_R1-joint](20261024T090647-server-b-method_test-hyp_cone_d64_s50_R1-joint.md)

- [20261024T090647-server-b-method_test-hyp_cone_d64_s50_R0-joint](20261024T090647-server-b-method_test-hyp_cone_d64_s50_R0-joint.md)

- [20261024T090647-server-b-method_test-euc_none_d64_s50_R1-joint](20261024T090647-server-b-method_test-euc_none_d64_s50_R1-joint.md)

- [20261024T090647-server-b-method_test-vast_d64_s50_R3-joint](20261024T090647-server-b-method_test-vast_d64_s50_R3-joint.md)

- [20261024T090647-server-b-method_test-gram_d64_s50_R1-joint](20261024T090647-server-b-method_test-gram_d64_s50_R1-joint.md)

- [20261024T090702-server-b-method_test-euc_none_d64_s50_R0-joint](20261024T090702-server-b-method_test-euc_none_d64_s50_R0-joint.md)

## 2026-10-25 完成与中断补录

核对：2026-10-25T07:22:03.941622+00:00。已完成14/20个选定条件及2个R0对照；训练进程当前已退出，剩余6条件未完成。

- [20261021T044353-server-b-train-hyp_cone_d64_s50_R1-joint](20261021T044353-server-b-train-hyp_cone_d64_s50_R1-joint.md)
- [20261021T044353-server-b-train-hyp_cone_d64_s50_R2-joint](20261021T044353-server-b-train-hyp_cone_d64_s50_R2-joint.md)
- [20261021T044353-server-b-train-euc_none_d64_s50_R1-joint](20261021T044353-server-b-train-euc_none_d64_s50_R1-joint.md)
- [20261021T044353-server-b-train-euc_none_d64_s50_R2-joint](20261021T044353-server-b-train-euc_none_d64_s50_R2-joint.md)
- [20261021T055332-server-b-train-vast_d64_s50_R2-joint](20261021T055332-server-b-train-vast_d64_s50_R2-joint.md)
- [20261021T055638-server-b-train-gram_d64_s50_R2-joint](20261021T055638-server-b-train-gram_d64_s50_R2-joint.md)
- [20261021T071412-server-b-train-pmrl_d64_s50_R2-joint](20261021T071412-server-b-train-pmrl_d64_s50_R2-joint.md)
- [20261021T072813-server-b-train-hyp_cone_d64_s50_R3-warmup](20261021T072813-server-b-train-hyp_cone_d64_s50_R3-warmup.md)
- [20261021T072813-server-b-train-euc_none_d64_s50_R3-warmup](20261021T072813-server-b-train-euc_none_d64_s50_R3-warmup.md)
- [20261021T073129-server-b-train-hyp_cone_d64_s50_R3-frozen](20261021T073129-server-b-train-hyp_cone_d64_s50_R3-frozen.md)
- [20261021T073129-server-b-train-euc_none_d64_s50_R3-frozen](20261021T073129-server-b-train-euc_none_d64_s50_R3-frozen.md)
- [20261021T074309-server-b-train-euc_none_d64_s50_R3-joint](20261021T074309-server-b-train-euc_none_d64_s50_R3-joint.md)
- [20261021T074410-server-b-train-hyp_cone_d64_s50_R3-joint](20261021T074410-server-b-train-hyp_cone_d64_s50_R3-joint.md)
- [20261021T084316-server-b-train-vast_d64_s50_R3-warmup](20261021T084316-server-b-train-vast_d64_s50_R3-warmup.md)
- [20261021T092953-server-b-train-gram_d64_s50_R3-warmup](20261021T092953-server-b-train-gram_d64_s50_R3-warmup.md)
- [20261021T130816-server-b-train-vast_d64_s50_R3-frozen](20261021T130816-server-b-train-vast_d64_s50_R3-frozen.md)
- [20261021T135115-server-b-train-gram_d64_s50_R3-frozen](20261021T135115-server-b-train-gram_d64_s50_R3-frozen.md)
- [20261022T094426-server-b-train-vast_d64_s50_R3-frozen](20261022T094426-server-b-train-vast_d64_s50_R3-frozen.md)
- [20261022T150607-server-b-train-gram_d64_s50_R3-frozen](20261022T150607-server-b-train-gram_d64_s50_R3-frozen.md)
- [20261022T193249-server-b-train-pmrl_d64_s50_R3-warmup](20261022T193249-server-b-train-pmrl_d64_s50_R3-warmup.md)
- [20261023T084459-server-b-train-pmrl_d64_s50_R3-frozen](20261023T084459-server-b-train-pmrl_d64_s50_R3-frozen.md)
- [20261023T124524-server-b-train-pmrl_d64_s50_R3-frozen](20261023T124524-server-b-train-pmrl_d64_s50_R3-frozen.md)
- [20261023T124709-server-b-train-gram_d64_s50_R3-frozen](20261023T124709-server-b-train-gram_d64_s50_R3-frozen.md)
- [20261023T160902-server-b-train-pmrl_d64_s50_R3-frozen](20261023T160902-server-b-train-pmrl_d64_s50_R3-frozen.md)
- [20261024T075456-server-b-train-gram_d64_s50_R3-joint](20261024T075456-server-b-train-gram_d64_s50_R3-joint.md)
- [20261024T201844-server-b-train-pmrl_d64_s50_R3-joint](20261024T201844-server-b-train-pmrl_d64_s50_R3-joint.md)
- [20261024T212040-server-b-method_test-pmrl_d64_s50_R3-joint](20261024T212040-server-b-method_test-pmrl_d64_s50_R3-joint.md)
- [20261024T212155-server-b-train-hyp_cone_d32_s50_R1-joint](20261024T212155-server-b-train-hyp_cone_d32_s50_R1-joint.md)
- [20261024T212155-server-b-train-hyp_cone_d128_s50_R1-joint](20261024T212155-server-b-train-hyp_cone_d128_s50_R1-joint.md)
- [20261024T212155-server-b-train-hyp_cone_d512_s50_R1-joint](20261024T212155-server-b-train-hyp_cone_d512_s50_R1-joint.md)
- [20261024T212155-server-b-train-euc_none_d32_s50_R1-joint](20261024T212155-server-b-train-euc_none_d32_s50_R1-joint.md)
- [20261024T212155-server-b-train-euc_none_d128_s50_R1-joint](20261024T212155-server-b-train-euc_none_d128_s50_R1-joint.md)
- [20261024T232735-server-b-method_test-hyp_cone_d512_s50_R1-joint](20261024T232735-server-b-method_test-hyp_cone_d512_s50_R1-joint.md)
- [20261024T234704-server-b-train-euc_none_d512_s50_R1-joint](20261024T234704-server-b-train-euc_none_d512_s50_R1-joint.md)
- [20261024T234719-server-b-train-gram_d32_s50_R1-joint](20261024T234719-server-b-train-gram_d32_s50_R1-joint.md)
- [20261024T235803-server-b-train-gram_d128_s50_R1-joint](20261024T235803-server-b-train-gram_d128_s50_R1-joint.md)
- [20261024T235803-server-b-method_test-euc_none_d128_s50_R1-joint](20261024T235803-server-b-method_test-euc_none_d128_s50_R1-joint.md)
- [20261024T235803-server-b-method_test-hyp_cone_d32_s50_R1-joint](20261024T235803-server-b-method_test-hyp_cone_d32_s50_R1-joint.md)
- [20261024T235803-server-b-method_test-hyp_cone_d128_s50_R1-joint](20261024T235803-server-b-method_test-hyp_cone_d128_s50_R1-joint.md)
- [20261025T003252-server-b-method_test-euc_none_d32_s50_R1-joint](20261025T003252-server-b-method_test-euc_none_d32_s50_R1-joint.md)
- [20261025T014108-server-b-train-gram_d512_s50_R1-joint](20261025T014108-server-b-train-gram_d512_s50_R1-joint.md)
- [20261025T014108-server-b-method_test-euc_none_d512_s50_R1-joint](20261025T014108-server-b-method_test-euc_none_d512_s50_R1-joint.md)
- [20261025T015950-server-b-method_test-gram_d128_s50_R1-joint](20261025T015950-server-b-method_test-gram_d128_s50_R1-joint.md)
- [20261025T023056-server-b-method_test-gram_d32_s50_R1-joint](20261025T023056-server-b-method_test-gram_d32_s50_R1-joint.md)
- [20261025T023111-server-b-train-vast_d32_s50_R3-warmup](20261025T023111-server-b-train-vast_d32_s50_R3-warmup.md)
- [20261025T034851-server-b-method_test-gram_d512_s50_R1-joint](20261025T034851-server-b-method_test-gram_d512_s50_R1-joint.md)
