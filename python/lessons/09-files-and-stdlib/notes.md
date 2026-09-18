# Lesson 09 — Files, JSON & The Standard Library

## 1. Paths with `pathlib` (stop using string concatenation)

```python
from pathlib import Path
p = Path("data") / "users.json"
p.exists(); p.is_file(); p.suffix; p.stem; p.parent
p.parent.mkdir(parents=True, exist_ok=True)
p.read_text(encoding="utf-8"); p.write_text(s, encoding="utf-8")
sorted(Path(".").glob("**/*.py"))
```

## 2. Reading and writing

```python
with open(path, "r", encoding="utf-8") as fh:
    for line in fh:              # streams; never .read() a huge file
        process(line.rstrip("\n"))

with open(path, "w", encoding="utf-8") as fh:
    fh.write("line\n")
    fh.writelines(f"{x}\n" for x in rows)
```
Modes: `r` read, `w` truncate, `a` append, `x` create-only, `b` binary, `+` read/write.
Always pass `encoding="utf-8"` — platform defaults differ.

## 3. Structured formats

```python
import json
json.loads(s); json.dumps(obj, indent=2, sort_keys=True)
json.load(fh); json.dump(obj, fh)

import csv
reader = csv.DictReader(fh)          # rows as dicts
writer = csv.DictWriter(fh, fieldnames=[...]); writer.writeheader()
```
JSON keys are always strings; tuples become lists on round-trip.

## 4. Standard library map (know these exist)

| Need | Module |
|---|---|
| CLI args | `argparse` |
| Dates/times | `datetime`, `zoneinfo`, `time` |
| Randomness | `random` (and `secrets` for tokens) |
| Math | `math`, `statistics`, `decimal`, `fractions` |
| Regex | `re` |
| Containers | `collections`, `heapq`, `bisect`, `array` |
| Functional | `itertools`, `functools`, `operator` |
| FS/OS | `pathlib`, `os`, `shutil`, `tempfile`, `glob` |
| Serialisation | `json`, `csv`, `pickle`, `sqlite3` |
| Concurrency | `threading`, `multiprocessing`, `concurrent.futures`, `asyncio` |
| Quality | `unittest`, `logging`, `typing`, `dataclasses`, `timeit`, `cProfile` |

## 5. Regex in 60 seconds

```python
import re
re.search(r"\d+", s)        # first match object or None
re.findall(r"\w+", s)       # list of strings
re.sub(r"\s+", " ", s)      # collapse whitespace
re.compile(...)             # reuse in loops
```
`\d \w \s`, `+ * ? {m,n}`, `^ $`, `( )` groups, `(?: )` non-capturing, `re.I` flag.

## Checkpoints
- Why `with open(...)` rather than `open()` + `close()`?
- How do you stream a 10 GB log file without exhausting memory?
- Which module gives you binary search over a sorted list?

## Practice
`python test_exercises.py`
