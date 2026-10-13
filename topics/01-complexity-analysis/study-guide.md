# Complexity Analysis: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Count how the dominant operation grows with input size. Analyze loops by total pointer movement, recursion by states and branching, and containers by their documented operation costs.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Big-O is an upper bound; Theta is a tight asymptotic bound. |
| 2 | Sequential phases add; independent nested phases multiply. |
| 3 | Amortized analysis spreads occasional expensive operations across a sequence. |
| 4 | Recursion space depends on maximum active depth, not total calls. |
| 5 | Output-sensitive algorithms must include the size of the produced answer. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Input repeatedly halves | O(log n) |
| Two monotonic pointers | Usually O(n), not O(n²) |
| Sorting dominates a scan | O(n log n) |
| States × transitions | Typical DP complexity |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For `i = 1, 2, 4, ... < n`, the loop executes `ceil(log2 n)` times. If each iteration scans all `n` values, total time is O(n log n). Two syntactically nested loops are not automatically O(n²): if an inner pointer never resets, total movement can still be O(n).

## Tricks and interview notes

- State what `n`, `V`, `E`, or `k` means before giving a bound.
- For hash tables, say “O(1) average” when precision matters.
- Include sorting, recursion stack, copied slices, and output storage.
- Use constraints to reject approaches before coding.

## Common mistakes

- **Watch for:** Multiplying loop bounds without checking dependencies.
- **Watch for:** Calling an algorithm O(n) while using O(n) slicing inside each iteration.
- **Watch for:** Ignoring a dense graph where E can be V².
- **Watch for:** Claiming memoization is O(n) without counting transition work.

## Implementation drills

1. Analyze a two-pointer loop using aggregate movement.
2. Draw the recursion tree for naive Fibonacci.
3. Compare adjacency matrix and list costs.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Count operations instead of guessing

The most reliable way to check a complexity claim is to count the inner-loop
iterations for several input sizes and compare the counts against your formula.

```python
def single_loop(n):
    ops = 0
    for _ in range(n):
        ops += 1
    return ops


def triangular(n):
    """for i in range(n): for j in range(i, n) -> n(n+1)/2, i.e. O(n^2)."""
    ops = 0
    for i in range(n):
        for j in range(i, n):
            ops += 1
    return ops


def halving(n):
    """while n > 1: n //= 2 -> floor(log2 n) + 1, i.e. O(log n)."""
    ops = 0
    while n > 1:
        n //= 2
        ops += 1
    return ops


def doubling_inner(n):
    """for i in range(n): inner loop doubles -> O(n log n)."""
    ops = 0
    for _ in range(n):
        j = 1
        while j < n:
            j *= 2
            ops += 1
    return ops


if __name__ == "__main__":
    print(f"{'n':>6} {'O(n)':>8} {'O(n^2)':>10} {'O(log n)':>9} {'O(n log n)':>11}")
    for n in (10, 100, 1_000):
        print(f"{n:>6} {single_loop(n):>8} {triangular(n):>10} "
              f"{halving(n):>9} {doubling_inner(n):>11}")

    n = 1_000
    assert triangular(n) == n * (n + 1) // 2        # exact formula
    assert halving(n) == n.bit_length() - 1
    print("formulas verified for n =", n)
```

Output:

```text
     n     O(n)     O(n^2)  O(log n)  O(n log n)
    10       10         55         3          40
   100      100       5050         6         700
  1000     1000     500500         9       10000
formulas verified for n = 1000
```

**How it works**

- `triangular` counts `n + (n−1) + … + 1 = n(n+1)/2` steps: still O(n²), just with a smaller constant than a full square.
- `halving` divides by 2 each step; the number of steps is the number of bits of `n`, i.e. `n.bit_length() − 1`.
- `doubling_inner` runs `⌈log₂ n⌉` inner steps for each of the `n` outer steps, giving O(n log n) — the shape of merge sort, heap sort, and "for each element, binary search".

### 2. Growth rates side by side

