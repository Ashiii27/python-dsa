# Advanced Strings: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Avoid restarting comparisons after mismatch by preprocessing reusable border information or hashing substrings. Choose deterministic algorithms when collisions are unacceptable.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | KMP prefix values encode longest proper prefix that is also a suffix. |
| 2 | Z values encode match length between a suffix and the whole string. |
| 3 | Rolling hash compares substrings after O(n) preprocessing. |
| 4 | Manacher finds all palindrome radii in O(n). |
| 5 | Trie and suffix structures serve different prefix/subsequence query needs. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Find pattern occurrences | KMP or Z |
| Compare many substrings | Rolling hash |
| Longest palindrome around centers | Expand or Manacher |
| Prefix equals suffix | Prefix/Z function |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For pattern `ababaca`, KMP fallback after mismatch does not return to zero blindly. It follows the prefix table to the longest border, reusing characters already known to match.

## Tricks and interview notes

- Use a separator absent from the alphabet when concatenating strings for KMP/Z tricks.
- Double hash or verify matches to control collision risk.
- Define whether hash intervals are inclusive or half-open.
- Start with center expansion before reaching for Manacher unless constraints demand linear time.

## Common mistakes

- **Watch for:** Building the prefix table with the search text instead of the pattern.
- **Watch for:** Incorrect KMP fallback (`j = lps[j-1]` is essential).
- **Watch for:** Assuming rolling hash is collision-free.
- **Watch for:** Ignoring Unicode/alphabet assumptions.

## Implementation drills

1. Implement prefix and Z functions from memory.
2. Find every pattern occurrence.
3. Build normalized substring hashes.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [String Matching](https://cses.fi/problemset/task/1753) | CSES | Medium |
| [Finding Borders](https://cses.fi/problemset/task/1732) | CSES | Medium |
| [String Functions](https://codeforces.com/edu/course/2/lesson/3) | Codeforces | Medium |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain kmp prefix values encode longest proper prefix that is also a suffix without notes.
- [ ] Explain z values encode match length between a suffix and the whole string without notes.
- [ ] Explain rolling hash compares substrings after o(n) preprocessing without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
