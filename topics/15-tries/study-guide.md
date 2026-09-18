# Tries: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A trie stores shared prefixes as paths. Work is proportional to key length rather than number of stored keys, making prefix lookup and lexicographic pruning natural.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Each node stores child edges and optional terminal/value metadata. |
| 2 | Insert/search/prefix operations are O(L). |
| 3 | Wildcard search branches at wildcard positions. |
| 4 | Trie-guided board DFS prunes prefixes absent from the dictionary. |
| 5 | Binary tries choose opposite bits to maximize XOR. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Many prefix queries | Character trie |
| Dictionary + grid search | Trie-pruned DFS |
| Wildcard word lookup | Trie DFS branching |
| Maximum XOR | Binary trie |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Insert `cat` and `car`: paths `c → a` are shared, then branch to `t` and `r`. Mark both final nodes terminal; without terminal markers, searching `ca` would incorrectly report a full word.

## Tricks and interview notes

- Store terminal words at nodes to avoid rebuilding paths during DFS.
- Delete found words or prune empty branches to reduce repeated work.
- Use arrays for fixed alphabets and maps for sparse/general alphabets.
- Track prefix aggregates with deltas when keys can be updated.

## Common mistakes

- **Watch for:** Treating every prefix as a complete word.
- **Watch for:** Exponential wildcard search without pruning.
- **Watch for:** Duplicating common prefixes in memory-heavy structures.
- **Watch for:** Forgetting cleanup of board visited state.

## Implementation drills

1. Implement insert/search/startsWith.
2. Add wildcard matching.
3. Build a binary trie for fixed-width integers.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Contacts](https://www.hackerrank.com/challenges/contacts/problem) | HackerRank | Medium |
| [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | LeetCode | Medium |
| [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) | LeetCode | Medium |
| [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain each node stores child edges and optional terminal/value metadata without notes.
- [ ] Explain insert/search/prefix operations are o(l) without notes.
- [ ] Explain wildcard search branches at wildcard positions without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
