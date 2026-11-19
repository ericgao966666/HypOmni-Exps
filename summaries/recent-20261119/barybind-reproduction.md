# BaryBind 复现与 WB 修订比较

[返回实验卡](../../experiments/EXP-20261009-barybind-reproduction.md) · 原结果 2026-10-09 至 10-10 · 文档更新 2026-11-19

R@1 为全部 caption 的 top-50 ITM 结果 (%)，各数据集单独排名。PMRL existing 使用已有 1,360 步权重；匹配预算的对照和 BaryBind 使用 3,263 步尝试预算。初始权重仅作起点参考。

## 原复现与对照

### msrvtt

| 配置 | 视频/文本 | T→V R@1 | V→T R@1 |
| --- | --- | --- | --- |
| vast | 884/884 | 49.661 | 44.118 |
| pmrl_existing | 884/884 | **53.054** | **51.471** |
| barybind_initial | 884/884 | 47.624 | 44.005 |
| barybind_final | 884/884 | <ins>52.941</ins> | <ins>50.905</ins> |
| pmrl_matched_budget_final | 884/884 | 51.357 | 50.339 |

### didemo

| 配置 | 视频/文本 | T→V R@1 | V→T R@1 |
| --- | --- | --- | --- |
| vast | 997/997 | 50.050 | 46.640 |
| pmrl_existing | 997/997 | **55.567** | 52.558 |
| barybind_initial | 997/997 | 43.531 | 46.339 |
| barybind_final | 997/997 | <ins>54.865</ins> | **52.859** |
| pmrl_matched_budget_final | 997/997 | 54.664 | <ins>52.658</ins> |

### activitynet

| 配置 | 视频/文本 | T→V R@1 | V→T R@1 |
| --- | --- | --- | --- |
| vast | 3987/3987 | 53.273 | 48.483 |
| pmrl_existing | 3987/3987 | <ins>59.343</ins> | 53.599 |
| barybind_initial | 3987/3987 | 31.026 | 48.658 |
| barybind_final | 3987/3987 | 59.092 | <ins>54.201</ins> |
| pmrl_matched_budget_final | 3987/3987 | **59.769** | **54.728** |

### vatex

| 配置 | 视频/文本 | T→V R@1 | V→T R@1 |
| --- | --- | --- | --- |
| vast | 1224/12240 | 77.663 | **90.850** |
| pmrl_existing | 1224/12240 | **79.371** | 88.807 |
| barybind_initial | 1224/12240 | 75.891 | <ins>90.605</ins> |
| barybind_final | 1224/12240 | 78.881 | 90.523 |
| pmrl_matched_budget_final | 1224/12240 | <ins>79.060</ins> | 90.523 |

## 软势函数 WB 修订

主比较以预定最终权重给出。修订同时改变可学习 WB 映射、MWB 梯度通路和势函数实现，单独组件的贡献尚未隔离。

### msrvtt

| 配置 | T→V R@1 | V→T R@1 |
| --- | --- | --- |
| 原复现最终 | **52.941** | **50.905** |
| WB 修订最终 | <ins>52.376</ins> | <ins>50.679</ins> |

### didemo

| 配置 | T→V R@1 | V→T R@1 |
| --- | --- | --- |
| 原复现最终 | **54.865** | **52.859** |
| WB 修订最终 | <ins>54.162</ins> | <ins>52.658</ins> |

### activitynet

| 配置 | T→V R@1 | V→T R@1 |
| --- | --- | --- |
| 原复现最终 | <ins>59.092</ins> | **54.201** |
| WB 修订最终 | **59.343** | <ins>54.176</ins> |

### vatex

| 配置 | T→V R@1 | V→T R@1 |
| --- | --- | --- |
| 原复现最终 | <ins>78.881</ins> | **90.523** |
| WB 修订最终 | **79.036** | <ins>90.441</ins> |

第 700 步修订权重与原复现第 1,100 步均由 MSR-VTT test T→V 选模。四集八方向均值差为 −0.268pp（修订选优减原复现选优）；修订选优比自身末态高 +0.049pp，作为选模敏感性报告。

本地 `workspace/BaryBind/reproduction/REPORT.md`，SHA-256 `0243677a3b15ba9a9a3ef4a731d18c371062368c08d21769c989de5b8fff9c8d`。

本地 `dataset_root/BaryBind/runs/wb_soft_train_20261009/COMPARISON.md`，SHA-256 `42b9ebca4cc2979f3d758b31d95331cd77b83ecff4cc6270312c5e5d833ba428`。

本地 `dataset_root/BaryBind/runs/wb_soft_step700_eval_20261010/SELECTED_COMPARISON.md`，SHA-256 `b53a542fbd809772386fafa694c39c870eba1e80ebeef3b1ebe4f53b50a5bbaa`。
