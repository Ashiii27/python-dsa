# Python Foundations for DSA

**Level:** Beginner

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Build the Python fluency needed to solve DSA problems quickly and safely.

---

## What you must learn

- Lists, tuples, strings, dictionaries, and sets
- Counter, defaultdict, deque, OrderedDict
- heapq, bisect, itertools, math, functools
- Mutability, references, shallow copies, and slicing costs
- Function decomposition, helper functions, and type hints

---

## Core patterns and approaches

- Use dict/set for average O(1) lookup
- Use deque for queues and sliding windows
- Use heapq for priority queues; push negative values for max-heap behavior
- Use list accumulation plus join for strings
- Use tuple sort keys for multi-key ordering

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
from collections import Counter, defaultdict, deque
import heapq, bisect

nums = [3, 1, 2, 1]
freq = Counter(nums)
positions = defaultdict(list)
for i, x in enumerate(nums):
    positions[x].append(i)

q = deque([0]); q.append(1); left = q.popleft()
heap = []; heapq.heappush(heap, (5, 'task')); priority, task = heapq.heappop(heap)
idx = bisect.bisect_left([1, 3, 5], 3)
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Build a Frequency Counter](https://docs.python.org/3/library/collections.html#collections.Counter) | Easy | Use a dict or Counter and increment per item. | O(n) | O(k) |
| [Group Items by Key](https://docs.python.org/3/library/collections.html#collections.defaultdict) | Easy | Use defaultdict(list) and append into each group. | O(n) | O(n) |
| [Implement Queue with deque](https://docs.python.org/3/library/collections.html#collections.deque) | Easy | Use append and popleft for true queue operations. | O(1) per op | O(n) |
| [Sort Records by Multiple Fields](https://docs.python.org/3/howto/sorting.html) | Easy | Use tuple key like (age, -score). | O(n log n) | O(n) |
| [Top K Values with Heap](https://docs.python.org/3/library/heapq.html) | Medium | Maintain a min-heap of size k. | O(n log k) | O(k) |
| [Parse and Count Log Events](https://docs.python.org/3/library/stdtypes.html#str.split) | Medium | Split lines, normalize fields, aggregate with maps. | O(total chars) | O(unique keys) |

---

## Mastery checklist

- [ ] I can explain the main idea without looking at notes.
- [ ] I can implement the canonical template from memory.
- [ ] I can solve the easy problems in under 10 minutes each.
- [ ] I can solve most medium problems in 20-35 minutes.
- [ ] I can explain brute force, optimized approach, proof idea, and complexity.
- [ ] I can identify edge cases before coding.

---

## Next steps

1. Read the related sections in [`docs/patterns-cheatsheet.md`](../../docs/patterns-cheatsheet.md).
2. Implement the relevant template from [`templates/python_dsa_templates.py`](../../templates/python_dsa_templates.py) without looking.
3. Add solved problems and mistakes to [`practice/study-tracker.md`](../../practice/study-tracker.md).
4. Browse the topic [`problems/`](problems/README.md) index for prompt links and worked solutions.
