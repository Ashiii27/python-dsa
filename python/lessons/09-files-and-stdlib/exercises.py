"""Lesson 09 exercises — files, json, stdlib."""
from __future__ import annotations

from pathlib import Path


def write_lines(path: str | Path, lines: list[str]) -> int:
    """Write each line followed by '\\n' (utf-8). Create parent dirs.
    Return the number of lines written."""
    raise NotImplementedError


def read_nonempty_lines(path: str | Path) -> list[str]:
    """Return stripped lines, skipping blank/whitespace-only ones."""
    raise NotImplementedError


def count_words_in_file(path: str | Path) -> dict[str, int]:
    """Case-insensitive count of word characters runs (use re), streaming line by line."""
    raise NotImplementedError


def save_json(path: str | Path, data: object) -> None:
    """Write pretty JSON (indent=2, sorted keys, utf-8, no ASCII escaping)."""
    raise NotImplementedError


def load_json(path: str | Path, default=None):
    """Load JSON; return default if the file is missing or invalid."""
    raise NotImplementedError


def largest_files(directory: str | Path, n: int) -> list[str]:
    """Names of the n largest regular files directly inside directory,
    biggest first, ties broken by name ascending."""
    raise NotImplementedError


def csv_column_sum(path: str | Path, column: str) -> float:
    """Sum a numeric column of a headed CSV file. Missing/blank cells count as 0."""
    raise NotImplementedError
