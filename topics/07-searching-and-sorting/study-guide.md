# Searching and Sorting: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Sorting creates order that enables greedy scans, binary search, two pointers, and divide-and-conquer counting. Know what each algorithm guarantees about time, stability, and memory.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Comparison sorting has an Ω(n log n) general lower bound. |
| 2 | Merge sort is stable and predictable O(n log n), using O(n) auxiliary space. |
| 3 | Quicksort is expected O(n log n), worst O(n²); partitioning powers quickselect. |
| 4 | Counting/bucket/radix methods exploit restricted keys. |
| 5 | Custom comparator problems compare concatenations or transformed keys. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need ordered sweep | Sort then scan |
| Need kth item only | Quickselect or heap |
| Small bounded key range | Counting/bucket sort |
| Count cross-order pairs | Merge-sort counting |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Merge `[2, 5]` and `[1, 3]`: choosing 1 before 2 contributes two inversions because both remaining left values exceed 1; choosing 3 before 5 contributes one. The merge simultaneously sorts and counts.

## Tricks and interview notes

- Ask whether input mutation is allowed before sorting in place.
- Python sort is stable, enabling multi-pass sorting.
- Use three-way partitioning when duplicate pivots are common.
- For largest-number ordering, compare `a+b` against `b+a`.

## Common mistakes

- **Watch for:** Claiming quickselect is worst-case O(n).
- **Watch for:** Forgetting key computation cost in sort complexity.
- **Watch for:** Using subtraction as a comparator where values may overflow in other languages.
- **Watch for:** Merging touching intervals without checking the problem definition.

## Implementation drills

1. Implement merge sort and prove its recurrence.
2. Implement Dutch national flag partition.
3. Count inversions while merging.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Apartments](https://cses.fi/problemset/task/1084) | CSES | Medium |
| [Array Division](https://cses.fi/problemset/task/1085) | CSES | Medium |
| [H-Index](https://leetcode.com/problems/h-index/) | LeetCode | Medium |
| [Sort an Array](https://leetcode.com/problems/sort-an-array/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain comparison sorting has an ω(n log n) general lower bound without notes.
- [ ] Explain merge sort is stable and predictable o(n log n), using o(n) auxiliary space without notes.
- [ ] Explain quicksort is expected o(n log n), worst o(n²); partitioning powers quickselect without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
