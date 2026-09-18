# Stacks and Queues: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A stack resolves nested or “most recent unresolved” relationships; a queue processes states in arrival or distance order. Monotonic variants retain only candidates that can still matter.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Stacks are LIFO and naturally model parsing, undo, and DFS. |
| 2 | Queues are FIFO and naturally model BFS and scheduling. |
| 3 | Monotonic stacks find next/previous greater or smaller boundaries. |
| 4 | Monotonic deques maintain a window optimum. |
| 5 | Two stacks can reverse order to implement a queue. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Nested delimiters | Stack |
| Next greater/smaller | Monotonic stack |
| Shortest unweighted steps | Queue/BFS |
| Window maximum | Monotonic deque |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For temperatures `[73, 71, 75]`, push indices 0 and 1 on a decreasing stack. At 75, pop 1 and 0: waits are `2-1=1` and `2-0=2`. Every index is pushed and popped once, so the scan is O(n).

## Tricks and interview notes

- Store indices when answers depend on distance or width.
- Add a sentinel bar of height zero to flush a histogram stack.
- For RPN, preserve operand order: second pop is the left operand.
- In a monotonic deque, remove expired indices before reading the front.

## Common mistakes

- **Watch for:** Using a stack of values when duplicate indices matter.
- **Watch for:** Marking BFS nodes visited only when dequeued.
- **Watch for:** Using floating division instead of truncation toward zero in RPN.
- **Watch for:** Forgetting width boundaries after popping a histogram bar.

## Implementation drills

1. Implement a queue with two stacks.
2. Derive next-greater element in both directions.
3. Implement a min stack with paired minima.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Alternating Current](https://codeforces.com/problemset/problem/343/B) | Codeforces | Easy |
| [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | LeetCode | Medium |
| [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | LeetCode | Medium |
| [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain stacks are lifo and naturally model parsing, undo, and dfs without notes.
- [ ] Explain queues are fifo and naturally model bfs and scheduling without notes.
- [ ] Explain monotonic stacks find next/previous greater or smaller boundaries without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
