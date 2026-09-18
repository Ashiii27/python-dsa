# Lesson 06 — Iterators, Generators & itertools

## 1. The iterator protocol

`for x in obj` really does:

```python
it = iter(obj)          # obj.__iter__()
while True:
    try: x = next(it)   # it.__next__()
    except StopIteration: break
```

An **iterable** can produce an iterator. An **iterator** is one-shot: once exhausted, it stays exhausted.
This explains the classic bug `list(zip(a, b))` being empty the second time when `a` was a generator.

## 2. Generators

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

A generator function returns a lazy iterator: state is suspended at each `yield`.
Benefits: O(1) memory, works with infinite streams, composes in pipelines.

```python
def read_ints(lines):
    for line in lines:                 # pipeline stage
        yield int(line.strip())

yield from other_generator()           # delegate
```

## 3. Generator expressions

```python
total = sum(x * x for x in range(10**7))   # no intermediate list
any(is_valid(x) for x in stream)           # short-circuits
```

## 4. `itertools` greatest hits

```python
from itertools import (count, cycle, repeat, chain, islice, accumulate,
                       groupby, product, permutations, combinations, pairwise)

chain([1,2], [3])                 # 1 2 3
islice(count(0), 5)               # 0 1 2 3 4 (slice any iterator)
accumulate([1,2,3])               # 1 3 6
pairwise([1,2,3])                 # (1,2) (2,3)    3.10+
product([0,1], repeat=3)          # bitmask enumeration
permutations("abc", 2); combinations(range(4), 2)
groupby(sorted(rows, key=k), key=k)   # MUST be sorted by the key first
```

## 5. Useful builtins on iterators

`enumerate`, `zip`, `zip(*, strict=True)` (3.10+), `reversed`, `sorted`, `sum`, `min/max(key=)`, `any/all`, `next(it, default)`.

## Checkpoints
- Difference between an iterable and an iterator?
- Why is `groupby` on unsorted data almost always a bug?
- How do you take the first 5 items of an infinite generator?

## Practice
`python test_exercises.py`
