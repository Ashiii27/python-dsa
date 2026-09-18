# Top Interview Questions by Topic

This list is curated from the topic guides. It focuses on patterns commonly seen in high-quality software engineering interviews. Problem names are intentionally concise; write your own full solution notes using `templates/problem-template.md`.

Legend: E = Easy, M = Medium, H = Hard. Solve in topic order first, then mix topics randomly.

## Python Foundations for DSA

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 1 | Build a Frequency Counter | Easy | Use a dict or Counter and increment per item. | O(n) | O(k) |
| 2 | Group Items by Key | Easy | Use defaultdict(list) and append into each group. | O(n) | O(n) |
| 3 | Implement Queue with deque | Easy | Use append and popleft for true queue operations. | O(1) per op | O(n) |
| 4 | Sort Records by Multiple Fields | Easy | Use tuple key like (age, -score). | O(n log n) | O(n) |
| 5 | Top K Values with Heap | Medium | Maintain a min-heap of size k. | O(n log k) | O(k) |
| 6 | Parse and Count Log Events | Medium | Split lines, normalize fields, aggregate with maps. | O(total chars) | O(unique keys) |

## Complexity Analysis

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 7 | Two Sum Brute Force | Easy | Two nested loops over all pairs. | O(n^2) | O(1) |
| 8 | Two Sum with Hash Map | Easy | One pass storing seen values or complements. | O(n) | O(n) |
| 9 | Merge Sort Analysis | Medium | Use T(n)=2T(n/2)+O(n). | O(n log n) | O(n) |
| 10 | Binary Search Analysis | Easy | Search space halves each step. | O(log n) | O(1) |
| 11 | Naive Fibonacci | Medium | Repeated branching calls create exponential tree. | O(2^n) | O(n) |
| 12 | Memoized Fibonacci | Medium | Each state 0..n computed once. | O(n) | O(n) |

## Arrays and Strings

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 13 | Two Sum | Easy | Hash map from value to index; check complement while scanning. | O(n) | O(n) |
| 14 | Best Time to Buy and Sell Stock | Easy | Track minimum price so far and best profit. | O(n) | O(1) |
| 15 | Product of Array Except Self | Medium | Prefix products then suffix products in reverse. | O(n) | O(1) extra |
| 16 | Maximum Subarray | Medium | Kadane: best subarray ending at current index. | O(n) | O(1) |
| 17 | 3Sum | Medium | Sort, fix one number, use two pointers and skip duplicates. | O(n^2) | O(1) extra |
| 18 | Container With Most Water | Medium | Move shorter wall because height is bottleneck. | O(n) | O(1) |
| 19 | Longest Substring Without Repeating Characters | Medium | Sliding window with last seen indices or set. | O(n) | O(k) |
| 20 | Minimum Window Substring | Hard | Expand to satisfy counts, shrink to minimize. | O(n) | O(k) |
| 21 | Subarray Sum Equals K | Medium | Count previous prefix sums equal to current-prefix minus k. | O(n) | O(n) |
| 22 | Rotate Image | Medium | Transpose then reverse rows, or rotate layer by layer. | O(n^2) | O(1) |
| 23 | Spiral Matrix | Medium | Maintain top/bottom/left/right boundaries. | O(mn) | O(1) extra |

## Linked Lists

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 24 | Reverse Linked List | Easy | Redirect pointers using prev/current/next. | O(n) | O(1) |
| 25 | Merge Two Sorted Lists | Easy | Dummy tail attaches the smaller current node. | O(n+m) | O(1) |
| 26 | Linked List Cycle | Easy | Floyd fast/slow pointers meet if a cycle exists. | O(n) | O(1) |
| 27 | Middle of the Linked List | Easy | Fast moves two steps while slow moves one. | O(n) | O(1) |
| 28 | Remove Nth Node From End | Medium | Dummy plus two pointers separated by n. | O(n) | O(1) |
| 29 | Add Two Numbers | Medium | Simulate digit addition with carry using dummy head. | O(max(n,m)) | O(1) extra |
| 30 | Reorder List | Medium | Find middle, reverse second half, merge alternating. | O(n) | O(1) |
| 31 | Copy List with Random Pointer | Medium | Map original nodes to cloned nodes, then wire pointers. | O(n) | O(n) |
| 32 | Reverse Nodes in k-Group | Hard | Check k nodes exist, reverse segment, reconnect. | O(n) | O(1) |

