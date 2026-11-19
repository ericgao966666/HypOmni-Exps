# 预设正余弦能否让PMRL从随机head学好

[返回实验总览](../README.md) · EXP-20261111-server-a-pmrl-positive-init · 完成核对：2026-11-11 12:08:32 +0800；文档更新：2026-11-11

**8/8条件已完成、无失败。单seed小试支持正向几何能改善PMRL的冷启动：无pairwise warm-up，Full验证R@1从普通随机的2.208%提高到仅正初始化的20.292%，持续正约束为20.229%。** 两种正向处理分别达到普通InfoNCE Full参照21.458%的约94.6%与94.3%。持续约束条件每个训练batch和全部验证节点均满足正余弦，后者负余弦率为0；仅正初始化条件后续允许少量负值，Full末态负余弦率1.71%。

所有条件初始R@1均0.1875%，初始增广前后R@1/5/10及score差为0；同一base参数哈希与batch序列一致。因而提高不是公共分量直接给初始检索带来的收益。当前结果只针对指定正锥构造、单seed和固定配方，不能证明非负性是唯一原因或足以保证任意PMRL模型成功；没有重做蒸馏或读取test。

## 研究问题与关键设置

| 设置 | 固定口径 |
|---|---|
| 数据 | 已有MSRVTT训练划分，Full7127/Random100、验证800；不读取test特征 |
| 模型 | 同一随机原生head产生单位1024D残差r；统一增广为z=normalize([r,b_m])、输出1025D，全部3151876参数 |
| 条件 | neutral:b=0；positive_free:b=1.05后自由学习；positive_projected:b=1.05并在每次SGD后约束b_m≥1.05 |
| 保证 | 正约束时任意模态/实例点积≥0.0487514863；比仅同实例Gram非负更强，也影响负例 |
| 主目标 | 谱CE＋raw-SVD proxy实例CE，权重1/1，tau=.1；无pairwise warm-up，无ITM/WBCE/S学习 |
| 对照 | 三条件×Full/Random共6项PMRL；另加neutral/positive_projected两个Full纯InfoNCE能力参照 |
| 训练 | 单head/subset/batch seed0；各3000更新、batch100、SGD .03/momentum .9/wd .0005 |
| 选择 | 验证Avg R@1+R@5选同一正更新节点，并列最早；固定末态一并报告 |
| 诊断 | 初始检索是否保留随机水平、训练/验证检索、负余弦率/最小值及下界、正负例相似度差、两项loss、谱间隙/残差、proxy符号/聚集程度、b变化、梯度有限性 |

## 主要结果

800条验证、六方向平均Recall（%），按同一节点Avg R@1+R@5选优；单seed，无标准差。下面三行均为从第1步使用纯PMRL对齐目标，分别在Full和Random列内排序。负余弦比例是所选Full节点的几何诊断，不作为性能排名。

| 初始化/约束 | Full R@1 ↑ | Random100 R@1 ↑ | Full负余弦比例 | Full选优步 |
|---|---:|---:|---:|---:|
| 普通随机，b=0 | 2.208 | 0.417 | 66.50% | 3000 |
| 仅正初始化，b后续自由 | **20.292** | <ins>2.896</ins> | 1.71% | 3000 |
| 每步保持b≥1.05 | <ins>20.229</ins> | **3.687** | 0% | 2700 |

Random的选优节点依次为2400/900/100。正初始化和持续正约束的Full−Random差距分别17.396/16.542pp；持续约束下Random训练probe R@1为99.333%，验证3.687%，不能以持续为正推断泛化已充分。

**固定3000更新：** Full依次为2.208/20.292/20.125%；Random依次0.458/2.437/2.396%。两个正向Full没有明显末态退化，Random仍存在小数据过拟合。完整R@5/R@10和两个读出保存在独立报告中。

**纯InfoNCE能力参照：** 普通初始化Full验证选优为**21.458%**（900步），持续正约束为<ins>17.750%</ins>（2400步）；固定3000步分别18.812/16.854%。二者同样没有warm-up、都是从第一步训练自己的目标。持续正锥改变余弦的平移/缩放，因而同一名义温度不代表相同有效温度；没有另行调温度，不能仅用20.229对17.750宣称PMRL普遍优于InfoNCE。

### 前提是否确实成立

- 初值b=1.05对应对任何单位残差都成立的下界0.0487514863；实测初始配对余弦严格为正。
- positive_projected每次SGD之后投影，所有训练batch和全部验证节点均检查通过；Full选优最小配对余弦0.4031、末态0.4056，负值率始终0。该保证也覆盖负例，不仅是配对正例。
- positive_free的b在开始数步降到1以下，后来短暂为负，最终接近0（Full约1e-15量级），不再具有全局非负保证；但检索继续提高，Full末态负余弦率只有1.71%。这提示初始几何可能改变了优化路径，尚不能作唯一因果归因。
- 持续正约束的Full选优正例平均余弦0.724、错配平均0.527、差0.197；仅正初始化的差约0.270。性能改善同时伴随正负例区分，不能仅由“全部方向为正”解释。

曲线在本地`HoPA-Rebuttal/positive_init_pilot/results/20261111T115501-server-a-positive-init-v1/learning_curves.png`及PDF；展示Full/Random检索、负余弦比例和公共坐标变化。

## 解释与局限

- 三个条件采用相同增广参数化，基线也有三个b参数；native head输入/权重与batch配对。新输出1025D，不能混作旧1024D原生实验。
- positive_projected属于持续约束，不仅是初始化；它同时把不同实例的负例点积限制为正，强于PMRL的同实例假设。
- 原PMRL这里指HoPA采用的两个对齐项，不是包含ITM的完整PMRL模型。raw-SVD符号约定保持一致，记录其行为但不额外修正。
- 单seed、单学习率和b值、固定预算；失败不证明全部正向参数化不可行，完成不证明收敛。

## 下一步判断

这个单seed结果支持继续正向初始化路线，也说明“PMRL本身不能从随机head学习”的说法过强。仅正初始化与持续正约束的Full结果相近，尚无证据证明必须全程强制；可优先复核自由初值的多seed稳定性，再检查真实CE与合成WBCE的差异。WBCE、learned S/LR和正式蒸馏尚未在这套新初始化下验证，当前不自动追加运行。

## 完整结果与来源

本地代码与协议：`HoPA-Rebuttal/positive_init_pilot/`。读取已有`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/random_head_pilot/20261110-v1-prepared/`，源缓存不改。新产物在`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_pilot/`，日志和源码快照在项目`runs/`；准确PID/命令/GPU/来源哈希记入运行清单。

权威运行：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/positive_init_pilot/20261111T115501-server-a-positive-init-v1/`。工作区阅读副本及图：`HoPA-Rebuttal/positive_init_pilot/results/20261111T115501-server-a-positive-init-v1/`。`archive_manifest.json`核对原报告/JSON和副本SHA256、同初始base、同batch、完整3000更新、test未读及持续正约束检查。
