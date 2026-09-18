# Python DSA Masterclass

A complete, interview-focused Data Structures and Algorithms learning repository using **Python**.

This repo is designed to take you from the absolute basics to the level expected in top-tier software engineering interviews: strong fundamentals, pattern recognition, clean Python implementations, complexity analysis, and curated high-value problems with approaches.

> Goal: do not memorize solutions. Learn the patterns, derive the approach, prove correctness, code cleanly, and test edge cases.

---

## New to Python? Start here

If you cannot yet write Python comfortably, do the **[Python Track](python/README.md)** first:
12 hands-on lessons (syntax → collections → functions → OOP → testing → packaging → DSA idioms),
each with notes, stub exercises, reference solutions and tests, plus capstone projects.

```bash
cd python && python run_tests.py      # grade your exercises
```

It takes you from installation to "can build and ship a tested Python project", and its final
lesson hands you straight into the DSA curriculum below.

---

## How to use this repo

Use every topic in three passes:

1. **Understand**: read the topic notes, learn the core idea, and trace the examples by hand.
2. **Implement**: code the templates without looking, then compare with [`templates/python_dsa_templates.py`](templates/python_dsa_templates.py).
3. **Study a worked example**: start with the complete [Arrays & Strings solution pack](topics/02-arrays-and-strings/problems/README.md), including proofs, diagrams, code, and tests.
4. **Interview drill**: solve the problem ladder. Every question title links to its canonical prompt. For every problem, write down:
   - brute force idea
   - optimized pattern
   - complexity
   - edge cases
   - why the solution is correct

Recommended daily loop:

```text
15 min     revise previous notes / flashcards
45-75 min  learn one concept or template deeply
60-120 min solve 2-4 problems from that topic
15 min     write post-solve notes and mistakes
```

---

## Repository map

```text
python-dsa/
├── README.md
├── CONTRIBUTING.md
├── python/                        # learn Python itself: lessons + projects
│   ├── README.md
│   ├── run_tests.py
│   ├── lessons/01..12/            # notes.md, exercises.py, solutions.py, tests
│   └── projects/                  # capstone builds (contacts CLI, etc.)
├── docs/
│   ├── learning-path.md
│   ├── problem-solving-framework.md
│   ├── patterns-cheatsheet.md
│   ├── complexity-and-python.md
│   ├── interview-playbook.md
│   ├── revision-checklists.md
│   ├── revision-flashcards.md
│   ├── visual-guides.md
│   └── resources.md
├── topics/
│   ├── 00-python-foundations/
│   │   └── problems/README.md
│   ├── 01-complexity-analysis/
│   │   └── problems/README.md
│   ├── 02-arrays-and-strings/
│   │   ├── study-guide.md        # concepts, examples, tricks, patterns
│   │   └── problems/             # worked notes, solutions, and tests
│   ├── ...                       # every topic has its own study guide
│   └── 23-design-data-structures/
├── practice/
│   ├── top-interview-questions.md
│   ├── extended-practice.md      # 96 additional cross-platform problems
│   ├── study-tracker.md
│   └── company-style-sheets.md
└── templates/
    ├── python_dsa_templates.py
    └── problem-template.md
```

---

## Curriculum: basics to advanced

| Phase | Topics | Target skill |
|---|---|---|
| -1. Learn Python | [Python Track (12 lessons + projects)](python/README.md) | Write, test, and package real Python from scratch |
| 0. Setup + Python | [Python Foundations](topics/00-python-foundations/README.md) | Write clean Python and use built-in collections correctly |
| 1. Foundations | [Complexity Analysis](topics/01-complexity-analysis/README.md) | Predict time/space and choose viable algorithms by constraints |
| 2. Linear structures | [Arrays & Strings](topics/02-arrays-and-strings/README.md), [Linked Lists](topics/03-linked-lists/README.md), [Stacks & Queues](topics/04-stacks-and-queues/README.md), [Hashing](topics/05-hashing/README.md) | Master the most common interview patterns |
| 3. Recursion + search | [Recursion & Backtracking](topics/06-recursion-and-backtracking/README.md), [Searching & Sorting](topics/07-searching-and-sorting/README.md), [Binary Search](topics/08-binary-search/README.md) | Build recursive solutions and reason about sorted spaces |
| 4. Trees + heaps | [Trees](topics/09-trees-and-binary-trees/README.md), [BSTs](topics/10-binary-search-trees/README.md), [Heaps](topics/11-heaps-and-priority-queues/README.md) | Solve hierarchical and streaming/top-k problems |
| 5. Graphs + DP | [Graphs](topics/12-graphs/README.md), [Dynamic Programming](topics/13-dynamic-programming/README.md), [Greedy](topics/14-greedy/README.md) | Handle the core hard-interview topics |
| 6. Advanced DSA | [Tries](topics/15-tries/README.md), [Intervals & Line Sweep](topics/16-intervals-and-line-sweep/README.md), [Union Find](topics/17-union-find/README.md), [Segment Tree & Fenwick](topics/18-segment-tree-and-fenwick/README.md), [Bit Manipulation](topics/19-bit-manipulation/README.md), [Math](topics/20-math-and-number-theory/README.md), [Advanced Strings](topics/21-advanced-strings/README.md), [Advanced Graphs](topics/22-advanced-graphs/README.md), [Design Data Structures](topics/23-design-data-structures/README.md) | Reach top-tier company hard-question readiness |

