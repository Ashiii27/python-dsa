# Binary Search Trees: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Every node partitions keys into strict ordered ranges. Carry ancestor bounds or exploit inorder order; balanced height gives logarithmic operations, but ordinary BSTs can become linear chains.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Valid BST nodes satisfy all ancestor bounds, not only parent comparisons. |
| 2 | Inorder traversal yields sorted keys. |
| 3 | Search/insert/delete follow one root-to-leaf path. |
| 4 | Deleting two-child nodes uses inorder successor or predecessor replacement. |
| 5 | Balanced construction chooses median roots. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need sorted rank | Inorder traversal |
| Validate ordering | Low/high bounds |
| Search by key | Iterative branch descent |
| Delete two-child node | Replace with successor |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

To validate `5 / left=1 / right=7 with left child 4`, parent-only checks pass at node 4 because `4 < 7`, but it violates root 5. Bounds catch it: node 4 inherits `(5, 7)` and fails.

## Tricks and interview notes

- Use strict inequalities unless duplicates have a defined placement rule.
- Iterative search uses O(1) auxiliary space.
- Stop inorder after the kth visit rather than traversing everything.
- A sorted array can build a height-balanced BST in O(n).

## Common mistakes

- **Watch for:** Checking only immediate children.
- **Watch for:** Assuming O(log n) without a balancing guarantee.
- **Watch for:** Losing a subtree during deletion.
- **Watch for:** Using global previous state across repeated validation calls.

## Implementation drills

1. Validate with bounds and inorder methods.
2. Implement all three deletion cases.
3. Build a balanced BST from sorted values.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. A complete BST class

The BST invariant: for every node, everything in its left subtree is smaller and
everything in its right subtree is larger. That single rule turns search into a
binary decision at each level — O(h) for insert, search, and delete, where h is
the height. A balanced tree keeps h = O(log n); inserting sorted data degenerates
it to h = n.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class BST:
    """Binary search tree with insert, search, delete and the usual queries."""

    def __init__(self, values=()):
        self.root = None
        self.size = 0
        for value in values:
            self.insert(value)

    # -- core operations -------------------------------------------------
    def insert(self, val):
        """O(h). Duplicates go to the right (pick one side and stay consistent)."""
        if self.root is None:
            self.root = TreeNode(val)
            self.size += 1
            return True
        node = self.root
        while node:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    self.size += 1
                    return True
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    self.size += 1
                    return True
                node = node.right

    def search(self, val):
        """Return the node holding val, or None. O(h)."""
        node = self.root
        while node:
            if val == node.val:
                return node
            node = node.left if val < node.val else node.right
        return None

    def __contains__(self, val):
        return self.search(val) is not None

    def delete(self, val):
        """O(h). Three cases: leaf, one child, two children. Returns True if removed."""
        removed = [False]                 # flag shared with the nested function

        def remove(node, target):
            if node is None:
                return None
            if target < node.val:
                node.left = remove(node.left, target)
            elif target > node.val:
                node.right = remove(node.right, target)
            else:
                removed[0] = True         # found it
                if node.left is None:
                    return node.right                 # 0 or 1 child
                if node.right is None:
                    return node.left
                successor = node.right                # 2 children: in-order successor
                while successor.left:
                    successor = successor.left
                node.val = successor.val              # copy, then delete the copy
                node.right = remove(node.right, successor.val)
            return node

        self.root = remove(self.root, val)
        if removed[0]:
            self.size -= 1
        return removed[0]

    # -- queries ---------------------------------------------------------
    def inorder(self):
        """Sorted values: this is the point of a BST."""
        out, stack, cur = [], [], self.root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            out.append(cur.val)
            cur = cur.right
        return out

    def height(self):
        def depth(node):
            return 0 if node is None else 1 + max(depth(node.left), depth(node.right))
        return depth(self.root)

    def min_value(self):
        node = self.root
        while node and node.left:
            node = node.left
        return node.val if node else None

    def max_value(self):
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else None

    def kth_smallest(self, k):
        """1-indexed k-th smallest: stop the in-order walk after k pops."""
        stack, cur, seen = [], self.root, 0
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            seen += 1
            if seen == k:
                return cur.val
            cur = cur.right
        return None

    def is_valid(self, low=float("-inf"), high=float("inf")):
        """Every value must stay inside the bounds its ancestors impose."""
        def check(node, low, high):
            if node is None:
                return True
            if not low < node.val < high:
                return False
            return check(node.left, low, node.val) and check(node.right, node.val, high)
        return check(self.root, low, high)

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"BST(size={self.size}, height={self.height()}, sorted={self.inorder()})"


if __name__ == "__main__":
    tree = BST([5, 3, 7, 2, 4, 6, 8])
    print(tree)
    print("search(4):", tree.search(4), "| search(99):", tree.search(99), "| 7 in tree:", 7 in tree)
    print("min:", tree.min_value(), "| max:", tree.max_value(), "| kth(3):", tree.kth_smallest(3))
    print("valid BST:", tree.is_valid(), "| height:", tree.height())

    print("delete leaf 2:", tree.delete(2), "->", tree.inorder())
    print("delete 7 (two children):", tree.delete(7), "->", tree.inorder())
    print("delete root 5:", tree.delete(5), "->", tree.inorder(), "| still valid:", tree.is_valid())
    print("delete missing 42:", tree.delete(42))
    print("empty checks:", BST().inorder(), BST().min_value(), BST().height())
