# Graphs: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Choose a representation, define the state being visited, and make direction explicit. Traversal solves reachability; BFS layers solve unweighted distance; topological order solves directed dependencies.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Adjacency lists use O(V+E); matrices use O(V²). |
| 2 | DFS and BFS both find components and reachability. |
| 3 | BFS gives shortest edge count in unweighted graphs. |
| 4 | Kahn indegrees or DFS colors detect directed cycles. |
| 5 | Grid cells are graph nodes with implicit neighbors. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Connected regions | DFS/BFS |
| Fewest unweighted steps | BFS |
| Prerequisites/order | Topological sort |
| Two-group constraint | Bipartite coloring |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

In multi-source BFS for rotten oranges, enqueue every rotten cell at minute zero. Each queue layer infects cells one minute farther away. This is equivalent to one virtual source connected to all initial rotten cells.

## Tricks and interview notes

- Mark visited when enqueuing to avoid duplicate queue entries.
- For undirected cycle DFS, track the parent edge.
- Build both forward and reverse graphs when direction reversal simplifies the query.
- Count all vertices, including isolated ones.

## Common mistakes

- **Watch for:** Treating a directed graph as undirected.
- **Watch for:** Using DFS depth as shortest distance.
- **Watch for:** Forgetting invalid-prefix handling in Alien Dictionary.
- **Watch for:** Mutating a grid when callers expect it preserved.

## Implementation drills

1. Implement recursive DFS, iterative DFS, and BFS.
2. Count grid components.
3. Implement Kahn topological sort with cycle detection.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. How to represent a graph in Python

Pick the representation from the operation you need: adjacency lists for
traversal (O(V + E)), an edge list for Kruskal and "process all edges", and an
adjacency matrix when you need O(1) "is there an edge u→v?" on a dense graph.

```python
from collections import defaultdict

EDGES = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]


def build_adjacency(edges, directed=False):
    """Adjacency list: node -> list of neighbours. Best default for traversal."""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        if not directed:
            adj[v].append(u)
    return dict(adj)


def build_weighted(edges, directed=False):
    """Weighted adjacency list: node -> list of (neighbour, weight)."""
    adj = defaultdict(list)
    for u, v, weight in edges:
        adj[u].append((v, weight))
        if not directed:
            adj[v].append((u, weight))
    return dict(adj)


def build_matrix(node_count, edges, directed=False):
    """Adjacency matrix: O(1) edge lookup, O(V^2) memory."""
    matrix = [[0] * node_count for _ in range(node_count)]
    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix


def degrees(adj):
    return {node: len(neighbours) for node, neighbours in adj.items()}


if __name__ == "__main__":
    adj = build_adjacency(EDGES)
    print("adjacency list:", adj)
    print("degrees:", degrees(adj))
    print("neighbours of 2:", adj.get(2, []))

    weighted = build_weighted([(0, 1, 4), (0, 2, 1), (2, 1, 2), (2, 3, 5)])
    print("weighted:", weighted)

    matrix = build_matrix(5, EDGES)
    for row in matrix:
        print("  ", row)
    print("edge 0-1 exists:", bool(matrix[0][1]), "| edge 0-4 exists:", bool(matrix[0][4]))

    directed = build_adjacency([(0, 1), (2, 0)], directed=True)
    print("directed (1 does not point back at 0):", directed)
```

Output:

```text
adjacency list: {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
degrees: {0: 2, 1: 2, 2: 3, 3: 2, 4: 1}
neighbours of 2: [0, 1, 3]
weighted: {0: [(1, 4), (2, 1)], 1: [(0, 4), (2, 2)], 2: [(0, 1), (1, 2), (3, 5)], 3: [(2, 5)]}
   [0, 1, 1, 0, 0]
   [1, 0, 1, 0, 0]
   [1, 1, 0, 1, 0]
   [0, 0, 1, 0, 1]
   [0, 0, 0, 1, 0]
edge 0-1 exists: True | edge 0-4 exists: False
directed (1 does not point back at 0): {0: [1], 2: [0]}
```

**How it works**

