# Segment Tree and Fenwick Tree: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Precompute hierarchical aggregates so point updates and range queries touch only logarithmically many nodes. Choose the structure based on the algebra of the operation.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Fenwick trees store partial prefix aggregates via the lowbit decomposition. |
| 2 | Segment trees store aggregates for explicit intervals. |
| 3 | Point update/range query are O(log n) in both common forms. |
| 4 | Lazy propagation postpones range updates. |
| 5 | Coordinate compression maps sparse ordered values into dense indices. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Prefix sums + point updates | Fenwick tree |
| General associative range query | Segment tree |
| Range updates + queries | Lazy segment tree |
| Values up to 10^9 but only n used | Coordinate compression |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

A Fenwick prefix query repeatedly performs `i -= i & -i`, removing the least significant set-bit block. An update performs `i += i & -i`, visiting every stored range that contains the index.

## Tricks and interview notes

- Use 1-based internal Fenwick indices even if the public API is 0-based.
- Define segment merge identity: 0 for sum, infinity for min, etc.
- Compression preserves order, not numeric distance.
- Test non-power-of-two lengths.

## Common mistakes

- **Watch for:** Off-by-one errors converting range sum to `prefix(r)-prefix(l-1)`.
- **Watch for:** Using Fenwick for an operation without a suitable inverse when arbitrary ranges are needed.
- **Watch for:** Forgetting to push lazy tags before descending.
- **Watch for:** Allocating a tree too small; 4n is a safe recursive size.

## Implementation drills

1. Implement Fenwick point-add and range-sum.
2. Implement iterative segment tree.
3. Add lazy range addition and range sum.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Dynamic Range Sum Queries](https://cses.fi/problemset/task/1648) | CSES | Medium |
| [Hotel Queries](https://cses.fi/problemset/task/1143) | CSES | Medium |
| [List Removals](https://cses.fi/problemset/task/1749) | CSES | Medium |
| [Range Sum Query 2D Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain fenwick trees store partial prefix aggregates via the lowbit decomposition without notes.
- [ ] Explain segment trees store aggregates for explicit intervals without notes.
- [ ] Explain point update/range query are o(log n) in both common forms without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
