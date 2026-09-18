# Math and Number Theory

**Level:** Core to Advanced

Use arithmetic, modular reasoning, primes, gcd, and combinatorics in coding problems.

---

## What you must learn

- GCD and Euclid algorithm
- LCM
- Fast exponentiation
- Modulo arithmetic
- Sieve of Eratosthenes
- Prime factorization
- Combinatorics basics
- Randomized probability patterns

---

## Core patterns and approaches

- Use gcd for ratios, cycles, and divisibility
- Use fast power for large exponents
- Use modulo at every multiplication/addition to avoid huge numbers
- Use sieve for many prime queries
- Use prefix probabilities or binary search for weighted random pick

---

## Python notes

- Start with a brute-force idea, then identify the repeated work.
- State the invariant before coding.
- Write edge cases before submitting.
- Explain time and space complexity in terms of input size.


---

## Canonical template

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def pow_mod(a, e, mod):
    ans = 1
    a %= mod
    while e:
        if e & 1: ans = ans * a % mod
        a = a * a % mod; e >>= 1
    return ans
```

---

## Top interview questions and approaches

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| Pow(x, n) | Medium | Fast exponentiation; handle negative exponent. | O(log n) | O(1) |
| Sqrt(x) | Easy | Binary search integer square root. | O(log x) | O(1) |
| Greatest Common Divisor of Strings | Easy | Use concatenation check and gcd of lengths. | O(n+m) | O(1) |
| Count Primes | Medium | Sieve of Eratosthenes. | O(n log log n) | O(n) |
| Happy Number | Easy | Cycle detection with set or fast/slow. | O(log n per step) | O(1) or O(k) |
| Fraction to Recurring Decimal | Medium | Map remainder to output position to detect cycle. | O(length) | O(length) |
| Random Pick with Weight | Medium | Prefix sums plus binary search random target. | O(log n) pick | O(n) |
| Nth Magical Number | Hard | Binary search answer with lcm inclusion-exclusion. | O(log answer) | O(1) |

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
