"""Lesson 02 reference solutions."""
from __future__ import annotations

import math


def digits_sum(n: int) -> int:
    return sum(int(ch) for ch in str(abs(n)))


def floor_div_mod(a: int, b: int) -> tuple[int, int]:
    return divmod(a, b)


def almost_equal(a: float, b: float) -> bool:
    return math.isclose(a, b, rel_tol=1e-9)


def build_sentence(words: list[str]) -> str:
    if not words:
        return ""
    return " ".join(words) + "."


def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def is_palindrome(text: str) -> bool:
    cleaned = [ch.lower() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]


def title_initials(full_name: str) -> str:
    return "".join(f"{part[0].upper()}." for part in full_name.split())


def to_base(n: int, base: int) -> str:
    if not 2 <= base <= 16:
        raise ValueError("base must be in 2..16")
    if n == 0:
        return "0"
    digits = "0123456789abcdef"
    out: list[str] = []
    while n:
        n, r = divmod(n, base)
        out.append(digits[r])
    return "".join(reversed(out))