---

## Topic study guides

Every curriculum topic now includes a dedicated `study-guide.md` with:

- a topic-specific mental model and learning objectives
- core concepts and pattern-recognition signals
- a worked example
- interview tricks and common mistakes
- implementation drills and active-recall checkpoints
- an additional cross-platform practice ladder

Open any topic from the curriculum table above and follow its **Complete study guide** link.

---

## The patterns that matter most

If you become excellent at these, most interview problems become recognizable:

- Two pointers
- Sliding window
- Prefix sums / difference arrays
- Hash maps and frequency counting
- Sorting + custom keys
- Binary search on index and on answer
- Fast/slow pointers
- Monotonic stack / monotonic queue
- Heap / priority queue
- DFS / BFS
- Topological sort
- Union Find
- Backtracking
- Dynamic programming states and transitions
- Greedy exchange arguments
- Trie prefix traversal
- Segment tree / Fenwick tree
- Dijkstra / MST / SCC / bridges
- Bitmasking and bitmask DP
- String matching: KMP, rolling hash, Z algorithm
- Design with combined data structures

See the full [Patterns Cheatsheet](docs/patterns-cheatsheet.md).

---

## Problem-solving framework

For every problem, train this exact flow:

1. **Clarify** inputs, outputs, constraints, duplicates, order, mutability.
2. **Write brute force** in words. This prevents blanking out.
3. **Find the bottleneck**: repeated scans, repeated recomputation, search over choices, sorted property, graph relationship, overlapping subproblems.
4. **Map to a pattern** using the [patterns cheatsheet](docs/patterns-cheatsheet.md).
5. **Prove the invariant**: what stays true after every step?
6. **Code small, test early** with edge cases.
7. **Analyze complexity** honestly, including Python-specific costs.

Detailed version: [Problem Solving Framework](docs/problem-solving-framework.md).

---

## High-value practice lists

- [Top interview questions by topic](practice/top-interview-questions.md) — all 191 entries include prompt links
- [Extended cross-platform practice](practice/extended-practice.md) — 96 additional LeetCode, Codeforces, CSES, HackerRank, and SPOJ problems
- [Fully worked Arrays & Strings problems](topics/02-arrays-and-strings/problems/README.md) — 11 solutions with standard-library tests
- [Visual pattern guide](docs/visual-guides.md) — Mermaid diagrams for core interview patterns
- [Revision flashcards](docs/revision-flashcards.md) — collapsible active-recall cards
- [Company-style preparation sheets](practice/company-style-sheets.md)
- [Study tracker](practice/study-tracker.md)
- [Problem write-up template](templates/problem-template.md)
- [External resources and references](docs/resources.md)

---

## Python implementation templates

The file [`templates/python_dsa_templates.py`](templates/python_dsa_templates.py) contains reusable reference implementations for:

- binary search variants
- sliding window
- prefix sums
- linked list helpers
- monotonic stack/queue
- heaps
- tree traversal
- BFS/DFS/topological sort
- Dijkstra and Bellman-Ford
- Union Find
- Trie
- Fenwick tree and segment tree
- KMP and Z algorithm
- DP classics
- LRU cache, TimeMap, RandomizedSet

Do not copy templates blindly in interviews. Use them to internalize the shape of solutions.

### Run the worked-solution tests

No third-party dependency is required:

```bash
python topics/02-arrays-and-strings/problems/run_tests.py
```

---

## Readiness standards

You are interview-ready for a topic when you can:

- explain the data structure and when to use it
- implement its core operations from memory
- solve easy problems in under 10 minutes
- solve medium problems in 20-35 minutes
- make meaningful progress on hard problems in 45 minutes
- explain time/space complexity without guessing
- name at least three common edge cases
- compare the pattern against nearby alternatives

---

## Suggested first milestone

Start here:

1. [Python Foundations](topics/00-python-foundations/README.md)
2. [Complexity Analysis](topics/01-complexity-analysis/README.md)
3. [Arrays & Strings](topics/02-arrays-and-strings/README.md)
4. [Hashing](topics/05-hashing/README.md)
5. [Stacks & Queues](topics/04-stacks-and-queues/README.md)

Then solve the first 40 questions in [Top interview questions](practice/top-interview-questions.md).
