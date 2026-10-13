# Dynamic Programming: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

DP is exhaustive search with repeated states computed once. Define a state with a precise meaning, derive transitions from the final decision, establish base cases, then choose evaluation order.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Memoization evaluates reachable states recursively. |
| 2 | Tabulation evaluates states in dependency order. |
| 3 | 1D DP handles prefix or amount states; 2D DP often handles two prefixes or intervals. |
| 4 | Knapsack distinguishes reuse (forward iteration) from single use (reverse iteration). |
| 5 | State compression is valid only when overwritten values are no longer needed. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Overlapping recursive states | Memoization/DP |
| Choose or skip item | Knapsack/subsequence DP |
| Two strings/prefixes | 2D grid DP |
| Choose split/last operation | Interval DP |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

House Robber state: after each house, keep `skip` (best if current is skipped) and `take` (best if current is taken). Update from old values: `new_take = skip + value`, `new_skip = max(skip, take)`.

## Tricks and interview notes

- Write the state definition above the code.
- Derive transitions by asking what the final choice was.
- Use reverse amount iteration for 0/1 knapsack to prevent reusing an item.
- Reconstruct an answer by storing parents/choices, not only scores.

## Common mistakes

- **Watch for:** Starting implementation before defining state.
- **Watch for:** Wrong table iteration order.
- **Watch for:** Confusing subarray with subsequence.
- **Watch for:** Optimizing memory before the recurrence is correct.

## Implementation drills

1. Solve Fibonacci top-down and bottom-up.
2. Derive 0/1 and unbounded knapsack side by side.
3. Reconstruct one longest common subsequence.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. From exponential recursion to a table

DP exists because of **overlapping subproblems**: the naive recursion recomputes
the same thing again and again. Two ways to fix it — memoise top-down, or fill a
table bottom-up. Both are O(n); pick whichever expresses the state more clearly.

```python
from functools import lru_cache


def fib_naive(n):
    """Exponential: each call recomputes both children."""
    calls = 0

    def go(k):
        nonlocal calls
        calls += 1
        if k < 2:
            return k
        return go(k - 1) + go(k - 2)

    value = go(n)
    return value, calls


@lru_cache(maxsize=None)
def fib_memo(n):
    """Top-down: same recursion, but each state is computed once."""
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_table(n):
    """Bottom-up: no recursion, O(1) space because we only need two states."""
    if n < 2:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


def fib_full_table(n):
    """Bottom-up with the whole table kept — use this shape when you need it later."""
    dp = [0, 1] + [0] * max(0, n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[:n + 1]


if __name__ == "__main__":
    value, calls = fib_naive(25)
    print(f"fib_naive(25) = {value} using {calls:,} recursive calls")
    print(f"fib_memo(30)  = {fib_memo(30)} using {fib_memo.cache_info().misses} computed states")
    print(f"fib_table(30) = {fib_table(30)}")
    print("table for n=10:", fib_full_table(10))
    print("base cases:", fib_table(0), fib_table(1))
```

Output:

```text
fib_naive(25) = 75025 using 242,785 recursive calls
fib_memo(30)  = 832040 using 31 computed states
fib_table(30) = 832040
table for n=10: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
base cases: 0 1
```

**How it works**

- The jump from 242,785 calls to 31 states is the entire point of DP. Count the calls once and you will never forget why.
- Top-down (`@lru_cache`) computes only the states you actually reach and reads like the recurrence — start there when the state space is sparse.
- Bottom-up has no recursion-limit problem, and lets you **compress** the table (here to two variables) once you see which previous states the transition needs.
- Define the state in words before coding: "`dp[i]` = number of ways to reach step `i`". If you cannot state it in one sentence, the recurrence will be wrong.

### 2. One-dimensional DP: the sequence patterns

