# Python Foundations: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Treat Python collections as data structures with explicit cost models. Fluency means choosing the right built-in, understanding mutation and references, and avoiding operations that hide linear work.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | `list`: dynamic array; O(1) amortized append and O(n) front insertion/removal. |
| 2 | `dict` / `set`: average O(1) membership; keys must be hashable. |
| 3 | `deque`: O(1) operations at both ends; preferred for queues and BFS. |
| 4 | `Counter`, `defaultdict`, `heapq`, and `bisect`: standard tools that remove boilerplate. |
| 5 | Sorting is stable; tuple keys express deterministic multi-field ordering. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need counts or grouping | `Counter` or `defaultdict(list)` |
| FIFO processing | `collections.deque` |
| Repeated smallest/largest item | `heapq` |
| Search in sorted data | `bisect_left` / `bisect_right` |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

```python
from collections import Counter

words = ["tea", "eat", "tea", "tan"]
frequency = Counter(words)
# Counter({'tea': 2, 'eat': 1, 'tan': 1})
most_common = frequency.most_common(1)  # [('tea', 2)]
```
The number of dictionary entries is the number of distinct words, not the total input size.

## Tricks and interview notes

- Accumulate strings in a list and call `"".join(parts)` instead of repeated concatenation.
- Use `enumerate`, `zip`, and tuple unpacking to make index relationships explicit.
- Copy nested data intentionally: `matrix[:]` is shallow; `[row[:] for row in matrix]` copies rows.
- Remember that `heapq` is a min-heap; store negative priorities only when a max-heap is truly needed.

## Common mistakes

- **Watch for:** Using `list.pop(0)` as a queue.
- **Watch for:** Mutating a list or dictionary while iterating over it.
- **Watch for:** Using a mutable object as a default argument.
- **Watch for:** Assuming slices are O(1); they copy and cost O(k).

## Implementation drills

1. Implement a frequency counter without `Counter`.
2. Group records with `defaultdict`.
3. Maintain top k values with a size-k heap.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. The standard-library toolkit

Nine tools cover most of DSA Python: `list`, `dict`, `set`, `Counter`,
`defaultdict`, `deque`, `heapq`, `bisect`, and `itertools`. Learn their costs as
well as their syntax.

```python
from bisect import bisect_left, bisect_right, insort
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, nlargest
from itertools import accumulate, combinations, permutations
import sys

nums = [3, 1, 2, 1, 2, 3, 3]

# Counter: build a frequency map in one line.
counts = Counter(nums)
print("Counter:", dict(counts), "| most_common(2):", counts.most_common(2))

# defaultdict: no "key in dict" branch needed.
positions = defaultdict(list)
for i, x in enumerate(nums):
    positions[x].append(i)
print("positions[3]:", positions[3], "| missing key stays empty:", positions[99])

# deque: O(1) at both ends. list.pop(0) is O(n) — never use it in a queue.
window = deque([1, 2, 3])
window.append(4)
window.popleft()
print("deque after append(4), popleft():", list(window))

# heapq: a min-heap. Negate the value for max-heap behaviour.
heap = []
for x in (5, 1, 4, 2):
    heappush(heap, x)
print("heap pop order:", [heappop(heap) for _ in range(4)])
print("two largest:", nlargest(2, nums))

# bisect: binary search over an already-sorted list.
ordered = [1, 3, 3, 5, 7]
print("bisect_left(3):", bisect_left(ordered, 3), "| bisect_right(3):", bisect_right(ordered, 3))
insort(ordered, 4)
print("after insort(4):", ordered)

# itertools: prefix sums and enumeration of choices.
print("prefix sums:", list(accumulate([1, 2, 3], initial=0)))
print("combinations:", list(combinations("abc", 2)))
print("permutations:", list(permutations("ab", 2)))

# Sorting with keys beats writing comparators.
words = ["banana", "kiwi", "apple", "fig"]
print("by length:", sorted(words, key=len))
print("by (length, alpha):", sorted(words, key=lambda w: (len(w), w)))

# Deep DFS needs a raised recursion limit (or an explicit stack).
print("default recursion limit:", sys.getrecursionlimit())
sys.setrecursionlimit(100_000)
print("raised to:", sys.getrecursionlimit())
```

