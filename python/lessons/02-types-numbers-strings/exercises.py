"""Lesson 02 exercises — numbers and strings."""
from __future__ import annotations


def digits_sum(n: int) -> int:
    """Sum the decimal digits of abs(n). digits_sum(-123) == 6."""
    raise NotImplementedError


def floor_div_mod(a: int, b: int) -> tuple[int, int]:
    """Return (a // b, a % b) using Python semantics, via one builtin call."""
    raise NotImplementedError


def almost_equal(a: float, b: float) -> bool:
    """True if a and b are equal within a relative tolerance of 1e-9."""
    raise NotImplementedError


def build_sentence(words: list[str]) -> str:
    """Join words with single spaces, efficiently, and end with a period.

    build_sentence(["hi", "there"]) == "hi there."  and [] -> ""
    """
    raise NotImplementedError


def normalize(text: str) -> str:
    """Lowercase, strip outer whitespace, and collapse inner runs of whitespace
    to a single space."""
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """Ignore case and every non-alphanumeric character."""
    raise NotImplementedError


def title_initials(full_name: str) -> str:
    """'ada  lovelace king' -> 'A.L.K.' (uppercase initials, each with a dot)."""
    raise NotImplementedError


def to_base(n: int, base: int) -> str:
    """Render non-negative n in base 2..16 using digits 0-9a-f. to_base(255,16)=='ff'.
    to_base(0, b) == '0'."""
    raise NotImplementedError
