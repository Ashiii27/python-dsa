# Searching and Sorting: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Sorting creates order that enables greedy scans, binary search, two pointers, and divide-and-conquer counting. Know what each algorithm guarantees about time, stability, and memory.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Comparison sorting has an Ω(n log n) general lower bound. |
| 2 | Merge sort is stable and predictable O(n log n), using O(n) auxiliary space. |
| 3 | Quicksort is expected O(n log n), worst O(n²); partitioning powers quickselect. |
| 4 | Counting/bucket/radix methods exploit restricted keys. |
| 5 | Custom comparator problems compare concatenations or transformed keys. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need ordered sweep | Sort then scan |
| Need kth item only | Quickselect or heap |
| Small bounded key range | Counting/bucket sort |
| Count cross-order pairs | Merge-sort counting |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Merge `[2, 5]` and `[1, 3]`: choosing 1 before 2 contributes two inversions because both remaining left values exceed 1; choosing 3 before 5 contributes one. The merge simultaneously sorts and counts.

## Tricks and interview notes

- Ask whether input mutation is allowed before sorting in place.
- Python sort is stable, enabling multi-pass sorting.
- Use three-way partitioning when duplicate pivots are common.
- For largest-number ordering, compare `a+b` against `b+a`.

## Common mistakes

- **Watch for:** Claiming quickselect is worst-case O(n).
- **Watch for:** Forgetting key computation cost in sort complexity.
- **Watch for:** Using subtraction as a comparator where values may overflow in other languages.
- **Watch for:** Merging touching intervals without checking the problem definition.

## Implementation drills

1. Implement merge sort and prove its recurrence.
2. Implement Dutch national flag partition.
3. Count inversions while merging.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Searching: linear, binary, and the bound variants

Binary search halves the search space every step, so 1,000,000 items take ~20
comparisons instead of 1,000,000. The price: the input must be sorted (or the
answer space must be monotonic).

```python
from bisect import bisect_left, bisect_right, insort


def linear_search(nums, target):
    """Works on any sequence: O(n)."""
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1


def binary_search(nums, target):
    """Index of target in a sorted list, or -1. O(log n)."""
    lo, hi = 0, len(nums) - 1                  # inclusive bounds
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1                       # mid is excluded: +1, not mid
        else:
            hi = mid - 1
    return -1


def lower_bound(nums, target):
    """First index with nums[i] >= target (len(nums) if none)."""
    lo, hi = 0, len(nums)                      # hi is EXCLUSIVE here
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


def upper_bound(nums, target):
    """First index with nums[i] > target."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 5, 7, 9]
    print("nums:", nums)
    print("linear_search(7):", linear_search(nums, 7), "| missing:", linear_search(nums, 4))
    print("binary_search(7):", binary_search(nums, 7), "| missing:", binary_search(nums, 4))

    print("lower_bound(2):", lower_bound(nums, 2), "| upper_bound(2):", upper_bound(nums, 2))
    print("count of 2s:", upper_bound(nums, 2) - lower_bound(nums, 2))
    print("bisect agrees:", bisect_left(nums, 2), bisect_right(nums, 2))

    ordered = [1, 3, 5]
    insort(ordered, 4)                          # insert in sorted position
    print("after insort(4):", ordered)
    print("empty list:", binary_search([], 1), lower_bound([], 1))
```

Output:

```text
nums: [1, 2, 2, 2, 5, 7, 9]
linear_search(7): 5 | missing: -1
binary_search(7): 5 | missing: -1
lower_bound(2): 1 | upper_bound(2): 4
count of 2s: 3
bisect agrees: 1 4
after insort(4): [1, 3, 4, 5]
empty list: -1 0
```

**How it works**

- Two loop shapes, never mixed: `while lo <= hi` with `hi = len − 1` for "find exactly", and `while lo < hi` with `hi = len` for "find a boundary". Mixing them is the number one source of infinite loops.
- `mid = (lo + hi) // 2` is safe in Python (arbitrary-precision ints never overflow).
- `lower_bound` / `upper_bound` answer "how many are less than x", "where does x belong", and "first/last occurrence" — the two primitives behind most medium binary-search problems. `bisect_left` and `bisect_right` are the C implementations; use them in production code.

