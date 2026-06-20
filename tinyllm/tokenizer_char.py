"""A tiny character tokenizer for Phase 01.

This tokenizer is intentionally simple: each unique character gets one integer
ID. It is useful for seeing the text-to-token boundary before introducing BPE.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DEFAULT_VOCAB_PATH = Path("data/tokenizers/char_vocab.json")


class CharTokenizer:
    """Map characters to token IDs and token IDs back to characters."""

    def __init__(self, vocab: list[str] | None = None) -> None:
        self._itos: list[str] = []
        self._stoi: dict[str, int] = {}
        self._fitted = False

        if vocab is not None:
            self._set_vocab(vocab)

    @property
    def vocab_size(self) -> int:
        return len(self._itos)

    @property
    def stoi(self) -> dict[str, int]:
        return dict(self._stoi)

    @property
    def itos(self) -> list[str]:
        return list(self._itos)

    def fit(self, text: str) -> None:
        """Build a deterministic sorted vocabulary from raw text."""

        vocab = sorted(set(text))
        self._set_vocab(vocab)

    def encode(self, text: str) -> list[int]:
        """Turn text into integer token IDs.

        Shape note: a Python string of length T becomes a list with T integers.
        """

        self._require_vocab()

        ids: list[int] = []
        for char in text:
            if char not in self._stoi:
                raise ValueError(
                    f"Unknown character {char!r}. Fit or load a vocabulary that contains it."
                )
            ids.append(self._stoi[char])
        return ids

    def decode(self, ids: list[int]) -> str:
        """Turn integer token IDs back into text."""

        self._require_vocab()

        chars: list[str] = []
        for token_id in ids:
            if token_id < 0 or token_id >= len(self._itos):
                raise ValueError(
                    f"Unknown token ID {token_id}. Valid IDs are 0 to {len(self._itos) - 1}."
                )
            chars.append(self._itos[token_id])
        return "".join(chars)

    def save(self, path: str | Path) -> None:
        """Save the vocabulary as JSON."""

        self._require_vocab()

        save_path = Path(path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {"vocab": self._itos}
        save_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: str | Path) -> "CharTokenizer":
        """Load a tokenizer from a JSON vocabulary file."""

        load_path = Path(path)
        payload = json.loads(load_path.read_text(encoding="utf-8"))

        if "vocab" not in payload or not isinstance(payload["vocab"], list):
            raise ValueError("Tokenizer JSON must contain a 'vocab' list.")

        return cls(vocab=payload["vocab"])

    def _set_vocab(self, vocab: list[str]) -> None:
        if len(vocab) != len(set(vocab)):
            raise ValueError("Vocabulary contains duplicate characters.")

        for char in vocab:
            if not isinstance(char, str) or len(char) != 1:
                raise ValueError("Character vocabulary entries must be one-character strings.")

        self._itos = list(vocab)
        self._stoi = {char: token_id for token_id, char in enumerate(self._itos)}
        self._fitted = True

    def _require_vocab(self) -> None:
        if not self._fitted:
            raise ValueError("Tokenizer has no vocabulary. Call fit() or load() first.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fit and inspect a tiny character tokenizer.")
    parser.add_argument("--text", required=True, help="Text to fit, encode, and decode.")
    parser.add_argument(
        "--save-path",
        default=str(DEFAULT_VOCAB_PATH),
        help="Where to save the character vocabulary JSON.",
    )
    args = parser.parse_args()

    tokenizer = CharTokenizer()
    tokenizer.fit(args.text)
    ids = tokenizer.encode(args.text)
    decoded = tokenizer.decode(ids)
    tokenizer.save(args.save_path)

    print("Text")
    print(args.text)
    print()
    print("IDs")
    print(ids)
    print()
    print("Decoded")
    print(decoded)
    print()
    print("Vocab size")
    print(tokenizer.vocab_size)


if __name__ == "__main__":
    main()

