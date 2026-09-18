# Lesson 01 — Setup, Syntax & The Mental Model

**Goal:** get a working Python, understand how a Python program actually runs, and write correct basic syntax without guessing.

## 1. Install and verify

```bash
python3 --version          # 3.10+ recommended (match/case, better errors)
python3 -m venv .venv      # one isolated environment per project
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -U pip
```

Never `pip install` into the system Python. A virtualenv is just a folder with its own `site-packages`; delete it and nothing breaks.

## 2. How Python runs your code

Source `.py` → compiled to bytecode (`__pycache__/*.pyc`) → executed by the CPython VM.
Consequences you will feel every day:

- Everything is an **object**, including functions, classes and modules.
- Names are **references**, not boxes. `b = a` copies the reference, not the value.
- Types are checked at **runtime**, not compile time — so tests matter more than in Java/C++.

## 3. Syntax essentials

```python
x = 10                  # no declarations, no semicolons
if x > 5:               # blocks are indentation (4 spaces, never tabs)
    print("big")
elif x == 5:
    print("five")
else:
    print("small")

name = "Ada"
print(f"{name} has {len(name)} letters")   # f-strings: the only formatting you need
```

- Comments `#`, docstrings `"""..."""` as the first statement of a module/function/class.
- Truthiness: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False` are falsy. Everything else is truthy.
- `==` compares values, `is` compares identity. Use `is` only with `None`, `True`, `False`.

## 4. The script/module boundary

```python
def main() -> None:
    ...

if __name__ == "__main__":
    main()
```

Code at module top level runs on **import**. Put side effects behind the `__main__` guard so the file can be both a script and an importable module (all lesson solutions do this).

## 5. Input, output, and the REPL loop

```python
python            # REPL: fastest way to test an idea
python -i file.py # run then drop into REPL with the state loaded
help(str.split); dir(list)
```

## Checkpoints

- Why is `if x is 5:` a bug even when it seems to work?  *(small-int caching, not semantics)*
- What does `b = a` do when `a` is a list, and what happens after `b.append(1)`?
- Why do we use `if __name__ == "__main__":`?

## Practice

Open `exercises.py`, implement the stubs, then run:

```bash
python test_exercises.py
```
