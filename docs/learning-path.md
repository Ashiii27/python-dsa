# DSA Learning Path: Beginner to Top-Tier Interview Level

This roadmap assumes Python as the implementation language. Adjust the speed based on your available time, but keep the order mostly intact because later topics reuse earlier patterns.

For each topic, use the materials in this order:

1. Read its `README.md` overview.
2. Complete its linked `study-guide.md` example and implementation drills.
3. Solve the core ladder in `problems/README.md`.
4. Add mixed-platform questions from [`practice/extended-practice.md`](../practice/extended-practice.md).
5. Record mistakes and use active recall before moving forward.

---

## Phase -1: Learn the Python language (skip only if you are already fluent)

**Outcome:** You can write, debug, test, and package Python without looking things up constantly.

Work through the [Python Track](../python/README.md): 12 lessons with exercises and tests,
plus capstone projects. Budget 2-8 weeks depending on your pace. You are done when you can
write a tested module with a dataclass, a generator, a decorator, and a CLI from a blank file.

---

## Phase 0: Python and problem-solving setup

**Outcome:** You can write bug-resistant Python quickly.

Study (the fast recap — full treatment in the [Python Track](../python/README.md)):

- Python lists, tuples, strings, dictionaries, and sets
- `collections.Counter`, `defaultdict`, `deque`, `OrderedDict`
- `heapq`, `bisect`, `itertools`, `math`, `functools`
- mutability, references, shallow copies, and slicing costs
- function design, recursion, and type hints

Checkpoint:

- Can you explain why `list.pop(0)` is slow?
- Can you use `heapq` for max-heap behavior?
- Can you sort by multiple keys?

---

## Phase 1: Complexity analysis

**Outcome:** You can reject impossible approaches from constraints.

| Input size | Usually acceptable |
|---:|---|
| `n <= 20` | exponential / backtracking / bitmask |
| `n <= 100` | `O(n^3)` sometimes |
| `n <= 2,000` | `O(n^2)` often |
| `n <= 100,000` | `O(n log n)` or `O(n)` |
| `n >= 1,000,000` | near-linear only |

Study Big-O, amortized analysis, recursion trees, space complexity, and Python operation costs.

---

## Phase 2: Core linear data structures

Topics:

1. Arrays and strings
2. Hashing
3. Linked lists
4. Stacks and queues

Patterns:

- two pointers
- sliding window
- prefix sum
- frequency map
- fast/slow pointers
- dummy node
- monotonic stack
- deque-based BFS

Checkpoint problems:

- Two Sum
- 3Sum
- Product of Array Except Self
- Minimum Window Substring
- Longest Consecutive Sequence
- Reverse Linked List
- Merge Two Sorted Lists
- Valid Parentheses
- Daily Temperatures
- Sliding Window Maximum

---

## Phase 3: Recursion, searching, sorting

Topics:

1. Recursion and backtracking
2. Searching and sorting
3. Binary search

Patterns:

- decision tree recursion
- choose/explore/unchoose
- pruning
- quickselect
- binary search lower/upper bound
- binary search on answer

Checkpoint problems:

- Subsets
- Permutations
- Combination Sum
- Word Search
- Kth Largest Element
- Search in Rotated Sorted Array
- Koko Eating Bananas
- Median of Two Sorted Arrays

---

## Phase 4: Trees and heaps

Topics:

1. Binary trees
2. Binary search trees
3. Heaps / priority queues

Patterns:

- pre/in/postorder traversal
- DFS returns information to parent
- BFS by levels
- LCA
- heap for top-k and scheduling
- two heaps for median

Checkpoint problems:

- Diameter of Binary Tree
- Binary Tree Maximum Path Sum
- Serialize and Deserialize Binary Tree
- Validate BST
- Kth Smallest in BST
- Merge K Sorted Lists
- Find Median from Data Stream

---

## Phase 5: Graphs, DP, greedy

Topics:

1. Graphs
2. Dynamic programming
3. Greedy

Patterns:

- graph modeling
- BFS shortest path in unweighted graph
- DFS connected components
- topological sort
- DP state definition
- memoization vs tabulation
- greedy sorting and exchange argument

Checkpoint problems:

- Number of Islands
- Course Schedule
- Word Ladder
- Clone Graph
- Coin Change
- Longest Increasing Subsequence
- Edit Distance
- Partition Equal Subset Sum
- Jump Game
- Gas Station

---

## Phase 6: Advanced interview topics

Topics:

- tries
- intervals and line sweep
- union find
- segment tree and Fenwick tree
- bit manipulation
- math and number theory
- advanced strings
- advanced graphs
- design data structures

Checkpoint problems:

- Word Search II
- My Calendar III
- Accounts Merge
- Count of Smaller Numbers After Self
- Maximum XOR of Two Numbers
- Count Primes
- Shortest Palindrome
- Critical Connections in a Network
- LRU Cache
- LFU Cache

---

## 12-week fast-track plan

| Week | Focus | Deliverable |
|---:|---|---|
| 1 | Python foundations, complexity, arrays | 20 easy/medium array problems |
| 2 | Strings, hashing, prefix sums | 25 problems, especially windows/maps |
| 3 | Linked lists, stacks, queues | Implement linked list + monotonic stack from memory |
| 4 | Recursion, backtracking | Subsets/permutations/combinations/grid search |
| 5 | Sorting, binary search | 25 binary search problems including answer search |
| 6 | Trees and BSTs | Traversal fluency + serialization/LCA |
| 7 | Heaps and intervals | Top-k, median, scheduling, sweep line |
| 8 | Graph basics | BFS/DFS/topological sort/components |
| 9 | Dynamic programming I | 1D/2D DP, knapsack, LIS |
| 10 | Dynamic programming II + greedy | interval DP, string DP, proofs |
| 11 | Advanced DS | trie, union find, Fenwick/segment tree |
| 12 | Advanced graphs/design + mocks | timed mixed sets and mock interviews |

---

## Long-term mastery loop

1. Redo missed problems after 3 days, 1 week, and 1 month.
2. Maintain a mistake log: wrong pattern, bug, edge case, complexity issue, or proof gap.
3. Mix topics. Real interviews rarely announce the pattern.
4. Do timed sessions: 35 minutes medium, 50 minutes hard.
5. Practice explaining before coding.
