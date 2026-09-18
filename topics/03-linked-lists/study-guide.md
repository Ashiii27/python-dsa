# Linked Lists: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Reason about links, not positions. Before changing a pointer, preserve every node that must remain reachable; dummy nodes remove head-specific branches.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Singly linked nodes support O(1) insertion after a known node. |
| 2 | Fast/slow pointers encode relative speed for cycles and midpoints. |
| 3 | In-place reversal maintains previous, current, and saved-next pointers. |
| 4 | A dummy head gives the first real node a predecessor. |
| 5 | Merging and partitioning are repeated tail-attachment operations. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Cycle or midpoint | Fast/slow pointers |
| Head may change | Dummy node |
| Process from the end | Gap pointers or reversal |
| Merge ordered chains | Dummy tail |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

```text
Before: prev <- current -> next
Save:   after = current.next
Flip:   current.next = prev
Move:   prev = current; current = after
```
The unprocessed suffix remains reachable through `after`, while `prev` is always the fully reversed prefix.

## Tricks and interview notes

- Draw arrows for a three-node example before coding.
- Use identity (`is`) when comparing nodes, not equality of values.
- For kth from end, keep two pointers exactly k nodes apart.
- When merging, attach the untouched remainder after one list ends.

## Common mistakes

- **Watch for:** Losing the suffix by reversing before saving `next`.
- **Watch for:** Dereferencing `fast.next` without checking `fast`.
- **Watch for:** Creating accidental cycles during reorder operations.
- **Watch for:** Forgetting that recursive reversal uses O(n) stack space.

## Implementation drills

1. Reverse iteratively and recursively.
2. Find and split at the midpoint.
3. Merge two sorted chains with a dummy node.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | LeetCode | Easy |
| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | LeetCode | Easy |
| [Partition List](https://leetcode.com/problems/partition-list/) | LeetCode | Medium |
| [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain singly linked nodes support o(1) insertion after a known node without notes.
- [ ] Explain fast/slow pointers encode relative speed for cycles and midpoints without notes.
- [ ] Explain in-place reversal maintains previous, current, and saved-next pointers without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
