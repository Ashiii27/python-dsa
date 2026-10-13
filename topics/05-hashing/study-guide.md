# Hashing: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Trade memory for fast lookup by storing the exact historical fact a future step will ask about: membership, frequency, earliest index, or canonical group key.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Sets answer existence; maps associate values with counts, indices, or objects. |
| 2 | Canonical keys turn equivalence relations into grouping problems. |
| 3 | Prefix-state maps count or locate earlier matching states. |
| 4 | A list plus index map supports average O(1) random-set operations. |
| 5 | Hash quality affects worst-case behavior, though Python handles ordinary inputs well. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need complement | Value-to-index map |
| Count occurrences | Frequency map |
| Group equivalent objects | Canonical key |
| Longest unique run | Set of values |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

In Two Sum, before reading index `i`, the map contains earlier value → index pairs. Check `target - nums[i]` first, then insert `nums[i]`; this guarantees distinct indices and returns in one pass.

## Tricks and interview notes

- Choose map values deliberately: count, latest index, earliest index, or full list.
- For lowercase anagrams, a 26-count tuple avoids sorting each word.
- Start a consecutive-sequence scan only when `x-1` is absent.
- Use immutable tuple/frozenset keys for composite state.

## Common mistakes

- **Watch for:** Overwriting an earliest index when longest length depends on it.
- **Watch for:** Using unhashable lists as keys.
- **Watch for:** Assuming iteration order is sorted order.
- **Watch for:** Forgetting frequency rather than simple membership when duplicates matter.

## Implementation drills

1. Group anagrams with two key strategies.
2. Implement RandomizedSet.
3. Count subarrays with a given prefix-state relation.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Build a hash map from scratch

A hash map turns a key into a bucket index with a hash function, then stores the
pair there. Collisions (two keys landing in the same bucket) are handled here by
**separate chaining**: each bucket is a list. When the load factor grows, the
table doubles in size and rehashes, which keeps lookups O(1) on average.

```python
class HashTable:
    """Hash map with separate chaining and automatic resizing."""

    def __init__(self, capacity=8, max_load=0.75):
        self.capacity = capacity
        self.max_load = max_load
        self.buckets = [[] for _ in range(capacity)]
        self.size = 0

    # -- internals ------------------------------------------------------
    def _index(self, key):
        return hash(key) % self.capacity

    def _resize(self, capacity):
        """Rehash every pair into a fresh, larger bucket array."""
        old_buckets = self.buckets
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]
        for bucket in old_buckets:
            for key, value in bucket:
                self.buckets[self._index(key)].append((key, value))

    def longest_chain(self):
        """Diagnostic: the worst-case lookup cost if hashing were unlucky."""
        return max(len(bucket) for bucket in self.buckets)

    # -- public API -----------------------------------------------------
    def put(self, key, value):
        index = self._index(key)
        bucket = self.buckets[index]
        for i, (existing, _) in enumerate(bucket):
            if existing == key:                     # update in place
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > self.max_load:
            self._resize(self.capacity * 2)

    def get(self, key, default=None):
        for existing, value in self.buckets[self._index(key)]:
            if existing == key:
                return value
        return default

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (existing, _) in enumerate(bucket):
            if existing == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def items(self):
        for bucket in self.buckets:
            yield from bucket

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return any(existing == key for existing, _ in self.buckets[self._index(key)])

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        sentinel = object()
        value = self.get(key, sentinel)
        if value is sentinel:
            raise KeyError(key)
        return value

    def __repr__(self):
        return "{" + ", ".join(f"{k!r}: {v!r}" for k, v in self.items()) + "}"


if __name__ == "__main__":
    table = HashTable(capacity=4)
    for i in range(6):
        table[i] = i * i
    print("6 inserts:", table, "| len:", len(table), "| capacity:", table.capacity)

    print("get(3):", table.get(3), "| get(99):", table.get(99, "missing"), "| 4 in table:", 4 in table)

    table[3] = 99                                  # same key -> update, not insert
    print("after update:", table[3], "| len still:", len(table))

    print("remove(3):", table.remove(3), "-> len:", len(table),
          "| remove again:", table.remove(3))

    # Forced collisions: with capacity 8 these four keys share bucket 0.
    collisions = HashTable(capacity=8)
    for key in (0, 8, 16, 24):
        collisions[key] = key
    print("longest chain with colliding keys:", collisions.longest_chain(),
          "| lookups still correct:", [collisions[k] for k in (0, 8, 16, 24)])

    words = HashTable()
    for word in ("apple", "banana", "cherry"):
        words[word] = len(word)
    print("word lengths:", words["apple"], words["banana"], words["cherry"],
          "| len:", len(words))
```

