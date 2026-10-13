# Union Find / Disjoint Set Union: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

DSU maintains a partition under repeated merges. It answers whether nodes share a component, but not arbitrary path, deletion, or historical connectivity questions.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Each element follows parent pointers to a representative root. |
| 2 | Path compression flattens find paths. |
| 3 | Union by size/rank attaches the smaller tree below the larger. |
| 4 | A failed union detects a cycle in an undirected edge stream. |
| 5 | Component metadata can live at roots. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Repeated connectivity after unions | DSU |
| First redundant undirected edge | Failed union |
| Kruskal MST | Sort edges + DSU |
| Merge accounts/identities | Map attributes then union |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Initially `{0},{1},{2}`. Union(0,1) makes one root size 2; union(1,2) first finds root(1)=root(0), then attaches 2. A later union(0,2) returns false and reveals a cycle edge.

## Tricks and interview notes

- Initialize component count to n and decrement only on successful unions.
- Compress coordinates such as emails, rows, and columns into DSU ids.
- Keep size/rank data meaningful only at roots.
- DSU is excellent offline; dynamic deletions usually need another technique.

## Common mistakes

- **Watch for:** Decrementing component count on redundant unions.
- **Watch for:** Comparing immediate parents instead of roots.
- **Watch for:** Applying DSU directly to directed-cycle detection.
- **Watch for:** Recursive find exceeding Python depth before compression.

## Implementation drills

1. Implement iterative path compression.
2. Count components after an edge stream.
3. Implement Kruskal and return failure if disconnected.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Disjoint Set Union from scratch

Union-Find keeps a forest where each tree is a set. Two optimisations make it
effectively O(1) per operation: **path compression** (flatten trees during
`find`) and **union by size** (attach the smaller tree under the larger one).
With both, the amortised cost is bounded by the inverse Ackermann function —
constant for any realistic input.

```python
class UnionFind:
    """Sets of 0..n-1 with path compression and union by size."""

    def __init__(self, n):
        self.parent = list(range(n))       # parent[i] = i means "i is a root"
        self.size = [1] * n                # only meaningful at roots
        self.components = n

    def find(self, x):
        """Root of the set containing x (path halving as we climb)."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # point to the grandparent
            x = self.parent[x]
        return x

    def union(self, a, b):
        """Merge the two sets. Returns True if they were separate."""
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False                   # already connected: nothing merged
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        self.components -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def component_size(self, x):
        return self.size[self.find(x)]

    def groups(self):
        """All members grouped by root."""
        buckets = {}
        for node in range(len(self.parent)):
            buckets.setdefault(self.find(node), []).append(node)
        return list(buckets.values())

    def __len__(self):
        return self.components

    def __repr__(self):
        return f"UnionFind(parent={self.parent}, components={self.components})"


if __name__ == "__main__":
    uf = UnionFind(7)
    print("start:", uf)

    for a, b in [(0, 1), (1, 2), (3, 4), (5, 6)]:
        uf.union(a, b)
        print(f"union({a}, {b}) -> components = {uf.components}")

    print("connected(0, 2):", uf.connected(0, 2), "| connected(0, 3):", uf.connected(0, 3))
    print("component_size(0):", uf.component_size(0))
    print("redundant union(1, 2):", uf.union(1, 2), "(already connected)")

    uf.union(2, 3)
    print("after union(2, 3):", uf)
    print("groups:", uf.groups())
    print("total components:", len(uf))
```

Output:

```text
start: UnionFind(parent=[0, 1, 2, 3, 4, 5, 6], components=7)
union(0, 1) -> components = 6
union(1, 2) -> components = 5
union(3, 4) -> components = 4
union(5, 6) -> components = 3
connected(0, 2): True | connected(0, 3): False
component_size(0): 3
redundant union(1, 2): False (already connected)
after union(2, 3): UnionFind(parent=[0, 0, 0, 0, 3, 5, 5], components=2)
groups: [[0, 1, 2, 3, 4], [5, 6]]
total components: 2
```

