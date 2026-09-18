"""Lesson 11 reference solutions."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from typing import Sequence

VERSION = "0.1.0"
_WORD = re.compile(r"\w+")


def word_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(_WORD.findall(text.lower())))


def format_report(freqs: dict[str, int], top: int) -> str:
    ordered = sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    return "\n".join(f"{word}: {count}" for word, count in ordered)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="wordcount", description="Count words in text.")
    parser.add_argument("text", help="text to analyse")
    parser.add_argument("-n", "--top", type=int, default=3, help="how many words to show")
    parser.add_argument("--version", action="version", version=VERSION)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    print(format_report(word_frequencies(args.text), args.top))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
