"""Lesson 07 exercises — classes."""
from __future__ import annotations


class Vector:
    """2D vector supporting +, -, scalar *, ==, abs(), repr, and hashing.

    repr must be exactly: Vector(1, 2)
    abs(Vector(3, 4)) == 5.0
    """

    def __init__(self, x: float, y: float) -> None:
        raise NotImplementedError


class Stack:
    """LIFO stack: push, pop (IndexError when empty), peek, len(), bool(), 'in'."""

    def __init__(self) -> None:
        raise NotImplementedError


class Temperature:
    """Stores celsius. `fahrenheit` is a read/write property.

    Setting celsius below -273.15 raises ValueError.
    Temperature.from_fahrenheit(212).celsius == 100
    """

    def __init__(self, celsius: float) -> None:
        raise NotImplementedError


class Task:
    """Comparable by priority (lower first) so it works in heapq and sorted().

    Attributes: name, priority. repr: Task('a', 1)
    """

    def __init__(self, name: str, priority: int) -> None:
        raise NotImplementedError
