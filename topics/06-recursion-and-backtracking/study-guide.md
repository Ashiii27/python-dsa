# Recursion and Backtracking: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Model the solution space as a decision tree. Each call owns one state; backtracking chooses, recurses, and restores so sibling branches see identical starting state.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | A base case emits or evaluates a complete state. |
| 2 | The recursion parameters must fully describe remaining choices. |
| 3 | Backtracking restores mutable state after each recursive call. |
| 4 | Pruning removes branches proven unable to succeed. |
| 5 | Duplicate handling usually combines sorting, start indices, and same-depth skipping. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Enumerate all choices | Backtracking |
| Repeated state results | Memoized recursion |
| Choose each item once | Advance start index |
| Constraint grid | Sets/bitmasks plus pruning |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For subsets of `[1, 2]`, the tree makes include/exclude decisions: `[] → [1] → [1,2]`, backtracks to `[1]`, then explores excluding 2; it later repeats under the branch excluding 1. Copy the path only when recording it.

## Tricks and interview notes

- Write the state meaning in one sentence before code.
- Use `path.append(x); dfs(...); path.pop()` as one visual unit.
- Process the most constrained Sudoku/N-Queens choice first for stronger pruning.
- Stop early when only one solution is required.

## Common mistakes

- **Watch for:** Appending the same mutable path object without copying.
- **Watch for:** Skipping duplicates across all depths instead of only siblings.
- **Watch for:** Using global state that is not restored.
- **Watch for:** Missing a termination condition when candidates may be reused.

## Implementation drills

1. Generate subsets with include/exclude and start-index styles.
2. Generate unique permutations with duplicate input.
3. Add pruning to N-Queens.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Recursion: the anatomy of a solution

Every recursive function has the same three parts: a **base case** that stops the
recursion, a **recursive case** that solves a strictly smaller instance, and the
combination step that builds the answer from the sub-answers.

```python
import sys


def factorial(n):
    if n <= 1:                     # 1. base case
        return 1
    return n * factorial(n - 1)    # 2. smaller instance, 3. combine


def sum_list(nums, i=0):
    """Avoid slicing (nums[1:] copies): pass an index instead."""
    if i == len(nums):
        return 0
    return nums[i] + sum_list(nums, i + 1)


def fib(n, memo=None):
    """Naive recursion is O(2^n); memoising the sub-answers makes it O(n)."""
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def trace_factorial(n, level=0):
    """Print the call tree so you can see what the interpreter is doing."""
    indent = "  " * level
    print(f"{indent}factorial({n}) called")
    if n <= 1:
        print(f"{indent}factorial({n}) -> 1 (base case)")
        return 1
    result = n * trace_factorial(n - 1, level + 1)
    print(f"{indent}factorial({n}) -> {result}")
    return result


def dive_to(depth):
    """Python has no tail-call optimisation and a frame limit."""
    def dive(n):
        return 0 if n == 0 else 1 + dive(n - 1)
    try:
        return f"reached depth {dive(depth)}"
    except RecursionError:
        return f"RecursionError before {depth} frames"


if __name__ == "__main__":
    print("factorial(5):", factorial(5))
    print("sum_list:", sum_list([1, 2, 3, 4]))
    print("fib(30):", fib(30), "| fib(10):", fib(10))
    print()
    trace_factorial(3)
    print()
    print("recursion limit:", sys.getrecursionlimit())

    original_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(120)                 # deliberately small for the demo
    try:
        print("dive(200) with limit 120:", dive_to(200))
    finally:
        sys.setrecursionlimit(original_limit)  # always restore what you change
    print("limit restored to:", sys.getrecursionlimit())
```

Output:

```text
factorial(5): 120
sum_list: 10
fib(30): 832040 | fib(10): 55

factorial(3) called
  factorial(2) called
    factorial(1) called
    factorial(1) -> 1 (base case)
  factorial(2) -> 2
factorial(3) -> 6

recursion limit: 1000
dive(200) with limit 120: RecursionError before 200 frames
limit restored to: 1000
```

**How it works**

- The base case must be reachable and must handle the smallest input (empty list, `n = 0`, `node is None`).
- Slice-based recursion (`sum_list(nums[1:])`) is O(n²) because each slice copies; pass an index instead.
- Memoisation works when the same sub-problem repeats (overlapping subproblems). `fib(30)` goes from ~2.7 million calls to 59.
- Python does **not** optimise tail calls, and the default frame limit is ~1000. Deep DFS on a graph needs `sys.setrecursionlimit(...)` or an explicit stack.

### 2. Backtracking: choose, explore, undo

Backtracking is DFS over a tree of choices. The template never changes: if the
path is complete, record it; otherwise try each candidate — **choose** it,
**explore**, then **undo** the choice so the next branch starts clean.

