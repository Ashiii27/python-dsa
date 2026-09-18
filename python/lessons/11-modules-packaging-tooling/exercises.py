"""Lesson 11 exercises — module design and a CLI entry point."""
from __future__ import annotations

from typing import Sequence

VERSION = "0.1.0"


def word_frequencies(text: str) -> dict[str, int]:
    """Lowercased word counts (split on non-word characters)."""
    raise NotImplementedError


def format_report(freqs: dict[str, int], top: int) -> str:
    """Lines 'word: count' for the top N (count desc, word asc), joined by '\\n'.
    Empty input -> ''."""
    raise NotImplementedError


def build_parser():
    """Return an argparse.ArgumentParser with:
      positional 'text'
      -n/--top int, default 3
      --version action='version' printing VERSION
    """
    raise NotImplementedError


def main(argv: Sequence[str] | None = None) -> int:
    """Parse argv, print the report, return 0."""
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit(main())
