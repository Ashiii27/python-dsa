# Advanced Strings: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Avoid restarting comparisons after mismatch by preprocessing reusable border information or hashing substrings. Choose deterministic algorithms when collisions are unacceptable.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | KMP prefix values encode longest proper prefix that is also a suffix. |
| 2 | Z values encode match length between a suffix and the whole string. |
| 3 | Rolling hash compares substrings after O(n) preprocessing. |
| 4 | Manacher finds all palindrome radii in O(n). |
| 5 | Trie and suffix structures serve different prefix/subsequence query needs. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Find pattern occurrences | KMP or Z |
| Compare many substrings | Rolling hash |
| Longest palindrome around centers | Expand or Manacher |
| Prefix equals suffix | Prefix/Z function |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

For pattern `ababaca`, KMP fallback after mismatch does not return to zero blindly. It follows the prefix table to the longest border, reusing characters already known to match.

## Tricks and interview notes

- Use a separator absent from the alphabet when concatenating strings for KMP/Z tricks.
- Double hash or verify matches to control collision risk.
- Define whether hash intervals are inclusive or half-open.
- Start with center expansion before reaching for Manacher unless constraints demand linear time.

## Common mistakes

- **Watch for:** Building the prefix table with the search text instead of the pattern.
- **Watch for:** Incorrect KMP fallback (`j = lps[j-1]` is essential).
- **Watch for:** Assuming rolling hash is collision-free.
- **Watch for:** Ignoring Unicode/alphabet assumptions.

## Implementation drills

1. Implement prefix and Z functions from memory.
2. Find every pattern occurrence.
3. Build normalized substring hashes.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. KMP prefix function and the Z-function

Both build, in O(n), a table that says "how much of the string matches itself at
this position" — the key to linear-time pattern matching and to many "border /
period" problems.

```python
def prefix_function(s):
    """pi[i] = length of the longest proper prefix of s[:i+1] that is also a suffix."""
    pi = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]                  # fall back to the next-best border
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text, pattern):
    """First index of `pattern` in `text`, or -1. O(n + m)."""
    if not pattern:
        return 0
    pi = prefix_function(pattern)
    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = pi[j - 1]                  # reuse what already matched
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
    return -1


def kmp_search_all(text, pattern):
    """Every starting index where `pattern` occurs."""
    if not pattern:
        return list(range(len(text) + 1))
    pi = prefix_function(pattern)
    positions, j = [], 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                positions.append(i - len(pattern) + 1)
                j = pi[j - 1]              # allow overlapping matches
    return positions


def z_function(s):
    """z[i] = length of the longest prefix of s starting at i."""
    n = len(s)
    z = [0] * n
    left = right = 0                       # current [left, right] match window
    for i in range(1, n):
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])     # reuse the mirrored value
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > right:
            left, right = i, i + z[i] - 1
    return z


def z_search(text, pattern):
    """All occurrences via the Z-function: combine as 'pattern#text'."""
    if not pattern:
        return list(range(len(text) + 1))
    combined = pattern + "#" + text        # '#' must not occur in either string
    z = z_function(combined)
    m = len(pattern)
    return [i - m - 1 for i in range(m + 1, len(combined)) if z[i] == m]


if __name__ == "__main__":
    print("prefix_function('aabaaab'):", prefix_function("aabaaab"))
    print("prefix_function('abcd'):", prefix_function("abcd"))
    print("kmp_search('hello', 'll'):", kmp_search("hello", "ll"))
    print("kmp_search('aaaaa', 'bba'):", kmp_search("aaaaa", "bba"))
    print("kmp_search('a', ''):", kmp_search("a", ""))
    print("kmp_search_all('abababab', 'abab'):", kmp_search_all("abababab", "abab"))
    print("z_function('aaaaa'):", z_function("aaaaa"))
    print("z_function('ababc'):", z_function("ababc"))
    print("z_search('abracadabra', 'abra'):", z_search("abracadabra", "abra"))
```

Output:

```text
prefix_function('aabaaab'): [0, 1, 0, 1, 2, 2, 3]
prefix_function('abcd'): [0, 0, 0, 0]
kmp_search('hello', 'll'): 2
kmp_search('aaaaa', 'bba'): -1
kmp_search('a', ''): 0
kmp_search_all('abababab', 'abab'): [0, 2, 4]
z_function('aaaaa'): [0, 4, 3, 2, 1]
z_function('ababc'): [0, 0, 2, 0, 0]
z_search('abracadabra', 'abra'): [0, 7]
```

**How it works**

- `pi[i]` is the "border" length: the longest prefix that is also a suffix of `s[:i+1]`. When a mismatch occurs at `pattern[j]`, `pi[j − 1]` tells you the longest prefix that still matches, so you never move the text pointer backwards — that is why KMP is linear.
- The Z-function's `z[i]` measures the match between the whole string and the suffix starting at `i`. The `[left, right]` window lets the algorithm copy a previously computed value instead of re-comparing, which is the same amortised argument as KMP.
- `z_search` concatenates as `pattern#text`: any `z` value equal to `len(pattern)` at a text position is a full match.
- Both tables also solve "shortest palindrome", "string period", and "concatenation of words" style problems, because a border of length `k` means a period of `n − k`.

