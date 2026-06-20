from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_phase00_key_files_exist() -> None:
    expected_files = [
        "README.md",
        "pyproject.toml",
        "requirements.txt",
        ".gitignore",
        "tinyllm/__init__.py",
        "docs/phase-00-project-map.md",
    ]

    for relative_path in expected_files:
        path = PROJECT_ROOT / relative_path
        assert path.is_file(), f"Missing file: {relative_path}"


def test_phase00_key_directories_exist() -> None:
    expected_directories = [
        "data/raw",
        "data/processed",
        "data/tokenizers",
        "tests",
        "checkpoints",
        "exports",
        "docs",
    ]

    for relative_path in expected_directories:
        path = PROJECT_ROOT / relative_path
        assert path.is_dir(), f"Missing directory: {relative_path}"