## Stacks and Queues

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 33 | Valid Parentheses | Easy | Push opens; every close must match stack top. | O(n) | O(n) |
| 34 | Min Stack | Medium | Maintain values plus current minimums. | O(1) per op | O(n) |
| 35 | Evaluate Reverse Polish Notation | Medium | Operators pop two operands and push result. | O(n) | O(n) |
| 36 | Daily Temperatures | Medium | Monotonic decreasing stack of indices waiting for warmer day. | O(n) | O(n) |
| 37 | Largest Rectangle in Histogram | Hard | Increasing stack; pop when height drops to compute widths. | O(n) | O(n) |
| 38 | Sliding Window Maximum | Hard | Deque stores indices in decreasing value order and removes expired front. | O(n) | O(k) |
| 39 | Basic Calculator | Hard | Use stack to handle sign context around parentheses. | O(n) | O(n) |

## Hashing

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 40 | Contains Duplicate | Easy | Compare list length with set length, or scan with seen set. | O(n) | O(n) |
| 41 | Valid Anagram | Easy | Compare character counts. | O(n) | O(k) |
| 42 | Group Anagrams | Medium | Use sorted word or 26-count tuple as canonical key. | O(n*k log k) | O(nk) |
| 43 | Longest Consecutive Sequence | Medium | Only start counting at sequence starts in a set. | O(n) | O(n) |
| 44 | Top K Frequent Elements | Medium | Count frequencies then heap or bucket sort. | O(n log k) or O(n) | O(n) |
| 45 | Subarray Sum Equals K | Medium | Prefix sum count map tracks previous prefixes. | O(n) | O(n) |
| 46 | Isomorphic Strings | Easy | Maintain two maps or map pairs consistently. | O(n) | O(k) |
| 47 | Insert Delete GetRandom O(1) | Medium | List plus map value to index; swap-delete. | O(1) avg | O(n) |

## Recursion and Backtracking

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 48 | Subsets | Medium | Include/exclude each element in a binary decision tree. | O(n*2^n) | O(n) |
| 49 | Permutations | Medium | Try each unused number at each position. | O(n*n!) | O(n) |
| 50 | Combination Sum | Medium | DFS with start index; reuse current candidate when allowed. | Exponential | O(depth) |
| 51 | Generate Parentheses | Medium | Add open if available; add close if valid. | O(Catalan n) | O(n) |
| 52 | Word Search | Medium | Backtrack over grid neighbors while marking visited cells. | O(mn*4^L) | O(L) |
| 53 | Palindrome Partitioning | Medium | Choose palindrome prefixes and recurse on suffix. | O(n*2^n) | O(n) |
| 54 | N-Queens | Hard | Place row by row tracking columns and diagonals. | O(n!) | O(n) |
| 55 | Sudoku Solver | Hard | Fill empty cells using row/col/box constraints. | Exponential | O(1) board |

## Searching and Sorting

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 56 | Sort Colors | Medium | Dutch national flag with low/mid/high pointers. | O(n) | O(1) |
| 57 | Merge Intervals | Medium | Sort by start, merge overlapping intervals. | O(n log n) | O(n) |
| 58 | Kth Largest Element in an Array | Medium | Quickselect average O(n) or heap O(n log k). | O(n) avg | O(1) |
| 59 | Meeting Rooms | Easy | Sort intervals by start and check overlaps. | O(n log n) | O(1) |
| 60 | Wiggle Sort II | Medium/Hard | Median partition; arrange larger/smaller alternately. | O(n) | O(n) or O(1) |
| 61 | Count Inversions | Hard | Merge sort while counting cross inversions. | O(n log n) | O(n) |
| 62 | Largest Number | Medium | Sort numbers by concatenation order. | O(n log n * k) | O(n) |

