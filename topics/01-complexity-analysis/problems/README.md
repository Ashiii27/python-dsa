# Complexity Analysis — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Two Sum Brute Force](https://leetcode.com/problems/two-sum/) | Easy | Two nested loops over all pairs. | O(n^2) | O(1) |
| [Two Sum with Hash Map](https://leetcode.com/problems/two-sum/) | Easy | One pass storing seen values or complements. | O(n) | O(n) |
| [Merge Sort Analysis](https://en.wikipedia.org/wiki/Merge_sort) | Medium | Use T(n)=2T(n/2)+O(n). | O(n log n) | O(n) |
| [Binary Search Analysis](https://leetcode.com/problems/binary-search/) | Easy | Search space halves each step. | O(log n) | O(1) |
| [Naive Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Repeated branching calls create exponential tree. | O(2^n) | O(n) |
| [Memoized Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Each state 0..n computed once. | O(n) | O(n) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
