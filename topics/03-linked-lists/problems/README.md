# Linked Lists — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

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

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
