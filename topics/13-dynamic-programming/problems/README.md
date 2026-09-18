# Dynamic Programming — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | dp[i]=dp[i-1]+dp[i-2]. | O(n) | O(1) |
| [House Robber](https://leetcode.com/problems/house-robber/) | Medium | At each house choose rob or skip. | O(n) | O(1) |
| [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | dp[amount] is min coins to form amount. | O(amount*coins) | O(amount) |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Patience tails array with binary search. | O(n log n) | O(n) |
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D DP over prefixes. | O(nm) | O(nm) |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | Hard | Insert/delete/replace transition over prefixes. | O(nm) | O(nm) |
| [Word Break](https://leetcode.com/problems/word-break/) | Medium | dp[i] true if a valid word ends at i. | O(n^2) | O(n) |
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | Ways to decode prefix i from one/two-digit endings. | O(n) | O(1) |
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 knapsack for target sum/2. | O(n*target) | O(target) |
| [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | Interval DP choosing last balloon in interval. | O(n^3) | O(n^2) |
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | String DP with dot and star transitions. | O(nm) | O(nm) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
