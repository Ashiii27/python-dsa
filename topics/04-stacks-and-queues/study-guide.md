# Stacks and Queues: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A stack resolves nested or “most recent unresolved” relationships; a queue processes states in arrival or distance order. Monotonic variants retain only candidates that can still matter.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Stacks are LIFO and naturally model parsing, undo, and DFS. |
| 2 | Queues are FIFO and naturally model BFS and scheduling. |
| 3 | Monotonic stacks find next/previous greater or smaller boundaries. |
| 4 | Monotonic deques maintain a window optimum. |
| 5 | Two stacks can reverse order to implement a queue. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Nested delimiters | Stack |
| Next greater/smaller | Monotonic stack |
| Shortest unweighted steps | Queue/BFS |
| Window maximum | Monotonic deque |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For temperatures `[73, 71, 75]`, push indices 0 and 1 on a decreasing stack. At 75, pop 1 and 0: waits are `2-1=1` and `2-0=2`. Every index is pushed and popped once, so the scan is O(n).

## Tricks and interview notes

- Store indices when answers depend on distance or width.
- Add a sentinel bar of height zero to flush a histogram stack.
- For RPN, preserve operand order: second pop is the left operand.
- In a monotonic deque, remove expired indices before reading the front.

## Common mistakes

- **Watch for:** Using a stack of values when duplicate indices matter.
- **Watch for:** Marking BFS nodes visited only when dequeued.
- **Watch for:** Using floating division instead of truncation toward zero in RPN.
- **Watch for:** Forgetting width boundaries after popping a histogram bar.

## Implementation drills

1. Implement a queue with two stacks.
2. Derive next-greater element in both directions.
3. Implement a min stack with paired minima.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Stack, queue, and queue-from-stacks

```python
from collections import deque


class Stack:
    """LIFO. Built on a list: append/pop at the END are O(1) amortised."""

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def __repr__(self):
        return f"Stack(bottom -> top: {self._data})"


class Queue:
    """FIFO. Built on deque: popleft() is O(1), while list.pop(0) is O(n)."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self):
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return bool(self._data)

    def __repr__(self):
        return f"Queue(front -> back: {list(self._data)})"


class QueueFromStacks:
    """A queue from two stacks: amortised O(1) per operation.

    _in accepts pushes; _out serves pops. Elements are poured from _in into
    _out only when _out is empty, which reverses them a second time and
    restores FIFO order. Each element is moved at most once.
    """

    def __init__(self):
        self._in, self._out = [], []

    def push(self, item):
        self._in.append(item)

    def pop(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        if not self._out:
            raise IndexError("pop from empty queue")
        return self._out.pop()

    def __len__(self):
        return len(self._in) + len(self._out)

    def __repr__(self):
        return f"QueueFromStacks({self._out[::-1] + self._in})"


if __name__ == "__main__":
    stack = Stack()
    for ch in "abc":
        stack.push(ch)
    print(stack, "| peek:", stack.peek())
    print("pop order:", [stack.pop() for _ in range(len(stack))], "| empty:", len(stack) == 0)

    queue = Queue()
    for ch in "abc":
        queue.enqueue(ch)
    print(queue, "| peek:", queue.peek())
    print("dequeue order:", [queue.dequeue() for _ in range(len(queue))])

    q2 = QueueFromStacks()
    for x in (1, 2, 3):
        q2.push(x)
    print("after pushes:", q2)
    print("pop:", q2.pop())
    q2.push(4)
    print("mixed push/pop stays FIFO:", [q2.pop() for _ in range(len(q2))])
```

Output:

```text
Stack(bottom -> top: ['a', 'b', 'c']) | peek: c
pop order: ['c', 'b', 'a'] | empty: True
Queue(front -> back: ['a', 'b', 'c']) | peek: a
dequeue order: ['a', 'b', 'c']
after pushes: QueueFromStacks([1, 2, 3])
pop: 1
mixed push/pop stays FIFO: [2, 3, 4]
```

**How it works**

- A Python `list` is already a stack: `append` and `pop()` (no index) are O(1). Never use `insert(0, x)` or `pop(0)` on a list — both shift every element and are O(n).
- `deque` is a doubly linked block structure: O(1) at both ends. Use it for queues, BFS, and sliding windows.
- In `QueueFromStacks` the expensive pour happens only when `_out` is empty, so each element is pushed/popped at most twice in total: amortised O(1), worst case O(n) for a single operation. This is the same amortised argument as dynamic-array resizing.

