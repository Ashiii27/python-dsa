# Lesson 04 — Control Flow & Comprehensions

## 1. Loops done the Python way

```python
for item in items: ...
for i, item in enumerate(items, start=1): ...
for a, b in zip(xs, ys): ...              # stops at the shorter one
for i in range(n) / range(a, b) / range(a, b, -1): ...
for k, v in d.items(): ...
```

Never write `for i in range(len(xs)): x = xs[i]` unless you genuinely need the index.

## 2. `break`, `continue`, and `for ... else`

```python
for x in xs:
    if pred(x):
        break
else:
    # runs only if the loop finished WITHOUT break
    handle_not_found()
```

## 3. Mutation while iterating

Never mutate a list/dict you are looping over. Iterate a copy (`for x in xs[:]`) or build a new list.

## 4. Comprehensions

```python
[f(x) for x in xs if pred(x)]                # list
{k: f(v) for k, v in d.items()}              # dict
{x % 3 for x in xs}                          # set
(x * x for x in xs)                          # generator: lazy, O(1) memory
[[cell for cell in row] for row in grid]     # nested
[y for row in grid for y in row]             # flatten: loops in for-statement order
```

Rule of thumb: one map + one filter = comprehension. More logic than that = a real loop.

## 5. Conditional expressions & short-circuit

```python
label = "even" if n % 2 == 0 else "odd"
value = user_input or "default"     # careful: 0 and "" are falsy
name = obj and obj.name
```

## 6. `while`, sentinels, and `match`

```python
while queue:
    node = queue.popleft()

match command.split():
    case ["go", direction]:  ...
    case ["quit"]:           ...
    case _:                  ...
```

## 7. Iteration helpers you should reach for

`any()`, `all()`, `sum()`, `min(..., key=)`, `max(..., key=)`, `sorted(..., key=, reverse=)`, `reversed()`, `filter`/`map` (prefer comprehensions).

## Checkpoints
- What does `for/else` actually mean?
- Why is `(x*x for x in range(10**9))` fine but the list version is not?
- What is wrong with `for x in xs: if bad(x): xs.remove(x)`?

## Practice
`python test_exercises.py`
