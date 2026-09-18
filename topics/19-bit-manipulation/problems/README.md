# Bit Manipulation — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR all numbers; duplicates cancel. | O(n) | O(1) |
| [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | dp[i]=dp[i>>1]+(i&1). | O(n) | O(n) |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | Shift result and consume input bits. | O(bits) | O(1) |
| [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | XOR indices and values, or use sum formula. | O(n) | O(1) |
| [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | Use XOR for sum and AND-shift for carry. | O(bits) | O(1) |
| [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Greedy prefix set or binary trie. | O(n*bits) | O(n) |
| [Subsets via Bitmask](https://leetcode.com/problems/subsets/) | Medium | Enumerate masks from 0 to 2^n-1. | O(n*2^n) | O(n) |
| [Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | Hard | Bitmask DP over last string and used set. | O(n^2*2^n) | O(n*2^n) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