- `defaultdict(list)` is the idiomatic adjacency list: `graph[u].append(v)` with no existence check. Build a `dict` of sets instead when you need O(1) "is `v` a neighbour of `u`?".
- Always model the node set explicitly (usually `range(n)`) — nodes with no edges are missing from a dict built from an edge list, which silently breaks loops like `for node in graph`.
- Weighted graphs store `(neighbour, weight)` tuples; for Dijkstra you want them as `(distance, node)` **in the heap**, which is the other order, and mixing the two up is a classic bug.
- A matrix is only right for dense graphs: 10⁵ nodes would need 10¹⁰ entries.

### 2. BFS: shortest paths and components

BFS explores in layers, so the first time you reach a node is via a shortest path
(in unweighted graphs). It uses a queue — never a stack.

```python
from collections import deque


def bfs(graph, start):
    """Visit order and distances from start. O(V + E)."""
    distances = {start: 0}
    order = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph.get(node, []):
            if neighbour not in distances:          # first visit = shortest path
                distances[neighbour] = distances[node] + 1
                queue.append(neighbour)
    return order, distances


def shortest_path(graph, start, target):
    """Reconstruct the path with a parent map. Returns None if unreachable."""
    parent = {start: None}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            path = []
            while node is not None:                 # walk parents backwards
                path.append(node)
                node = parent[node]
            return path[::-1]
        for neighbour in graph.get(node, []):
            if neighbour not in parent:
                parent[neighbour] = node
                queue.append(neighbour)
    return None


def connected_components(node_count, graph):
    """Number of components plus their members: run BFS from every unseen node."""
    seen = set()
    components = []
    for node in range(node_count):
        if node in seen:
            continue
        queue, group = deque([node]), []
        seen.add(node)
        while queue:
            current = queue.popleft()
            group.append(current)
            for neighbour in graph.get(current, []):
                if neighbour not in seen:
                    seen.add(neighbour)
                    queue.append(neighbour)
        components.append(sorted(group))
    return len(components), components


def bfs_grid(grid, start, walkable="."):
    """BFS on a grid: neighbours are the four orthogonal cells."""
    rows, cols = len(grid), len(grid[0])
    distances = {start: 0}
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == walkable
                    and (nr, nc) not in distances):
                distances[(nr, nc)] = distances[(r, c)] + 1
                queue.append((nr, nc))
    return distances


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [4], 5: []}
    order, distances = bfs(graph, 0)
    print("BFS order:", order)
    print("distances from 0:", distances)
    print("shortest path 0 -> 4:", shortest_path(graph, 0, 4))
    print("unreachable:", shortest_path(graph, 0, 5))
    print("components:", connected_components(6, graph))

    grid = ["..#..",
            ".#...",
            "....."]
    print("grid distances from (0, 0):", sorted(bfs_grid(grid, (0, 0)).items())[:5], "...")
```

Output:

```text
BFS order: [0, 1, 2, 3, 4]
distances from 0: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}
shortest path 0 -> 4: [0, 2, 3, 4]
unreachable: None
components: (2, [[0, 1, 2, 3, 4], [5]])
grid distances from (0, 0): [((0, 0), 0), ((0, 1), 1), ((0, 3), 7), ((0, 4), 8), ((1, 0), 1)] ...
```

**How it works**

- Mark a node **seen when you enqueue it**, not when you dequeue it — otherwise it can be enqueued many times (O(V · E) blow-up on dense graphs).
- `distances` doubles as the visited set; `parent` doubles as the visited set in `shortest_path`. One structure, two jobs.
- `connected_components` iterates over `range(node_count)` rather than the dict keys, so isolated nodes still count.
- Grid BFS treats `(row, col)` as the node; the four-direction tuple `((1, 0), (−1, 0), (0, 1), (0, −1))` is worth memorising.

### 3. DFS: recursion, iteration, cycles, and topological order

DFS goes as deep as possible before backtracking. Use it for connectivity,
cycle detection, topological sorting, and any "explore a whole region" task
(islands, flood fill).

