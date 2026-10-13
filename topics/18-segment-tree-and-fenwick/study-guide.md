# Segment Tree and Fenwick Tree: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Precompute hierarchical aggregates so point updates and range queries touch only logarithmically many nodes. Choose the structure based on the algebra of the operation.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Fenwick trees store partial prefix aggregates via the lowbit decomposition. |
| 2 | Segment trees store aggregates for explicit intervals. |
| 3 | Point update/range query are O(log n) in both common forms. |
| 4 | Lazy propagation postpones range updates. |
| 5 | Coordinate compression maps sparse ordered values into dense indices. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Prefix sums + point updates | Fenwick tree |
| General associative range query | Segment tree |
| Range updates + queries | Lazy segment tree |
| Values up to 10^9 but only n used | Coordinate compression |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

A Fenwick prefix query repeatedly performs `i -= i & -i`, removing the least significant set-bit block. An update performs `i += i & -i`, visiting every stored range that contains the index.

## Tricks and interview notes

- Use 1-based internal Fenwick indices even if the public API is 0-based.
- Define segment merge identity: 0 for sum, infinity for min, etc.
- Compression preserves order, not numeric distance.
- Test non-power-of-two lengths.

## Common mistakes

- **Watch for:** Off-by-one errors converting range sum to `prefix(r)-prefix(l-1)`.
- **Watch for:** Using Fenwick for an operation without a suitable inverse when arbitrary ranges are needed.
- **Watch for:** Forgetting to push lazy tags before descending.
- **Watch for:** Allocating a tree too small; 4n is a safe recursive size.

## Implementation drills

1. Implement Fenwick point-add and range-sum.
2. Implement iterative segment tree.
3. Add lazy range addition and range sum.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Fenwick tree (Binary Indexed Tree)

A Fenwick tree answers prefix sums and point updates in O(log n) with about half
the code of a segment tree. Each position `i` stores the sum of a range whose
length is the lowest set bit of `i`. Moving to the parent is `i -= i & -i`;
moving to the next covered range is `i += i & -i`.

```python
class Fenwick:
    """0-indexed public API, 1-indexed internally. O(log n) add/prefix_sum."""

    def __init__(self, values):
        data = list(values)
        self.n = len(data)
        self.bit = [0] * (self.n + 1)
        for i, value in enumerate(data):
            self.add(i, value)                  # O(n log n) build

    @classmethod
    def from_values(cls, values):
        """O(n) build: seed the tree, then let each parent absorb its children."""
        data = list(values)
        tree = cls.__new__(cls)
        tree.n = len(data)
        tree.bit = [0] + data[:]                # shift to 1-based
        for i in range(1, tree.n + 1):
            parent = i + (i & -i)
            if parent <= tree.n:
                tree.bit[parent] += tree.bit[i]
        return tree

    def add(self, index, delta):
        """Add `delta` at `index` (point update)."""
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i                         # jump to the next covered range

    def prefix_sum(self, index):
        """Sum of values[0..index] inclusive (0 if index < 0)."""
        if index < 0:
            return 0
        i = min(index, self.n - 1) + 1
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i                         # drop the lowest set bit
        return total

    def range_sum(self, left, right):
        """Sum of values[left:right] (half-open)."""
        return self.prefix_sum(right - 1) - self.prefix_sum(left - 1)

    def lower_bound(self, target):
        """Smallest index whose cumulative sum is >= target (values must be >= 0)."""
        index = 0
        step = 1 << (self.n.bit_length() - 1)   # largest power of two <= n
        while step:
            nxt = index + step
            if nxt <= self.n and self.bit[nxt] < target:
                index = nxt
                target -= self.bit[nxt]
            step >>= 1
        return index                            # the position where target lands

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"Fenwick(size={self.n}, total={self.prefix_sum(self.n - 1) if self.n else 0})"


if __name__ == "__main__":
    values = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = Fenwick(values)
    fast = Fenwick.from_values(values)

    print("values:", values)
    print("prefix_sum(3):", tree.prefix_sum(3), "| expected:", sum(values[:4]))
    print("range_sum(2, 6):", tree.range_sum(2, 6), "| expected:", sum(values[2:6]))
    print("O(n) build agrees:", tree.range_sum(0, len(values)) == fast.range_sum(0, len(values)))

    tree.add(3, 6)                              # values[3] += 6
    print("after add(3, 6) -> range_sum(0, 4):", tree.range_sum(0, 4))

    counts = Fenwick([1, 0, 0, 1, 1])           # frequencies, for lower_bound
    print("lower_bound(2):", counts.lower_bound(2), "(first index reaching cumulative 2)")
    print("empty tree total:", Fenwick([]).prefix_sum(0))
```

