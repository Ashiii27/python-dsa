# Hashing — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

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

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
