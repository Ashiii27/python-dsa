# Arrays and Strings: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Think in indices, contiguous ranges, and information that can be updated when a boundary moves. Most optimizations replace repeated range work with a maintained state.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Two pointers discard impossible pairs from sorted or boundary-based searches. |
| 2 | Sliding windows maintain a valid contiguous range incrementally. |
| 3 | Prefix sums turn repeated range sums into subtraction. |
| 4 | Kadane stores the best subarray ending at the current index. |
| 5 | Difference arrays encode range updates at their boundaries. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Sorted pair/triplet search | Two pointers |
| Longest/shortest valid substring | Sliding window |
| Many range queries | Prefix sum |
| Best contiguous sum | Kadane |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For `nums = [1, -1, 2, 3]`, prefix sums are `[0, 1, 0, 2, 5]`. The sum of indices 1 through 3 is `prefix[4] - prefix[1] = 4`. Storing counts of earlier prefixes also counts target-sum subarrays even when values are negative.

## Tricks and interview notes

- Move each pointer only for a reason you can prove.
- Store last-seen indices to jump a window boundary instead of shrinking one step at a time.
- For in-place matrix rotation, transpose then reverse each row.
- Use sentinel prefix `0` to include ranges beginning at index zero.

## Common mistakes

- **Watch for:** Applying a sum-based sliding window when negative values destroy monotonicity.
- **Watch for:** Forgetting duplicate skipping in 3Sum.
- **Watch for:** Updating the answer before a window becomes valid.
- **Watch for:** Off-by-one mistakes in half-open ranges.

## Implementation drills

1. Write fixed and variable sliding-window templates.
2. Derive Kadane from “extend or restart.”
3. Rotate a matrix without allocating another matrix.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`. Full write-ups with proofs live in
[`problems/`](problems/README.md).

### 1. Prefix sums, difference arrays and Kadane

The three array tools that replace nested loops. Prefix sums answer "sum of a
range" in O(1); difference arrays apply range updates in O(1); Kadane finds the
best contiguous sum in one pass.

```python
def prefix_sums(nums):
    """prefix[i] = sum(nums[:i]), so prefix has len(nums) + 1 entries."""
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return prefix


def range_sum(prefix, left, right):
    """Sum of nums[left:right] (half-open) in O(1)."""
    return prefix[right] - prefix[left]


def difference_array(n, updates):
    """Apply (left, right, delta) range updates in O(1) each, then sweep once."""
    diff = [0] * (n + 1)                 # extra slot absorbs the closing -delta
    for left, right, delta in updates:
        diff[left] += delta
        diff[right + 1] -= delta
    result, running = [], 0
    for i in range(n):
        running += diff[i]
        result.append(running)
    return result


def kadane(nums):
    """Return (best sum, the subarray achieving it): extend the run or restart."""
    best = cur = nums[0]
    start = best_left = best_right = 0
    for i in range(1, len(nums)):
        if cur + nums[i] < nums[i]:       # restarting beats extending
            cur, start = nums[i], i
        else:
            cur += nums[i]
        if cur > best:
            best, best_left, best_right = cur, start, i
    return best, nums[best_left:best_right + 1]


if __name__ == "__main__":
    nums = [2, 1, 3, 4, 5]
    prefix = prefix_sums(nums)
    print("nums:", nums, "| prefix:", prefix)
    print("sum of nums[1:4]:", range_sum(prefix, 1, 4), "| total:", range_sum(prefix, 0, len(nums)))

    print("difference array:", difference_array(5, [(1, 3, 2), (2, 4, 1)]))

    print("kadane:", kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print("all negatives:", kadane([-5, -2, -9]))
    print("single element:", kadane([7]))
```

Output:

```text
nums: [2, 1, 3, 4, 5] | prefix: [0, 2, 3, 6, 10, 15]
sum of nums[1:4]: 8 | total: 15
difference array: [0, 2, 3, 3, 1]
kadane: (6, [4, -1, 2, 1])
all negatives: (-2, [-2])
single element: (7, [7])
```

**How it works**

- `prefix_sums` keeps a leading `0` so `range_sum(prefix, 0, r)` works — without the sentinel, ranges starting at index 0 need a special case.
- `difference_array` marks only the boundaries: `+delta` where the range starts, `−delta` just past where it ends. The final sweep accumulates them into the real values, so k updates cost O(n + k) instead of O(n · k).
- `kadane` keeps the best subarray **ending at** the current index. The only decision is extend (`cur + x`) or restart (`x`). Initialising from `nums[0]` (not 0) is what makes an all-negative array return the largest negative instead of 0.

### 2. Sliding windows

A window is a contiguous range `[left, right]` maintained incrementally. Fixed
size: add one element, drop one. Variable size: grow while valid, shrink while
invalid.

```python
from collections import Counter, defaultdict


def fixed_window_sums(nums, k):
    """Every k-sized window sum in O(n) instead of O(n*k)."""
    if k > len(nums):
        return []
    window = sum(nums[:k])
    sums = [window]
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]   # slide: add the new, drop the old
        sums.append(window)
    return sums


