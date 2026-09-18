"""Lesson 01 exercises — syntax, truthiness, identity, f-strings.

Fill in each function. Run `python test_exercises.py` to grade.
"""
from __future__ import annotations


def greet(name: str) -> str:
    """Return 'Hello, <name>! Your name has <n> letters.' using an f-string."""
    raise NotImplementedError


def classify(n: int) -> str:
    """Return 'negative', 'zero', or 'positive'."""
    raise NotImplementedError


def is_truthy(value: object) -> bool:
    """Return Python's truthiness of value (without using bool())."""
    raise NotImplementedError


def same_object(a: object, b: object) -> bool:
    """Return True only if a and b are the *same* object."""
    raise NotImplementedError


def fizzbuzz(n: int) -> list[str]:
    """Return FizzBuzz for 1..n as strings: '1', '2', 'Fizz', ... 'FizzBuzz'."""
    raise NotImplementedError


def safe_div(a: float, b: float) -> float | None:
    """Return a / b, or None when b == 0. Do not raise."""
    raise NotImplementedError
