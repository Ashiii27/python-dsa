# Segment Tree And Fenwick — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Fenwick or segment tree for updates and range sums. | O(log n) op | O(n) |
| [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | Coordinate compress; scan right to left with Fenwick counts. | O(n log n) | O(n) |
| [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | Fenwick/merge sort counting greater-than-twice relation. | O(n log n) | O(n) |
| [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | Hard | Line sweep with ordered map or dynamic segment tree. | O(n log C) | O(n log C) |
| [Falling Squares](https://leetcode.com/problems/falling-squares/) | Hard | Coordinate compression plus segment tree max range update. | O(n log n) | O(n) |
| [Num Array](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Classic mutable range sum with Fenwick. | O(log n) | O(n) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
