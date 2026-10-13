# Heaps and Priority Queues: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A heap keeps the next extreme item accessible without fully sorting everything. Heap entries should contain all fields needed for deterministic priority and lazy stale-entry detection.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Python `heapq` is a binary min-heap. |
| 2 | Push/pop are O(log n); peek is O(1); heapify is O(n). |
| 3 | A min-heap of size k retains the k largest processed items. |
| 4 | Two heaps split a stream around its median. |
| 5 | K-way merge stores only one frontier item per source. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Repeated next minimum | Min-heap |
| Top k from stream | Size-k min-heap |
| Running median | Two balanced heaps |
| Merge sorted sources | Heap of frontiers |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For top 3 values, push each item. Whenever size becomes 4, pop the minimum. The heap root is the third-largest processed value, and discarded values can never re-enter the top three.

## Tricks and interview notes

- Store `(priority, tie_breaker, item)` when items are not directly comparable.
- Use lazy deletion when arbitrary heap removal would be expensive.
- `heapq.nlargest` is useful, but implement the pattern for interviews.
- Choose a heap over sorting when data streams or only k outputs are needed.

## Common mistakes

- **Watch for:** Negating some but not all max-heap comparisons.
- **Watch for:** Letting equal priorities compare non-orderable objects.
- **Watch for:** Forgetting to remove stale entries.
- **Watch for:** Calling heapify O(n log n); bottom-up heapify is O(n).

## Implementation drills

1. Implement top-k streaming values.
2. Merge k sorted arrays.
3. Maintain a streaming median.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Build a binary heap from scratch

A heap is a **complete** binary tree stored in a flat list: the parent of index
`i` is `(i − 1) // 2`, its children are `2i + 1` and `2i + 2`. The heap property
(every parent ≤ its children) keeps the minimum at index 0, so `peek` is O(1)
while `push` and `pop` are O(log n).

```python
class BinaryHeap:
    """Array-backed min-heap with O(log n) push/pop and O(n) heapify."""

    def __init__(self, values=()):
        self.data = list(values)
        self._heapify()

    # -- internals -------------------------------------------------------
    def _sift_up(self, index):
        """Move a too-small value towards the root."""
        while index > 0:
            parent = (index - 1) // 2
            if self.data[parent] <= self.data[index]:
                break
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent

    def _sift_down(self, index):
        """Move a too-large value towards the leaves; swap with the smaller child."""
        size = len(self.data)
        while True:
            left, right = 2 * index + 1, 2 * index + 2
            smallest = index
            if left < size and self.data[left] < self.data[smallest]:
                smallest = left
            if right < size and self.data[right] < self.data[smallest]:
                smallest = right
            if smallest == index:                    # heap property restored
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def _heapify(self):
        """Build a heap in O(n): sift down from the last internal node upwards."""
        for index in range(len(self.data) // 2 - 1, -1, -1):
            self._sift_down(index)

    # -- public API ------------------------------------------------------
    def push(self, value):
        self.data.append(value)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        if not self.data:
            raise IndexError("pop from an empty heap")
        root = self.data[0]
        last = self.data.pop()                       # move the last leaf to the root
        if self.data:
            self.data[0] = last
            self._sift_down(0)
        return root

    def peek(self):
        return self.data[0] if self.data else None

    def is_heap(self):
        """Verify the heap property — use it to test your own implementation."""
        size = len(self.data)
        return all(self.data[i] <= self.data[child]
                   for i in range(size)
                   for child in (2 * i + 1, 2 * i + 2)
                   if child < size)

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)

    def __repr__(self):
        return f"BinaryHeap({self.data})"


def heap_sort(values):
    """Sort with a heap: O(n log n) time, O(n) extra space here."""
    heap = BinaryHeap(values)
    return [heap.pop() for _ in range(len(heap))]


if __name__ == "__main__":
    heap = BinaryHeap()
    for x in (5, 3, 8, 1, 2):
        heap.push(x)
        print(f"push {x}: {heap.data} | heap property holds: {heap.is_heap()}")
    print("peek (min):", heap.peek())
    print("pop order:", [heap.pop() for _ in range(len(heap))])

    built = BinaryHeap([9, 5, 6, 2, 3])
    print("heapified:", built, "| heap property holds:", built.is_heap())
    print("heap_sort:", heap_sort([9, 5, 6, 2, 3]))

    empty = BinaryHeap()
    try:
        empty.pop()
    except IndexError as exc:
        print("empty pop ->", exc)
```

Output:

