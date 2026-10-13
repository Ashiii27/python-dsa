# Intervals and Line Sweep: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Convert spans into ordered boundaries. Sorting by start supports merging; sorting by end supports selection; events turn active intervals into a running count or data structure.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Overlap rules depend on closed, open, or half-open endpoints. |
| 2 | Merge after sorting by start. |
| 3 | Earliest-end greedy maximizes non-overlapping selections. |
| 4 | Sweep events add at starts and subtract at ends. |
| 5 | A heap tracks active intervals by earliest ending time. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Combine overlaps | Sort by start + merge |
| Minimum removals/arrows | Sort by end |
| Maximum simultaneous activity | Events or end-time heap |
| Insert into sorted disjoint list | Three-phase scan |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For half-open meetings `[1,3)` and `[3,5)`, process an end event before a start event at the same time so they do not overlap. For closed intervals, tie handling may reverse. Endpoint semantics decide correctness.

## Tricks and interview notes

- Write interval semantics before choosing comparison operators.
- Represent half-open event deltas as `+1` at start and `-1` at end.
- Separate intervals before, overlapping, and after an inserted interval.
- Use coordinate compression when endpoints are huge but sparse.

## Common mistakes

- **Watch for:** Merging touching intervals when touching is allowed but not overlapping—or vice versa.
- **Watch for:** Incorrect event tie order.
- **Watch for:** Mutating input ordering unexpectedly.
- **Watch for:** Using O(max_coordinate) arrays for sparse 10^9 endpoints.

## Implementation drills

1. Merge unsorted intervals.
2. Compute maximum overlap with events.
3. Insert one interval into sorted disjoint intervals.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Interval fundamentals

Almost every interval problem starts with the same move: **sort by start**. Then a
single scan merges, inserts, or compares. Decide whether touching intervals
(`end == next start`) count as overlapping — that is the usual off-by-one.

```python
def merge_intervals(intervals):
    """Merge all overlapping intervals. Touching ends count as overlapping."""
    if not intervals:
        return []
    ordered = sorted(intervals)
    merged = [list(ordered[0])]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:                  # <= merges [1,2] and [2,3]
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


def insert_interval(intervals, new_interval):
    """Insert and merge: add everything before, merge the overlap, add the rest."""
    result, i = [], 0
    start, end = new_interval
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])                 # strictly before
        i += 1
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])         # grow the merged interval
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])
    result.extend(intervals[i:])
    return result


def interval_intersection(first, second):
    """Overlaps between two lists: two pointers, advance the one that ends first."""
    result, i, j = [], 0, 0
    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])
        if start <= end:
            result.append([start, end])
        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1
    return result


def can_attend_meetings(intervals):
    """Any overlap at all? Sort, then compare each interval with the previous end."""
    ordered = sorted(intervals)
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True


def is_covered_by(intervals, target):
    """Is every point of `target` covered by the (merged) intervals?"""
    merged = merge_intervals(intervals)
    left, right = target
    for start, end in merged:
        if start <= left <= end:
            left = end + 1                          # covered up to here
            if left > right:
                return True
    return False


if __name__ == "__main__":
    print("merge:", merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print("merge touching:", merge_intervals([[1, 2], [2, 3]]))
    print("merge nested:", merge_intervals([[1, 10], [2, 3], [4, 5]]))
    print("insert [4, 8]:", insert_interval([[1, 3], [6, 9]], [4, 8]))
    print("insert [2, 5]:", insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [2, 5]))
    print("intersection:", interval_intersection([[0, 2], [5, 10], [13, 23]], [[1, 5], [8, 12], [15, 24]]))
    print("can attend:", can_attend_meetings([[0, 30], [5, 10], [15, 20]]))
    print("can attend (no clash):", can_attend_meetings([[7, 10], [2, 4]]))
    print("covered by:", is_covered_by([[1, 2], [3, 4], [5, 6]], [1, 6]))
    print("not covered:", is_covered_by([[1, 2], [3, 4]], [1, 6]))
```

Output:

```text
merge: [[1, 6], [8, 10], [15, 18]]
merge touching: [[1, 3]]
merge nested: [[1, 10]]
insert [4, 8]: [[1, 3], [4, 9]]
insert [2, 5]: [[1, 5], [6, 7], [8, 10], [12, 16]]
intersection: [[1, 2], [5, 5], [8, 10], [15, 23]]
can attend: False
can attend (no clash): True
covered by: True
not covered: False
```

**How it works**

