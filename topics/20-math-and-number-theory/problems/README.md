# Math And Number Theory — problem index

Use this folder for worked solutions in this topic. Each question below links to its canonical prompt; new solutions should follow [`templates/problem-template.md`](../../../templates/problem-template.md) and include executable tests.

| Problem | Level | Core approach | Time | Space |
|---|---|---|---|---|
| [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | Fast exponentiation; handle negative exponent. | O(log n) | O(1) |
| [Sqrt(x)](https://leetcode.com/problems/sqrt-x/) | Easy | Binary search integer square root. | O(log x) | O(1) |
| [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Easy | Use concatenation check and gcd of lengths. | O(n+m) | O(1) |
| [Count Primes](https://leetcode.com/problems/count-primes/) | Medium | Sieve of Eratosthenes. | O(n log log n) | O(n) |
| [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | Cycle detection with set or fast/slow. | O(log n per step) | O(1) or O(k) |
| [Fraction to Recurring Decimal](https://leetcode.com/problems/fraction-to-recurring-decimal/) | Medium | Map remainder to output position to detect cycle. | O(length) | O(length) |
| [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Medium | Prefix sums plus binary search random target. | O(log n) pick | O(n) |
| [Nth Magical Number](https://leetcode.com/problems/nth-magical-number/) | Hard | Binary search answer with lcm inclusion-exclusion. | O(log answer) | O(1) |

## Solution checklist

- [ ] Restatement and constraints
- [ ] Brute-force baseline
- [ ] Optimized approach and invariant
- [ ] Complexity analysis
- [ ] Python implementation
- [ ] Automated tests and edge cases
