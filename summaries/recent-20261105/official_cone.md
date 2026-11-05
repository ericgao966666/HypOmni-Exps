# 官方 HyCoCLIP / UNCHA checkpoint 锥蕴含审计

> 归档核对：2026-11-05T08:39:54.407550+00:00；原实验时间与范围以正文为准。本次未重跑实验。
> 本地原文：`workspace/meru-width-coco/output/official_cone_audit_20261029/REPORT.md`；SHA-256：`5f7688fe9af264a2f5a6373fef665dd330490eb3837d32914a8e4fa996248093`。详细数值和图件仅存本地，见[访问说明](../../LOCAL_ARTIFACTS.md)。

使用作者发布的ViT-B/16 checkpoint，无训练、无微调。COCO val2017共5,000图、25,014图文正配对，与此前MERU审计的标注SHA256一致；另评估本地GRIT开发集5,000图、11,688区域。

两份官方ViT-B权重都存在大量文本域外点。COCO上HyCoCLIP的合法覆盖为0，原始锥clamp后的表观满足率却为98.305%；UNCHA合法覆盖为1.371%，表观满足为99.972%，全样本合法满足仅1.347%。这不是自训对照结果。

UNCHA的失败构成与此前MERU不同：343个合法COCO图文配对中337个满足原始锥（98.251%）；MERU为269个中2个（0.743%）。因此“合法域外占多数、合法域内基本满足”对本次UNCHA原始锥读出成立，对MERU并不成立；HyCoCLIP没有合法配对，条件满足率应记为不可定义而非0。

作者实际采用的图文阈值eta=.7更严格：HyCoCLIP/UNCHA表观满足率为10.054%/9.667%，全样本合法满足率为0%/0.004%（UNCHA仅1对）。因此不能用eta=1的高表观比例代替作者训练阈值符合度。

GRIT区域图→全图：HyCoCLIP合法覆盖38.492%，原始锥合法满足为0%，放宽eta=1.2后为26.865%；UNCHA合法覆盖100%，原始锥和eta=1.2下均为0%。这些官方checkpoint并没有在所有局部→整体关系上实现严格锥包含。预训练数据、训练目标不同，本报告是checkpoint几何描述，不是受控方法优劣排名。

## COCO：全文 → 全图

统一K=.1。合法定义为父、子双方的q=√c||x_space||均≥.2。S/all为合法且满足/全部配对；表观满足率包含clamp后的域外配对。

| 官方模型 | 合法覆盖 % | 表观满足 η=1 % | 合法S/all η=1 % | 表观满足 η=.7 % | 合法S/all η=.7 % | 错配表观 η=1 % |
|---|---:|---:|---:|---:|---:|---:|
| MERU ViT-B（历史审计） | 1.075 | 51.103 | 0.00800 | — | — | 3.870 |
| hycoclip ViT-B | 0.000 | 98.305 | 0.00000 | 10.054 | 0.00000 | 6.336 |
| uncha ViT-B | 1.371 | 99.972 | 1.34725 | 9.667 | 0.00400 | 48.245 |

MERU为既有审计结果，本轮没有重新运行MERU。历史错配构造与本轮不保证完全一致，因此错配列作各模型内部控制，不能直接进行严格跨模型排名。

COCO文本/图像的q分布（图件仅存本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/q_domain.png`）
PDF（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/q_domain.pdf`）。点为中位数，线为P5–P95；虚线q=.2为合法域边界。统计按25,014配对加权。

## GRIT：四类关系

eta=.7用于跨模态两类关系，eta=1.2用于局部→整体的同模态关系。eta=1.2的训练阈值符合度不能等同于原始锥的严格蕴含。