Output:

```text
values: [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
prefix_sum(3): 7 | expected: 7
range_sum(2, 6): 9 | expected: 9
O(n) build agrees: True
after add(3, 6) -> range_sum(0, 4): 13
lower_bound(2): 3 (first index reaching cumulative 2)
empty tree total: 0
```

**How it works**

- `i & -i` isolates the lowest set bit, which is the size of the range stored at `i`. Addition climbs to the ranges that cover this index; the prefix walk strips the lowest bit and accumulates.
- Building by repeated `add` is O(n log n); `from_values` seeds the array and lets each parent absorb its children for a true O(n) build.
- `lower_bound` walks down the powers of two, greedily taking any jump that keeps the cumulative sum below the target. It only works for non-negative values — it is the "find the k-th one" primitive behind order statistics.
- Fenwick trees support anything with an **inverse** operation (sum, XOR, min is not invertible for updates). For range minima or arbitrary associative ops, use a segment tree.

### 2. Segment tree (iterative)

A segment tree stores sums over intervals in a heap-like array. It handles range
queries, point updates, and (with lazy propagation) range updates in O(log n),
and it works for **any** associative operation: sum, min, max, gcd, XOR.

```python
class SegmentTree:
    """Iterative segment tree: O(n) build, O(log n) query and point update."""

    def __init__(self, values, operation=sum, identity=0):
        self.n = len(values)
        self.op = operation
        self.identity = identity
        self.size = 1
        while self.size < self.n:               # next power of two
            self.size *= 2
        self.tree = [identity] * (2 * self.size)
        for i, value in enumerate(values):      # leaves
            self.tree[self.size + i] = value
        for i in range(self.size - 1, 0, -1):   # parents, bottom-up
            self.tree[i] = self.op([self.tree[2 * i], self.tree[2 * i + 1]])

    def update(self, index, value):
        """Set values[index] = value."""
        i = self.size + index
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = self.op([self.tree[2 * i], self.tree[2 * i + 1]])
            i //= 2

    def query(self, left, right):
        """Combine values[left:right] (half-open range)."""
        left += self.size
        right += self.size
        result_left = result_right = self.identity
        while left < right:
            if left & 1:                        # left border is a right child
                result_left = self.op([result_left, self.tree[left]])
                left += 1
            if right & 1:                       # right border is a right child
                right -= 1
                result_right = self.op([self.tree[right], result_right])
            left //= 2
            right //= 2
        return self.op([result_left, result_right])

    def value_at(self, index):
        return self.tree[self.size + index]

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"SegmentTree(size={self.n}, total={self.query(0, self.n) if self.n else self.identity})"


if __name__ == "__main__":
    values = [2, 1, 1, 3, 2, 3, 4, 5]
    tree = SegmentTree(values)
    print("values:", values)
    print("query(0, 8):", tree.query(0, 8), "| query(2, 6):", tree.query(2, 6))
    print("query(3, 4):", tree.query(3, 4), "| value_at(4):", tree.value_at(4))

    tree.update(3, 10)
    print("after update(3, 10) -> query(2, 6):", tree.query(2, 6))
    print("total:", tree.query(0, len(values)))

    mins = SegmentTree([5, 2, 8, 1, 9], operation=min, identity=float("inf"))
    print("min tree query(0, 3):", mins.query(0, 3), "| query(1, 5):", mins.query(1, 5))
    print("empty tree:", SegmentTree([], operation=min, identity=float("inf")).query(0, 0))
```

Output:

```text
values: [2, 1, 1, 3, 2, 3, 4, 5]
query(0, 8): 21 | query(2, 6): 9
query(3, 4): 3 | value_at(4): 2
after update(3, 10) -> query(2, 6): 16
total: 28
min tree query(0, 3): 2 | query(1, 5): 1
empty tree: inf
```

**How it works**

- Leaves live at `size + i`, and each internal node combines its two children. The next power of two keeps the tree complete, with unused leaves set to the identity element.
- `query` decomposes the range into O(log n) disjoint nodes, accumulating from both borders — order matters for non-commutative operations, which is why the left and right accumulators are kept apart.
- The iterative version avoids recursion entirely: no recursion-limit worries, and it is usually faster in Python than the recursive form.
- Swap `operation=min` / `max` / a custom function and the same code answers range-minimum and range-maximum queries.

## Solved examples

### Example 1 — Range sum query with updates (Medium)

**Problem.** Design a structure over an array supporting `update(index, value)`
and `sum_range(left, right)`.

