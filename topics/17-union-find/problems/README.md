# Union Find — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | Union every edge and count remaining components. | O((V+E) alpha V) | O(V) |
| [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | First edge whose endpoints are already connected creates cycle. | O(E alpha V) | O(V) |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union accounts sharing emails, group by root. | O(N alpha N) | O(N) |
| [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | Union connected cities or DFS matrix. | O(n^2 alpha n) | O(n) |
| [Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | Union stones sharing row/column; answer n-components. | O(n alpha n) | O(n) |
| [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Hard | Union strings that differ in at most two positions. | O(n^2*m) | O(n) |
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal MST over all point edges. | O(E log E) | O(E) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
