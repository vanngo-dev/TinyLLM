# Phase 01 - Character Tokenizer

## What I Built

I built a small `CharTokenizer` that learns a vocabulary from text, converts text into token IDs, converts token IDs back into text, and saves or loads its vocabulary as JSON.

The tokenizer uses one token per unique character. Its vocabulary is sorted so the same input text always creates the same IDs.

## Why This Matters

Every language model sees numbers, not raw text. A tokenizer is the boundary between human-readable text and integer token IDs that can become tensors later.

In this phase, `hello tiny llm` becomes a list of integers. Decoding those integers returns the original text. That round trip makes the text-to-token step visible before any dataset, model, training loop, BPE tokenizer, checkpoint, runtime, or KV cache exists.

## Architecture Before

Phase 00 had only the project shell:

- package, data, test, docs, checkpoint, and export folders
- pytest configuration
- a project map
- no tokenizer implementation

## Architecture After

Phase 01 adds a simple tokenizer layer:

```text
raw text
  -> CharTokenizer.fit()
  -> sorted character vocabulary
  -> CharTokenizer.encode()
  -> token IDs
  -> CharTokenizer.decode()
  -> text again
```

The tokenizer can also save its vocabulary to `data/tokenizers/char_vocab.json` and load it later.

## Key Files Changed

- `tinyllm/tokenizer_char.py` implements `CharTokenizer` and its CLI.
- `tests/test_tokenizer_char.py` tests encode, decode, save, load, unknown-character behavior, and CLI output.
- `docs/phase-01-tokenizer.md` explains the phase.
- `README.md` includes a short command reference.
- `.gitignore` allows the Phase 01 character vocabulary artifact.
- `data/tokenizers/char_vocab.json` stores the vocabulary created by the manual command.

## Commands Run

```powershell
python -m tinyllm.tokenizer_char --text "hello tiny llm"
pytest tests/test_tokenizer_char.py
python -m pytest tests/test_tokenizer_char.py
python -m pytest
```

## Test Results

- `python -m tinyllm.tokenizer_char --text "hello tiny llm"` ran successfully and wrote `data/tokenizers/char_vocab.json`.
- `pytest tests/test_tokenizer_char.py` did not run because the `pytest` executable is not on this shell's PATH.
- `python -m pytest tests/test_tokenizer_char.py` collected 5 tests and passed 5 tests.
- `python -m pytest` collected 7 tests and passed 7 tests.

## What Confused Me

The tricky part is that a tokenizer is not the model. It does not learn language patterns. It only defines how text is represented as IDs.

Unknown characters are another important boundary. This tokenizer raises a clear error instead of silently inventing an ID.

## What I Understand Now

I understand that token IDs are just integer labels for vocabulary entries. In a character tokenizer, each vocabulary entry is a single character. Later, a model will learn weights that operate on these IDs after they are embedded into tensors.

## Next Phase Gate

The next phase may begin only after:

- the character tokenizer can encode and decode text
- the vocabulary can be saved and loaded
- unknown characters fail clearly
- the Phase 01 tests pass

Do not implement the dataset builder until the next phase explicitly requests it.