```python
from collections import deque, defaultdict


def dfs_recursive(graph, start, seen=None):
    if seen is None:
        seen = set()
    seen.add(start)
    order = [start]
    for neighbour in graph.get(start, []):
        if neighbour not in seen:
            order.extend(dfs_recursive(graph, neighbour, seen))
    return order


def dfs_iterative(graph, start):
    """Same order, explicit stack — required for deep graphs in Python."""
    seen, order, stack = {start}, [], [start]
    while stack:
        node = stack.pop()
        order.append(node)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in seen:
                seen.add(neighbour)
                stack.append(neighbour)
    return order


def has_cycle_undirected(graph):
    """A back edge to a visited node that is not the parent means a cycle."""
    seen = set()
    for start in list(graph):
        if start in seen:
            continue
        stack = [(start, None)]
        seen.add(start)
        while stack:
            node, parent = stack.pop()
            for neighbour in graph.get(node, []):
                if neighbour not in seen:
                    seen.add(neighbour)
                    stack.append((neighbour, node))
                elif neighbour != parent:
                    return True
    return False


def topological_sort_kahn(node_count, prereqs):
    """Order courses so every prerequisite comes first; [] if a cycle exists."""
    graph = defaultdict(list)
    indegree = [0] * node_count
    for course, prereq in prereqs:                 # prereq must come before course
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque([node for node in range(node_count) if indegree[node] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)
    return order if len(order) == node_count else []      # short order => cycle


def is_bipartite(graph):
    """Two-colour the graph: a conflict between neighbours means it is not bipartite."""
    colour = {}
    for start in list(graph):
        if start in colour:
            continue
        colour[start] = 0
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbour in graph.get(node, []):
                if neighbour not in colour:
                    colour[neighbour] = 1 - colour[node]
                    queue.append(neighbour)
                elif colour[neighbour] == colour[node]:
                    return False
    return True


if __name__ == "__main__":
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    print("dfs recursive:", dfs_recursive(graph, 0))
    print("dfs iterative:", dfs_iterative(graph, 0))

    cyclic = {0: [1], 1: [2], 2: [0]}
    print("cycle in undirected triangle:", has_cycle_undirected(cyclic))
    # 0 -> 1 -> 3 and 0 -> 2 -> 3: in an undirected graph that diamond IS a cycle
    print("cycle in the diamond 0-1-3-2-0:", has_cycle_undirected(graph))
    tree = {0: [1, 2], 1: [], 2: [3], 3: []}
    print("cycle in a real tree:", has_cycle_undirected(tree))

    print("topological order:", topological_sort_kahn(4, [(1, 0), (2, 0), (3, 1), (3, 2)]))
    print("cyclic prerequisites:", topological_sort_kahn(3, [(0, 1), (1, 2), (2, 0)]))

    print("bipartite (path 0-1-2):", is_bipartite({0: [1], 1: [0, 2], 2: [1]}))
    print("not bipartite (triangle):", is_bipartite({0: [1, 2], 1: [0, 2], 2: [0, 1]}))
```

Output:

```text
dfs recursive: [0, 1, 3, 2]
dfs iterative: [0, 1, 3, 2]
cycle in undirected triangle: True
cycle in the diamond 0-1-3-2-0: True
cycle in a real tree: False
topological order: [0, 1, 2, 3]
cyclic prerequisites: []
bipartite (path 0-1-2): True
not bipartite (triangle): False
```

**How it works**

- `has_cycle_undirected` must skip the **parent**, otherwise every undirected edge looks like a cycle. For directed graphs use three colours (unvisited / in-stack / done) instead: a neighbour that is "in-stack" is a back edge.
- Kahn's algorithm repeatedly removes nodes with indegree 0. If fewer than `n` nodes come out, the rest are in (or behind) a cycle — that single length check is the cycle test.
- `is_bipartite` is BFS with two colours; the same idea detects odd cycles and solves "is the graph 2-colourable".
- Prefer the iterative DFS for graphs with more than ~1000 nodes of depth — Python's recursion limit will stop the recursive one.

## Solved examples

### Example 1 — Number of islands (Medium)

**Problem.** Count the islands in a grid of `"1"` (land) and `"0"` (water),
where islands are 4-connected land regions.