```

Output:

```text
BST(size=7, height=3, sorted=[2, 3, 4, 5, 6, 7, 8])
search(4): TreeNode(4) | search(99): None | 7 in tree: True
min: 2 | max: 8 | kth(3): 4
valid BST: True | height: 3
delete leaf 2: True -> [3, 4, 5, 6, 7, 8]
delete 7 (two children): True -> [3, 4, 5, 6, 8]
delete root 5: True -> [3, 4, 6, 8] | still valid: True
delete missing 42: False
empty checks: [] None 0
```

**How it works**

- `insert` walks down, comparing at each node, and attaches the new node where the walk falls off the tree. Iterative (no recursion) means no stack-depth worries.
- `delete` is the only tricky operation. Leaf → return `None`. One child → return that child (the parent rewires itself to it). Two children → replace the value with its **in-order successor** (the smallest value in the right subtree, found by going right once then left forever), then delete that successor, which has at most one child.
- `inorder` produces values in sorted order — that is the BST property made visible, and it is also how you validate or flatten a BST.
- `is_valid` threads narrowing bounds down the recursion. Comparing only with the immediate parent is a classic bug: `TreeNode(5, TreeNode(1), TreeNode(7))` under `TreeNode(3)` passes a parent-only check but violates the BST property.

### 2. BST-specific patterns in Python

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_recursive(root, val):
    """Textbook recursive insert: returns the (possibly new) subtree root."""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_recursive(root.left, val)
    else:
        root.right = insert_recursive(root.right, val)
    return root


def build_bst(values):
    root = None
    for value in values:
        root = insert_recursive(root, value)
    return root


def range_sum(root, low, high):
    """Sum of values in [low, high]; prune the subtrees outside the range."""
    if root is None:
        return 0
    if root.val < low:
        return range_sum(root.right, low, high)     # left subtree is all smaller
    if root.val > high:
        return range_sum(root.left, low, high)      # right subtree is all larger
    return root.val + range_sum(root.left, low, high) + range_sum(root.right, low, high)


def lca_bst(root, p, q):
    """For a BST the split point is found by comparing values, no searching."""
    low, high = min(p, q), max(p, q)
    node = root
    while node:
        if node.val > high:
            node = node.left
        elif node.val < low:
            node = node.right
        else:
            return node.val                          # values straddle this node
    return None


def successor(root, val):
    """Smallest value greater than val, or None."""
    best = None
    node = root
    while node:
        if node.val > val:
            best = node.val                          # a candidate
            node = node.left                         # try to do better
        else:
            node = node.right
    return best


def is_balanced_bst(root):
    """Balanced check: return the height, or -1 as an 'unbalanced' sentinel."""
    def check(node):
        if node is None:
            return 0
        left, right = check(node.left), check(node.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check(root) != -1


def inorder_morris_free(root):
    """Recursive in-order (simple version) — used to compare orderings below."""
    return [] if root is None else inorder_morris_free(root.left) + [root.val] + inorder_morris_free(root.right)


if __name__ == "__main__":
    values = [5, 3, 7, 2, 4, 6, 8]
    root = build_bst(values)
    print("inorder:", inorder_morris_free(root), "| sorted input check:", inorder_morris_free(root) == sorted(values))
    print("range_sum(3, 7):", range_sum(root, 3, 7))
    print("LCA of 2 and 8:", lca_bst(root, 2, 8), "| LCA of 4 and 6:", lca_bst(root, 4, 6))
    print("successor of 5:", successor(root, 5), "| successor of 8:", successor(root, 8))
    print("balanced:", is_balanced_bst(root))

    skewed = build_bst([1, 2, 3, 4, 5])             # sorted input -> a linked list
    print("skewed tree balanced:", is_balanced_bst(skewed), "| height behaves like O(n)")
```

Output:

```text
inorder: [2, 3, 4, 5, 6, 7, 8] | sorted input check: True
range_sum(3, 7): 25
LCA of 2 and 8: 5 | LCA of 4 and 6: 5
successor of 5: 6 | successor of 8: None
balanced: True
skewed tree balanced: False | height behaves like O(n)
```

**How it works**

- `range_sum` prunes whole subtrees: if the node's value is below `low`, everything in its left subtree is too. That pruning is the reason BSTs beat a sorted array for range queries with updates.
- `lca_bst` needs no recursion: the answer is the first node whose value lies between the two targets (inclusive).
- `successor` keeps the best candidate seen so far while walking down — one pass, O(h), no parent pointers.
- Inserting sorted data produces a degenerate O(n)-height tree. That is exactly why production maps use self-balancing trees (AVL, red-black) or skip lists.

## Solved examples

### Example 1 — Validate a binary search tree (Medium)

