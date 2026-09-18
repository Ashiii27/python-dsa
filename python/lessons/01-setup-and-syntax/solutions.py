"""Lesson 01 reference solutions."""
from __future__ import annotations


def greet(name: str) -> str:
    return f"Hello, {name}! Your name has {len(name)} letters."


def classify(n: int) -> str:
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"


def is_truthy(value: object) -> bool:
    if value:
        return True
    return False


def same_object(a: object, b: object) -> bool:
    return a is b


def fizzbuzz(n: int) -> list[str]:
    out: list[str] = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


def safe_div(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b
