# Binary Search — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Compare middle with target and discard half. | O(log n) | O(1) |
| [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | Find first true predicate. | O(log n) | O(1) |
| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Lower bound for target. | O(log n) | O(1) |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Identify sorted half and decide where target can be. | O(log n) | O(1) |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare mid with right to locate pivot/minimum. | O(log n) | O(1) |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary search speed; feasible if hours <= h. | O(n log M) | O(1) |
| [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Binary search capacity and simulate days. | O(n log sum) | O(1) |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | Binary search max subarray sum; greedily count partitions. | O(n log sum) | O(1) |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Binary search partition in smaller array. | O(log min(n,m)) | O(1) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
