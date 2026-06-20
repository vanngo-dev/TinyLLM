import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from uuid import uuid4

import pytest

from tinyllm.tokenizer_char import CharTokenizer


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_ROOT = PROJECT_ROOT / ".test-artifacts"


@contextmanager
def local_artifact_path(filename: str):
    ARTIFACT_ROOT.mkdir(exist_ok=True)
    path = ARTIFACT_ROOT / f"{uuid4().hex}_{filename}"
    try:
        yield path
    finally:
        if path.exists():
            path.unlink()


def test_encode_returns_integers() -> None:
    tokenizer = CharTokenizer()
    tokenizer.fit("hello tiny llm")

    ids = tokenizer.encode("hello")

    assert ids
    assert all(isinstance(token_id, int) for token_id in ids)


def test_decode_reverses_encode() -> None:
    text = "hello tiny llm"
    tokenizer = CharTokenizer()
    tokenizer.fit(text)

    ids = tokenizer.encode(text)
    decoded = tokenizer.decode(ids)

    assert decoded == text


def test_save_and_load_preserve_vocab() -> None:
    tokenizer = CharTokenizer()
    tokenizer.fit("cab")

    with local_artifact_path("char_vocab.json") as save_path:
        tokenizer.save(save_path)
        loaded = CharTokenizer.load(save_path)

    assert loaded.stoi == tokenizer.stoi
    assert loaded.itos == tokenizer.itos
    assert loaded.vocab_size == tokenizer.vocab_size
    assert loaded.decode(loaded.encode("abc")) == "abc"


def test_unknown_characters_fail_clearly() -> None:
    tokenizer = CharTokenizer()
    tokenizer.fit("abc")

    with pytest.raises(ValueError, match="Unknown character 'z'"):
        tokenizer.encode("z")


def test_cli_prints_expected_sections_and_saves_vocab() -> None:
    with local_artifact_path("char_vocab.json") as save_path:
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "tinyllm.tokenizer_char",
                "--text",
                "hello tiny llm",
                "--save-path",
                str(save_path),
            ],
            cwd=PROJECT_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )

        assert save_path.is_file()

    assert "Text" in result.stdout
    assert "IDs" in result.stdout
    assert "Decoded" in result.stdout
    assert "Vocab size" in result.stdout
    assert "hello tiny llm" in result.stdout