Output:

```text
6 inserts: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} | len: 6 | capacity: 8
get(3): 9 | get(99): missing | 4 in table: True
after update: 99 | len still: 6
remove(3): True -> len: 5 | remove again: False
longest chain with colliding keys: 4 | lookups still correct: [0, 8, 16, 24]
word lengths: 5 6 6 | len: 3
```

**How it works**

1. `_index` compresses any hash into `0 … capacity − 1` with a modulo. That compression is the source of collisions, not a bug.
2. Chaining stores a list per bucket, so a collision costs one extra equality comparison instead of a failure. `put` scans the bucket first: an existing key must be updated, not duplicated.
3. Resizing at load factor 0.75 keeps chains short. It costs O(n) but happens so rarely (doubling) that the **amortised** cost of `put` stays O(1) — the same argument as dynamic-array growth.
4. `longest_chain` is the number to watch: if it grows, lookups degrade from O(1) to O(n). Every element lands in one bucket only if the hash function is broken.
5. `get` compares with `==` after the hash matches, which is why keys must implement both `__hash__` and `__eq__` consistently.

### 2. Python's hashing toolkit in practice

You will almost always use `dict` and `set` instead of the class above. What
matters is knowing the idioms, what is hashable, and how to build composite keys.

```python
from collections import Counter, defaultdict
from dataclasses import dataclass

nums = [4, 1, 2, 1, 3, 2]

# 1. Frequency map: Counter, or a plain dict with get.
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
print("frequency:", freq, "| Counter agrees:", dict(Counter(nums)))

# 2. Value -> index map (the two-sum shape).
index_of = {x: i for i, x in enumerate(nums)}     # later duplicates win
print("index_of:", index_of)

# 3. Membership tests: use a set, never a list, inside a loop.
seen = {1, 2, 3}
print("membership:", 2 in seen, "| list scan would be O(n)")

# 4. Grouping with defaultdict.
by_parity = defaultdict(list)
for x in nums:
    by_parity[x % 2].append(x)
print("grouped by parity:", dict(by_parity))

# 5. Composite keys: tuples and strings stand in for "combination" keys.
grid_keys = [(r, c) for r in range(2) for c in range(2)]
print("tuple keys:", grid_keys)
row_key = "r=1"
col_key = "c=2"
print("string key:", f"{row_key},{col_key}")

# 6. Hashability: mutable containers are unhashable, so freeze them.
try:
    {[1, 2]: "nope"}
except TypeError as exc:
    print("list as key ->", exc)
print("tuple works:", {(1, 2): "ok"})
print("frozenset works:", {frozenset({1, 2}): "ok"})

# 7. Custom objects: define __hash__ and __eq__ together (frozen dataclass does it).
@dataclass(frozen=True)
class Point:
    x: int
    y: int

points = {Point(1, 2), Point(3, 4), Point(1, 2)}
print("equal points dedupe:", len(points), "| hashes match:",
      hash(Point(1, 2)) == hash(Point(1, 2)))

# 8. dict preserves insertion order, which is often the answer's order.
print("keys in insertion order:", list(freq))
```

Output:

```text
frequency: {4: 1, 1: 2, 2: 2, 3: 1} | Counter agrees: {4: 1, 1: 2, 2: 2, 3: 1}
index_of: {4: 0, 1: 3, 2: 5, 3: 4}
membership: True | list scan would be O(n)
grouped by parity: {0: [4, 2, 2], 1: [1, 1, 3]}
tuple keys: [(0, 0), (0, 1), (1, 0), (1, 1)]
string key: r=1,c=2
list as key -> unhashable type: 'list'
tuple works: {(1, 2): 'ok'}
frozenset works: {frozenset({1, 2}): 'ok'}
equal points dedupe: 2 | hashes match: True
keys in insertion order: [4, 1, 2, 3]
```

**How it works**

