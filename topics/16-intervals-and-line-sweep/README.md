# Intervals and Line Sweep

**Level:** Core to Advanced

Handle ranges, overlaps, scheduling, and event-based counting.

---

## What you must learn

- Interval representation
- Sorting by start/end
- Merging intervals
- Insertion
- Sweep-line events
- Difference arrays
- Heap of active intervals

---

## Core patterns and approaches

- Sort by start for merging
- Sort by end for greedy non-overlap
- Sweep events by coordinate to count active intervals
- Use heap of end times for meeting rooms
- Use difference arrays for many range increments on discrete indices

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Sort by start and merge overlaps. | O(n log n) | O(n) |
| [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Add all before, merge overlapping, then add after. | O(n) | O(n) |
| [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) | Medium | Sort starts and use min-heap of end times. | O(n log n) | O(n) |
| [My Calendar I](https://leetcode.com/problems/my-calendar-i/) | Medium | Check if new interval overlaps existing intervals. | O(n) | O(n) |
| [Employee Free Time](https://leetcode.com/problems/employee-free-time/) | Hard | Merge all busy intervals, gaps are free time. | O(n log n) | O(n) |
| [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | Difference array or sorted pickup/drop events. | O(n log n) or O(U) | O(n or U) |
| [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | Sweep events with max-heap and lazy deletion. | O(n log n) | O(n) |
| [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end and greedily shoot arrows. | O(n log n) | O(1) |

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
