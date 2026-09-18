"""Lesson 06 reference solutions."""
from __future__ import annotations

from itertools import count, groupby, islice
from typing import Iterable, Iterator


def countdown(n: int) -> Iterator[int]:
    while n > 0:
        yield n
        n -= 1


def take(iterable: Iterable, n: int) -> list:
    return list(islice(iterable, n))


def evens() -> Iterator[int]:
    for n in count(0, 2):
        yield n


def sliding_pairs(items: Iterable) -> Iterator[tuple]:
    it = iter(items)
    try:
        previous = next(it)
    except StopIteration:
        return
    for current in it:
        yield (previous, current)
        previous = current


def run_length_encode(text: str) -> list[tuple[str, int]]:
    return [(ch, sum(1 for _ in group)) for ch, group in groupby(text)]


def flatten_once(nested: Iterable[Iterable]) -> list:
    return [item for sub in nested for item in sub]


def unique_justseen(items: Iterable) -> Iterator:
    for key, _group in groupby(items):
        yield key


def fib_stream() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def lazy_sum_of_squares(limit: int) -> int:
    return sum(i * i for i in range(limit))
