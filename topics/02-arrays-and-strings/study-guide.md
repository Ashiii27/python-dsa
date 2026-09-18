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
