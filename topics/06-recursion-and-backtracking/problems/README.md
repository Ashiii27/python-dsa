# Recursion And Backtracking — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

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

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