```python
def subsets(nums):
    """All 2^n subsets: at each index, skip it or take it."""
    result = []

    def backtrack(i, path):
        if i == len(nums):                 # complete path
            result.append(path.copy())     # copy: path is reused
            return
        backtrack(i + 1, path)             # choice 1: skip nums[i]
        path.append(nums[i])               # choose
        backtrack(i + 1, path)             # explore
        path.pop()                         # undo  <- the line people forget

    backtrack(0, [])
    return result


def permutations(nums):
    """All n! orderings: at each step pick one unused element."""
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True                 # choose
            path.append(x)
            backtrack(path)                # explore
            path.pop()                     # undo
            used[i] = False

    backtrack([])
    return result


def combinations(nums, k):
    """All k-sized subsets: prune the branches that cannot reach size k."""
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path.copy())
            return
        # Only pick from start.. end, which also prevents duplicate orderings.
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


if __name__ == "__main__":
    print("subsets([1, 2, 3]):", subsets([1, 2, 3]))
    print("count:", len(subsets(list(range(5)))), "(2^5 expected)")
    print("permutations([1, 2, 3]):", permutations([1, 2, 3]))
    print("combinations([1, 2, 3, 4], 2):", combinations([1, 2, 3, 4], 2))
    print("empty input subsets:", subsets([]))
```

Output:

```text
subsets([1, 2, 3]): [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
count: 32 (2^5 expected)
permutations([1, 2, 3]): [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
combinations([1, 2, 3, 4], 2): [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
empty input subsets: [[]]
```

**How it works**

- Three shapes cover most problems: **include/exclude** (subsets), **pick one unused** (permutations), and **pick from a moving start index** (combinations). Everything else is a variation with extra pruning.
- `path.copy()` before appending is mandatory: `path` is a single shared list, so appending it directly would store a reference that later mutates.
- The undo step must restore state exactly (`path.pop()`, `used[i] = False`). Forgetting it produces paths that carry leftovers from previous branches.
- Complexity is the size of the decision tree: O(2ⁿ) for subsets, O(n!) for permutations, O(n choose k) for combinations — times the cost of copying a path.

### 3. Pruning: cutting branches before they are built

Backtracking is only fast enough when you abandon hopeless branches early.

```python
def combination_sum(candidates, target):
    """Reusable candidates that sum to target; sorted input lets us stop early."""
    candidates = sorted(candidates)
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:      # prune: sorted, so the rest are worse
                break
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)   # i, not i+1: reuse allowed
            path.pop()

    backtrack(0, target, [])
    return result


def count_n_queens(n):
    """Number of ways to place n queens: one per column, check conflicts per row."""
    def backtrack(row, columns, diag1, diag2):
        if row == n:
            return 1
        total = 0
        for col in range(n):
            d1, d2 = row - col, row + col     # the two diagonal identifiers
            if col in columns or d1 in diag1 or d2 in diag2:
                continue                      # attacked: skip this branch entirely
            total += backtrack(row + 1, columns | {col}, diag1 | {d1}, diag2 | {d2})
        return total

    return backtrack(0, frozenset(), frozenset(), frozenset())


def solve_n_queens(n):
    """Return one board as a list of strings, or None."""
    board = [["."] * n for _ in range(n)]

    def attacked(row, col):
        for r in range(row):
            if board[r][col] == "Q":
                return True
            if col - (row - r) >= 0 and board[r][col - (row - r)] == "Q":
                return True
            if col + (row - r) < n and board[r][col + (row - r)] == "Q":
                return True
        return False

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if attacked(row, col):
                continue
            board[row][col] = "Q"             # choose
            if backtrack(row + 1):            # explore
                return True
            board[row][col] = "."             # undo
        return False

    return ["".join(row) for row in board] if backtrack(0) else None


if __name__ == "__main__":
    print("combination_sum([2, 3, 6, 7], 7):", combination_sum([2, 3, 6, 7], 7))
    print("combination_sum([2, 4, 6], 5):", combination_sum([2, 4, 6], 5))
    print("queens counts n=1..8:", [count_n_queens(n) for n in range(1, 9)])
    print("one 6-queen solution:")
    for row in solve_n_queens(6):
        print("   ", row)
```

Output:

```text
combination_sum([2, 3, 6, 7], 7): [[2, 2, 3], [7]]
combination_sum([2, 4, 6], 5): []
queens counts n=1..8: [1, 0, 0, 2, 10, 4, 40, 92]
one 6-queen solution:
    .Q....
    ...Q..
    .....Q
    Q.....
    ..Q...
    ....Q.
```

**How it works**

