# Advanced Graphs: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Advanced graph algorithms refine traversal with a stronger invariant: finalized shortest distance, safe relaxation count, low-link reachability, or cut/component structure.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Dijkstra finalizes smallest tentative distances with non-negative edges. |
| 2 | Bellman-Ford relaxes all edges and handles negatives/cycle detection. |
| 3 | Floyd-Warshall is O(V³) all-pairs DP. |
| 4 | Tarjan low-link values identify bridges, articulation points, and SCC structure. |
| 5 | Prim and Kruskal construct MSTs using cut safety. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Non-negative weighted shortest path | Dijkstra |
| Negative edges or bounded flights | Bellman-Ford |
| Connect all nodes cheaply | MST |
| Critical edge/component | Low-link DFS |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Dijkstra heap entries may become stale. When `(distance,node)` is popped, skip it if it differs from the current best distance. Non-negative edges guarantee the first non-stale pop finalizes that shortest distance.

## Tricks and interview notes

- Store adjacency as `(weight, neighbor)` consistently.
- Use infinity rather than an arbitrary large number.
- In bridge DFS, skip only the parent edge id when parallel edges can exist.
- Choose Prim for implicit dense graphs and Kruskal for sortable edge lists.

## Common mistakes

- **Watch for:** Using Dijkstra with negative edges.
- **Watch for:** Marking a Dijkstra node visited when pushed.
- **Watch for:** Confusing MST with a shortest-path tree.
- **Watch for:** Updating low-link incorrectly across tree versus back edges.

## Implementation drills

1. Implement Dijkstra with stale-entry skipping.
2. Implement Kruskal with DSU.
3. Find bridges and test parallel-edge behavior.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Shortest Routes I](https://cses.fi/problemset/task/1671) | CSES | Medium |
| [High Score](https://cses.fi/problemset/task/1673) | CSES | Hard |
| [Road Reparation](https://cses.fi/problemset/task/1675) | CSES | Medium |
| [Planets and Kingdoms](https://cses.fi/problemset/task/1683) | CSES | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain dijkstra finalizes smallest tentative distances with non-negative edges without notes.
- [ ] Explain bellman-ford relaxes all edges and handles negatives/cycle detection without notes.
- [ ] Explain floyd-warshall is o(v³) all-pairs dp without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
