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
