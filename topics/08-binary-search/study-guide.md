# Binary Search: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Search for a boundary in a monotonic domain. Define what is true on each side, preserve that invariant, and choose a loop form whose termination and returned boundary are explicit.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Exact search returns a matching position or absence. |
| 2 | Lower bound finds the first value ≥ target; upper bound finds the first value > target. |
| 3 | Rotated arrays retain at least one sorted half. |
| 4 | Answer search turns optimization into a monotonic feasibility test. |
| 5 | Integer boundaries avoid floating precision when the answer is discrete. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Sorted lookup | Index binary search |
| Minimum feasible capacity/speed | First-true answer search |
| Maximum feasible value | Last-true answer search |
| Rotated sorted input | Identify sorted half |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For first true in `[False, False, True, True]`, maintain a half-open interval `[left, right)`. If `predicate(mid)` is true set `right = mid`; otherwise set `left = mid + 1`. At termination `left == right` is the first true index.

## Tricks and interview notes

- Write “first true” or “last true” before writing code.
- Use `mid = left + (right-left)//2` as a portable habit.
- Set answer-search bounds from minimum and maximum possible answers.
- Test arrays of size 0, 1, 2 and targets outside both ends.

## Common mistakes

- **Watch for:** Mixing inclusive and half-open updates.
- **Watch for:** Returning immediately on equality when the first occurrence is needed.
- **Watch for:** Using a non-monotonic predicate for answer search.
- **Watch for:** Not proving which rotated half is sorted.

## Implementation drills

1. Implement exact, lower-bound, and upper-bound variants.
2. Solve one minimum-feasible and one maximum-feasible problem.
3. Trace duplicate boundary cases by hand.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. The three templates

Almost every binary-search problem is one of these shapes. Learn to recognise
which one you are in before writing the loop.

```python
def find_exact(nums, target):
    """Template 1 — is it there? Returns the index or -1."""
    lo, hi = 0, len(nums) - 1                 # closed interval [lo, hi]
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def first_true(lo, hi, predicate):
    """Template 2 — smallest x in [lo, hi] where predicate(x) is True.

    Requires a monotone predicate: False...False, then True...True.
    """
    while lo < hi:
        mid = (lo + hi) // 2                  # floor: never picks hi
        if predicate(mid):
            hi = mid                          # mid might be the answer: keep it
        else:
            lo = mid + 1
    return lo                                 # lo == hi


def last_true(lo, hi, predicate):
    """Template 3 — largest x in [lo, hi] where predicate(x) is True."""
    while lo < hi:
        mid = (lo + hi + 1) // 2              # ceil: never picks lo
        if predicate(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9, 11]
    print("find_exact(7):", find_exact(nums, 7), "| find_exact(4):", find_exact(nums, 4))

    # First index whose value is at least 8: predicate = "nums[i] >= 8".
    print("first >= 8:", first_true(0, len(nums) - 1, lambda i: nums[i] >= 8))
    # Last index whose value is at most 8.
    print("last <= 8:", last_true(0, len(nums) - 1, lambda i: nums[i] <= 8))
    # Integer square root: largest x with x*x <= n.
    print("isqrt(10) via search:", last_true(0, 10, lambda x: x * x <= 10))
    print("isqrt(16) via search:", last_true(0, 16, lambda x: x * x <= 16))
```

Output:

```text
find_exact(7): 3 | find_exact(4): -1
first >= 8: 4
last <= 8: 3
isqrt(10) via search: 3
isqrt(16) via search: 4
```

**How it works**

- Template 1 uses `while lo <= hi` and a **closed** interval; templates 2 and 3 use `while lo < hi` and never test `mid` against the answer by equality — they converge on a boundary.
- In `first_true`, `mid` uses the floor, and on `True` we keep `mid` (`hi = mid`); on `False` we must move (`lo = mid + 1`). Getting these two lines wrong is what causes infinite loops.
- In `last_true`, `mid` uses the ceiling (`(lo + hi + 1) // 2`) and the branches mirror: `True` keeps `mid` via `lo = mid`, `False` uses `hi = mid − 1`.
- The predicate does not have to index an array: it can be any monotone test, which is what makes "binary search on the answer" possible.

### 2. Binary search on the answer