```text
push 5: [5] | heap property holds: True
push 3: [3, 5] | heap property holds: True
push 8: [3, 5, 8] | heap property holds: True
push 1: [1, 3, 8, 5] | heap property holds: True
push 2: [1, 2, 8, 5, 3] | heap property holds: True
peek (min): 1
pop order: [1, 2, 3, 5, 8]
heapified: BinaryHeap([2, 3, 6, 5, 9]) | heap property holds: True
heap_sort: [2, 3, 5, 6, 9]
empty pop -> pop from an empty heap
```

**How it works**

- The array layout is the whole trick: no node objects, no pointers. Index arithmetic finds parents and children, and "complete" means the array never has holes.
- `push` appends at the next free slot and sifts **up**; `pop` removes the root, moves the last element there, and sifts **down**, always swapping with the smaller child so the smaller value rises.
- `_heapify` is O(n), not O(n log n): most nodes are near the leaves and barely move, and the sum of the heights is bounded by n. That is why `heapify` beats pushing n items one by one.
- `is_heap` is the test to write first — a broken sift shows up immediately.

### 2. `heapq` patterns you will actually use

Python's `heapq` is a min-heap over a plain list. In interviews it replaces the
class above; know the idioms, including the two that trip people up: heapq is
min-only, and non-comparable payloads need a tie-breaker.

```python
import heapq
from itertools import count

# --- basics -------------------------------------------------------------
heap = []
for x in (5, 3, 8, 1, 2):
    heapq.heappush(heap, x)
print("internal list (not fully sorted):", heap)
print("peek:", heap[0], "| pop:", heapq.heappop(heap))
print("heappushpop(4):", heapq.heappushpop(heap, 4))   # push then pop (cheaper)
print("heapreplace(0):", heapq.heapreplace(heap, 0))   # pop then push
print("heapify in place:", (lambda h: (heapq.heapify(h), h)[1])([9, 5, 6, 2, 3]))

# --- max-heap: negate the values ---------------------------------------
max_heap = []
for x in (5, 3, 8, 1):
    heapq.heappush(max_heap, -x)
print("max-heap pop:", -heapq.heappop(max_heap))

# --- tuples as (priority, payload) -------------------------------------
tasks = [(3, "write tests"), (1, "fix crash"), (2, "review PR")]
heapq.heapify(tasks)
print("priority order:", [heapq.heappop(tasks)[1] for _ in range(len(tasks))])

# --- tie-breaker for non-comparable payloads ---------------------------
counter = count()
jobs = []
for priority, name in ((1, "b"), (1, "a"), (0, "c")):
    heapq.heappush(jobs, (priority, next(counter), name))
print("stable tie-break:", [heapq.heappop(jobs)[2] for _ in range(len(jobs))])

# --- top-k (cheaper than sorting when k << n) --------------------------
nums = [5, 1, 9, 3, 7, 9]
print("nlargest(3):", heapq.nlargest(3, nums), "| nsmallest(2):", heapq.nsmallest(2, nums))


def top_k(values, k):
    """Manual top-k: keep a heap of size k, evicting the smallest."""
    heap = []
    for x in values:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return sorted(heap, reverse=True)


print("manual top_k(3):", top_k(nums, 3))

# --- merging sorted streams --------------------------------------------
streams = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print("heapq.merge:", list(heapq.merge(*streams)))
```

Output:

```text
internal list (not fully sorted): [1, 2, 8, 5, 3]
peek: 1 | pop: 1
heappushpop(4): 2
heapreplace(0): 3
heapify in place: [2, 3, 6, 5, 9]
max-heap pop: 8
priority order: ['fix crash', 'review PR', 'write tests']
stable tie-break: ['c', 'b', 'a']
nlargest(3): [9, 9, 7] | nsmallest(2): [1, 3]
manual top_k(3): [9, 9, 7]
heapq.merge: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**How it works**

- `heapq` functions work on a plain list, and the list is **not** kept fully sorted — only the heap property holds, so never read it directly expecting order.
- `heappushpop` (push then pop) is faster than separate calls when the new item is smaller; `heapreplace` (pop then push) is faster when it is larger. Both keep the heap size fixed, which is exactly what top-k needs.
- Negation gives a max-heap for numbers. For custom ordering, push `(priority, tie_breaker, payload)` — the counter keeps equal priorities in insertion order and prevents comparisons between payloads that do not support them.
- `nlargest` / `nsmallest` are O(n log k); use them instead of `sorted(...)[:k]` when k is small relative to n.

## Solved examples

### Example 1 — Kth largest element in a stream (Easy)

**Problem.** Design a class that takes `k` at construction and returns the k-th
largest element of all numbers added so far.

**Approach.** Keep a min-heap of size k holding the k largest values seen. Its root is the k-th largest answer, so `add` is O(log k) and the query is O(1). Anything smaller than the root can never be in the top k, so it is discarded immediately.

```python
import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)      # evict the smallest of the top k
        return self.heap[0]


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    for value in (3, 5, 10, 9, 4):
        print(f"add {value:>2} -> 3rd largest = {kth.add(value)}")
    print("heap contents (the current top 3):", kth.heap)
    print("fewer than k so far:", KthLargest(3, [1]).add(2))
