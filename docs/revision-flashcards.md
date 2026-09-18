# DSA Revision Flashcards

Use these for active recall: hide the answer, answer aloud, then rate the card **again**, **hard**, or **easy**. Revisit failed cards after 1 day, 3 days, 1 week, and 1 month.

## Python and complexity

<details><summary>Why use <code>deque.popleft()</code> instead of <code>list.pop(0)</code>?</summary>

A deque removes from either end in O(1); removing index zero from a list shifts the remaining elements and costs O(n).
</details>

<details><summary>When is dictionary lookup not strictly O(1)?</summary>

It is O(1) average/amortized. Hash collisions and resizing can make an individual operation slower; pathological collisions can degrade the worst case.
</details>

<details><summary>What does amortized complexity mean?</summary>

A sequence of operations has a bounded average cost even though occasional individual operations, such as list resizing, are expensive.
</details>

<details><summary>How should constraints guide an approach?</summary>

Roughly: n around 20 suggests exponential/bitmasking; 10³ may allow O(n²); 10⁵ usually needs O(n log n) or O(n); 10⁹ often suggests O(log n) or mathematics.
</details>

## Arrays, strings, and hashing

<details><summary>What is the two-pointer discard proof?</summary>

Show that moving one boundary cannot remove an unseen optimal answer. In Container With Most Water, moving the taller wall cannot improve area while the shorter wall remains and width decreases.
</details>

<details><summary>Fixed window or variable window?</summary>

Use a fixed window when candidate length is prescribed. Use a variable window when validity changes monotonically as either boundary moves.
</details>

<details><summary>Why does prefix-sum counting work with negative numbers?</summary>

It does not rely on monotonic sums. At prefix p, each previous prefix p-k identifies a subarray summing to k, regardless of element signs.
</details>

<details><summary>Why initialize a prefix-count map with <code>{0: 1}</code>?</summary>

It represents the empty prefix, allowing a valid subarray that starts at index zero to be counted.
</details>

<details><summary>When is sorting strings for anagram keys preferable to count tuples?</summary>

Sorting is alphabet-independent and concise. Fixed count tuples are faster for a small known alphabet because they avoid O(k log k) sorting per word.
</details>

## Linked lists, stacks, and queues

<details><summary>Why use a dummy linked-list head?</summary>

It removes special cases when the real head is inserted, removed, or replaced, so every operation has a predecessor node.
</details>

<details><summary>What does Floyd's cycle algorithm guarantee?</summary>

If a cycle exists, pointers moving one and two steps eventually meet. Resetting one to the head and moving both one step locates the cycle entrance.
</details>

<details><summary>What is stored in a monotonic stack?</summary>

Usually indices whose answer is unresolved, ordered by their values. A new value pops entries for which it provides the next boundary.
</details>

<details><summary>When should visited state be set in BFS?</summary>

When enqueuing. Waiting until dequeue can enqueue the same node many times.
</details>

## Searching, sorting, and binary search

<details><summary>What are the three requirements for binary search on an answer?</summary>

An ordered answer domain, a monotonic feasibility predicate, and known feasible/impossible boundaries (or a range containing the transition).
</details>

<details><summary>What does lower bound return?</summary>

The first index whose value is greater than or equal to the target; equivalently, the first position where inserting the target preserves order.
</details>

<details><summary>What is quickselect's complexity?</summary>

O(n) expected time and O(n²) worst-case time; random pivots make the worst case unlikely. In-place partitioning can use O(1) auxiliary space.
</details>

<details><summary>Why is merge sort useful for inversion counting?</summary>

When a right-half item precedes the current left-half item during merge, it forms inversions with every unmerged left-half item.
</details>

## Trees, BSTs, and heaps

<details><summary>What is the key BST validation mistake?</summary>

Comparing a node only with its parent. Every node must satisfy strict lower and upper bounds inherited from all ancestors.
</details>

<details><summary>What is tree recursion space complexity?</summary>

O(h) call-stack space, where h is tree height: O(log n) for a balanced tree and O(n) for a skewed tree.
</details>

<details><summary>Why use two heaps for a running median?</summary>

A max-heap stores the lower half and a min-heap stores the upper half. Balancing their sizes exposes the middle value or values at the roots.
</details>

<details><summary>Min-heap of size k or max-heap of all n?</summary>

For top k from n items, a min-heap of size k uses O(k) space and O(n log k) time; its root is the weakest retained item.
</details>

## Graphs and Union Find

<details><summary>BFS or Dijkstra?</summary>

BFS finds shortest paths when every edge has equal weight. Dijkstra handles non-negative varying weights by expanding the smallest tentative distance.
</details>

<details><summary>How does Kahn's topological sort detect a cycle?</summary>

If fewer than V nodes can be removed through indegree-zero processing, the remaining nodes are part of or depend on a directed cycle.
</details>

<details><summary>What makes multi-source BFS correct?</summary>

Enqueueing every source at distance zero is equivalent to adding a virtual super-source with zero-cost edges, so layers give distance to the nearest source.
</details>

<details><summary>What are the two Union Find optimizations?</summary>

Path compression during find and union by size/rank. Together they give near-constant amortized operations, O(alpha(n)).
</details>

<details><summary>Why can Dijkstra fail on negative edges?</summary>

A node considered final can later receive a shorter path through a negative edge, violating the greedy finalization argument.
</details>

## Recursion and backtracking

<details><summary>What are the four parts of a backtracking function?</summary>

A base case, candidate choices, constraint/pruning checks, and choose–recurse–undo state management.
</details>

<details><summary>How do you avoid duplicate combinations?</summary>

Sort candidates, use a start index, and skip equal values at the same decision-tree depth while still allowing them at different depths when permitted.
</details>

<details><summary>When should memoization replace plain recursion?</summary>

When different recursion paths reach the same state and the result depends only on that state rather than path-specific mutable context.
</details>

## Dynamic programming and greedy

<details><summary>What defines a good DP state?</summary>

It contains exactly the information needed to determine future choices and results—enough for a valid transition, but no irrelevant history.
</details>

<details><summary>Memoization or tabulation?</summary>

Memoization is demand-driven and often easier to derive. Tabulation avoids recursion depth, has predictable iteration, and can make memory optimization clearer.
</details>

<details><summary>When can a 2D DP be compressed?</summary>

When each transition reads only a fixed number of prior rows/columns. Preserve update order so values are not overwritten before use.
</details>

<details><summary>What constitutes a greedy proof?</summary>

Usually an exchange argument, stays-ahead argument, or invariant showing a locally optimal choice can belong to some global optimum.
</details>

## Advanced structures and strings

<details><summary>Fenwick tree or segment tree?</summary>

Fenwick trees are compact and simple for prefix-combinable operations such as sums. Segment trees support broader range queries/updates and richer node state.
</details>

<details><summary>What does KMP's prefix table store?</summary>

At each position, the length of the longest proper prefix of the pattern that is also a suffix ending there, enabling reuse after mismatch.
</details>

<details><summary>What collision issue comes with rolling hashes?</summary>

Different strings can share a hash. Use double hashing or verify matching substrings when correctness must be deterministic.
</details>

<details><summary>How does an O(1) RandomizedSet work?</summary>

A list provides random indexing and a map stores each value's list index. Deletion swaps the target with the last value, updates its index, then pops.
</details>

<details><summary>What is the LRU cache invariant?</summary>

The map points to every live node, while a doubly linked list orders exactly those nodes from least to most recently used; every access moves one node to the recent end.
</details>
