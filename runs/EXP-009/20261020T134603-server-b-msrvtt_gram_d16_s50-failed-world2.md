# GRAM 16D：原双卡失败尝试

| 字段 | 内容 |
|---|---|
| 实验卡 | [EXP-009](../../experiments/EXP-009-lowdim-finetune.md) |
| run ID | `20261020T134603-server-b-msrvtt_gram_d16_s50-failed-world2` |
| 服务器 / 状态 | server-b / FAILED |
| 开始时间 | 2026-10-20T13:46:03.544555+00:00 |
| 配置 | seed50，16D，world size=2，全局 batch64 |
| PID / GPU | 2866691 / 1, 3 |
| 失败原因 | 进程分配上限 29.6328125 GiB 触发 CUDA OOM；报错时物理卡仍有约 45.12 GiB 空闲 |
| 影响 | 未完成一个训练 epoch；不计入 43 组完成结果 |
| 证据 | 失败文件 SHA-256 `1fd64184737e8b536c0fd2af6e340f9fa3600c1061af834d128087dbd9c5d1a7`；原路径见 [运行清单](../../results/EXP-009/2026-10-20-server-b/provenance/run_provenance.json) |
| 恢复 | [独立单卡重跑](./20261020T142250-server-b-msrvtt_gram_d16_s50.md)，原失败文件与 epoch0 产物保留 |

该失败是显存分配限额问题，不能记作模型收敛或检索结果。单卡重跑经用户明确要求跳过新增预检；world size 从 2 变为 1，全局 batch 仍为 64。