Output:

```text
Counter: {3: 3, 1: 2, 2: 2} | most_common(2): [(3, 3), (1, 2)]
positions[3]: [0, 5, 6] | missing key stays empty: []
deque after append(4), popleft(): [2, 3, 4]
heap pop order: [1, 2, 4, 5]
two largest: [3, 3]
bisect_left(3): 1 | bisect_right(3): 3
after insort(4): [1, 3, 3, 4, 5, 7]
prefix sums: [0, 1, 3, 6]
combinations: [('a', 'b'), ('a', 'c'), ('b', 'c')]
permutations: [('a', 'b'), ('b', 'a')]
by length: ['fig', 'kiwi', 'apple', 'banana']
by (length, alpha): ['fig', 'kiwi', 'apple', 'banana']
default recursion limit: 1000
raised to: 100000
```

**How it works**

- `Counter.most_common(k)` already uses a heap internally, so you rarely need to write one.
- `defaultdict(list)` removes the branch; prefer `.get(key, default)` when you do not want the key inserted as a side effect.
- `heapq` implements a **min**-heap only. For a max-heap push `-x` and negate on pop; for tie-safe ordering push tuples like `(priority, counter, item)`.
- `bisect_left` / `bisect_right` are the two boundaries you need for "count of items `< x`", "first index `>= x`", and insertion points.
- `sorted(..., key=...)` is stable, so multi-key sorts compose: sort by the least important key first, or use a tuple key as above.

### 2. Idioms you will type in every solution

```python
from functools import lru_cache
import sys

# Tuple swap: no temporary variable.
a, b = 3, 5
a, b = b, a
print("swap:", a, b)

# enumerate gives index and value together.
for i, x in enumerate([10, 20, 30]):
    print(f"  nums[{i}] = {x}")

# zip walks two sequences in lockstep.
for name, score in zip(["ada", "alan"], [95, 88]):
    print(" ", name, score)

# Build grids with a comprehension: [[0] * 3] * 2 would share one row object.
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print("grid:", grid)

# Never grow strings in a loop (O(n^2)); collect and join once.
parts = []
for ch in "abc":
    parts.append(ch)
print("join:", "".join(parts))

# Contests: read all input at once and parse it.
def read_ints(text):
    return list(map(int, text.split()))

print("parsed:", read_ints("1 2 3"))
print("fast read pattern: data = sys.stdin.buffer.read().split()")

# lru_cache: top-down DP without writing the table by hand.
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print("fib(30):", fib(30), "| calls cached:", fib.cache_info().hits > 0)
```

Output:

```text
swap: 5 3
  nums[0] = 10
  nums[1] = 20
  nums[2] = 30
  ada 95
  alan 88
grid: [[1, 0, 0], [0, 0, 0]]
join: abc
parsed: [1, 2, 3]
fast read pattern: data = sys.stdin.buffer.read().split()
fib(30): 832040 | calls cached: True
```

**How it works**

- `a, b = b, a` builds a tuple and unpacks it; the right-hand side is evaluated first, which is why no temporary is needed.
- `[[0] * 3 for _ in range(2)]` creates three fresh rows; `[[0] * 3] * 2` repeats the *same* row object, so `grid[0][0] = 1` would appear in both rows.
- `sys.stdin.buffer.read().split()` reads bytes (faster than text) and is the standard fast-input trick.
- `@lru_cache` memoizes on the arguments, turning the exponential Fibonacci recursion into O(n). Note that it needs hashable arguments and adds O(n) memory.

## Solved examples

### Example 1 — Group anagrams (Medium)

**Problem.** Given a list of strings, group the anagrams together.

