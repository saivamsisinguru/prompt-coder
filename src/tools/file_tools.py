"""File tools for Prompt Coder - reading and (later) writing files."""

from pathlib import Path


def read_file(path: str) -> str:
    """Read a file and return its contents as a string.

    Raises a helpful error if the file doesn't exist or can't be read.
    """
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not file_path.is_file():
        raise ValueError(f"Not a file: {path}")

    try:
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raise ValueError(f"Cannot read (not a text file): {path}")