## Binary Search

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 63 | Binary Search | Easy | Compare middle with target and discard half. | O(log n) | O(1) |
| 64 | First Bad Version | Easy | Find first true predicate. | O(log n) | O(1) |
| 65 | Search Insert Position | Easy | Lower bound for target. | O(log n) | O(1) |
| 66 | Search in Rotated Sorted Array | Medium | Identify sorted half and decide where target can be. | O(log n) | O(1) |
| 67 | Find Minimum in Rotated Sorted Array | Medium | Compare mid with right to locate pivot/minimum. | O(log n) | O(1) |
| 68 | Koko Eating Bananas | Medium | Binary search speed; feasible if hours <= h. | O(n log M) | O(1) |
| 69 | Capacity To Ship Packages Within D Days | Medium | Binary search capacity and simulate days. | O(n log sum) | O(1) |
| 70 | Split Array Largest Sum | Hard | Binary search max subarray sum; greedily count partitions. | O(n log sum) | O(1) |
| 71 | Median of Two Sorted Arrays | Hard | Binary search partition in smaller array. | O(log min(n,m)) | O(1) |

## Trees and Binary Trees

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 72 | Maximum Depth of Binary Tree | Easy | DFS returns 1 + max child depth. | O(n) | O(h) |
| 73 | Invert Binary Tree | Easy | Swap children recursively or iteratively. | O(n) | O(h) |
| 74 | Diameter of Binary Tree | Easy/Medium | Candidate at node is left height + right height. | O(n) | O(h) |
| 75 | Balanced Binary Tree | Easy | Return height or -1 if unbalanced. | O(n) | O(h) |
| 76 | Lowest Common Ancestor of Binary Tree | Medium | Current is LCA if both sides find targets. | O(n) | O(h) |
| 77 | Binary Tree Level Order Traversal | Medium | BFS by queue level sizes. | O(n) | O(w) |
| 78 | Path Sum III | Medium | Prefix sum count map during DFS. | O(n) | O(h) |
| 79 | Construct Binary Tree from Preorder and Inorder | Medium | Use preorder root and inorder index map. | O(n) | O(n) |
| 80 | Serialize and Deserialize Binary Tree | Hard | Preorder or BFS with null markers. | O(n) | O(n) |
| 81 | Binary Tree Maximum Path Sum | Hard | Return downward gain; update through-node path. | O(n) | O(h) |

## Binary Search Trees

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 82 | Validate Binary Search Tree | Medium | DFS with strict low/high bounds. | O(n) | O(h) |
| 83 | Kth Smallest Element in a BST | Medium | Inorder traversal and stop at kth node. | O(h+k) | O(h) |
| 84 | Lowest Common Ancestor of a BST | Medium | Move left/right while both targets are on same side. | O(h) | O(1) |
| 85 | Search in a BST | Easy | Follow left/right based on comparison. | O(h) | O(1) |
| 86 | Delete Node in a BST | Medium | For 2 children replace with successor. | O(h) | O(h) or O(1) |
| 87 | Convert Sorted Array to BST | Easy | Choose middle recursively to build balanced tree. | O(n) | O(log n) |
| 88 | Recover Binary Search Tree | Medium/Hard | Inorder should be sorted; find swapped nodes. | O(n) | O(h) |
| 89 | Inorder Successor in BST | Medium | Use right subtree leftmost or track ancestor. | O(h) | O(1) |

## Heaps and Priority Queues

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 90 | Kth Largest Element in a Stream | Easy | Maintain min-heap of size k. | O(log k) per add | O(k) |
| 91 | Kth Largest Element in an Array | Medium | Min-heap size k or quickselect. | O(n log k) | O(k) |
| 92 | Top K Frequent Elements | Medium | Count then heap by frequency or bucket sort. | O(n log k) | O(n) |
| 93 | Merge k Sorted Lists | Hard | Heap stores current node from each list. | O(N log k) | O(k) |
| 94 | Find Median from Data Stream | Hard | Two heaps: max lower half, min upper half. | O(log n) add | O(n) |
| 95 | Meeting Rooms II | Medium | Sort starts; min-heap of active meeting ends. | O(n log n) | O(n) |
| 96 | Task Scheduler | Medium | Greedy formula or max-heap simulation with cooldown. | O(n) | O(1) |
| 97 | Reorganize String | Medium | Always place most frequent non-conflicting char. | O(n log k) | O(k) |