### 2. Monotonic stack

A stack whose values are kept in one order (increasing or decreasing). It answers
"next greater/smaller element" for every position in O(n), because each index is
pushed once and popped once.

```python
def next_greater_element(nums):
    """For each index, the next value to the right that is greater (-1 if none)."""
    answer = [-1] * len(nums)
    stack = []                                  # indices, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:    # x is the answer for these
            answer[stack.pop()] = x
        stack.append(i)
    return answer


def daily_temperatures(temps):
    """Days to wait until a warmer temperature (0 if never)."""
    answer = [0] * len(temps)
    stack = []                                  # indices, temperatures decreasing
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


def largest_rectangle_area(heights):
    """Biggest rectangle in a histogram: pop when a shorter bar arrives."""
    stack = []                                  # indices, heights increasing
    best = 0
    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0     # sentinel flushes the stack
        while stack and heights[stack[-1]] > current:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            best = max(best, height * (i - left - 1))
        stack.append(i)
    return best


if __name__ == "__main__":
    print("next greater:", next_greater_element([2, 1, 2, 4, 3]))
    print("daily temps :", daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("largest rect:", largest_rectangle_area([2, 1, 5, 6, 2, 3]))
    print("no greater  :", next_greater_element([5, 4, 3, 2, 1]))
```

Output:

```text
next greater: [4, 2, 4, -1, -1]
daily temps : [1, 1, 4, 2, 1, 1, 0, 0]
largest rect: 10
no greater  : [-1, -1, -1, -1, -1]
```

**How it works**

- Store **indices**, not values: you need the distance (`daily_temperatures`) or the width (`largest_rectangle_area`), not just the number.
- The `while` loop is the whole algorithm: a new element resolves every stack entry it dominates, then it is pushed. Total work is O(n) because each index enters and leaves once.
- `largest_rectangle_area` appends a sentinel height of 0 at `i = len(heights)` so the remaining stack is flushed; the width of a popped bar is `i − left − 1` where `left` is the index now on top (the first bar shorter to the left).

### 3. Monotonic deque and the min-stack

A monotonic deque keeps candidates in order at both ends, which is what
sliding-window extremes need. A min-stack keeps the current minimum next to each
element so `get_min` stays O(1).

```python
from collections import deque


def sliding_window_max(nums, k):
    """Maximum of every k-sized window in O(n)."""
    dq = deque()                       # indices, values decreasing
    result = []
    for i, x in enumerate(nums):
        if dq and dq[0] <= i - k:      # index fell out of the window
            dq.popleft()
        while dq and nums[dq[-1]] < x: # smaller candidates can never win
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]]) # front is the window maximum
    return result


class MinStack:
    """Stack with O(1) push, pop, top and get_min."""

    def __init__(self):
        self._stack = []               # (value, minimum up to here)

    def push(self, value):
        current_min = value if not self._stack else min(value, self._stack[-1][1])
        self._stack.append((value, current_min))

    def pop(self):
        if not self._stack:
            raise IndexError("pop from empty stack")
        return self._stack.pop()[0]

    def top(self):
        return self._stack[-1][0]

    def get_min(self):
        return self._stack[-1][1]

    def __len__(self):
        return len(self._stack)


if __name__ == "__main__":
    print("window max k=3:", sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print("k=1:", sliding_window_max([4, 2, 9], 1))
    print("k=len:", sliding_window_max([4, 2, 9], 3))

    ms = MinStack()
    for value in (5, 3, 7, 3, 2):
        ms.push(value)
        print(f"push {value}: min = {ms.get_min()}")
    print("pop:", ms.pop(), "-> min:", ms.get_min())
```

Output:

```text
window max k=3: [3, 3, 5, 5, 6, 7]
k=1: [4, 2, 9]
k=len: [9]
push 5: min = 5
push 3: min = 3
push 7: min = 3
push 3: min = 3
push 2: min = 2
pop: 2 -> min: 3
```

**How it works**

- In `sliding_window_max` the deque holds indices in decreasing value order. Popping from the back removes values that can never become the maximum (the new value is both larger and newer, so it outlives them).
- Expiry check `dq[0] <= i − k` runs before insertion, so the front is always inside the current window.
- `MinStack` stores the running minimum with each element instead of a second sorted structure: no extra lookups, and popping restores the previous minimum automatically.

## Solved examples

### Example 1 — Valid parentheses (Easy)

**Problem.** Given a string of `()[]{}`, decide whether the brackets are properly
opened and closed in the right order.