Constants and hardware change; growth rates do not. This table is the one to
memorise.

```python
import math

NS = [10, 100, 1_000, 10_000, 100_000, 1_000_000]


def cell(value):
    return "too large" if value > 10 ** 18 else f"{value:,.0f}"


if __name__ == "__main__":
    print(f"{'n':>10} | {'log2 n':>7} | {'n':>10} | {'n log2 n':>12} | {'n^2':>14} | {'2^n':>10}")
    print("-" * 78)
    for n in NS:
        log_n = math.log2(n)
        n_log_n = n * log_n
        n_sq = n * n
        pow2 = 2 ** n if n <= 64 else float("inf")
        print(f"{n:>10,} | {log_n:>7.1f} | {cell(n):>10} | {cell(n_log_n):>12} | "
              f"{cell(n_sq):>14} | {cell(pow2):>10}")
```

Output:

```text
         n |  log2 n |          n |     n log2 n |            n^2 |        2^n
------------------------------------------------------------------------------
        10 |     3.3 |         10 |           33 |            100 |      1,024
       100 |     6.6 |        100 |          664 |         10,000 |  too large
     1,000 |    10.0 |      1,000 |        9,966 |      1,000,000 |  too large
    10,000 |    13.3 |     10,000 |      132,877 |    100,000,000 |  too large
   100,000 |    16.6 |    100,000 |    1,660,964 | 10,000,000,000 |  too large
 1,000,000 |    19.9 |  1,000,000 |   19,931,569 | 1,000,000,000,000 |  too large
```

**How it works**

- The gap between columns is what matters: at n = 1,000,000 an O(n log n) algorithm does ~20 million steps while an O(n²) one does a trillion.
- `2^n` explodes past any budget after about n = 60, which is why exponential brute force only survives with pruning (backtracking with strong constraints) or tiny n.

### 3. Amortised cost: dynamic arrays

`list.append` is **amortised** O(1): most appends are O(1), but when the
capacity is full the array doubles and every element is copied. Total copying
stays under 2n, so n appends cost O(n) in total.

```python
def simulate_appends(n):
    """Model a doubling array; return (element copies, final capacity)."""
    capacity, size, copies, resizes = 1, 0, 0, 0
    history = []
    for _ in range(n):
        if size == capacity:                 # full: allocate 2x and copy
            copies += size
            capacity *= 2
            resizes += 1
            history.append((size, capacity))
        size += 1
    return copies, capacity, resizes, history[:4]


if __name__ == "__main__":
    for n in (10, 100, 1_000, 10_000):
        copies, capacity, resizes, first = simulate_appends(n)
        print(f"n={n:>6}: copies={copies:>7}  (< 2n = {2 * n:>7})  "
              f"capacity={capacity:>7}  resizes={resizes}")
    print("first few resizes (size at resize -> new capacity):",
          simulate_appends(100)[3])
    print("total copies for n=10_000 is under 2n:",
          simulate_appends(10_000)[0] < 2 * 10_000)
```

Output:

```text
n=    10: copies=     15  (< 2n =      20)  capacity=     16  resizes=4
n=   100: copies=    127  (< 2n =     200)  capacity=    128  resizes=7
n=  1000: copies=   1023  (< 2n =    2000)  capacity=   1024  resizes=10
n= 10000: copies=  16383  (< 2n =   20000)  capacity=  16384  resizes=14
first few resizes (size at resize -> new capacity): [(1, 2), (2, 4), (4, 8), (8, 16)]
total copies for n=10_000 is under 2n: True
```

**How it works**

- Resizes happen at sizes 1, 2, 4, 8, … so the copies sum to `1 + 2 + 4 + … + n/2 < n`. The total work for n appends is therefore O(n) — the amortised cost per append is O(1).
- The same argument explains `dict` and `set` growth, and why `list.pop()` from the end is O(1) while `pop(0)` is O(n) (it shifts everything).

### 4. Choosing an algorithm from the constraints