## Graphs

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 98 | Number of Islands | Medium | DFS/BFS flood fill every unvisited land cell. | O(mn) | O(mn) |
| 99 | Clone Graph | Medium | DFS/BFS with map original node to clone. | O(V+E) | O(V) |
| 100 | Course Schedule | Medium | Topological sort or DFS cycle detection. | O(V+E) | O(V+E) |
| 101 | Pacific Atlantic Water Flow | Medium | Reverse search from both oceans and intersect reachability. | O(mn) | O(mn) |
| 102 | Rotting Oranges | Medium | Multi-source BFS from all rotten oranges. | O(mn) | O(mn) |
| 103 | Word Ladder | Hard | BFS over wildcard-pattern neighbors. | O(N*L^2) | O(N*L) |
| 104 | Graph Valid Tree | Medium | Check edges n-1 and connectivity, or DSU no cycle. | O(V+E) | O(V+E) |
| 105 | Alien Dictionary | Hard | Build character graph from adjacent words and topologically sort. | O(total chars) | O(1) to O(k) |

## Dynamic Programming

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 106 | Climbing Stairs | Easy | dp[i]=dp[i-1]+dp[i-2]. | O(n) | O(1) |
| 107 | House Robber | Medium | At each house choose rob or skip. | O(n) | O(1) |
| 108 | Coin Change | Medium | dp[amount] is min coins to form amount. | O(amount*coins) | O(amount) |
| 109 | Longest Increasing Subsequence | Medium | Patience tails array with binary search. | O(n log n) | O(n) |
| 110 | Longest Common Subsequence | Medium | 2D DP over prefixes. | O(nm) | O(nm) |
| 111 | Edit Distance | Hard | Insert/delete/replace transition over prefixes. | O(nm) | O(nm) |
| 112 | Word Break | Medium | dp[i] true if a valid word ends at i. | O(n^2) | O(n) |
| 113 | Decode Ways | Medium | Ways to decode prefix i from one/two-digit endings. | O(n) | O(1) |
| 114 | Partition Equal Subset Sum | Medium | 0/1 knapsack for target sum/2. | O(n*target) | O(target) |
| 115 | Burst Balloons | Hard | Interval DP choosing last balloon in interval. | O(n^3) | O(n^2) |
| 116 | Regular Expression Matching | Hard | String DP with dot and star transitions. | O(nm) | O(nm) |

## Greedy Algorithms

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 117 | Jump Game | Medium | Track farthest reachable index. | O(n) | O(1) |
| 118 | Jump Game II | Medium | BFS-layer style greedy over current range. | O(n) | O(1) |
| 119 | Gas Station | Medium | If total gas sufficient, reset start when tank goes negative. | O(n) | O(1) |
| 120 | Non-overlapping Intervals | Medium | Sort by end and keep intervals finishing earliest. | O(n log n) | O(1) |
| 121 | Candy | Hard | Two passes satisfy left and right neighbor constraints. | O(n) | O(n) |
| 122 | Partition Labels | Medium | Use last occurrence to close partitions greedily. | O(n) | O(1) |
| 123 | Queue Reconstruction by Height | Medium | Sort taller first, insert by k. | O(n^2) | O(n) |
| 124 | Minimum Arrows to Burst Balloons | Medium | Sort by end; shoot arrow at current end. | O(n log n) | O(1) |
| 125 | Boats to Save People | Medium | Sort weights; pair lightest with heaviest when possible. | O(n log n) | O(1) |

## Tries

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 126 | Implement Trie | Medium | Nested nodes with children map and end marker. | O(L) per op | O(total chars) |
| 127 | Word Search II | Hard | Trie of words plus board DFS with pruning. | O(mn*4^L) worst | O(total chars) |
| 128 | Design Add and Search Words | Medium | Trie plus DFS branching on wildcard dot. | O(26^dots * L) | O(total chars) |
| 129 | Replace Words | Medium | Find shortest root prefix in trie for each word. | O(total chars) | O(dict chars) |
| 130 | Map Sum Pairs | Medium | Trie nodes store prefix sums or deltas. | O(L) per op | O(total chars) |
| 131 | Maximum XOR of Two Numbers | Medium | Binary trie; greedily choose opposite bit. | O(n*bits) | O(n*bits) |

