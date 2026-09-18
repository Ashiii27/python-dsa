# Advanced Strings — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Implement strStr](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy | KMP or built-in for practice; KMP is linear. | O(n+m) | O(m) |
| [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | Use prefix function or string trick. | O(n) | O(n) |
| [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | Hard | Last value of KMP prefix table gives longest border. | O(n) | O(n) |
| [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Medium | Rolling hash or fixed-length substring set. | O(n) | O(n) |
| [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | Hard | KMP on s + separator + reverse(s). | O(n) | O(n) |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand around centers or Manacher. | O(n^2) or O(n) | O(1) or O(n) |
| [Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings/) | Hard | Rolling hash compare adjacent equal-length substrings. | O(n^2) | O(n^2) set |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
