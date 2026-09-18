# Python Foundations — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Build a Frequency Counter](https://docs.python.org/3/library/collections.html#collections.Counter) | Easy | Use a dict or Counter and increment per item. | O(n) | O(k) |
| [Group Items by Key](https://docs.python.org/3/library/collections.html#collections.defaultdict) | Easy | Use defaultdict(list) and append into each group. | O(n) | O(n) |
| [Implement Queue with deque](https://docs.python.org/3/library/collections.html#collections.deque) | Easy | Use append and popleft for true queue operations. | O(1) per op | O(n) |
| [Sort Records by Multiple Fields](https://docs.python.org/3/howto/sorting.html) | Easy | Use tuple key like (age, -score). | O(n log n) | O(n) |
| [Top K Values with Heap](https://docs.python.org/3/library/heapq.html) | Medium | Maintain a min-heap of size k. | O(n log k) | O(k) |
| [Parse and Count Log Events](https://docs.python.org/3/library/stdtypes.html#str.split) | Medium | Split lines, normalize fields, aggregate with maps. | O(total chars) | O(unique keys) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
