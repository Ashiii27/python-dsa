# Stacks and Queues

**Level:** Core

Use LIFO/FIFO structures for parsing, simulation, monotonic candidates, and shortest-step traversal.

---

## What you must learn

- Stack LIFO behavior
- Queue FIFO behavior
- Deque operations
- Monotonic stacks
- Monotonic queues
- Expression parsing
- BFS levels

---

## Core patterns and approaches

- Parentheses problems keep unmatched opens on a stack
- Next greater/smaller uses a monotonic stack of unresolved indices
- Sliding window max uses a decreasing deque of candidate indices
- BFS uses a queue and often tracks distance or level size
- Calculator problems use stacks for signs, numbers, or operators

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Valid Parentheses | Easy | Push opens; every close must match stack top. | O(n) | O(n) |
| Min Stack | Medium | Maintain values plus current minimums. | O(1) per op | O(n) |
| Evaluate Reverse Polish Notation | Medium | Operators pop two operands and push result. | O(n) | O(n) |
| Daily Temperatures | Medium | Monotonic decreasing stack of indices waiting for warmer day. | O(n) | O(n) |
| Largest Rectangle in Histogram | Hard | Increasing stack; pop when height drops to compute widths. | O(n) | O(n) |
| Sliding Window Maximum | Hard | Deque stores indices in decreasing value order and removes expired front. | O(n) | O(k) |
| Basic Calculator | Hard | Use stack to handle sign context around parentheses. | O(n) | O(n) |

---

## Mastery checklist

- [ ] I can explain the main idea without looking at notes.
- [ ] I can implement the canonical template from memory.
- [ ] I can solve the easy problems in under 10 minutes each.
- [ ] I can solve most medium problems in 20-35 minutes.
- [ ] I can explain brute force, optimized approach, proof idea, and complexity.
- [ ] I can identify edge cases before coding.

---

## Next steps

1. Read the related sections in [`docs/patterns-cheatsheet.md`](../../docs/patterns-cheatsheet.md).
2. Implement the relevant template from [`templates/python_dsa_templates.py`](../../templates/python_dsa_templates.py) without looking.
3. Add solved problems and mistakes to [`practice/study-tracker.md`](../../practice/study-tracker.md).
