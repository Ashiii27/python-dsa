# Graphs — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

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

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