- `merge_intervals` compares `start` with the running end. Use `<=` to merge touching intervals, `<` to keep them separate — ask which the problem wants.
- `insert_interval` is three phases in one pass: copy what ends before the new interval, grow the new interval over everything that overlaps it, then copy the rest. No explicit merging step is needed.
- `interval_intersection` advances the pointer whose interval ends first: the other one might still overlap with several intervals.
- Sorting costs O(n log n); everything after that is O(n).

### 2. Line sweep: count what happens at each boundary

Instead of comparing interval pairs, turn each interval into two **events**
(`+1` at start, `−1` at end) and sweep left to right while maintaining a running
counter. This answers "maximum overlap", "is capacity exceeded", and "how many are
active at time t" in O(n log n).

```python
from collections import defaultdict


def max_overlap(intervals):
    """Maximum number of intervals active at the same instant."""
    events = defaultdict(int)
    for start, end in intervals:
        events[start] += 1
        events[end] -= 1
    active = best = 0
    for time in sorted(events):                  # sweep in time order
        active += events[time]
        best = max(best, active)
    return best


def min_meeting_rooms_sweep(intervals):
    """Same idea: the peak of the sweep is the number of rooms required."""
    events = defaultdict(int)
    for start, end in intervals:
        events[start] += 1
        events[end] -= 1
    active = peak = 0
    for time in sorted(events):
        active += events[time]
        peak = max(peak, active)
    return peak


def car_pooling(trips, capacity):
    """trips = (passengers, from, to). Pick-ups happen before drop-offs at the
    same location, so a plain per-location delta works: sort events by location."""
    events = defaultdict(int)
    for passengers, start, end in trips:
        events[start] += passengers
        events[end] -= passengers
    load = 0
    for location in sorted(events):
        load += events[location]
        if load > capacity:
            return False
    return True


def is_point_covered(intervals, point):
    """Sweep answer to a membership query: count of starts minus ends before it."""
    active = 0
    for start, end in intervals:
        if start <= point <= end:
            active += 1
    return active


if __name__ == "__main__":
    intervals = [(0, 30), (5, 10), (15, 20)]
    print("max overlap:", max_overlap(intervals))
    print("rooms needed (sweep):", min_meeting_rooms_sweep(intervals))
    print("non-overlapping:", max_overlap([(1, 2), (3, 4)]))

    print("car pooling ok:", car_pooling([(2, 1, 5), (3, 3, 7)], 4))
    print("car pooling too full:", car_pooling([(2, 1, 5), (3, 3, 7)], 3))
    print("point 7 covered:", is_point_covered(intervals, 7),
          "| point 12 covered:", is_point_covered(intervals, 12))
    print("empty input:", max_overlap([]), min_meeting_rooms_sweep([]))
```

Output:

```text
max overlap: 2
rooms needed (sweep): 2
non-overlapping: 1
car pooling ok: False
car pooling too full: False
point 7 covered: 2 | point 12 covered: 1
empty input: 0 0
```

**How it works**

- A sweep reduces a 2D problem (intervals over time) to a 1D walk over sorted event points. The counter between events is the number of active intervals.
- Ordering matters when a start and an end share a coordinate: `[1, 2]` and `[2, 3]` overlap only if you treat the end as inclusive. With `+1/−1` at the same key they cancel, which models half-open intervals — state your convention.
- `car_pooling` shows the "sweep over a different axis" (location instead of time): the technique is identical, only the meaning of the coordinate changes.

## Solved examples

### Example 1 — Insert interval (Medium)

**Problem.** Given a sorted list of non-overlapping intervals, insert a new one
and merge any resulting overlaps.

**Approach.** Three-phase single pass: append intervals that end before the new one starts, merge everything that overlaps it (growing `start` and `end`), then append the remainder. Because the input is already sorted and disjoint, no sorting is needed — O(n).

```python
def insert(intervals, new_interval):
    result, i = [], 0
    start, end = new_interval

    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])                 # entirely before
        i += 1

    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])         # overlap: widen the interval
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    result.extend(intervals[i:])                    # entirely after
    return result


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))                         # [[1,5],[6,9]]
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
    print("insert at the front:", insert([[3, 5], [6, 9]], [1, 2]))
    print("insert at the end:", insert([[1, 2]], [5, 7]))
    print("empty list:", insert([], [5, 7]))
```

Output:

```text
[[1, 5], [6, 9]]
[[1, 2], [3, 10], [12, 16]]
insert at the front: [[1, 2], [3, 5], [6, 9]]
insert at the end: [[1, 2], [5, 7]]
empty list: [[5, 7]]
```

**Complexity.** O(n) time, O(n) space for the result. The two `while` loops each advance `i`, so every interval is examined once.

### Example 2 — Meeting rooms II (Medium)

