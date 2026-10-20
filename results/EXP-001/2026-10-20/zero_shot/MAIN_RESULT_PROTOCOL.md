# Main-result execution protocol

This directory is the control layer for the paper's local main-result runs. It does not reimplement VAST, GRAM, TRIANGLE, or HyperGRAM. Each external method runs in its pinned official repository; only paths, seeds, GPU assignment, checkpoint policy, and result serialization are normalized.

## Claims and comparison roles

- **PMRL vs Ours** is the causal comparison. Both run in this minimal PMRL branch from the same VAST checkpoint, the same accepted 86,707-sample manifest, the same four GPUs, the same three seeds, and the same evaluation code. The intended differences are the hyperbolic module, spectral/entailment losses, and the learning rate of parameters introduced by that module.
- **VAST, GRAM, TRIANGLE, and HyperGRAM** are method-level performance references. They use their own official implementations and method-native paper settings. They are not presented as single-variable ablations.
- Published numbers and local VAST-86.7K reproductions must be separate rows. A dagger marks a setting that official code supports but the paper does not report, especially TRIANGLE/HyperGRAM four-dataset finetuning.

TRIANGLE belongs in the comparison because it is a directly relevant three-modality method, but it is not the primary causal baseline. PMRL is the primary causal baseline; HyperGRAM is the closest contemporary hyperbolic/Gramian performance baseline.

## Selection and reporting

- Main tables use final checkpoints, R@1, both T→V and V→T, and the mean of seeds 42/50/123.
- R@5, R@10, Ravg, per-seed values, and sample standard deviations go to the appendix.
- Author-native best-on-test results, when a repository selects on a test set, go to a separate appendix track and are never mixed with final-checkpoint main results.
- Reranking uses Top-50 for PMRL/Ours. This was fixed before the main-result run because it reflected the selected method better than Top-20.
- Ours was tuned against all four test sets. This is explicitly disclosed; these four zero-shot results are not described as untouched-test generalization.

The exact machine-readable contract, source commits, input hashes, and hyperparameters are in `protocol.json`.

## Commands

Run all commands from the minimal repository with its project environment:

```bash
PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py validate

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py paired-stage1

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py paired-zeroshot

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py collect

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py validate-finetune

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/run.py paired-finetune
```

`status` is read-only. The runner never kills a process. It launches one distributed job at a time on physical GPUs 4–7 and preserves the configured global batch size rather than silently changing it after an OOM.

## Current execution order

1. Train the missing PMRL `tau1=0.05` Stage-1 checkpoints for three seeds. Reuse Ours' already completed, exactly matching selected checkpoints after provenance validation.
2. Evaluate both paired methods on all four datasets using Top-50.
3. Prepare and smoke-test official-repository Stage-1 jobs in the order GRAM, TRIANGLE, HyperGRAM. VAST's published row uses the released VAST checkpoint; a local rerun is a separately labeled reproduction.
4. Run dataset-specific finetuning only after Stage-1 checkpoint and metric parity checks pass.

For the causal PMRL/Ours fine-tuning comparison, both methods use `ret%tv%ta` with no subtitle input. This preserves the selected method's two text-anchored modality pairs and keeps the task definition identical between the two rows. The paper's native PMRL `ret%tva`/`ret%tvas` result remains a separately labeled published/native reference rather than being mixed into the causal row.

## Official-repository baselines

The external runner operates only in the pinned checkouts documented by `../main_result_baselines/OFFICIAL_SOURCES.md`:

```bash
PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/external_runner.py validate

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/external_runner.py smoke --method gram

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/external_runner.py stage1 --method gram

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/external_runner.py zeroshot --method gram

PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/external_runner.py finetune --method gram
```

Replace `gram` with `triangle` or `hypergram`; VAST has no local Stage-1 command because its zero-shot row starts from the released VAST checkpoint. External configurations retain method-native tasks. TRIANGLE downstream runs and HyperGRAM's non-MSR-VTT downstream runs are tagged as official-code adaptations because their papers do not report that four-dataset table.

For an early single-seed zero-shot read before the full three-seed run, use `--seeds 42` on GRAM, HyperGRAM, and TRIANGLE `stage1`/`zeroshot` commands. The released VAST checkpoint keeps its protocol label `--seeds 50`. `run_external_zeroshot_seed42.sh` serializes this pilot as VAST, GRAM, HyperGRAM, then TRIANGLE. Its seed-42 checkpoints and metrics use the final main-result paths, so the later multi-seed runner reuses them and only fills seeds 50 and 123.

Official evaluation logs are parsed without changing method code. VAST-style logs use `video_recall`/`txt_recall`; GRAM and HyperGRAM use `volume_ITM_T2D`/`D2T`; TRIANGLE uses `area_ITM_T2D`/`D2T`. If an evaluation process completed successfully but serialization encountered a previously unknown log schema, the runner reparses that completed log and never repeats the expensive evaluation.

GRAM, TRIANGLE, and HyperGRAM share the small runtime-only patch in `official_runtime_gradient_accumulation.patch`. It makes the already-declared gradient accumulation effective on four GPUs and saves the actual final optimizer step. The model, loss, and scoring implementations remain pinned; the only loader edit is the explicitly recorded WAV existence-check fix below. Official and execution hashes are both recorded in `protocol.json`.

