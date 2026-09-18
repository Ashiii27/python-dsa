# Problem-Solving Framework

Use this for every DSA problem until it becomes automatic.

---

## 1. Restate and clarify

Ask or answer:

- What are the exact inputs and outputs?
- Are there duplicates?
- Are values sorted? Can I sort them?
- Are negative numbers possible?
- Is the graph directed or undirected?
- Do I need all solutions, one solution, or a count?
- Are there memory constraints?
- What should happen for empty input?

---

## 2. Read constraints like a map

Constraints usually reveal the expected complexity.

- `n <= 20`: backtracking, bitmask, subset enumeration
- `n <= 500`: `O(n^3)` may pass
- `n <= 2,000`: `O(n^2)` often passes
- `n <= 100,000`: `O(n log n)` or `O(n)`
- values up to `10^9`: do not build arrays indexed by value
- graph with `V, E`: think `O(V + E)`, `O(E log V)`, or DSU

---

## 3. Always state brute force

Brute force gives you a correctness baseline, a small-case test oracle, and the bottleneck to optimize.

Examples:

- Repeated range sums -> prefix sums
- Repeated membership scans -> hash set
- Repeated min/max retrieval -> heap or monotonic deque
- Trying all partitions -> DP
- Exploring all paths -> graph traversal/backtracking

---

## 4. Identify the pattern

| Signal in problem | Candidate pattern |
|---|---|
| sorted array, first/last valid index | binary search |
| maximize/minimize feasible value | binary search on answer |
| contiguous subarray/substring | sliding window or prefix sums |
| pair/triplet in sorted array | two pointers |
| nearest greater/smaller | monotonic stack |
| top-k, repeated smallest/largest | heap |
| connected components | DFS/BFS/Union Find |
| prerequisites/dependencies | topological sort |
| shortest path unweighted | BFS |
| shortest path weighted nonnegative | Dijkstra |
| overlapping subproblems | dynamic programming |
| prefix lookup | trie |
| range query with updates | Fenwick/segment tree |

---

## 5. Design invariants

An invariant is something that remains true throughout the algorithm.

Examples:

- Sliding window: all characters in the current window are unique.
- Binary search: the answer is always inside `[lo, hi]`.
- Monotonic stack: indices in the stack have decreasing temperatures.
- BFS: the first time a node is reached is the shortest distance in an unweighted graph.
- Union Find: each set representative identifies one connected component.

If you cannot state an invariant, you probably do not fully understand the approach yet.

---

## 6. Code with defensive structure

Good interview code uses descriptive variables, separates helpers cleanly, handles edge cases early, keeps loops simple, and updates state in one obvious place.

Avoid silent coding, magic indices, unnecessary mutation, recursion without depth awareness, and mixing too many concerns in one loop.

---

## 7. Test intentionally

Minimum tests:

- empty input
- one element
- two elements
- duplicates
- negative numbers if allowed
- all equal values
- already sorted / reverse sorted
- impossible case
- maximum-ish shape: skewed tree, disconnected graph, long string

---

## 8. Explain complexity

Say:

```text
Time: O(...), because each element/node/edge is processed ... times.
Space: O(...), for the hash map/recursion stack/queue/DP table.
```

Include hidden Python costs: slicing copies, string concatenation in loops can be quadratic, `list.pop(0)` shifts elements, recursion uses call-stack space, and sorting costs `O(n log n)`.

---

## 9. Post-solve review

After each problem, write:

- Pattern:
- Key invariant:
- Complexity:
- Bug I made:
- Edge case I missed:
- Could I solve it again from scratch tomorrow?
