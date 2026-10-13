# Tries

**Level:** Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Store strings by prefixes for fast prefix lookup, dictionary pruning, and bitwise branching.

---

## What you must learn

- Trie nodes
- Word-ending markers
- Prefix search
- Wildcard DFS
- Compressed trie idea
- Binary trie for XOR

---

## Core patterns and approaches

- Use trie when many prefix queries share work
- For word search, build trie and DFS board with pruning
- For wildcard dot, branch over children
- For maximum XOR, walk opposite bits when possible
- Store counts to support deletion or prefix frequencies

---

## Python notes

- `is_word` is what separates a stored word from a prefix of another word.
- Store counts on nodes to answer "how many words start with P" in O(len P).
- `node.children.setdefault(ch, TrieNode())` keeps insertion short and readable.
- Nested dicts are a compact alternative when the alphabet is small and you do not need counts.

Runnable builds, step-by-step walkthroughs and solved examples live in **Python implementation (build it from scratch)** in the [complete study guide](study-guide.md).

---

## Canonical template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self): self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Nested nodes with children map and end marker. | O(L) per op | O(total chars) |
| [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie of words plus board DFS with pruning. | O(mn*4^L) worst | O(total chars) |
| [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie plus DFS branching on wildcard dot. | O(26^dots * L) | O(total chars) |
| [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | Find shortest root prefix in trie for each word. | O(total chars) | O(dict chars) |
| [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | Trie nodes store prefix sums or deltas. | O(L) per op | O(total chars) |
| [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Binary trie; greedily choose opposite bit. | O(n*bits) | O(n*bits) |

---

## Mastery checklist

- [ ] I can explain the main idea without looking at notes.
- [ ] I can implement the canonical template from memory.
- [ ] I can solve the easy problems in under 10 minutes each.
- [ ] I can solve most medium problems in 20-35 minutes.
- [ ] I can explain brute force, optimized approach, proof idea, and complexity.
- [ ] I can identify edge cases before coding.

---

## Next steps

1. Read the related sections in [`docs/patterns-cheatsheet.md`](../../docs/patterns-cheatsheet.md).
2. Implement the relevant template from [`templates/python_dsa_templates.py`](../../templates/python_dsa_templates.py) without looking.
3. Add solved problems and mistakes to [`practice/study-tracker.md`](../../practice/study-tracker.md).
4. Browse the topic [`problems/`](problems/README.md) index for prompt links and worked solutions.
