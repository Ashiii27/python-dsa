# Lesson 02 — Types, Numbers & Strings

**Goal:** know exactly what each built-in scalar does, and be fluent with strings (the most common interview input type).

## 1. The scalar types

| Type | Notes |
|---|---|
| `int` | arbitrary precision — no overflow, but big ints cost more than a machine word |
| `float` | IEEE-754 double; `0.1 + 0.2 != 0.3` |
| `bool` | subclass of `int`: `True + True == 2` |
| `str` | immutable sequence of Unicode code points |
| `bytes` | immutable sequence of 0–255; `str.encode()` / `bytes.decode()` |
| `None` | the single null object |

## 2. Numbers

```python
7 / 2      # 3.5   true division (always float)
7 // 2     # 3     floor division
-7 // 2    # -4    floors toward -inf, unlike C
7 % 3      # 1
-7 % 3     # 2     result carries the divisor's sign  <-- interview favourite
divmod(7, 3)          # (2, 1)
2 ** 10               # 1024
round(2.5), round(3.5)  # (2, 4) banker's rounding
```

Float comparison: use `math.isclose(a, b)`, never `==`. Exact decimal money: `decimal.Decimal("0.1")`. Exact fractions: `fractions.Fraction(1, 3)`.

## 3. Strings are immutable

Every "mutation" makes a new string. Building in a loop with `s += x` is O(n²):

```python
parts = []
for w in words:
    parts.append(w)
"".join(parts)        # O(total length)
```

Core methods worth memorising:

```python
s.strip() / .lstrip() / .rstrip()
s.split() / s.split(",") / s.rsplit(",", 1) / s.splitlines()
",".join(items)
s.replace(old, new)
s.startswith(p) / s.endswith(p) / p in s
s.lower() / .upper() / .casefold() / .title()
s.find(sub)   # -1 if missing     s.index(sub)  # raises
s.isdigit() / .isalpha() / .isalnum() / .isspace()
s.zfill(3) / s.ljust(5) / s.rjust(5)
```

## 4. Slicing (works on every sequence)

```python
s[a:b:step]   # half-open: includes a, excludes b
s[::-1]       # reverse
s[:n], s[n:]  # split at n
```
Slices **copy** → O(k). Out-of-range slice bounds clamp silently; out-of-range indexing raises `IndexError`.

## 5. Conversion and formatting

```python
int("42"), int("ff", 16), float("1e-3"), str(42)
bin(10), oct(10), hex(10)            # '0b1010', '0o12', '0xa'
f"{3.14159:.2f}"  f"{42:05d}"  f"{0.25:.1%}"  f"{x!r}"  f"{x=}"
ord('a'), chr(97)                    # 97, 'a'
```

## Checkpoints

- Why does `-7 // 2 == -4`? What is `-7 % 2`?
- Why is repeated `s += c` quadratic, and what is the fix?
- What does `"abc"[::-1]` cost in time and space?

## Practice
`python test_exercises.py`
