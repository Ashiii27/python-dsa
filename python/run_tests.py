"""Run every lesson test in the Python track.

    python run_tests.py                 # grade your work in exercises.py
    python run_tests.py --solutions     # verify the reference solutions
    python run_tests.py 03 07           # only lessons whose folder starts with 03/07
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    target = "exercises"
    if "--solutions" in argv:
        target = "solutions"
        argv = [a for a in argv if a != "--solutions"]

    root = Path(__file__).resolve().parent / "lessons"
    lessons = sorted(p for p in root.iterdir() if p.is_dir())
    if argv:
        lessons = [p for p in lessons if any(p.name.startswith(a) for a in argv)]

    env = {**os.environ, "PY_TRACK_TARGET": target}
    failures: list[str] = []
    for lesson in lessons:
        test = lesson / "test_exercises.py"
        if not test.exists():
            continue
        print(f"\n==> {lesson.name} [{target}]", flush=True)
        result = subprocess.run([sys.executable, test.name], cwd=lesson, env=env, check=False)
        if result.returncode != 0:
            failures.append(lesson.name)

    print(f"\nLessons run: {len(lessons)} | failing: {len(failures)}")
    for name in failures:
        print(f"  - {name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
