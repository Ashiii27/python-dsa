# Greedy — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Track farthest reachable index. | O(n) | O(1) |
| [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | BFS-layer style greedy over current range. | O(n) | O(1) |
| [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | If total gas sufficient, reset start when tank goes negative. | O(n) | O(1) |
| [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end and keep intervals finishing earliest. | O(n log n) | O(1) |
| [Candy](https://leetcode.com/problems/candy/) | Hard | Two passes satisfy left and right neighbor constraints. | O(n) | O(n) |
| [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Use last occurrence to close partitions greedily. | O(n) | O(1) |
| [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | Sort taller first, insert by k. | O(n^2) | O(n) |
| [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end; shoot arrow at current end. | O(n log n) | O(1) |
| [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | Sort weights; pair lightest with heaviest when possible. | O(n log n) | O(1) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
