# Lesson 08 — Errors, Debugging & Testing

## 1. Exceptions are control flow, not disasters

```python
try:
    value = int(text)
except ValueError as exc:
    logger.warning("bad input %r: %s", text, exc)
    value = 0
except (KeyError, IndexError):
    raise                       # re-raise unchanged
else:
    print("no exception happened")
finally:
    cleanup()                   # always runs
```

Rules:
- Catch the **narrowest** exception you can handle. Never bare `except:`.
- `raise ValueError("msg") from exc` keeps the cause chain.
- EAFP ("try it and handle failure") is idiomatic Python; LBYL ("check first") invites races.

## 2. The hierarchy you should know

`BaseException` → `Exception` → `ValueError`, `TypeError`, `KeyError`, `IndexError`,
`AttributeError`, `ZeroDivisionError`, `FileNotFoundError` (an `OSError`), `StopIteration`.
`KeyboardInterrupt` / `SystemExit` sit outside `Exception` — that's why bare `except:` is harmful.

## 3. Custom exceptions

```python
class AppError(Exception): ...
class NotFound(AppError):
    def __init__(self, key): super().__init__(f"{key} not found"); self.key = key
```
One base class per app makes callers able to catch everything you raise.

## 4. Context managers

```python
with open("f.txt") as fh:      # closed even on exception
    ...

from contextlib import contextmanager, suppress
@contextmanager
def timer():
    start = time.perf_counter()
    try: yield
    finally: print(time.perf_counter() - start)

with suppress(FileNotFoundError):
    os.remove(path)
```

## 5. Debugging

- Read the traceback **bottom-up**: last line = error, above it = where.
- `breakpoint()` drops into pdb (`n` next, `s` step, `c` continue, `p expr`, `l` list, `q` quit).
- `logging` over `print` in real code; `print(f"{x=}")` for quick checks.

## 6. Testing with `unittest` (stdlib) / `pytest`

```python
class TestThing(unittest.TestCase):
    def setUp(self): self.obj = Thing()
    def test_happy(self): self.assertEqual(self.obj.run(1), 2)
    def test_raises(self):
        with self.assertRaises(ValueError): self.obj.run(-1)

python -m unittest discover -s . -p "test_*.py"
```

Always test: the happy path, empty input, a single element, duplicates, the maximum size, and the error case.

## Checkpoints
- Why is bare `except:` dangerous?
- What's the difference between `else` and `finally` on a `try`?
- What is EAFP, and give a dict example.

## Practice
`python test_exercises.py`
