# Design Data Structures — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

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

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
