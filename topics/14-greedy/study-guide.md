# Greedy Algorithms: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Make a locally best irreversible choice only after proving an optimal solution can be transformed to include it. Sorting often exposes the safe choice.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Exchange arguments replace an optimal solution’s first differing choice. |
| 2 | Stays-ahead proofs compare every prefix of greedy and optimal solutions. |
| 3 | Earliest finishing interval maximizes the room left for future choices. |
| 4 | Farthest-reach scans compress BFS-like layers. |
| 5 | Global feasibility can coexist with local resets, as in Gas Station. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Max non-overlapping intervals | Sort by end |
| Pair extremes | Sort + two pointers |
| Reachability | Track farthest index |
| Need repeated best available choice | Heap-based greedy |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For interval scheduling, choose the compatible interval with earliest end. If an optimum first chooses a later-ending interval, swapping in the greedy interval cannot invalidate any later selected interval and leaves at least as much room.

## Tricks and interview notes

- State the greedy choice and its proof separately.
- Try sorting by start, end, value, or ratio and search for a counterexample.
- A heap can choose the current best while a sorted pointer releases candidates.
- Greedy may compute feasibility even when DP computes optimum.

## Common mistakes

- **Watch for:** Assuming a plausible heuristic is a proof.
- **Watch for:** Sorting by start when earliest end is required.
- **Watch for:** Ignoring ties that affect feasibility.
- **Watch for:** Using greedy for 0/1 knapsack by value/weight ratio.

## Implementation drills

1. Write an exchange proof for interval scheduling.
2. Derive Jump Game II as layers.
3. Find a counterexample to a wrong coin-change greedy rule.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Movie Festival](https://cses.fi/problemset/task/1629) | CSES | Medium |
| [Tasks and Deadlines](https://cses.fi/problemset/task/1630) | CSES | Medium |
| [Ferris Wheel](https://cses.fi/problemset/task/1090) | CSES | Medium |
| [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) | LeetCode | Easy |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain exchange arguments replace an optimal solution’s first differing choice without notes.
- [ ] Explain stays-ahead proofs compare every prefix of greedy and optimal solutions without notes.
- [ ] Explain earliest finishing interval maximizes the room left for future choices without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