## Intervals and Line Sweep

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 132 | Merge Intervals | Medium | Sort by start and merge overlaps. | O(n log n) | O(n) |
| 133 | Insert Interval | Medium | Add all before, merge overlapping, then add after. | O(n) | O(n) |
| 134 | Meeting Rooms II | Medium | Sort starts and use min-heap of end times. | O(n log n) | O(n) |
| 135 | My Calendar I | Medium | Check if new interval overlaps existing intervals. | O(n) | O(n) |
| 136 | Employee Free Time | Hard | Merge all busy intervals, gaps are free time. | O(n log n) | O(n) |
| 137 | Car Pooling | Medium | Difference array or sorted pickup/drop events. | O(n log n) or O(U) | O(n or U) |
| 138 | The Skyline Problem | Hard | Sweep events with max-heap and lazy deletion. | O(n log n) | O(n) |
| 139 | Minimum Arrows to Burst Balloons | Medium | Sort by end and greedily shoot arrows. | O(n log n) | O(1) |

## Union Find / Disjoint Set Union

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 140 | Number of Connected Components | Medium | Union every edge and count remaining components. | O((V+E) alpha V) | O(V) |
| 141 | Redundant Connection | Medium | First edge whose endpoints are already connected creates cycle. | O(E alpha V) | O(V) |
| 142 | Accounts Merge | Medium | Union accounts sharing emails, group by root. | O(N alpha N) | O(N) |
| 143 | Number of Provinces | Medium | Union connected cities or DFS matrix. | O(n^2 alpha n) | O(n) |
| 144 | Most Stones Removed | Medium | Union stones sharing row/column; answer n-components. | O(n alpha n) | O(n) |
| 145 | Similar String Groups | Hard | Union strings that differ in at most two positions. | O(n^2*m) | O(n) |
| 146 | Min Cost to Connect All Points | Medium | Kruskal MST over all point edges. | O(E log E) | O(E) |

## Segment Tree and Fenwick Tree

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 147 | Range Sum Query Mutable | Medium | Fenwick or segment tree for updates and range sums. | O(log n) op | O(n) |
| 148 | Count of Smaller Numbers After Self | Hard | Coordinate compress; scan right to left with Fenwick counts. | O(n log n) | O(n) |
| 149 | Reverse Pairs | Hard | Fenwick/merge sort counting greater-than-twice relation. | O(n log n) | O(n) |
| 150 | My Calendar III | Hard | Line sweep with ordered map or dynamic segment tree. | O(n log C) | O(n log C) |
| 151 | Falling Squares | Hard | Coordinate compression plus segment tree max range update. | O(n log n) | O(n) |
| 152 | Num Array | Medium | Classic mutable range sum with Fenwick. | O(log n) | O(n) |

## Bit Manipulation

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 153 | Single Number | Easy | XOR all numbers; duplicates cancel. | O(n) | O(1) |
| 154 | Counting Bits | Easy | dp[i]=dp[i>>1]+(i&1). | O(n) | O(n) |
| 155 | Reverse Bits | Easy | Shift result and consume input bits. | O(bits) | O(1) |
| 156 | Missing Number | Easy | XOR indices and values, or use sum formula. | O(n) | O(1) |
| 157 | Sum of Two Integers | Medium | Use XOR for sum and AND-shift for carry. | O(bits) | O(1) |
| 158 | Maximum XOR of Two Numbers | Medium | Greedy prefix set or binary trie. | O(n*bits) | O(n) |
| 159 | Subsets via Bitmask | Medium | Enumerate masks from 0 to 2^n-1. | O(n*2^n) | O(n) |
| 160 | Shortest Superstring | Hard | Bitmask DP over last string and used set. | O(n^2*2^n) | O(n*2^n) |

