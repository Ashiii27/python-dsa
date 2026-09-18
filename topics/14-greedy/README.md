# Greedy Algorithms

**Level:** Core to Advanced

Make locally optimal choices only when you can prove they are globally safe.

---

## What you must learn

- Exchange arguments
- Stays-ahead proofs
- Sorting by key
- Interval scheduling
- Reachability greediness
- Heap-assisted greedy
- Cut property for MST

---

## Core patterns and approaches

- Sort intervals by end to maximize non-overlap
- Track farthest reach for jump problems
- Use heap when the best available choice changes over time
- Use exchange argument to justify local choices
- If greedy fails, look for DP

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def can_jump(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Track farthest reachable index. | O(n) | O(1) |
| [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | BFS-layer style greedy over current range. | O(n) | O(1) |
| [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | If total gas sufficient, reset start when tank goes negative. | O(n) | O(1) |
| [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Sort by end and keep intervals finishing earliest. | O(n log n) | O(1) |
| [Candy](https://leetcode.com/problems/candy/) | Hard | Two passes satisfy left and right neighbor constraints. | O(n) | O(n) |
| [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | Use last occurrence to close partitions greedily. | O(n) | O(1) |
| [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | Sort taller first, insert by k. | O(n^2) | O(n) |
| [Minimum Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | Medium | Sort by end; shoot arrow at current end. | O(n log n) | O(1) |
| [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | Sort weights; pair lightest with heaviest when possible. | O(n log n) | O(1) |

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
