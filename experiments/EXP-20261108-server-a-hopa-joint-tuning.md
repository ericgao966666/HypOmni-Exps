# HoPA Table 9：MSR-VTT N=500 联合3-pair调参

[返回实验总览](../README.md) · EXP-20261108-server-a-hopa-joint-tuning · 完成记录：2026-11-09 13:29:34 +0800；本地结果核对与文档更新：2026-11-12（Asia/Shanghai）

**7/7组单seed搜索已完成，但没有一组在R@1上超过各自配对Random。** 按预定R@1+R@5选中的`conservative`为20.2489% R@1，比原配置17.6471%提高2.6018pp，仍比配对Random20.7014%低0.4525pp。该候选在outer300/学生epoch5选中；固定outer3000/epoch20降至16.3462%。因此本轮支持“调参可改善联合3-pair原配置”，不支持“已优于真实随机子集”。测试集参与参数、外层checkpoint及学生epoch选择，只有一个蒸馏seed。

## 研究问题与关键设置

问题是：保持联合3-pair目标不变时，调整优化参数能否改善MSR-VTT N500表现？仍先探索3-pair，不加L_M，不扩展T-bind/V-bind。

| 影响结果解读的设置 | 当前v2口径 |
|---|---|
| 数据 | 完整7927训练/884测试，不另划验证集；专家和合成初始化只用训练数据，test参与选参 |
| 模型与目标 | 冻结ImageBind backbone、训练投影头；专家三项InfoNCE求和，蒸馏/学生三项wBCE求和，无L_M |
| 专家 | 20独立seed、各10实际epoch；必须对应3-pair联合目标 |
| 合成预算 | N500、蒸馏seed1、3000实际更新，每300步检查候选；内层16步、mini-batch25、专家跨度2、max_start_epoch5 |
| 学生 | 每候选1次训练，seed1000，20实际epoch；每5epoch评估 |
| 选择规则 | 先按测试六方向Avg.R@1+Avg.R@5选epoch5/10/15/20，再按同分数选outer300/600/.../3000；排除epoch0/outer0，平分取较早状态 |
| Random | 同一500真实初始化与单位相似度；同样20轮、同种子及对应初始LR，按同规则选epoch |
| 保存 | 各外层合成集、逐epoch指标、实际选中epoch的head；另保留outer3000/epoch20末态指标 |
| 搜索范围 | 原配置、内层LR降/升、特征LR降/升、相似度LR降低，以及组合降低，共7组；第一轮单seed |

基准特征LR100、内层初始LR0.01、相似度LR100；候选分别为特征LR30/300、内层0.01/3与0.03、相似度LR10，以及30/0.01/3/10组合。固定温度0.07、rank20、alpha0.01、lr_lr=1e-4。选模规则核对自theory_selected与low_budget的当前协议，N500检查间隔与q5_native一致。

## 主要结果

884条test、六方向平均Recall，单位%；同一候选各指标取同一个R@1+R@5最优节点。所有配置实际完成3000更新；最优/次优按列标记，不表示显著性。

| 配置 | R@1 ↑ | R@5 ↑ | R@10 ↑ | R@1+R@5 ↑ | 外层步 | 学生epoch |
|---|---:|---:|---:|---:|---:|---:|
| reference | 17.6471 | 40.3658 | 51.6591 | 58.0128 | 2700 | 20 |
| inner_div3 | 17.9110 | 40.3846 | 51.5083 | 58.2956 | 3000 | 20 |
| inner_x3 | 17.7225 | <ins>40.5354</ins> | 51.4894 | 58.2579 | 2400 | 20 |
| data_30 | 17.0060 | 39.1780 | 50.1508 | 56.1840 | 1800 | 5 |
| data_300 | <ins>18.4012</ins> | **40.9879** | **51.9985** | <ins>59.3891</ins> | 2700 | 20 |
| sim_10 | 17.8356 | 40.5166 | <ins>51.6780</ins> | 58.3522 | 2700 | 20 |
| conservative | **20.2489** | 39.6305 | 50.0377 | **59.8793** | 300 | 5 |