## Math and Number Theory

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 161 | Pow(x, n) | Medium | Fast exponentiation; handle negative exponent. | O(log n) | O(1) |
| 162 | Sqrt(x) | Easy | Binary search integer square root. | O(log x) | O(1) |
| 163 | Greatest Common Divisor of Strings | Easy | Use concatenation check and gcd of lengths. | O(n+m) | O(1) |
| 164 | Count Primes | Medium | Sieve of Eratosthenes. | O(n log log n) | O(n) |
| 165 | Happy Number | Easy | Cycle detection with set or fast/slow. | O(log n per step) | O(1) or O(k) |
| 166 | Fraction to Recurring Decimal | Medium | Map remainder to output position to detect cycle. | O(length) | O(length) |
| 167 | Random Pick with Weight | Medium | Prefix sums plus binary search random target. | O(log n) pick | O(n) |
| 168 | Nth Magical Number | Hard | Binary search answer with lcm inclusion-exclusion. | O(log answer) | O(1) |

## Advanced Strings

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 169 | Implement strStr | Easy | KMP or built-in for practice; KMP is linear. | O(n+m) | O(m) |
| 170 | Repeated Substring Pattern | Easy | Use prefix function or string trick. | O(n) | O(n) |
| 171 | Longest Happy Prefix | Hard | Last value of KMP prefix table gives longest border. | O(n) | O(n) |
| 172 | Repeated DNA Sequences | Medium | Rolling hash or fixed-length substring set. | O(n) | O(n) |
| 173 | Shortest Palindrome | Hard | KMP on s + separator + reverse(s). | O(n) | O(n) |
| 174 | Longest Palindromic Substring | Medium | Expand around centers or Manacher. | O(n^2) or O(n) | O(1) or O(n) |
| 175 | Distinct Echo Substrings | Hard | Rolling hash compare adjacent equal-length substrings. | O(n^2) | O(n^2) set |

## Advanced Graphs

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 176 | Network Delay Time | Medium | Dijkstra from source over directed weighted graph. | O(E log V) | O(V+E) |
| 177 | Cheapest Flights Within K Stops | Medium | Bellman-Ford style k+1 relaxations or stateful Dijkstra. | O(K E) | O(V) |
| 178 | Min Cost to Connect All Points | Medium | MST using Prim or Kruskal. | O(E log V) | O(E) |
| 179 | Critical Connections in a Network | Hard | Tarjan bridge-finding with discovery and low times. | O(V+E) | O(V+E) |
| 180 | Reconstruct Itinerary | Hard | Hierholzer DFS with lexical min-heaps. | O(E log E) | O(E) |
| 181 | Swim in Rising Water | Hard | Dijkstra/minimax path or binary search + BFS. | O(n^2 log n) | O(n^2) |
| 182 | Find the City With Smallest Number of Neighbors | Medium | Floyd-Warshall or Dijkstra from each city. | O(V^3) | O(V^2) |

## Design Data Structures

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 183 | LRU Cache | Medium | Hash map plus doubly linked list or OrderedDict. | O(1) | O(capacity) |
| 184 | LFU Cache | Hard | Map key->node plus frequency buckets ordered by recency. | O(1) | O(capacity) |
| 185 | Insert Delete GetRandom O(1) | Medium | Array plus map value to index; swap-delete. | O(1) avg | O(n) |
| 186 | Time Based Key-Value Store | Medium | Map key to sorted timestamp-value list; binary search get. | O(log n) get | O(n) |
| 187 | Design Twitter | Medium | User follow graph plus heap merge of recent tweets. | O(f log f) | O(total data) |
| 188 | All O(1) Data Structure | Hard | Doubly linked count buckets plus key map. | O(1) | O(n) |
| 189 | Snapshot Array | Medium | Per-index sorted history and binary search by snapshot id. | O(log updates) | O(updates) |
| 190 | Design Browser History | Medium | Two stacks or dynamic array with current pointer. | O(steps) | O(n) |
| 191 | Design Underground System | Medium | Maps for active trips and aggregate route stats. | O(1) avg | O(n) |

---

## Total questions: 191

How to use this list:

1. First pass: solve topic-by-topic after reading the guide.
2. Second pass: redo only missed/slow problems.
3. Third pass: randomize problems across all topics to simulate real interviews.
4. For every hard problem, write the invariant or proof idea before coding.
