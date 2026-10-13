# Advanced Graphs: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Advanced graph algorithms refine traversal with a stronger invariant: finalized shortest distance, safe relaxation count, low-link reachability, or cut/component structure.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Dijkstra finalizes smallest tentative distances with non-negative edges. |
| 2 | Bellman-Ford relaxes all edges and handles negatives/cycle detection. |
| 3 | Floyd-Warshall is O(V³) all-pairs DP. |
| 4 | Tarjan low-link values identify bridges, articulation points, and SCC structure. |
| 5 | Prim and Kruskal construct MSTs using cut safety. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Non-negative weighted shortest path | Dijkstra |
| Negative edges or bounded flights | Bellman-Ford |
| Connect all nodes cheaply | MST |
| Critical edge/component | Low-link DFS |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Dijkstra heap entries may become stale. When `(distance,node)` is popped, skip it if it differs from the current best distance. Non-negative edges guarantee the first non-stale pop finalizes that shortest distance.

## Tricks and interview notes

- Store adjacency as `(weight, neighbor)` consistently.
- Use infinity rather than an arbitrary large number.
- In bridge DFS, skip only the parent edge id when parallel edges can exist.
- Choose Prim for implicit dense graphs and Kruskal for sortable edge lists.

## Common mistakes

- **Watch for:** Using Dijkstra with negative edges.
- **Watch for:** Marking a Dijkstra node visited when pushed.
- **Watch for:** Confusing MST with a shortest-path tree.
- **Watch for:** Updating low-link incorrectly across tree versus back edges.

## Implementation drills

1. Implement Dijkstra with stale-entry skipping.
2. Implement Kruskal with DSU.
3. Find bridges and test parallel-edge behavior.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Shortest paths: Dijkstra, Bellman-Ford, Floyd-Warshall

Choose by the weights: non-negative → Dijkstra (O((V + E) log V)); negative
weights allowed → Bellman-Ford (O(V · E), also detects negative cycles); all-pairs
on a small graph → Floyd-Warshall (O(V³)).

```python
import heapq
from math import inf


def dijkstra(graph, source):
    """Shortest distances from `source`. Weights must be non-negative.

    graph: node -> iterable of (neighbour, weight)
    """
    dist = {source: 0}
    heap = [(0, source)]
    settled = set()
    while heap:
        d, node = heapq.heappop(heap)
        if node in settled:                       # stale heap entry
            continue
        settled.add(node)                         # first pop = final distance
        for neighbour, weight in graph.get(node, []):
            candidate = d + weight
            if candidate < dist.get(neighbour, inf):
                dist[neighbour] = candidate
                heapq.heappush(heap, (candidate, neighbour))
    return dist


def dijkstra_with_paths(graph, source):
    """Distances plus the predecessor map, so you can rebuild the paths."""
    dist = {source: 0}
    parent = {source: None}
    heap = [(0, source)]
    settled = set()
    while heap:
        d, node = heapq.heappop(heap)
        if node in settled:
            continue
        settled.add(node)
        for neighbour, weight in graph.get(node, []):
            candidate = d + weight
            if candidate < dist.get(neighbour, inf):
                dist[neighbour] = candidate
                parent[neighbour] = node
                heapq.heappush(heap, (candidate, neighbour))
    return dist, parent


def bellman_ford(node_count, edges, source):
    """Negative weights allowed. Returns (distances, has_negative_cycle).

    edges: iterable of (u, v, weight)
    """
    dist = [inf] * node_count
    dist[source] = 0
    for _ in range(node_count - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:                           # already converged
            break
    negative_cycle = any(dist[u] + w < dist[v] for u, v, w in edges)
    return dist, negative_cycle


def floyd_warshall(node_count, edges):
    """All-pairs shortest paths: dist[i][j] for every pair. O(V^3)."""
    dist = [[inf] * node_count for _ in range(node_count)]
    for i in range(node_count):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)
    for k in range(node_count):
        for i in range(node_count):
            dik = dist[i][k]
            if dik == inf:
                continue
            for j in range(node_count):
                if dik + dist[k][j] < dist[i][j]:
                    dist[i][j] = dik + dist[k][j]
    return dist


if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    print("dijkstra from 0:", dijkstra(graph, 0))
    dist, parent = dijkstra_with_paths(graph, 0)
    node, path = 3, []
    while node is not None:
        path.append(node)
        node = parent[node]
    print("path 0 -> 3:", path[::-1], "| cost:", dist[3])

    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    distances, negative = bellman_ford(4, edges, 0)
    print("bellman_ford:", distances, "| negative cycle:", negative)

    negative_edges = [(0, 1, 1), (1, 2, -3), (2, 0, 1)]
    print("with a negative cycle:", bellman_ford(3, negative_edges, 0))

    all_pairs = floyd_warshall(4, edges)
    print("floyd_warshall row 0:", all_pairs[0])
    print("floyd_warshall dist(0, 3):", all_pairs[0][3])
    print("unreachable stays infinite:", floyd_warshall(2, [])[0][1])
```

Output:

