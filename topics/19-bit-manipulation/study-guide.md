# Bit Manipulation: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

View integers as fixed-width sets of binary positions. XOR captures parity/difference, masks select subsets or fields, and lowbit isolates the least significant set bit.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | AND tests/clears bits; OR sets bits; XOR toggles and cancels pairs. |
| 2 | `x & (x-1)` removes the lowest set bit. |
| 3 | `x & -x` isolates the lowest set bit. |
| 4 | Subsets of n items correspond to masks 0 through 2^n-1. |
| 5 | Python negative integers require explicit masking for fixed-width emulation. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Pairs cancel, one remains | XOR |
| Enumerate small-n subsets | Bitmask |
| State is a small set | Bitmask DP |
| Need per-bit counts | Scan fixed bit positions |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

`12 = 1100₂`. Then `12 & 11 = 1100 & 1011 = 1000`, removing one set bit. Repeating until zero counts set bits in time proportional to the number of ones.

## Tricks and interview notes

- Use `(mask >> bit) & 1` for a readable membership test.
- Parenthesize bit expressions; precedence is easy to misread.
- For 32-bit answers in Python, mask with `0xFFFFFFFF`.
- XOR prefix arrays answer range XOR exactly like sum prefixes.

## Common mistakes

- **Watch for:** Assuming right shift of a negative Python integer inserts zeros.
- **Watch for:** Using floating `log2` to locate bits.
- **Watch for:** Confusing XOR with exponentiation (`**` is exponentiation in Python).
- **Watch for:** Ignoring exponential 2^n mask count.

## Implementation drills

1. Implement popcount three ways.
2. Enumerate submasks of a mask.
3. Solve single-number variants using per-bit reasoning.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Hamming Distance](https://leetcode.com/problems/hamming-distance/) | LeetCode | Easy |
| [Bit Strings](https://cses.fi/problemset/task/1617) | CSES | Easy |
| [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | LeetCode | Medium |
| [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain and tests/clears bits; or sets bits; xor toggles and cancels pairs without notes.
- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
