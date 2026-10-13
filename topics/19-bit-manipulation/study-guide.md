# Bit Manipulation: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

View integers as fixed-width sets of binary positions. XOR captures parity/difference, masks select subsets or fields, and lowbit isolates the least significant set bit.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | AND tests/clears bits; OR sets bits; XOR toggles and cancels pairs. |
| 2 | `x & (x-1)` removes the lowest set bit. |
| 3 | `x & -x` isolates the lowest set bit. |
| 4 | Subsets of n items correspond to masks 0 through 2^n-1. |
| 5 | Python negative integers require explicit masking for fixed-width emulation. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Pairs cancel, one remains | XOR |
| Enumerate small-n subsets | Bitmask |
| State is a small set | Bitmask DP |
| Need per-bit counts | Scan fixed bit positions |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

`12 = 1100₂`. Then `12 & 11 = 1100 & 1011 = 1000`, removing one set bit. Repeating until zero counts set bits in time proportional to the number of ones.

## Tricks and interview notes

- Use `(mask >> bit) & 1` for a readable membership test.
- Parenthesize bit expressions; precedence is easy to misread.
- For 32-bit answers in Python, mask with `0xFFFFFFFF`.
- XOR prefix arrays answer range XOR exactly like sum prefixes.

## Common mistakes

- **Watch for:** Assuming right shift of a negative Python integer inserts zeros.
- **Watch for:** Using floating `log2` to locate bits.
- **Watch for:** Confusing XOR with exponentiation (`**` is exponentiation in Python).
- **Watch for:** Ignoring exponential 2^n mask count.

## Implementation drills

1. Implement popcount three ways.
2. Enumerate submasks of a mask.
3. Solve single-number variants using per-bit reasoning.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Bit primitives

Everything below is O(1). The six operations to know cold: `&` (and), `|` (or),
`^` (xor), `~` (not), `<<` (shift left = multiply by 2), `>>` (shift right =
divide by 2).

```python
def get_bit(n, i):
    """Value of bit i (0 or 1)."""
    return (n >> i) & 1


def set_bit(n, i):
    """Force bit i to 1."""
    return n | (1 << i)


def clear_bit(n, i):
    """Force bit i to 0."""
    return n & ~(1 << i)


def toggle_bit(n, i):
    """Flip bit i."""
    return n ^ (1 << i)


def update_bit(n, i, value):
    """Set bit i to `value` (0 or 1) in one expression."""
    return (n & ~(1 << i)) | (value << i)


def is_power_of_two(n):
    """A power of two has exactly one set bit: n & (n-1) clears it."""
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n):
    """Brian Kernighan: one loop iteration per set bit, not per bit."""
    count = 0
    while n:
        n &= n - 1                 # clear the lowest set bit
        count += 1
    return count


def lowest_set_bit(n):
    """Isolate the rightmost 1 (0 if n == 0)."""
    return n & -n


def clear_lowest_set_bit(n):
    return n & (n - 1)


def swap_with_xor(a, b):
    """XOR swap — a curiosity; use a, b = b, a in real Python."""
    a ^= b
    b ^= a
    a ^= b
    return a, b


def reverse_bits(n, width=8):
    """Mirror the bits within `width` positions."""
    result = 0
    for i in range(width):
        if (n >> i) & 1:
            result |= 1 << (width - 1 - i)
    return result


if __name__ == "__main__":
    n = 0b1011_0100
    print(f"n = {n:>3} = {n:08b}")
    for i in (0, 2, 7):
        print(f"  bit {i}: {get_bit(n, i)}")
    print("set bit 0   :", f"{set_bit(n, 0):08b}")
    print("clear bit 2 :", f"{clear_bit(n, 2):08b}")
    print("toggle bit 7:", f"{toggle_bit(n, 7):08b}")
    print("update bit 7 to 0:", f"{update_bit(n, 7, 0):08b}")

    for value in (1, 2, 8, 12, 16):
        print(f"  {value:>2} = {value:05b} | power of two: {is_power_of_two(value)} "
              f"| set bits: {count_set_bits(value)}")

    print("lowest_set_bit(12):", f"{lowest_set_bit(12):08b}", "(= 4)")
    print("clear_lowest_set_bit(12):", f"{clear_lowest_set_bit(12):08b}")
    print("swap_with_xor(3, 9):", swap_with_xor(3, 9))
    print("reverse_bits(0b00000101, 8):", f"{reverse_bits(0b00000101):08b}")
    print("negative note: ~5 =", ~5, "because Python ints are unbounded (two's complement)")
```

