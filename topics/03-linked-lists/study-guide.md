# Linked Lists: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Reason about links, not positions. Before changing a pointer, preserve every node that must remain reachable; dummy nodes remove head-specific branches.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Singly linked nodes support O(1) insertion after a known node. |
| 2 | Fast/slow pointers encode relative speed for cycles and midpoints. |
| 3 | In-place reversal maintains previous, current, and saved-next pointers. |
| 4 | A dummy head gives the first real node a predecessor. |
| 5 | Merging and partitioning are repeated tail-attachment operations. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Cycle or midpoint | Fast/slow pointers |
| Head may change | Dummy node |
| Process from the end | Gap pointers or reversal |
| Merge ordered chains | Dummy tail |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

```text
Before: prev <- current -> next
Save:   after = current.next
Flip:   current.next = prev
Move:   prev = current; current = after
```
The unprocessed suffix remains reachable through `after`, while `prev` is always the fully reversed prefix.

## Tricks and interview notes

- Draw arrows for a three-node example before coding.
- Use identity (`is`) when comparing nodes, not equality of values.
- For kth from end, keep two pointers exactly k nodes apart.
- When merging, attach the untouched remainder after one list ends.

## Common mistakes

- **Watch for:** Losing the suffix by reversing before saving `next`.
- **Watch for:** Dereferencing `fast.next` without checking `fast`.
- **Watch for:** Creating accidental cycles during reorder operations.
- **Watch for:** Forgetting that recursive reversal uses O(n) stack space.

## Implementation drills

1. Reverse iteratively and recursively.
2. Find and split at the midpoint.
3. Merge two sorted chains with a dummy node.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. The node and a full `LinkedList` class

A linked list is a chain of nodes. Each node owns a value and one link forward,
so insertion and deletion are O(1) **once you already hold the node**, but
reaching the k-th node always costs O(k).

```python
class Node:
    """One element of a singly linked list."""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """Singly linked list with the operations interviews expect."""

    def __init__(self, values=()):
        self.head = None
        self.tail = None
        self.size = 0
        for v in values:
            self.append(v)

    # -- dunder niceties -------------------------------------------------
    def __iter__(self):
        cur = self.head
        while cur:                       # stop at None, never at a value
            yield cur.val
            cur = cur.next

    def __len__(self):
        return self.size

    def __repr__(self):
        return " -> ".join(map(str, self)) + " -> None"

    # -- mutations -------------------------------------------------------
    def append(self, val):
        """Add at the tail: O(1) because we maintain a tail pointer."""
        node = Node(val)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return node

    def prepend(self, val):
        """Add at the head: O(1)."""
        self.head = Node(val, self.head)
        if self.tail is None:
            self.tail = self.head
        self.size += 1
        return self.head

    def insert_after(self, node, val):
        """Insert right after a node you already have: O(1)."""
        new = Node(val, node.next)
        node.next = new
        if node is self.tail:
            self.tail = new
        self.size += 1
        return new

    def delete(self, val):
        """Delete the first node holding val: O(n) — you must find its predecessor."""
        dummy = Node(0, self.head)       # dummy gives the real head a predecessor
        prev, cur = dummy, self.head
        while cur and cur.val != val:
            prev, cur = cur, cur.next
        if cur is None:
            return False
        prev.next = cur.next
        if cur is self.tail:
            self.tail = None if prev is dummy else prev
        self.head = dummy.next
        self.size -= 1
        return True

    def reverse(self):
        """Reverse in place: O(n) time, O(1) space."""
        prev, cur = None, self.head
        self.tail = self.head
        while cur:
            nxt = cur.next               # 1. save the suffix
            cur.next = prev              # 2. flip the arrow
            prev, cur = cur, nxt         # 3. advance both
        self.head = prev


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3])
    print("start:", ll, "| length:", len(ll))

    ll.prepend(0)
    ll.append(4)
    print("prepend(0), append(4):", ll)

    node_two = ll.head.next.next         # the node holding 2
    ll.insert_after(node_two, 99)
    print("insert 99 after 2:", ll)

    print("delete(99):", ll.delete(99), "->", ll)
    print("delete(42) (absent):", ll.delete(42))

    ll.reverse()
    print("reversed:", ll, "| head:", ll.head.val, "| tail:", ll.tail.val)
```

Output:

```text
start: 1 -> 2 -> 3 -> None | length: 3
prepend(0), append(4): 0 -> 1 -> 2 -> 3 -> 4 -> None
insert 99 after 2: 0 -> 1 -> 2 -> 99 -> 3 -> 4 -> None
delete(99): True -> 0 -> 1 -> 2 -> 3 -> 4 -> None
delete(42) (absent): False
reversed: 4 -> 3 -> 2 -> 1 -> 0 -> None | head: 4 | tail: 0
```