```python
def climb_stairs(n):
    """Ways to reach step n taking 1 or 2 steps: dp[i] = dp[i-1] + dp[i-2]."""
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


def min_cost_climbing_stairs(cost):
    """Cheapest way to pass step i: pay to leave i-1 or i-2."""
    prev2, prev1 = 0, 0                      # standing on step 0 or 1 is free
    for i in range(2, len(cost) + 1):
        prev2, prev1 = prev1, min(prev1 + cost[i - 1], prev2 + cost[i - 2])
    return prev1


def house_robber(nums):
    """Max loot without adjacent houses: take this house, or skip it."""
    take = skip = 0
    for amount in nums:
        take, skip = skip + amount, max(take, skip)
    return max(take, skip)


def max_subarray_sum_dp(nums):
    """Kadane as DP: best sum ending here = extend or restart."""
    best = current = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best


def decode_ways_count(s):
    """Number of ways to split a digit string into 1-26 codes; 0 is invalid alone."""
    if not s or s[0] == "0":
        return 0
    prev2, prev1 = 1, 1                      # dp[0] = dp[1] = 1
    for i in range(2, len(s) + 1):
        ways = 0
        if s[i - 1] != "0":
            ways += prev1                    # single digit
        if 10 <= int(s[i - 2:i]) <= 26:
            ways += prev2                    # two digits
        prev2, prev1 = prev1, ways
    return prev1


if __name__ == "__main__":
    print("climb_stairs(5):", climb_stairs(5))
    print("min_cost([10, 15, 20]):", min_cost_climbing_stairs([10, 15, 20]))
    print("min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]):",
          min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print("house_robber([2, 7, 9, 3, 1]):", house_robber([2, 7, 9, 3, 1]))
    print("max_subarray([-2, 1, -3, 4, -1]):", max_subarray_sum_dp([-2, 1, -3, 4, -1]))
    for s in ("226", "06", "27", "11106"):
        print(f"decode_ways({s!r}):", decode_ways_count(s))
```

Output:

```text
climb_stairs(5): 8
min_cost([10, 15, 20]): 15
min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]): 6
house_robber([2, 7, 9, 3, 1]): 12
max_subarray([-2, 1, -3, 4, -1]): 4
decode_ways('226'): 3
decode_ways('06'): 0
decode_ways('27'): 1
decode_ways('11106'): 2
```

**How it works**

- Every one of these keeps only the last one or two states — the pattern to internalise is "which previous states does my transition read?", then keep exactly those.
- `house_robber` is the cleanest "take / skip" formulation: `take` means "I robbed the previous house", `skip` means "I did not", and the answer is `max` at the end.
- `decode_ways_count` shows the two classic edge cases in 1D DP: an invalid single character (`"0"`) contributes nothing, and the two-digit window must be range-checked, not just length-checked.

### 3. Two-dimensional DP: grids and two sequences

```python
def unique_paths(rows, cols):
    """Ways to walk from the top-left to the bottom-right, only down or right."""
    dp = [1] * cols                          # one row of rolling state
    for _ in range(1, rows):
        for c in range(1, cols):
            dp[c] += dp[c - 1]               # from above (old dp[c]) + from the left
    return dp[cols - 1]


def longest_common_subsequence(a, b):
    """Length of the longest subsequence shared by both strings."""
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1      # match: extend
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])   # skip one character
    return dp[len(a)][len(b)]


def edit_distance(word1, word2):
    """Minimum insert/delete/replace operations to turn word1 into word2."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i                         # delete everything
    for j in range(n + 1):
        dp[0][j] = j                         # insert everything
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],        # delete
                                   dp[i][j - 1],        # insert
                                   dp[i - 1][j - 1])    # replace
    return dp[m][n]


def longest_palindromic_substring(s):
    """Expand around each centre: O(n^2) time, O(1) space."""
    best = ""
    for centre in range(len(s)):
        for left, right in ((centre, centre), (centre, centre + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(best):
                best = s[left + 1:right]
    return best


if __name__ == "__main__":
    print("unique_paths(3, 7):", unique_paths(3, 7))
    print("LCS('abcde', 'ace'):", longest_common_subsequence("abcde", "ace"))
    print("LCS('abc', 'abc'):", longest_common_subsequence("abc", "abc"))
    print("LCS('abc', 'def'):", longest_common_subsequence("abc", "def"))
    print("edit_distance('horse', 'ros'):", edit_distance("horse", "ros"))
    print("edit_distance('intention', 'execution'):", edit_distance("intention", "execution"))
    print("longest palindrome in 'babad':", longest_palindromic_substring("babad"))
    print("longest palindrome in 'cbbd':", longest_palindromic_substring("cbbd"))
```

