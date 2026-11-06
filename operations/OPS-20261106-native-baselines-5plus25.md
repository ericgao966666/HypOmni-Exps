# 新服务器操作：VAST / GRAM / PMRL 共同初始化的 5+25 实验

[返回实验总览](../README.md) · [实验卡](../experiments/EXP-20261106-server-b-vast-init-baselines.md)

文档更新：2026-11-06 UTC。已核对下列代码发布版本；本文是可复用操作指南，不是目标服务器的实际运行记录。目标服务器尚无本轮正式结果，不能把源服务器的功能检查视为已完成目标端训练。

## 1. 本次要运行的版本和范围

| 项目 | 固定内容 |
| --- | --- |
| 实验记录仓库 | `ericgao966666/HypOmni-Exps`，`main`；保存说明与研究总结 |
| 实验代码仓库 | `ericgao966666/Hyperbolic-Omnimodal` |
| 代码分支 | `native-baselines-vast-init-5plus25-20261106` |
| 固定代码提交 | `ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2` |
| 本次运行目录 | **`portable_baselines/`**；不运行代码仓库其他历史入口 |
| 方法与起点 | VAST、GRAM、PMRL全部加载同一份VAST `model_step_204994.pt` |
| 阶段与预算 | 前5轮仅有效对齐head，后25轮联合训练；seed50、512D、global batch256、322步/轮、共9660步 |

