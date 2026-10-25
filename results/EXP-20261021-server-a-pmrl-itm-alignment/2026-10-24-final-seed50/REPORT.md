# PMRL ITM 实验结果

固定末轮；四数据集 × 双向 R@1 等权平均，单位 %。
不同 seed 数分别排名；单种子不估计训练方差。

| 采样 | 候选 | 融合权重 | Seeds | 平均 R@1 ± 样本标准差 |
|---|---|---:|---:|---:|
| legacy_va | legacy_va | 0.0 | 1 | 57.2519 |
| legacy_va | legacy_va | 1.0 | 1 | 48.5816 |
| legacy_va | tv | 0.0 | 1 | 57.5799 |
| legacy_va | tv | 1.0 | 1 | 51.6185 |
| legacy_va | mean_tv_ta | 0.0 | 1 | 57.1837 |
| legacy_va | mean_tv_ta | 1.0 | 1 | 45.8464 |
| legacy_va | sigma_max | 0.0 | 1 | 55.9533 |
| legacy_va | sigma_max | 1.0 | 1 | 42.8976 |
| tv | legacy_va | 0.0 | 1 | 57.3998 |
| tv | legacy_va | 1.0 | 1 | 48.1434 |
| tv | tv | 0.0 | 1 | 57.5385 |
| tv | tv | 1.0 | 1 | 51.9240 |
| tv | mean_tv_ta | 0.0 | 1 | 57.1454 |
| tv | mean_tv_ta | 1.0 | 1 | 45.4883 |
| tv | sigma_max | 0.0 | 1 | 56.0965 |
| tv | sigma_max | 1.0 | 1 | 42.8214 |
| mean_tv_ta | legacy_va | 0.0 | 1 | 57.7343 |
| mean_tv_ta | legacy_va | 1.0 | 1 | 48.3931 |
| mean_tv_ta | tv | 0.0 | 1 | **58.0271** |
| mean_tv_ta | tv | 1.0 | 1 | 51.8406 |
| mean_tv_ta | mean_tv_ta | 0.0 | 1 | 57.6418 |
| mean_tv_ta | mean_tv_ta | 1.0 | 1 | 45.9886 |
| mean_tv_ta | sigma_max | 0.0 | 1 | 56.4578 |
| mean_tv_ta | sigma_max | 1.0 | 1 | 43.1506 |
| sigma_max | legacy_va | 0.0 | 1 | 57.6739 |
| sigma_max | legacy_va | 1.0 | 1 | 47.9423 |
| sigma_max | tv | 0.0 | 1 | <ins>57.9886</ins> |
| sigma_max | tv | 1.0 | 1 | 51.4771 |
| sigma_max | mean_tv_ta | 0.0 | 1 | 57.6825 |
| sigma_max | mean_tv_ta | 1.0 | 1 | 45.3940 |
| sigma_max | sigma_max | 0.0 | 1 | 56.5213 |
| sigma_max | sigma_max | 1.0 | 1 | 42.3943 |

完整方向、评分交叉表及条件于单个训练种子的配对 bootstrap 区间见 results.json。
测试结果不参与候选、融合或采样方案的选择。