```text
dijkstra from 0: {0: 0, 1: 3, 2: 1, 3: 4}
path 0 -> 3: [0, 2, 1, 3] | cost: 4
bellman_ford: [0, 3, 1, 4] | negative cycle: False
with a negative cycle: ([-2, 0, -3], True)
floyd_warshall row 0: [0, 3, 1, 4]
floyd_warshall dist(0, 3): 4
unreachable stays infinite: inf
```

**How it works**

- Dijkstra is greedy with a proof: once the smallest tentative distance is popped, no later path can beat it (all weights are ≥ 0). The `settled` set skips stale heap entries instead of using a decrease-key operation.
- With negative weights Dijkstra's proof breaks — that is exactly what Bellman-Ford fixes by relaxing every edge `V − 1` times. One extra pass that still improves something proves a negative cycle exists.
- Floyd-Warshall is three nested loops with `k` outermost: after processing `k`, `dist[i][j]` may route through nodes `0..k`. The `k` loop must be first, or the invariant is wrong.
- For unweighted graphs use plain BFS (O(V + E)); Dijkstra on unit weights is an unnecessary log factor.

### 2. Minimum spanning trees and strongly connected components

```python
import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
        return True


def kruskal(node_count, edges):
    """Sort edges by weight, take any that joins two components. O(E log E)."""
    uf = UnionFind(node_count)
    total, used = 0, []
    for u, v, w in sorted(edges, key=lambda edge: edge[2]):
        if uf.union(u, v):
            total += w
            used.append((u, v, w))
            if len(used) == node_count - 1:
                break
    return total, used


def prim(graph, start=0):
    """Grow the tree from `start`, always adding the cheapest crossing edge."""
    visited = {start}
    heap = [(weight, start, neighbour) for neighbour, weight in graph.get(start, [])]
    heapq.heapify(heap)
    total, used = 0, []
    while heap and len(visited) < len(graph):
        weight, u, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        total += weight
        used.append((u, v, weight))
        for neighbour, edge_weight in graph.get(v, []):
            if neighbour not in visited:
                heapq.heappush(heap, (edge_weight, v, neighbour))
    return total, used


def kosaraju(node_count, edges):
    """Strongly connected components in O(V + E): DFS order, then DFS on the
    reversed graph. Iterative to avoid Python's recursion limit."""
    graph = [[] for _ in range(node_count)]
    reverse = [[] for _ in range(node_count)]
    for u, v in edges:
        graph[u].append(v)
        reverse[v].append(u)

    order, seen = [], [False] * node_count
    for start in range(node_count):
        if seen[start]:
            continue
        seen[start] = True
        stack = [(start, 0)]
        while stack:
            node, index = stack.pop()
            if index < len(graph[node]):
                stack.append((node, index + 1))
                neighbour = graph[node][index]
                if not seen[neighbour]:
                    seen[neighbour] = True
                    stack.append((neighbour, 0))
            else:
                order.append(node)                # post-order

    component = [-1] * node_count
    components = []
    for node in reversed(order):
        if component[node] != -1:
            continue
        group = []
        component[node] = len(components)
        stack = [node]
        while stack:
            current = stack.pop()
            group.append(current)
            for neighbour in reverse[current]:
                if component[neighbour] == -1:
                    component[neighbour] = len(components)
                    stack.append(neighbour)
        components.append(sorted(group))
    return components


if __name__ == "__main__":
    edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4), (3, 4, 2), (4, 0, 7)]
    print("kruskal:", kruskal(5, edges))

    # Prim needs an UNDIRECTED adjacency list: every edge in both directions.
    graph = {node: [] for node in range(5)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    print("prim   :", prim(graph, 0), "(same total as Kruskal)")

    directed = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 3)]
    print("strongly connected components:", kosaraju(5, directed))
    print("no edges (each node alone):", kosaraju(3, []))
    print("single node:", kosaraju(1, []))
```

Output:

```text
kruskal: (8, [(1, 2, 1), (1, 3, 2), (3, 4, 2), (0, 2, 3)])
prim   : (8, [(0, 2, 3), (2, 1, 1), (1, 3, 2), (3, 4, 2)]) (same total as Kruskal)
strongly connected components: [[0, 1, 2], [3, 4]]
no edges (each node alone): [[2], [1], [0]]
single node: [[0]]
```

**How it works**

- Kruskal sorts edges and takes any that connects two different components (Union-Find decides that in near-constant time). Prim grows one tree, always adding the cheapest edge that crosses the cut — a heap gives the same O(E log V).
- Both are greedy with a cut/cycle exchange argument: the cheapest edge crossing any cut belongs to some MST. They produce different but equally optimal trees when weights tie.
- Kosaraju needs **two** traversals: finishing order on the original graph, then DFS on the reversed graph in reverse finishing order. Each DFS on the reversed graph yields exactly one SCC. Tarjan's algorithm does it in one pass with a low-link array.
- SCCs condense a directed graph into a DAG of components, which is how you solve 2-SAT, "minimum vertices to reach all nodes", and reachability-with-cycles problems.

## Solved examples

### Example 1 — Network delay time (Medium)

**Problem.** A signal starts at node `k`; edges have transmission times. Return
the time until every node has received it, or −1 if some node is unreachable.

