# Advanced Graphs — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra from source over directed weighted graph. | O(E log V) | O(V+E) |
| [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford style k+1 relaxations or stateful Dijkstra. | O(K E) | O(V) |
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | MST using Prim or Kruskal. | O(E log V) | O(E) |
| [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Tarjan bridge-finding with discovery and low times. | O(V+E) | O(V+E) |
| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Hierholzer DFS with lexical min-heaps. | O(E log E) | O(E) |
| [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Dijkstra/minimax path or binary search + BFS. | O(n^2 log n) | O(n^2) |
| [Find the City With Smallest Number of Neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Floyd-Warshall or Dijkstra from each city. | O(V^3) | O(V^2) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
