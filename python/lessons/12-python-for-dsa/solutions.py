"""Lesson 12 reference solutions."""
from __future__ import annotations

import heapq
from bisect import bisect_left
from collections import defaultdict, deque
from itertools import accumulate


def top_k_largest(nums: list[int], k: int) -> list[int]:
    return heapq.nlargest(k, nums)


def k_smallest_with_heap(nums: list[int], k: int) -> list[int]:
    return heapq.nsmallest(k, nums)


def lower_bound(sorted_nums: list[int], target: int) -> int:
    return bisect_left(sorted_nums, target)


def prefix_sums(nums: list[int]) -> list[int]:
    return list(accumulate(nums, initial=0))


def build_graph(edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return dict(graph)


def bfs_order(graph: dict[int, list[int]], start: int) -> list[int]:
    seen = {start}
    queue = deque([start])
    order: list[int] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, ()):
            if neighbour not in seen:
                seen.add(neighbour)
                queue.append(neighbour)
    return order


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = defaultdict(list)
    for word in words:
        groups[tuple(sorted(word))].append(word)
    return list(groups.values())


def climb_stairs(n: int) -> int:
    """Bottom-up DP: O(n) time, O(1) space, and no recursion-limit risk."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 1, 1  # ways to climb 0 and 1 stairs
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def iterative_inorder(root) -> list[int]:
    out: list[int] = []
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        out.append(node.val)
        node = node.right
    return out
