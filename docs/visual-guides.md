# Visual DSA Pattern Guide

These Mermaid diagrams are designed for quick recall. GitHub renders them directly; redraw them by hand when revising.

## Two pointers

```mermaid
flowchart LR
    L[Left pointer] --> M[Unexplored range]
    M --> R[Right pointer]
    C{Compare / evaluate} -->|Need larger| L2[Move left right]
    C -->|Need smaller| R2[Move right left]
    C -->|Match| A[Record answer]
```

**Invariant:** everything outside the pointers has been processed or proved unable to improve the answer.

## Sliding window

```mermaid
flowchart LR
    E[Expand right] --> U[Update counts/state]
    U --> V{Window valid?}
    V -->|No| E
    V -->|Yes| A[Update answer]
    A --> S[Shrink left]
    S --> U
```

**Recognition signal:** a contiguous range and a constraint that can be maintained incrementally.

## Prefix sums

```mermaid
flowchart LR
    A[nums 0..l-1] --> P1[prefix l]
    B[nums 0..r] --> P2[prefix r+1]
    P2 --> D[range sum = prefix r+1 - prefix l]
    P1 --> D
```

For target-sum subarrays, store counts of earlier prefixes: `current_prefix - earlier_prefix = target`.

## Monotonic stack

```mermaid
flowchart TD
    N[Read next value] --> C{Breaks stack order?}
    C -->|Yes| P[Pop; next boundary found]
    P --> C
    C -->|No| Q[Push index]
    Q --> N
```

Each index is pushed and popped at most once, which explains the linear-time bound.

## Binary search on answer

```mermaid
flowchart LR
    L[Impossible / low] --> M[Test midpoint]
    M --> F{Feasible?}
    F -->|Yes| H[Keep midpoint and lower half]
    F -->|No| G[Discard lower half]
    H --> M
    G --> M
```

First prove the predicate is monotonic; then choose whether you need the first true or last false boundary.

## Tree DFS return values

```mermaid
flowchart BT
    LL[Left result] --> N[Combine at node]
    RR[Right result] --> N
    N --> G[Update global candidate]
    N --> P[Return one-branch result to parent]
```

Separate the value a parent may extend from the candidate that is complete at the current node.

## BFS levels and multi-source BFS

```mermaid
flowchart LR
    S1[Source 1] --> Q[Queue at distance 0]
    S2[Source 2] --> Q
    S3[Source 3] --> Q
    Q --> L1[Distance 1 layer]
    L1 --> L2[Distance 2 layer]
```

Mark nodes visited when enqueuing, not when dequeuing, to avoid duplicate work.

## Topological sort

```mermaid
flowchart LR
    E[Build indegrees] --> Z[Queue all indegree-zero nodes]
    Z --> R[Remove node]
    R --> D[Decrement neighbors]
    D --> Z
    R --> C{Processed all nodes?}
    C -->|Yes| O[Valid order]
    C -->|No| X[Cycle exists]
```

## Backtracking decision tree

```mermaid
flowchart TD
    S[Choose state] --> C1[Choice A]
    S --> C2[Choice B]
    C1 --> R1[Recurse]
    C2 --> R2[Recurse]
    R1 --> U1[Undo choice A]
    R2 --> U2[Undo choice B]
```

The state must be restored exactly before exploring the next sibling.

## Dynamic programming workflow

```mermaid
flowchart LR
    S[Define state] --> T[Write transition]
    T --> B[Set base cases]
    B --> O[Choose evaluation order]
    O --> X[Compute answer]
    X --> M[Optimize memory if dependencies allow]
```

## Union Find

```mermaid
flowchart LR
    A[Node] --> F[Find root]
    B[Node] --> G[Find root]
    F --> C{Same root?}
    G --> C
    C -->|Yes| Y[Already connected / cycle]
    C -->|No| U[Union by size or rank]
```

Path compression flattens find paths; union by size prevents tall trees.

## Heap for top-k

```mermaid
flowchart LR
    N[Read item] --> P[Push into min-heap]
    P --> S{Size greater than k?}
    S -->|Yes| X[Pop smallest]
    S -->|No| N
    X --> N
```

The heap contains the best `k` items from the processed prefix.
