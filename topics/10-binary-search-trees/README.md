# Binary Search Trees

**Level:** Core

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Use ordering properties to validate, search, traverse, and modify binary search trees.

---

## What you must learn

- BST property
- Inorder sorted order
- Search/insert/delete
- Lower and upper bounds
- Kth smallest
- Successor/predecessor
- Balanced vs skewed BST

---

## Core patterns and approaches

- Validate using allowed low/high bounds
- Inorder traversal gives sorted values
- Kth smallest can stop after k inorder visits
- LCA in BST follows value ranges
- Delete by replacing with inorder successor or predecessor

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def is_valid_bst(root):
    def dfs(node, low, high):
        if not node: return True
        if not (low < node.val < high): return False
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float('-inf'), float('inf'))
```

---

## Top interview questions and approaches

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