**Approach.** Scan the grid; whenever you find unvisited land, increment the count and run a flood fill (DFS or BFS) that marks the whole island as visited. Sinking the island in place (writing `"0"`) avoids a separate visited set, which keeps the space at O(1) beyond the recursion stack.

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def sink(r, c):
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"                        # mark visited by sinking it
        for dr, dc in directions:
            sink(r + dr, c + dc)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                sink(r, c)
    return islands


def num_islands_bfs(grid):
    """Iterative version: same idea with an explicit queue."""
    from collections import deque
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen, islands = set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            islands += 1
            queue = deque([(r, c)])
            seen.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
    return islands


if __name__ == "__main__":
    grid1 = [["1", "1", "0", "0"],
             ["1", "1", "0", "0"],
             ["0", "0", "1", "0"]]
    grid2 = [row[:] for row in grid1]
    print("DFS islands:", num_islands(grid1))
    print("BFS islands:", num_islands_bfs(grid2))
    print("no land:", num_islands_bfs([["0", "0"]]))
    print("empty grid:", num_islands([]))
```

Output:

```text
DFS islands: 2
BFS islands: 2
no land: 0
empty grid: 0
```

**Complexity.** O(rows · cols) time — every cell is visited a constant number of times — and O(rows · cols) stack/queue space in the worst case.

### Example 2 — Course schedule II: topological order (Medium)

**Problem.** Given `n` courses and prerequisite pairs, return an order in which
you can take all of them, or `[]` if it is impossible.

**Approach.** Kahn's algorithm. Build the graph `prerequisite -> course`, count indegrees, and repeatedly take a course whose indegree is zero. If we emit all `n` courses, that is a valid order; if the queue empties early, a cycle among the prerequisites makes it impossible.

```python
from collections import defaultdict, deque


def find_order(num_courses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque([c for c in range(num_courses) if indegree[c] == 0])
    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    return order if len(order) == num_courses else []


if __name__ == "__main__":
    print("4 courses, chain:", find_order(4, [(1, 0), (2, 0), (3, 1), (3, 2)]))
    print("2 courses:", find_order(2, [(1, 0)]))
    print("cycle ->", find_order(2, [(0, 1), (1, 0)]))
    print("no prerequisites:", find_order(3, []))
    print("self-loop ->", find_order(1, [(0, 0)]))
```

Output:

```text
4 courses, chain: [0, 1, 2, 3]
2 courses: [0, 1]
cycle -> []
no prerequisites: [0, 1, 2]
self-loop -> []
```

**Complexity.** O(V + E) time and O(V + E) space. The DFS alternative appends nodes in reverse post-order; both are correct, and Kahn's is easier to adapt when you need to detect the cycle or output any valid order.

### Example 3 — Rotting oranges: multi-source BFS (Medium)

**Problem.** Each cell is empty, a fresh orange (1), or a rotten orange (2).
Every minute, rot spreads to 4-neighbours. Return the minutes until no fresh
orange remains, or −1 if impossible.

**Approach.** This is BFS from **all** rotten cells at once: push every source into the queue at time 0, then expand layer by layer. The answer is the maximum timestamp reached; if any fresh orange was never reached, return −1.

```python
from collections import deque


def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))            # (row, col, minutes)
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    while queue:
        r, c, time = queue.popleft()
        minutes = max(minutes, time)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2                   # mark when enqueuing
                fresh -= 1
                queue.append((nr, nc, time + 1))
    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))     # 4
    print(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))     # -1 (isolated)
    print("already all rotten:", oranges_rotting([[2, 2], [2, 2]]))
    print("no oranges:", oranges_rotting([[0]]))
```

Output:

```text
4
-1
already all rotten: 0
no oranges: 0
```

**Complexity.** O(rows · cols) time and space. Multi-source BFS is the standard tool for "spread from several starting points": walls and gates, 01-matrices (distance to nearest 0), and fire spread.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Counting Rooms](https://cses.fi/problemset/task/1192) | CSES | Medium |
| [Building Roads](https://cses.fi/problemset/task/1666) | CSES | Medium |
| [Message Route](https://cses.fi/problemset/task/1667) | CSES | Medium |
| [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain adjacency lists use o(v+e); matrices use o(v²) without notes.
- [ ] Explain dfs and bfs both find components and reachability without notes.
- [ ] Explain bfs gives shortest edge count in unweighted graphs without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
