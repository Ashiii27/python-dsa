# Lesson 12 — Python Performance & Idioms for DSA

This is the handoff lesson: everything here is what you will actually type during
interviews and contests. After it, go to [`topics/01-complexity-analysis`](../../../topics/01-complexity-analysis/README.md).

## 1. Operation costs to memorise

```text
list index/append          O(1)         list insert(0)/pop(0)   O(n)
list slice / copy          O(k)         x in list               O(n)
dict/set get/add/in        O(1) avg     sorting                 O(n log n)
heapq push/pop             O(log n)     heapify                 O(n)
bisect insort              O(n) (shift) bisect search           O(log n)
str concat in loop         O(n^2)       "".join(parts)          O(n)
deque append/pop both ends O(1)
```

## 2. The competitive-Python toolkit

```python
import sys
input = sys.stdin.readline          # 10x faster input in contests
data = sys.stdin.buffer.read().split()

from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify, nlargest, nsmallest
from bisect import bisect_left, bisect_right, insort
from functools import lru_cache, cache, cmp_to_key, reduce
from itertools import accumulate, permutations, combinations, product
from math import inf, gcd, lcm, isqrt, comb, perm

sys.setrecursionlimit(300000)       # DFS on big graphs
```

## 3. Idioms that replace whole algorithms

```python
heapq.nlargest(k, nums)                  # top-k
counts = Counter(s)                      # frequency map
graph = defaultdict(list)                # adjacency list
dist = [inf] * n                         # Dijkstra init
prefix = list(accumulate(nums, initial=0))
i = bisect_left(sorted_list, target)     # lower bound
max_heap: push -value, pop -value        # heapq is min-only
sorted(words, key=lambda w: (len(w), w)) # multi-key sort
grid = [[0] * m for _ in range(n)]       # never [[0]*m]*n
dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)    # 4-directional moves
@cache                                    # top-down DP in one line
```

## 4. Recursion → iteration

Python has no TCO and a ~1000-frame limit. Convert deep DFS to an explicit stack:

```python
stack = [(root, False)]
while stack:
    node, visited = stack.pop()
    if node is None: continue
    if visited:
        process(node)                       # post-order
    else:
        stack.append((node, True))
        stack.append((node.right, False))
        stack.append((node.left, False))
```

## 5. Measuring instead of guessing

```python
import timeit; timeit.timeit("sum(range(1000))", number=10000)
python -m cProfile -s cumtime script.py
```

Micro-optimisations that actually help: local variable lookups inside hot loops,
avoiding attribute access in loops (`append = out.append`), using builtins (`sum`, `min`, `any`)
which run in C, and choosing the right container in the first place.

## Checkpoints
- How do you build a max-heap with `heapq`?
- What is the cost of `bisect.insort` and why?
- Why does `"".join` beat `+=` for strings?

## Practice
`python test_exercises.py`, then start the DSA curriculum.
