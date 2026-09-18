# Graphs

**Level:** Core to Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Model relationships with nodes and edges; solve traversal, connectivity, ordering, and shortest-step problems.

---

## What you must learn

- Adjacency list/matrix
- Directed vs undirected graphs
- Weighted vs unweighted graphs
- DFS and BFS
- Visited state
- Connected components
- Cycle detection
- Topological sort
- Grid graphs

---

## Core patterns and approaches

- Use DFS/BFS for components and reachability
- Use BFS for shortest path in unweighted graphs
- Use topological sort for prerequisites/dependencies
- Use coloring for bipartite checks
- For grid problems, treat each cell as a node

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
from collections import deque

def bfs(start, graph):
    seen, q, order = {start}, deque([start]), []
    while q:
        node = q.popleft(); order.append(node)
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei); q.append(nei)
    return order
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | DFS/BFS flood fill every unvisited land cell. | O(mn) | O(mn) |
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | DFS/BFS with map original node to clone. | O(V+E) | O(V) |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Topological sort or DFS cycle detection. | O(V+E) | O(V+E) |
| [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Reverse search from both oceans and intersect reachability. | O(mn) | O(mn) |
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS from all rotten oranges. | O(mn) | O(mn) |
| [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | BFS over wildcard-pattern neighbors. | O(N*L^2) | O(N*L) |
| [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | Check edges n-1 and connectivity, or DSU no cycle. | O(V+E) | O(V+E) |
| [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | Build character graph from adjacent words and topologically sort. | O(total chars) | O(1) to O(k) |

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
