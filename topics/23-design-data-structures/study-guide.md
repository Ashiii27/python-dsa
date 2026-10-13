# Design Data Structures: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Start from required operation bounds, then compose structures whose strengths cover each other’s weaknesses. Write invariants linking every index, map entry, list node, and counter.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Map + doubly linked list gives O(1) keyed recency updates for LRU. |
| 2 | Array + index map gives O(1) average insert/delete/random access. |
| 3 | Two heaps plus lazy deletion maintain dynamic medians. |
| 4 | Timestamped append-only lists support binary-search history queries. |
| 5 | Frequency buckets combine count ordering with recency for LFU. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| O(1) lookup + ordering | Map + doubly linked list |
| O(1) random set | Array + index map |
| Historical value by time | Map + sorted histories |
| Frequency then recency eviction | Maps + frequency lists |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

RandomizedSet deletion: find index `i`, move the last value into `i`, update that value’s map entry, pop the list, then remove the deleted key. The map and array remain exact inverses.

## Tricks and interview notes

- Write the representation invariant before methods.
- Use dummy head/tail nodes to simplify linked-list moves.
- Define behavior for zero capacity and duplicate operations.
- Separate public API logic from private structure-maintenance helpers.

## Common mistakes

- **Watch for:** Updating one structure but not its companion.
- **Watch for:** Using linear list removal in an allegedly O(1) API.
- **Watch for:** Ignoring tie-breaking requirements.
- **Watch for:** Failing to remove empty LFU frequency buckets or update minimum frequency.

## Implementation drills

1. Implement LRU without `OrderedDict`.
2. Implement RandomizedSet and property-test its invariant.
3. Implement TimeMap with `bisect`.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. LRU cache: the canonical design problem

Requirement: O(1) `get` and `put`, with the least recently used entry evicted at
capacity. Two primitives combine: a **hash map** for O(1) lookup and a **doubly
linked list** for O(1) reordering and eviction. `OrderedDict` already is that
structure, so know both versions.

```python
from collections import OrderedDict


class LRUCacheOrderedDict:
    """Shortest correct version: OrderedDict remembers insertion order."""

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        if key not in self.data:
            return -1
        self.data.move_to_end(key)              # mark as most recently used
        return self.data[key]

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)       # evict the oldest


class _Node:
    """Doubly linked list node used by the from-scratch version."""

    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """Hash map + doubly linked list, with sentinel head/tail nodes.

    Invariant: the list is ordered from most recently used (after head) to
    least recently used (before tail), so `tail.prev` is the eviction victim.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}                            # key -> node
        self.head, self.tail = _Node(), _Node()  # sentinels: never None
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node):
        """Insert right after head = most recently used."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key, value):
        node = self.map.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._insert_front(node)
            return
        new_node = _Node(key, value)
        self.map[key] = new_node
        self._insert_front(new_node)
        if len(self.map) > self.capacity:
            victim = self.tail.prev
            self._remove(victim)
            del self.map[victim.key]

    def __len__(self):
        return len(self.map)

    def __repr__(self):
        ordered, node = [], self.head.next
        while node is not self.tail:
            ordered.append((node.key, node.value))
            node = node.next
        return f"LRUCache(capacity={self.capacity}, mru->lru={ordered})"


if __name__ == "__main__":
    for cache in (LRUCacheOrderedDict(2), LRUCache(2)):
        cache.put(1, 1)
        cache.put(2, 2)
        print(type(cache).__name__)
        print("  get(1):", cache.get(1))
        cache.put(3, 3)                          # evicts key 2
        print("  get(2) after eviction:", cache.get(2))
        cache.put(4, 4)                          # evicts key 1
        print("  get(1):", cache.get(1), "| get(3):", cache.get(3), "| get(4):", cache.get(4))

    custom = LRUCache(2)
    custom.put("a", 1)
    custom.put("b", 2)
    custom.get("a")                              # 'a' becomes most recent
    custom.put("c", 3)                           # evicts 'b'
    print(custom)
    print("capacity 1:", (lambda c: (c.put(1, 1), c.put(2, 2), c.get(1), c.get(2)))(LRUCache(1)))
```

