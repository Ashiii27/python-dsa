# Lesson 03 — Lists, Tuples, Sets & Dicts

**Goal:** pick the right container instantly and know its cost. This is the bridge between "Python" and "DSA".

## 1. Cost model (CPython)

| Operation | list | dict / set | deque |
|---|---|---|---|
| index / key lookup | O(1) | O(1) avg | O(1) at ends |
| append / add | O(1) amortized | O(1) avg | O(1) |
| insert(0) / pop(0) | **O(n)** | – | O(1) |
| `x in c` | **O(n)** | O(1) avg | O(n) |
| slice `c[a:b]` | O(k) copy | – | – |

The single most common beginner performance bug: `if x in big_list`. Convert to a `set` first.

## 2. Lists

```python
xs = [3, 1, 2]
xs.append(4); xs.extend([5, 6]); xs.insert(0, 0)
xs.pop(); xs.pop(0); xs.remove(3)         # remove() is by value, O(n)
xs.sort(); xs.sort(reverse=True)          # in place, returns None
ys = sorted(xs, key=lambda v: -v)         # new list
xs.index(2); xs.count(2); xs.reverse()
```

Copying: `xs[:]`, `list(xs)`, `copy.copy` are **shallow**. Nested structures need `[row[:] for row in grid]` or `copy.deepcopy`.

Gotcha: `grid = [[0] * 3] * 3` makes three references to *one* row. Use `[[0] * 3 for _ in range(3)]`.

## 3. Tuples

Immutable, hashable (if their contents are), great as dict keys and lightweight records.
`point = (x, y)`, unpacking `a, b = b, a`, starred `first, *rest = xs`.
`collections.namedtuple` / `typing.NamedTuple` for named fields.

## 4. Sets

`{1, 2}`, `set()` (not `{}`), `add`, `discard` (safe) vs `remove` (raises),
operators `|` union, `&` intersection, `-` difference, `^` symmetric difference,
`<=` subset. `frozenset` is the hashable version — usable as a dict key.

## 5. Dicts

```python
d = {"a": 1}
d["b"] = 2
d.get("z", 0)                 # no KeyError
d.setdefault("c", []).append(1)
d.pop("a", None)
for k, v in d.items(): ...
{**d1, **d2}   or   d1 | d2   # merge (3.9+)
sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))   # by value desc, key asc
```

Dicts preserve **insertion order** (guaranteed since 3.7). Keys must be hashable → no lists as keys, use tuples.

## 6. `collections` power tools

```python
from collections import Counter, defaultdict, deque
Counter("mississippi").most_common(2)     # [('i', 4), ('s', 4)]
groups = defaultdict(list); groups[k].append(v)
q = deque([1, 2]); q.appendleft(0); q.popleft()
deque(maxlen=3)                            # sliding buffer
```

## Checkpoints

- Why is `[[0]*3]*3` dangerous?
- When do you need `frozenset`?
- How do you sort by value descending and break ties by key ascending?

## Practice
`python test_exercises.py`
