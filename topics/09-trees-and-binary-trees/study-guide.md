# Trees and Binary Trees: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Recursive structure suggests recursive contracts: decide what one subtree returns and how a node combines child results. Iterative traversals make the same pending work explicit in a stack or queue.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Preorder processes node before children; inorder between; postorder after. |
| 2 | BFS processes levels and exposes shortest edge distance from the root. |
| 3 | Height, balance, and diameter are postorder combinations. |
| 4 | Path problems distinguish downward return values from complete global candidates. |
| 5 | Serialization must preserve null structure, not only values. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Combine child facts | Postorder DFS |
| Level-by-level output | BFS |
| Root-to-leaf state | Preorder DFS |
| Ancestor/path query | Recursive return contract |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For diameter, each node receives left and right heights. `left + right` is the best path passing through that node; return `1 + max(left, right)` because a parent can extend only one branch.

## Tricks and interview notes

- State whether height counts nodes or edges.
- Use a deque for level-order traversal.
- Pass prefix state down; undo map counts when returning from DFS.
- Iterative postorder can use `(node, visited)` pairs.

## Common mistakes

- **Watch for:** Returning the global path candidate to a parent instead of a one-branch value.
- **Watch for:** Ignoring recursion depth on a skewed tree.
- **Watch for:** Reconstructing from traversals when values are not unique.
- **Watch for:** Serializing without null markers.

## Implementation drills

1. Implement all three DFS orders recursively and iteratively.
2. Compute height and diameter in one traversal.
3. Serialize and deserialize a sparse tree.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. The node, a builder, and every traversal

Almost every tree problem is a traversal with something computed on the way.
Learn the four orders cold: pre-order (node first), in-order (node in the
middle), post-order (children first), and level-order (breadth first).

```python
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values):
    """Build from a level-order list where None marks a missing child."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:      # left child
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:      # right child
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# -- recursive: three lines each, the order is just where you visit --------
def preorder(root):
    return [] if not root else [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root):
    return [] if not root else inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root):
    return [] if not root else postorder(root.left) + postorder(root.right) + [root.val]


# -- iterative: same results with an explicit stack ------------------------
def preorder_iterative(root):
    if not root:
        return []
    stack, out = [root], []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)       # right pushed first -> left popped first
        if node.left:
            stack.append(node.left)
    return out


def inorder_iterative(root):
    """Go as far left as possible, then pop and step right."""
    stack, out, cur = [], [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def level_order(root):
    """BFS level by level; the inner loop fixes the level size first."""
    if not root:
        return []
    out, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):        # snapshot: only this level
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(level)
    return out


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("tree (level order):", level_order(root))
    print("preorder  :", preorder(root), "| iterative:", preorder_iterative(root))
    print("inorder   :", inorder(root), "| iterative:", inorder_iterative(root))
    print("postorder :", postorder(root))
    print("empty tree:", level_order(None), preorder(None))
```

Output:

```text
tree (level order): [[1], [2, 3], [4, 5, 6, 7]]
preorder  : [1, 2, 4, 5, 3, 6, 7] | iterative: [1, 2, 4, 5, 3, 6, 7]
inorder   : [4, 2, 5, 1, 6, 3, 7] | iterative: [4, 2, 5, 1, 6, 3, 7]
postorder : [4, 5, 2, 6, 7, 3, 1]
empty tree: [] []
```

**How it works**

- `build_tree` uses a queue of "parents waiting for children" and reads the level-order list left to right. This is the same representation LeetCode uses, so you can paste test cases straight in.
- Recursive traversals differ only in where the node's own value is placed relative to the two recursive calls — one line moves, the algorithm changes.
- `preorder_iterative` pushes the **right** child first so the left child is popped first (stacks reverse order).
- `inorder_iterative` is the pattern behind BST iterators: descend left, pop, then move to the right subtree.
- `level_order` snapshots `len(queue)` before the inner loop; without that snapshot you cannot tell where a level ends.

