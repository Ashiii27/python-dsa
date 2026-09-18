"""Lesson 12 exercises — the DSA toolkit in Python."""
from __future__ import annotations


def top_k_largest(nums: list[int], k: int) -> list[int]:
    """The k largest values, descending. Use heapq, not a full sort."""
    raise NotImplementedError


def k_smallest_with_heap(nums: list[int], k: int) -> list[int]:
    """The k smallest values, ascending, using a heap."""
    raise NotImplementedError


def lower_bound(sorted_nums: list[int], target: int) -> int:
    """First index whose value is >= target (len if none). Use bisect."""
    raise NotImplementedError


def prefix_sums(nums: list[int]) -> list[int]:
    """Prefix array of length n+1 with a leading 0."""
    raise NotImplementedError


def build_graph(edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    """Undirected adjacency list with defaultdict; neighbours in insertion order."""
    raise NotImplementedError


def bfs_order(graph: dict[int, list[int]], start: int) -> list[int]:
    """Visit order of a BFS from start using deque."""
    raise NotImplementedError


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group anagrams; groups in first-appearance order, words in input order."""
    raise NotImplementedError


def climb_stairs(n: int) -> int:
    """Number of ways to climb n stairs taking 1 or 2 steps. Must handle n=500 fast."""
    raise NotImplementedError


def iterative_inorder(root) -> list[int]:
    """In-order traversal of a binary tree with nodes having .val/.left/.right,
    using an explicit stack (no recursion). root may be None."""
    raise NotImplementedError
