# Binary Search Trees: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Every node partitions keys into strict ordered ranges. Carry ancestor bounds or exploit inorder order; balanced height gives logarithmic operations, but ordinary BSTs can become linear chains.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Valid BST nodes satisfy all ancestor bounds, not only parent comparisons. |
| 2 | Inorder traversal yields sorted keys. |
| 3 | Search/insert/delete follow one root-to-leaf path. |
| 4 | Deleting two-child nodes uses inorder successor or predecessor replacement. |
| 5 | Balanced construction chooses median roots. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need sorted rank | Inorder traversal |
| Validate ordering | Low/high bounds |
| Search by key | Iterative branch descent |
| Delete two-child node | Replace with successor |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

To validate `5 / left=1 / right=7 with left child 4`, parent-only checks pass at node 4 because `4 < 7`, but it violates root 5. Bounds catch it: node 4 inherits `(5, 7)` and fails.

## Tricks and interview notes

- Use strict inequalities unless duplicates have a defined placement rule.
- Iterative search uses O(1) auxiliary space.
- Stop inorder after the kth visit rather than traversing everything.
- A sorted array can build a height-balanced BST in O(n).

## Common mistakes

- **Watch for:** Checking only immediate children.
- **Watch for:** Assuming O(log n) without a balancing guarantee.
- **Watch for:** Losing a subtree during deletion.
- **Watch for:** Using global previous state across repeated validation calls.

## Implementation drills

1. Validate with bounds and inorder methods.
2. Implement all three deletion cases.
3. Build a balanced BST from sorted values.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/) | LeetCode | Medium |
| [BST Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | LeetCode | Medium |
| [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | LeetCode | Medium |
| [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain valid bst nodes satisfy all ancestor bounds, not only parent comparisons without notes.
- [ ] Explain inorder traversal yields sorted keys without notes.
- [ ] Explain search/insert/delete follow one root-to-leaf path without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
