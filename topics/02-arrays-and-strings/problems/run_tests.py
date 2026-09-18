"""Run every standalone unittest module in this topic."""

from pathlib import Path
import subprocess
import sys


def main() -> int:
    root = Path(__file__).parent
    tests = sorted(root.glob("*/test_solution.py"))
    failures = 0
    for test in tests:
        print(f"\n==> {test.parent.name}", flush=True)
        result = subprocess.run([sys.executable, test.name], cwd=test.parent, check=False)
        failures += result.returncode != 0
    print(f"\nRan {len(tests)} problem test modules; failures: {failures}")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
