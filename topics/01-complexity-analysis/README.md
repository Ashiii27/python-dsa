# Complexity Analysis

**Level:** Beginner

Estimate time and space, compare approaches, and read constraints like interview hints.

---

## What you must learn

- Big-O, Big-Theta, Big-Omega
- Worst-case vs average-case
- Amortized analysis
- Space complexity and recursion stack
- Recurrence relations and recursion trees
- Constraint-based algorithm selection

---

## Core patterns and approaches

- Nested independent loops often multiply
- Sequential loops add then simplify
- Divide-by-two loops are logarithmic
- Each push/pop once often means amortized linear
- Memoization turns repeated recursion into states times transitions

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def logarithmic_steps(n: int) -> int:
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

# Binary search halves the search space -> O(log n).
# A single scan where each pointer only moves forward -> O(n).
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Two Sum Brute Force](https://leetcode.com/problems/two-sum/) | Easy | Two nested loops over all pairs. | O(n^2) | O(1) |
| [Two Sum with Hash Map](https://leetcode.com/problems/two-sum/) | Easy | One pass storing seen values or complements. | O(n) | O(n) |
| [Merge Sort Analysis](https://en.wikipedia.org/wiki/Merge_sort) | Medium | Use T(n)=2T(n/2)+O(n). | O(n log n) | O(n) |
| [Binary Search Analysis](https://leetcode.com/problems/binary-search/) | Easy | Search space halves each step. | O(log n) | O(1) |
| [Naive Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Repeated branching calls create exponential tree. | O(2^n) | O(n) |
| [Memoized Fibonacci](https://leetcode.com/problems/fibonacci-number/) | Medium | Each state 0..n computed once. | O(n) | O(n) |

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
4. Browse the topic [`problems/`](problems/README.md) index for prompt links and worked solutions.
