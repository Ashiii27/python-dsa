# Contributing to This DSA Masterclass

Use this guide whenever you add a new topic, problem, or implementation.

---

## Topic guide standard

Every topic should include:

1. **What you must learn** - the concepts and vocabulary.
2. **Core patterns and approaches** - how to recognize and solve problems in the topic.
3. **Python notes** - implementation details and common mistakes.
4. **Canonical template** - a short reference implementation.
5. **Top interview questions** - problem, level, approach, time, and space.
6. **Mastery checklist** - how to know when the topic is interview-ready.

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

## Practice standard

For each topic:

1. Solve easy problems until the pattern feels automatic.
2. Solve medium problems under a timer.
3. Redo missed problems after spaced intervals.
4. Add hard problems only after the core pattern is solid.
5. Update `practice/study-tracker.md` with mistake labels.
