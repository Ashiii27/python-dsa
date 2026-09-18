# Advanced Graphs

**Level:** Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Go beyond BFS/DFS into weighted shortest paths, MSTs, SCCs, bridges, and advanced connectivity.

---

## What you must learn

- Dijkstra
- Bellman-Ford
- Floyd-Warshall
- Minimum spanning tree
- Kruskal and Prim
- Strongly connected components
- Bridges and articulation points
- Euler path basics

---

## Core patterns and approaches

- Use Dijkstra for nonnegative weights
- Use Bellman-Ford for negative edges or limited stops
- Use Floyd-Warshall for small all-pairs shortest path
- Use Kruskal with DSU for MST
- Use Tarjan low-link values for bridges
- Use Hierholzer for itinerary/Euler path style problems

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
import heapq

def dijkstra(graph, source):
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d != dist[node]: continue
        for nei, w in graph.get(node, []):
            nd = d + w
            if nd < dist.get(nei, float('inf')):
                dist[nei] = nd
                heapq.heappush(heap, (nd, nei))
    return dist
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra from source over directed weighted graph. | O(E log V) | O(V+E) |
| [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford style k+1 relaxations or stateful Dijkstra. | O(K E) | O(V) |
| [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | MST using Prim or Kruskal. | O(E log V) | O(E) |
| [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Tarjan bridge-finding with discovery and low times. | O(V+E) | O(V+E) |
| [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Hierholzer DFS with lexical min-heaps. | O(E log E) | O(E) |
| [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Dijkstra/minimax path or binary search + BFS. | O(n^2 log n) | O(n^2) |
| [Find the City With Smallest Number of Neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Floyd-Warshall or Dijkstra from each city. | O(V^3) | O(V^2) |

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