**How it works**

- `parent[x] == x` marks a root. Everything else is a pointer towards its set's representative, so `find` walks up until it stops moving.
- Path compression (here path **halving**) rewires nodes to their grandparent on the way up. After the first `find`, the tree is much flatter, so later queries are nearly free.
- Union by size keeps trees shallow by always attaching the smaller tree to the larger one. Without it, unions can build a chain of length n and `find` degrades to O(n).
- `union` returning `False` is a **cycle signal** in graph problems: merging two already-connected nodes means the edge is redundant.

### 2. Union-Find over arbitrary keys, and graph applications

```python
class KeyedUnionFind:
    """Same structure over any hashable keys: strings, tuples, coordinates."""

    def __init__(self):
        self.parent = {}
        self.size = {}
        self.components = 0

    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.size[key] = 1
            self.components += 1

    def find(self, key):
        self.add(key)                                   # auto-register unknown keys
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

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

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def groups(self):
        buckets = {}
        for key in self.parent:
            buckets.setdefault(self.find(key), []).append(key)
        return {root: sorted(members) for root, members in sorted(buckets.items())}


def count_components(node_count, edges):
    """Number of connected components in an undirected graph."""
    uf = UnionFind(node_count)
    for u, v in edges:
        uf.union(u, v)
    return uf.components


def largest_component(node_count, edges):
    """Size of the biggest component (0 for an empty graph)."""
    uf = UnionFind(node_count)
    for u, v in edges:
        uf.union(u, v)
    sizes = {}
    for node in range(node_count):
        root = uf.find(node)
        sizes[root] = sizes.get(root, 0) + 1
    return max(sizes.values(), default=0)


def find_redundant_edge(node_count, edges):
    """First edge whose endpoints are already connected => it closes a cycle."""
    uf = UnionFind(node_count)
    for u, v in edges:
        if not uf.union(u, v):
            return (u, v)
    return None


class UnionFind:
    """Index-based version used by the helpers above (kept here for runnability)."""

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


if __name__ == "__main__":
    emails = KeyedUnionFind()
    for account in (["a@x.com", "b@x.com"], ["b@x.com", "c@x.com"], ["d@x.com"]):
        first, *rest = account
        for other in rest:
            emails.union(first, other)
    print("merged accounts:", emails.groups())
    print("components:", emails.components)

    edges = [(0, 1), (1, 2), (3, 4)]
    print("components in graph:", count_components(5, edges))
    print("largest component:", largest_component(5, edges))
    print("redundant edge (closes a cycle):", find_redundant_edge(3, [(0, 1), (1, 2), (0, 2)]))
    print("no cycle:", find_redundant_edge(3, [(0, 1), (1, 2)]))
```

Output:

```text
merged accounts: {'a@x.com': ['a@x.com', 'b@x.com', 'c@x.com']}
components: 1
components in graph: 2
largest component: 3
redundant edge (closes a cycle): (0, 2)
no cycle: None
```

**How it works**

- `KeyedUnionFind` swaps the list for a dict, so the "elements" can be anything hashable: emails, `(row, col)` coordinates, node names.
- `count_components` starts at `n` components and decrements on every successful union — no traversal needed.
- `find_redundant_edge` is cycle detection in an undirected graph: the first edge that fails to merge two sets closes a loop.
- Union-Find handles **merging only**. It cannot split a set, so it suits offline/append-only problems (Kruskal, connectivity queries, dynamic component counts) but not deletions.

## Solved examples

### Example 1 — Number of provinces (Medium)

**Problem.** Given an `n × n` adjacency matrix where `is_connected[i][j]` means
cities `i` and `j` are directly connected, count the provinces (connected groups).

**Approach.** Union every pair `i < j` that is connected (the matrix is symmetric, so only the upper triangle is needed). The number of components left is the answer. Union-Find is a natural fit because the input is a connectivity relation, not a traversal problem.

