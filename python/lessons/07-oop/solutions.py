"""Lesson 07 reference solutions."""
from __future__ import annotations

import math


class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    __rmul__ = __mul__

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __abs__(self) -> float:
        return math.hypot(self.x, self.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


class Stack:
    def __init__(self) -> None:
        self._items: list = []

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __contains__(self, item) -> bool:
        return item in self._items

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        self.celsius = (value - 32) * 5 / 9

    @classmethod
    def from_fahrenheit(cls, value: float) -> "Temperature":
        return cls((value - 32) * 5 / 9)

    def __repr__(self) -> str:
        return f"Temperature({self._celsius})"


class Task:
    def __init__(self, name: str, priority: int) -> None:
        self.name = name
        self.priority = priority

    def __lt__(self, other: "Task") -> bool:
        return self.priority < other.priority

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return (self.name, self.priority) == (other.name, other.priority)

    def __hash__(self) -> int:
        return hash((self.name, self.priority))

    def __repr__(self) -> str:
        return f"Task({self.name!r}, {self.priority})"
