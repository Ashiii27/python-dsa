# Binary Search

**Level:** Core to Advanced

Search sorted positions and monotonic answer spaces with precise boundary control.

---

## What you must learn

- Classic binary search
- Lower bound and upper bound
- Search in rotated sorted arrays
- Binary search on answer
- Monotonic predicates
- Floating-point binary search

---

## Core patterns and approaches

- Use lower bound for first true predicate
- Use upper bound for first value greater than target
- For rotated arrays, one half is sorted
- For answer search, write can(x) and prove monotonicity
- Keep invariant that answer remains inside the interval

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def first_true(lo, hi, pred):
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Compare middle with target and discard half. | O(log n) | O(1) |
| [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | Find first true predicate. | O(log n) | O(1) |
| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | Lower bound for target. | O(log n) | O(1) |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Identify sorted half and decide where target can be. | O(log n) | O(1) |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Compare mid with right to locate pivot/minimum. | O(log n) | O(1) |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Binary search speed; feasible if hours <= h. | O(n log M) | O(1) |
| [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Binary search capacity and simulate days. | O(n log sum) | O(1) |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | Binary search max subarray sum; greedily count partitions. | O(n log sum) | O(1) |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | Binary search partition in smaller array. | O(log min(n,m)) | O(1) |

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
