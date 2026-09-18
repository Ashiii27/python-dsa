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