- `dict.get(key, default)` and `collections.defaultdict` remove the `if key in d` branch; pick `defaultdict` when you want the key inserted, `.get` when you do not.
- A key must be **hashable and immutable while stored**: use `tuple` instead of `list`, `frozenset` instead of `set`. For custom classes, define `__eq__` and `__hash__` together (or use `@dataclass(frozen=True)`), because Python sets `__hash__ = None` as soon as you define `__eq__`.
- Composite keys are how you turn "two things identify this item" into one dict lookup: `(row, col)`, `f"{row}#{col}"`, or `tuple(sorted(pair))` for order-independent pairs.
- `dict` and `set` operations are O(1) **average**, not worst case. In an interview, saying "average O(1), worst case O(n) with adversarial collisions" is the precise answer.

## Solved examples

### Example 1 — Two sum (Easy)

**Problem.** Return the indices of two numbers that add up to `target`.

**Approach.** Brute force tests every pair: O(n²). Instead walk once and store `value -> index`; before inserting `x`, check whether `target − x` is already stored. Because we look backwards, the complement is always to the left, so each pair is found exactly once and no index can pair with itself.

```python
def two_sum(nums, target):
    seen = {}                                  # value -> index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i                            # insert AFTER the check
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))          # [0, 1]
    print(two_sum([3, 3], 6))                  # [0, 1] (same value twice)
    print(two_sum([3, 2, 4], 6))               # [1, 2]
    print("no answer:", two_sum([1, 2], 10))
```

Output:

```text
[0, 1]
[0, 1]
[1, 2]
no answer: []
```

**Complexity.** O(n) time and O(n) space, down from O(n²) time and O(1) space. Inserting after the check is what makes `[3, 3] -> [0, 1]` work.

### Example 2 — Longest consecutive sequence (Medium)

**Problem.** Given unsorted integers, return the length of the longest run of
consecutive numbers. Required: O(n).

**Approach.** Sorting would be O(n log n). Put the numbers in a set, then only start counting from a number whose predecessor is absent — a true sequence start. Each number is then visited at most twice (once as a candidate, once inside a scan), so the total is O(n).

```python
def longest_consecutive(nums):
    values = set(nums)
    best = 0
    for x in values:
        if x - 1 in values:                    # not the start of a sequence
            continue
        length = 1
        while x + length in values:
            length += 1
        best = max(best, length)
    return best


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))     # 4  -> 1,2,3,4
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
    print("duplicates ignored:", longest_consecutive([1, 1, 1]))
    print("empty:", longest_consecutive([]))
```

Output:

```text
4
9
duplicates ignored: 1
empty: 0
```

**Complexity.** O(n) time, O(n) space. The `if x − 1 in values` guard is the whole optimisation: without it, the inner `while` would re-scan the same run from every starting point and the solution would be O(n²).

### Example 3 — Valid Sudoku (Medium)

**Problem.** Decide whether a partially filled 9×9 board is valid: no repeated
digit in any row, column, or 3×3 box.

**Approach.** One pass, one set of composite keys. For each filled cell with digit `d`, build three keys — `("row", r, d)`, `("col", c, d)`, `("box", r // 3, c // 3, d)` — and fail if any was already seen. This is the composite-key pattern: the key encodes the constraint, so three separate checks collapse into one set.

```python
def is_valid_sudoku(board):
    seen = set()
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == ".":
                continue
            keys = (
                ("row", r, cell),
                ("col", c, cell),
                ("box", r // 3, c // 3, cell),
            )
            for key in keys:
                if key in seen:
                    return False
                seen.add(key)
    return True


if __name__ == "__main__":
    valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print("valid board:", is_valid_sudoku(valid))

    invalid = [row[:] for row in valid]
    invalid[0][2] = "5"                        # duplicate 5 in the first row
    print("after duplicating a 5 in row 0:", is_valid_sudoku(invalid))
```

Output:

```text
valid board: True
after duplicating a 5 in row 0: False
```

**Complexity.** O(81) = O(1) for a fixed board, conceptually O(cells) time and space. The same "encode the constraint in the key" trick solves isomorphic-strings, word-patterns, and grouping problems.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Ransom Note](https://leetcode.com/problems/ransom-note/) | LeetCode | Easy |
| [Four Sum II](https://leetcode.com/problems/4sum-ii/) | LeetCode | Medium |
| [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | LeetCode | Medium |
| [C. Registration System](https://codeforces.com/problemset/problem/4/C) | Codeforces | Easy |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain sets answer existence; maps associate values with counts, indices, or objects without notes.
- [ ] Explain canonical keys turn equivalence relations into grouping problems without notes.
- [ ] Explain prefix-state maps count or locate earlier matching states without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
