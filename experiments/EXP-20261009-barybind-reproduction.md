# BaryBind 公开实现复现：匹配预算后各数据集增益不同

[返回实验总览](../README.md) · `EXP-20261009-barybind-reproduction` · 原结果 2026-10-09 至 10-10 · 文档更新 2026-11-19

四集本机复现以 T↔VA、Top-50 ITM 比较。MSR-VTT 上 BaryBind 末态为 **52.941/50.905%**（T→V/V→T），比同预算 PMRL 高 **1.584/0.566pp**。ActivityNet 则低 **0.677/0.527pp**。软势函数 WB 修订的选优增益在四集八方向平均上未超过原复现选优。

## 研究问题与关键设置

VAST 初始化、86,707 条训练样本、seed50、global batch128、3,263 次尝试。四集使用本地可用视频和全部 caption。不同方法实际 AMP 有效更新数见原文。MSR-VTT 预定最终 checkpoint 为主结果，test 参与选模的保留为探索性对照。

## BaryBind 相对同预算 PMRL 最终权重

| 数据集 | T→V Δ R@1 (pp) | V→T Δ R@1 (pp) |
|---|---:|---:|
| MSR-VTT | +1.584 | +0.566 |
| DiDeMo | +0.201 | +0.201 |
| ActivityNet | −0.677 | −0.527 |
| VATEX | −0.180 | +0.000 |

WB 修订保留软势函数，修复梯度与输入映射。按 MSR-VTT test 选优的第 700 步，相对原复现第 1,100 步四集八方向平均 ITM R@1 下降 0.268pp。本机数据和预算小于原论文协议，报告局限于单 seed。

[原复现与 WB 各集结果](../summaries/recent-20261119/barybind-reproduction.md)

## 结果来源

本地 `workspace/BaryBind/reproduction/REPORT.md`，SHA-256 `0243677a3b15ba9a9a3ef4a731d18c371062368c08d21769c989de5b8fff9c8d`。

本地 `dataset_root/BaryBind/runs/wb_soft_train_20261009/COMPARISON.md`，SHA-256 `42b9ebca4cc2979f3d758b31d95331cd77b83ecff4cc6270312c5e5d833ba428`。

本地 `dataset_root/BaryBind/runs/wb_soft_step700_eval_20261010/SELECTED_COMPARISON.md`，SHA-256 `b53a542fbd809772386fafa694c39c870eba1e80ebeef3b1ebe4f53b50a5bbaa`。
