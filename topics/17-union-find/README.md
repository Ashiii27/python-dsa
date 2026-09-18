# Union Find / Disjoint Set Union

**Level:** Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Maintain dynamic connected components with near-constant-time union and find.

---

## What you must learn

- Parent array
- Path compression
- Union by rank/size
- Connected components
- Cycle detection
- Kruskal minimum spanning tree
- DSU on grids/accounts

---

## Core patterns and approaches

- Use DSU for undirected connectivity with many union queries
- Cycle exists if an edge connects two nodes already in same set
- Components decrease when union merges two roots
- For account merging, union accounts sharing an email
- Kruskal sorts edges then unions if endpoints are separate

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)); self.size = [1] * n; self.components = n
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False
        if self.size[ra] < self.size[rb]: ra, rb = rb, ra
        self.parent[rb] = ra; self.size[ra] += self.size[rb]; self.components -= 1
        return True
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | Union every edge and count remaining components. | O((V+E) alpha V) | O(V) |
| [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | First edge whose endpoints are already connected creates cycle. | O(E alpha V) | O(V) |
| [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union accounts sharing emails, group by root. | O(N alpha N) | O(N) |
| [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | Union connected cities or DFS matrix. | O(n^2 alpha n) | O(n) |
| [Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | Union stones sharing row/column; answer n-components. | O(n alpha n) | O(n) |
| [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Hard | Union strings that differ in at most two positions. | O(n^2*m) | O(n) |
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal MST over all point edges. | O(E log E) | O(E) |

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
