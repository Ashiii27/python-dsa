# Greedy Algorithms: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Make a locally best irreversible choice only after proving an optimal solution can be transformed to include it. Sorting often exposes the safe choice.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Exchange arguments replace an optimal solution’s first differing choice. |
| 2 | Stays-ahead proofs compare every prefix of greedy and optimal solutions. |
| 3 | Earliest finishing interval maximizes the room left for future choices. |
| 4 | Farthest-reach scans compress BFS-like layers. |
| 5 | Global feasibility can coexist with local resets, as in Gas Station. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Max non-overlapping intervals | Sort by end |
| Pair extremes | Sort + two pointers |
| Reachability | Track farthest index |
| Need repeated best available choice | Heap-based greedy |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For interval scheduling, choose the compatible interval with earliest end. If an optimum first chooses a later-ending interval, swapping in the greedy interval cannot invalidate any later selected interval and leaves at least as much room.

## Tricks and interview notes

- State the greedy choice and its proof separately.
- Try sorting by start, end, value, or ratio and search for a counterexample.
- A heap can choose the current best while a sorted pointer releases candidates.
- Greedy may compute feasibility even when DP computes optimum.

## Common mistakes

- **Watch for:** Assuming a plausible heuristic is a proof.
- **Watch for:** Sorting by start when earliest end is required.
- **Watch for:** Ignoring ties that affect feasibility.
- **Watch for:** Using greedy for 0/1 knapsack by value/weight ratio.

## Implementation drills

1. Write an exchange proof for interval scheduling.
2. Derive Jump Game II as layers.
3. Find a counterexample to a wrong coin-change greedy rule.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. When greedy works — and when it silently fails

Greedy is only correct with an **exchange argument**: show that taking the
locally best choice can never block a better solution. The coin-change example is
the fastest way to see a greedy rule break.

```python
def coin_change_greedy(coins, amount):
    """Take the largest coin that fits, repeatedly."""
    coins = sorted(coins, reverse=True)
    used = 0
    for coin in coins:
        used += amount // coin
        amount %= coin
    return used if amount == 0 else -1


def coin_change_dp(coins, amount):
    """True optimum: dp[a] = fewest coins for amount a."""
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return -1 if dp[amount] == INF else dp[amount]


def activity_selection(intervals):
    """Max non-overlapping intervals: always take the one that FINISHES first.

    Exchange argument: an earlier finish leaves at least as much room as any
    other choice, so swapping the first chosen interval for this one is safe.
    """
    ordered = sorted(intervals, key=lambda x: x[1])
    chosen, last_end = [], float("-inf")
    for start, end in ordered:
        if start >= last_end:              # no overlap with what we took
            chosen.append((start, end))
            last_end = end
    return chosen


if __name__ == "__main__":
    for coins, amount in (([1, 5, 10, 25], 63), ([1, 3, 4], 6), ([1, 5, 10, 25], 30)):
        print(f"coins={coins}, amount={amount}: greedy={coin_change_greedy(coins, amount)}, "
              f"optimal={coin_change_dp(coins, amount)}")

    intervals = [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
    print("intervals:", intervals)
    print("maximum non-overlapping set:", activity_selection(intervals))
    print("count:", len(activity_selection(intervals)))
    print("no intervals:", activity_selection([]))
```

Output:

```text
coins=[1, 5, 10, 25], amount=63: greedy=6, optimal=6
coins=[1, 3, 4], amount=6: greedy=3, optimal=2
coins=[1, 5, 10, 25], amount=30: greedy=2, optimal=2
intervals: [(1, 3), (2, 5), (3, 9), (6, 8), (8, 11)]
maximum non-overlapping set: [(1, 3), (6, 8), (8, 11)]
count: 3
no intervals: []
```

**How it works**

- With canonical denominations `[1, 5, 10, 25]` greedy is optimal; with `[1, 3, 4]` and amount 6 greedy picks `4 + 1 + 1` (3 coins) while the optimum is `3 + 3` (2 coins). The greedy rule is a heuristic, not a proof — and the proof only exists for special ("canonical") coin systems.
- `activity_selection` sorts by **finish time**, not start time or duration. That single choice is the exchange argument: the earliest-finishing interval can never be a worse first pick.
- Greedy runtime is usually O(n log n) from the sort; the scan afterwards is O(n).

### 2. Greedy patterns that show up repeatedly

Three shapes cover most greedy problems: sort then scan, keep the best so far,
and repeatedly take the current extreme with a heap.

