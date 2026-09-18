"""Lesson 05 reference solutions."""
from __future__ import annotations

import functools
from typing import Callable


def append_to(item, bucket: list | None = None) -> list:
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


def apply_n(fn: Callable[[int], int], n: int, x: int) -> int:
    for _ in range(n):
        x = fn(x)
    return x


def make_counter(start: int = 0) -> Callable[[], int]:
    value = start

    def inc() -> int:
        nonlocal value
        value += 1
        return value

    return inc


def make_multipliers(n: int) -> list[Callable[[int], int]]:
    return [(lambda x, i=i: i * x) for i in range(n)]


def counted(fn: Callable) -> Callable:
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@functools.lru_cache(maxsize=None)
def memoized_fib(n: int) -> int:
    if n < 2:
        return n
    return memoized_fib(n - 1) + memoized_fib(n - 2)


def summarize(*nums: float, precision: int = 2, label: str = "sum") -> str:
    return f"{label}={round(sum(nums), precision)}"
