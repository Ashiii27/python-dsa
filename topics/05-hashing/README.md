# Hashing

**Level:** Core

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Use dictionaries and sets for fast lookup, counting, grouping, canonicalization, and prefix relationships.

---

## What you must learn

- Hash tables
- Sets vs dictionaries
- Frequency maps
- Canonical keys
- Prefix maps
- Collision intuition
- Mutable vs immutable keys

---

## Core patterns and approaches

- Use complement lookup for pair-sum problems
- Use frequency counts for anagrams and multiset comparisons
- Use canonical representations to group equivalent structures
- Use prefix sum counts for subarray sum problems
- Use sets for visited states and duplicate detection

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Compare list length with set length, or scan with seen set. | O(n) | O(n) |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Compare character counts. | O(n) | O(k) |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Use sorted word or 26-count tuple as canonical key. | O(n*k log k) | O(nk) |
| [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Only start counting at sequence starts in a set. | O(n) | O(n) |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count frequencies then heap or bucket sort. | O(n log k) or O(n) | O(n) |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Prefix sum count map tracks previous prefixes. | O(n) | O(n) |
| [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | Maintain two maps or map pairs consistently. | O(n) | O(k) |
| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | List plus map value to index; swap-delete. | O(1) avg | O(n) |

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