Output:

```text
LRUCacheOrderedDict
  get(1): 1
  get(2) after eviction: -1
  get(1): -1 | get(3): 3 | get(4): 4
LRUCache
  get(1): 1
  get(2) after eviction: -1
  get(1): -1 | get(3): 3 | get(4): 4
LRUCache(capacity=2, mru->lru=[('c', 3), ('a', 1)])
capacity 1: (None, None, -1, 2)
```

**How it works**

- The map gives O(1) access to the node; the list gives O(1) removal and re-insertion. Neither alone is enough: a list alone needs a search, a map alone cannot express "least recently used".
- Sentinel `head` and `tail` nodes remove every `if node is None` branch from `_remove` / `_insert_front` — the single best trick for linked-list code.
- `tail.prev` is always the LRU entry, so eviction is one unlink plus one `del`.
- `OrderedDict` version: `move_to_end(key)` marks recency, `popitem(last=False)` evicts. Use it unless the interviewer asks for the internals.

### 2. Combining primitives: the recurring design patterns

Most "design" questions are two known structures wired together. Learn the
pairings and you can derive the rest.

```python
import bisect
import random
from collections import deque


class RandomizedSet:
    """O(1) insert / remove / getRandom: array + value -> index map.

    Removal swaps the element with the last one so no shifting is needed.
    """

    def __init__(self):
        self.values = []
        self.position = {}

    def insert(self, val):
        if val in self.position:
            return False
        self.position[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.position:
            return False
        index = self.position[val]
        last = self.values[-1]
        self.values[index] = last                 # move the last element here
        self.position[last] = index
        self.values.pop()
        del self.position[val]
        return True

    def get_random(self):
        return random.choice(self.values)

    def __len__(self):
        return len(self.values)


class TimeMap:
    """Key -> value with timestamps: dict + parallel sorted lists + bisect."""

    def __init__(self):
        self.store = {}                            # key -> (times, values)

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = ([], [])
        times, values = self.store[key]
        times.append(timestamp)                    # appends arrive in order
        values.append(value)

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        times, values = self.store[key]
        index = bisect.bisect_right(times, timestamp) - 1    # last time <= timestamp
        return values[index] if index >= 0 else ""


class RecentCounter:
    """Sliding time window: a deque is the whole structure."""

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        while self.requests[0] < t - 3000:         # drop events outside the window
            self.requests.popleft()
        return len(self.requests)


class ExtremumTracker:
    """Track the current minimum and maximum of a multiset.

    Simplest correct version: keep counts in a dict and scan it on read.
    The structure to *mention* in interviews is a balanced multiset
    (two heaps with lazy deletion), which gives O(log n) reads.
    """

    def __init__(self):
        self.counts = {}

    def add(self, value):
        self.counts[value] = self.counts.get(value, 0) + 1

    def remove(self, value):
        if self.counts.get(value, 0) == 0:
            return False
        self.counts[value] -= 1
        if self.counts[value] == 0:
            del self.counts[value]
        return True

    def extremum(self, select):
        return select(self.counts) if self.counts else None


if __name__ == "__main__":
    randomised = RandomizedSet()
    for value in (1, 2, 3):
        randomised.insert(value)
    print("insert duplicate 2:", randomised.insert(2))
    print("remove 2:", randomised.remove(2), "| remove 9:", randomised.remove(9))
    random.seed(7)                             # reproducible output for these notes
    print("values now:", randomised.values, "| a random pick:", randomised.get_random())

    timeline = TimeMap()
    timeline.set("foo", "bar", 1)
    timeline.set("foo", "bar2", 4)
    print("get(foo, 1):", timeline.get("foo", 1))
    print("get(foo, 3):", timeline.get("foo", 3), "| get(foo, 5):", timeline.get("foo", 5))
    print("missing key:", repr(timeline.get("nope", 3)))

    counter = RecentCounter()
    print("pings:", [counter.ping(t) for t in (1, 100, 3001, 3002)])

    tracker = ExtremumTracker()
    for value in (5, 1, 9):
        tracker.add(value)
    print("min:", tracker.extremum(min), "| max:", tracker.extremum(max))
    tracker.remove(1)
    print("after removing 1 -> min:", tracker.extremum(min))
```

