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
