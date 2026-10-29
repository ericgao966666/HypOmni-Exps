"""Read-only analysis of saved validation features; no training or test inference."""
from pathlib import Path
import os
OUT=Path(__file__).resolve().parent
os.environ.update(CUDA_VISIBLE_DEVICES='',PYTHONNOUSERSITE='1',OMP_NUM_THREADS='2',MPLBACKEND='Agg',MPLCONFIGDIR=str(OUT/'.mplconfig'))
import json,hashlib,csv,datetime
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
ROOT=Path('/data0/xiaobo.xia/yuxuan.gao/lowdim_retrieval_20261021')
methods=['hyp_cone','euc_none','pmrl','vast','gram']
names=dict(hyp_cone='双曲有锥',euc_none='欧氏无锥',pmrl='PMRL',vast='VAST',gram='GRAM')
subs=['t','v','a','tv','ta','va','tva'];keys=['R@1','R@5','R@10'];recipes=['R0','R1','R2','R3']
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inputs={}
def record(p):
 assert p.resolve().is_relative_to(ROOT.resolve())
 inputs[str(p.relative_to(ROOT))]=sha(p)
 return p
def read(p):return json.loads(record(p).read_text())
sel={m:read(ROOT/'selections'/f'{m}.json') for m in methods}
candidates={(m,c['recipe']):c for m in methods for c in sel[m]['candidates']}
lock=read(ROOT/'SELECTIONS_LOCKED.json')
for m in methods:assert inputs[f'selections/{m}.json']==lock['selection_sha256'][m]
def mark(v,vs):
 values=sorted(set(round(x,4) for x in vs),reverse=True);s=f'{v:.4f}'
 return '**'+s+'**' if round(v,4)==values[0] else '<ins>'+s+'</ins>' if len(values)>1 and round(v,4)==values[1] else s
radii={};stats=[];layers=[];ids=None
for m in methods[:2]:
 for r in ['R1','R3']:
  folder=ROOT/'runs'/f'{m}_d64_s50_{r}'/'joint'
  done=read(folder/'DONE.json');metrics=read(folder/'validation_metrics.json');c=candidates[m,r]
  assert done['passed'] and done['selected_epoch']==c['selected_epoch'] and done['best_sha256']==c['best_sha256']
  assert metrics==c['validation']
  pack=torch.load(record(folder/'validation_features.pt'),map_location='cpu',weights_only=True)
  assert len(pack['ids'])==500
  if ids is None:ids=pack['ids']
  assert ids==pack['ids']
  rr={}
  for s in subs:
   v=pack['features'][s].double();assert v.shape==(500,64) and torch.isfinite(v).all()
   rr[s]=(torch.asinh(v.norm(dim=-1)) if m=='hyp_cone' else v.norm(dim=-1)).numpy()
   x=rr[s];orig=metrics['geometry']['radii'][s]
   assert abs(float(x.mean())-orig['mean'])<1e-10
   for q,key in [(.05,'p05'),(.95,'p95')]:assert abs(float(np.quantile(x,q))-orig[key])<1e-10
   stats.append(dict(method=m,recipe=r,selected_epoch=c['selected_epoch'],subset=s,mean=float(x.mean()),std=float(x.std()),p05=float(np.quantile(x,.05)),p25=float(np.quantile(x,.25)),median=float(np.median(x)),p75=float(np.quantile(x,.75)),p95=float(np.quantile(x,.95))))
  radii[m,r]=rr
  layers.append(dict(method=m,recipe=r,single=float(np.mean([rr[s].mean() for s in subs[:3]])),double=float(np.mean([rr[s].mean() for s in subs[3:6]])),triple=float(rr['tva'].mean())))
colors=['#0072B2','#E69F00','#009E73','#D55E00','#CC79A7','#56B4E9','#9467BD']
fig,axes=plt.subplots(2,2,figsize=(12,8))
for i,r in enumerate(['R1','R3']):
 for j,m in enumerate(methods[:2]):
  ax=axes[i,j];rr=radii[m,r]
  b=ax.boxplot([rr[s] for s in subs],tick_labels=[s.upper() for s in subs],whis=(5,95),showfliers=False,patch_artist=True)
  for box,color in zip(b['boxes'],colors):box.set(facecolor=color,alpha=.5)
  ax.set_ylim((.955,1.115) if r=='R1' else (1.0,3.5))
  ax.axhline(1,ls='--',lw=1,color='gray');ax.grid(axis='y',alpha=.2)
  ax.set_title(f'{r}: '+('Hyperbolic + cone' if m=='hyp_cone' else 'Euclidean, no cone')+f"\nSelected epoch {candidates[m,r]['selected_epoch']}")
  ax.set_ylabel('Native radius: '+('asinh(||spatial||)' if m=='hyp_cone' else '||embedding||'))
  if r=='R1':ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