The three trainable external repositories also share the one-line compatibility patch in `official_runtime_vast_wav_loader.patch`: their `finetune_area` index checks for `<clip_id>.mp3`, although their own VAST download/preprocessing scripts and the accepted shared assets produce `<clip_id>.wav`. The patch changes that existence check to WAV. Their existing `AudioMapper` already reads WAV, so decoding, sampling, models, losses, and scores remain unchanged. VAST itself has no suffix-based annotation prefilter, while PMRL already checks WAV. The original and execution-tree hashes remain separately recorded.

HyperGRAM additionally uses `official_runtime_hypergram_py313_audio.patch`. In its isolated Python 3.13 environment, librosa 1.x rejects audio reads inherited by the repository's forked DataLoader workers; the official mapper catches that error and substitutes another training item, then raises during evaluation. The patch routes only PCM WAV reads through TorchAudio's SoundFile backend, retaining librosa for non-WAV inputs and leaving resampling, fbank construction, sampling, model, loss, and scores unchanged. A waveform equality check and an eight-worker fork smoke are recorded in the experiment handoff.

## Data preparation and queues

The public PMRL `MM_eval` archive contains 10,463 DiDeMo video files but only 1,016 test-audio files. An audit of the released videos found real audio streams for just 13 of the 9,366 IDs used by PMRL's train/test annotations; the remaining videos are low-frame-rate, video-only transcodes. Consequently, the local-video extraction below is retained only as an audit and is **not** sufficient for finetuning:

```bash
PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/extract_dataset_audio.py \
  --annotations \
    /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/annotations/didemo/descs_ret_train.json \
    /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/annotations/didemo/descs_ret_test.json \
  --videos /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/didemo/videos \
  --output /data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/didemo/audios \
  --workers 2
```

The missing train audio is therefore read from the original DiDeMo authors' official YFCC100M/Multimedia Commons source. All 1,016 official test MP3s are linked without copying, and real audio is extracted from the raw AWS video for the remaining IDs. The 13 streams recovered during the released-video audit are preserved separately under `released_video_audio_audit/`; they are not allowed to override the official test MP3s. Unavailable or audio-less items are reported and never replaced by synthetic silence:

```bash
PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/fetch_official_didemo_audio.py \
  --annotations \
    /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/annotations/didemo/descs_ret_train.json \
    /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/annotations/didemo/descs_ret_test.json \
  --hash-map /data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/didemo/official_source/yfcc100m_hash.txt \
  --released-audio /data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/didemo/test_audios \
  --output /data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/didemo/audios \
  --ffmpeg /home/xiaobo.xia/YuxuanGao/PMRL/.venv/lib/python3.9/site-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2 \
  --workers 12 --retries 2
```

`validate-finetune` requires the official-source report to be complete and checks at least 8,000 effective DiDeMo train IDs and 990 test IDs. The test threshold reflects the 995 IDs for which both a released video and released test audio are actually present, rather than pretending all 1,003 annotated IDs are usable.

The fixed PMRL environment exposes only a `sox_io` torchaudio backend, and that build cannot decode the valid MP3 files in these four datasets. A first MSR-VTT launch consequently produced no optimizer step: every worker failed at `torchaudio.load` and recursively resampled another item. This invalid attempt is not a result. To avoid method-specific loader patches, all four source directories are decoded once to lossless PCM16 WAV while preserving source sampling rates and channel counts:

```bash
PYTHONNOUSERSITE=1 /home/xiaobo.xia/YuxuanGao/PMRL/.venv/bin/python \
  main_results/transcode_audio_to_wav.py \
  --workers 12 \
  --dataset msrvtt=/data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/MSRVTT/audios=/data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/decoded_wav/msrvtt \
  --dataset didemo=/data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/didemo/audios=/data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/decoded_wav/didemo \
  --dataset activitynet=/data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/activitynet/audios=/data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/decoded_wav/activitynet \
  --dataset vatex=/data-nfs/xiaoboxia/YuxuanGao/PMRL/datasets/vatex/audios=/data-nfs/xiaoboxia/YuxuanGao/PMRL/main_result_assets_20260824/decoded_wav/vatex
```

Each decoded directory contains a same-ID MP3 symlink for the official dataset index and a WAV that the unchanged official `AudioMapper` preferentially reads. Conversion is resumable and atomically records `_conversion_report.json`; failures are never replaced with silence. PMRL, Ours, VAST, GRAM, TRIANGLE, and HyperGRAM all consume these exact same decoded directories for finetuning. `validate-finetune` requires both the MP3 index link and decoded WAV for every effective ID.

The active detached queues are deliberately ordered so only one four-GPU experiment starts at a time:

1. the current paired PMRL Stage-1 run;
2. `wait_then_paired_zeroshot.sh`;
3. `prepare_decoded_audio_and_run.sh` decodes the shared audio, smoke-tests it in the fixed PMRL environment, then runs paired finetuning;
4. `wait_then_external_baselines.sh` after the paired causal table is complete.

Within the external queue, VAST zero-shot, GRAM, and HyperGRAM are prioritized. TRIANGLE is last and uses the user-selected one-epoch Stage-1 schedule on the same accepted VAST subset. Every queue exits on a recorded upstream failure and never kills another process.