Output:

```text
insert duplicate 2: False
remove 2: True | remove 9: False
values now: [1, 3] | a random pick: 3
get(foo, 1): bar
get(foo, 3): bar | get(foo, 5): bar2
missing key: ''
pings: [1, 2, 3, 3]
min: 1 | max: 9
after removing 1 -> min: 5
```

**How it works**

- `RandomizedSet`: the index map lets `remove` swap the doomed element with the last one in O(1). This "swap with the last and pop" trick is the reason arrays can beat linked lists when you also need O(1) random access.
- `TimeMap`: history per key stays sorted because timestamps arrive in increasing order, so `bisect_right(times, t) − 1` is the latest value at or before `t`. If timestamps arrive out of order, use `insort` or sort on first read.
- `RecentCounter`: a deque plus "pop from the front while too old" is the universal sliding-window design; the same shape powers rate limiters and "number of recent requests".
- When a value can be *updated* (not just added), pair a heap with a hash map and use **lazy deletion**: push the new value, and skip heap entries whose cached value no longer matches.

## Solved examples

### Example 1 — Insert, delete and getRandom in O(1) (Medium)

**Problem.** A set supporting `insert`, `remove`, and `getRandom` (uniformly
random) — all in average O(1).

**Approach.** A list gives O(1) random access but O(n) removal (shifting); a set gives O(1) removal but no uniform random pick. Use both: the list holds the values and a dict maps value → index. To remove, overwrite the slot with the last element, fix that element's index, and pop the tail.

```python
import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.position = {}                    # value -> index in values

    def insert(self, val):
        if val in self.position:
            return False
        self.position[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val):
        if val not in self.position:
            return False
        index = self.position[val]
        last = self.values[-1]
        self.values[index] = last             # move the last element into the gap
        self.position[last] = index
        self.values.pop()
        del self.position[val]
        return True

    def get_random(self):
        return random.choice(self.values)


if __name__ == "__main__":
    rs = RandomizedSet()
    print("insert 1:", rs.insert(1), "| insert 2:", rs.insert(2), "| insert 1 again:", rs.insert(1))
    print("values:", rs.values)
    print("remove 1:", rs.remove(1), "| values:", rs.values)
    print("remove 3 (absent):", rs.remove(3))
    print("10 random picks:", sorted({rs.get_random() for _ in range(10)}))
    print("empty structure:", RandomizedSet().values)
```

Output:

```text
insert 1: True | insert 2: True | insert 1 again: False
values: [1, 2]
remove 1: True | values: [2]
remove 3 (absent): False
10 random picks: [2]
empty structure: []
```

**Complexity.** O(1) average for all three operations, O(n) space. Note that `remove` is O(1) only because we do **not** care about order — if you do, use a list plus tombstones, or accept O(n).

### Example 2 — Time-based key-value store (Medium)

**Problem.** Store `(key, value, timestamp)` and answer "value of `key` at time
`t`" — the latest value with timestamp ≤ `t`.

**Approach.** Per key, keep parallel sorted lists of timestamps and values. Because writes arrive with non-decreasing timestamps, both stay sorted, so the lookup is a single binary search: `bisect_right(times, t) − 1`. Return `""` when the index is negative (no value at or before `t`).

