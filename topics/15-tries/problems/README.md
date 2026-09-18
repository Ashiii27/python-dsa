# Tries — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Nested nodes with children map and end marker. | O(L) per op | O(total chars) |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie of words plus board DFS with pruning. | O(mn*4^L) worst | O(total chars) |
| [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie plus DFS branching on wildcard dot. | O(26^dots * L) | O(total chars) |
| [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | Find shortest root prefix in trie for each word. | O(total chars) | O(dict chars) |
| [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | Trie nodes store prefix sums or deltas. | O(L) per op | O(total chars) |
| [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Binary trie; greedily choose opposite bit. | O(n*bits) | O(n*bits) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
