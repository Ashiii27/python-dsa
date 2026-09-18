# Graphs: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Choose a representation, define the state being visited, and make direction explicit. Traversal solves reachability; BFS layers solve unweighted distance; topological order solves directed dependencies.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Adjacency lists use O(V+E); matrices use O(V²). |
| 2 | DFS and BFS both find components and reachability. |
| 3 | BFS gives shortest edge count in unweighted graphs. |
| 4 | Kahn indegrees or DFS colors detect directed cycles. |
| 5 | Grid cells are graph nodes with implicit neighbors. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Connected regions | DFS/BFS |
| Fewest unweighted steps | BFS |
| Prerequisites/order | Topological sort |
| Two-group constraint | Bipartite coloring |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

In multi-source BFS for rotten oranges, enqueue every rotten cell at minute zero. Each queue layer infects cells one minute farther away. This is equivalent to one virtual source connected to all initial rotten cells.

## Tricks and interview notes

- Mark visited when enqueuing to avoid duplicate queue entries.
- For undirected cycle DFS, track the parent edge.
- Build both forward and reverse graphs when direction reversal simplifies the query.
- Count all vertices, including isolated ones.

## Common mistakes

- **Watch for:** Treating a directed graph as undirected.
- **Watch for:** Using DFS depth as shortest distance.
- **Watch for:** Forgetting invalid-prefix handling in Alien Dictionary.
- **Watch for:** Mutating a grid when callers expect it preserved.

## Implementation drills

1. Implement recursive DFS, iterative DFS, and BFS.
2. Count grid components.
3. Implement Kahn topological sort with cycle detection.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Counting Rooms](https://cses.fi/problemset/task/1192) | CSES | Medium |
| [Building Roads](https://cses.fi/problemset/task/1666) | CSES | Medium |
| [Message Route](https://cses.fi/problemset/task/1667) | CSES | Medium |
| [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain adjacency lists use o(v+e); matrices use o(v²) without notes.
- [ ] Explain dfs and bfs both find components and reachability without notes.
- [ ] Explain bfs gives shortest edge count in unweighted graphs without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