```python
import bisect


class TimeMap:
    def __init__(self):
        self.store = {}                        # key -> (times, values)

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = ([], [])
        times, values = self.store[key]
        times.append(timestamp)
        values.append(value)

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        times, values = self.store[key]
        index = bisect.bisect_right(times, timestamp) - 1
        return values[index] if index >= 0 else ""


if __name__ == "__main__":
    kv = TimeMap()
    kv.set("foo", "bar", 1)
    print("get(foo, 1):", kv.get("foo", 1))
    print("get(foo, 3):", kv.get("foo", 3))
    kv.set("foo", "bar2", 4)
    print("get(foo, 4):", kv.get("foo", 4), "| get(foo, 5):", kv.get("foo", 5))
    print("before any write, get(foo, 0):", repr(kv.get("foo", 0)))
    print("unknown key:", repr(kv.get("x", 10)))
```

Output:

```text
get(foo, 1): bar
get(foo, 3): bar
get(foo, 4): bar2 | get(foo, 5): bar2
before any write, get(foo, 0): ''
unknown key: ''
```

**Complexity.** O(1) amortised `set`, O(log n) `get` (n = number of writes to that key), O(total writes) space.

### Example 3 — Design Twitter (Medium)

**Problem.** Support `postTweet(userId, tweetId)`, `getNewsFeed(userId)` (the 10
most recent tweets from the user and everyone they follow), `follow`, and
`unfollow`.

**Approach.** Store each user's tweets as a list with an increasing timestamp, plus a `follows` set. For the feed, use a heap seeded with the **latest tweet of each followed user**; pop the newest, push that user's previous tweet, and repeat 10 times. This is "merge k sorted lists" with a heap — the work is O(k log k) where k is the number of followed users, instead of collecting every tweet.

```python
import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)          # user -> [(time, tweetId), ...]
        self.following = defaultdict(set)        # user -> set of users they follow

    def post_tweet(self, user_id, tweet_id):
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id):
        users = self.following[user_id] | {user_id}
        heap = []
        for user in users:
            if self.tweets[user]:
                time, tweet_id = self.tweets[user][-1]     # their latest tweet
                heapq.heappush(heap, (-time, tweet_id, user, len(self.tweets[user]) - 1))

        feed = []
        while heap and len(feed) < 10:
            _, tweet_id, user, index = heapq.heappop(heap)
            feed.append(tweet_id)
            if index > 0:                                   # push their previous tweet
                time, previous_id = self.tweets[user][index - 1]
                heapq.heappush(heap, (-time, previous_id, user, index - 1))
        return feed

    def follow(self, follower_id, followee_id):
        if follower_id != followee_id:
            self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        self.following[follower_id].discard(followee_id)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.post_tweet(1, 101)
    twitter.post_tweet(2, 202)
    twitter.follow(1, 2)
    print("feed for user 1:", twitter.get_news_feed(1))
    twitter.post_tweet(1, 103)
    print("feed after posting 103:", twitter.get_news_feed(1))
    twitter.unfollow(1, 2)
    print("feed after unfollow:", twitter.get_news_feed(1))
    print("feed for user 3 (no activity):", twitter.get_news_feed(3))
    print("self-follow is ignored:", (twitter.follow(5, 5), twitter.get_news_feed(5)))
```

Output:

```text
feed for user 1: [202, 101]
feed after posting 103: [103, 202, 101]
feed after unfollow: [103, 101]
feed for user 3 (no activity): []
self-follow is ignored: (None, [])
```

**Complexity.** `postTweet` O(1); `getNewsFeed` O(F log F) for F followed users (plus 10 pops); `follow` / `unfollow` O(1). The production version fans the tweet out to followers' pre-computed feeds at write time, trading write cost for O(1) reads — a trade-off worth mentioning out loud.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | LeetCode | Medium |
| [Design Authentication Manager](https://leetcode.com/problems/design-authentication-manager/) | LeetCode | Medium |
| [Design Food Rating System](https://leetcode.com/problems/design-a-food-rating-system/) | LeetCode | Medium |
| [Dinner Plate Stacks](https://leetcode.com/problems/dinner-plate-stacks/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain map + doubly linked list gives o(1) keyed recency updates for lru without notes.
- [ ] Explain array + index map gives o(1) average insert/delete/random access without notes.
- [ ] Explain two heaps plus lazy deletion maintain dynamic medians without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