```python
import heapq


# --- 1. Sort, then match greedily --------------------------------------
def assign_cookies(children, cookies):
    """Give the smallest cookie that satisfies the least greedy child."""
    children.sort()
    cookies.sort()
    i = j = fed = 0
    while i < len(children) and j < len(cookies):
        if cookies[j] >= children[i]:
            fed += 1
            i += 1
        j += 1                            # too small to help anyone: discard
    return fed


def boats_to_save(people, limit):
    """Pair the heaviest person with the lightest that fits."""
    people.sort()
    light, heavy, boats = 0, len(people) - 1, 0
    while light <= heavy:
        if people[light] + people[heavy] <= limit:
            light += 1                    # they share a boat
        heavy -= 1                        # the heavy one always goes
        boats += 1
    return boats


# --- 2. Keep the best so far -------------------------------------------
def can_jump(nums):
    """Farthest reachable index: if we ever stand on an unreachable one, fail."""
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
    return True


def max_profit(prices):
    """One transaction: track the lowest price seen so far."""
    best, lowest = 0, prices[0]
    for price in prices[1:]:
        best = max(best, price - lowest)
        lowest = min(lowest, price)
    return best


# --- 3. Repeatedly take the extreme (heap-assisted greedy) -------------
def connect_ropes(ropes):
    """Cheapest way to join ropes: always join the two shortest first (Huffman)."""
    heap = list(ropes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        total += first + second
        heapq.heappush(heap, first + second)
    return total


if __name__ == "__main__":
    print("assign_cookies([1, 2, 3], [1, 1]):", assign_cookies([1, 2, 3], [1, 1]))
    print("assign_cookies([1, 2], [1, 2, 3]):", assign_cookies([1, 2], [1, 2, 3]))
    print("boats([3, 2, 2, 1], limit 3):", boats_to_save([3, 2, 2, 1], 3))
    print("can_jump([2, 3, 1, 1, 4]):", can_jump([2, 3, 1, 1, 4]))
    print("can_jump([3, 2, 1, 0, 4]):", can_jump([3, 2, 1, 0, 4]))
    print("max_profit([7, 1, 5, 3, 6, 4]):", max_profit([7, 1, 5, 3, 6, 4]))
    print("connect_ropes([4, 3, 2, 6]):", connect_ropes([4, 3, 2, 6]))
```

Output:

```text
assign_cookies([1, 2, 3], [1, 1]): 1
assign_cookies([1, 2], [1, 2, 3]): 2
boats([3, 2, 2, 1], limit 3): 3
can_jump([2, 3, 1, 1, 4]): True
can_jump([3, 2, 1, 0, 4]): False
max_profit([7, 1, 5, 3, 6, 4]): 5
connect_ropes([4, 3, 2, 6]): 29
```

**How it works**

- In `assign_cookies` and `boats_to_save`, sorting first turns a matching problem into a two-pointer scan. The proof is always "the smallest sufficient resource is never worse than a larger one".
- `can_jump` maintains one number: the farthest index reachable so far. If the loop reaches an index beyond it, that index cannot be reached at all.
- `connect_ropes` is Huffman coding: joining the two shortest first is optimal because early joins get paid for repeatedly, so they must involve the smallest lengths.

## Solved examples

### Example 1 — Jump game II: minimum jumps (Medium)

**Problem.** Each element is the maximum jump length from that position. Return
the minimum number of jumps to reach the last index.

**Approach.** BFS-style layered greedy: the jumps reachable in `k` steps form a window `[current_end + 1, farthest]`. Scan that window, tracking how far the next jump could reach; when the scan reaches the end of the current window, you must jump, and the new window is everything up to `farthest`. One pass, O(n), no DP table needed.

```python
def jump(nums):
    if len(nums) <= 1:
        return 0
    jumps = 0
    current_end = 0            # farthest index reachable with `jumps` jumps
    farthest = 0               # farthest index reachable with one more jump
    for i in range(len(nums) - 1):       # never need to jump from the last index
        farthest = max(farthest, i + nums[i])
        if i == current_end:             # window exhausted: jump
            jumps += 1
            current_end = farthest
            if current_end >= len(nums) - 1:
                break
    return jumps


if __name__ == "__main__":
    print("jumps for [2, 3, 1, 1, 4]:", jump([2, 3, 1, 1, 4]))       # 2
    print("jumps for [2, 3, 0, 1, 4]:", jump([2, 3, 0, 1, 4]))       # 2
    print("jumps for [1, 1, 1, 1]:", jump([1, 1, 1, 1]))             # 3
    print("single element:", jump([5]))                              # 0
```

