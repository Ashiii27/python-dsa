# Python Foundations: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Treat Python collections as data structures with explicit cost models. Fluency means choosing the right built-in, understanding mutation and references, and avoiding operations that hide linear work.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | `list`: dynamic array; O(1) amortized append and O(n) front insertion/removal. |
| 2 | `dict` / `set`: average O(1) membership; keys must be hashable. |
| 3 | `deque`: O(1) operations at both ends; preferred for queues and BFS. |
| 4 | `Counter`, `defaultdict`, `heapq`, and `bisect`: standard tools that remove boilerplate. |
| 5 | Sorting is stable; tuple keys express deterministic multi-field ordering. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Need counts or grouping | `Counter` or `defaultdict(list)` |
| FIFO processing | `collections.deque` |
| Repeated smallest/largest item | `heapq` |
| Search in sorted data | `bisect_left` / `bisect_right` |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

```python
from collections import Counter

words = ["tea", "eat", "tea", "tan"]
frequency = Counter(words)
# Counter({'tea': 2, 'eat': 1, 'tan': 1})
most_common = frequency.most_common(1)  # [('tea', 2)]
```
The number of dictionary entries is the number of distinct words, not the total input size.

## Tricks and interview notes

- Accumulate strings in a list and call `"".join(parts)` instead of repeated concatenation.
- Use `enumerate`, `zip`, and tuple unpacking to make index relationships explicit.
- Copy nested data intentionally: `matrix[:]` is shallow; `[row[:] for row in matrix]` copies rows.
- Remember that `heapq` is a min-heap; store negative priorities only when a max-heap is truly needed.

## Common mistakes

- **Watch for:** Using `list.pop(0)` as a queue.
- **Watch for:** Mutating a list or dictionary while iterating over it.
- **Watch for:** Using a mutable object as a default argument.
- **Watch for:** Assuming slices are O(1); they copy and cost O(k).

## Implementation drills

1. Implement a frequency counter without `Counter`.
2. Group records with `defaultdict`.
3. Maintain top k values with a size-k heap.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Python Lists](https://www.hackerrank.com/challenges/python-lists/problem) | HackerRank | Easy |
| [Company Logo](https://www.hackerrank.com/challenges/most-commons/problem) | HackerRank | Medium |
| [Word Order](https://www.hackerrank.com/challenges/word-order/problem) | HackerRank | Medium |
| [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem) | HackerRank | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Explain  without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