Work backwards from the limits. A rough Python budget is ~10⁷ simple operations
per second; estimate the step count before you write the solution.

```python
import math

BUDGET = 10 ** 7          # rough ops for ~1 second of Python
COSTS = {
    "O(log n)": lambda n: math.log2(n),
    "O(n)": lambda n: n,
    "O(n log n)": lambda n: n * math.log2(n),
    "O(n^2)": lambda n: n * n,
}


def verdict(n, label):
    ops = COSTS[label](n)
    return ops, "fits" if ops <= BUDGET else "too slow"


if __name__ == "__main__":
    for n in (1_000, 100_000, 1_000_000):
        print(f"\nn = {n:,}")
        for label in COSTS:
            ops, call = verdict(n, label)
            shown = "too large" if ops > 10 ** 18 else f"{ops:,.0f}"
            print(f"  {label:<10} {shown:>18} ops -> {call}")
```

Output:

```text

n = 1,000
  O(log n)                   10 ops -> fits
  O(n)                    1,000 ops -> fits
  O(n log n)              9,966 ops -> fits
  O(n^2)              1,000,000 ops -> fits

n = 100,000
  O(log n)                   17 ops -> fits
  O(n)                  100,000 ops -> fits
  O(n log n)          1,660,964 ops -> fits
  O(n^2)         10,000,000,000 ops -> too slow

n = 1,000,000
  O(log n)                   20 ops -> fits
  O(n)                1,000,000 ops -> fits
  O(n log n)         19,931,569 ops -> too slow
  O(n^2)      1,000,000,000,000 ops -> too slow
```

**How it works**

- Read the constraint first: n ≤ 2·10⁵ usually means "O(n log n) or better"; n ≤ 20 means exponential backtracking is fine; n ≤ 10⁷ means O(n) and a tight constant.
- Space matters too: a `dp` table of 10⁶ × 10⁶ is impossible no matter how fast the algorithm is.

## Solved examples

### Example 1 — Contains duplicate: O(n²) vs O(n) (Easy)

**Problem.** Return `True` if any value appears at least twice.

**Approach.** Brute force compares every pair: O(n²). Hashing keeps a `set` of what we have already seen: one pass, O(n) expected. We count comparisons to show the difference concretely.

```python
def contains_duplicate_brute(nums):
    comparisons = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            comparisons += 1
            if nums[i] == nums[j]:
                return True, comparisons
    return False, comparisons


def contains_duplicate_set(nums):
    seen = set()
    comparisons = 0
    for x in nums:
        comparisons += 1                 # one hash lookup
        if x in seen:
            return True, comparisons
        seen.add(x)
    return False, comparisons


if __name__ == "__main__":
    nums = list(range(2_000)) + [7]      # duplicate sits near the end
    print("brute:", contains_duplicate_brute(nums))
    print("set  :", contains_duplicate_set(nums))

    small = [1, 2, 3, 1]
    print("no-duplicate case:", contains_duplicate_brute([1, 2, 3]),
          contains_duplicate_set([1, 2, 3]))
    print("empty:", contains_duplicate_set([]))
    assert contains_duplicate_brute(small)[0] == contains_duplicate_set(small)[0] is True
```

Output:

```text
brute: (True, 15972)
set  : (True, 2001)
no-duplicate case: (False, 3) (False, 3)
empty: (False, 0)
```

**Complexity.** Brute force is O(n²) time, O(1) space. The set version is O(n) expected time and O(n) space. Both exit early on the first duplicate, but only the hash version is viable at n = 10⁵.

### Example 2 — Two sum: the hash-map trade (Easy)

**Problem.** Return indices of two numbers adding up to a target.

**Approach.** Brute force tests all pairs: O(n²). Instead, walk once and store `value -> index` in a dict; for each `x` check whether `target − x` was already seen. One pass, O(n). The space is the price you pay for the speed — this "space for time" trade is the central move of complexity analysis.