fig.suptitle('MSRVTT validation: same 500 videos, 64D, seed50',fontsize=14)
fig.text(.5,.02,'Shared y-limits within each row; R1 and R3 use different scales. Boxes: IQR; whiskers: P5–P95. Radii are not performance scores.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.05,1,.94))
for ext in ['png','pdf']:fig.savefig(OUT/f'radius_R1_R3.{ext}',dpi=180)
plt.close(fig)
tests={m:read(ROOT/'method_evaluations'/f'{m}_d64_s50_R1.json') for m in methods[:2]}
assert len({d['test_ids_sha256'] for d in tests.values()})==1
for m,d in tests.items():assert d['passed'] and d['metrics']['n_candidates']==884 and d['checkpoint_sha256']==candidates[m,'R1']['best_sha256']
missing={m:not (ROOT/'method_evaluations'/f'{m}_d64_s50_R3.json').exists() for m in methods[:2]}
assert all(missing.values())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
lines=['# 64D 同训练方案对比与 R1/R3 半径分布','',f'核对时间：{now}。仅整理已有结果并在 CPU 上读取已保存验证特征；未训练、未新增测试推理。','',
'本补充与[五方法最终测试报告](../2026-10-27-five-method-tests/README.md)配套。主报告比较各方法选中的方案；本补充在 R0/R1/R2/R3 各自内部比较方法，避免把不同训练方案混为同预算对照。','',
'## 最终选中的双曲 R1：半径仍接近 1','',
'使用与最终测试模型相同的最佳 checkpoint（微调 epoch26），下列半径来自 **500 个验证视频**，不是测试集。R1 为30轮微调，未增加VAST头部预训练。单模态/双模态/三模态平均半径约 **0.9902 / 1.0248 / 1.0699**；有轻微分层，但整体仍接近初始化 r=1。严格锥满足率为0%。','',
'| 子集 | 平均半径 | 标准差 | P5 | 中位数 | P95 |','|---|---:|---:|---:|---:|---:|']
for row in stats:
 if row['method']=='hyp_cone' and row['recipe']=='R1':lines.append('| '+row['subset'].upper()+' | '+' | '.join(f"{row[k]:.4f}" for k in ['mean','std','p05','median','p95'])+' |')
lines+=['','## R1 与 R3 的半径分布','', '![R1/R3同方案半径对照](radius_R1_R3.png)','',
'[PDF](radius_R1_R3.pdf) · [完整七头分位数 CSV](radius_statistics.csv)','',
'同一行采用相同纵轴范围；R1 行放大至0.955–1.115，R3 行为1.0–3.5，不能直接比较上下箱体视觉高度。每个头500条数据，箱体为IQR，须为P5–P95，隐藏离群点。双曲半径为 asinh(||spatial||)，欧氏半径为 ||embedding||，均由原64D特征计算，未使用二维投影。不同几何的相同数值不代表相同的距离结构。','',
'| 方法 | 方案 | 单模态平均半径 | 双模态平均半径 | TVA平均半径 |','|---|---|---:|---:|---:|']
for row in layers:lines.append(f"| {names[row['method']]} | {row['recipe']} | {row['single']:.4f} | {row['double']:.4f} | {row['triple']:.4f} |")
lines+=['','半径没有越大越好的性能方向，因此不标最优。R3双曲的径向分层明显强于R1；欧氏R3也整体向外移动，但层间分离较弱。欧氏R3的V均值约1.6465，高于TV约1.5254，说明层均值排序不能替代逐边排序。双曲R1和R3的严格锥满足率均为0%；不能把较强径向分层称为已经形成严格包含层级。','',
'## 双曲有锥与欧氏无锥：同方案验证集比较','',
'所有数值来自相同500视频验证集、64D、seed50、六方向macro，按每个方案内的两个方法分别排名。每个方法/方案仍使用各自验证最优checkpoint，因此选中epoch可不同。R0=10轮；R1=30轮；R2=10轮且提高头部学习率；R3=VAST头部预训练后10轮微调。双曲有锥与欧氏无锥同时改变几何和锥目标，不能视为纯曲率消融。','',
'| 方案 | 方法 | 最佳epoch | 验证R@1 ↑ | 验证R@5 ↑ | 验证R@10 ↑ |','|---|---|---:|---:|---:|---:|']
for r in recipes:
 for m in methods[:2]:
  c=candidates[m,r];v=c['validation']['macro']
  lines.append(f"| {r} | {names[m]} | {c['selected_epoch']} | "+' | '.join(mark(v[k],[candidates[x,r]['validation']['macro'][k] for x in methods[:2]]) for k in keys)+' |')
lines+=['','R3双曲/欧氏验证R@1为28.1000%/28.2667%，R@5为55.1000%/55.3000%，R@10为65.9333%/65.8000%。双方R3的R@1都略低于各自R1，但R@5略高；不存在所有指标一致改善的结论。单seed差异不代表稳定优势。','',
'## 同方案最终测试：目前可用的 R1 对照','',
'| 方法 | 方案 | 测试R@1 ↑ | 测试R@5 ↑ | 测试R@10 ↑ |','|---|---|---:|---:|---:|']
for m,d in tests.items():lines.append(f'| {names[m]} | R1 | '+' | '.join(mark(d['metrics']['macro'][k],[x['metrics']['macro'][k] for x in tests.values()]) for k in keys)+' |')
lines+=['','这里使用884视频测试集。现有 method_evaluations 中**没有双曲有锥R3或欧氏无锥R3的最终测试JSON**；对应joint目录只保存验证结果。上面的R3数字不可标为最终测试结果，本次没有补跑测试或更改选模规则。','', '## 五方法同方案验证表','']
for r in recipes:
 lines+=['### '+r,'','| 方法 | 最佳epoch | 验证R@1 ↑ | 验证R@5 ↑ | 验证R@10 ↑ |','|---|---:|---:|---:|---:|']
 for m in methods:
  c=candidates[m,r];lines.append(f"| {names[m]} | {c['selected_epoch']} | "+' | '.join(mark(c['validation']['macro'][k],[candidates[x,r]['validation']['macro'][k] for x in methods]) for k in keys)+' |')
 lines.append('')
lines+=['原生方法保留各自目标和前向路径；相同方案统一的是训练安排，不代表目标、模型结构或计算量完全一致。','',
'## 数据与核验','',
'[全部同方案验证指标](validation_recipes.csv) · [结构化结果](results.json) · [来源与核验](provenance.json) · [生成脚本](summarize.py)','',
'核对五方法选模文件与全体锁哈希、四个R1/R3的DONE与选模checkpoint元数据、相同500个验证ID、真实64D特征半径均值及P5/P95与原记录一致；R1测试记录核对相同884候选及checkpoint。未加载模型权重或重跑训练/推理。std为同一checkpoint跨验证视频的总体标准差，不是训练种子标准差；分位区间不是置信区间。','']
(OUT/'README.md').write_text('\n'.join(lines))
rows=[dict(method=m,recipe=r,selected_epoch=candidates[m,r]['selected_epoch'],**candidates[m,r]['validation']['macro']) for r in recipes for m in methods]
for name,rs in [('radius_statistics.csv',stats),('validation_recipes.csv',rows)]:
 with (OUT/name).open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rs[0]));w.writeheader();w.writerows(rs)
(OUT/'results.json').write_text(json.dumps(dict(validation=rows,radius_statistics=stats,layer_means=layers,r1_tests=tests,r3_test_missing=missing),indent=2,ensure_ascii=False)+'\n')
for rel,h in inputs.items():assert sha(ROOT/rel)==h
(OUT/'provenance.json').write_text(json.dumps(dict(captured_at=now,source_root='dataset_root',source_directory=ROOT.name,input_sha256=inputs,script_sha256=sha(Path(__file__)),checks=dict(selection_hashes=True,checkpoint_metadata=True,matching_validation_ids=500,recomputed_native_radius_mean_p05_p95=True,r1_test_candidates=884),no_training_or_test_inference=True),indent=2)+'\n')
print(json.dumps(layers,indent=2))