When the question asks for the minimum (or maximum) value that satisfies a
condition, search the **answer space** instead of the input. Two ingredients: the
feasibility check, and the monotonicity proof ("if capacity C works, any larger
capacity also works").

```python
def min_eating_speed(piles, hours):
    """Koko: minimum bananas/hour to finish all piles within `hours`."""
    def can_finish(speed):
        return sum((pile + speed - 1) // speed for pile in piles) <= hours

    return first_true(1, max(piles), can_finish)


def ship_within_days(weights, days):
    """Minimum ship capacity that delivers everything within `days`."""
    def can_ship(capacity):
        needed, load = 1, 0
        for weight in weights:
            if load + weight > capacity:      # would overflow: start a new day
                needed += 1
                load = 0
            load += weight
        return needed <= days

    return first_true(max(weights), sum(weights), can_ship)


def first_true(lo, hi, predicate):
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    for hours in (8, 5, 4):
        print(f"piles={piles}, hours={hours} -> speed {min_eating_speed(piles, hours)}")

    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for days in (5, 3, 1):
        print(f"weights 1..10, days={days} -> capacity {ship_within_days(weights, days)}")
```

Output:

```text
piles=[3, 6, 7, 11], hours=8 -> speed 4
piles=[3, 6, 7, 11], hours=5 -> speed 7
piles=[3, 6, 7, 11], hours=4 -> speed 11
weights 1..10, days=5 -> capacity 15
weights 1..10, days=3 -> capacity 21
weights 1..10, days=1 -> capacity 55
```

**How it works**

- Define `can_do(x)` first, make it O(n) and obviously monotone, and the search is four lines.
- The bounds matter: the smallest possible answer is the minimum feasible value (`max(piles)` — you must be able to lift the heaviest item in one go), and the largest is `sum(weights)` (everything in one trip). Tight bounds are free performance.
- `(pile + speed − 1) // speed` is the ceiling-division idiom for integers — how many hours one pile takes.

## Solved examples

### Example 1 — First and last position of a target (Medium)

**Problem.** In a sorted array, find the first and last index of `target`, or
`[-1, -1]` if absent.

**Approach.** Two boundary searches: the first index with `nums[i] >= target` (`lower_bound`), and the first index with `nums[i] > target` (`upper_bound`) minus one. If the lower bound is out of range or does not point at `target`, the value is absent — no separate existence check is needed.

```python
def search_range(nums, target):
    def lower_bound(value):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < value:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    last = lower_bound(target + 1) - 1        # works for floats too
    return [first, last]


if __name__ == "__main__":
    print(search_range([5, 7, 7, 8, 8, 10], 8))    # [3, 4]
    print(search_range([5, 7, 7, 8, 8, 10], 7))    # [1, 2]
    print(search_range([5, 7, 7, 8, 8, 10], 6))    # [-1, -1]
    print(search_range([1], 1))                    # [0, 0]
    print(search_range([], 1))                     # [-1, -1]
```

Output:

```text
[3, 4]
[1, 2]
[-1, -1]
[0, 0]
[-1, -1]
```

**Complexity.** O(log n) time, O(1) space — two searches instead of one linear scan. Note that `lower_bound(target + 1)` only works for integers; for floats use a separate `> target` predicate.

### Example 2 — Find the minimum in a rotated sorted array (Medium)

**Problem.** A sorted array was rotated; find its minimum in O(log n).

**Approach.** Compare `nums[mid]` with `nums[hi]`. If `nums[mid] > nums[hi]`, the rotation pivot — and therefore the minimum — lies strictly to the right of `mid`. Otherwise `nums[mid]` itself might be the minimum, so keep it in the interval (`hi = mid`). This is `first_true` with the predicate `nums[i] <= nums[hi]`.

```python
def find_min(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1            # minimum is to the right of mid
        else:
            hi = mid                # mid could be the minimum: keep it
    return nums[lo]


if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))       # 1
    print(find_min([4, 5, 6, 7, 0, 1, 2])) # 0
    print(find_min([11, 13, 15, 17]))      # 11 (not rotated)
    print(find_min([2, 1]))                # 1
    print(find_min([1]))                   # 1
```

Output:

```text
1
0
11
1
1
```

**Complexity.** O(log n) time, O(1) space. With duplicates the comparison is ambiguous; shrink with `hi -= 1` when `nums[mid] == nums[hi]`, which degrades to O(n) in the worst case.

### Example 3 — Aggressive cows / largest minimum distance (Medium)

**Problem.** Place `k` cows in `n` stalls so that the minimum distance between
any two cows is as large as possible.

**Approach.** Feasibility is monotone: if distance `d` fits `k` cows, then any smaller distance also fits. So binary-search the largest feasible `d` — template 3 (`last_true`). The greedy check places the first cow in the first stall and every next cow in the first stall at least `d` away; greedy is optimal here because taking the earliest possible stall never hurts later choices.

```python
def largest_minimum_distance(stalls, cows):
    stalls = sorted(stalls)

    def can_place(distance):
        placed, last = 1, stalls[0]
        for position in stalls[1:]:
            if position - last >= distance:
                placed += 1
                last = position
                if placed >= cows:
                    return True
        return placed >= cows

    lo, hi = 0, stalls[-1] - stalls[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2              # ceiling mid for last_true
        if can_place(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9]
    print(stalls, "with 3 cows ->", largest_minimum_distance(stalls, 3))
    print(stalls, "with 2 cows ->", largest_minimum_distance(stalls, 2))
    print([1, 2, 3], "with 2 cows ->", largest_minimum_distance([1, 2, 3], 2))
    print([1, 5], "with 2 cows ->", largest_minimum_distance([1, 5], 2))
```

Output:

```text
[1, 2, 4, 8, 9] with 3 cows -> 3
[1, 2, 4, 8, 9] with 2 cows -> 8
[1, 2, 3] with 2 cows -> 2
[1, 5] with 2 cows -> 4
```

**Complexity.** O(n log n) to sort plus O(n log(range)) for the search. This "maximise the minimum" shape also covers allocating pages to students, splitting arrays, and magnetic-force problems.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Maximum Median](https://codeforces.com/problemset/problem/1201/C) | Codeforces | Medium |
| [Factory Machines](https://cses.fi/problemset/task/1620) | CSES | Medium |
| [Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/) | LeetCode | Medium |
| [Aggressive Cows](https://www.spoj.com/problems/AGGRCOW/) | SPOJ | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain exact search returns a matching position or absence without notes.
- [ ] Explain lower bound finds the first value ≥ target; upper bound finds the first value > target without notes.
- [ ] Explain rotated arrays retain at least one sorted half without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