```python
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


def find_circle_num(is_connected):
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):                  # upper triangle only
            if is_connected[i][j]:
                uf.union(i, j)
    return uf.components


if __name__ == "__main__":
    print("provinces:", find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print("provinces:", find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    print("all connected:", find_circle_num([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
    print("single city:", find_circle_num([[1]]))
```

Output:

```text
provinces: 2
provinces: 3
all connected: 1
single city: 1
```

**Complexity.** O(n² · α(n)) time — the matrix must be read anyway — and O(n) space. DFS would be O(n²) too; Union-Find wins when edges arrive incrementally.

### Example 2 — Redundant connection (Medium)

**Problem.** An undirected graph has one extra edge that creates a cycle. Return
that edge (the last one that could be removed to leave a tree).

**Approach.** Union edges one at a time. The first edge whose endpoints are already in the same component closes a cycle, and because the input becomes a tree after removing one edge, that edge is the answer.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])    # full path compression
        return self.parent[x]

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False                                  # cycle
        if self.rank[root_a] < self.rank[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        if self.rank[root_a] == self.rank[root_b]:
            self.rank[root_a] += 1
        return True


def find_redundant_connection(edges):
    """Nodes are 1-indexed in the problem statement, so size from the max label."""
    node_count = max(max(edge) for edge in edges) + 1
    uf = UnionFind(node_count)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


if __name__ == "__main__":
    print(find_redundant_connection([[1, 2], [1, 3], [2, 3]]))          # [2, 3]
    print(find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
    print("tree (no cycle):", find_redundant_connection([[1, 2], [2, 3]]))
```

Output:

```text
[2, 3]
[1, 4]
tree (no cycle): []
```

**Complexity.** O(n · α(n)) time, O(n) space. This example uses **union by rank** instead of by size — both bound the tree height by O(log n), and either is accepted in interviews.

### Example 3 — Most stones removed with same row or column (Medium)

**Problem.** Stones sit at `(row, col)`. You may remove a stone if another stone
shares its row or column. Return the maximum number removable.

**Approach.** Stones sharing a row or column are connected, so all stones in one connected component can be reduced to a single survivor. Answer = total stones − number of components. The trick: a row and a column are different kinds of node, so encode a row as `("r", r)` and a column as `("c", c)` to keep them distinct in the same Union-Find.

```python
class KeyedUnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}
        self.components = 0

    def add(self, key):
        if key not in self.parent:
            self.parent[key] = key
            self.size[key] = 1
            self.components += 1

    def find(self, key):
        self.add(key)
        while self.parent[key] != key:
            self.parent[key] = self.parent[self.parent[key]]
            key = self.parent[key]
        return key

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


def remove_stones(stones):
    uf = KeyedUnionFind()
    for row, col in stones:
        uf.union(("r", row), ("c", col))       # the stone links its row and column
    return len(stones) - uf.components


if __name__ == "__main__":
    print("removable:", remove_stones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
    print("removable:", remove_stones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
    print("isolated stones:", remove_stones([[0, 0], [1, 1]]))
    print("one stone:", remove_stones([[0, 0]]))
```

Output:

```text
removable: 5
removable: 3
isolated stones: 0
one stone: 0
```

**Complexity.** O(n · α(n)) time and O(n) space. The "two node types with a shared counter" encoding is the general technique for bipartite-linking problems (row/column, word/pattern, account/email).

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Road Construction](https://cses.fi/problemset/task/1676) | CSES | Medium |
| [Road Reparation](https://cses.fi/problemset/task/1675) | CSES | Medium |
| [Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) | LeetCode | Medium |
| [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain each element follows parent pointers to a representative root without notes.
- [ ] Explain path compression flattens find paths without notes.
- [ ] Explain union by size/rank attaches the smaller tree below the larger without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
