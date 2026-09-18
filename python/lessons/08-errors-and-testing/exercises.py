"""Lesson 08 exercises — errors and context managers."""
from __future__ import annotations

from typing import Iterator


class ValidationError(Exception):
    """Base class for this module's errors."""


class OutOfRange(ValidationError):
    """Raised when a value is outside the allowed range; exposes .value."""


def parse_int(text: str, default: int | None = None) -> int | None:
    """Parse text as int. On failure return default; if default is None, re-raise
    a ValueError whose message is exactly 'invalid int: <text>' chained from the original."""
    raise NotImplementedError


def validate_age(age: int) -> int:
    """Return age if 0 <= age <= 130, else raise OutOfRange with .value set."""
    raise NotImplementedError


def safe_get(data: dict, *keys):
    """Walk nested dicts with EAFP; return None if any key is missing
    or an intermediate value is not a dict."""
    raise NotImplementedError


def divide_all(nums: list[float], denom: float) -> list[float | None]:
    """Divide each number by denom; entries that fail become None. Never raise."""
    raise NotImplementedError


def collecting() -> Iterator[list]:
    """Context manager yielding a list; on exit every item is doubled in place.

    with collecting() as bucket:
        bucket.append(2)
    # bucket == [4]
    Doubling must happen even if the body raises.
    """
    raise NotImplementedError


def retry(times: int, fn):
    """Call fn() up to `times` times, returning its first successful result.
    If all attempts raise, re-raise the last exception. times < 1 -> ValueError."""
    raise NotImplementedError
