# Complexity Analysis and Python-Specific Costs

Big-O tells you how performance scales. In interviews, combine Big-O with constraint reading and Python operation awareness.

---

## Common growth rates

| Complexity | Meaning | Common examples |
|---|---|---|
| `O(1)` | constant | hash lookup average, array index |
| `O(log n)` | divide each step | binary search, heap height |
| `O(n)` | scan once | two pointers, BFS over nodes |
| `O(n log n)` | divide+merge or sorting | merge sort, heap sort, sort + scan |
| `O(n^2)` | all pairs | many DP tables, pair loops |
| `O(2^n)` | all subsets | subset backtracking |
| `O(n!)` | all permutations | permutation generation |

---

## Python operation cheat sheet

| Operation | Average complexity | Notes |
|---|---:|---|
| `arr[i]` | `O(1)` | list index |
| `arr.append(x)` | amortized `O(1)` | occasional resize |
| `arr.pop()` | `O(1)` | pop from end |
| `arr.pop(0)` | `O(n)` | shifts all elements; use `deque.popleft()` |
| `x in list` | `O(n)` | scan |
| `x in set` / `x in dict` | average `O(1)` | hash table |
| `dict[key] = value` | average `O(1)` | collision worst cases ignored in interviews |
| `s += char` in loop | can become `O(n^2)` | collect list and `''.join(...)` |
| `s[l:r]` | `O(r-l)` | slicing copies |
| `arr[l:r]` | `O(r-l)` | slicing copies |
| `sorted(arr)` | `O(n log n)` | creates new list |
| `arr.sort()` | `O(n log n)` | in-place |
| `heapq.heappush/pop` | `O(log n)` | min-heap |
| `deque.append/popleft` | `O(1)` | queue operations |

---

## Amortized analysis

A Python list append is amortized `O(1)` because resizing is occasional. Most appends are constant; rare expensive resizes are spread over many cheap operations.

Other amortized examples:

- dynamic arrays
- hash table resizing
- monotonic stack where each item is pushed and popped once
- sliding window where each pointer moves at most `n` times

---

## Recursion complexity

For recursive algorithms, count the number of subproblems, work per subproblem, and recursion depth for space.

```text
Binary tree DFS:
Time O(n): each node once
Space O(h): recursion depth, h = tree height

Merge sort:
Time O(n log n): log n levels, n work each level
Space O(n): temporary arrays

Naive Fibonacci:
Time O(2^n): repeated overlapping calls
Space O(n): maximum call depth
```

---

## Complexity traps

### Slicing in recursion

```python
left = arr[:mid]   # copies
right = arr[mid:]  # copies
```

Prefer indices for performance-sensitive code.

### String building

```python
# Potentially quadratic
ans = ""
for ch in chars:
    ans += ch

# Better
ans = "".join(chars)
```

### Sorting inside a loop

```python
for item in items:
    values.sort()  # often accidental O(n^2 log n)
```

Consider heap, balanced structure, counting, or one final sort.

### Recursion limit

Python's default recursion limit is often around 1000. For deep trees/graphs, use iterative DFS or carefully adjust:

```python
import sys
sys.setrecursionlimit(300_000)
```

Use this with care: raising the limit does not remove memory limits.

---

## Interview explanation examples

Sliding window:

```text
Time is O(n) because left and right each move at most n times. Even though there is a nested while loop, every iteration advances left, so total movement is linear.
Space is O(k) or O(charset) for the frequency map.
```

Monotonic stack:

```text
Time is O(n) because each index is pushed once and popped once. Space is O(n) in the worst case for the stack.
```

Dijkstra:

```text
Time is O(E log V) using a binary heap. Some nodes may appear in the heap multiple times due to stale entries, but each edge relaxation can push at most one new candidate distance.
Space is O(V + E) for the graph and distance structures.
```