**Approach.** Single-source shortest paths with non-negative weights → Dijkstra. The answer is the maximum finite distance; if any node was never reached, return −1.

```python
import heapq
from math import inf


def network_delay_time(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {k: 0}
    heap = [(0, k)]
    settled = set()
    while heap:
        d, node = heapq.heappop(heap)
        if node in settled:
            continue
        settled.add(node)
        for neighbour, weight in graph.get(node, []):
            candidate = d + weight
            if candidate < dist.get(neighbour, inf):
                dist[neighbour] = candidate
                heapq.heappush(heap, (candidate, neighbour))

    if len(dist) < n:
        return -1
    return max(dist.values())


if __name__ == "__main__":
    times = [(2, 1, 1), (2, 3, 1), (3, 4, 1)]
    print("network delay time:", network_delay_time(times, 4, 2))
    print("unreachable node:", network_delay_time([(1, 2, 1)], 3, 1))
    print("single node:", network_delay_time([], 1, 1))
    print("direct chain:", network_delay_time([(1, 2, 3), (2, 3, 4)], 3, 1))
```

Output:

```text
network delay time: 2
unreachable node: -1
single node: 0
direct chain: 7
```

**Complexity.** O((V + E) log V) time, O(V + E) space. For a dense graph with non-negative weights you can drop the heap and scan for the minimum each round: O(V²).

### Example 2 — Cheapest flight with at most k stops (Medium)

**Problem.** Cheapest price from `src` to `dst` using at most `k` stops
(so at most `k + 1` edges).

**Approach.** Bellman-Ford restricted to `k + 1` relaxation rounds: after round `r`, `cost[v]` is the cheapest price using at most `r` edges. Read from a **copy** of the previous round, otherwise a single pass could chain several edges and break the stop limit.

```python
from math import inf


def find_cheapest_price(n, flights, src, dst, k):
    """flights: (from, to, price). k = maximum number of stops."""
    cost = [inf] * n
    cost[src] = 0
    for _ in range(k + 1):                       # at most k + 1 edges
        next_cost = cost[:]                       # snapshot: one edge per round
        for u, v, price in flights:
            if cost[u] + price < next_cost[v]:
                next_cost[v] = cost[u] + price
        cost = next_cost
    return -1 if cost[dst] == inf else cost[dst]


if __name__ == "__main__":
    flights = [(0, 1, 100), (1, 2, 100), (0, 2, 500)]
    print("cheapest with 0 stops:", find_cheapest_price(3, flights, 0, 2, 0))
    print("cheapest with 1 stop :", find_cheapest_price(3, flights, 0, 2, 1))
    print("unreachable:", find_cheapest_price(3, [(0, 1, 10)], 0, 2, 2))
    print("same city:", find_cheapest_price(2, [(0, 1, 5)], 0, 0, 1))
```

Output:

```text
cheapest with 0 stops: 500
cheapest with 1 stop : 200
unreachable: -1
same city: 0
```

**Complexity.** O(k · E) time and O(V) space. A Dijkstra variant that tracks the number of stops per state also works and is often faster in practice.

### Example 3 — Minimum cost to connect all points (Medium)

**Problem.** Given points on a plane, connect them all with the minimum total
Manhattan distance.

**Approach.** Build the complete graph of pairwise distances (or generate edges on the fly), then run Kruskal: sort edges by weight and add the ones that join distinct components. Prim with a heap is the usual alternative and avoids materialising all O(n²) edges for dense inputs.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


def min_cost_connect_points(points):
    n = len(points)
    edges = []
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))

    edges.sort()                                  # Kruskal: cheapest edge first
    uf = UnionFind(n)
    total, used = 0, 0
    for weight, u, v in edges:
        if uf.union(u, v):
            total += weight
            used += 1
            if used == n - 1:
                break
    return total


if __name__ == "__main__":
    points = [(0, 0), (2, 2), (3, 10), (5, 2), (7, 0)]
    print("min cost (kruskal):", min_cost_connect_points(points))
    print("two points:", min_cost_connect_points([(0, 0), (1, 1)]))
    print("single point:", min_cost_connect_points([(5, 5)]))
    print("collinear:", min_cost_connect_points([(0, 0), (1, 0), (2, 0), (3, 0)]))
```

Output:

```text
min cost (kruskal): 20
two points: 2
single point: 0
collinear: 3
```

**Complexity.** O(n² log n) time (n² edges, sorted) and O(n²) space. With Prim using a heap over lazily generated edges you get O(n² log n) time but only O(n) space — the usual optimisation for the "connect all points" family.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Shortest Routes I](https://cses.fi/problemset/task/1671) | CSES | Medium |
| [High Score](https://cses.fi/problemset/task/1673) | CSES | Hard |
| [Road Reparation](https://cses.fi/problemset/task/1675) | CSES | Medium |
| [Planets and Kingdoms](https://cses.fi/problemset/task/1683) | CSES | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain dijkstra finalizes smallest tentative distances with non-negative edges without notes.
- [ ] Explain bellman-ford relaxes all edges and handles negatives/cycle detection without notes.
- [ ] Explain floyd-warshall is o(v³) all-pairs dp without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
