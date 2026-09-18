# Heaps and Priority Queues

**Level:** Core to Advanced

Use priority queues for top-k, streaming medians, scheduling, merging, and shortest path algorithms.

---

## What you must learn

- Min-heap property
- Push/pop complexity
- Heapify
- Top-k selection
- Two heaps
- Lazy deletion
- Priority queues in graph algorithms

---

## Core patterns and approaches

- Keep a min-heap of size k for kth largest/top k
- Use two heaps to maintain lower and upper halves for median
- Use heap of current heads to merge k sorted lists
- Use heap for earliest ending meeting/task
- Use lazy deletion when arbitrary removal is needed

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
import heapq

def top_k_largest(nums, k):
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Kth Largest Element in a Stream | Easy | Maintain min-heap of size k. | O(log k) per add | O(k) |
| Kth Largest Element in an Array | Medium | Min-heap size k or quickselect. | O(n log k) | O(k) |
| Top K Frequent Elements | Medium | Count then heap by frequency or bucket sort. | O(n log k) | O(n) |
| Merge k Sorted Lists | Hard | Heap stores current node from each list. | O(N log k) | O(k) |
| Find Median from Data Stream | Hard | Two heaps: max lower half, min upper half. | O(log n) add | O(n) |
| Meeting Rooms II | Medium | Sort starts; min-heap of active meeting ends. | O(n log n) | O(n) |
| Task Scheduler | Medium | Greedy formula or max-heap simulation with cooldown. | O(n) | O(1) |
| Reorganize String | Medium | Always place most frequent non-conflicting char. | O(n log k) | O(k) |

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
