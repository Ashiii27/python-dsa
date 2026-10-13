#!/usr/bin/env python3
"""Verify (and optionally fill in) the Python snippets inside the course notes.

The markdown files in this repository are the single source of truth for the
website, so every ```python block has to be real, runnable code — not a
fragment that fails when a reader copies it. This script proves that.

Usage
-----
    python3 tools/check_snippets.py                 # check every snippet
    python3 tools/check_snippets.py --fill          # write real output into <<output>> blocks
    python3 tools/check_snippets.py --refresh       # re-run and overwrite existing outputs
    python3 tools/check_snippets.py --all           # include python/ lessons too
    python3 tools/check_snippets.py topics/03-linked-lists/study-guide.md

How snippets are found
----------------------
Every fenced block opened with ```python is executed on its own in a fresh
namespace. A block is skipped when its first line is the marker
``# skip-check`` (use it for deliberately partial fragments).

How output blocks are filled
----------------------------
When a python block is immediately followed by

    Output:

    ```text
    <<output>>
    ```

``--fill`` runs the snippet and replaces ``<<output>>`` with its real stdout.
Outputs are therefore generated, never hand-written, so they cannot drift.
"""

from __future__ import annotations

import io
import re
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# A code block body: anything that does not contain a fence on its own line.
BODY = r"(?:(?!^```$).)*?"
PY_BLOCK_RE = re.compile(rf"^```python\n({BODY})^```", re.S | re.M)
ANY_OUTPUT_RE = re.compile(
    rf"(?P<head>^```python\n(?P<code>{BODY})^```\n(?:\s*Output:?\s*)?)"
    r"(?P<out>^```text\n(.*?)^```)",
    re.S | re.M,
)
OUTPUT_BLOCK_RE = re.compile(
    rf"(?P<head>^```python\n(?P<code>{BODY})^```\n(?:\s*Output:?\s*)?)"
    r"(?P<out>^```text\n<<output>>\n^```)",
    re.S | re.M,
)

DEFAULT_GLOBS = ["topics/**/*.md", "docs/*.md", "README.md"]
EXTRA_GLOBS = ["python/**/*.md", "CONTRIBUTING.md", "templates/*.md"]


def iter_markdown(paths: list[str], include_all: bool) -> list[Path]:
    if paths:
        found: list[Path] = []
        for raw in paths:
            p = Path(raw).expanduser()
            p = p if p.is_absolute() else (Path.cwd() / p)
            if p.is_file():
                found.append(p.resolve())
            elif p.is_dir():
                found.extend(sorted(p.rglob("*.md")))
            else:
                found.extend(sorted(REPO.glob(raw)))
        return sorted(set(found))
    globs = DEFAULT_GLOBS + (EXTRA_GLOBS if include_all else [])
    out: list[Path] = []
    for pattern in globs:
        out.extend(sorted(REPO.glob(pattern)))
    return sorted(set(out))


def blocks(md: str) -> list[str]:
    """Return executable python blocks (partial fragments excluded)."""
    result = []
    for m in PY_BLOCK_RE.finditer(md):
        code = m.group(1)
        first = next((ln for ln in code.splitlines() if ln.strip()), "")
        if first.strip() == "# skip-check":
            continue
        result.append(code)
    return result


def run_block(code: str) -> tuple[bool, str, str]:
    """Execute one snippet; return (ok, stdout, error)."""
    buf = io.StringIO()
    # Snippets may change interpreter state (e.g. sys.setrecursionlimit); undo it
    # so one snippet cannot change another snippet's result.
    recursion_limit = sys.getrecursionlimit()
    try:
        with redirect_stdout(buf):
            # __name__ = "__main__" so snippets with a main-guard run their demo.
            exec(compile(code, "<snippet>", "exec"), {"__name__": "__main__"})  # noqa: S102
        return True, buf.getvalue(), ""
    except Exception:
        return False, buf.getvalue(), traceback.format_exc(limit=3)
    finally:
        sys.setrecursionlimit(recursion_limit)


def check(paths: list[str], include_all: bool) -> int:
    failures = 0
    total = 0
    files = iter_markdown(paths, include_all)
    for path in files:
        md = path.read_text(encoding="utf-8")
        file_blocks = blocks(md)
        if not file_blocks:
            continue
        rel = path.relative_to(REPO).as_posix()
        for i, code in enumerate(file_blocks, 1):
            total += 1
            ok, _out, err = run_block(code)
            if not ok:
                failures += 1
                last = err.strip().splitlines()[-1]
                print(f"FAIL {rel} [block {i}]: {last}")
    verb = "snippet" if total == 1 else "snippets"
    print(f"\n{total - failures}/{total} {verb} executed successfully "
          f"across {len(files)} file(s).")
    if failures:
        print(f"{failures} failing snippet(s).")
    return 1 if failures else 0


def refresh(paths: list[str], include_all: bool) -> int:
    """Re-run every snippet and overwrite the ```text block that follows it."""
    refreshed = failures = 0
    for path in iter_markdown(paths, include_all):
        md = path.read_text(encoding="utf-8")
        rel = path.relative_to(REPO).as_posix()

        def replace(match: re.Match) -> str:
            nonlocal refreshed, failures
            ok, out, err = run_block(match.group("code"))
            if not ok:
                failures += 1
                print(f"FAIL {rel}: {err.strip().splitlines()[-1]}")
                return match.group(0)
            refreshed += 1
            body = out.rstrip("\n") or "(no output)"
            return f"{match.group('head')}```text\n{body}\n```"

        new_md = ANY_OUTPUT_RE.sub(replace, md)
        if new_md != md:
            path.write_text(new_md, encoding="utf-8")
    print(f"\nRefreshed {refreshed} output block(s).")
    return 1 if failures else 0


def fill(paths: list[str], include_all: bool) -> int:
    filled = 0
    failures = 0
    for path in iter_markdown(paths, include_all):
        md = path.read_text(encoding="utf-8")
        if "<<output>>" not in md:
            continue
        rel = path.relative_to(REPO).as_posix()

        def replace(match: re.Match) -> str:
            nonlocal filled, failures
            ok, out, err = run_block(match.group("code"))
            if not ok:
                failures += 1
                last = err.strip().splitlines()[-1]
                print(f"FAIL {rel}: {last}")
                return match.group(0)
            filled += 1
            body = out.rstrip("\n")
            if not body:
                body = "(no output)"
            return f"{match.group('head')}```text\n{body}\n```"

        new_md = OUTPUT_BLOCK_RE.sub(replace, md)
        if new_md != md:
            path.write_text(new_md, encoding="utf-8")
    print(f"\nFilled {filled} output block(s).")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:]]
    fill_mode = "--fill" in args
    include_all = "--all" in args
    paths = [a for a in args if not a.startswith("--")]
    if "--refresh" in args:
        return refresh(paths, include_all)
    if fill_mode:
        return fill(paths, include_all)
    return check(paths, include_all)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