def longest_at_most_k_distinct(s, k):
    """Length of the longest substring with at most k distinct characters."""
    freq = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        freq[ch] += 1
        while len(freq) > k:              # shrink until valid again
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]         # delete, otherwise len(freq) never drops
            left += 1
        best = max(best, right - left + 1)
    return best


def min_window(s, t):
    """Shortest substring of s containing every character of t, with multiplicity."""
    need = Counter(t)                     # how many of each char we still require
    have = defaultdict(int)
    missing = len(t)                      # characters still needed overall
    best_left, best_right = 0, None
    left = 0
    for right, ch in enumerate(s):
        if have[ch] < need[ch]:
            missing -= 1
        have[ch] += 1
        while missing == 0:               # valid: record, then shrink to find smaller
            if best_right is None or right - left < best_right - best_left:
                best_left, best_right = left, right
            have[s[left]] -= 1
            if have[s[left]] < need[s[left]]:
                missing += 1
            left += 1
    return "" if best_right is None else s[best_left:best_right + 1]


if __name__ == "__main__":
    print("window sums k=3:", fixed_window_sums([1, 3, 2, 5, 7, 2], 3))
    print("longest with <=2 distinct:", longest_at_most_k_distinct("eceba", 2))
    print("longest with <=3 distinct:", longest_at_most_k_distinct("ccaabbb", 3))
    print("min window:", min_window("ADOBECODEBANC", "ABC"))
    print("no window possible:", repr(min_window("ABCDE", "XYZ")))
```

Output:

```text
window sums k=3: [6, 10, 14, 14]
longest with <=2 distinct: 3
longest with <=3 distinct: 7
min window: BANC
no window possible: ''
```

**How it works**

- `fixed_window_sums` recomputes nothing: each slide is one add and one subtraction, so k-sized windows cost O(n) total.
- The variable window has one invariant: after the inner `while`, `[left, right]` is valid. Grow with `right` in the outer loop, repair with `left` in the inner loop, and read the answer only when the window is valid.
- `missing` in `min_window` counts characters (not distinct keys), which is how multiplicity in `t` is respected. It is the standard "formed/missing" counter pattern.
- Deleting zero-count keys from `freq` is essential: otherwise `len(freq)` keeps counting characters that left the window.

### 3. Two pointers and in-place tricks

When both pointers only move forward, the scan is O(n) even though it looks like
two nested loops.

```python
def two_sum_sorted(nums, target):
    """Sorted input: shrink the window from both ends. O(n) time, O(1) space."""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:                # too small: the left side is exhausted
            left += 1
        else:                             # too big: the right side is exhausted
            right -= 1
    return []


def dedupe_sorted(nums):
    """Compact duplicates of a sorted array in place; return the new length."""
    if not nums:
        return 0
    write = 1                             # index 0 is always kept
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def reverse_words(sentence):
    """Reverse words without slicing tricks: reverse everything, then each word."""
    chars = list(sentence)
    chars.reverse()
    start = 0
    for i in range(len(chars) + 1):
        if i == len(chars) or chars[i] == " ":
            chars[start:i] = reversed(chars[start:i])
            start = i + 1
    return "".join(chars)


def rotate_matrix(matrix):
    """Rotate n x n by 90 degrees clockwise in place: transpose, then reverse rows."""
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):         # transpose across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix


if __name__ == "__main__":
    print("two_sum_sorted:", two_sum_sorted([1, 2, 3, 4, 6], 6))

    nums = [1, 1, 2, 2, 2, 3, 4]
    length = dedupe_sorted(nums)
    print("dedupe -> length:", length, "| kept:", nums[:length])

    print("reverse words:", repr(reverse_words("the sky is blue")))

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("rotated:", rotate_matrix(matrix))
```

Output:

```text
two_sum_sorted: [1, 3]
dedupe -> length: 4 | kept: [1, 2, 3, 4]
reverse words: 'blue is sky the'
rotated: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

**How it works**