Output:

```text
unique_paths(3, 7): 28
LCS('abcde', 'ace'): 3
LCS('abc', 'abc'): 3
LCS('abc', 'def'): 0
edit_distance('horse', 'ros'): 3
edit_distance('intention', 'execution'): 5
longest palindrome in 'babad': bab
longest palindrome in 'cbbd': bb
```

**How it works**

- `unique_paths` uses a **rolling row**: `dp[c]` before the update is the value from the row above, and after the update it is the current row. Same result, O(cols) memory.
- Two-string DP always indexes `dp[i][j]` over prefixes `a[:i]` and `b[:j]`, with row 0 and column 0 reserved as empty-string base cases. That off-by-one padding is why the loops start at 1.
- `edit_distance`'s three transitions map exactly to the three operations, and the base row/column is "delete/insert everything" — derive the base cases from the state definition and you cannot get them wrong.
- Row-by-row order matters: `dp[i][j]` must be computed after `dp[i−1][j]`, `dp[i][j−1]`, and `dp[i−1][j−1]`. Standard nested loops do that automatically; recursion with memoisation also does, but the iterative form lets you compress a dimension.

## Solved examples

### Example 1 — Coin change: minimum coins and number of ways (Medium)

**Problem.** Given coin denominations and an amount, (a) find the fewest coins
needed, and (b) count the number of combinations that make the amount.

**Approach.** Two different DPs over the same state. For the minimum, `dp[a]` is the fewest coins for amount `a`, and the answer is built by trying every coin. For the count, iterate **coins in the outer loop** — that way each combination is counted once instead of once per permutation. Order of loops is the whole difference.

```python
def coin_change_min(coins, amount):
    """Fewest coins, or -1. dp[a] = 1 + min(dp[a - c])."""
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return -1 if dp[amount] == INF else dp[amount]


def coin_change_ways(coins, amount):
    """Number of combinations. Coins in the OUTER loop avoids counting order."""
    dp = [1] + [0] * amount
    for coin in coins:
        for a in range(coin, amount + 1):
            dp[a] += dp[a - coin]
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    print("min coins for 11:", coin_change_min(coins, 11))
    print("ways to make 5:", coin_change_ways(coins, 5))
    print("ways to make 0:", coin_change_ways(coins, 0))
    print("impossible amount:", coin_change_min([2], 3))
    print("impossible ways:", coin_change_ways([2], 3))
```

Output:

```text
min coins for 11: 3
ways to make 5: 4
ways to make 0: 1
impossible amount: -1
impossible ways: 0
```

**Complexity.** Both are O(n · amount) time and O(amount) space. Swapping the loops in the "ways" version counts permutations instead of combinations — a classic interview follow-up.

### Example 2 — Longest increasing subsequence (Medium)

**Problem.** Length of the longest strictly increasing subsequence.

**Approach.** Two ways. The O(n²) DP keeps `dp[i]` = best LIS ending at `i` and extends from every earlier smaller element. The O(n log n) version keeps a list `tails` where `tails[k]` is the smallest possible tail of an increasing subsequence of length `k + 1`; `bisect_left` finds where each value belongs. Smaller tails are always better, which is why the greedy replacement is safe.

