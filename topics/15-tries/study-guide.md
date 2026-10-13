# Tries: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

A trie stores shared prefixes as paths. Work is proportional to key length rather than number of stored keys, making prefix lookup and lexicographic pruning natural.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Each node stores child edges and optional terminal/value metadata. |
| 2 | Insert/search/prefix operations are O(L). |
| 3 | Wildcard search branches at wildcard positions. |
| 4 | Trie-guided board DFS prunes prefixes absent from the dictionary. |
| 5 | Binary tries choose opposite bits to maximize XOR. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Many prefix queries | Character trie |
| Dictionary + grid search | Trie-pruned DFS |
| Wildcard word lookup | Trie DFS branching |
| Maximum XOR | Binary trie |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

Insert `cat` and `car`: paths `c → a` are shared, then branch to `t` and `r`. Mark both final nodes terminal; without terminal markers, searching `ca` would incorrectly report a full word.

## Tricks and interview notes

- Store terminal words at nodes to avoid rebuilding paths during DFS.
- Delete found words or prune empty branches to reduce repeated work.
- Use arrays for fixed alphabets and maps for sparse/general alphabets.
- Track prefix aggregates with deltas when keys can be updated.

## Common mistakes

- **Watch for:** Treating every prefix as a complete word.
- **Watch for:** Exponential wildcard search without pruning.
- **Watch for:** Duplicating common prefixes in memory-heavy structures.
- **Watch for:** Forgetting cleanup of board visited state.

## Implementation drills

1. Implement insert/search/startsWith.
2. Add wildcard matching.
3. Build a binary trie for fixed-width integers.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. Build a trie from scratch

A trie (prefix tree) stores characters on edges, so every path from the root
spells a prefix and every node is a prefix shared by all words below it. Insert,
search, and prefix lookups are all O(length of the word) — independent of how
many words are stored.

```python
class TrieNode:
    """One prefix. `children` maps the next character to the next node."""

    def __init__(self):
        self.children = {}          # character -> TrieNode
        self.is_word = False        # does a complete word end here?
        self.prefix_count = 0       # how many words pass through this node
        self.word_count = 0         # how many times THIS word was inserted


class Trie:
    def __init__(self, words=()):
        self.root = TrieNode()
        self.size = 0               # number of distinct words
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        node.prefix_count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.prefix_count += 1
        if not node.is_word:
            self.size += 1
        node.is_word = True
        node.word_count += 1

    def node_for(self, prefix):
        """Node reached by walking `prefix`, or None."""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word):
        """Exact match (not just a prefix)."""
        node = self.node_for(word)
        return node is not None and node.is_word

    def starts_with(self, prefix):
        return self.node_for(prefix) is not None

    def count_prefix(self, prefix):
        """How many inserted words start with `prefix`."""
        node = self.node_for(prefix)
        return 0 if node is None else node.prefix_count

    def words_with_prefix(self, prefix):
        """Every stored word starting with `prefix` (DFS from the prefix node)."""
        node = self.node_for(prefix)
        if node is None:
            return []
        found = []

        def collect(current, word):
            if current.is_word:
                found.append(word)
            for ch in sorted(current.children):       # sorted => deterministic order
                collect(current.children[ch], word + ch)

        collect(node, prefix)
        return found

    def delete(self, word):
        """Remove one occurrence; prune branches that no longer lead anywhere."""
        node = self.node_for(word)
        if node is None or not node.is_word:
            return False
        node.is_word = False
        node.word_count = 0
        self.size -= 1

        path = []
        current = self.root
        current.prefix_count -= 1
        for ch in word:
            path.append((current, ch))
            current = current.children[ch]
            current.prefix_count -= 1
        for parent, ch in reversed(path):             # prune from the leaf upwards
            child = parent.children[ch]
            if child.prefix_count == 0 and not child.is_word:
                del parent.children[ch]
        return True

    def __contains__(self, word):
        return self.search(word)

    def __len__(self):
        return self.size

    def __iter__(self):
        return iter(self.words_with_prefix(""))

    def __repr__(self):
        return f"Trie(size={self.size}, words={sorted(self)})"


if __name__ == "__main__":
    trie = Trie(["app", "apple", "apply", "bat", "ball"])
    print(trie)
    print("search('app'):", trie.search("app"), "| search('ap') (prefix only):", trie.search("ap"))
    print("starts_with('ap'):", trie.starts_with("ap"), "| 'app' in trie:", "app" in trie)
    print("words with prefix 'app':", trie.words_with_prefix("app"))
    print("count_prefix('ap'):", trie.count_prefix("ap"), "| count_prefix('b'):", trie.count_prefix("b"))

    trie.insert("apple")                              # duplicate: counted, not sized twice
    print("after re-inserting 'apple': size =", len(trie), "| count_prefix('apple') =", trie.count_prefix("apple"))

    print("delete('app'):", trie.delete("app"), "->", trie)
    print("delete('apple') once:", trie.delete("apple"), "->", trie)
    print("delete missing:", trie.delete("nope"))
```

