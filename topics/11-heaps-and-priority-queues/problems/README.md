# Heaps And Priority Queues — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | Maintain min-heap of size k. | O(log k) per add | O(k) |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Min-heap size k or quickselect. | O(n log k) | O(k) |
| [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Count then heap by frequency or bucket sort. | O(n log k) | O(n) |
| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Heap stores current node from each list. | O(N log k) | O(k) |
| [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Two heaps: max lower half, min upper half. | O(log n) add | O(n) |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Sort starts; min-heap of active meeting ends. | O(n log n) | O(n) |
| [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Greedy formula or max-heap simulation with cooldown. | O(n) | O(1) |
| [Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | Always place most frequent non-conflicting char. | O(n log k) | O(k) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