### 2. Rolling hash (Rabin–Karp)

Treat a substring as a number in a large base: `hash = c₀·B^(L−1) + c₁·B^(L−2) + …`.
With prefix hashes and powers of the base, any substring hash is O(1), so you can
compare substrings — or slide a window — in O(n) total.

```python
class RollingHash:
    """Polynomial rolling hash: O(n) preprocessing, O(1) substring hash."""

    def __init__(self, text, base=911_382_323, mod=972_663_749):
        self.text = text
        self.base = base
        self.mod = mod
        self.prefix = [0] * (len(text) + 1)
        self.powers = [1] * (len(text) + 1)
        for i, ch in enumerate(text):
            self.prefix[i + 1] = (self.prefix[i] * base + ord(ch)) % mod
            self.powers[i + 1] = self.powers[i] * base % mod

    def substring_hash(self, left, right):
        """Hash of text[left:right] (half-open)."""
        length = right - left
        return (self.prefix[right] - self.prefix[left] * self.powers[length]) % self.mod


def rabin_karp(text, pattern):
    """All occurrences of pattern in text, with a real comparison to confirm hits."""
    if not pattern:
        return list(range(len(text) + 1))
    m, n = len(pattern), len(text)
    if m > n:
        return []
    text_hash = RollingHash(text)
    target = RollingHash(pattern).substring_hash(0, m)
    hits = []
    for i in range(n - m + 1):
        if text_hash.substring_hash(i, i + m) == target:
            if text[i:i + m] == pattern:                  # guard against collisions
                hits.append(i)
    return hits


def longest_common_substring(a, b):
    """Binary search the length + rolling hash: O((n + m) log min(n, m))."""
    def has_common(length):
        if length == 0:
            return True
        seen = {b_hash.substring_hash(i, i + length) for i in range(len(b) - length + 1)}
        for i in range(len(a) - length + 1):
            if a_hash.substring_hash(i, i + length) in seen:
                if a[i:i + length] in b:
                    return True
        return False

    a_hash, b_hash = RollingHash(a), RollingHash(b)
    lo, hi, best = 0, min(len(a), len(b)), ""
    while lo <= hi:
        mid = (lo + hi) // 2
        if has_common(mid):
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1
    for start in range(len(a) - best + 1):
        if a[start:start + best] in b:
            return a[start:start + best]
    return ""


if __name__ == "__main__":
    text = "abracadabra"
    print("rabin_karp('abracadabra', 'abra'):", rabin_karp(text, "abra"))
    print("rabin_karp('aaaa', 'aa'):", rabin_karp("aaaa", "aa"))
    print("rabin_karp('abc', 'd'):", rabin_karp("abc", "d"))

    hasher = RollingHash("abcdef")
    print("hash of 'cd':", hasher.substring_hash(2, 4),
          "| equal substrings match:", hasher.substring_hash(2, 4) == hasher.substring_hash(2, 4))
    print("longest common substring of 'xabxac' and 'abcabxabcd':",
          longest_common_substring("xabxac", "abcabxabcd"))
```

Output:

```text
rabin_karp('abracadabra', 'abra'): [0, 7]
rabin_karp('aaaa', 'aa'): [0, 1, 2]
rabin_karp('abc', 'd'): []
hash of 'cd': 741785169 | equal substrings match: True
longest common substring of 'xabxac' and 'abcabxabcd': abxa
```

**How it works**

- `substring_hash` subtracts the shifted prefix: `prefix[right] − prefix[left] · B^(length)`. Every hash is taken modulo a large prime; using **two** different moduli (or a 64-bit modulus) makes collisions negligible in practice.
- Always confirm a hash hit with a real comparison (as `rabin_karp` does) unless the problem allows a negligible error probability — and say which you are doing.
- Hash + binary search over the length is a general technique: "longest repeated substring", "longest common substring", and "longest duplicated substring" all fall out of it in O(n log n).

## Solved examples

### Example 1 — Find the index of the first occurrence (Easy)

**Problem.** Return the index of the first occurrence of `needle` in `haystack`,
or −1. (Implement `strStr`.)

**Approach.** The naive check is O(n · m). KMP preprocesses the needle into a prefix table so that after a mismatch we know exactly how much of the needle still matches, and the haystack pointer never moves backwards. Total time O(n + m). Note that Python's own `str.find` is implemented in C and is faster in practice — the point here is the algorithm.

```python
def str_str(haystack, needle):
    if not needle:
        return 0

    # Build the prefix (border) table for the needle.
    pi = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        while j > 0 and needle[i] != needle[j]:
            j = pi[j - 1]
        if needle[i] == needle[j]:
            j += 1
        pi[i] = j

    # Scan the haystack, never moving backwards.
    j = 0
    for i, ch in enumerate(haystack):
        while j > 0 and ch != needle[j]:
            j = pi[j - 1]
        if ch == needle[j]:
            j += 1
            if j == len(needle):
                return i - len(needle) + 1
    return -1


if __name__ == "__main__":
    print(str_str("sadbutsad", "sad"))        # 0
    print(str_str("leetcode", "leeto"))       # -1
    print(str_str("hello", "ll"))             # 2
    print(str_str("a", "a"))                  # 0
    print("empty needle:", str_str("abc", ""))  # 0
    print("agrees with str.find:",
          all(str_str(h, n) == h.find(n)
              for h, n in [("hello", "ll"), ("aaaaa", "bba"), ("", ""), ("abc", "c")]))
```

