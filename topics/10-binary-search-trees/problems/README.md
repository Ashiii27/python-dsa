# Binary Search Trees — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | DFS with strict low/high bounds. | O(n) | O(h) |
| [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | Inorder traversal and stop at kth node. | O(h+k) | O(h) |
| [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Move left/right while both targets are on same side. | O(h) | O(1) |
| [Search in a BST](https://leetcode.com/problems/search-in-a-bst/) | Easy | Follow left/right based on comparison. | O(h) | O(1) |
| [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | For 2 children replace with successor. | O(h) | O(h) or O(1) |
| [Convert Sorted Array to BST](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) | Easy | Choose middle recursively to build balanced tree. | O(n) | O(log n) |
| [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Medium/Hard | Inorder should be sorted; find swapped nodes. | O(n) | O(h) |
| [Inorder Successor in BST](https://leetcode.com/problems/inorder-successor-in-bst/) | Medium | Use right subtree leftmost or track ancestor. | O(h) | O(1) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
