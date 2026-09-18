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
