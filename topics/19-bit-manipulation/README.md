# Bit Manipulation

**Level:** Core to Advanced

Use binary representation for XOR tricks, masks, subsets, and compact DP state.

---

## What you must learn

- Bitwise AND/OR/XOR/NOT
- Shifts
- Set/clear/test bits
- XOR cancellation
- Power of two checks
- Subset masks
- Bitmask DP

---

## Core patterns and approaches

- XOR cancels equal values: a ^ a = 0
- n & (n-1) removes the lowest set bit
- Use masks to represent chosen subsets
- Iterate submasks with (sub-1) & mask
- For max XOR, use binary trie or greedy prefix set

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def iterate_subsets(n):
    for mask in range(1 << n):
        chosen = [i for i in range(n) if mask & (1 << i)]
        yield chosen
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Single Number | Easy | XOR all numbers; duplicates cancel. | O(n) | O(1) |
| Counting Bits | Easy | dp[i]=dp[i>>1]+(i&1). | O(n) | O(n) |
| Reverse Bits | Easy | Shift result and consume input bits. | O(bits) | O(1) |
| Missing Number | Easy | XOR indices and values, or use sum formula. | O(n) | O(1) |
| Sum of Two Integers | Medium | Use XOR for sum and AND-shift for carry. | O(bits) | O(1) |
| Maximum XOR of Two Numbers | Medium | Greedy prefix set or binary trie. | O(n*bits) | O(n) |
| Subsets via Bitmask | Medium | Enumerate masks from 0 to 2^n-1. | O(n*2^n) | O(n) |
| Shortest Superstring | Hard | Bitmask DP over last string and used set. | O(n^2*2^n) | O(n*2^n) |

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
