# Intervals And Line Sweep — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start and merge overlaps. | O(n log n) | O(n) |
| [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Add all before, merge overlapping, then add after. | O(n) | O(n) |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Sort starts and use min-heap of end times. | O(n log n) | O(n) |
| [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | Check if new interval overlaps existing intervals. | O(n) | O(n) |
| [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Merge all busy intervals, gaps are free time. | O(n log n) | O(n) |
| [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | Difference array or sorted pickup/drop events. | O(n log n) or O(U) | O(n or U) |
| [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | Sweep events with max-heap and lazy deletion. | O(n log n) | O(n) |
| [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end and greedily shoot arrows. | O(n log n) | O(1) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
