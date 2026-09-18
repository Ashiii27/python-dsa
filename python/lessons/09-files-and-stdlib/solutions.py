"""Lesson 09 reference solutions."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

WORD = re.compile(r"\w+")


def write_lines(path: str | Path, lines: list[str]) -> int:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(f"{line}\n")
    return len(lines)


def read_nonempty_lines(path: str | Path) -> list[str]:
    with Path(path).open("r", encoding="utf-8") as fh:
        return [stripped for line in fh if (stripped := line.strip())]


def count_words_in_file(path: str | Path) -> dict[str, int]:
    counts: Counter[str] = Counter()
    with Path(path).open("r", encoding="utf-8") as fh:
        for line in fh:
            counts.update(WORD.findall(line.lower()))
    return dict(counts)


def save_json(path: str | Path, data: object) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )


def load_json(path: str | Path, default=None):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, IsADirectoryError):
        return default


def largest_files(directory: str | Path, n: int) -> list[str]:
    files = [p for p in Path(directory).iterdir() if p.is_file()]
    files.sort(key=lambda p: (-p.stat().st_size, p.name))
    return [p.name for p in files[:n]]


def csv_column_sum(path: str | Path, column: str) -> float:
    total = 0.0
    with Path(path).open("r", encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            raw = (row.get(column) or "").strip()
            total += float(raw) if raw else 0.0
    return total
