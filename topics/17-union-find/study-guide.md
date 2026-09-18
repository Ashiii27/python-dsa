# Union Find / Disjoint Set Union: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

DSU maintains a partition under repeated merges. It answers whether nodes share a component, but not arbitrary path, deletion, or historical connectivity questions.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Each element follows parent pointers to a representative root. |
| 2 | Path compression flattens find paths. |
| 3 | Union by size/rank attaches the smaller tree below the larger. |
| 4 | A failed union detects a cycle in an undirected edge stream. |
| 5 | Component metadata can live at roots. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Repeated connectivity after unions | DSU |
| First redundant undirected edge | Failed union |
| Kruskal MST | Sort edges + DSU |
| Merge accounts/identities | Map attributes then union |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Initially `{0},{1},{2}`. Union(0,1) makes one root size 2; union(1,2) first finds root(1)=root(0), then attaches 2. A later union(0,2) returns false and reveals a cycle edge.

## Tricks and interview notes

- Initialize component count to n and decrement only on successful unions.
- Compress coordinates such as emails, rows, and columns into DSU ids.
- Keep size/rank data meaningful only at roots.
- DSU is excellent offline; dynamic deletions usually need another technique.

## Common mistakes

- **Watch for:** Decrementing component count on redundant unions.
- **Watch for:** Comparing immediate parents instead of roots.
- **Watch for:** Applying DSU directly to directed-cycle detection.
- **Watch for:** Recursive find exceeding Python depth before compression.

## Implementation drills

1. Implement iterative path compression.
2. Count components after an edge stream.
3. Implement Kruskal and return failure if disconnected.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Road Construction](https://cses.fi/problemset/task/1676) | CSES | Medium |
| [Road Reparation](https://cses.fi/problemset/task/1675) | CSES | Medium |
| [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | LeetCode | Medium |
| [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain each element follows parent pointers to a representative root without notes.
- [ ] Explain path compression flattens find paths without notes.
- [ ] Explain union by size/rank attaches the smaller tree below the larger without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