**How it works**

1. `Node` holds `val` plus a single `next` pointer; the end of the list is `None`.
2. `__iter__` walks with `while cur:` — the standard pointer-walking loop. Because it yields values, `__repr__`, `len`, and `for` loops all work for free.
3. `append` is O(1) only because the class maintains `tail`; without it every append would rescan the list (O(n)).
4. `insert_after` is the operation that makes linked lists attractive: O(1) once you hold the node. The equivalent array insert is O(n) because elements shift.
5. `delete` needs the predecessor, so we keep `prev` one step behind and use a **dummy node** so deleting the real head is not a special case.
6. `reverse` is the core pointer dance: save `next`, flip `cur.next` to `prev`, then advance. `prev` ends up as the new head, and the old head becomes the new tail (which is why `self.tail` is reassigned before the loop mangles the links).

### 2. The operations interview problems are built from

Most linked-list questions are combinations of these six helpers. They work on
bare heads (LeetCode style), so they also work on the class above via `ll.head`.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    """Build a list from an iterable and return its head."""
    dummy = cur = Node()
    for v in values:
        cur.next = Node(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    """Collect values back into a Python list (for printing and testing)."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def has_cycle(head):
    """Floyd's tortoise and hare: O(n) time, O(1) space."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:                 # compare identity, not value
            return True
    return False


def middle_node(head):
    """Second middle for even lengths (the one 'reverse second half' needs)."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def remove_nth_from_end(head, n):
    """One pass: keep the pointers n+1 apart so slow lands on the predecessor."""
    dummy = Node(0, head)
    fast = slow = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


def merge_two_sorted(a, b):
    """Dummy tail repeatedly attaches the smaller current node."""
    dummy = tail = Node()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b                   # attach the untouched remainder
    return dummy.next


def add_two_numbers(a, b):
    """Digits stored least-significant first; simulate addition with carry."""
    dummy = tail = Node()
    carry = 0
    while a or b or carry:
        carry, digit = divmod(carry + (a.val if a else 0) + (b.val if b else 0), 10)
        tail.next = Node(digit)
        tail = tail.next
        a = a.next if a else None
        b = b.next if b else None
    return dummy.next


if __name__ == "__main__":
    head = from_list([1, 2, 3, 4, 5])
    print("middle of 1..5:", middle_node(head).val)
    print("remove 2nd from end:", to_list(remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2)))
    print("merge sorted:", to_list(merge_two_sorted(from_list([1, 3, 5]), from_list([2, 4, 6]))))
    print("342 + 465 =", to_list(add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))))

    a, b, c = Node(1), Node(2), Node(3)
    a.next, b.next, c.next = b, c, b     # 1 -> 2 -> 3 -> back to 2
    print("cycle?", has_cycle(a), "| acyclic?", has_cycle(from_list([1, 2, 3])))
```

Output:

```text
middle of 1..5: 3
remove 2nd from end: [1, 2, 3, 5]
merge sorted: [1, 2, 3, 4, 5, 6]
342 + 465 = [7, 0, 8]
cycle? True | acyclic? False
```

**How it works**

- `from_list` / `to_list` are the bridge between Python lists and heads; use them in every test you write.
- `has_cycle` moves `fast` two steps and `slow` one. If there is a cycle they must meet inside it; if there is none, `fast` reaches `None`.
- `middle_node` uses the same two speeds: when `fast` falls off the end, `slow` is at the middle.
- `remove_nth_from_end` moves `fast` `n + 1` steps ahead first, so when `fast` hits `None`, `slow` sits exactly on the node *before* the one to delete.
- `merge_two_sorted` never creates new nodes (except the dummy): it rewires, so it is O(1) extra space. `tail.next = a or b` attaches the leftovers in one step.
- `add_two_numbers` loops while `a or b or carry` — that last `carry` is what produces the final digit (e.g. 5 + 5 = 10 → `0 -> 1`).

## Solved examples

### Example 1 — Reverse a linked list (Easy)

**Problem.** Given the head of a singly linked list, reverse the list and return the new head.

**Approach.** Keep three pointers. `prev` is the already-reversed prefix, `cur` is the node being flipped, and `nxt` preserves the unprocessed suffix. Invariant: after each step, the prefix ending at `prev` is reversed and `cur` still reaches every remaining node. Starting `prev = None` makes empty and single-node lists fall out for free.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def from_list(values):
    dummy = cur = Node()
    for v in values:
        cur.next = Node(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_iterative(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


def reverse_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head      # make the successor point back
    head.next = None           # break the original link to avoid a cycle
    return new_head


if __name__ == "__main__":
    for values in ([1, 2, 3, 4, 5], [], [7]):
        print(values, "->", to_list(reverse_iterative(from_list(values))))

    head = from_list([1, 2, 3])
    print("recursive:", to_list(reverse_recursive(head)))
    print("empty stays empty:", reverse_iterative(None) is None)
```

Output:

```text
[1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
[] -> []
[7] -> [7]
recursive: [3, 2, 1]
empty stays empty: True
```

**Complexity.** Both versions are O(n) time. The iterative one is O(1) extra space; the recursive one uses O(n) call-stack space and hits Python's recursion limit at roughly 1000 nodes — prefer the loop.

### Example 2 — Where does the cycle begin? (Medium)

**Problem.** Given a linked list, return the node where a cycle begins, or `None` if there is none.

**Approach.** Floyd's algorithm in two phases. Phase 1: `slow` (1 step) and `fast` (2 steps) meet somewhere inside the cycle. Phase 2: put one pointer back at the head and advance both one step at a time; they meet exactly at the cycle entry. Why: if the distance from head to entry is `d` and the meeting point is `k` steps past the entry, then `2(d + k) = d + k + m·C` (C = cycle length), so `d + k = m·C`, meaning `d ≡ C − k (mod C)` — walking `d` steps from the meeting point, or from the head, lands on the entry.

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle_entry(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:                       # phase 1: met inside the cycle
            ptr = head                         # phase 2: find the entry
            while ptr is not slow:
                ptr = ptr.next
                slow = slow.next
            return ptr
    return None


if __name__ == "__main__":
    a, b, c, d = Node(3), Node(2), Node(0), Node(-4)
    a.next, b.next, c.next, d.next = b, c, d, b     # cycle starts at node 2
    entry = detect_cycle_entry(a)
    print("cycle starts at:", entry.val)

    linear = Node(1, Node(2, Node(3)))
    print("no cycle:", detect_cycle_entry(linear))

    self_loop = Node(1)
    self_loop.next = self_loop
    print("self loop starts at:", detect_cycle_entry(self_loop).val)
```

Output:

```text
cycle starts at: 2
no cycle: None
self loop starts at: 1
```

**Complexity.** O(n) time, O(1) extra space — no hash set needed.

### Example 3 — Copy a list with a random pointer (Medium)

**Problem.** Each node has `next` and `random` (pointing to any node or `None`). Return a deep copy: no node from the original may appear in the copy.

**Approach.** Two passes with a hash map from original node → clone. Pass 1 clones every node (values only). Pass 2 wires `next` and `random` through the map. The alternative *interweaving* trick (clone each node into `original.next`, wire, then split) is O(1) extra space but mutates the input — say so out loud in an interview and ask whether that is acceptable.

```python
class RandomNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if head is None:
        return None
    clones = {}                                  # original node -> clone
    cur = head
    while cur:
        clones[cur] = RandomNode(cur.val)        # pass 1: values only
        cur = cur.next
    cur = head
    while cur:
        clone = clones[cur]
        clone.next = clones.get(cur.next)        # None maps to None
        clone.random = clones.get(cur.random)
        cur = cur.next
    return clones[head]


def to_lists(head):
    """Return (values, [index of each node's random target or -1])."""
    nodes, order = [], {}
    cur = head
    while cur:
        order[id(cur)] = len(nodes)
        nodes.append(cur)
        cur = cur.next
    return [n.val for n in nodes], [order.get(id(n.random), -1) for n in nodes]


if __name__ == "__main__":
    n1, n2, n3 = RandomNode(1), RandomNode(2), RandomNode(3)
    n1.next, n2.next = n2, n3
    n1.random, n2.random, n3.random = n3, n1, n2

    copy = copy_random_list(n1)
    print("original:", to_lists(n1))
    print("copy    :", to_lists(copy))
    print("deep copy (no shared nodes):", copy is not n1 and copy.next is not n2)
    print("empty input:", copy_random_list(None))
```

Output:

```text
original: ([1, 2, 3], [2, 0, 1])
copy    : ([1, 2, 3], [2, 0, 1])
deep copy (no shared nodes): True
empty input: None
```

**Complexity.** O(n) time and O(n) space for the map. Keying the dict by the node object works because Python objects are hashable by identity by default.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) | LeetCode | Easy |
| [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/) | LeetCode | Easy |
| [Partition List](https://leetcode.com/problems/partition-list/) | LeetCode | Medium |
| [Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain singly linked nodes support o(1) insertion after a known node without notes.
- [ ] Explain fast/slow pointers encode relative speed for cycles and midpoints without notes.
- [ ] Explain in-place reversal maintains previous, current, and saved-next pointers without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
