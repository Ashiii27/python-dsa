# Lesson 10 — Typing, Dataclasses & Clean Code

## 1. Type hints

```python
def total(prices: list[float], discount: float = 0.0) -> float: ...

from typing import Optional, Iterable, Callable, Any, TypeVar, Protocol
name: str | None = None                  # 3.10+ union syntax
mapping: dict[str, list[int]] = {}
handler: Callable[[int, str], bool]
T = TypeVar("T")
def first(xs: list[T]) -> T | None: ...
```

Hints do **not** run at runtime — they are for readers and for `mypy`/`pyright`:

```bash
pip install mypy && mypy .
```

`from __future__ import annotations` at the top makes all annotations lazy strings (cheap + forward refs).

## 2. Dataclasses

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Point:
    x: int
    y: int
    tags: list[str] = field(default_factory=list)   # never a mutable default
```
You get `__init__`, `__repr__`, `__eq__` free; `frozen=True` also gives `__hash__` and immutability;
`order=True` gives comparisons. Use `enum.Enum` for fixed choice sets.

## 3. Clean code rules that matter in reviews and interviews

- Names: `snake_case` functions/variables, `PascalCase` classes, `UPPER_CASE` constants.
- One function = one job; keep them short enough to read without scrolling.
- Return early instead of nesting `if`s.
- No magic numbers — name them.
- Docstrings say *what and why*, comments explain *why*, never restate the code.
- Prefer pure functions; isolate I/O at the edges. That is what makes code testable.
- Follow PEP 8; let tools enforce it (`ruff`, `black`) instead of arguing.

## 4. Structure of a real project

```text
project/
├── pyproject.toml
├── README.md
├── src/package/__init__.py
├── src/package/core.py
└── tests/test_core.py
```

## Checkpoints
- Do type hints slow your program down or change behaviour?
- Why `field(default_factory=list)` and not `= []`?
- When is `frozen=True` the right choice?

## Practice
`python test_exercises.py`
