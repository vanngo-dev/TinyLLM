# TinyLLM Anatomy Workbench

This project builds a small GPT-style language model from raw text to inference so I can understand tokenizer, tensors, transformer blocks, checkpoints, binary model formats, KV cache, MoE experts, and distributed inference concepts.

## Phase Map

Phase 00 creates the project shell and mental map. It does not implement a tokenizer, model, training loop, generation, checkpointing, runtime, KV cache, MoE, or distributed simulation yet.

## Current Shape

- `tinyllm/` contains the Python package.
- `tests/` contains project and phase tests.
- `data/raw/` will hold source text.
- `data/processed/` will hold prepared datasets.
- `data/tokenizers/` will hold tokenizer artifacts.
- `checkpoints/` will hold training checkpoints.
- `exports/` will hold exported binary model files.
- `docs/` records each phase in plain language.

## Getting Started

```powershell
python -m pip install -r requirements.txt
pytest
```

