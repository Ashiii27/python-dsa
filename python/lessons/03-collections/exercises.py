"""Lesson 03 exercises — containers."""
from __future__ import annotations


def make_grid(rows: int, cols: int) -> list[list[int]]:
    """Return a rows x cols grid of zeros where each row is an independent list."""
    raise NotImplementedError


def dedupe_keep_order(items: list) -> list:
    """Remove duplicates while preserving first-seen order. O(n)."""
    raise NotImplementedError


def word_count(text: str) -> dict[str, int]:
    """Count whitespace-separated, lowercased words."""
    raise NotImplementedError


def top_k_words(text: str, k: int) -> list[tuple[str, int]]:
    """Top k (word, count) sorted by count desc, then word asc."""
    raise NotImplementedError


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Map word length -> list of words in input order."""
    raise NotImplementedError


def common_elements(a: list[int], b: list[int]) -> list[int]:
    """Sorted list of values present in both, each once."""
    raise NotImplementedError


def invert(mapping: dict) -> dict:
    """Swap keys and values. On duplicate values, the last key wins."""
    raise NotImplementedError


def rotate(items: list, k: int) -> list:
    """Return a new list rotated right by k (k may exceed len or be negative)."""
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Fully flatten arbitrarily nested lists: [1,[2,[3]]] -> [1,2,3]."""
    raise NotImplementedError
