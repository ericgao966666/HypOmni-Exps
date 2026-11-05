# Paired VAST-86.7K zero-shot results

> 本页是用于 GitHub 阅读的 Markdown 报告，保留原报告的数值、结论与局限。分层整理日期：2026-11-05；实验核对时间沿用原文。
> 原文仅存本地：`results/EXP-001/2026-10-20/zero_shot/paired_zeroshot.md`；原文 SHA-256：`8073ee3a730587f26a334013ccbee3ff95195ea3964685807f75e1cac54203e4`。数据、图件和运行记录的访问方式见[本地证据说明](../../../../LOCAL_ARTIFACTS.md)。

Final checkpoint, Top-50; mean ± sample standard deviation over seeds.

| method | MSR-VTT T→V | MSR-VTT V→T | DiDeMo T→V | DiDeMo V→T | ActivityNet T→V | ActivityNet V→T | VATEX T→V | VATEX V→T |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| PMRL (local paired) | 55.40 ± 0.44 | 52.37 ± 0.55 | 54.17 ± 0.32 | 51.67 ± 0.46 | 56.20 ± 0.17 | 50.27 ± 0.42 | 79.57 ± 0.50 | 74.67 ± 0.40 |
| Ours | 55.27 ± 0.46 | 52.67 ± 0.60 | 53.77 ± 0.29 | 52.17 ± 0.15 | 55.93 ± 0.12 | 51.03 ± 0.06 | 79.40 ± 0.20 | 74.07 ± 0.47 |