Output:

```text
Trie(size=5, words=['app', 'apple', 'apply', 'ball', 'bat'])
search('app'): True | search('ap') (prefix only): False
starts_with('ap'): True | 'app' in trie: True
words with prefix 'app': ['app', 'apple', 'apply']
count_prefix('ap'): 3 | count_prefix('b'): 2
after re-inserting 'apple': size = 5 | count_prefix('apple') = 2
delete('app'): True -> Trie(size=4, words=['apple', 'apply', 'ball', 'bat'])
delete('apple') once: True -> Trie(size=3, words=['apply', 'ball', 'bat'])
delete missing: False
```

**How it works**

- The node is: children map + `is_word` flag. `is_word` is what distinguishes "stored word" from "merely a prefix of another word" — forgetting it is the classic bug.
- `prefix_count` is maintained during insertion and gives "how many words start with this prefix" in O(length) — the autocomplete query, for free.
- `delete` has two jobs: clear the word flag and decrement counters, then prune dead branches from the leaf upwards. Pruning is optional for correctness but keeps memory honest.
- Cost is O(L) per operation where L is the word length, and memory is O(total characters) — better than a hash set when prefixes are shared.

### 2. Trie applications: autocomplete, counting, prefix chains

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.prefix_count = 0
        self.word_count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight=1):
        node = self.root
        node.prefix_count += weight
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.prefix_count += weight
        node.is_word = True
        node.word_count += weight

    def node_for(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


def autocomplete(trie, prefix, k=3):
    """Top-k suggestions for a prefix, most frequent first (ties alphabetical)."""
    start = trie.node_for(prefix)
    if start is None:
        return []
    suggestions = []

    def walk(node, word):
        if node.is_word:
            suggestions.append((-node.word_count, word))
        for ch in sorted(node.children):
            walk(node.children[ch], word + ch)

    walk(start, prefix)
    suggestions.sort()
    return [word for _, word in suggestions[:k]]


def count_nodes(trie):
    """Number of distinct prefixes stored (every node except the root)."""
    total = 0
    stack = [trie.root]
    while stack:
        node = stack.pop()
        total += 1
        stack.extend(node.children.values())
    return total - 1


def longest_word_with_all_prefixes(trie):
    """Longest stored word whose every prefix is also a stored word."""
    best = ""

    def walk(node, word):
        nonlocal best
        if not node.is_word:
            return                             # only continue through real words
        if len(word) > len(best):
            best = word
        for ch in sorted(node.children):
            walk(node.children[ch], word + ch)

    for ch in sorted(trie.root.children):
        walk(trie.root.children[ch], ch)
    return best


if __name__ == "__main__":
    trie = Trie()
    for word, weight in [("python", 5), ("pyramid", 2), ("pythagoras", 7),
                         ("java", 9), ("javascript", 4), ("rust", 1)]:
        trie.insert(word, weight)

    print("autocomplete('py'):", autocomplete(trie, "py"))
    print("autocomplete('ja'):", autocomplete(trie, "ja"))
    print("autocomplete('z') :", autocomplete(trie, "z"))
    print("distinct prefixes stored:", count_nodes(trie))

    word_trie = Trie()
    for word in ("w", "wo", "wor", "worl", "world", "word", "words"):
        word_trie.insert(word)
    print("longest word with every prefix present:", longest_word_with_all_prefixes(word_trie))
```

Output:

```text
autocomplete('py'): ['pythagoras', 'python', 'pyramid']
autocomplete('ja'): ['java', 'javascript']
autocomplete('z') : []
distinct prefixes stored: 31
longest word with every prefix present: words
```

**How it works**

- `autocomplete` collects every word below the prefix node and ranks by frequency. With a huge dictionary you would store the top-k at each node instead of collecting everything — the same trick as caching "top suggestions per prefix".
- `count_nodes` counts distinct prefixes: useful for "how many unique prefixes does this dictionary have" and for sizing the structure.
- `longest_word_with_all_prefixes` prunes at every non-word node, so the DFS only walks chains of real words — a trie version of a DP over prefixes.
- For memory-constrained cases a **radix/compressed trie** (edges hold whole strings) is the standard optimisation; for very large alphabets, swap the dict for a sorted list plus binary search.

## Solved examples

### Example 1 — Word search II (Hard)

**Problem.** Given a letter board and a list of words, find every word that can be
built by walking through adjacent cells without reusing a cell.

**Approach.** Put the words in a trie, then DFS from every cell, but **stop as soon as the path is not a trie prefix** — that prunes whole branches instead of testing every word separately. Store the complete word at the terminal node so the DFS can report it without rebuilding it, and clear the flag once found (or use a set) to avoid duplicates.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None                 # complete word stored at the end node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.word = word


def find_words(board, words):
    trie = Trie()
    for word in words:
        trie.insert(word)

    rows, cols = len(board), len(board[0])
    found = set()

    def dfs(r, c, node):
        child = node.children.get(board[r][c])
        if child is None:                     # dead end: prune
            return
        if child.word:
            found.add(child.word)
        letter = board[r][c]
        board[r][c] = "#"                     # mark visited in place
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, child)
        board[r][c] = letter                  # restore

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root)
    return sorted(found)


if __name__ == "__main__":
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print("found:", find_words(board, words))
    print("board restored:", board[0])

    board2 = [["a", "b"], ["c", "d"]]
    print("no matches:", find_words(board2, ["abcb"]))
```

Output:

```text
found: ['eat', 'oath']
board restored: ['o', 'a', 'a', 'n']
no matches: []
```

**Complexity.** O(rows · cols · 4^L) worst case for the DFS (L = longest word), pruned hard by the trie; building the trie is O(total characters). Much faster than checking each word separately, which is O(words · rows · cols · 4^L).

### Example 2 — Search words with wildcards (Medium)

**Problem.** Design a structure supporting `add_word` and `search`, where
`search` may contain `.` matching any single character.

**Approach.** Trie + DFS: on a normal character follow the single matching child; on `.` try every child. Because `.` forces branching, the search is O(26^L) in the worst case, but ordinary prefixes still prune the tree. Using nested dicts keeps the implementation short.

```python
class WordDictionary:
    """Trie over nested dicts; '#' marks the end of a word."""

    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def search(self, word):
        def dfs(index, node):
            if index == len(word):
                return "#" in node
            ch = word[index]
            if ch == ".":
                return any(dfs(index + 1, child)
                           for key, child in node.items() if key != "#")
            if ch not in node:
                return False
            return dfs(index + 1, node[ch])

        return dfs(0, self.root)


if __name__ == "__main__":
    dictionary = WordDictionary()
    for word in ("bad", "dad", "mad"):
        dictionary.add_word(word)

    for query in ("pad", "bad", ".ad", "b..", "..."):
        print(f"search({query!r}):", dictionary.search(query))
    print("empty dictionary:", WordDictionary().search("a"))
```

Output:

```text
search('pad'): False
search('bad'): True
search('.ad'): True
search('b..'): True
search('...'): True
empty dictionary: False
```

**Complexity.** `add_word` is O(L); `search` is O(L) without wildcards and O( branching^L ) with them. For heavy wildcard use, a per-length set of words is a competitive alternative.

### Example 3 — Replace words with their shortest root (Medium)

**Problem.** Given a list of roots and a sentence, replace each word with the
shortest root that is a prefix of it (or leave it unchanged).

**Approach.** Insert all roots into a trie. For each word, walk character by character and stop at the first node that terminates a root — that is automatically the shortest one, because we stop at the earliest match. If the walk falls off the trie, keep the original word.

```python
def replace_words(roots, sentence):
    trie = {}
    for root in roots:
        node = trie
        for ch in root:
            node = node.setdefault(ch, {})
        node["#"] = root                      # store the root at its end node

    def shortest_root(word):
        node = trie
        for ch in word:
            if "#" in node:                   # a root ends here: shortest match
                return node["#"]
            if ch not in node:
                return word
            node = node[ch]
        return node.get("#", word)

    return " ".join(shortest_root(word) for word in sentence.split())


if __name__ == "__main__":
    roots = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(replace_words(roots, sentence))

    print(replace_words(["a", "b", "c"], "aadsfasf absds bbab cadsfafs"))
    print("no roots match:", replace_words(["x"], "hello world"))
    print("empty sentence:", repr(replace_words(["a"], "")))
```

Output:

```text
the cat was rat by the bat
a a b c
no roots match: hello world
empty sentence: ''
```

**Complexity.** O(total characters in roots + total characters in sentence). Checking `"#" in node` **before** consuming the next character is what guarantees the shortest root wins.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Contacts](https://www.hackerrank.com/challenges/contacts/problem) | HackerRank | Medium |
| [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | LeetCode | Medium |
| [Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/) | LeetCode | Medium |
| [Prefix and Suffix Search](https://leetcode.com/problems/prefix-and-suffix-search/) | LeetCode | Hard |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain each node stores child edges and optional terminal/value metadata without notes.
- [ ] Explain insert/search/prefix operations are o(l) without notes.
- [ ] Explain wildcard search branches at wildcard positions without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
