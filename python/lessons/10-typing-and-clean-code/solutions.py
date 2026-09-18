"""Lesson 10 reference solutions."""
from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Iterable, TypeVar

T = TypeVar("T")

_BANDS: tuple[tuple[float, str], ...] = ((90, "A"), (80, "B"), (70, "C"))


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def distance_to(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


@dataclass
class Student:
    name: str
    grades: list[float] = field(default_factory=list)

    @property
    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def add(self, grade: float) -> None:
        if not 0 <= grade <= 100:
            raise ValueError(f"grade out of range: {grade}")
        self.grades.append(grade)


def first_or_none(items: Iterable[T]) -> T | None:
    return next(iter(items), None)


def _band(average: float) -> str:
    for threshold, label in _BANDS:
        if average >= threshold:
            return label
    return "F"


def group_students(students: list) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for student in students:
        groups.setdefault(_band(student.average), []).append(student.name)
    return groups
