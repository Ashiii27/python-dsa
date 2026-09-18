# Trees and Binary Trees: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Recursive structure suggests recursive contracts: decide what one subtree returns and how a node combines child results. Iterative traversals make the same pending work explicit in a stack or queue.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Preorder processes node before children; inorder between; postorder after. |
| 2 | BFS processes levels and exposes shortest edge distance from the root. |
| 3 | Height, balance, and diameter are postorder combinations. |
| 4 | Path problems distinguish downward return values from complete global candidates. |
| 5 | Serialization must preserve null structure, not only values. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Combine child facts | Postorder DFS |
| Level-by-level output | BFS |
| Root-to-leaf state | Preorder DFS |
| Ancestor/path query | Recursive return contract |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For diameter, each node receives left and right heights. `left + right` is the best path passing through that node; return `1 + max(left, right)` because a parent can extend only one branch.

## Tricks and interview notes

- State whether height counts nodes or edges.
- Use a deque for level-order traversal.
- Pass prefix state down; undo map counts when returning from DFS.
- Iterative postorder can use `(node, visited)` pairs.

## Common mistakes

- **Watch for:** Returning the global path candidate to a parent instead of a one-branch value.
- **Watch for:** Ignoring recursion depth on a skewed tree.
- **Watch for:** Reconstructing from traversals when values are not unique.
- **Watch for:** Serializing without null markers.

## Implementation drills

1. Implement all three DFS orders recursively and iteratively.
2. Compute height and diameter in one traversal.
3. Serialize and deserialize a sparse tree.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Tree Diameter](https://cses.fi/problemset/task/1131) | CSES | Medium |
| [Subordinates](https://cses.fi/problemset/task/1674) | CSES | Medium |
| [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | LeetCode | Hard |
| [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain preorder processes node before children; inorder between; postorder after without notes.
- [ ] Explain bfs processes levels and exposes shortest edge distance from the root without notes.
- [ ] Explain height, balance, and diameter are postorder combinations without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
