# Searching and Sorting

**Level:** Core

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

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

- `bisect_left` / `bisect_right` are the two primitives behind boundaries, counts and insertion points.
- `heapq.nlargest(k, ...)` is O(n log k) — cheaper than a full sort when k is small.
- Naive quicksort is O(n^2) on duplicates; three-way partitioning fixes that case.
- `sorted()` returns a new list; `list.sort()` mutates and returns `None`.

Runnable builds, step-by-step walkthroughs and solved examples live in **Python implementation (build it from scratch)** in the [complete study guide](study-guide.md).

---

## Canonical template

```python
import heapq

intervals = [[2, 3], [1, 4], [1, 2]]
records = [{'age': 30, 'score': 90, 'name': 'ada'},
           {'age': 30, 'score': 90, 'name': 'alan'},
           {'age': 25, 'score': 95, 'name': 'bob'}]

# Multi-key sorting: start ascending, then end ascending.
intervals.sort(key=lambda x: (x[0], x[1]))        # [[1, 2], [1, 4], [2, 3]]

# Mixed directions: age ascending, score descending, name ascending.
records.sort(key=lambda r: (r['age'], -r['score'], r['name']))

def kth_largest_heap(nums, k):
    """k-th largest without sorting everything: O(n log k)."""
    return heapq.nlargest(k, nums)[-1]
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Dutch national flag with low/mid/high pointers. | O(n) | O(1) |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start, merge overlapping intervals. | O(n log n) | O(n) |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Quickselect average O(n) or heap O(n log k). | O(n) avg | O(1) |
| [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Easy | Sort intervals by start and check overlaps. | O(n log n) | O(1) |
| [Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/) | Medium/Hard | Median partition; arrange larger/smaller alternately. | O(n) | O(n) or O(1) |
| [Count Inversions](https://www.geeksforgeeks.org/dsa/inversion-count-in-array-using-merge-sort/) | Hard | Merge sort while counting cross inversions. | O(n log n) | O(n) |
| [Largest Number](https://leetcode.com/problems/largest-number/) | Medium | Sort numbers by concatenation order. | O(n log n * k) | O(n) |

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