**Approach.** Anagrams are exactly the strings with the same sorted characters, so `sorted(word)` is a canonical key. Insert every word into a `defaultdict(list)` under that key; the values are the groups. Using `"".join(sorted(word))` (a string) rather than a list makes the key hashable.

```python
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))       # "eat", "tea", "ate" -> "aet"
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for group in group_anagrams(words):
        print(sorted(group))
    print("single word:", group_anagrams(["hello"]))
    print("empty input:", group_anagrams([]))
```

Output:

```text
['ate', 'eat', 'tea']
['nat', 'tan']
['bat']
single word: [['hello']]
empty input: []
```

**Complexity.** O(n · k log k) time where n is the number of words and k the maximum length (sorting each word); O(n · k) space. A counting-sort signature (`tuple(Counter(word).items())`) is O(n · k) but is only worth it for long words.

### Example 2 — Top k frequent elements (Medium)

**Problem.** Given `nums` and `k`, return the `k` most frequent elements.

**Approach.** Count with `Counter`, then take the `k` largest by frequency. `Counter.most_common(k)` does exactly this with a heap internally. The alternative — sorting all items — costs O(n log n) instead of O(n log k), which matters when n is large and k is small.

```python
from collections import Counter
from heapq import nlargest
from operator import itemgetter


def top_k_frequent(nums, k):
    counts = Counter(nums)
    return [num for num, _ in counts.most_common(k)]


def top_k_frequent_heap(nums, k):
    """Same result using heapq directly — use this shape when the interviewer
    asks you not to use Counter.most_common."""
    counts = Counter(nums)
    return [num for num, _ in nlargest(k, counts.items(), key=itemgetter(1))]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print("most_common:", top_k_frequent(nums, 2))
    print("heapq      :", top_k_frequent_heap(nums, 2))
    print("k > length :", top_k_frequent([4, 4], 5))
    print("empty      :", top_k_frequent([], 2))
```

Output:

```text
most_common: [1, 2]
heapq      : [1, 2]
k > length : [4]
empty      : []
```

**Complexity.** O(n) to count, then O(n log k) to select: better than sorting when k ≪ n. Space O(n) for the frequency map. Note the tie behaviour: with equal frequencies the order comes from insertion order, so ask whether any valid answer is acceptable.

### Example 3 — Largest number (Medium)

**Problem.** Arrange non-negative integers so that they form the largest possible number, returned as a string.

**Approach.** Sorting numbers numerically is wrong (`10` vs `2` → `210` beats `102`). The correct pairwise rule is: put `a` before `b` when `a + b > b + a` (string concatenation). This is a custom comparison, so we translate it with `functools.cmp_to_key`. Finally strip leading zeros: `[0, 0]` must return `"0"`.

```python
from functools import cmp_to_key


def largest_number(nums):
    if not nums:
        return ""
    parts = list(map(str, nums))

    def compare(a, b):
        if a + b > b + a:
            return -1        # a comes first
        if a + b < b + a:
            return 1
        return 0

    parts.sort(key=cmp_to_key(compare))
    result = "".join(parts)
    return "0" if result[0] == "0" else result


if __name__ == "__main__":
    print(largest_number([10, 2]))              # 210
    print(largest_number([3, 30, 34, 5, 9]))    # 9534330
    print(largest_number([0, 0]))               # 0
    print(largest_number([1]))                  # 1
```

Output:

```text
210
9534330
0
1
```

**Complexity.** O(n log n · k) time (n comparisons of strings of length k) and O(n · k) space for the string forms. `cmp_to_key` is slower than a `key=` function, so prefer tuple keys when the ordering can be expressed that way.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Python Lists](https://www.hackerrank.com/challenges/python-lists/problem) | HackerRank | Easy |
| [Company Logo](https://www.hackerrank.com/challenges/most-commons/problem) | HackerRank | Medium |
| [Word Order](https://www.hackerrank.com/challenges/word-order/problem) | HackerRank | Medium |
| [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem) | HackerRank | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
