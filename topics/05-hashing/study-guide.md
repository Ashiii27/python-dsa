# Hashing: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Trade memory for fast lookup by storing the exact historical fact a future step will ask about: membership, frequency, earliest index, or canonical group key.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Sets answer existence; maps associate values with counts, indices, or objects. |
| 2 | Canonical keys turn equivalence relations into grouping problems. |
| 3 | Prefix-state maps count or locate earlier matching states. |
| 4 | A list plus index map supports average O(1) random-set operations. |
| 5 | Hash quality affects worst-case behavior, though Python handles ordinary inputs well. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need complement | Value-to-index map |
| Count occurrences | Frequency map |
| Group equivalent objects | Canonical key |
| Longest unique run | Set of values |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

In Two Sum, before reading index `i`, the map contains earlier value → index pairs. Check `target - nums[i]` first, then insert `nums[i]`; this guarantees distinct indices and returns in one pass.

## Tricks and interview notes

- Choose map values deliberately: count, latest index, earliest index, or full list.
- For lowercase anagrams, a 26-count tuple avoids sorting each word.
- Start a consecutive-sequence scan only when `x-1` is absent.
- Use immutable tuple/frozenset keys for composite state.

## Common mistakes

- **Watch for:** Overwriting an earliest index when longest length depends on it.
- **Watch for:** Using unhashable lists as keys.
- **Watch for:** Assuming iteration order is sorted order.
- **Watch for:** Forgetting frequency rather than simple membership when duplicates matter.

## Implementation drills

1. Group anagrams with two key strategies.
2. Implement RandomizedSet.
3. Count subarrays with a given prefix-state relation.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Ransom Note](https://leetcode.com/problems/ransom-note/) | LeetCode | Easy |
| [Four Sum II](https://leetcode.com/problems/4sum-ii/) | LeetCode | Medium |
| [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | LeetCode | Medium |
| [C. Registration System](https://codeforces.com/problemset/problem/4/C) | Codeforces | Easy |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain sets answer existence; maps associate values with counts, indices, or objects without notes.
- [ ] Explain canonical keys turn equivalence relations into grouping problems without notes.
- [ ] Explain prefix-state maps count or locate earlier matching states without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