Output:

```text
jumps for [2, 3, 1, 1, 4]: 2
jumps for [2, 3, 0, 1, 4]: 2
jumps for [1, 1, 1, 1]: 3
single element: 0
```

**Complexity.** O(n) time, O(1) space. The greedy choice is "jump to the index that maximises the next reach" — and you never need to know which index that is, only the resulting boundary.

### Example 2 — Gas station (Medium)

**Problem.** Two arrays: `gas[i]` is the fuel gained at station `i`, `cost[i]`
the fuel to reach station `i + 1`. Find a starting station from which you can
complete the circuit, or −1.

**Approach.** Two facts make this O(n). (1) If total gas < total cost, no circuit exists. (2) Otherwise a start exists: whenever the tank goes negative at station `i + 1`, no station from the current start up to `i` can be the answer (each of them would also have died there or earlier, since they all arrive with at most as much fuel), so restart at `i + 1`. One pass, one restart candidate.

```python
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1                          # not enough fuel in total
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:                       # stations start..i all fail
            start = i + 1
            tank = 0
    return start


if __name__ == "__main__":
    print("start for gas=[1,2,3,4,5], cost=[3,4,5,1,2]:",
          can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))     # 3
    print("start for gas=[2,3,4], cost=[3,4,3]:",
          can_complete_circuit([2, 3, 4], [3, 4, 3]))                 # -1
    print("single station:", can_complete_circuit([5], [4]))          # 0
    print("single station, not enough:", can_complete_circuit([3], [4]))
```

Output:

```text
start for gas=[1,2,3,4,5], cost=[3,4,5,1,2]: 3
start for gas=[2,3,4], cost=[3,4,3]: -1
single station: 0
single station, not enough: -1
```

**Complexity.** O(n) time, O(1) space. The "restart after the failure point" argument is worth stating out loud in an interview — it is the whole proof.

### Example 3 — Non-overlapping intervals (Medium)

**Problem.** Given intervals, return the minimum number to remove so that no
two overlap.

**Approach.** Equivalent to keeping the maximum number of non-overlapping intervals, which is activity selection: sort by end time and greedily take the next interval that starts at or after the last chosen end. Alternative formulation: sort by start and, on overlap, drop the interval with the **later** end (it blocks more of the future) — both are correct and both are O(n log n).

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    ordered = sorted(intervals, key=lambda x: x[1])
    kept, last_end = 0, float("-inf")
    for start, end in ordered:
        if start >= last_end:              # keep the earliest-finishing option
            kept += 1
            last_end = end
    return len(intervals) - kept


def erase_overlap_by_start(intervals):
    """Same answer sorting by start: on overlap, drop the later-ending interval."""
    if not intervals:
        return 0
    ordered = sorted(intervals)
    removed, previous_end = 0, ordered[0][1]
    for start, end in ordered[1:]:
        if start < previous_end:           # overlap: remove the one ending later
            removed += 1
            previous_end = min(previous_end, end)
        else:
            previous_end = end
    return removed


if __name__ == "__main__":
    intervals = [(1, 2), (2, 3), (3, 4), (1, 3)]
    print("removals (by end):", erase_overlap_intervals(intervals))
    print("removals (by start):", erase_overlap_by_start(intervals))
    print("no overlaps:", erase_overlap_intervals([(1, 2), (2, 3)]))
    print("all overlapping:", erase_overlap_intervals([(1, 5), (2, 3), (3, 4)]))
    print("empty:", erase_overlap_intervals([]))
```

Output:

```text
removals (by end): 1
removals (by start): 1
no overlaps: 0
all overlapping: 1
empty: 0
```

**Complexity.** O(n log n) time (the sort dominates) and O(1) extra space beyond it. The same greedy appears in "minimum arrows to burst balloons" and "meeting rooms II" (the latter needs a heap to count simultaneous rooms).

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Movie Festival](https://cses.fi/problemset/task/1629) | CSES | Medium |
| [Tasks and Deadlines](https://cses.fi/problemset/task/1630) | CSES | Medium |
| [Ferris Wheel](https://cses.fi/problemset/task/1090) | CSES | Medium |
| [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) | LeetCode | Easy |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain exchange arguments replace an optimal solution’s first differing choice without notes.
- [ ] Explain stays-ahead proofs compare every prefix of greedy and optimal solutions without notes.
- [ ] Explain earliest finishing interval maximizes the room left for future choices without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
