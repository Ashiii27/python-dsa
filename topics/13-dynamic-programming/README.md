# Dynamic Programming

**Level:** Core to Advanced

Turn repeated subproblems into states, transitions, and ordered computation.

---

## What you must learn

- Memoization vs tabulation
- State definition
- Transitions and base cases
- 1D and 2D DP
- Knapsack
- LIS
- String DP
- Interval DP
- Bitmask DP
- Tree DP

---

## Core patterns and approaches

- If recursion repeats states, memoize
- Define state in one sentence before writing recurrence
- Tabulation requires computing dependencies first
- Compress memory only after recurrence is correct
- For optimization DP, decide whether state stores best value, count, or boolean feasibility

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def coin_change(coins, amount):
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if a >= c:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == INF else dp[amount]
```

---

## Top interview questions and approaches

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