| 模型 | 关系 | 配对数 | 合法覆盖 % | 表观S η=1 % | 合法S/all η=1 % | native eta | 表观S native % | 合法S/all native % | 错配合法S/all native % |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hycoclip | T_to_I | 5000 | 0.000 | 99.220 | 0.000 | 0.7 | 15.120 | 0.000 | 0.000 |
| hycoclip | partT_to_partI | 11688 | 0.000 | 99.393 | 0.000 | 0.7 | 19.858 | 0.000 | 0.000 |
| hycoclip | partI_to_I | 11688 | 38.492 | 0.051 | 0.000 | 1.2 | 69.901 | 26.865 | 0.000 |
| hycoclip | partT_to_T | 11688 | 0.000 | 49.820 | 0.000 | 1.2 | 98.888 | 0.000 | 0.000 |
| uncha | T_to_I | 5000 | 2.520 | 99.960 | 2.500 | 0.7 | 23.320 | 0.120 | 0.000 |
| uncha | partT_to_partI | 11688 | 1.788 | 99.589 | 1.472 | 0.7 | 10.489 | 0.026 | 0.000 |
| uncha | partI_to_I | 11688 | 100.000 | 0.000 | 0.000 | 1.2 | 0.000 | 0.000 | 0.000 |
| uncha | partT_to_T | 11688 | 0.385 | 7.272 | 0.000 | 1.2 | 51.249 | 0.308 | 0.000 |

GRIT开发集是我们本地实验的划分，可能与作者GRIT预训练重叠；这里用于描述已发布表示的几何，不能作为未见样本泛化证据。区域标注为现有全部11,688区域，未按效果筛选。

## 失败类型与精度

完整metrics.csv（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/metrics.csv`）包含合法/非法 × 满足/不满足的四格计数，以及FP32和FP64读出。FP64只重算同一批FP32特征的几何，不代表重新用FP64编码。

作者阈值和原始锥分别报告；UNCHA的alpha角度项不用于入锥布尔判定。错配以“下一张不同图像”构造，避免caption轮转仍对应同图；错配不是人工语义负标签。

## 推理与核验

- 两份权重均核对Hugging Face固定revision、文件大小和LFS SHA256；原始模型和特征保存在数据盘专用目录。见权重来源（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/remote_weights.json`）、作者源码版本及哈希（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/sources.json`）。
- 使用作者模型类、tokenizer、原始checkpoint归一化buffer；RGB图像以bicubic缩放为224×224。FP32推理，禁用AMP/TF32，math attention；无模型参数修改。
- checkpoint中的OmegaConf训练配置仅通过显式类型白名单加载，保持weights_only=True。
- UNCHA源码存在权重中没有的textual.min_radius_head；该模块只由未被推理调用的get_min_radius引用。移除模型实例中这一闲置模块后严格加载全部其余参数，未改作者源码或checkpoint；独立检查（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/uncha_compatibility_test.json`）确认把该头置NaN或移除均不改变文本编码器forward输出。
- 批量/单条实际推理对齐检查通过；四项几何与数据索引检查通过。保存特征由独立NumPy FP64公式复算，逐项核对正配对及错配的全部阈值计数；verification.json（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/verification.json`）。
- 原始结果：HyCoCLIP（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/hycoclip_results.json`）、UNCHA（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/uncha_results.json`）。COCO检索仅作为推理合理性检查，不与使用不同划分的论文表格强行排名。

| 模型 | COCO I→T R@1 / R@10 % | COCO T→I R@1 / R@10 % |
|---|---:|---:|
| hycoclip | 45.500 / 82.040 | 32.434 / 69.341 |
| uncha | 45.300 / 82.560 | 33.825 / 70.996 |

仅新增本次审计目录和数据目录；已有自训实验和作者源码快照保留。项目环境补充绘图依赖，NumPy保留1.26.4，pip check通过。运行命令与退出码见launches_attempt2.json和uncha_launch_attempt3.json；首次加载失败过程保留在attempt1/和attempt2_uncha/。

## 精度与自配对补充

FP32/FP64间，所有主表的合法配对数和合法满足计数保持一致；部分域外表观判定会变动。COCO跨模态的作者阈值表观成功计数，HyCoCLIP为2515/2511、UNCHA为2418/2410（FP32/FP64）。不能把FP32的90°截断视为精确几何。

GRIT短语→全文中有969条在作者77-token限制下具有相同token序列，属于自配对，零长度测地线的外角不宜解释成严格局部→整体关系。它们解释了大部分文本关系的精度敏感性。去掉这些样本的10,719对中，HyCoCLIP仍没有合法配对；UNCHA有28个合法配对，原始锥满足0个，eta=1.2满足19个（全样本0.177%）。完整统计保留，不静默替换主表；见text_selfpair_check.json（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/text_selfpair_check.json`）。

详细精度差异：HyCoCLIP（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/hycoclip_precision_comparison.json`） · UNCHA（本地 `workspace/meru-width-coco/output/official_cone_audit_20261029/uncha_precision_comparison.json`）。
