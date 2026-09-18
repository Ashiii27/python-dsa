"""Lesson 08 reference solutions."""
from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator


class ValidationError(Exception):
    """Base class for this module's errors."""


class OutOfRange(ValidationError):
    def __init__(self, value: object) -> None:
        super().__init__(f"value out of range: {value}")
        self.value = value


def parse_int(text: str, default: int | None = None) -> int | None:
    try:
        return int(text)
    except (TypeError, ValueError) as exc:
        if default is None:
            raise ValueError(f"invalid int: {text}") from exc
        return default


def validate_age(age: int) -> int:
    if not 0 <= age <= 130:
        raise OutOfRange(age)
    return age


def safe_get(data: dict, *keys):
    current = data
    for key in keys:
        try:
            current = current[key]
        except (KeyError, TypeError, IndexError):
            return None
    return current


def divide_all(nums: list[float], denom: float) -> list[float | None]:
    out: list[float | None] = []
    for n in nums:
        try:
            out.append(n / denom)
        except (ZeroDivisionError, TypeError):
            out.append(None)
    return out


@contextmanager
def collecting() -> Iterator[list]:
    bucket: list = []
    try:
        yield bucket
    finally:
        bucket[:] = [item * 2 for item in bucket]


def retry(times: int, fn):
    if times < 1:
        raise ValueError("times must be >= 1")
    last: Exception | None = None
    for _ in range(times):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - deliberate retry boundary
            last = exc
    assert last is not None
    raise last
