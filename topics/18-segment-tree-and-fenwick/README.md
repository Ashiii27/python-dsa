# Segment Tree and Fenwick Tree

**Level:** Advanced

Answer range queries with updates efficiently.

---

## What you must learn

- Prefix queries with updates
- Fenwick tree structure
- Segment tree nodes
- Range query and point update
- Lazy propagation idea
- Coordinate compression

---

## Core patterns and approaches

- Use Fenwick for prefix sums and point updates
- Use segment tree for range min/max/sum/gcd with updates
- Use lazy propagation for range updates
- Coordinate-compress large values before indexing
- Offline sort plus Fenwick can count inversions/rank relationships

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n; self.bit = [0] * (n + 1)
    def add(self, i, delta):
        i += 1
        while i <= self.n:
            self.bit[i] += delta; i += i & -i
    def prefix_sum(self, i):
        i += 1; total = 0
        while i > 0:
            total += self.bit[i]; i -= i & -i
        return total
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Fenwick or segment tree for updates and range sums. | O(log n) op | O(n) |
| [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | Coordinate compress; scan right to left with Fenwick counts. | O(n log n) | O(n) |
| [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | Fenwick/merge sort counting greater-than-twice relation. | O(n log n) | O(n) |
| [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | Hard | Line sweep with ordered map or dynamic segment tree. | O(n log C) | O(n log C) |
| [Falling Squares](https://leetcode.com/problems/falling-squares/) | Hard | Coordinate compression plus segment tree max range update. | O(n log n) | O(n) |
| [Num Array](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Classic mutable range sum with Fenwick. | O(log n) | O(n) |

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
