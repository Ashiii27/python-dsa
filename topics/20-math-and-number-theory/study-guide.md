# Math and Number Theory: Complete Study Guide

> Start with the [topic overview](README.md), use the [problem index](problems/README.md), and revise with the repository-wide [flashcards](../../docs/revision-flashcards.md) and [visual pattern guide](../../docs/visual-guides.md).

## Mental model

Replace simulation with identities, divisibility structure, modular arithmetic, or monotonic numerical search. State overflow and precision assumptions even though Python integers are unbounded.

## Learning objectives

By the end of this topic, you should be able to explain each concept, recognize its problem signals, implement the core operations without copying, prove the main invariant, and select an approach from constraints.

## Core concepts

| # | What to know |
|---:|---|
| 1 | Euclid computes gcd via repeated remainder; lcm(a,b)=abs(a/gcd(a,b)*b). |
| 2 | Sieve marks composites to list primes up to n. |
| 3 | Fast exponentiation squares the base and halves the exponent. |
| 4 | Modular arithmetic keeps values bounded and supports congruence reasoning. |
| 5 | Remainder states detect cycles in recurring decimals. |

## Pattern recognition

| Problem signal | First tool to consider |
|---|---|
| Repeated multiplication | Binary exponentiation |
| Many primality queries up to n | Sieve |
| Repeating division state | Remainder map |
| Integer root/answer | Binary search |

These are starting hypotheses, not automatic rules. Verify the required invariant and complexity before committing to a pattern.

## Worked example

To compute `3^13`, read `13 = 1101₂`. Multiply the answer by current base when the low bit is 1, square the base each step, and shift the exponent. Only O(log 13) multiplications are needed.

## Tricks and interview notes

- Reduce before multiplying in fixed-width languages.
- Start sieve crossing-out at p²; smaller composites were handled earlier.
- Normalize signs in gcd/lcm APIs.
- Use `math.isqrt` for exact integer square roots in production Python.

## Common mistakes

- **Watch for:** Using floating point for exact divisibility.
- **Watch for:** Forgetting zero and negative exponent cases.
- **Watch for:** Marking 1 as prime.
- **Watch for:** Using `(a*b)//gcd` where fixed-width overflow is possible.

## Implementation drills

1. Implement gcd and extended gcd.
2. Write a prime sieve and factor numbers using its primes.
3. Implement modular binary exponentiation.

After each drill, write its invariant and test minimum input, duplicates, impossible answers, and maximum constraints where relevant.

## Additional practice ladder

These supplement the questions in [`problems/README.md`](problems/README.md) and intentionally mix platforms.

| Problem | Platform | Suggested level |
|---|---|---|
| [Common Divisors](https://cses.fi/problemset/task/1081) | CSES | Medium |
| [Exponentiation](https://cses.fi/problemset/task/1095) | CSES | Easy |
| [Prime Multiples](https://cses.fi/problemset/task/2185) | CSES | Hard |
| [Ugly Number II](https://leetcode.com/problems/ugly-number-ii/) | LeetCode | Medium |

Platform difficulty labels are approximate; use the problem constraints as the final guide.

## Active-recall checkpoint

- [ ] Explain euclid computes gcd via repeated remainder; lcm(a,b)=abs(a/gcd(a,b)*b) without notes.
- [ ] Explain sieve marks composites to list primes up to n without notes.
- [ ] Explain fast exponentiation squares the base and halves the exponent without notes.
- [ ] Derive the worked example from a blank page.
- [ ] Name two common bugs and the test that exposes each one.
- [ ] State the time and space complexity of the canonical implementation.

## Suggested study session

1. **20 min:** read the mental model and core concepts.
2. **20 min:** trace the worked example by hand.
3. **30 min:** complete one implementation drill without notes.
4. **45–90 min:** solve one practice problem and document mistakes.
5. **10 min:** answer the active-recall checkpoint and schedule a redo.