- `combination_sum` prunes with `break` (not `continue`) because the candidates are sorted: once one is too large, every later one is too.
- Passing `i` (not `i + 1`) as the next start allows reusing a candidate; `i + 1` would make each candidate usable once — that single character is the difference between two different problems.
- In `count_n_queens` the constraints are encoded as sets: a column conflict is `col in columns`, a diagonal conflict is `row − col` (↘) or `row + col` (↗) already used. Checking before placing prunes a whole subtree for the cost of one `in` test.

## Solved examples

### Example 1 — Generate parentheses (Medium)

**Problem.** Given `n`, generate every well-formed combination of `n` pairs of parentheses.

**Approach.** Build strings left to right, tracking how many opens are available and how many more closes are currently allowed. Two rules prune every invalid string: place `(` only if any remain, and place `)` only if it would match an unmatched `(`. Every generated string is valid, so no final filtering is needed.

```python
def generate_parentheses(n):
    result = []

    def backtrack(path, opens_left, closes_allowed):
        if len(path) == 2 * n:                     # complete: all pairs used
            result.append("".join(path))
            return
        if opens_left > 0:                         # we may open
            path.append("(")
            backtrack(path, opens_left - 1, closes_allowed + 1)
            path.pop()
        if closes_allowed > 0:                     # we may close a pending open
            path.append(")")
            backtrack(path, opens_left, closes_allowed - 1)
            path.pop()

    backtrack([], n, 0)
    return result


if __name__ == "__main__":
    for n in (0, 1, 2, 3):
        combos = generate_parentheses(n)
        print(f"n={n}: {len(combos):>2} -> {combos}")
```

Output:

```text
n=0:  1 -> ['']
n=1:  1 -> ['()']
n=2:  2 -> ['(())', '()()']
n=3:  5 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
```

**Complexity.** O(Cₙ · n) time and O(n) recursion depth, where Cₙ is the n-th Catalan number — the count of valid strings, so the output itself sets the lower bound.

### Example 2 — Combination sum II, no duplicate sets (Medium)

**Problem.** Find all unique combinations of `candidates` summing to `target`,
where each candidate may be used at most once and the input may contain duplicates.

**Approach.** Sort first so duplicates sit next to each other. Then, at each level of the decision tree, skip a value if it equals the previous value **at the same level** — that is the standard de-duplication rule. Using `i + 1` for the next start enforces "each candidate once".

```python
def combination_sum2(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(path.copy())
            return
        previous = None
        for i in range(start, len(candidates)):
            value = candidates[i]
            if value > remaining:
                break                              # sorted: prune the rest
            if value == previous:
                continue                           # same level: skip duplicate branch
            previous = value
            path.append(value)
            backtrack(i + 1, remaining - value, path)   # i + 1: use each once
            path.pop()

    backtrack(0, target, [])
    return result


if __name__ == "__main__":
    print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combination_sum2([2, 5, 2, 1, 2], 5))
    print("no solution:", combination_sum2([2, 4], 3))
```

Output:

```text
[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
[[1, 2, 2], [5]]
no solution: []
```

**Complexity.** O(2ⁿ) in the worst case (each element is taken or skipped) with O(n) space for the path; de-duplication removes repeated branches but does not change the worst case.

### Example 3 — Word search (Medium)

**Problem.** Given a grid of letters and a word, decide whether the word can be
built by walking through adjacent cells without reusing a cell.

**Approach.** Try every cell as a starting point, then DFS in four directions. Mark the current cell as visited while exploring and restore it on the way out — the same choose/explore/undo cycle, applied to a grid. Stop descending as soon as a character mismatches.

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def dfs(r, c, i):
        if i == len(word):                      # every character matched
            return True
        if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
            return False
        board[r][c] = "#"                       # mark visited
        found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in directions)
        board[r][c] = word[i]                   # restore
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    print("ABCCED:", exist(board, "ABCCED"))
    print("SEE   :", exist(board, "SEE"))
    print("ABCB  :", exist(board, "ABCB"))
    print("board restored:", board[0])
```

Output:

```text
ABCCED: True
SEE   : True
ABCB  : False
board restored: ['A', 'B', 'C', 'E']
```

**Complexity.** O(rows · cols · 3^L) time (the first step has 4 directions, every later one at most 3 because we cannot go back) and O(L) recursion depth. Mutating the board in place is the fastest visit-marking trick, but restore it — the grid must look untouched when the function returns.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | LeetCode | Medium |
| [Combinations](https://leetcode.com/problems/combinations/) | LeetCode | Medium |
| [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) | LeetCode | Medium |
| [Chessboard and Queens](https://cses.fi/problemset/task/1624) | CSES | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain a base case emits or evaluates a complete state without notes.
- [ ] Explain the recursion parameters must fully describe remaining choices without notes.
- [ ] Explain backtracking restores mutable state after each recursive call without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