```python
def two_sum_brute(nums, target):
    steps = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            steps += 1
            if nums[i] + nums[j] == target:
                return [i, j], steps
    return None, steps


def two_sum_hash(nums, target):
    seen = {}
    steps = 0
    for i, x in enumerate(nums):
        steps += 1
        if target - x in seen:
            return [seen[target - x], i], steps
        seen[x] = i
    return None, steps


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
    print("brute:", two_sum_brute(nums, target))
    print("hash :", two_sum_hash(nums, target))

    big = list(range(5_000))
    target = 4_998 + 4_999                     # answer sits at the very end
    print("worst case, n = 5,000:")
    print("  hash :", two_sum_hash(big, target)[1], "steps")
    print("  brute: ~", len(big) * (len(big) - 1) // 2,
          "steps (predicted n(n-1)/2 — far too slow to run in Python)")
    print("no answer:", two_sum_hash([1, 2], 10))
```

Output:

```text
brute: ([0, 1], 1)
hash : ([0, 1], 2)
worst case, n = 5,000:
  hash : 5000 steps
  brute: ~ 12497500 steps (predicted n(n-1)/2 — far too slow to run in Python)
no answer: (None, 2)
```

**Complexity.** O(n²) → O(n) time, O(1) → O(n) space. Saving the index as the value (not just `True`) is what lets you return the pair immediately.

### Example 3 — Name the complexity of a snippet (drill)

**Problem.** For each loop below, predict the complexity, then verify it by
counting operations against the formula.

```python
import math


def snippet_a(n):
    """i doubles, inner loop runs i times."""
    ops = 0
    i = 1
    while i <= n:
        for _ in range(i):
            ops += 1
        i *= 2
    return ops


def snippet_b(n):
    """Inner loop shrinks by half each time."""
    ops = 0
    i = n
    while i > 0:
        for _ in range(i):
            ops += 1
        i //= 2
    return ops


def snippet_c(n):
    """Break on the first match; worst case still O(n^2)."""
    ops = 0
    for i in range(n):
        for j in range(n):
            ops += 1
            if j == n - 1:
                break
    return ops


if __name__ == "__main__":
    for n in (16, 64, 256):
        a, b, c = snippet_a(n), snippet_b(n), snippet_c(n)
        print(f"n={n:>4}: A={a:>7} (<= 2n: {a <= 2 * n}), "
              f"B={b:>7} (<= 2n: {b <= 2 * n}), C={c:>7} (== n^2: {c == n * n})")
    print("A and B are O(n): geometric series 1+2+4+...+n = 2n-1")
    print("C is O(n^2): the break only skips the last inner iteration of each row")
```

Output:

```text
n=  16: A=     31 (<= 2n: True), B=     31 (<= 2n: True), C=    256 (== n^2: True)
n=  64: A=    127 (<= 2n: True), B=    127 (<= 2n: True), C=   4096 (== n^2: True)
n= 256: A=    511 (<= 2n: True), B=    511 (<= 2n: True), C=  65536 (== n^2: True)
A and B are O(n): geometric series 1+2+4+...+n = 2n-1
C is O(n^2): the break only skips the last inner iteration of each row
```

**Complexity.** A and B are O(n) because `1 + 2 + 4 + … + n = 2n − 1` (a geometric series, not an arithmetic one — this is the mistake to avoid). C is O(n²): the `break` is a constant-factor saving, not an asymptotic one.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Time Complexity: Primality](https://www.hackerrank.com/challenges/ctci-big-o/problem) | HackerRank | Easy |
| [Interesting Function](https://codeforces.com/problemset/problem/1538/F) | Codeforces | Medium |
| [Binary Search](https://leetcode.com/problems/binary-search/) | LeetCode | Easy |
| [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/) | LeetCode | Easy |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain big-o is an upper bound; theta is a tight asymptotic bound without notes.
- [ ] Explain sequential phases add; independent nested phases multiply without notes.
- [ ] Explain amortized analysis spreads occasional expensive operations across a sequence without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
