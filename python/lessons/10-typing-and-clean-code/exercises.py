"""Lesson 10 exercises — typing and dataclasses."""
from __future__ import annotations

from typing import Iterable, TypeVar

T = TypeVar("T")


class Point:
    """Make this an immutable, hashable dataclass with fields x: int, y: int
    and a method distance_to(other) -> float."""


class Student:
    """Dataclass with: name: str, grades: list[float] (default empty list),
    ordered by (average desc is NOT required) — just support:
      .average -> float (0.0 when no grades)
      .add(grade) -> None, raising ValueError outside 0..100
    """


def first_or_none(items: Iterable[T]) -> T | None:
    """Return the first item or None. Must work on any iterable."""
    raise NotImplementedError


def group_students(students: list) -> dict[str, list[str]]:
    """Bucket student names by grade band using their .average:
    'A' >= 90, 'B' >= 80, 'C' >= 70, else 'F'. Names keep input order."""
    raise NotImplementedError