- `two_sum_sorted` is correct because moving the pointer that can only make things worse is never wrong: if the sum is too small, `nums[left]` cannot pair with anything to the right of `right`.
- The read/write pointer pair in `dedupe_sorted` is the general shape of every "compact in place" problem: `read` scans, `write` only advances when something is kept.
- `rotate_matrix` transposes (swap `(i, j)` with `(j, i)` for `j > i` only, or you swap twice) and then reverses each row. No second matrix is allocated.

## Solved examples

### Example 1 — Trapping rain water (Hard)

**Problem.** Given bar heights, compute how much water the shape holds after raining.

**Approach.** The water above index `i` is `min(best height to the left, best height to the right) − height[i]`, clamped at zero. Computing those maxima with prefix/suffix arrays costs O(n) space; two pointers do it in O(1): maintain `left_max` and `right_max`, and always advance the side with the smaller maximum — that side's water is already determined by the smaller bound.

```python
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]      # right side is at least left_max
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # 6
    print(trap([4, 2, 0, 3, 2, 5]))                     # 9
    print("flat:", trap([3, 3, 3]), "| empty:", trap([]), "| two bars:", trap([1, 2]))
```

Output:

```text
6
9
flat: 0 | empty: 0 | two bars: 0
```

**Complexity.** O(n) time, O(1) extra space. The alternative is a monotonic stack (process water in horizontal layers); both are O(n), and the two-pointer version is the one with the cleanest proof.

### Example 2 — Range updates with a difference array (Medium)

**Problem.** (`Corporate Flight Bookings`) You have `n` flights and bookings
`(first, last, seats)`. Each booking reserves `seats` on every flight from
`first` to `last` inclusive. Return the total seats per flight.

**Approach.** Naively looping over every flight in every booking is O(n · k) and times out. Mark the boundaries instead: add `seats` at `first`, subtract it at `last + 1`, then prefix-sum once.

```python
def corp_flight_bookings(bookings, n):
    diff = [0] * (n + 2)                       # 1-indexed flights + closing slot
    for first, last, seats in bookings:
        diff[first] += seats
        diff[last + 1] -= seats
    total, running = [], 0
    for i in range(1, n + 1):
        running += diff[i]
        total.append(running)
    return total


if __name__ == "__main__":
    print(corp_flight_bookings([(1, 2, 10), (2, 3, 20), (2, 5, 25)], 5))
    print("single flight:", corp_flight_bookings([(1, 1, 7)], 1))
    print("no bookings:", corp_flight_bookings([], 3))
```

Output:

```text
[10, 55, 45, 25, 25]
single flight: [7]
no bookings: [0, 0, 0]
```

**Complexity.** O(n + k) time and O(n) space, versus O(n · k) for the obvious simulation. This is the same trick as prefix sums, read backwards: prefix sums answer range queries, difference arrays apply range updates.

### Example 3 — Sort colors / Dutch national flag (Medium)

**Problem.** Sort an array of 0s, 1s and 2s in place, in one pass, with O(1) space.

**Approach.** Three-way partition with three pointers: `low` is the boundary of the 0-zone, `high` the boundary of the 2-zone, and `i` scans the unknown middle. Swap 0s left and 2s right; 1s stay. The invariant is `[0, low)` are 0s, `[low, i)` are 1s, `(high, end]` are 2s.

```python
def sort_colors(nums):
    low = i = 0
    high = len(nums) - 1
    while i <= high:
        if nums[i] == 0:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1                      # do NOT advance i: the swapped-in value is unknown
        else:
            i += 1
    return nums


if __name__ == "__main__":
    print(sort_colors([2, 0, 2, 1, 1, 0]))
    print(sort_colors([2, 2, 2]))
    print(sort_colors([1]))
    print(sort_colors([]))
```

Output:

```text
[0, 0, 1, 1, 2, 2]
[2, 2, 2]
[1]
[]
```

**Complexity.** O(n) time (one pass, each element placed once) and O(1) extra space. The classic bug is advancing `i` after swapping with `high` — the value swapped in has not been examined yet.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Books](https://codeforces.com/problemset/problem/279/B) | Codeforces | Medium |
| [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | LeetCode | Easy |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | LeetCode | Hard |
| [Forest Queries](https://cses.fi/problemset/task/1652) | CSES | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain two pointers discard impossible pairs from sorted or boundary-based searches without notes.
- [ ] Explain sliding windows maintain a valid contiguous range incrementally without notes.
- [ ] Explain prefix sums turn repeated range sums into subtraction without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