```

Output:

```text
add  3 -> 3rd largest = 4
add  5 -> 3rd largest = 5
add 10 -> 3rd largest = 5
add  9 -> 3rd largest = 8
add  4 -> 3rd largest = 8
heap contents (the current top 3): [8, 10, 9]
fewer than k so far: 1
```

**Complexity.** O(log k) per `add`, O(k) space — far better than re-sorting the stream each time (O(n log n)).

### Example 2 — Merge k sorted lists (Hard)

**Problem.** Merge `k` sorted sequences into one sorted sequence.

**Approach.** Push the first element of each list onto a heap as `(value, list_index, element_index)`, then repeatedly pop the smallest and push that list's next element. Every pop costs O(log k), so the total is O(n log k) instead of O(n · k) for repeated pairwise merging. The `list_index` tie-breaker matters: without it Python would try to compare the payloads.

```python
import heapq


def merge_k_sorted(lists):
    heap = []
    for list_index, values in enumerate(lists):
        if values:                                  # skip empty inputs
            heapq.heappush(heap, (values[0], list_index, 0))

    merged = []
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        merged.append(value)
        if element_index + 1 < len(lists[list_index]):
            nxt = element_index + 1
            heapq.heappush(heap, (lists[list_index][nxt], list_index, nxt))
    return merged


if __name__ == "__main__":
    print(merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]))
    print(merge_k_sorted([[1, 2, 3]]))
    print("with empty lists:", merge_k_sorted([[], [1], [0, 2]]))
    print("all empty:", merge_k_sorted([[], []]))
```

Output:

```text
[1, 1, 2, 3, 4, 4, 5, 6]
[1, 2, 3]
with empty lists: [0, 1, 2]
all empty: []
```

**Complexity.** O(n log k) time where n is the total number of elements, O(k) space for the heap (O(n) if you count the output). `heapq.merge(*lists)` does the same thing lazily as a generator.

### Example 3 — Find the median from a data stream (Hard)

**Problem.** Support `add_num` and `find_median` in O(log n) / O(1).

**Approach.** Split the numbers into two heaps: a max-heap for the lower half and a min-heap for the upper half (Python has no max-heap, so negate the values). Keep the lower half either equal in size or one larger. Then the median is the top of the bigger heap, or the average of both tops. Every insertion rebalances so the invariant `len(low) >= len(high)` and `max(low) <= min(high)` holds.

```python
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []        # lower half, max-heap via negation
        self.high = []       # upper half, min-heap

    def add_num(self, num):
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        # rebalance: low may hold at most one extra element
        if len(self.low) > len(self.high) + 1:
            heapq.heappush(self.high, -heapq.heappop(self.low))
        elif len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def find_median(self):
        if not self.low:
            return None
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        return float(-self.low[0])


if __name__ == "__main__":
    finder = MedianFinder()
    for num in (5, 2, 9, 1, 7):
        finder.add_num(num)
        print(f"added {num}: low(max-heap)={sorted(-x for x in finder.low)} "
              f"high={sorted(finder.high)} -> median {finder.find_median()}")
    print("empty finder:", MedianFinder().find_median())
```

Output:

```text
added 5: low(max-heap)=[5] high=[] -> median 5.0
added 2: low(max-heap)=[2] high=[5] -> median 3.5
added 9: low(max-heap)=[2, 5] high=[9] -> median 5.0
added 1: low(max-heap)=[1, 2] high=[5, 9] -> median 3.5
added 7: low(max-heap)=[1, 2, 5] high=[7, 9] -> median 5.0
empty finder: None
```

**Complexity.** O(log n) per insertion, O(1) for the median, O(n) space. The "two halves with a size invariant" idea also solves sliding-window median (add a lazy-deletion map) and running-percentile problems.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Restaurant Customers](https://cses.fi/problemset/task/1619) | CSES | Medium |
| [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | LeetCode | Hard |
| [IPO](https://leetcode.com/problems/ipo/) | LeetCode | Hard |
| [Jesse and Cookies](https://www.hackerrank.com/challenges/jesse-and-cookies/problem) | HackerRank | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain python without notes.
- [ ] Explain push/pop are o(log n); peek is o(1); heapify is o(n) without notes.
- [ ] Explain a min-heap of size k retains the k largest processed items without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