**Approach.** Prefix sums give O(1) queries but O(n) updates; a plain array gives O(1) updates but O(n) queries. Both a Fenwick tree and a segment tree give O(log n) for each. Fenwick is shorter and faster by constant factors; the segment tree generalises to min/max/gcd.

```python
class Fenwick:
    def __init__(self, values):
        self.n = len(values)
        self.bit = [0] * (self.n + 1)
        for i, value in enumerate(values):
            self.add(i, value)

    def add(self, index, delta):
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, index):
        total = 0
        i = index + 1
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


class NumArray:
    """Fenwick-backed: update by delta, query by prefix difference."""

    def __init__(self, nums):
        self.data = list(nums)
        self.tree = Fenwick(nums)

    def update(self, index, value):
        delta = value - self.data[index]
        self.data[index] = value
        self.tree.add(index, delta)

    def sum_range(self, left, right):
        if not self.data:
            return 0
        return self.tree.prefix_sum(right) - self.tree.prefix_sum(left - 1)


class NumArraySegTree:
    """Segment-tree-backed version: same API, different internals."""

    def __init__(self, nums):
        self.n = len(nums)
        self.size = 1
        while self.size < max(self.n, 1):
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for i, value in enumerate(nums):
            self.tree[self.size + i] = value
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        i = self.size + index
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
            i //= 2

    def sum_range(self, left, right):
        left += self.size
        right += self.size + 1                 # inclusive right border
        total = 0
        while left < right:
            if left & 1:
                total += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                total += self.tree[right]
            left //= 2
            right //= 2
        return total


if __name__ == "__main__":
    nums = [1, 3, 5]
    a, b = NumArray(nums), NumArraySegTree(nums)
    print("sum_range(0, 2):", a.sum_range(0, 2), b.sum_range(0, 2))
    a.update(1, 2)
    b.update(1, 2)
    print("after update(1, 2) -> sum_range(0, 2):", a.sum_range(0, 2), b.sum_range(0, 2))
    print("single element:", a.sum_range(1, 1), b.sum_range(1, 1))
    print("empty array:", NumArray([]).sum_range(0, 0), NumArraySegTree([]).sum_range(0, 0))
```

Output:

```text
sum_range(0, 2): 9 9
after update(1, 2) -> sum_range(0, 2): 8 8
single element: 2 2
empty array: 0 0
```

**Complexity.** O(n) build (or O(n log n) with repeated adds), O(log n) per update and query, O(n) space. Note the bookkeeping: a Fenwick stores deltas, so `update` must apply `new − old`.

### Example 2 — Count of smaller numbers after self (Hard)

**Problem.** For each element, count how many elements to its **right** are
smaller.

**Approach.** Scan right to left, inserting values into a Fenwick tree of
frequencies over **compressed coordinates** (values can be large or negative, but
there are at most n distinct ones). The count of previously seen values strictly
smaller than `x` is the prefix sum up to `x − 1`, i.e. the Fenwick prefix at rank
`(x) − 1`. Merge sort also solves this in O(n log n); the Fenwick version is
shorter and extends to online variants.

```python
class Fenwick:
    def __init__(self, size):
        self.n = size
        self.bit = [0] * (size + 1)

    def add(self, index, delta):
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, index):
        total = 0
        i = index + 1
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total


def count_smaller(nums):
    """Compress values to ranks, then count with a Fenwick frequency table."""
    ranks = {value: i for i, value in enumerate(sorted(set(nums)))}
    tree = Fenwick(len(ranks))
    answer = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):      # right to left
        rank = ranks[nums[i]]
        answer[i] = tree.prefix_sum(rank - 1)   # strictly smaller ranks seen so far
        tree.add(rank, 1)
    return answer


if __name__ == "__main__":
    print("count_smaller([5, 2, 6, 1]):", count_smaller([5, 2, 6, 1]))
    print("count_smaller([-1, -1]):", count_smaller([-1, -1]))
    print("increasing:", count_smaller([1, 2, 3]))
    print("decreasing:", count_smaller([3, 2, 1]))
    print("single:", count_smaller([7]))
```

Output:

```text
count_smaller([5, 2, 6, 1]): [2, 1, 1, 0]
count_smaller([-1, -1]): [0, 0]
increasing: [0, 0, 0]
decreasing: [2, 1, 0]
single: [0]
```

**Complexity.** O(n log n) time (sorting for compression plus one Fenwick pass) and O(n) space. Coordinate compression is the standard bridge between "arbitrary values" and "array-index structures" — it is also how you use a Fenwick tree for negative numbers.