[固定版本运行说明](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2/portable_baselines/README.md)、[机器协议](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2/portable_baselines/protocol.json)、[实际检查范围](https://github.com/ericgao966666/Hyperbolic-Omnimodal/blob/ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2/portable_baselines/TESTING.md)。若以后采用新代码提交，需要更新本指南与实验记录，并使用明确的新实验版本；不能在运行中静默换源码。

GitHub传输代码、固定manifest和轻量配置。媒体、模型、特征缓存、检查点与实际运行日志使用目标服务器本地存储。

## 2. 先更新实验记录仓库

在目标服务器的 `HypOmni-Exps` 目录执行：

```bash
pwd
git status --short --branch
git fetch origin
git diff --name-status HEAD..origin/main
```

确认本地工作已保留、没有需要合并的改动且可快进后，再执行：

```bash
git merge --ff-only origin/main
```

若目标机器仍停留在2026-11-05文档分层之前的版本，先按 [SYNC.md](../SYNC.md) 备份和恢复将停止跟踪的本地结果，不能直接把这些文件随pull删除。已有分叉或本地改动时先合并，不使用reset/clean/强推清理。

## 3. 准备资源和独立代码目录

先确认GPU型号、单卡显存、可使用的GPU及工作区/数据盘权限：

```bash
nvidia-smi
command -v python3
python3 --version
```

源端检查使用Python3.11、PyTorch2.8.0+cu128；目标GPU/驱动需能运行所选CUDA wheel。依赖改变后必须重新执行目标端检查。建议在既有媒体之外预留约250GiB空闲供三模型里程碑、Adam恢复点、缓存和40GiB保护余量，另确认CPU内存足以容纳多组完整模型与检查点。

在目标机器自己有权操作的目录中设置以下路径；替换示例，不照抄源服务器路径。代码目录应是新的独立目录，避免切换另一个正在运行的代码工作树。 以下命令按顺序在同一个shell中执行；换终端或重新登录后，先重新设置这些变量并进入本次代码目录。

```bash
BASELINE_WORKSPACE=/填写目标服务器的个人工作区
BASELINE_DATA_ROOT=/填写目标服务器的数据根目录
BASELINE_CODE="$BASELINE_WORKSPACE/Hyperbolic-Omnimodal-native5plus25"
BASELINE_COMMIT=ca8a866c2a7d9a1f5eec43049ec1153e4a3cbdc2

df -h "$BASELINE_WORKSPACE" "$BASELINE_DATA_ROOT"
# BASELINE_CODE已存在时先检查其状态；不要覆盖已有项目。
test ! -e "$BASELINE_CODE" || { echo '代码目录已存在，请检查或选择新目录'; exit 1; }
git clone --single-branch --branch native-baselines-vast-init-5plus25-20261106 \
  https://github.com/ericgao966666/Hyperbolic-Omnimodal.git "$BASELINE_CODE"
git -C "$BASELINE_CODE" checkout --detach "$BASELINE_COMMIT"
git -C "$BASELINE_CODE" rev-parse HEAD
cd "$BASELINE_CODE/portable_baselines"
```

`rev-parse HEAD` 应输出上表完整提交号。固定提交的detached HEAD是有意设置；这份目录用于运行，不在训练过程中pull或修改代码。

## 4. 配置现有数据和模型

只需共同的VAST主checkpoint，不需要GRAM、PMRL各自发布的checkpoint：

```text
VAST主checkpoint: model_step_204994.pt
SHA256: 9005d283ea0de99549efbedeb7d21c8e25bea8fa41c0f6570296b0e7a055a6c5

<assets_root>/
  clip/EVA01_CLIP_g_14_psz14_s11B.pt
  beats/BEATs_iter3_plus_AS2M.pt
  bert/bert-base-uncased/
    config.json
    model.safetensors 或 pytorch_model.bin
    vocab.txt
    tokenizer_config.json 等原目录文件
```

构造权重及BERT配置与词表也要准备完整。入口会检查VAST SHA256、构造资源哈希和加载后公共参数指纹；文件名相同不代表版本相同。权重不在GitHub迁移包中，缺少时先从已有授权资源或作者官方来源准备到目标服务器。

创建本机配置，已有配置不覆盖：

```bash
test -e configs/paths.local.json || cp configs/paths.example.json configs/paths.local.json
```

编辑 `configs/paths.local.json`，全部填写为真实绝对路径：

| 字段 | 应填写什么 |
| --- | --- |
| `data_root` | 本实验有权访问的数据根目录，包含以下媒体、权重与输出路径 |
| `output_root` | `data_root`下新的实验专用子目录，例如`…/native_baselines_5plus25_seed50`；不能与媒体目录重叠 |
| `assets_root` | 上述包含clip/beats/bert的构造权重根目录 |
| `vast_checkpoint` | 同一份VAST `model_step_204994.pt`的完整路径 |
| `datasets.vast.video` / `.audio` | VAST视频/音频目录 |
| `datasets.msrvtt.video` / `.audio` | MSRVTT视频/音频目录 |
| `datasets.vatex.video` / `.audio` | VATEX视频/音频目录 |
| `datasets.activitynet.video` / `.audio` | ActivityNet视频/音频目录 |
| `datasets.didemo.video` / `.audio` | DiDeMo视频/音频目录 |
| `resources` | GPU显存上限/余量、磁盘余量及每rank数据worker数；先保留模板，再结合目标GPU预检判断 |

此配置只是绑定目标路径，不会迁移媒体。它被代码仓库忽略，不提交到Git。实验仓库的 `config/servers.local.json` 则只记录服务器别名与项目位置，二者作用不同；见 [本机配置说明](../config/README.md)。

固定数据范围如下；即使目标服务器有更多样本，也不重新划分或补入：

| 集合 | 视频数 | caption/query数 |
| --- | ---: | ---: |
| VAST train | 82608 | 82608 |
| VAST val | 2048 | 2048 |
| VAST test | 2051 | 2051 |
| MSRVTT test | 884 | 884 |
| VATEX test | 1224 | 12240 |
| ActivityNet test | 3987 | 3987 |
| DiDeMo test | 995 | 995 |

这些是当前固定视听交集，并非各论文完整标准测试集合。manifest在代码包的 `manifests/` 中，大文件为无损 `.json.gz`，由程序直接读取；`index.json`可查看计数和逻辑哈希。音频扩展名按manifest保留，不自动以另一格式替换。目标端重建本地size/mtime记录，不要求文件时间戳等于源服务器。

## 5. 安装项目环境

以下命令均在 `portable_baselines/` 下执行。使用该目录专用 `.venv`，不安装到系统或共享用户环境。先检查实时磁盘空间：

```bash
: "${BASELINE_DATA_ROOT:?先设置目标数据根目录BASELINE_DATA_ROOT}"
df -h . "$BASELINE_DATA_ROOT"
export PYTHONNOUSERSITE=1
export PIP_CACHE_DIR="$PWD/.cache/pip"
export HF_HOME="$BASELINE_DATA_ROOT/.cache/huggingface"
export TORCH_HOME="$BASELINE_DATA_ROOT/.cache/torch"
# 已有本项目.venv时先检查并沿用，不重新覆盖。
test -x .venv/bin/python || python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -r requirements-plot.txt
.venv/bin/python -c 'import sys, torch; print(sys.executable); print(torch.__version__, torch.version.cuda)'
```

`requirements-plot.txt`用于PNG/PDF曲线；CPU/GPU训练与CSV/Markdown汇总不依赖它。GPU运行入口默认离线，不会替用户下载缺失的大权重。

## 6. 依次通过CPU、输入和初始化检查

```bash
export PYTHONNOUSERSITE=1
.venv/bin/python -B tests.py
.venv/bin/python -B prepare.py --config configs/paths.local.json
.venv/bin/python -B audit_models.py --config configs/paths.local.json
```

检查含义：

1. `tests.py`：固定manifest及划分、global256采样、Adam交接、召回分母，以及三方法原生对齐损失/梯度的双进程Gloo对照。
2. `prepare.py`：全部媒体存在性与大小、固定样本内容哈希、token及caption映射精确校验、每套输入抽样解码，并保存目标端绑定记录。
3. `audit_models.py`：三种真实模型都加载同一VAST checkpoint，公共参数指纹一致，warmup参数名单符合协议。

有需要可在首次准备时给 `prepare.py` 加 `--full-decode`，进行七套输入的全量解码检查。默认抽样通过不代表全部媒体逐字节相同；后续训练和评估仍检查文件变化并实际解码。遇到缺媒体、格式/哈希不同、路径越界或配置变化时先解决具体问题，不重新筛选manifest或伪造READY。

## 7. 构建一次共享VAST特征缓存

确认一组GPU当前可用。下面假设物理GPU0–3可用；否则替换为目标服务器实际可用的一组：

```bash
nvidia-smi
.venv/bin/python -u -B cache.py \
  --config configs/paths.local.json --devices 0,1,2,3
```

缓存只包含共同VAST在固定train/val上的冻结特征，供三种方法前5轮共享，不包含测试集特征。缓存完成会产生目标输出目录内的 `cache/READY.json`。已有合法缓存会核验复用；源码、配置、输入或缓存发生变化会拒绝混用。

## 8. 启动后台队列

选择下列一种布局；分组不重叠，每方法默认4卡、每卡64，全局batch仍为256。

**12张可用GPU：三方法各4卡并行。**

```bash
.venv/bin/python -B launch.py --config configs/paths.local.json \
  --groups '0,1,2,3;4,5,6,7;8,9,10,11'
```

**8张可用GPU：两组并行，第三种方法自动排队。**

```bash
.venv/bin/python -B launch.py --config configs/paths.local.json \
  --groups '0,1,2,3;4,5,6,7'
```

只有一组可用4卡时，写 `--groups '0,1,2,3'` 即顺序运行三种方法。允许经预检的8卡/每卡32布局；同一run恢复必须保持原world size。不能为了通过显存检查静默缩小global batch。

启动入口返回PID和日志路径后，队列会先对每种方法执行**目标GPU、global256的真实预检**，验证head更新、阶段交接、缓存一致性、联合梯度及重启恢复；通过后才正式训练。打印PID不等于已经通过预检。源服务器只完成过CPU和小批次功能检查，不能复制其READY冒充目标服务器通过。

## 9. 评估与保存频率

轮数包含前5轮head阶段：

| 项目 | 频率 |
| --- | --- |
| 初始化诊断 | epoch0，记录ITC与ITM |
| 验证集ITC R@1/5/10及候选R@32 | 每个epoch |
| 验证集ITM重排 | epoch0、5、6、10、15、20、25、30 |
| warmup head快照 | epoch1、2、3、4、5 |
| joint模型快照 | epoch6、10、15、20、25、30 |
| 完整`last.pt`恢复点 | 每轮；包括阶段、模型、Adam、AMP和各rank RNG |
| 五数据集正式测试 | 每方法epoch30完成后，固定末轮，不按测试成绩选模 |

前5轮训练各自对齐损失实际使用的head；编码器和ITM冻结。第6轮承接head权重、Adam状态与RNG，解冻有效编码器/共享BERT/ITM等模块，再训练25轮。三方法保留各自原生目标和ITM采样；没有原生entailment cone指标。`BEST.json`仅作验证诊断，主测试仍用第30轮。

## 10. 查看结果、恢复和排障

从配置中读出本次输出目录：

```bash
BASELINE_OUTPUT=$(.venv/bin/python -c 'import json; print(json.load(open("configs/paths.local.json"))["output_root"])')
cat "$BASELINE_OUTPUT/status.json"
cat "$BASELINE_OUTPUT/launch.json"
.venv/bin/python -B report.py --config configs/paths.local.json
```

| 目标端本地路径（相对`output_root`） | 内容 |
| --- | --- |
| `status.json`、`jobs.json`、`launch.json` | 队列状态、已登记子进程、命令和日志位置 |
| `logs/` | 预检、训练、评估日志 |
| `checks/` | 目标端CPU/共同初始化/GPU预检记录 |
| `runs/<method>/training_metrics.jsonl` | loss、学习率、梯度、AMP、步数和耗时 |
| `runs/<method>/validation/epoch_*.json` | 逐轮验证 |
| `runs/<method>/snapshots/`、`last.pt`、`final.pt` | 里程碑、完整恢复点、固定末轮模型 |
| `evaluation/<method>/<dataset>/` | 正式测试分数和结果 |
| `reports/REPORT.md`、`validation.csv`、`tests.csv` | 自动汇总与表格 |
| `reports/validation.png`、`validation.pdf` | 安装绘图依赖后生成的曲线 |

`DONE.json`、模型身份和结果校验通过才表示对应阶段完成。三方法完成训练且15项正式测试齐全，整个队列才是`complete`。

- 监督器意外退出：用**相同配置、相同GPU分组**重新执行原来的 `launch.py` 命令。目录锁阻止重复监督器；已登记且仍存活的子进程会被接管，有检查点的训练自动恢复。
- 资源暂停：退出码75会按原配置重试，不减少训练预算。
- 普通失败：先看对应日志。解决资源问题、保持代码和科学配置不变后，可给原 `launch.py` 命令加 `--retry-failed`。代码或协议改变应使用新输出目录，不能冒充原run续跑。
- 监督器停止不会自动杀死训练子进程。不要按共享用户名批量结束进程，不要同时用手动训练入口与队列启动同一个方法。

## 11. 在实验仓库留下什么

在目标端按实际稳定服务器别名登记 [本机路径配置](../config/README.md)，用 [run模板](../templates/run.md) 建立唯一run记录，保存在本地 `runs/EXP-20261106-server-b-vast-init-baselines/` 下。编号中的server-b表示本次建卡/交接来源，不替代目标端实际服务器信息。

实际PID、GPU、日志、路径、失败重试及详细JSON/CSV只留在产生它们的服务器。实验完成后，把关键检索表、同协议对照、限制与结论回填到[实验卡](../experiments/EXP-20261106-server-b-vast-init-baselines.md)，再按仓库规范更新首页和同步总结。当前记录不能填入历史GRAM/PMRL作者权重的成绩作为本轮结果。
