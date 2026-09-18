# Stacks And Queues — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Push opens; every close must match stack top. | O(n) | O(n) |
| [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | Maintain values plus current minimums. | O(1) per op | O(n) |
| [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Operators pop two operands and push result. | O(n) | O(n) |
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Monotonic decreasing stack of indices waiting for warmer day. | O(n) | O(n) |
| [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Increasing stack; pop when height drops to compute widths. | O(n) | O(n) |
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Deque stores indices in decreasing value order and removes expired front. | O(n) | O(k) |
| [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | Use stack to handle sign context around parentheses. | O(n) | O(n) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