### Example 3 — Range add and range sum with lazy propagation (Hard)

**Problem.** Support "add `value` to every element in `[l, r]`" and "sum of
`[l, r]`" — both in O(log n).

**Approach.** A segment tree where a range update is applied to a node **only if
that node's segment is fully covered**; the update is then recorded in a `lazy`
array and pushed down to the children just before they are needed. This defers
work: a range touching O(log n) nodes costs O(log n), not O(range length).

```python
class LazySegmentTree:
    """Range add + range sum over [0, n-1]. Recursive, O(log n) per operation."""

    def __init__(self, values):
        self.n = len(values)
        self.tree = [0] * (4 * max(self.n, 1))
        self.lazy = [0] * (4 * max(self.n, 1))
        if self.n:
            self._build(1, 0, self.n - 1, list(values))

    def _build(self, node, left, right, values):
        if left == right:
            self.tree[node] = values[left]
            return
        mid = (left + right) // 2
        self._build(2 * node, left, mid, values)
        self._build(2 * node + 1, mid + 1, right, values)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def _apply(self, node, left, right, value):
        """Add `value` to every element of this node's segment."""
        self.tree[node] += value * (right - left + 1)
        self.lazy[node] += value                # children learn about it later

    def _push(self, node, left, right):
        """Propagate a pending update to the children, then clear it."""
        if self.lazy[node] == 0 or left == right:
            return
        mid = (left + right) // 2
        self._apply(2 * node, left, mid, self.lazy[node])
        self._apply(2 * node + 1, mid + 1, right, self.lazy[node])
        self.lazy[node] = 0

    def range_add(self, target_left, target_right, value):
        if self.n == 0:
            return
        self._add(1, 0, self.n - 1, target_left, target_right, value)

    def _add(self, node, left, right, target_left, target_right, value):
        if target_right < left or right < target_left:
            return                              # no overlap
        if target_left <= left and right <= target_right:
            self._apply(node, left, right, value)
            return
        self._push(node, left, right)
        mid = (left + right) // 2
        self._add(2 * node, left, mid, target_left, target_right, value)
        self._add(2 * node + 1, mid + 1, right, target_left, target_right, value)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def range_sum(self, target_left, target_right):
        if self.n == 0:
            return 0
        return self._sum(1, 0, self.n - 1, target_left, target_right)

    def _sum(self, node, left, right, target_left, target_right):
        if target_right < left or right < target_left:
            return 0
        if target_left <= left and right <= target_right:
            return self.tree[node]
        self._push(node, left, right)
        mid = (left + right) // 2
        return (self._sum(2 * node, left, mid, target_left, target_right)
                + self._sum(2 * node + 1, mid + 1, right, target_left, target_right))


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    tree = LazySegmentTree(values)
    print("values:", values)
    print("sum(0, 4):", tree.range_sum(0, 4))
    tree.range_add(1, 3, 10)                    # [1, 12, 13, 14, 5]
    print("after add 10 to [1, 3] -> sum(0, 4):", tree.range_sum(0, 4))
    print("sum(1, 3):", tree.range_sum(1, 3), "| sum(0, 1):", tree.range_sum(0, 1))
    tree.range_add(2, 2, -3)
    print("after add -3 to [2, 2] -> sum(2, 2):", tree.range_sum(2, 2))
    print("single element tree:", LazySegmentTree([5]).range_sum(0, 0))
    print("empty tree:", LazySegmentTree([]).range_sum(0, 0))
```

Output:

```text
values: [1, 2, 3, 4, 5]
sum(0, 4): 15
after add 10 to [1, 3] -> sum(0, 4): 45
sum(1, 3): 39 | sum(0, 1): 13
after add -3 to [2, 2] -> sum(2, 2): 10
single element tree: 5
empty tree: 0
```

**Complexity.** O(n) build, O(log n) per range add and range sum, O(n) space (a `4n` array is the safe size for the recursive layout). Two Fenwick trees can also do range-add/range-sum; lazy propagation is the version that generalises to min/max and to "set" instead of "add".

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Dynamic Range Sum Queries](https://cses.fi/problemset/task/1648) | CSES | Medium |
| [Hotel Queries](https://cses.fi/problemset/task/1143) | CSES | Medium |
| [List Removals](https://cses.fi/problemset/task/1749) | CSES | Medium |
| [Range Sum Query 2D Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain fenwick trees store partial prefix aggregates via the lowbit decomposition without notes.
- [ ] Explain segment trees store aggregates for explicit intervals without notes.
- [ ] Explain point update/range query are o(log n) in both common forms without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
