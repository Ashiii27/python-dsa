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
