# Interview Playbook

This is how to behave in a 45-60 minute DSA interview.

---

## 45-minute timeline

| Time | What to do |
|---:|---|
| 0-5 min | Clarify problem, constraints, examples |
| 5-10 min | Explain brute force and bottleneck |
| 10-18 min | Derive optimized approach and complexity |
| 18-32 min | Code cleanly |
| 32-40 min | Test edge cases and fix bugs |
| 40-45 min | Discuss complexity, alternatives, follow-ups |

If stuck, say what you know:

```text
The brute force is O(...). The repeated work is (...). This looks like a sliding window/prefix sum/graph shortest path because (...). I will try to maintain the invariant that (...).
```

---

## Communication rules

Do:

- Think out loud.
- State assumptions.
- Name the pattern.
- Define invariants.
- Mention trade-offs.
- Test before the interviewer asks.

Avoid:

- Silent coding for 20 minutes.
- Jumping directly to code without approach.
- Saying “I know this problem” and reciting memorized code.
- Ignoring constraints.
- Pretending a bug is impossible.

---

## What top-tier interviewers look for

They usually evaluate:

1. **Problem understanding**: can you clarify ambiguity?
2. **Algorithm design**: can you move from brute force to optimal?
3. **Correctness reasoning**: do you understand why it works?
4. **Code quality**: can you write clean, testable code?
5. **Complexity analysis**: can you reason honestly?
6. **Debugging**: can you find mistakes using examples?
7. **Adaptability**: can you handle follow-ups?

---

## Edge-case checklist

- empty list/string
- one element
- two elements
- all duplicates
- no valid answer
- multiple valid answers
- negative values
- zero values
- very large values
- sorted input
- reverse sorted input
- disconnected graph
- cycle in graph
- skewed tree
- duplicate keys

---

## Follow-up readiness

Common follow-ups:

- Can you reduce memory?
- Can you handle streaming input?
- What if input is too large for memory?
- What if updates are added?
- What if values are negative?
- What if the graph is weighted?
- Can you return the actual path, not just length?
- Can you solve it without modifying input?

Prepare by knowing nearby patterns:

- Static range sums -> prefix sums
- Range sums with point updates -> Fenwick tree
- Range min/max with updates -> segment tree
- Range updates -> difference array or lazy segment tree

---

## Mock interview routine

1. Pick one medium or hard problem at random.
2. Set a 45-minute timer.
3. Record yourself explaining.
4. After finishing, write a short postmortem:
   - where did I hesitate?
   - what pattern did I miss?
   - what bug appeared?
   - what follow-up would make this harder?
5. Redo the problem one week later.
