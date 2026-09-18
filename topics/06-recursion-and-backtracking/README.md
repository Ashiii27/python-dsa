# Recursion and Backtracking

**Level:** Core to Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Explore decision trees, generate combinations/permutations, and solve constraint-search problems with pruning.

---

## What you must learn

- Base cases
- Recursive call stack
- Decision tree modeling
- Choose/explore/unchoose
- Pruning invalid branches
- Duplicate handling
- Backtracking on grids

---

## Core patterns and approaches

- For subsets, choose include/exclude at each index
- For permutations, choose each unused element
- For combinations, carry a start index to avoid reordering duplicates
- For grid search, mark visited, explore neighbors, unmark
- For constraints, prune as soon as partial state cannot become valid

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def subsets(nums):
    ans, path = [], []
    def backtrack(i):
        if i == len(nums):
            ans.append(path.copy()); return
        backtrack(i + 1)
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
    backtrack(0)
    return ans
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Subsets](https://leetcode.com/problems/subsets/) | Medium | Include/exclude each element in a binary decision tree. | O(n*2^n) | O(n) |
| [Permutations](https://leetcode.com/problems/permutations/) | Medium | Try each unused number at each position. | O(n*n!) | O(n) |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | DFS with start index; reuse current candidate when allowed. | Exponential | O(depth) |
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | Add open if available; add close if valid. | O(Catalan n) | O(n) |
| [Word Search](https://leetcode.com/problems/word-search/) | Medium | Backtrack over grid neighbors while marking visited cells. | O(mn*4^L) | O(L) |
| [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | Choose palindrome prefixes and recurse on suffix. | O(n*2^n) | O(n) |
| [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Place row by row tracking columns and diagonals. | O(n!) | O(n) |
| [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | Fill empty cells using row/col/box constraints. | Exponential | O(1) board |

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
