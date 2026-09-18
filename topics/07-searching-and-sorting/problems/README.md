# Searching And Sorting — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Dutch national flag with low/mid/high pointers. | O(n) | O(1) |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start, merge overlapping intervals. | O(n log n) | O(n) |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Quickselect average O(n) or heap O(n log k). | O(n) avg | O(1) |
| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | Sort intervals by start and check overlaps. | O(n log n) | O(1) |
| [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Medium/Hard | Median partition; arrange larger/smaller alternately. | O(n) | O(n) or O(1) |
| [Count Inversions](https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-merge-sort/) | Hard | Merge sort while counting cross inversions. | O(n log n) | O(n) |
| [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | Sort numbers by concatenation order. | O(n log n * k) | O(n) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
