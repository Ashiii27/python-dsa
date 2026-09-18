# Lesson 11 — Modules, Virtualenvs, Packaging & Tooling

**Goal:** the "development" half of the track — everything around the code that makes it a real project.

## 1. Modules and packages

- A **module** is a `.py` file. A **package** is a directory (with `__init__.py` for classic packages).
- `import pkg.mod`, `from pkg.mod import thing`, `import numpy as np`.
- Use **absolute imports** in applications; relative (`from .core import x`) only inside a package.
- `sys.path` decides where imports come from; run code as `python -m package.module` to keep
  the project root on the path instead of fighting with relative paths.
- Avoid circular imports by moving shared code into a third module.

## 2. Environments and dependencies

```bash
python -m venv .venv && source .venv/bin/activate
pip install requests
pip freeze > requirements.txt          # exact pins for reproducibility
pip install -r requirements.txt
deactivate
```
Modern alternatives: `uv`, `poetry`, `pipx` (for CLI tools). The principle never changes:
one isolated environment per project, dependencies written down in a file that is committed.

## 3. `pyproject.toml` — the single config file

```toml
[project]
name = "mytool"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["requests>=2.31"]

[project.scripts]
mytool = "mytool.cli:main"     # creates a real command on install

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

`pip install -e .` installs your project in editable mode so imports work everywhere.

## 4. Tooling worth setting up once

| Tool | Purpose |
|---|---|
| `ruff` | lint + autofix + import sorting (fast, replaces flake8/isort) |
| `black` or `ruff format` | deterministic formatting |
| `mypy` / `pyright` | static type checking |
| `pytest` | test runner (`pytest -q`, `-k name`, `--cov`) |
| `pre-commit` | run all of the above on every commit |
| `timeit` / `cProfile` | measure before optimising |

## 5. A CLI in 15 lines

```python
import argparse

def main() -> int:
    parser = argparse.ArgumentParser(description="Count words")
    parser.add_argument("path")
    parser.add_argument("-n", "--top", type=int, default=5)
    args = parser.parse_args()
    ...
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

## 6. Git hygiene for Python projects

`.gitignore` should contain `__pycache__/`, `*.pyc`, `.venv/`, `.pytest_cache/`, `.mypy_cache/`, `dist/`, `build/`, `.env`.
Never commit secrets; read them from the environment (`os.environ["API_KEY"]`).

## Checkpoints
- What does `python -m package.module` do that `python package/module.py` doesn't?
- Why commit `requirements.txt` (or a lockfile) rather than the `.venv`?
- What is editable install (`pip install -e .`) for?

## Practice
`python test_exercises.py` — here you implement a small importable module + CLI-style entry point.
