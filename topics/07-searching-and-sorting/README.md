# Searching and Sorting

**Level:** Core

Understand comparison sorting, selection, ordering tricks, and when sorting unlocks simpler algorithms.

---

## What you must learn

- Linear search
- Comparison sorting
- Stable sorting
- Custom sort keys
- Merge sort and quicksort intuition
- Quickselect
- Counting/bucket sort when value range is small

---

## Core patterns and approaches

- Sort first to enable two pointers or greedy ordering
- Use custom keys for intervals and events
- Use quickselect/heap for kth element instead of full sort when needed
- Use stable sorting when previous order matters
- Use counting sort/buckets for small integer domains

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
intervals.sort(key=lambda x: (x[0], x[1]))
records.sort(key=lambda r: (r['age'], -r['score'], r['name']))

def kth_largest_heap(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Sort Colors | Medium | Dutch national flag with low/mid/high pointers. | O(n) | O(1) |
| Merge Intervals | Medium | Sort by start, merge overlapping intervals. | O(n log n) | O(n) |
| Kth Largest Element in an Array | Medium | Quickselect average O(n) or heap O(n log k). | O(n) avg | O(1) |
| Meeting Rooms | Easy | Sort intervals by start and check overlaps. | O(n log n) | O(1) |
| Wiggle Sort II | Medium/Hard | Median partition; arrange larger/smaller alternately. | O(n) | O(n) or O(1) |
| Count Inversions | Hard | Merge sort while counting cross inversions. | O(n log n) | O(n) |
| Largest Number | Medium | Sort numbers by concatenation order. | O(n log n * k) | O(n) |

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
