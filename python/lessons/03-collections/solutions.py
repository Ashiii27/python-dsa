"""Lesson 03 reference solutions."""
from __future__ import annotations

from collections import Counter, defaultdict


def make_grid(rows: int, cols: int) -> list[list[int]]:
    return [[0] * cols for _ in range(rows)]


def dedupe_keep_order(items: list) -> list:
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def word_count(text: str) -> dict[str, int]:
    return dict(Counter(text.lower().split()))


def top_k_words(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ordered[:k]


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def common_elements(a: list[int], b: list[int]) -> list[int]:
    return sorted(set(a) & set(b))


def invert(mapping: dict) -> dict:
    return {value: key for key, value in mapping.items()}


def rotate(items: list, k: int) -> list:
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else list(items)


def flatten(nested: list) -> list:
    out: list = []
    stack = list(reversed(nested))
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(reversed(item))
        else:
            out.append(item)
    return out
