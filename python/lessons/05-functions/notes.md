# Lesson 05 — Functions, Scope & Arguments

## 1. Argument kinds

```python
def f(pos, /, normal, *args, kw_only, default=1, **kwargs): ...
```

- `/` — everything before it is positional-only.
- `*args` — extra positional args as a tuple.
- `*` or `*args` — everything after is **keyword-only** (great for boolean flags).
- `**kwargs` — extra keyword args as a dict.

Call with keywords whenever an argument is not self-explanatory: `sort(items, reverse=True)`.

## 2. The mutable default trap

```python
def bad(item, bucket=[]):      # the list is created ONCE, at def time
    bucket.append(item); return bucket

def good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    ...
```

## 3. Scope: LEGB

Local → Enclosing → Global → Builtins. Assignment inside a function makes the name local
unless you declare `global x` or `nonlocal x`. Reading is fine without declaration.

## 4. Closures

```python
def counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc
```
Late-binding gotcha: `[lambda: i for i in range(3)]` all return 2. Fix with `lambda i=i: i`.

## 5. First-class functions & lambdas

Functions are objects: pass them, store them, return them. `key=` parameters are the everyday use.
Keep lambdas to one expression; name anything longer.

## 6. Decorators

```python
import functools

def logged(fn):
    @functools.wraps(fn)                # preserve __name__/__doc__
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} -> {result}")
        return result
    return wrapper

@functools.lru_cache(maxsize=None)      # memoization: turns exponential recursion linear
def fib(n): return n if n < 2 else fib(n-1) + fib(n-2)
```

## 7. Recursion in Python

Default recursion limit ~1000 (`sys.setrecursionlimit`). No tail-call optimization — deep
recursion on 10^5 nodes must be converted to an explicit stack. This matters constantly in DSA.

## Checkpoints
- Why does the mutable default bug happen and what is the idiom that avoids it?
- What does `nonlocal` do that `global` doesn't?
- How does `lru_cache` change the complexity of naive fib?

## Practice
`python test_exercises.py`
