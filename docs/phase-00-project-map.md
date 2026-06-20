# Phase 00 - Project Map

## What I Built

I created the initial Python project shell for TinyLLM Anatomy Workbench:

- a package folder at `tinyllm/`
- data folders for raw text, processed data, and tokenizer artifacts
- output folders for checkpoints and exported model files
- a pytest setup
- a Phase 00 smoke test
- a README mission statement
- this documentation page

No model code exists yet. No tokenizer exists yet. This phase is only the map and foundation.

## Why This Matters

An LLM project can become confusing quickly because many different objects get called "the model" in casual conversation. This project keeps the pieces separate from the beginning:

- Architecture is the recipe for the neural network: layers, tensor shapes, attention heads, feed-forward blocks, embeddings, and normalization.
- Weights are the learned numbers inside that architecture.
- A tokenizer turns text into token IDs and token IDs back into text.
- A checkpoint is a saved training state. It usually contains model weights and may also contain optimizer state, step counts, and training metadata.
- A binary model file is an exported inference artifact. It is shaped for loading and running, not for resuming training.
- A runtime is the program that loads model files, prepares inputs, manages memory, and executes inference.
- Inference is the act of using a trained model to predict the next token and generate text.
- A KV cache stores previous attention keys and values so generation does not recompute the entire prompt every step.
- Experts are separate feed-forward networks used in mixture-of-experts models. A router chooses which experts handle each token.

Keeping these names precise makes each later phase easier to understand.

## Architecture Before

Before Phase 00, the workspace had no project structure.

There was no package, no tests, no data layout, no documentation map, and no committed baseline.

## Architecture After

After Phase 00, the repository has a simple educational layout:

```text
.
|-- README.md
|-- pyproject.toml
|-- requirements.txt
|-- data/
|   |-- raw/
|   |-- processed/
|   `-- tokenizers/
|-- tinyllm/
|   `-- __init__.py
|-- tests/
|   `-- test_phase00_project_structure.py
|-- checkpoints/
|-- exports/
`-- docs/
    `-- phase-00-project-map.md
```

## Key Files Changed

- `README.md` explains the project mission.
- `pyproject.toml` defines Python 3.11+ and pytest settings.
- `requirements.txt` lists the starter dependencies.
- `tinyllm/__init__.py` marks the Python package.
- `tests/test_phase00_project_structure.py` verifies the Phase 00 structure.
- `docs/phase-00-project-map.md` records the mental model.
- `.gitignore` keeps generated caches and large output artifacts out of git while preserving empty folders.

## Commands Run

```powershell
python --version
pip freeze
pytest
python -m pytest
```

## Test Results

- `python --version` reported Python 3.12.10.
- `pip freeze` completed and showed pytest 9.1.0 installed.
- `pytest` did not run because the executable is not on this shell's PATH.
- `python -m pytest` collected 2 tests and passed 2 tests.

## What Confused Me

The main source of confusion is that words like model, checkpoint, and runtime often blur together. Phase 00 separates the vocabulary before any code is written.

## What I Understand Now

I understand that the architecture is the shape of the network, the weights are learned values inside that shape, the tokenizer is the text-to-token boundary, and the runtime is the system that executes inference from saved artifacts.

## Next Phase Gate

The next phase may begin only after:

- the project structure exists
- pytest discovers and passes the Phase 00 smoke test
- the Phase 00 documentation is complete
- the baseline is committed

Do not implement the tokenizer until the next phase explicitly requests it.