Output:

```text
n = 180 = 10110100
  bit 0: 0
  bit 2: 1
  bit 7: 1
set bit 0   : 10110101
clear bit 2 : 10110000
toggle bit 7: 00110100
update bit 7 to 0: 00110100
   1 = 00001 | power of two: True | set bits: 1
   2 = 00010 | power of two: True | set bits: 1
   8 = 01000 | power of two: True | set bits: 1
  12 = 01100 | power of two: False | set bits: 2
  16 = 10000 | power of two: True | set bits: 1
lowest_set_bit(12): 00000100 (= 4)
clear_lowest_set_bit(12): 00001000
swap_with_xor(3, 9): (9, 3)
reverse_bits(0b00000101, 8): 10100000
negative note: ~5 = -6 because Python ints are unbounded (two's complement)
```

**How it works**

- `1 << i` builds a mask with a single bit; `~(1 << i)` is its complement. In Python `~n = −n − 1`, and negative numbers behave as if they had infinitely many leading 1s, which is what makes `n & ~(1 << i)` work for any width.
- `n & (n − 1)` drops the lowest set bit — the engine behind "count set bits", "is power of two", and "iterate over set bits".
- `n & −n` isolates the lowest set bit, used for splitting numbers by their lowest differing bit (the two-single-numbers problem) and for Fenwick tree steps.
- Precedence trap: `==` binds tighter than `&`, so always parenthesise bit expressions in comparisons.

### 2. Bitmasks as sets and search spaces

A mask is an `n`-bit number where bit `i` means "element i is in the set". That
turns subset enumeration into a loop and set operations into single instructions.

```python
def all_subsets(items):
    """Every subset: 2^n masks, bit i selects items[i]."""
    n = len(items)
    subsets = []
    for mask in range(1 << n):
        subsets.append([items[i] for i in range(n) if mask & (1 << i)])
    return subsets


def submasks(mask):
    """All subsets of a mask, largest first: m = (m - 1) & mask."""
    m = mask
    while m:
        yield m
        m = (m - 1) & mask
    yield 0


def mask_of(indices):
    """Build a mask from a list of chosen positions."""
    mask = 0
    for i in indices:
        mask |= 1 << i
    return mask


def popcount_dp(limit):
    """popcount for every number 0..limit: dp[i] = dp[i >> 1] + (i & 1)."""
    bits = [0] * (limit + 1)
    for i in range(1, limit + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


def subset_sum_possible(values, target):
    """Bitmask DP: reachable sums after each element (classic 'can we hit target')."""
    reachable = 1                                  # bit 0 = sum 0 is reachable
    for value in values:
        reachable |= reachable << value
    return bool(reachable & (1 << target))


def xor_prefix(nums):
    """prefix[i] = XOR of nums[:i], so XOR of [l, r] = prefix[r+1] ^ prefix[l]."""
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] ^ x)
    return prefix


if __name__ == "__main__":
    print("subsets of ['a', 'b', 'c']:")
    for subset in all_subsets(["a", "b", "c"]):
        print("  ", subset)

    mask = 0b1011
    print("submasks of 1011:", [f"{m:04b}" for m in submasks(mask)])
    print("mask_of([0, 2]):", f"{mask_of([0, 2]):04b}")
    print("popcounts 0..8:", popcount_dp(8))
    print("subset_sum([3, 34, 4, 12, 5, 2], 9):", subset_sum_possible([3, 34, 4, 12, 5, 2], 9))
    print("subset_sum([3, 34, 4, 12, 5, 2], 30):", subset_sum_possible([3, 34, 4, 12, 5, 2], 30))

    prefix = xor_prefix([1, 2, 3, 4])
    print("xor prefix:", prefix, "| xor of [1, 3):", prefix[3] ^ prefix[1])
```

