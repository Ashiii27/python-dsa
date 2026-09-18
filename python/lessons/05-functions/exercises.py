"""Lesson 05 exercises — functions, closures, decorators."""
from __future__ import annotations

from typing import Callable


def append_to(item, bucket: list | None = None) -> list:
    """Append item to bucket and return it. A fresh list is used when bucket is None.
    Must NOT share state between calls."""
    raise NotImplementedError


def apply_n(fn: Callable[[int], int], n: int, x: int) -> int:
    """Apply fn to x, n times. apply_n(f, 0, x) == x."""
    raise NotImplementedError


def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a function that returns start+1, start+2, ... on each call."""
    raise NotImplementedError


def make_multipliers(n: int) -> list[Callable[[int], int]]:
    """Return [f0, f1, ... f(n-1)] where fi(x) == i * x (beware late binding)."""
    raise NotImplementedError


def counted(fn: Callable) -> Callable:
    """Decorator: wrapper.calls counts invocations; name/doc are preserved."""
    raise NotImplementedError


def memoized_fib(n: int) -> int:
    """nth Fibonacci (fib(0)=0, fib(1)=1) computed with caching, fast for n=200."""
    raise NotImplementedError


def summarize(*nums: float, precision: int = 2, label: str = "sum") -> str:
    """Return '<label>=<total rounded to precision>'. summarize(1, 2) == 'sum=3'."""
    raise NotImplementedError