### 2. Sorting algorithms from scratch

Know the mechanics and the trade-offs: insertion sort is O(n²) but tiny and
stable; merge sort is O(n log n) and stable but needs O(n) memory; quicksort is
O(n log n) average, in-place, unstable; heap sort is O(n log n) worst case with
O(1) extra memory; counting sort is O(n + k) for small integer ranges.

```python
import heapq


def insertion_sort(values):
    """O(n^2) time, O(1) extra space, stable. Great for nearly sorted input."""
    a = list(values)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:        # shift the sorted prefix right
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(values):
    """O(n log n) time, O(n) extra space, stable."""
    if len(values) <= 1:
        return list(values)
    mid = len(values) // 2
    left, right = merge_sort(values[:mid]), merge_sort(values[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:             # <= keeps it stable
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(values):
    """O(n log n) average, O(n^2) worst, O(log n) average stack, not stable.
    Three-way partition: elements < pivot, == pivot, > pivot."""
    a = list(values)

    def sort(lo, hi):
        if lo >= hi:
            return
        pivot = a[(lo + hi) // 2]
        lt, i, gt = lo, lo, hi
        while i <= gt:
            if a[i] < pivot:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif a[i] > pivot:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
        sort(lo, lt - 1)
        sort(gt + 1, hi)

    sort(0, len(a) - 1)
    return a


def heap_sort(values):
    """O(n log n) worst case, O(1) extra space (heapq sorts in place)."""
    heap = list(values)
    heapq.heapify(heap)                     # O(n)
    return [heapq.heappop(heap) for _ in range(len(heap))]


def counting_sort(values, max_value=None):
    """O(n + k) for non-negative integers in a small range; stable."""
    if not values:
        return []
    max_value = max(values) if max_value is None else max_value
    counts = [0] * (max_value + 1)
    for value in values:
        counts[value] += 1
    ordered = []
    for value, how_many in enumerate(counts):
        ordered.extend([value] * how_many)
    return ordered


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("input:", data)
    print("insertion:", insertion_sort(data))
    print("merge    :", merge_sort(data))
    print("quick    :", quick_sort(data))
    print("heap     :", heap_sort(data))
    print("counting :", counting_sort(data))
    print("stability check (merge keeps equal order):",
          merge_sort([(1, "a"), (0, "b"), (1, "c")]))
    print("empty:", insertion_sort([]), merge_sort([]), quick_sort([]))
```

Output:

```text
input: [5, 2, 9, 1, 5, 6]
insertion: [1, 2, 5, 5, 6, 9]
merge    : [1, 2, 5, 5, 6, 9]
quick    : [1, 2, 5, 5, 6, 9]
heap     : [1, 2, 5, 5, 6, 9]
counting : [1, 2, 5, 5, 6, 9]
stability check (merge keeps equal order): [(0, 'b'), (1, 'a'), (1, 'c')]
empty: [] [] []
```

**How it works**

- `insertion_sort` builds a sorted prefix and inserts each new element by shifting. Quadratic, but with a tiny constant — it is what Python's `sorted` uses for very small runs (Timsort).
- `merge_sort`'s work happens in the merge; the recursion only splits. `<=` (not `<`) is what keeps it stable.
- `quick_sort` here uses a three-way partition, which makes arrays full of duplicates O(n) instead of O(n²) — the reason a naive two-way quicksort dies on `[5, 5, 5, 5]`.
- `counting_sort` is the reminder that comparison sorts are not always optimal: when the key range is small, counting beats any O(n log n) sort.

### 3. Sorting in real Python code

In interviews and production you call `sorted` / `list.sort`; the skill is in
the keys.

