"""Reusable Python DSA templates.

These are reference implementations for learning and revision. In interviews,
explain the invariant and adapt the template to the exact problem instead of
copying blindly.
"""

from __future__ import annotations

from collections import Counter, OrderedDict, defaultdict, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from math import inf
from random import choice
from typing import Any, Callable, DefaultDict, Dict, Hashable, Iterable, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Binary search
# ---------------------------------------------------------------------------


def binary_search(nums: List[int], target: int) -> int:
    """Return index of target in sorted nums, or -1 if absent."""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def lower_bound(nums: List[int], target: int) -> int:
    """First index i where nums[i] >= target. Returns len(nums) if none."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    """First index i where nums[i] > target. Returns len(nums) if none."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def first_true(lo: int, hi: int, predicate: Callable[[int], bool]) -> int:
    """Return first x in inclusive [lo, hi] where predicate(x) is True.

    Requires predicate to be monotonic: False...False True...True.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def last_true(lo: int, hi: int, predicate: Callable[[int], bool]) -> int:
    """Return last x in inclusive [lo, hi] where predicate(x) is True.

    Requires predicate to be monotonic: True...True False...False.
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if predicate(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


# ---------------------------------------------------------------------------
# Arrays and strings
# ---------------------------------------------------------------------------


def two_sum_indices(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    return None


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ans: List[List[int]] = []
    n = len(nums)
    for i in range(n - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return ans


def product_except_self(nums: List[int]) -> List[int]:
    ans = [1] * len(nums)
    prefix = 1
    for i, x in enumerate(nums):
        ans[i] = prefix
        prefix *= x
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]
    return ans


def max_subarray(nums: List[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1
    for x in nums:
        prefix += x
        count += seen[prefix - k]
        seen[prefix] += 1
    return count


def longest_substring_without_repeat(s: str) -> int:
    left = 0
    last: Dict[str, int] = {}
    best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best


def min_window_substring(s: str, t: str) -> str:
    if not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (inf, 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            old = s[left]
            need[old] += 1
            if need[old] > 0:
                missing += 1
            left += 1
    return "" if best[0] == inf else s[best[1] : best[2]]


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged: List[List[int]] = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


# ---------------------------------------------------------------------------
# Linked lists
# ---------------------------------------------------------------------------


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev


def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
    if slow.next:
        slow.next = slow.next.next
    return dummy.next


# ---------------------------------------------------------------------------
# Stacks, queues, monotonic structures
# ---------------------------------------------------------------------------


def next_greater_elements(nums: List[int]) -> List[int]:
    ans = [-1] * len(nums)
    stack: List[int] = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x
        stack.append(i)
    return ans


def daily_temperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack: List[int] = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans


def sliding_window_max(nums: List[int], k: int) -> List[int]:
    q: deque[int] = deque()  # indices, values decreasing
    ans: List[int] = []
    for i, x in enumerate(nums):
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans


def largest_rectangle_area(heights: List[int]) -> int:
    stack: List[int] = []
    best = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left_smaller = stack[-1] if stack else -1
            width = i - left_smaller - 1
            best = max(best, height * width)
        stack.append(i)
    return best


# ---------------------------------------------------------------------------
# Trees
# ---------------------------------------------------------------------------


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    ans: List[int] = []
    stack: List[TreeNode] = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        ans.append(cur.val)
        cur = cur.right
    return ans


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans: List[List[int]] = []
    q: deque[TreeNode] = deque([root])
    while q:
        level: List[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
    return ans


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


def serialize_preorder(root: Optional[TreeNode]) -> str:
    values: List[str] = []

    def dfs(node: Optional[TreeNode]) -> None:
        if not node:
            values.append("#")
            return
        values.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return " ".join(values)


def deserialize_preorder(data: str) -> Optional[TreeNode]:
    values = iter(data.split())

    def build() -> Optional[TreeNode]:
        val = next(values)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()


# ---------------------------------------------------------------------------
# Graphs
# ---------------------------------------------------------------------------


def build_undirected_graph(edges: Iterable[Tuple[Hashable, Hashable]]) -> DefaultDict[Hashable, List[Hashable]]:
    graph: DefaultDict[Hashable, List[Hashable]] = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def bfs_shortest_distances(graph: Dict[Hashable, List[Hashable]], source: Hashable) -> Dict[Hashable, int]:
    dist = {source: 0}
    q = deque([source])
    while q:
        node = q.popleft()
        for nei in graph.get(node, []):
            if nei not in dist:
                dist[nei] = dist[node] + 1
                q.append(nei)
    return dist


def topological_sort(num_nodes: int, edges: Iterable[Tuple[int, int]]) -> List[int]:
    graph = [[] for _ in range(num_nodes)]
    indeg = [0] * num_nodes
    for pre, nxt in edges:
        graph[pre].append(nxt)
        indeg[nxt] += 1
    q = deque([i for i, d in enumerate(indeg) if d == 0])
    order: List[int] = []
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph[node]:
            indeg[nei] -= 1
            if indeg[nei] == 0:
                q.append(nei)
    return order if len(order) == num_nodes else []


def dijkstra(graph: Dict[Hashable, List[Tuple[Hashable, int]]], source: Hashable) -> Dict[Hashable, float]:
    dist: Dict[Hashable, float] = {source: 0}
    heap: List[Tuple[float, Hashable]] = [(0, source)]
    while heap:
        d, node = heappop(heap)
        if d != dist[node]:
            continue
        for nei, weight in graph.get(node, []):
            nd = d + weight
            if nd < dist.get(nei, inf):
                dist[nei] = nd
                heappush(heap, (nd, nei))
    return dist


def bellman_ford(num_nodes: int, edges: Iterable[Tuple[int, int, int]], source: int) -> Tuple[List[float], bool]:
    """Return distances and whether a negative cycle is reachable."""
    edge_list = list(edges)
    dist = [inf] * num_nodes
    dist[source] = 0
    for _ in range(num_nodes - 1):
        changed = False
        for u, v, w in edge_list:
            if dist[u] != inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    has_negative_cycle = any(dist[u] != inf and dist[u] + w < dist[v] for u, v, w in edge_list)
    return dist, has_negative_cycle


# ---------------------------------------------------------------------------
# Union Find
# ---------------------------------------------------------------------------


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.components -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)


# ---------------------------------------------------------------------------
# Trie
# ---------------------------------------------------------------------------


class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.is_word)

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, text: str) -> Optional[TrieNode]:
        node = self.root
        for ch in text:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ---------------------------------------------------------------------------
# Fenwick tree and segment tree
# ---------------------------------------------------------------------------


class FenwickTree:
    """Fenwick tree for point updates and prefix/range sums, 0-indexed API."""

    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        index += 1
        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def range_sum(self, left: int, right: int) -> int:
        if right < left:
            return 0
        return self.prefix_sum(right) - (self.prefix_sum(left - 1) if left else 0)


class SegmentTreeSum:
    """Iterative segment tree for point updates and inclusive range sums."""

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i, x in enumerate(nums):
            self.tree[self.n + i] = x
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, value: int) -> None:
        pos = self.n + index
        self.tree[pos] = value
        pos //= 2
        while pos:
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]
            pos //= 2

    def query(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        ans = 0
        while left <= right:
            if left % 2 == 1:
                ans += self.tree[left]
                left += 1
            if right % 2 == 0:
                ans += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return ans


# ---------------------------------------------------------------------------
# Dynamic programming
# ---------------------------------------------------------------------------


def coin_change_min(coins: List[int], amount: int) -> int:
    sentinel = amount + 1
    dp = [0] + [sentinel] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if a >= coin:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return -1 if dp[amount] == sentinel else dp[amount]


def lis_length(nums: List[int]) -> int:
    tails: List[int] = []
    for x in nums:
        i = lower_bound(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def lcs_length(a: str, b: str) -> int:
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0] * (len(b) + 1)
        for j, cb in enumerate(b, 1):
            if ca == cb:
                cur[j] = prev[j - 1] + 1
            else:
                cur[j] = max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


def edit_distance(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            if ca == cb:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev = cur
    return prev[-1]


# ---------------------------------------------------------------------------
# Backtracking
# ---------------------------------------------------------------------------


def subsets(nums: List[int]) -> List[List[int]]:
    ans: List[List[int]] = []
    path: List[int] = []

    def backtrack(i: int) -> None:
        if i == len(nums):
            ans.append(path.copy())
            return
        backtrack(i + 1)
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()

    backtrack(0)
    return ans


def permutations(nums: List[int]) -> List[List[int]]:
    ans: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            ans.append(path.copy())
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            backtrack()
            path.pop()
            used[i] = False

    backtrack()
    return ans


# ---------------------------------------------------------------------------
# Heap-based patterns and design structures
# ---------------------------------------------------------------------------


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    return [num for num, _ in Counter(nums).most_common(k)]


class MedianFinder:
    def __init__(self):
        self.small: List[int] = []  # max-heap via negatives
        self.large: List[int] = []  # min-heap

    def add_num(self, num: int) -> None:
        heappush(self.small, -num)
        heappush(self.large, -heappop(self.small))
        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


class RandomizedSet:
    def __init__(self):
        self.values: List[int] = []
        self.index: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        idx = self.index[val]
        last = self.values[-1]
        self.values[idx] = last
        self.index[last] = idx
        self.values.pop()
        del self.index[val]
        return True

    def get_random(self) -> int:
        return choice(self.values)


class TimeMap:
    def __init__(self):
        self.store: DefaultDict[str, List[Tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo - 1][1] if lo else ""


# ---------------------------------------------------------------------------
# String algorithms
# ---------------------------------------------------------------------------


def prefix_function(pattern: str) -> List[int]:
    """KMP prefix table: longest proper prefix that is also suffix for each prefix."""
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text: str, pattern: str) -> List[int]:
    if not pattern:
        return list(range(len(text) + 1))
    pi = prefix_function(pattern)
    ans: List[int] = []
    j = 0
    for i, ch in enumerate(text):
        while j and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            ans.append(i - len(pattern) + 1)
            j = pi[j - 1]
    return ans


def z_function(s: str) -> List[int]:
    z = [0] * len(s)
    left = right = 0
    for i in range(1, len(s)):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


# ---------------------------------------------------------------------------
# Math and bit manipulation
# ---------------------------------------------------------------------------


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)


def pow_mod(base: int, exp: int, mod: int) -> int:
    ans = 1
    base %= mod
    while exp:
        if exp & 1:
            ans = ans * base % mod
        base = base * base % mod
        exp >>= 1
    return ans


def sieve(n: int) -> List[int]:
    """Return all primes <= n."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    return [i for i, ok in enumerate(is_prime) if ok]


def count_bits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    ans: List[List[int]] = []
    n = len(nums)
    for mask in range(1 << n):
        ans.append([nums[i] for i in range(n) if mask & (1 << i)])
    return ans
