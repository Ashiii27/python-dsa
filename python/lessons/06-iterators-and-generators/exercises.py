"""Lesson 06 exercises — laziness."""
from __future__ import annotations

from typing import Iterable, Iterator


def countdown(n: int) -> Iterator[int]:
    """Yield n, n-1, ..., 1."""
    raise NotImplementedError


def take(iterable: Iterable, n: int) -> list:
    """First n items of any iterable (works on infinite ones)."""
    raise NotImplementedError


def evens() -> Iterator[int]:
    """Infinite generator: 0, 2, 4, ..."""
    raise NotImplementedError


def sliding_pairs(items: Iterable) -> Iterator[tuple]:
    """Yield consecutive pairs: [1,2,3] -> (1,2), (2,3). Fewer than 2 items -> nothing."""
    raise NotImplementedError


def run_length_encode(text: str) -> list[tuple[str, int]]:
    """'aaabbc' -> [('a',3), ('b',2), ('c',1)]."""
    raise NotImplementedError


def flatten_once(nested: Iterable[Iterable]) -> list:
    """Concatenate one level: [[1,2],[3]] -> [1,2,3]."""
    raise NotImplementedError


def unique_justseen(items: Iterable) -> Iterator:
    """Drop *consecutive* duplicates: [1,1,2,1] -> 1, 2, 1."""
    raise NotImplementedError


def fib_stream() -> Iterator[int]:
    """Infinite Fibonacci generator starting 0, 1, 1, 2, 3, ..."""
    raise NotImplementedError


def lazy_sum_of_squares(limit: int) -> int:
    """Sum of i*i for i in range(limit) using a generator expression (no list)."""
    raise NotImplementedError