```python
from bisect import bisect_left


def lis_dp(nums):
    """O(n^2): dp[i] = 1 + max(dp[j] for j < i and nums[j] < nums[i])."""
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_fast(nums):
    """O(n log n): maintain the smallest tail for each subsequence length."""
    tails = []
    for x in nums:
        position = bisect_left(tails, x)         # first tail >= x
        if position == len(tails):
            tails.append(x)                      # new longest length
        else:
            tails[position] = x                  # improve an existing tail
    return len(tails)


def lis_sequence(nums):
    """Reconstruct one LIS using parent pointers with the O(n log n) method."""
    tails, tails_index, parent = [], [], [-1] * len(nums)
    for i, x in enumerate(nums):
        position = bisect_left(tails, x)
        if position > 0:
            parent[i] = tails_index[position - 1]
        if position == len(tails):
            tails.append(x)
            tails_index.append(i)
        else:
            tails[position] = x
            tails_index[position] = i
    sequence, k = [], tails_index[-1] if tails_index else -1
    while k != -1:
        sequence.append(nums[k])
        k = parent[k]
    return sequence[::-1]


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS length (DP):", lis_dp(nums))
    print("LIS length (fast):", lis_fast(nums))
    print("one LIS:", lis_sequence(nums))
    print("descending:", lis_fast([5, 4, 3, 2, 1]))
    print("empty:", lis_fast([]), lis_dp([]))
```

Output:

```text
LIS length (DP): 4
LIS length (fast): 4
one LIS: [2, 3, 7, 18]
descending: 1
empty: 0 0
```

**Complexity.** O(n²) for the DP, O(n log n) for the patience-sorting version; both O(n) space. The `tails` trick also solves Russian-doll envelopes (sort one dimension, LIS on the other) and "minimum number of increasing subsequences".

### Example 3 — 0/1 knapsack with reconstruction (Medium)

**Problem.** Each item has a weight and a value; maximise the value without
exceeding the capacity, using each item at most once.

**Approach.** `dp[i][c]` is the best value using the first `i` items with capacity `c`: either skip item `i`, or take it (if it fits) and add its value to `dp[i−1][c−w]`. That is the 2D table; because row `i` only reads row `i − 1`, it compresses to one array — and the capacity loop must then run **backwards**, so each item is used at most once.

```python
def knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]                     # skip item i-1
            if c >= weights[i - 1]:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - weights[i - 1]] + values[i - 1])
    # reconstruct which items were taken
    chosen, c = [], capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            chosen.append(i - 1)
            c -= weights[i - 1]
    return dp[n][capacity], chosen[::-1]


def knapsack_1d(weights, values, capacity):
    """Same answer with one row: iterate capacity BACKWARDS to avoid reusing items."""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for c in range(capacity, weights[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - weights[i]] + values[i])
    return dp[capacity]


if __name__ == "__main__":
    weights, values, capacity = [1, 3, 4, 5], [1, 4, 5, 7], 7
    best, items = knapsack_2d(weights, values, capacity)
    print("best value:", best, "| items taken (indices):", items)
    print("best value (1D):", knapsack_1d(weights, values, capacity))
    print("zero capacity:", knapsack_1d(weights, values, 0))
    print("no items:", knapsack_1d([], [], 5))
```

Output:

```text
best value: 9 | items taken (indices): [1, 2]
best value (1D): 9
zero capacity: 0
no items: 0
```

**Complexity.** O(n · capacity) time; O(n · capacity) space for the 2D version (needed for reconstruction) and O(capacity) for the 1D version. Forward iteration in the 1D version turns it into the *unbounded* knapsack — another standard follow-up.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Dice Combinations](https://cses.fi/problemset/task/1633) | CSES | Easy |
| [Book Shop](https://cses.fi/problemset/task/1158) | CSES | Medium |
| [Removing Digits](https://cses.fi/problemset/task/1637) | CSES | Medium |
| [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain memoization evaluates reachable states recursively without notes.
- [ ] Explain tabulation evaluates states in dependency order without notes.
- [ ] Explain 1d dp handles prefix or amount states; 2d dp often handles two prefixes or intervals without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
