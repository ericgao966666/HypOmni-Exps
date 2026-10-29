"""Redraw the existing R0/R3 figure with an independently scaled R0 radius axis."""
from pathlib import Path
import importlib.util
import hashlib
import json
import os
os.environ.update(PYTHONDONTWRITEBYTECODE='1', CUDA_VISIBLE_DEVICES='', PYTHONNOUSERSITE='1')
OUT = Path(__file__).resolve().parent
WORKSPACE = OUT.parents[3]
SOURCE = WORKSPACE / 'Hyperbolic-Omnimodal/code/outputs/lowdim_retrieval_20261021/analysis/geometry_validation_20261023'
assert SOURCE.resolve().is_relative_to(WORKSPACE)
spec = importlib.util.spec_from_file_location('original_geometry_plot', SOURCE / 'analyze_recipes.py')
original = importlib.util.module_from_spec(spec)
spec.loader.exec_module(original)
summary = json.loads((SOURCE / 'analysis_summary.json').read_text())
inputs = {}
def record(path):
    path = Path(path)
    inputs[str(path)] = original.sha(path)
    return path
record(SOURCE / 'analysis_summary.json')
record(SOURCE / 'analyze_recipes.py')
items = {}
for recipe in ('R0', 'R3'):
    feature = (original.SUITE / 'analysis/geometry_validation_20261023/R0_validation_features.pt' if recipe == 'R0'
               else original.SUITE / 'runs/hyp_cone_d64_s50_R3/joint/validation_features.pt')
    assert original.sha(feature) == summary['input_hashes'][str(feature)]
    pack = original.torch.load(record(feature), map_location='cpu', weights_only=True)
    radii = {s: original.torch.asinh(pack['features'][s].double().norm(dim=-1)).numpy() for s in original.SUBSETS}
    native = next(row for row in summary['native_metrics'] if row['recipe'] == recipe)
    for s in original.SUBSETS:
        assert abs(float(radii[s].mean()) - native[f'radius_{s}']) < 1e-10
    items[recipe] = dict(radii=radii, geometry={'strict_pct': native['strict_pct']}, selected_epoch=summary['selected_checkpoints'][recipe]['epoch'],
        projections={m: {'embedding': original.np.load(record(SOURCE / f'{m}_{recipe}.npy')), 'quality': summary['projection_details'][recipe][m]['quality']} for m in ('horo', 'cosne')})
old_row_plot = original.row_plot
limits = {}
def row_plot(axes, recipe, item):
    old_row_plot(axes, recipe, item)
    if recipe == 'R0':
        values = original.np.concatenate(list(item['radii'].values()))
        low, high = min(float(values.min()), 1.0), max(float(values.max()), 1.0)
        pad = max((high-low)*.12, .002)
        axes[2].set_ylim(low-pad, high+pad)
        from matplotlib.ticker import FormatStrFormatter, MaxNLocator
        axes[2].yaxis.set_major_locator(MaxNLocator(nbins=6))
        axes[2].yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
        axes[2].set_ylabel('Native hyperbolic radius (independent zoom)')
        axes[2].text(.98,.98,'Independent y-scale near r = 1',ha='right',va='top',transform=axes[2].transAxes,fontsize=9,color='#555555')
    limits[recipe] = list(axes[2].get_ylim())
original.row_plot = row_plot
original.ROOT = OUT
fig = original.paired_figure(items, ('R0','R3'), 'geometry_R0_vs_R3')
original.a.plt.close(fig)
assert limits['R3'] == [.8, 3.6]
assert all(original.sha(path) == digest for path,digest in inputs.items())
provenance = {'change':'Only the R0 radius panel uses an independent y-axis; existing projections and all numerical results reused unchanged.', 'axis_limits':limits, 'input_sha256':inputs, 'script_sha256':original.sha(Path(__file__)), 'outputs':{name:original.sha(OUT/name) for name in ('geometry_R0_vs_R3.png','geometry_R0_vs_R3.pdf')}}
(OUT/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps({'axis_limits':limits,'verified':'Feature hashes, native means and unchanged inputs'},indent=2))