Output:

```text
0
-1
2
0
empty needle: 0
agrees with str.find: True
```

**Complexity.** O(n + m) time, O(m) space for the table.

### Example 2 — Longest duplicate substring (Hard)

**Problem.** Find the longest substring that appears at least twice.

**Approach.** Binary search the answer length `L` (if a duplicate of length `L` exists, one of length `L − 1` does too — monotone). For a fixed `L`, slide a rolling hash over the string and store the first start index for each hash; a repeat is a duplicate. Verify with a real substring comparison before returning, so a hash collision cannot produce a wrong answer.

```python
class RollingHash:
    def __init__(self, text, base=911_382_323, mod=972_663_749):
        self.text = text
        self.mod = mod
        self.prefix = [0] * (len(text) + 1)
        self.powers = [1] * (len(text) + 1)
        for i, ch in enumerate(text):
            self.prefix[i + 1] = (self.prefix[i] * base + ord(ch)) % mod
            self.powers[i + 1] = self.powers[i] * base % mod

    def substring_hash(self, left, right):
        length = right - left
        return (self.prefix[right] - self.prefix[left] * self.powers[length]) % self.mod


def longest_duplicate_substring(text):
    n = len(text)
    if n < 2:
        return ""
    hasher = RollingHash(text)

    def duplicate_of_length(length):
        seen = {}
        for i in range(n - length + 1):
            key = hasher.substring_hash(i, i + length)
            if key in seen and text[seen[key]:seen[key] + length] == text[i:i + length]:
                return text[i:i + length]
            seen.setdefault(key, i)
        return None

    best = ""
    lo, hi = 1, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        found = duplicate_of_length(mid)
        if found:
            best = found
            lo = mid + 1
        else:
            hi = mid - 1
    return best


if __name__ == "__main__":
    print("banana ->", repr(longest_duplicate_substring("banana")))
    print("abcd   ->", repr(longest_duplicate_substring("abcd")))
    print("aaaa   ->", repr(longest_duplicate_substring("aaaa")))
    print("ababab ->", repr(longest_duplicate_substring("ababab")))
    print("short  ->", repr(longest_duplicate_substring("a")))
```

Output:

```text
banana -> 'ana'
abcd   -> ''
aaaa   -> 'aaa'
ababab -> 'abab'
short  -> ''
```

**Complexity.** O(n log n) time (binary search × one hash pass) and O(n) space. Suffix-array / suffix-automaton solutions reach O(n), but this version is short enough to write under interview pressure.

### Example 3 — Find all anagrams in a string (Medium)

**Problem.** Find every start index where an anagram of `p` appears in `s`.

**Approach.** Fixed-size sliding window with two frequency counters and a `matches` tally: increment when a character enters and is still needed, decrement when a character leaves and was needed. When `matches == len(p)`, the window is an exact anagram. This is O(n) with O(1) space for a lowercase alphabet — no re-comparison per window.

```python
from collections import Counter


def find_anagrams(s, p):
    if len(p) > len(s):
        return []
    need = Counter(p)
    window = Counter()
    matches = 0
    result = []

    for i, ch in enumerate(s):
        window[ch] += 1
        if window[ch] <= need[ch]:               # this copy is still needed
            matches += 1

        if i >= len(p):                          # slide: drop the leftmost char
            out = s[i - len(p)]
            if window[out] <= need[out]:
                matches -= 1
            window[out] -= 1

        if matches == len(p):
            result.append(i - len(p) + 1)
    return result


if __name__ == "__main__":
    print("find_anagrams('cbaebabacd', 'abc'):", find_anagrams("cbaebabacd", "abc"))
    print("find_anagrams('abab', 'ab'):", find_anagrams("abab", "ab"))
    print("pattern longer than text:", find_anagrams("ab", "abc"))
    print("no matches:", find_anagrams("xyz", "abc"))
```

Output:

```text
find_anagrams('cbaebabacd', 'abc'): [0, 6]
find_anagrams('abab', 'ab'): [0, 1, 2]
pattern longer than text: []
no matches: []
```

**Complexity.** O(n) time and O(k) space, where k is the alphabet size (26 for lowercase). The `matches` counter is the trick that avoids comparing the full window on every step.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [String Matching](https://cses.fi/problemset/task/1753) | CSES | Medium |
| [Finding Borders](https://cses.fi/problemset/task/1732) | CSES | Medium |
| [String Functions](https://codeforces.com/edu/course/2/lesson/3) | Codeforces | Medium |
| [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain kmp prefix values encode longest proper prefix that is also a suffix without notes.
- [ ] Explain z values encode match length between a suffix and the whole string without notes.
- [ ] Explain rolling hash compares substrings after o(n) preprocessing without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
