# DSA Patterns Cheatsheet

Pattern recognition is the fastest way to improve. This file maps problem signals to approaches.

---

## Array and string patterns

| Pattern | Use when | Core invariant | Typical complexity |
|---|---|---|---|
| Two pointers | sorted array, pair/triplet, reverse, palindrome | left/right pointers shrink search space safely | `O(n)` after sort |
| Sliding window | contiguous subarray/substring | window satisfies or is adjusted toward a constraint | `O(n)` |
| Prefix sum | repeated range sum, subarray sum equals target | prefix difference represents a subarray | `O(n)` |
| Difference array | many range increments | mark changes at boundaries, prefix once | `O(n + q)` |
| Kadane | maximum subarray-like contiguous score | best subarray ending here | `O(n)` |
| Matrix traversal | grids, islands, spirals | boundary or visited state prevents repeats | `O(rows*cols)` |

---

## Hashing patterns

| Pattern | Use when | Idea |
|---|---|---|
| Frequency map | anagrams, counts, majority-like checks | map value -> count |
| Last seen index | longest substring/window | map item -> most recent position |
| Complement lookup | two sum-like | store what would complete answer |
| Canonical key | group equivalent items | sort tuple/count signature/normalized form |
| Prefix count map | subarray sum, path sum | count previous prefixes that form target |

---

## Stack and queue patterns

| Pattern | Use when | Idea |
|---|---|---|
| Stack simulation | parentheses, undo, path simplification | last unmatched item matters |
| Monotonic stack | next greater/smaller, histogram | stack keeps candidates in sorted order |
| Monotonic deque | sliding window max/min | deque keeps best candidate at front |
| BFS queue | shortest steps in unweighted graph | process by increasing distance |

---

## Linked list patterns

| Pattern | Use when | Idea |
|---|---|---|
| Dummy node | building/removing list nodes | avoids special head cases |
| Fast/slow pointers | cycle, middle, palindrome | one pointer moves faster |
| Reversal | reverse whole list or segment | keep `prev`, `cur`, `next` |
| Merge | sorted lists | choose smaller head repeatedly |

---

## Binary search patterns

| Pattern | Use when | Template |
|---|---|---|
| Exact search | target in sorted list | compare mid with target |
| Lower bound | first index with `arr[i] >= x` | move right/left by predicate |
| Upper bound | first index with `arr[i] > x` | variant of lower bound |
| Rotated search | sorted halves exist | identify sorted half each step |
| Answer search | min/max feasible value | binary search over answer range |

Answer-search phrase to remember:

```text
If feasibility is monotonic, binary search the answer.
```

---

## Tree patterns

| Pattern | Use when | Idea |
|---|---|---|
| DFS return value | height, balance, diameter | child returns useful summary to parent |
| Global/nonlocal answer | max path, diameter | update answer while returning another value |
| BFS levels | right view, level order | process queue level by level |
| LCA | ancestry | recurse left/right and combine |
| BST inorder | sorted order | inorder traversal yields ascending values |
| Serialize | persist tree | preorder with null markers or BFS |

---

## Graph patterns

| Pattern | Use when | Complexity |
|---|---|---|
| DFS/BFS components | islands, provinces, connected components | `O(V + E)` |
| BFS shortest path | unweighted shortest path | `O(V + E)` |
| Topological sort | prerequisites, dependency ordering | `O(V + E)` |
| Union Find | dynamic connectivity, cycle in undirected graph | near `O(1)` per op |
| Dijkstra | nonnegative weighted shortest path | `O(E log V)` |
| Bellman-Ford | negative edges / k-stop relaxation | `O(VE)` or bounded rounds |
| Floyd-Warshall | all-pairs shortest path, small `V` | `O(V^3)` |
| Kruskal MST | minimum spanning tree | `O(E log E)` |
| Tarjan bridges | critical connections | `O(V + E)` |

---

## Dynamic programming patterns

| Pattern | Use when | State idea |
|---|---|---|
| 1D DP | choices along sequence | `dp[i]` best/count using first `i` |
| 2D grid DP | paths in grid | `dp[r][c]` ways/best to reach cell |
| Knapsack | choose items with capacity/target | `dp[i][cap]` or compressed 1D |
| LIS | increasing subsequence | `tails[length]` or `dp[i]` |
| String DP | edit distance, LCS, regex | `dp[i][j]` over prefixes |
| Interval DP | burst balloons, matrix chain | `dp[l][r]` best inside interval |
| Bitmask DP | visit subsets, TSP-like | `dp[mask][last]` |
| Tree DP | choose/not choose on tree | return states per node |

DP checklist:

1. What does the state mean?
2. What choices transition into it?
3. What is the base case?
4. What order computes dependencies first?
5. Can memory be compressed?

---

## Greedy patterns

Greedy works when a local choice can be proven safe.

Common proof styles:

- **Exchange argument**: replace an optimal solution's first choice with the greedy choice without hurting optimality.
- **Stays ahead**: after every step, greedy is at least as good as any alternative.
- **Cut property**: for MST-like problems, the cheapest crossing edge is safe.

Signals include sorting by end time, choosing smallest/largest available each step, scheduling with deadlines, and jump/reachability where only farthest reach matters.

---

## Advanced structure patterns

| Pattern | Use when |
|---|---|
| Trie | prefix queries, word search pruning, dictionary matching |
| Fenwick tree | prefix sums with point updates |
| Segment tree | range queries with updates, min/max/sum/gcd |
| Lazy propagation | range updates + range queries |
| Binary trie | maximum XOR |
| KMP/Z algorithm | linear-time string pattern matching |
| Rolling hash | compare substrings quickly, duplicate detection |
| Combined DS design | cache, frequency tracker, randomized set |
