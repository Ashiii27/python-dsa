"""Lesson 04 exercises — loops and comprehensions."""
from __future__ import annotations


def squares_of_evens(nums: list[int]) -> list[int]:
    """Squares of the even numbers, in order. Use one comprehension."""
    raise NotImplementedError


def index_of_first(nums: list[int], target: int) -> int:
    """Index of the first occurrence of target, or -1. Use a for/else."""
    raise NotImplementedError


def transpose(grid: list[list[int]]) -> list[list[int]]:
    """Transpose a rectangular grid. [] -> []."""
    raise NotImplementedError


def flatten_matrix(grid: list[list[int]]) -> list[int]:
    """Row-major flatten with a nested comprehension."""
    raise NotImplementedError


def running_total(nums: list[int]) -> list[int]:
    """Prefix sums: [1,2,3] -> [1,3,6]."""
    raise NotImplementedError


def chunk(items: list, size: int) -> list[list]:
    """Split into consecutive chunks of at most `size`. size <= 0 -> ValueError."""
    raise NotImplementedError


def first_non_repeating(text: str) -> str | None:
    """First character occurring exactly once, else None."""
    raise NotImplementedError


def collatz_steps(n: int) -> int:
    """Steps to reach 1 (n even -> n//2, odd -> 3n+1). collatz_steps(1) == 0."""
    raise NotImplementedError
