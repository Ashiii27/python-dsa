# Top Interview Questions by Topic

This list is curated from the topic guides. It focuses on patterns commonly seen in high-quality software engineering interviews. Problem names are intentionally concise; write your own full solution notes using `templates/problem-template.md`.

Legend: E = Easy, M = Medium, H = Hard. Solve in topic order first, then mix topics randomly.

## Python Foundations for DSA

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 1 | [Build a Frequency Counter](https://docs.python.org/3/library/collections.html#collections.Counter) | Easy | Use a dict or Counter and increment per item. | O(n) | O(k) |
| 2 | [Group Items by Key](https://docs.python.org/3/library/collections.html#collections.defaultdict) | Easy | Use defaultdict(list) and append into each group. | O(n) | O(n) |
| 3 | [Implement Queue with deque](https://docs.python.org/3/library/collections.html#collections.deque) | Easy | Use append and popleft for true queue operations. | O(1) per op | O(n) |
| 4 | [Sort Records by Multiple Fields](https://docs.python.org/3/howto/sorting.html) | Easy | Use tuple key like (age, -score). | O(n log n) | O(n) |
| 5 | [Top K Values with Heap](https://docs.python.org/3/library/heapq.html) | Medium | Maintain a min-heap of size k. | O(n log k) | O(k) |
| 6 | [Parse and Count Log Events](https://docs.python.org/3/library/stdtypes.html#str.split) | Medium | Split lines, normalize fields, aggregate with maps. | O(total chars) | O(unique keys) |

## Complexity Analysis

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 7 | [Two Sum Brute Force](https://leetcode.com/problems/two-sum/) | Easy | Two nested loops over all pairs. | O(n^2) | O(1) |
| 8 | [Two Sum with Hash Map](https://leetcode.com/problems/two-sum/) | Easy | One pass storing seen values or complements. | O(n) | O(n) |
| 9 | [Merge Sort Analysis](https://en.wikipedia.org/wiki/Merge_sort) | Medium | Use T(n)=2T(n/2)+O(n). | O(n log n) | O(n) |
| 10 | [Binary Search Analysis](https://leetcode.com/problems/binary-search/) | Easy | Search space halves each step. | O(log n) | O(1) |
| 11 | [Naive Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Repeated branching calls create exponential tree. | O(2^n) | O(n) |
| 12 | [Memoized Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Each state 0..n computed once. | O(n) | O(n) |

## Arrays and Strings

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 13 | [Two Sum](https://leetcode.com/problems/two-sum/) · [worked solution](../topics/02-arrays-and-strings/problems/two-sum/README.md) | Easy | Hash map from value to index; check complement while scanning. | O(n) | O(n) |
| 14 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · [worked solution](../topics/02-arrays-and-strings/problems/best-time-to-buy-and-sell-stock/README.md) | Easy | Track minimum price so far and best profit. | O(n) | O(1) |
| 15 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · [worked solution](../topics/02-arrays-and-strings/problems/product-of-array-except-self/README.md) | Medium | Prefix products then suffix products in reverse. | O(n) | O(1) extra |
| 16 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · [worked solution](../topics/02-arrays-and-strings/problems/maximum-subarray/README.md) | Medium | Kadane: best subarray ending at current index. | O(n) | O(1) |
| 17 | [3Sum](https://leetcode.com/problems/3sum/) · [worked solution](../topics/02-arrays-and-strings/problems/3sum/README.md) | Medium | Sort, fix one number, use two pointers and skip duplicates. | O(n^2) | O(1) extra |
| 18 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · [worked solution](../topics/02-arrays-and-strings/problems/container-with-most-water/README.md) | Medium | Move shorter wall because height is bottleneck. | O(n) | O(1) |
| 19 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · [worked solution](../topics/02-arrays-and-strings/problems/longest-substring-without-repeating-characters/README.md) | Medium | Sliding window with last seen indices or set. | O(n) | O(k) |
| 20 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) · [worked solution](../topics/02-arrays-and-strings/problems/minimum-window-substring/README.md) | Hard | Expand to satisfy counts, shrink to minimize. | O(n) | O(k) |
| 21 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · [worked solution](../topics/02-arrays-and-strings/problems/subarray-sum-equals-k/README.md) | Medium | Count previous prefix sums equal to current-prefix minus k. | O(n) | O(n) |
| 22 | [Rotate Image](https://leetcode.com/problems/rotate-image/) · [worked solution](../topics/02-arrays-and-strings/problems/rotate-image/README.md) | Medium | Transpose then reverse rows, or rotate layer by layer. | O(n^2) | O(1) |
| 23 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) · [worked solution](../topics/02-arrays-and-strings/problems/spiral-matrix/README.md) | Medium | Maintain top/bottom/left/right boundaries. | O(mn) | O(1) extra |

## Linked Lists

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 24 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Redirect pointers using prev/current/next. | O(n) | O(1) |
| 25 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Dummy tail attaches the smaller current node. | O(n+m) | O(1) |
| 26 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd fast/slow pointers meet if a cycle exists. | O(n) | O(1) |
| 27 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Fast moves two steps while slow moves one. | O(n) | O(1) |
| 28 | [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end/) | Medium | Dummy plus two pointers separated by n. | O(n) | O(1) |
| 29 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Simulate digit addition with carry using dummy head. | O(max(n,m)) | O(1) extra |
| 30 | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Find middle, reverse second half, merge alternating. | O(n) | O(1) |
| 31 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Map original nodes to cloned nodes, then wire pointers. | O(n) | O(n) |
| 32 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Check k nodes exist, reverse segment, reconnect. | O(n) | O(1) |

## Stacks and Queues

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 33 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Push opens; every close must match stack top. | O(n) | O(n) |
| 34 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Maintain values plus current minimums. | O(1) per op | O(n) |
| 35 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Operators pop two operands and push result. | O(n) | O(n) |
| 36 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic decreasing stack of indices waiting for warmer day. | O(n) | O(n) |
| 37 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Increasing stack; pop when height drops to compute widths. | O(n) | O(n) |
| 38 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Deque stores indices in decreasing value order and removes expired front. | O(n) | O(k) |
| 39 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | Use stack to handle sign context around parentheses. | O(n) | O(n) |

## Hashing

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 40 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Compare list length with set length, or scan with seen set. | O(n) | O(n) |
| 41 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Compare character counts. | O(n) | O(k) |
| 42 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Use sorted word or 26-count tuple as canonical key. | O(n*k log k) | O(nk) |
| 43 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Only start counting at sequence starts in a set. | O(n) | O(n) |
| 44 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count frequencies then heap or bucket sort. | O(n log k) or O(n) | O(n) |
| 45 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · [worked solution](../topics/02-arrays-and-strings/problems/subarray-sum-equals-k/README.md) | Medium | Prefix sum count map tracks previous prefixes. | O(n) | O(n) |
| 46 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | Maintain two maps or map pairs consistently. | O(n) | O(k) |
| 47 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | List plus map value to index; swap-delete. | O(1) avg | O(n) |

## Recursion and Backtracking

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 48 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | Include/exclude each element in a binary decision tree. | O(n*2^n) | O(n) |
| 49 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | Try each unused number at each position. | O(n*n!) | O(n) |
| 50 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | DFS with start index; reuse current candidate when allowed. | Exponential | O(depth) |
| 51 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Add open if available; add close if valid. | O(Catalan n) | O(n) |
| 52 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtrack over grid neighbors while marking visited cells. | O(mn*4^L) | O(L) |
| 53 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | Choose palindrome prefixes and recurse on suffix. | O(n*2^n) | O(n) |
| 54 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Place row by row tracking columns and diagonals. | O(n!) | O(n) |
| 55 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | Fill empty cells using row/col/box constraints. | Exponential | O(1) board |

## Searching and Sorting

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 56 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Dutch national flag with low/mid/high pointers. | O(n) | O(1) |
| 57 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start, merge overlapping intervals. | O(n log n) | O(n) |
| 58 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Quickselect average O(n) or heap O(n log k). | O(n) avg | O(1) |
| 59 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | Sort intervals by start and check overlaps. | O(n log n) | O(1) |
| 60 | [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Medium/Hard | Median partition; arrange larger/smaller alternately. | O(n) | O(n) or O(1) |
| 61 | [Count Inversions](https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-merge-sort/) | Hard | Merge sort while counting cross inversions. | O(n log n) | O(n) |
| 62 | [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | Sort numbers by concatenation order. | O(n log n * k) | O(n) |

## Binary Search

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 63 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Compare middle with target and discard half. | O(log n) | O(1) |
| 64 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | Find first true predicate. | O(log n) | O(1) |
| 65 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Lower bound for target. | O(log n) | O(1) |
| 66 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Identify sorted half and decide where target can be. | O(log n) | O(1) |
| 67 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare mid with right to locate pivot/minimum. | O(log n) | O(1) |
| 68 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary search speed; feasible if hours <= h. | O(n log M) | O(1) |
| 69 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Binary search capacity and simulate days. | O(n log sum) | O(1) |
| 70 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | Binary search max subarray sum; greedily count partitions. | O(n log sum) | O(1) |
| 71 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Binary search partition in smaller array. | O(log min(n,m)) | O(1) |

## Trees and Binary Trees

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 72 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | DFS returns 1 + max child depth. | O(n) | O(h) |
| 73 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Swap children recursively or iteratively. | O(n) | O(h) |
| 74 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy/Medium | Candidate at node is left height + right height. | O(n) | O(h) |
| 75 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | Return height or -1 if unbalanced. | O(n) | O(h) |
| 76 | [Lowest Common Ancestor of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Current is LCA if both sides find targets. | O(n) | O(h) |
| 77 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS by queue level sizes. | O(n) | O(w) |
| 78 | [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Medium | Prefix sum count map during DFS. | O(n) | O(h) |
| 79 | [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder/) | Medium | Use preorder root and inorder index map. | O(n) | O(n) |
| 80 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Preorder or BFS with null markers. | O(n) | O(n) |
| 81 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Return downward gain; update through-node path. | O(n) | O(h) |

## Binary Search Trees

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 82 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | DFS with strict low/high bounds. | O(n) | O(h) |
| 83 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Inorder traversal and stop at kth node. | O(h+k) | O(h) |
| 84 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Move left/right while both targets are on same side. | O(h) | O(1) |
| 85 | [Search in a BST](https://leetcode.com/problems/search-in-a-bst/) | Easy | Follow left/right based on comparison. | O(h) | O(1) |
| 86 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | For 2 children replace with successor. | O(h) | O(h) or O(1) |
| 87 | [Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | Choose middle recursively to build balanced tree. | O(n) | O(log n) |
| 88 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Medium/Hard | Inorder should be sorted; find swapped nodes. | O(n) | O(h) |
| 89 | [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) | Medium | Use right subtree leftmost or track ancestor. | O(h) | O(1) |

## Heaps and Priority Queues

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 90 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | Maintain min-heap of size k. | O(log k) per add | O(k) |
| 91 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Min-heap size k or quickselect. | O(n log k) | O(k) |
| 92 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count then heap by frequency or bucket sort. | O(n log k) | O(n) |
| 93 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Heap stores current node from each list. | O(N log k) | O(k) |
| 94 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Two heaps: max lower half, min upper half. | O(log n) add | O(n) |
| 95 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Sort starts; min-heap of active meeting ends. | O(n log n) | O(n) |
| 96 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Greedy formula or max-heap simulation with cooldown. | O(n) | O(1) |
| 97 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | Always place most frequent non-conflicting char. | O(n log k) | O(k) |

## Graphs

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 98 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | DFS/BFS flood fill every unvisited land cell. | O(mn) | O(mn) |
| 99 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | DFS/BFS with map original node to clone. | O(V+E) | O(V) |
| 100 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Topological sort or DFS cycle detection. | O(V+E) | O(V+E) |
| 101 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Reverse search from both oceans and intersect reachability. | O(mn) | O(mn) |
| 102 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Multi-source BFS from all rotten oranges. | O(mn) | O(mn) |
| 103 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | BFS over wildcard-pattern neighbors. | O(N*L^2) | O(N*L) |
| 104 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | Check edges n-1 and connectivity, or DSU no cycle. | O(V+E) | O(V+E) |
| 105 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) | Hard | Build character graph from adjacent words and topologically sort. | O(total chars) | O(1) to O(k) |

## Dynamic Programming

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 106 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | dp[i]=dp[i-1]+dp[i-2]. | O(n) | O(1) |
| 107 | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | At each house choose rob or skip. | O(n) | O(1) |
| 108 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | dp[amount] is min coins to form amount. | O(amount*coins) | O(amount) |
| 109 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Patience tails array with binary search. | O(n log n) | O(n) |
| 110 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2D DP over prefixes. | O(nm) | O(nm) |
| 111 | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Hard | Insert/delete/replace transition over prefixes. | O(nm) | O(nm) |
| 112 | [Word Break](https://leetcode.com/problems/word-break/) | Medium | dp[i] true if a valid word ends at i. | O(n^2) | O(n) |
| 113 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | Ways to decode prefix i from one/two-digit endings. | O(n) | O(1) |
| 114 | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 knapsack for target sum/2. | O(n*target) | O(target) |
| 115 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | Interval DP choosing last balloon in interval. | O(n^3) | O(n^2) |
| 116 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | String DP with dot and star transitions. | O(nm) | O(nm) |

## Greedy Algorithms

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 117 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Track farthest reachable index. | O(n) | O(1) |
| 118 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | BFS-layer style greedy over current range. | O(n) | O(1) |
| 119 | [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | If total gas sufficient, reset start when tank goes negative. | O(n) | O(1) |
| 120 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end and keep intervals finishing earliest. | O(n log n) | O(1) |
| 121 | [Candy](https://leetcode.com/problems/candy/) | Hard | Two passes satisfy left and right neighbor constraints. | O(n) | O(n) |
| 122 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Use last occurrence to close partitions greedily. | O(n) | O(1) |
| 123 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | Sort taller first, insert by k. | O(n^2) | O(n) |
| 124 | [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end; shoot arrow at current end. | O(n log n) | O(1) |
| 125 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | Sort weights; pair lightest with heaviest when possible. | O(n log n) | O(1) |

## Tries

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 126 | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Nested nodes with children map and end marker. | O(L) per op | O(total chars) |
| 127 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Trie of words plus board DFS with pruning. | O(mn*4^L) worst | O(total chars) |
| 128 | [Design Add and Search Words](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | Trie plus DFS branching on wildcard dot. | O(26^dots * L) | O(total chars) |
| 129 | [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | Find shortest root prefix in trie for each word. | O(total chars) | O(dict chars) |
| 130 | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | Trie nodes store prefix sums or deltas. | O(L) per op | O(total chars) |
| 131 | [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Binary trie; greedily choose opposite bit. | O(n*bits) | O(n*bits) |

## Intervals and Line Sweep

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 132 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start and merge overlaps. | O(n log n) | O(n) |
| 133 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Add all before, merge overlapping, then add after. | O(n) | O(n) |
| 134 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Sort starts and use min-heap of end times. | O(n log n) | O(n) |
| 135 | [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | Check if new interval overlaps existing intervals. | O(n) | O(n) |
| 136 | [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Merge all busy intervals, gaps are free time. | O(n log n) | O(n) |
| 137 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | Difference array or sorted pickup/drop events. | O(n log n) or O(U) | O(n or U) |
| 138 | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | Sweep events with max-heap and lazy deletion. | O(n log n) | O(n) |
| 139 | [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end and greedily shoot arrows. | O(n log n) | O(1) |

## Union Find / Disjoint Set Union

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 140 | [Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Medium | Union every edge and count remaining components. | O((V+E) alpha V) | O(V) |
| 141 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | First edge whose endpoints are already connected creates cycle. | O(E alpha V) | O(V) |
| 142 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Union accounts sharing emails, group by root. | O(N alpha N) | O(N) |
| 143 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | Union connected cities or DFS matrix. | O(n^2 alpha n) | O(n) |
| 144 | [Most Stones Removed](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/) | Medium | Union stones sharing row/column; answer n-components. | O(n alpha n) | O(n) |
| 145 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) | Hard | Union strings that differ in at most two positions. | O(n^2*m) | O(n) |
| 146 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Kruskal MST over all point edges. | O(E log E) | O(E) |

## Segment Tree and Fenwick Tree

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 147 | [Range Sum Query Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Fenwick or segment tree for updates and range sums. | O(log n) op | O(n) |
| 148 | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | Hard | Coordinate compress; scan right to left with Fenwick counts. | O(n log n) | O(n) |
| 149 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | Fenwick/merge sort counting greater-than-twice relation. | O(n log n) | O(n) |
| 150 | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) | Hard | Line sweep with ordered map or dynamic segment tree. | O(n log C) | O(n log C) |
| 151 | [Falling Squares](https://leetcode.com/problems/falling-squares/) | Hard | Coordinate compression plus segment tree max range update. | O(n log n) | O(n) |
| 152 | [Num Array](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Classic mutable range sum with Fenwick. | O(log n) | O(n) |

## Bit Manipulation

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 153 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR all numbers; duplicates cancel. | O(n) | O(1) |
| 154 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | Easy | dp[i]=dp[i>>1]+(i&1). | O(n) | O(n) |
| 155 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | Easy | Shift result and consume input bits. | O(bits) | O(1) |
| 156 | [Missing Number](https://leetcode.com/problems/missing-number/) | Easy | XOR indices and values, or use sum formula. | O(n) | O(1) |
| 157 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | Medium | Use XOR for sum and AND-shift for carry. | O(bits) | O(1) |
| 158 | [Maximum XOR of Two Numbers](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | Greedy prefix set or binary trie. | O(n*bits) | O(n) |
| 159 | [Subsets via Bitmask](https://leetcode.com/problems/subsets/) | Medium | Enumerate masks from 0 to 2^n-1. | O(n*2^n) | O(n) |
| 160 | [Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/) | Hard | Bitmask DP over last string and used set. | O(n^2*2^n) | O(n*2^n) |

## Math and Number Theory

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 161 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | Fast exponentiation; handle negative exponent. | O(log n) | O(1) |
| 162 | [Sqrt(x)](https://leetcode.com/problems/sqrt-x/) | Easy | Binary search integer square root. | O(log x) | O(1) |
| 163 | [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Easy | Use concatenation check and gcd of lengths. | O(n+m) | O(1) |
| 164 | [Count Primes](https://leetcode.com/problems/count-primes/) | Medium | Sieve of Eratosthenes. | O(n log log n) | O(n) |
| 165 | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Cycle detection with set or fast/slow. | O(log n per step) | O(1) or O(k) |
| 166 | [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Medium | Map remainder to output position to detect cycle. | O(length) | O(length) |
| 167 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Medium | Prefix sums plus binary search random target. | O(log n) pick | O(n) |
| 168 | [Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) | Hard | Binary search answer with lcm inclusion-exclusion. | O(log answer) | O(1) |

## Advanced Strings

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 169 | [Implement strStr](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Easy | KMP or built-in for practice; KMP is linear. | O(n+m) | O(m) |
| 170 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | Easy | Use prefix function or string trick. | O(n) | O(n) |
| 171 | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | Hard | Last value of KMP prefix table gives longest border. | O(n) | O(n) |
| 172 | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) | Medium | Rolling hash or fixed-length substring set. | O(n) | O(n) |
| 173 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | Hard | KMP on s + separator + reverse(s). | O(n) | O(n) |
| 174 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Expand around centers or Manacher. | O(n^2) or O(n) | O(1) or O(n) |
| 175 | [Distinct Echo Substrings](https://leetcode.com/problems/distinct-echo-substrings/) | Hard | Rolling hash compare adjacent equal-length substrings. | O(n^2) | O(n^2) set |

## Advanced Graphs

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 176 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra from source over directed weighted graph. | O(E log V) | O(V+E) |
| 177 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Bellman-Ford style k+1 relaxations or stateful Dijkstra. | O(K E) | O(V) |
| 178 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | MST using Prim or Kruskal. | O(E log V) | O(E) |
| 179 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Tarjan bridge-finding with discovery and low times. | O(V+E) | O(V+E) |
| 180 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Hierholzer DFS with lexical min-heaps. | O(E log E) | O(E) |
| 181 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | Hard | Dijkstra/minimax path or binary search + BFS. | O(n^2 log n) | O(n^2) |
| 182 | [Find the City With Smallest Number of Neighbors](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | Floyd-Warshall or Dijkstra from each city. | O(V^3) | O(V^2) |

## Design Data Structures

| # | Problem | Level | Core approach | Time | Space |
|---:|---|---|---|---|---|
| 183 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Hash map plus doubly linked list or OrderedDict. | O(1) | O(capacity) |
| 184 | [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | Map key->node plus frequency buckets ordered by recency. | O(1) | O(capacity) |
| 185 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | Array plus map value to index; swap-delete. | O(1) avg | O(n) |
| 186 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | Map key to sorted timestamp-value list; binary search get. | O(log n) get | O(n) |
| 187 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | User follow graph plus heap merge of recent tweets. | O(f log f) | O(total data) |
| 188 | [All O(1) Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Hard | Doubly linked count buckets plus key map. | O(1) | O(n) |
| 189 | [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | Per-index sorted history and binary search by snapshot id. | O(log updates) | O(updates) |
| 190 | [Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | Two stacks or dynamic array with current pointer. | O(steps) | O(n) |
| 191 | [Design Underground System](https://leetcode.com/problems/design-underground-system/) | Medium | Maps for active trips and aggregate route stats. | O(1) avg | O(n) |

---

## Total questions: 191

How to use this list:

1. First pass: solve topic-by-topic after reading the guide.
2. Second pass: redo only missed/slow problems.
3. Third pass: randomize problems across all topics to simulate real interviews.
4. For every hard problem, write the invariant or proof idea before coding.
