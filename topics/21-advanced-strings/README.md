# Advanced Strings

**Level:** Advanced

Use linear-time string algorithms for matching, borders, repeated patterns, and substring comparison.

---

## What you must learn

- KMP prefix function
- Z algorithm
- Rolling hash / Rabin-Karp
- String borders
- Palindrome expansion/Manacher idea
- Suffix array/tree concepts

---

## Core patterns and approaches

- Use KMP when searching a pattern without backing up text pointer
- Use Z array for prefix matches at each position
- Use rolling hash for many substring comparisons with collision awareness
- Use borders to detect repeated patterns
- For palindrome-heavy problems, choose expand-around-center, DP, or Manacher based on constraints

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def prefix_function(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Implement strStr | Easy | KMP or built-in for practice; KMP is linear. | O(n+m) | O(m) |
| Repeated Substring Pattern | Easy | Use prefix function or string trick. | O(n) | O(n) |
| Longest Happy Prefix | Hard | Last value of KMP prefix table gives longest border. | O(n) | O(n) |
| Repeated DNA Sequences | Medium | Rolling hash or fixed-length substring set. | O(n) | O(n) |
| Shortest Palindrome | Hard | KMP on s + separator + reverse(s). | O(n) | O(n) |
| Longest Palindromic Substring | Medium | Expand around centers or Manacher. | O(n^2) or O(n) | O(1) or O(n) |
| Distinct Echo Substrings | Hard | Rolling hash compare adjacent equal-length substrings. | O(n^2) | O(n^2) set |

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
