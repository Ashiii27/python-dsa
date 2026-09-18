"""Shared test helper for the Python track.

Every lesson has two modules with the same function names:

* ``exercises.py``  - your stubs to fill in
* ``solutions.py``  - the reference implementation

The test file in each lesson imports the module under test through this
loader, so the same tests grade either one:

    python test_exercises.py             # grades exercises.py (default)
    PY_TRACK_TARGET=solutions python test_exercises.py
"""

from __future__ import annotations

import importlib.util
import os
import sys
import types
from pathlib import Path


def load(lesson_file: str) -> types.ModuleType:
    """Load the module under test that sits next to ``lesson_file``."""
    target = os.environ.get("PY_TRACK_TARGET", "exercises")
    path = Path(lesson_file).resolve().parent / f"{target}.py"
    if not path.exists():
        raise FileNotFoundError(f"no module {target}.py next to {lesson_file}")
    spec = importlib.util.spec_from_file_location(f"pytrack_{path.parent.name}_{target}", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


TODO = "This exercise is not implemented yet. Open exercises.py and finish it."
