# 外部评测输入准备完成

本次只做CPU解码、输入预处理和索引检查，没有加载模型，也没有计算MSRVTT/VATEX检索性能。测试性能仍应在Tier A选模锁定后统一查看。

| 数据集 | 已解码视频 | caption query | 新增解码失败 |
| --- | ---: | ---: | ---: |
| MSRVTT当前可用子集 | 884 | 884 | 0 |
| VATEX当前可用子集 | 1224 | 12240 | 0 |

存在性审计中已记录的缺失仍然存在：这些集合不能标作标准MSRVTT-1K/VATEX-1500全量榜单。此次没有进一步删除样本。VATEX每视频10条caption全部保留。

共享输入保存在`/data0/xiaobo.xia/yuxuan.gao/itm_hierarchy_20261026/eval_inputs_v1`，实际约2.9GiB，使用FP32像素和音频fbank。两帧取确定性位置；空间与音频处理严格复用本轮VAST流程，文本统一40token、无字幕。视频和音频字段可供所有方法共同读取，但各模型必须用自己的编码器提取特征，不能把VAST token当作PMRL token。

验证证据：

- `eval_media_input_check.json`：两条VAST样本的独立预处理与训练加载器逐元素一致；外部数据六条样本的形状和有限值检查通过。
- 数据目录`READY.json`及工作区`eval_input_cache_status.json`：完整解码成功，记录各分片、文本和索引SHA256，`cuda_initialized=false`。
- `external_input_reader_check.json`：真实数据的跨分片、文件映射释放后重读、caption/video对应关系均通过；VATEX所有视频均有10条caption。
- `test_evaluation_pools.py`：2项检查通过，覆盖非方形矩阵、反向多正例、候选漏召回仍计入分母及稳定同分排序。实现初检中的argsort参数调用错误已修正后重跑。

`external_inputs.py`严格区分文本行索引与视频行索引；`evaluation_pools.py`为后续统一测试提供T×V双向候选。预处理从未使用模型表现选择数据、caption或规则。

PMRL比较协议更新为v2，见`PMRL_COMPARISON_PROTOCOL.md`与`pmrl_protocol_audit_v2.json`；初版原文和audit保留。封存C0实验代码没有改变。