配对Random使用同500条初始化tuple及该候选初始LR，按相同学生选择规则读取。下表仅在每行两方法之间排名，不混排不同LR的Random。

| 配置 | 配对Random R@1 ↑ | 所选合成集 R@1 ↑ | 合成−Random（pp） |
|---|---:|---:|---:|
| reference | **20.2677** | <ins>17.6471</ins> | -2.6207 |
| inner_div3 | **20.7014** | <ins>17.9110</ins> | -2.7903 |
| inner_x3 | **18.8160** | <ins>17.7225</ins> | -1.0935 |
| data_30 | **20.2677** | <ins>17.0060</ins> | -3.2617 |
| data_300 | **20.2677** | <ins>18.4012</ins> | -1.8665 |
| sim_10 | **20.2677** | <ins>17.8356</ins> | -2.4321 |
| conservative | **20.7014** | <ins>20.2489</ins> | -0.4525 |

固定outer3000/学生epoch20的R@1：reference 17.7036%、inner_div3 17.9110%、inner_x3 17.8922%、data_30 16.5158%、data_300 18.2692%、sim_10 17.7602%、conservative 16.3462%。其中`results.json`的`final`仍可能选学生epoch，固定末态必须读取`fixed_final`，不能混用。

终态以`finished.json`的complete及7个完整候选为准；`latest_run.json`和最后一份`progress.json`仍保留完成前的running快照。本次没有重训或重评。

## 解释与历史

- 本实验主读数标为test-selected；R@10仍记录但不参与选模。
- 原生3-pair函数的附属best_results.jsonl采用含R@10的旧综合分数，本轮权威选择来自外围逐epoch记录的R@1+R@5，避免混用。
- 旧v1的7134训练/793验证、固定学生50轮方案已被用户修订，旧源码、配置、划分和记录保存在本地revision及旧run目录，未覆盖历史。
- 原始Table9运行配置与数值的绑定仍未恢复；本轮是现存实现的新调参实验，不能预先称为原论文结果的严格复现。

## 下一步

保留这轮未超过Random的负结果，不自动扩展参数或seed。如果后续继续，需先明确独立验证选模与是否继续联合3-pair方向；当前单seed、test-selected搜索不作为稳定收益证据。

## 本地来源

项目`HoPA-Rebuttal/q4_tuning/`：protocol.json、split_manifest.json、source.patch、source_manifest.json、implementation_manifest.json和PAUSED.json。旧协议归档`revisions/20261108T221402-before-test-selected/`。

最后停止的控制目录`HoPA-Rebuttal/q4_tuning/runs/20261108T215130-server-a-msrvtt-n500-pilot/`；user_stop_request.json、stop_verification.json、finished.json保存停止证据。重型旧预检产物位于`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/q4_tuning/20261108T215130-server-a-msrvtt-n500-pilot/`，保持原样。运行记录存本地`runs/EXP-20261108-server-a-hopa-joint-tuning/`。

本轮未提交或上传；fetch失败，远端状态尚未核实。已有其他实验改动全部保留。

已完成运行：`HoPA-Rebuttal/q4_tuning/runs/20261109T000033-server-a-n500-test-selected/`；重型输出：`/data-nfs/xiaoboxia/YuxuanGao/HoPA/runs/q4_tuning/20261109T000033-server-a-n500-test-selected`。历史GPU调度基于可用显存，最多7个worker、每卡1个，预留4GiB；共用卡耗时不作效率对比。暂停前源码已归档`revisions/20261108T235850-before-capacity-resume/`，原生训练代码字节未变。

本次回填依据：上述控制目录`results.json`（SHA-256：`9d47056f50728e5a6176cb44d462d34cfc42081cf5cceae39df52e79e63031ed`）与`finished.json`。原先“尚无结果”的卡片完整保存在本地`runs/rebuttal-record-audit-20261112T1705/before/`；原始报告及JSON未改写。