**Problem.** Decide whether a binary tree satisfies the BST invariant.

**Approach.** Carry the allowable interval down the tree. The root may hold anything in `(−∞, +∞)`; going left tightens the upper bound to the parent's value, going right tightens the lower bound. A parent-only comparison is not enough — you must check against every ancestor, which is what the interval does.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root):
    def check(node, low, high):
        if node is None:
            return True
        if not low < node.val < high:          # strict: no duplicates allowed
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)
    return check(root, float("-inf"), float("inf"))


def is_valid_bst_inorder(root):
    """Equivalent check: an in-order walk of a BST must be strictly increasing."""
    previous = None
    stack, cur = [], root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        if previous is not None and cur.val <= previous:
            return False
        previous = cur.val
        cur = cur.right
    return True


if __name__ == "__main__":
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    print("valid:", is_valid_bst(valid), is_valid_bst_inorder(valid))

    # 5 is in the left subtree of 3, but is greater than 3 -> invalid
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print("invalid (nested violation):", is_valid_bst(invalid), is_valid_bst_inorder(invalid))

    duplicates = TreeNode(2, TreeNode(2), TreeNode(3))
    print("duplicates rejected:", is_valid_bst(duplicates))
    print("empty tree is valid:", is_valid_bst(None))
```

Output:

```text
valid: True True
invalid (nested violation): False False
duplicates rejected: False
empty tree is valid: True
```

**Complexity.** O(n) time, O(h) space. Use `<=` / `>=` instead of `<` / `>` if the tree permits duplicates on one side; `float("inf")` bounds work for any numeric type, and `None` bounds are safer for non-numeric keys.

### Example 2 — Delete a node from a BST (Medium)

**Problem.** Delete the node with value `key` and return the (possibly new) root.

**Approach.** Search for the key by comparison. When found, handle three cases: no children (drop it), one child (return that child so the parent re-links), two children (replace the value with the in-order successor, then delete that successor recursively). Returning the subtree root at every step is what makes the parent rewire without extra bookkeeping.

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root, key):
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right                       # case 1 & 2a
        if root.right is None:
            return root.left                        # case 2b
        successor = root.right                      # case 3: two children
        while successor.left:
            successor = successor.left
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)
    return root


def inorder(root):
    return [] if root is None else inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    tree = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
    print("original:", inorder(tree))

    tree = delete_node(tree, 3)                     # two children
    print("delete 3:", inorder(tree))
    tree = delete_node(tree, 5)                     # root
    print("delete root 5:", inorder(tree))
    tree = delete_node(tree, 2)                     # leaf
    print("delete leaf 2:", inorder(tree))
    tree = delete_node(tree, 99)                    # absent
    print("delete missing:", inorder(tree))
```

Output:

```text
original: [2, 3, 4, 5, 6, 7]
delete 3: [2, 4, 5, 6, 7]
delete root 5: [2, 4, 6, 7]
delete leaf 2: [4, 6, 7]
delete missing: [4, 6, 7]
```

**Complexity.** O(h) time and O(h) recursion space. Using the in-order **predecessor** (largest in the left subtree) works equally well; mixing both consistently is a common interview discussion point.

### Example 3 — Kth smallest element in a BST (Medium)

**Problem.** Return the k-th smallest value (1-indexed) in a BST.

**Approach.** In-order traversal visits values in ascending order, so count pops and stop at the k-th. The iterative version can return early, which the recursive "collect everything" version cannot — important when the tree is large and k is small. If the tree is used for many such queries, store the subtree size at each node and descend in O(h).

```python
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root, k):
    """Iterative in-order with an early exit. O(h + k) time, O(h) space."""
    stack, cur, seen = [], root, 0
    while stack or cur:
        while cur:                       # descend to the leftmost node
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        seen += 1
        if seen == k:
            return cur.val
        cur = cur.right                  # then the node's right subtree
    return None


if __name__ == "__main__":
    tree = TreeNode(5,
                    TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                    TreeNode(6))
    print("sorted values: [1, 2, 3, 4, 5, 6]")
    for k in (1, 3, 6):
        print(f"  k={k} ->", kth_smallest(tree, k))
    print("k out of range:", kth_smallest(tree, 7))
    print("empty tree:", kth_smallest(None, 1))
```

Output:

```text
sorted values: [1, 2, 3, 4, 5, 6]
  k=1 -> 1
  k=3 -> 3
  k=6 -> 6
k out of range: None
empty tree: None
```

**Complexity.** O(h + k) time (h to reach the leftmost node, then k steps) and O(h) space for the stack. The augmented-tree variant (subtree sizes) answers in O(h) per query, which is the "follow-up" interviewers ask about.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Trim a Binary Search Tree](https://leetcode.com/problems/trim-a-binary-search-tree/) | LeetCode | Medium |
| [BST Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) | LeetCode | Medium |
| [Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/) | LeetCode | Medium |
| [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain valid bst nodes satisfy all ancestor bounds, not only parent comparisons without notes.
- [ ] Explain inorder traversal yields sorted keys without notes.
- [ ] Explain search/insert/delete follow one root-to-leaf path without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
