# Trees And Binary Trees — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | DFS returns 1 + max child depth. | O(n) | O(h) |
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Swap children recursively or iteratively. | O(n) | O(h) |
| [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy/Medium | Candidate at node is left height + right height. | O(n) | O(h) |
| [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | Return height or -1 if unbalanced. | O(n) | O(h) |
| [Lowest Common Ancestor of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Current is LCA if both sides find targets. | O(n) | O(h) |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS by queue level sizes. | O(n) | O(w) |
| [Path Sum III](https://leetcode.com/problems/path-sum-iii/) | Medium | Prefix sum count map during DFS. | O(n) | O(h) |
| [Construct Binary Tree from Preorder and Inorder](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder/) | Medium | Use preorder root and inorder index map. | O(n) | O(n) |
| [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Preorder or BFS with null markers. | O(n) | O(n) |
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Return downward gain; update through-node path. | O(n) | O(h) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
