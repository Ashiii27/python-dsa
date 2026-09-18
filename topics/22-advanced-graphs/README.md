# Advanced Graphs

**Level:** Advanced

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
| Network Delay Time | Medium | Dijkstra from source over directed weighted graph. | O(E log V) | O(V+E) |
| Cheapest Flights Within K Stops | Medium | Bellman-Ford style k+1 relaxations or stateful Dijkstra. | O(K E) | O(V) |
| Min Cost to Connect All Points | Medium | MST using Prim or Kruskal. | O(E log V) | O(E) |
| Critical Connections in a Network | Hard | Tarjan bridge-finding with discovery and low times. | O(V+E) | O(V+E) |
| Reconstruct Itinerary | Hard | Hierholzer DFS with lexical min-heaps. | O(E log E) | O(E) |
| Swim in Rising Water | Hard | Dijkstra/minimax path or binary search + BFS. | O(n^2 log n) | O(n^2) |
| Find the City With Smallest Number of Neighbors | Medium | Floyd-Warshall or Dijkstra from each city. | O(V^3) | O(V^2) |

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