Output:

```text
subsets of ['a', 'b', 'c']:
   []
   ['a']
   ['b']
   ['a', 'b']
   ['c']
   ['a', 'c']
   ['b', 'c']
   ['a', 'b', 'c']
submasks of 1011: ['1011', '1010', '1001', '1000', '0011', '0010', '0001', '0000']
mask_of([0, 2]): 0101
popcounts 0..8: [0, 1, 1, 2, 1, 2, 2, 3, 1]
subset_sum([3, 34, 4, 12, 5, 2], 9): True
subset_sum([3, 34, 4, 12, 5, 2], 30): False
xor prefix: [0, 1, 3, 0, 4] | xor of [1, 3): 1
```

**How it works**

- `all_subsets` enumerates `2ⁿ` masks. It is the brute force behind assignment and partition problems, and the baseline that bitmask DP improves on.
- `m = (m − 1) & mask` walks all submasks in O(2^k) for k set bits — the standard enumeration for subset-DP transitions.
- `reachable |= reachable << value` is a subset-sum DP encoded in the bits of one integer: after processing an element, every previously reachable sum `s` also makes `s + value` reachable.
- XOR prefix sums work exactly like additive prefix sums because XOR is its own inverse (`a ^ a = 0`).

## Solved examples

### Example 1 — The single-number family (Easy)

**Problem.** (a) Every number appears twice except one — find it. (b) Two numbers
appear once — find both. (c) Find the missing number in `0..n`.

**Approach.** XOR cancels pairs (`a ^ a = 0`, `a ^ 0 = a`), so XOR-ing everything leaves the odd one out. For two singles, XOR-ing everything gives `a ^ b`; any set bit in that result is a bit where `a` and `b` differ, so partition the input on that bit and XOR each group separately. For the missing number, XOR the indices and the values together — everything present cancels.

```python
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result


def single_number_iii(nums):
    """Two elements appear once; return both."""
    xor_all = 0
    for x in nums:
        xor_all ^= x
    differing_bit = xor_all & -xor_all            # lowest set bit: a and b differ here
    a = b = 0
    for x in nums:
        if x & differing_bit:                    # split into two groups
            a ^= x
        else:
            b ^= x
    return [a, b]


def missing_number(nums):
    """nums holds n of the n+1 values in 0..n."""
    result = len(nums)                           # the extra index
    for i, x in enumerate(nums):
        result ^= i ^ x
    return result


if __name__ == "__main__":
    print("single_number([4, 1, 2, 1, 2]):", single_number([4, 1, 2, 1, 2]))
    print("single_number_iii([1, 2, 1, 3, 2, 5]):", single_number_iii([1, 2, 1, 3, 2, 5]))
    print("missing_number([3, 0, 1]):", missing_number([3, 0, 1]))
    print("missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]):",
          missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print("single element:", single_number([7]))
```

Output:

```text
single_number([4, 1, 2, 1, 2]): 4
single_number_iii([1, 2, 1, 3, 2, 5]): [3, 5]
missing_number([3, 0, 1]): 2
missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]): 8
single element: 7
```

**Complexity.** O(n) time and O(1) space in every case — no hash map needed.

### Example 2 — Counting bits and power checks (Easy)

**Problem.** Return the number of 1-bits for every number from `0` to `n`.

