# Linked Lists

**Level:** Core

Learn pointer manipulation, dummy nodes, fast/slow pointers, reversal, merging, and cycle handling.

---

## What you must learn

- Singly linked list node structure
- Pointer reassignment order
- Dummy/sentinel nodes
- Fast and slow pointers
- Cycle detection
- Reversal and segment reversal
- Merging and splitting lists

---

## Core patterns and approaches

- Use a dummy node when the head may change
- Use fast/slow pointers for middle or cycle detection
- Reverse with prev, cur, and saved nxt
- For nth-from-end, separate pointers by n nodes
- For random pointers, map original node to clone or interweave nodes

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Redirect pointers using prev/current/next. | O(n) | O(1) |
| [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Dummy tail attaches the smaller current node. | O(n+m) | O(1) |
| [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Floyd fast/slow pointers meet if a cycle exists. | O(n) | O(1) |
| [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | Fast moves two steps while slow moves one. | O(n) | O(1) |
| [Remove Nth Node From End](https://leetcode.com/problems/remove-nth-node-from-end/) | Medium | Dummy plus two pointers separated by n. | O(n) | O(1) |
| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Simulate digit addition with carry using dummy head. | O(max(n,m)) | O(1) extra |
| [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Find middle, reverse second half, merge alternating. | O(n) | O(1) |
| [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Map original nodes to cloned nodes, then wire pointers. | O(n) | O(n) |
| [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Check k nodes exist, reverse segment, reconnect. | O(n) | O(1) |

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