**Approach.** Push every opener. On a closer, the stack top must be the matching opener; otherwise the string is invalid. At the end the stack must be empty — this catches unclosed openers, which is the case a naive counter misses.

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:                       # a closer
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:                                 # an opener
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    for test in ("()", "()[]{}", "(]", "([)]", "{[]}", "(((", "())"):
        print(f"{test:<8} -> {is_valid(test)}")
    print("empty string:", is_valid(""))
```

Output:

```text
()       -> True
()[]{}   -> True
(]       -> False
([)]     -> False
{[]}     -> True
(((      -> False
())      -> False
empty string: True
```

**Complexity.** O(n) time, O(n) space in the worst case (all openers). This "match against the most recent opener" idea is the same one behind evaluating expressions, decoding strings, and simplifying paths.

### Example 2 — Asteroid collision (Medium)

**Problem.** Asteroids move along a line, positive = right, negative = left. When
two meet, the smaller explodes; equal sizes both explode. Return what survives.

**Approach.** Simulate with a stack of survivors. A collision can only happen when the top of the stack moves right (`> 0`) and the incoming asteroid moves left (`< 0`) — every other case is simply a push. Resolve collisions in a loop, since one asteroid can destroy several.

```python
def asteroid_collision(asteroids):
    stack = []
    for size in asteroids:
        alive = True
        while alive and size < 0 and stack and stack[-1] > 0:
            if stack[-1] < -size:             # top is smaller: it explodes, keep going
                stack.pop()
                continue
            if stack[-1] == -size:            # equal: both explode
                stack.pop()
            alive = False                     # incoming is destroyed (or equal)
        if alive:
            stack.append(size)
    return stack


if __name__ == "__main__":
    print(asteroid_collision([5, 10, -5]))        # [5, 10]
    print(asteroid_collision([8, -8]))            # []
    print(asteroid_collision([10, 2, -5]))        # [10]
    print(asteroid_collision([-2, -1, 1, 2]))     # [-2, -1, 1, 2]  (never meet)
    print("no asteroids:", asteroid_collision([]))
```

Output:

```text
[5, 10]
[]
[10]
[-2, -1, 1, 2]
no asteroids: []
```

**Complexity.** O(n) time (each asteroid is pushed once and popped at most once) and O(n) space. The `while` condition encodes exactly the collision case — getting that guard right is the whole problem.

### Example 3 — Largest rectangle in a histogram (Hard)

**Problem.** Given bar heights, find the largest rectangle that fits under the
histogram.

**Approach.** For each bar used as the rectangle's height, the widest possible rectangle stretches until the first shorter bar on each side. A monotonically increasing stack of indices finds both boundaries in one pass: when a shorter bar arrives, the bars taller than it are finalized — their right boundary is the current index and their left boundary is the new stack top.

```python
def largest_rectangle_area(heights):
    stack = []                                   # indices with increasing heights
    best = 0
    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0    # sentinel: flush at the end
        while stack and heights[stack[-1]] > current:
            height = heights[stack.pop()]
            left_boundary = stack[-1] if stack else -1
            width = i - left_boundary - 1
            best = max(best, height * width)
        stack.append(i)
    return best


def maximal_rectangle(matrix):
    """Same idea in 2D: treat each row as a histogram of consecutive 1-columns."""
    if not matrix:
        return 0
    heights = [0] * len(matrix[0])
    best = 0
    for row in matrix:
        heights = [h + 1 if cell == "1" else 0 for h, cell in zip(heights, row)]
        best = max(best, largest_rectangle_area(heights))
    return best


if __name__ == "__main__":
    print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))     # 10
    print(largest_rectangle_area([2, 4]))                 # 4
    print("empty:", largest_rectangle_area([]))
    grid = [["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
    print("maximal rectangle in binary matrix:", maximal_rectangle(grid))
```

Output:

```text
10
4
empty: 0
maximal rectangle in binary matrix: 6
```

**Complexity.** O(n) time and O(n) space for the histogram; the 2D extension is O(rows · cols). The sentinel `0` at the end is what makes the final bars pop without a special case.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Alternating Current](https://codeforces.com/problemset/problem/343/B) | Codeforces | Easy |
| [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | LeetCode | Medium |
| [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | LeetCode | Medium |
| [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain stacks are lifo and naturally model parsing, undo, and dfs without notes.
- [ ] Explain queues are fifo and naturally model bfs and scheduling without notes.
- [ ] Explain monotonic stacks find next/previous greater or smaller boundaries without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
