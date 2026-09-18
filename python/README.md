# Python Track: Zero to Development & DSA Ready

The DSA curriculum in [`topics/`](../topics) assumes you can already *write* Python.
This track is how you get there — from installing Python to writing clean, tested,
packaged code and the specific idioms that make DSA in Python fast.

Every lesson is the same shape:

```text
lessons/NN-topic/
├── notes.md            # the concepts, with the gotchas that actually bite
├── exercises.py        # stubs you implement
├── solutions.py        # reference implementation (read AFTER you try)
└── test_exercises.py   # the same tests grade either file
```

## How to use it

```bash
cd python
python3 --version            # need 3.10+

python run_tests.py          # grade YOUR work (exercises.py) - everything fails at first
python run_tests.py 03       # only lesson 03
python run_tests.py --solutions   # sanity-check the reference answers

cd lessons/03-collections
python test_exercises.py     # single lesson, verbose
```

Loop per lesson: **read `notes.md` → answer the checkpoint questions out loud → fill in
`exercises.py` until tests pass → only then diff your code against `solutions.py`.**
If your version is longer or slower, understand why before moving on.

## The lessons

| # | Lesson | You can do this afterwards |
|---:|---|---|
| 01 | [Setup, Syntax & The Mental Model](lessons/01-setup-and-syntax/notes.md) | Install Python, use venvs, write correct basic syntax, understand references |
| 02 | [Types, Numbers & Strings](lessons/02-types-numbers-strings/notes.md) | Integer/float semantics, string methods, slicing, formatting |
| 03 | [Lists, Tuples, Sets & Dicts](lessons/03-collections/notes.md) | Pick the right container and know its cost |
| 04 | [Control Flow & Comprehensions](lessons/04-control-flow/notes.md) | Idiomatic loops, comprehensions, `enumerate`/`zip`/`any`/`all` |
| 05 | [Functions, Scope & Arguments](lessons/05-functions/notes.md) | Argument kinds, closures, decorators, `lru_cache`, recursion limits |
| 06 | [Iterators & Generators](lessons/06-iterators-and-generators/notes.md) | Lazy pipelines, infinite streams, `itertools` |
| 07 | [Classes, Dunders & OOP](lessons/07-oop/notes.md) | Design types, operator overloading, `__lt__` for heaps |
| 08 | [Errors, Debugging & Testing](lessons/08-errors-and-testing/notes.md) | Exception design, context managers, pdb, `unittest` |
| 09 | [Files, JSON & The Standard Library](lessons/09-files-and-stdlib/notes.md) | `pathlib`, streaming I/O, JSON/CSV, regex, stdlib map |
| 10 | [Typing, Dataclasses & Clean Code](lessons/10-typing-and-clean-code/notes.md) | Type hints, `mypy`, dataclasses, PEP 8, project layout |
| 11 | [Modules, Virtualenvs, Packaging & Tooling](lessons/11-modules-packaging-tooling/notes.md) | Imports, `pyproject.toml`, `ruff`/`black`/`pytest`, CLIs, git hygiene |
| 12 | [Python Performance & Idioms for DSA](lessons/12-python-for-dsa/notes.md) | The contest/interview toolkit and cost table — the bridge into `topics/` |

Then build something: [`projects/`](projects/README.md), starting with the
[Contacts CLI](projects/contacts-cli/README.md), which is test-driven end to end.

## Suggested schedule

| Pace | Plan |
|---|---|
| **Fast (2 weeks)** | Lessons 1–6 in week 1, 7–12 in week 2, project 1 on the weekend |
| **Steady (4 weeks)** | 3 lessons/week + 1 project; start DSA topic 02 in week 3 in parallel |
| **Part-time (8 weeks)** | 1–2 lessons/week, every project, then the DSA path |

You are ready to leave this track when you can, from a blank file and without help:
write a tested module with a dataclass, a generator, a decorator and a CLI; explain the
cost of every operation you used; and reach for `Counter`/`deque`/`heapq`/`bisect` by reflex.

## Where to go next

1. [`docs/learning-path.md`](../docs/learning-path.md) — the full study roadmap.
2. [`topics/01-complexity-analysis`](../topics/01-complexity-analysis/README.md) — start the DSA curriculum.
3. [`templates/python_dsa_templates.py`](../templates/python_dsa_templates.py) — the algorithm templates you will now be able to read fluently.

## Free references

- [Official tutorial](https://docs.python.org/3/tutorial/) and [stdlib docs](https://docs.python.org/3/library/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/) (beginner, practical)
- [Fluent Python, 2nd ed.](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) (after lesson 07)
- [Real Python](https://realpython.com/), [PEP 8](https://peps.python.org/pep-0008/), [pytest docs](https://docs.pytest.org/)
