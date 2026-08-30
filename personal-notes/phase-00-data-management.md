# Phase 00 — Data Management

## Environment

- Python 3.12.14
- `datasets` 5.0.1
- `huggingface_hub` 1.29.0
- `pyarrow` 25.0.1
- Repository virtual environment: `.venv`

## Supplied data utility

Ran the lesson's `data_utils.py` successfully.

It verified:

- Dataset downloading and local caching
- Dataset inspection
- Streaming
- CSV, JSON and Parquet conversion
- Train/validation/test splitting
- Parquet reloading
- Model-file caching
- Dataset fingerprinting

The Rotten Tomatoes training split contained 8,530 rows.

For a 500-row sample:

- CSV: 59,539 bytes
- JSON: 68,473 bytes
- Parquet: 41,350 bytes
- Parquet was 1.4 times smaller than CSV

The sample produced reproducible 80/10/10 splits using seed 42.

## Exercise 1 — GLUE/MRPC

Loaded `nyu-mll/glue` with the `mrpc` configuration.

- Training rows: 3,668
- Columns: `sentence1`, `sentence2`, `label`, and `idx`
- Inspected the first five examples
- Labels identify equivalent and non-equivalent sentence pairs

## Exercise 2 — C4 streaming

Streamed `allenai/c4` with the English configuration without downloading the complete dataset.

During one ten-second measurement:

- Examples processed: 32,053
- Characters processed: 68,729,319
- Rate: approximately 3,126.8 examples per second

The exact rate depends on network and cache conditions.

## Exercise 3 — CSV and Parquet

Converted the 3,668-row MRPC training split.

- CSV: 915,219 bytes
- Parquet: 623,315 bytes
- Parquet used 31.9% less space
- All 3,668 Parquet rows reloaded successfully

Temporary conversion files were automatically removed.

## Exercise 4 — Reproducible splits

Created 70/15/15 splits using seed 42:

- Train: 2,567 rows
- Validation: 550 rows
- Test: 551 rows

Verified:

- All rows were preserved
- No examples overlapped between splits
- Repeating the operation with seed 42 produced identical splits

## Hugging Face cache

Downloaded a selected SafeTensors snapshot of
`sentence-transformers/all-MiniLM-L6-v2`.

- Cached files: 10
- Snapshot size: 87.3 MB
- Alternative framework copies were not downloaded
- Offline cache lookup completed in 0.0007 seconds
- `model.safetensors` was present

The cache is stored outside the repository under
`~/.cache/huggingface/`.

The unauthenticated-request warning is acceptable for these small public
downloads. No Hugging Face token was stored in the project.

## Large-file management

The repository already ignores:

- `data/`
- `models/`
- PyTorch model files
- ONNX files
- SafeTensors files
- Binary model files

Git LFS and DVC are not currently installed because this course can re-fetch
its public datasets and models. They should be introduced only when large
artifacts must be shared or exact datasets must be versioned across machines.

Local Hugging Face caching and `.gitignore` are sufficient for the current
course work.

## Result

The data workflow can now load, stream, cache, convert, split and verify
datasets reproducibly without committing downloaded data or model weights to
Git.
