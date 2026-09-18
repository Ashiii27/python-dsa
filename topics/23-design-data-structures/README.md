# Design Data Structures

**Level:** Advanced

> **Deep dive:** [Complete study guide](study-guide.md) — documentation, worked example, pattern signals, tricks, pitfalls, drills, and extra practice.

Combine multiple data structures to satisfy strict operation complexity requirements.

---

## What you must learn

- Operation contracts
- Hash map plus list
- Hash map plus doubly linked list
- Heap plus lazy deletion
- Ordered buckets
- Timestamped values
- Amortized O(1) design

---

## Core patterns and approaches

- Start by writing required complexities per operation
- Combine structures so one gives lookup and another gives ordering
- Keep bidirectional references/indexes synchronized
- For deletion from array in O(1), swap with last and update index
- For caches, use map for lookup and linked order for recency/frequency

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()
    def get(self, key):
        if key not in self.data: return -1
        self.data.move_to_end(key)
        return self.data[key]
    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Hash map plus doubly linked list or OrderedDict. | O(1) | O(capacity) |
| [LFU Cache](https://leetcode.com/problems/lfu-cache/) | Hard | Map key->node plus frequency buckets ordered by recency. | O(1) | O(capacity) |
| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | Array plus map value to index; swap-delete. | O(1) avg | O(n) |
| [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | Map key to sorted timestamp-value list; binary search get. | O(log n) get | O(n) |
| [Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | User follow graph plus heap merge of recent tweets. | O(f log f) | O(total data) |
| [All O(1) Data Structure](https://leetcode.com/problems/all-oone-data-structure/) | Hard | Doubly linked count buckets plus key map. | O(1) | O(n) |
| [Snapshot Array](https://leetcode.com/problems/snapshot-array/) | Medium | Per-index sorted history and binary search by snapshot id. | O(log updates) | O(updates) |
| [Design Browser History](https://leetcode.com/problems/design-browser-history/) | Medium | Two stacks or dynamic array with current pointer. | O(steps) | O(n) |
| [Design Underground System](https://leetcode.com/problems/design-underground-system/) | Medium | Maps for active trips and aggregate route stats. | O(1) avg | O(n) |

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