### 2. Measuring trees: height, diameter, balance, LCA

Post-order is the workhorse: children are processed before the parent, so the
parent can combine their answers.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    from collections import deque
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def height(root):
    """Number of nodes on the longest root-to-leaf path (0 for an empty tree)."""
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    """Longest path between any two nodes, counted in EDGES."""
    best = 0

    def depth(node):
        nonlocal best
        if not node:
            return 0
        left, right = depth(node.left), depth(node.right)
        best = max(best, left + right)     # path through this node
        return 1 + max(left, right)        # what the parent needs
    depth(root)
    return best


def is_balanced(root):
    """Every node's subtrees differ in height by at most 1. Returns heights or -1."""
    def check(node):
        if not node:
            return 0
        left, right = check(node.left), check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1                      # propagate "unbalanced" upwards
        return 1 + max(left, right)
    return check(root) != -1


def lowest_common_ancestor(root, p, q):
    """First node with p and q in different subtrees (or equal to one of them)."""
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root                        # split: this node is the ancestor
    return left or right


def count_nodes_level_order(root):
    """Level-order without recursion: safe for very deep trees."""
    if not root:
        return 0
    from collections import deque
    queue, total = deque([root]), 0
    while queue:
        node = queue.popleft()
        total += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return total


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("height (nodes):", height(root), "| diameter (edges):", diameter(root))
    print("balanced:", is_balanced(root), "| node count:", count_nodes_level_order(root))

    node4, node5, node6 = root.left.left, root.left.right, root.right.left
    print("LCA of 4 and 5:", lowest_common_ancestor(root, node4, node5).val)
    print("LCA of 4 and 6:", lowest_common_ancestor(root, node4, node6).val)
    print("LCA with the node itself:", lowest_common_ancestor(root, node4, node4).val)

    chain = build_tree([1, 2, None, 3])
    print("left chain -> height:", height(chain), "| balanced:", is_balanced(chain))
    print("empty tree -> height:", height(None), "| diameter:", diameter(None))
```

Output:

```text
height (nodes): 3 | diameter (edges): 4
balanced: True | node count: 7
LCA of 4 and 5: 2
LCA of 4 and 6: 1
LCA with the node itself: 4
left chain -> height: 3 | balanced: False
empty tree -> height: 0 | diameter: 0
```

**How it works**

- `height` counts **nodes** (empty = 0). Always state which convention you use; mixing node-count and edge-count heights causes off-by-one answers in diameter and balance problems.
- `diameter` computes two different things in one traversal: the return value is the height the parent needs, while `best` tracks the longest path through the current node (`left + right`).
- `is_balanced` returns `-1` as a sentinel meaning "already unbalanced", so the tree is visited once instead of re-measuring heights at every node (which would be O(n²)).
- `lowest_common_ancestor` returns a non-`None` result from the left and right subtrees exactly when the two targets are split — that node is the answer. It handles the case where one target is an ancestor of the other via the `root is p` check.

## Solved examples

### Example 1 — Invert a binary tree (Easy)

**Problem.** Mirror the tree: every left child swaps with its right child.

**Approach.** Post-order in one line: invert both subtrees, then swap the node's own children. The recursion's base case is `None`. Iterative BFS works identically — swap children for every node you dequeue.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root):
    from collections import deque
    if not root:
        return []
    out, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        out.append(level)
    return out


if __name__ == "__main__":
    tree = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7, TreeNode(6), TreeNode(9)))
    print("before:", level_order(tree))
    print("after :", level_order(invert_tree(tree)))
    print("empty:", invert_tree(None))
```

Output:

```text
before: [[4], [2, 7], [1, 3, 6, 9]]
after : [[4], [7, 2], [9, 6, 3, 1]]
empty: None
```

**Complexity.** O(n) time (every node visited once) and O(h) stack space, where h is the height — O(n) for a skewed tree, O(log n) for a balanced one.

### Example 2 — Binary tree maximum path sum (Hard)

