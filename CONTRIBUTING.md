# Contributing to This DSA Masterclass

Use this guide whenever you add a new topic, problem, or implementation.

---

## The website

The course site at `https://ashiii27.github.io/python-dsa/` is generated from this
repository's markdown and Python files — the repo is the single source of truth.
To improve the website, improve the content here (lessons in `python/`, topics
and problems in `topics/`, guides in `docs/`, practice lists in `practice/`).
The site shell lives in `website/`; run it locally with
`cd website && npm install && npm start` (see [`website/README.md`](website/README.md)).

---

## Topic guide standard

Every topic should include:

1. **What you must learn** - the concepts and vocabulary.
2. **Core patterns and approaches** - how to recognize and solve problems in the topic.
3. **Python notes** - implementation details and common mistakes.
4. **Canonical template** - a short reference implementation.
5. **Top interview questions** - problem, level, approach, time, and space.
6. **Mastery checklist** - how to know when the topic is interview-ready.

Every topic also has a `study-guide.md`. Keep it topic-specific and include:

- a mental model and concise concept documentation
- pattern-recognition signals rather than pattern-name memorization
- at least one traceable worked example
- practical tricks, common mistakes, and implementation drills
- an active-recall checkpoint
- additional practice from at least two platforms when good problems are available

Verify every external problem URL before adding it and label platform difficulty as approximate.

---

## Problem solution standard

When adding a solved problem, use `templates/problem-template.md` and include:

- restatement
- constraints
- brute force
- optimized approach
- invariant/proof idea
- Python solution
- complexity
- edge cases
- automated tests using the Python standard library
- a canonical external problem link (when available)
- mistakes and redo date

Place each solution under `topics/<topic>/problems/<problem-slug>/`:

```text
problem-slug/
├── README.md          # worked explanation, proof, complexity, diagram
├── solution.py        # dependency-free implementation
└── test_solution.py   # examples plus boundary/regression cases
```

Tests must run from a fresh clone without third-party packages. Topic-level runners may aggregate standalone problem tests.

---

## Python code standard

- Prefer clear names over clever one-liners.
- Use standard library tools appropriately: `deque`, `heapq`, `Counter`, `defaultdict`, `bisect`.
- Avoid hidden quadratic behavior from slicing, string concatenation, or `list.pop(0)`.
- Add short docstrings to reusable templates.
- Keep templates dependency-free unless there is a strong reason.

---

## Code snippets inside the notes

Every topic's `study-guide.md` ends with two code-heavy sections:

1. **Python implementation (build it from scratch)** — the data structure or
   technique implemented from first principles, with a step-by-step "How it
   works" walkthrough.
2. **Solved examples** — two or three worked problems: statement, approach,
   runnable code, real output, and complexity.

Standards for those snippets:

- **Every ```python block must run on its own.** Copy-paste into a file and it
  executes; no hidden setup, no `...`, no undefined names.
- Put the demo under `if __name__ == "__main__":` and print something.
- Show the real output underneath. Write `<<output>>` inside a ```text fence
  and let the tooling fill it in:

  ````text
  ```python
  print("hi")
  ```

  Output:

  ```text
  <<output>>
  ```
  ````

- Keep output deterministic: no wall-clock timings, no unseeded randomness, no
  printing of sets or dicts whose order depends on string hashing.
- A deliberately partial fragment must start with the marker `# skip-check`.
- Snippets must not depend on interpreter state they changed earlier (restore
  `sys.setrecursionlimit` if you raise it).

### Tooling

```bash
python3 tools/check_snippets.py            # verify every snippet executes
python3 tools/check_snippets.py --fill     # write real output into <<output>> blocks
python3 tools/check_snippets.py --refresh  # re-run and overwrite existing outputs
python3 tools/check_snippets.py --all      # include python/ lessons as well
python3 tools/check_snippets.py topics/03-linked-lists/study-guide.md   # one file
```

The same command runs in CI, so a broken snippet fails the build.

---

## Practice standard

For each topic:

1. Solve easy problems until the pattern feels automatic.
2. Solve medium problems under a timer.
3. Redo missed problems after spaced intervals.
4. Add hard problems only after the core pattern is solid.
5. Update `practice/study-tracker.md` with mistake labels.
