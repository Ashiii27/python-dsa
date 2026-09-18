# Lesson 07 — Classes, Dunders & OOP Design

## 1. A class, properly written

```python
class Account:
    interest_rate = 0.02              # class attribute: shared

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner            # instance attributes
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount

    def __repr__(self) -> str:        # for developers; show how to rebuild it
        return f"Account(owner={self.owner!r}, balance={self.balance!r})"
```

`self` is explicit. A method is just a function whose first argument is the instance.

## 2. Dunder methods that earn their keep

| Dunder | Enables |
|---|---|
| `__repr__` / `__str__` | debugging / printing |
| `__eq__` + `__hash__` | `==`, use in sets/dict keys (define together, or none) |
| `__lt__` (+ `functools.total_ordering`) | sorting, `heapq` |
| `__len__`, `__getitem__`, `__contains__`, `__iter__` | container behaviour |
| `__enter__` / `__exit__` | `with` blocks |
| `__call__` | callable objects |

In DSA, `__lt__` is what lets you push custom objects into a heap.

## 3. Inheritance, composition, `super()`

```python
class Savings(Account):
    def __init__(self, owner, balance=0.0, rate=0.05):
        super().__init__(owner, balance)
        self.rate = rate
```

Prefer **composition** ("has-a") over deep inheritance trees. Use `abc.ABC` + `@abstractmethod`
when you want to define an interface; use `typing.Protocol` for duck-typed structural interfaces.

## 4. Static/class methods and properties

```python
@classmethod
def from_dict(cls, data): return cls(**data)    # alternative constructors

@staticmethod
def validate(x): ...

@property
def is_overdrawn(self) -> bool: return self.balance < 0
```

## 5. Encapsulation conventions

`_private` by convention, `__mangled` triggers name mangling. There is no real `private`;
Python trusts the caller. `__slots__` cuts memory when you create millions of objects (e.g. graph nodes).

## Checkpoints
- What breaks if you define `__eq__` but not `__hash__`?
- When do you need `@classmethod` instead of `@staticmethod`?
- Which dunder makes your class usable in a `heapq`?

## Practice
`python test_exercises.py`
