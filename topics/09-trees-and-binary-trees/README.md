# Trees and Binary Trees

**Level:** Core to Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Solve hierarchical problems using DFS, BFS, recursion returns, path reasoning, and serialization.

---

## What you must learn

- Tree terminology
- Preorder, inorder, postorder
- Recursive and iterative DFS
- Level-order BFS
- Height/depth
- Path sums
- Lowest common ancestor
- Serialization

---

## Core patterns and approaches

- DFS returns a summary to parent: height, sum, validity, or gain
- Use nonlocal result when answer differs from returned value
- BFS level order uses queue length to separate levels
- LCA in binary tree combines left/right search results
- Serialization needs null markers to preserve shape

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def max_depth(root):
    if not root: return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

def level_order(root):
    from collections import deque
    if not root: return []
    ans, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft(); level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(level)
    return ans
```

---

## Top interview questions and approaches

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
