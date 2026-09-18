# Design Data Structures: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Start from required operation bounds, then compose structures whose strengths cover each other’s weaknesses. Write invariants linking every index, map entry, list node, and counter.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Map + doubly linked list gives O(1) keyed recency updates for LRU. |
| 2 | Array + index map gives O(1) average insert/delete/random access. |
| 3 | Two heaps plus lazy deletion maintain dynamic medians. |
| 4 | Timestamped append-only lists support binary-search history queries. |
| 5 | Frequency buckets combine count ordering with recency for LFU. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| O(1) lookup + ordering | Map + doubly linked list |
| O(1) random set | Array + index map |
| Historical value by time | Map + sorted histories |
| Frequency then recency eviction | Maps + frequency lists |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

RandomizedSet deletion: find index `i`, move the last value into `i`, update that value’s map entry, pop the list, then remove the deleted key. The map and array remain exact inverses.

## Tricks and interview notes

- Write the representation invariant before methods.
- Use dummy head/tail nodes to simplify linked-list moves.
- Define behavior for zero capacity and duplicate operations.
- Separate public API logic from private structure-maintenance helpers.

## Common mistakes

- **Watch for:** Updating one structure but not its companion.
- **Watch for:** Using linear list removal in an allegedly O(1) API.
- **Watch for:** Ignoring tie-breaking requirements.
- **Watch for:** Failing to remove empty LFU frequency buckets or update minimum frequency.

## Implementation drills

1. Implement LRU without `OrderedDict`.
2. Implement RandomizedSet and property-test its invariant.
3. Implement TimeMap with `bisect`.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | LeetCode | Medium |
| [Design Authentication Manager](https://leetcode.com/problems/design-authentication-manager/) | LeetCode | Medium |
| [Design Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/) | LeetCode | Medium |
| [Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain map + doubly linked list gives o(1) keyed recency updates for lru without notes.
- [ ] Explain array + index map gives o(1) average insert/delete/random access without notes.
- [ ] Explain two heaps plus lazy deletion maintain dynamic medians without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
