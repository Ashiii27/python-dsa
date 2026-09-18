"""Lesson 04 reference solutions."""
from __future__ import annotations

from collections import Counter
from itertools import accumulate


def squares_of_evens(nums: list[int]) -> list[int]:
    return [n * n for n in nums if n % 2 == 0]


def index_of_first(nums: list[int], target: int) -> int:
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1


def transpose(grid: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*grid)]


def flatten_matrix(grid: list[list[int]]) -> list[int]:
    return [value for row in grid for value in row]


def running_total(nums: list[int]) -> list[int]:
    return list(accumulate(nums))


def chunk(items: list, size: int) -> list[list]:
    if size <= 0:
        raise ValueError("size must be positive")
    return [items[i:i + size] for i in range(0, len(items), size)]


def first_non_repeating(text: str) -> str | None:
    counts = Counter(text)
    for ch in text:
        if counts[ch] == 1:
            return ch
    return None


def collatz_steps(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