```python
from heapq import nlargest, nsmallest

records = [("alice", 30, 88), ("bob", 25, 95), ("carol", 30, 75)]

# Sort by score, highest first.
print("by score desc:", sorted(records, key=lambda r: -r[2]))

# Multi-key: age ascending, then score descending (negate numeric fields).
print("age asc, score desc:", sorted(records, key=lambda r: (r[1], -r[2])))

# Stability: equal keys keep their original order.
pairs = [("a", 1), ("b", 0), ("c", 1)]
print("stable:", sorted(pairs, key=lambda p: p[1]))

# Strings: default sort is by code point, so "Banana" precedes "apple".
words = ["Banana", "apple", "cherry"]
print("default:", sorted(words), "| casefold:", sorted(words, key=str.casefold))

# Top-k without sorting everything: O(n log k) instead of O(n log n).
nums = [5, 1, 9, 3, 7, 9]
print("nlargest(3):", nlargest(3, nums), "| nsmallest(2):", nsmallest(2, nums))

# Unique + sorted in one line.
print("unique sorted:", sorted(set([3, 1, 3, 2, 1])))

# In-place vs copy: list.sort() mutates and returns None, sorted() returns a list.
mutable = [3, 1, 2]
result = mutable.sort()
print("sort() returns:", result, "| list is now:", mutable)
```

Output:

```text
by score desc: [('bob', 25, 95), ('alice', 30, 88), ('carol', 30, 75)]
age asc, score desc: [('bob', 25, 95), ('alice', 30, 88), ('carol', 30, 75)]
stable: [('b', 0), ('a', 1), ('c', 1)]
default: ['Banana', 'apple', 'cherry'] | casefold: ['apple', 'Banana', 'cherry']
nlargest(3): [9, 9, 7] | nsmallest(2): [1, 3]
unique sorted: [1, 2, 3]
sort() returns: None | list is now: [1, 2, 3]
```

**How it works**

- Use `key=` rather than a comparator: `key` is called once per element (O(n) key computations) instead of O(n log n) comparisons.
- Negate numeric fields inside a tuple key for mixed ascending/descending orders; for non-numeric fields, sort twice (least important key first) or wrap with a custom class.
- `nlargest(k, ...)` / `nsmallest(k, ...)` avoid the full sort when k ≪ n — the same heap idea as the top-k pattern.

## Solved examples

### Example 1 — Search in a rotated sorted array (Medium)

**Problem.** A sorted array was rotated at an unknown pivot (for example
`[4, 5, 6, 7, 0, 1, 2]`). Find `target` in O(log n).

**Approach.** At each `mid`, one half of the range is guaranteed to be sorted. Compare `nums[lo]` with `nums[mid]` to find out which, then test whether `target` lies inside that sorted half's value range. If it does, search there; otherwise search the other half. The messy half is never wrong to discard, because we only ever discard based on a known-sorted interval.

```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:                     # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                         # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    print("find 0:", search_rotated(nums, 0), "| find 3:", search_rotated(nums, 3))
    print("find 4:", search_rotated(nums, 4), "| find 2:", search_rotated(nums, 2))
    print("not rotated:", search_rotated([1, 2, 3], 3))
    print("single element:", search_rotated([1], 0), search_rotated([1], 1))
    print("empty:", search_rotated([], 1))
```

Output:

```text
find 0: 4 | find 3: -1
find 4: 0 | find 2: 6
not rotated: 2
single element: -1 0
empty: -1
```

**Complexity.** O(log n) time, O(1) space. Duplicates break the `nums[lo] <= nums[mid]` test (it cannot tell which half is sorted); the fix is to shrink `lo` by one when `nums[lo] == nums[mid]`, which degrades to O(n) in the worst case.

### Example 2 — Kth largest element with quickselect (Medium)

**Problem.** Return the k-th largest element in O(n) average time.

**Approach.** Sort is O(n log n). Quickselect uses the partition idea from quicksort but recurses into only one side: partition around a pivot into `<`, `==`, `>` groups, then continue only in the group containing index `k`. Average O(n) because each step discards a constant fraction; worst case O(n²) with unlucky pivots (randomising the pivot makes that vanishingly unlikely).