**Problem.** Minimum number of rooms needed so no two meetings overlap in the
same room.

**Approach.** Sort start times and end times separately, then walk both: if the earliest meeting starts before the earliest ending, we need a new room; otherwise a room frees up and we reuse it. (The heap version below tracks the end time of each occupied room and is easier to adapt when you also need the assignment.)

```python
import heapq


def min_meeting_rooms(intervals):
    """Two-pointer over sorted starts and ends."""
    if not intervals:
        return 0
    starts = sorted(start for start, _ in intervals)
    ends = sorted(end for _, end in intervals)
    rooms = active = 0
    s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:                     # new meeting before a room frees
            active += 1
            rooms = max(rooms, active)
            s += 1
        else:                                       # a room became free
            active -= 1
            e += 1
    return rooms


def min_meeting_rooms_heap(intervals):
    """Heap of end times: reuse the room that frees up earliest."""
    if not intervals:
        return 0
    intervals = sorted(intervals)
    rooms = []                                      # end times of occupied rooms
    for start, end in intervals:
        if rooms and rooms[0] <= start:             # earliest-ending room is free
            heapq.heapreplace(rooms, end)
        else:
            heapq.heappush(rooms, end)
    return len(rooms)


if __name__ == "__main__":
    intervals = [(0, 30), (5, 10), (15, 20)]
    print("rooms (two pointers):", min_meeting_rooms(intervals))
    print("rooms (heap):", min_meeting_rooms_heap(intervals))
    print("no overlap:", min_meeting_rooms([(1, 2), (3, 4)]))
    print("all overlap:", min_meeting_rooms([(1, 5), (2, 6), (3, 7)]))
    print("empty:", min_meeting_rooms([]), min_meeting_rooms_heap([]))
```

Output:

```text
rooms (two pointers): 2
rooms (heap): 2
no overlap: 1
all overlap: 3
empty: 0 0
```

**Complexity.** O(n log n) time (sorting) and O(n) space for both versions. The heap version returns the actual room count naturally and extends to "which room for which meeting".

### Example 3 — Minimum arrows to burst balloons (Medium)

**Problem.** Balloons are horizontal intervals; an arrow shot at x bursts every
balloon whose interval contains x. Find the minimum number of arrows.

**Approach.** Sort by end, then greedily shoot at the end of the first balloon: that arrow bursts every balloon starting at or before it, so it is never worse than shooting earlier. Move to the first unburst balloon and repeat. This is the interval-covering greedy — the same one as activity selection, applied to points instead of intervals.

```python
def find_min_arrow_shots(points):
    if not points:
        return 0
    ordered = sorted(points, key=lambda p: p[1])
    arrows = 0
    arrow_at = float("-inf")
    for start, end in ordered:
        if start > arrow_at:                 # not burst by the current arrow
            arrows += 1
            arrow_at = end                   # shoot at its end: covers the most
    return arrows


def non_overlapping_removals(intervals):
    """Related greedy: minimum removals so no intervals overlap."""
    if not intervals:
        return 0
    ordered = sorted(intervals, key=lambda x: x[1])
    kept, last_end = 0, float("-inf")
    for start, end in ordered:
        if start >= last_end:
            kept += 1
            last_end = end
    return len(intervals) - kept


if __name__ == "__main__":
    print("arrows for [[10,16],[2,8],[1,6],[7,12]]:",
          find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    print("arrows for [[1,2],[3,4],[5,6],[7,8]]:",
          find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]))
    print("arrows for [[1,2],[2,3],[3,4],[4,5]]:",
          find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]))
    print("removals for [[1,2],[2,3],[3,4],[1,3]]:",
          non_overlapping_removals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print("empty:", find_min_arrow_shots([]))
```

Output:

```text
arrows for [[10,16],[2,8],[1,6],[7,12]]: 2
arrows for [[1,2],[3,4],[5,6],[7,8]]: 4
arrows for [[1,2],[2,3],[3,4],[4,5]]: 2
removals for [[1,2],[2,3],[3,4],[1,3]]: 1
empty: 0
```

**Complexity.** O(n log n) time for the sort, O(1) extra space beyond it. Note the touching case: `[1, 2]` and `[2, 3]` are both burst by an arrow at 2, which the `start > arrow_at` test handles.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Room Allocation](https://cses.fi/problemset/task/1164) | CSES | Medium |
| [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | LeetCode | Medium |
| [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/) | LeetCode | Medium |
| [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain overlap rules depend on closed, open, or half-open endpoints without notes.
- [ ] Explain merge after sorting by start without notes.
- [ ] Explain earliest-end greedy maximizes non-overlapping selections without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