**Approach.** Compute each from a smaller number: dropping the lowest bit gives `i >> 1`, so `bits[i] = bits[i >> 1] + (i & 1)`. One pass, O(n). The same "one bit at a time" reasoning gives the power-of-four test: a power of four is a power of two whose single set bit sits at an even position, and `0x55555555` is the mask of all even-position bits.

```python
def count_bits(n):
    """bits[i] = number of 1-bits in i, for every i in 0..n."""
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


def is_power_of_four(n):
    """Power of two AND its single bit is at an even index."""
    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0


def reverse_bits_32(n):
    """Reverse the bits of a 32-bit unsigned integer."""
    result = 0
    for i in range(32):
        result = (result << 1) | ((n >> i) & 1)
    return result


if __name__ == "__main__":
    print("count_bits(5):", count_bits(5), "(0,1,1,2,1,2)")
    print("count_bits(8):", count_bits(8))
    print("check against bin():", all(bits == bin(i).count("1")
                                     for i, bits in enumerate(count_bits(64))))
    for value in (1, 2, 4, 8, 16, 3, 5):
        print(f"  {value:>2}: power of two = {value > 0 and (value & (value - 1)) == 0}, "
              f"power of four = {is_power_of_four(value)}")
    print("reverse_bits_32(0b101):", reverse_bits_32(0b101))
```

Output:

```text
count_bits(5): [0, 1, 1, 2, 1, 2] (0,1,1,2,1,2)
count_bits(8): [0, 1, 1, 2, 1, 2, 2, 3, 1]
check against bin(): True
   1: power of two = True, power of four = True
   2: power of two = True, power of four = False
   4: power of two = True, power of four = True
   8: power of two = True, power of four = False
  16: power of two = True, power of four = True
   3: power of two = False, power of four = False
   5: power of two = False, power of four = False
reverse_bits_32(0b101): 2684354560
```

**Complexity.** O(n) time and O(n) space for `count_bits`; O(1) for the power checks.

### Example 3 — Sum of two integers without `+` or `-` (Medium)

**Problem.** Compute `a + b` using only bit operations.

**Approach.** Think in two columns: `a ^ b` adds without carrying, and `(a & b) << 1` is the carry. Repeat until the carry is zero. In Python (unbounded ints) you must mask to a fixed width, otherwise a negative operand loops forever — masking to 32 bits and re-interpreting the sign at the end is the standard fix.

```python
def get_sum(a, b, bits=32):
    mask = (1 << bits) - 1                  # 0xFFFFFFFF for 32-bit arithmetic
    a &= mask
    b &= mask
    while b:
        carry = ((a & b) << 1) & mask       # which columns carry
        a = (a ^ b) & mask                  # add without carry
        b = carry
    # Reinterpret as a signed value if the top bit is set.
    return a if a <= mask >> 1 else a - (1 << bits)


if __name__ == "__main__":
    print("get_sum(1, 2):", get_sum(1, 2))
    print("get_sum(5, 7):", get_sum(5, 7))
    print("get_sum(-1, 1):", get_sum(-1, 1))
    print("get_sum(-2, 3):", get_sum(-2, 3))
    print("get_sum(0, 0):", get_sum(0, 0))
    print("matches Python:", get_sum(12345, 6789) == 12345 + 6789)
```

Output:

```text
get_sum(1, 2): 3
get_sum(5, 7): 12
get_sum(-1, 1): 0
get_sum(-2, 3): 1
get_sum(0, 0): 0
matches Python: True
```

**Complexity.** O(bits) time — at most 32 iterations — and O(1) space. The same add-without-carry idea underlies hardware adders and is a favourite interview question precisely because it forces you to reason about carries.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Hamming Distance](https://leetcode.com/problems/hamming-distance/) | LeetCode | Easy |
| [Bit Strings](https://cses.fi/problemset/task/1617) | CSES | Easy |
| [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | LeetCode | Medium |
| [Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain and tests/clears bits; or sets bits; xor toggles and cancels pairs without notes.
- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
