# Heaps and Priority Queues: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A heap keeps the next extreme item accessible without fully sorting everything. Heap entries should contain all fields needed for deterministic priority and lazy stale-entry detection.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Python `heapq` is a binary min-heap. |
| 2 | Push/pop are O(log n); peek is O(1); heapify is O(n). |
| 3 | A min-heap of size k retains the k largest processed items. |
| 4 | Two heaps split a stream around its median. |
| 5 | K-way merge stores only one frontier item per source. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Repeated next minimum | Min-heap |
| Top k from stream | Size-k min-heap |
| Running median | Two balanced heaps |
| Merge sorted sources | Heap of frontiers |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For top 3 values, push each item. Whenever size becomes 4, pop the minimum. The heap root is the third-largest processed value, and discarded values can never re-enter the top three.

## Tricks and interview notes

- Store `(priority, tie_breaker, item)` when items are not directly comparable.
- Use lazy deletion when arbitrary heap removal would be expensive.
- `heapq.nlargest` is useful, but implement the pattern for interviews.
- Choose a heap over sorting when data streams or only k outputs are needed.

## Common mistakes

- **Watch for:** Negating some but not all max-heap comparisons.
- **Watch for:** Letting equal priorities compare non-orderable objects.
- **Watch for:** Forgetting to remove stale entries.
- **Watch for:** Calling heapify O(n log n); bottom-up heapify is O(n).

## Implementation drills

1. Implement top-k streaming values.
2. Merge k sorted arrays.
3. Maintain a streaming median.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Restaurant Customers](https://cses.fi/problemset/task/1619) | CSES | Medium |
| [Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) | LeetCode | Hard |
| [IPO](https://leetcode.com/problems/ipo/) | LeetCode | Hard |
| [Jesse and Cookies](https://www.hackerrank.com/challenges/jesse-and-cookies/problem) | HackerRank | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain python without notes.
- [ ] Explain push/pop are o(log n); peek is o(1); heapify is o(n) without notes.
- [ ] Explain a min-heap of size k retains the k largest processed items without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