```python
def quickselect(values, k):
    """Return the k-th smallest element (0-indexed)."""
    a = list(values)
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        pivot = a[(lo + hi) // 2]
        left, right, equal = [], [], 0
        for i in range(lo, hi + 1):
            if a[i] < pivot:
                left.append(a[i])
            elif a[i] > pivot:
                right.append(a[i])
            else:
                equal += 1
        # k is a global index, so compare it against the group boundaries
        # expressed in global terms: lo + size of the group.
        if k < lo + len(left):                        # answer is in the left group
            a[lo:lo + len(left)] = left
            hi = lo + len(left) - 1
        elif k < lo + len(left) + equal:              # inside the pivot group
            return pivot
        else:                                         # answer is in the right group
            a[lo + len(left) + equal:hi + 1] = right
            lo = lo + len(left) + equal
    return a[k]


def kth_largest(values, k):
    """k-th largest == (n-k)-th smallest."""
    return quickselect(values, len(values) - k)


if __name__ == "__main__":
    print("kth_largest([3, 2, 1, 5, 6, 4], 2):", kth_largest([3, 2, 1, 5, 6, 4], 2))
    print("kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4):",
          kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print("smallest:", quickselect([3, 1, 2], 0), "| largest:", kth_largest([3, 1, 2], 1))
    print("sorted check:", sorted([9, 4, 2, 7, 1])[2] == quickselect([9, 4, 2, 7, 1], 2))
```

Output:

```text
kth_largest([3, 2, 1, 5, 6, 4], 2): 5
kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4): 4
smallest: 1 | largest: 3
sorted check: True
```

**Complexity.** Average O(n) time and O(1) extra space with an in-place partition (this version allocates the three groups, so O(n) space per level but O(n) overall). For a guaranteed O(n) worst case use the median-of-medians pivot selection.

### Example 3 — Count inversions with merge sort (Hard)

**Problem.** Count the pairs `(i, j)` with `i < j` and `nums[i] > nums[j]` — a
measure of how far the array is from sorted.

**Approach.** Brute force is O(n²). Merge sort already compares elements across the two halves, so count while merging: when `left[i] > right[j]`, that `right[j]` is smaller than every remaining element of `left`, so it contributes `len(left) − i` inversions at once. Total inversions = left + right + split.

```python
def count_inversions(values):
    def sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, left_count = sort_and_count(arr[:mid])
        right, right_count = sort_and_count(arr[mid:])
        merged, i, j, split = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                split += len(left) - i          # right[j] beats everything left
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, left_count + right_count + split

    return sort_and_count(list(values))[1]


if __name__ == "__main__":
    print("inversions([2, 4, 1, 3, 5]):", count_inversions([2, 4, 1, 3, 5]))
    print("inversions([3, 2, 1]):", count_inversions([3, 2, 1]))
    print("inversions([1, 2, 3]):", count_inversions([1, 2, 3]))
    print("inversions([2, 2, 2]):", count_inversions([2, 2, 2]))
    print("empty:", count_inversions([]))
```

Output:

```text
inversions([2, 4, 1, 3, 5]): 3
inversions([3, 2, 1]): 3
inversions([1, 2, 3]): 0
inversions([2, 2, 2]): 0
empty: 0
```

**Complexity.** O(n log n) time and O(n) space. The key insight — count crossings during the merge rather than afterwards — is the same "use the algorithm's existing comparisons" trick behind counting smaller-elements-to-the-right.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Apartments](https://cses.fi/problemset/task/1084) | CSES | Medium |
| [Array Division](https://cses.fi/problemset/task/1085) | CSES | Medium |
| [H-Index](https://leetcode.com/problems/h-index/) | LeetCode | Medium |
| [Sort an Array](https://leetcode.com/problems/sort-an-array/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain comparison sorting has an ω(n log n) general lower bound without notes.
- [ ] Explain merge sort is stable and predictable o(n log n), using o(n) auxiliary space without notes.
- [ ] Explain quicksort is expected o(n log n), worst o(n²); partitioning powers quickselect without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
