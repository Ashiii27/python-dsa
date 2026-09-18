# Arrays and Strings

**Level:** Core

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Master contiguous data, indexing, two pointers, sliding windows, prefix sums, and matrix traversal.

---

## What you must learn

- Array indexing and in-place updates
- String immutability
- Two pointers
- Fixed and variable sliding window
- Prefix sums and difference arrays
- Kadane algorithm
- Matrix traversal and boundary simulation

---

## Core patterns and approaches

- Use two pointers when sorting lets you discard one side
- Use sliding window for contiguous ranges with adjustable constraints
- Use prefix sums when range sums repeat
- Use prefix-count maps when subarray sums can include negative numbers
- Use Kadane when the best segment can be extended or restarted

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

def two_pointers_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target: return [l, r]
        if s < target: l += 1
        else: r -= 1
    return []
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Two Sum](https://leetcode.com/problems/two-sum/) · [worked solution](problems/two-sum/README.md) | Easy | Hash map from value to index; check complement while scanning. | O(n) | O(n) |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · [worked solution](problems/best-time-to-buy-and-sell-stock/README.md) | Easy | Track minimum price so far and best profit. | O(n) | O(1) |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) · [worked solution](problems/product-of-array-except-self/README.md) | Medium | Prefix products then suffix products in reverse. | O(n) | O(1) extra |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) · [worked solution](problems/maximum-subarray/README.md) | Medium | Kadane: best subarray ending at current index. | O(n) | O(1) |
| [3Sum](https://leetcode.com/problems/3sum/) · [worked solution](problems/3sum/README.md) | Medium | Sort, fix one number, use two pointers and skip duplicates. | O(n^2) | O(1) extra |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) · [worked solution](problems/container-with-most-water/README.md) | Medium | Move shorter wall because height is bottleneck. | O(n) | O(1) |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · [worked solution](problems/longest-substring-without-repeating-characters/README.md) | Medium | Sliding window with last seen indices or set. | O(n) | O(k) |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) · [worked solution](problems/minimum-window-substring/README.md) | Hard | Expand to satisfy counts, shrink to minimize. | O(n) | O(k) |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) · [worked solution](problems/subarray-sum-equals-k/README.md) | Medium | Count previous prefix sums equal to current-prefix minus k. | O(n) | O(n) |
| [Rotate Image](https://leetcode.com/problems/rotate-image/) · [worked solution](problems/rotate-image/README.md) | Medium | Transpose then reverse rows, or rotate layer by layer. | O(n^2) | O(1) |
| [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) · [worked solution](problems/spiral-matrix/README.md) | Medium | Maintain top/bottom/left/right boundaries. | O(mn) | O(1) extra |

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