**Problem.** Find the maximum sum of any path in the tree. The path may start and
end at any nodes, but must go through parent-child edges.

**Approach.** Post-order again. For each node, the best path **that can be extended upward** uses at most one child (else the path would branch), and it is `node.val + max(0, best left gain, best right gain)`. The best path **anywhere** may pass through the node using both children, so track that separately in a global maximum. Negative contributions are clamped to zero: a subtree that only makes the sum worse is dropped.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    best = float("-inf")

    def gain(node):
        """Best sum of a path starting at `node` and going down one branch."""
        nonlocal best
        if not node:
            return 0
        left = max(0, gain(node.left))          # ignore negative branches
        right = max(0, gain(node.right))
        best = max(best, node.val + left + right)   # path through this node
        return node.val + max(left, right)          # extendable upward

    gain(root)
    return best


if __name__ == "__main__":
    tree = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print("max path sum:", max_path_sum(tree))          # 42 = 15 + 20 + 7

    single = TreeNode(5)
    print("single node:", max_path_sum(single))

    negatives = TreeNode(-3, TreeNode(-1), TreeNode(-2))
    print("all negative:", max_path_sum(negatives))     # -1
```

Output:

```text
max path sum: 42
single node: 5
all negative: -1
```

**Complexity.** O(n) time, O(h) space. The two-different-answers-in-one-traversal structure is the same as the diameter problem — recognise it and the hard problem becomes a template.

### Example 3 — Build a tree from preorder and inorder (Medium)

**Problem.** Reconstruct the binary tree from its pre-order and in-order traversals.

**Approach.** Pre-order's first element is always the root. Find that value in the in-order list: everything left of it is the left subtree, everything right is the right subtree, and the sizes tell you how to split the pre-order list. Recurse. Hashing the in-order indices turns the repeated `index()` scan (O(n²)) into O(n).

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    index_of = {value: i for i, value in enumerate(inorder)}

    def build(pre_lo, pre_hi, in_lo, in_hi):
        if pre_lo > pre_hi:
            return None
        root_value = preorder[pre_lo]
        root = TreeNode(root_value)
        split = index_of[root_value] - in_lo          # size of the left subtree
        root.left = build(pre_lo + 1, pre_lo + split, in_lo, in_lo + split - 1)
        root.right = build(pre_lo + split + 1, pre_hi, in_lo + split + 1, in_hi)
        return root

    return build(0, len(preorder) - 1, 0, len(inorder) - 1)


def inorder_traversal(root):
    return [] if not root else inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)


def preorder_traversal(root):
    return [] if not root else [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)


if __name__ == "__main__":
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    tree = build_tree(pre, ino)
    print("rebuilt inorder :", inorder_traversal(tree), "| matches input:", inorder_traversal(tree) == ino)
    print("rebuilt preorder:", preorder_traversal(tree), "| matches input:", preorder_traversal(tree) == pre)

    tree2 = build_tree([1, 2, 3], [2, 1, 3])      # root 1 with both children
    print("second tree preorder:", preorder_traversal(tree2))
    print("single node:", preorder_traversal(build_tree([1], [1])))
```

Output:

```text
rebuilt inorder : [9, 3, 15, 20, 7] | matches input: True
rebuilt preorder: [3, 9, 20, 15, 7] | matches input: True
second tree preorder: [1, 2, 3]
single node: [1]
```

**Complexity.** O(n) time and O(n) space with the index map. In-order + post-order works the same way (the root is the **last** post-order element); pre-order + post-order alone cannot uniquely determine a tree.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Tree Diameter](https://cses.fi/problemset/task/1131) | CSES | Medium |
| [Subordinates](https://cses.fi/problemset/task/1674) | CSES | Medium |
| [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) | LeetCode | Hard |
| [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain preorder processes node before children; inorder between; postorder after without notes.
- [ ] Explain bfs processes levels and exposes shortest edge distance from the root without notes.
- [ ] Explain height, balance, and diameter are postorder combinations without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
