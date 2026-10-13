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

## Python implementation (build it from scratch)

This is the reference code for the drills above: every block is complete and
runnable (copy it into a file or a REPL). The output shown under each block is
the real output of that exact code — regenerate it any time with
`python3 tools/check_snippets.py --fill`.

### 1. GCD, primes, and modular arithmetic

These five tools cover most number-theory interview problems: Euclid's GCD,
fast modular exponentiation, primality by trial division, the sieve, and prime
factorisation.

```python
def gcd(a, b):
    """Euclid: gcd(a, b) = gcd(b, a mod b)."""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0


def extended_gcd(a, b):
    """Return (g, x, y) such that a*x + b*y = g = gcd(a, b)."""
    if b == 0:
        return abs(a), (1 if a >= 0 else -1), 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def pow_mod(base, exponent, mod):
    """Fast exponentiation: O(log exponent) by squaring."""
    result = 1
    base %= mod
    while exponent:
        if exponent & 1:
            result = result * base % mod
        base = base * base % mod
        exponent >>= 1
    return result


def mod_inverse(a, mod):
    """Inverse of a modulo `mod` (requires gcd(a, mod) == 1)."""
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError(f"no inverse: gcd({a}, {mod}) = {g}")
    return x % mod


def is_prime(n):
    """Trial division up to sqrt(n): O(sqrt n)."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def sieve(limit):
    """All primes <= limit. O(n log log n)."""
    if limit < 2:
        return []
    is_composite = [False] * (limit + 1)
    primes = []
    for number in range(2, limit + 1):
        if not is_composite[number]:
            primes.append(number)
            for multiple in range(number * number, limit + 1, number):
                is_composite[multiple] = True
    return primes


def prime_factors(n):
    """Prime factorisation with multiplicity; O(sqrt n)."""
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1 if divisor == 2 else 2       # 2, then odd numbers only
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    print("gcd(48, 18):", gcd(48, 18), "| lcm(4, 6):", lcm(4, 6))
    g, x, y = extended_gcd(35, 15)
    print(f"extended_gcd(35, 15) -> g={g}, x={x}, y={y} (35*{x} + 15*{y} = {35*x + 15*y})")

    print("pow_mod(2, 10, 1000):", pow_mod(2, 10, 1000))
    print("pow_mod(3, 5, 7):", pow_mod(3, 5, 7), "| built-in pow agrees:", pow(3, 5, 7))
    print("mod_inverse(3, 11):", mod_inverse(3, 11), "| check:", 3 * mod_inverse(3, 11) % 11)

    print("primes up to 30:", sieve(30))
    print("is_prime:", [(n, is_prime(n)) for n in (0, 1, 2, 17, 25, 97)])
    print("prime_factors(360):", prime_factors(360))
    print("prime_factors(97):", prime_factors(97))
    print("prime_factors(1):", prime_factors(1))
```

Output:

```text
gcd(48, 18): 6 | lcm(4, 6): 12
extended_gcd(35, 15) -> g=5, x=1, y=-2 (35*1 + 15*-2 = 5)
pow_mod(2, 10, 1000): 24
pow_mod(3, 5, 7): 5 | built-in pow agrees: 5
mod_inverse(3, 11): 4 | check: 1
primes up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
is_prime: [(0, False), (1, False), (2, True), (17, True), (25, False), (97, True)]
prime_factors(360): [2, 2, 2, 3, 3, 5]
prime_factors(97): [97]
prime_factors(1): []
```

**How it works**

- Euclid's algorithm shrinks the problem by a modulo each step, so it is O(log min(a, b)) — never write a loop up to `min(a, b)`.
- `pow_mod` squares the base and halves the exponent: 10¹⁸ multiplications would be impossible, but ~60 iterations are free. Python's built-in `pow(a, e, mod)` does the same in C — use it in production code.
- A modular inverse exists only when `gcd(a, mod) = 1`. For a **prime** modulus you can use Fermat's little theorem: `a^(mod−2) mod mod` — that is `pow_mod(a, mod - 2, mod)`.
- The sieve marks composites starting from `p²` (smaller multiples were already marked by smaller primes) — that detail is what keeps it near-linear.

### 2. Combinatorics and matrix exponentiation

Counting answers modulo a prime, and collapsing a linear recurrence to O(log n)
with matrix powers.

```python
MOD = 1_000_000_007


def build_factorials(limit, mod=MOD):
    """factorials[i] and inverse factorials[i], so nCr is O(1) afterwards."""
    factorials = [1] * (limit + 1)
    for i in range(1, limit + 1):
        factorials[i] = factorials[i - 1] * i % mod
    inverses = [1] * (limit + 1)
    inverses[limit] = pow(factorials[limit], mod - 2, mod)      # Fermat inverse
    for i in range(limit, 0, -1):
        inverses[i - 1] = inverses[i] * i % mod
    return factorials, inverses


def n_choose_r(n, r, factorials=None, inverses=None, mod=MOD):
    """nCr mod p: n! / (r! (n-r)!) using modular inverses (never real division)."""
    if r < 0 or r > n:
        return 0
    if factorials is None:
        factorials, inverses = build_factorials(n, mod)
    return factorials[n] * inverses[r] % mod * inverses[n - r] % mod


def pascal_row(n, mod=MOD):
    """Row n of Pascal's triangle built in place: O(n)."""
    row = [1] * (n + 1)
    for i in range(1, n):
        row[i] = row[i - 1] * (n - i + 1) % mod * pow(i, mod - 2, mod) % mod
    return row


def matrix_multiply(a, b, mod=None):
    """Multiply two square matrices."""
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % mod if mod \
                        else result[i][j] + a[i][k] * b[k][j]
    return result


def matrix_power(matrix, exponent, mod=None):
    """matrix^exponent by repeated squaring: O(n^3 log exponent)."""
    n = len(matrix)
    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]   # identity
    base = [row[:] for row in matrix]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base, mod)
        base = matrix_multiply(base, base, mod)
        exponent >>= 1
    return result


def fibonacci(n, mod=None):
    """n-th Fibonacci in O(log n): [[1,1],[1,0]]^n."""
    if n == 0:
        return 0
    powered = matrix_power([[1, 1], [1, 0]], n, mod)
    return powered[0][1] if not mod else powered[0][1] % mod


if __name__ == "__main__":
    print("10 choose 3:", n_choose_r(10, 3))
    print("52 choose 5 mod 1e9+7:", n_choose_r(52, 5))
    print("out of range (3 choose 5):", n_choose_r(3, 5))
    print("pascal row 5:", pascal_row(5))

    print("fibonacci(10):", fibonacci(10))
    print("fibonacci(50):", fibonacci(50))
    print("fibonacci(90) mod 1e9+7:", fibonacci(90, MOD))
    print("identity check:", matrix_power([[2, 0], [0, 2]], 0))
```

Output:

```text
10 choose 3: 120
52 choose 5 mod 1e9+7: 2598960
out of range (3 choose 5): 0
pascal row 5: [1, 5, 10, 10, 5, 1]
fibonacci(10): 55
fibonacci(50): 12586269025
fibonacci(90) mod 1e9+7: 210345902
identity check: [[1, 0], [0, 1]]
```

**How it works**

- Modular arithmetic has no division: dividing by `x` means multiplying by `x^(mod−2)` when the modulus is prime (Fermat). Precomputing factorials **and** inverse factorials turns every `nCr` into three multiplications.
- `pascal_row` builds each entry from the previous one with the ratio `(n − i + 1) / i` — the standard O(n) trick that avoids factorial tables entirely.
- Matrix exponentiation applies to any linear recurrence: encode the state as a vector, evolve it with a transition matrix, and raise that matrix to the power `n` in O(log n). Fibonacci is the canonical example; tribonacci, "climb stairs with k steps", and counting paths in a graph all reduce to it.

## Solved examples

### Example 1 — Count primes below n (Easy)

**Problem.** Count the primes strictly less than `n`.

**Approach.** Testing each candidate independently is O(n √n). The sieve of Eratosthenes marks multiples of every prime once, giving O(n log log n). Starting the marking loop at `p²` is safe because any smaller multiple of `p` has a smaller prime factor and was already marked.

```python
def count_primes(n):
    if n < 3:
        return 0
    is_composite = [False] * n
    count = 0
    for number in range(2, n):
        if is_composite[number]:
            continue
        count += 1
        for multiple in range(number * number, n, number):
            is_composite[multiple] = True
    return count


def primes_up_to(n):
    """The primes themselves, using the same sieve."""
    if n < 2:
        return []
    is_composite = [False] * n
    primes = []
    for number in range(2, n):
        if not is_composite[number]:
            primes.append(number)
            for multiple in range(number * number, n, number):
                is_composite[multiple] = True
    return primes


if __name__ == "__main__":
    print("count_primes(10):", count_primes(10), "| primes:", primes_up_to(10))
    print("count_primes(2):", count_primes(2))
    print("count_primes(100):", count_primes(100))
    print("count_primes(1_000):", count_primes(1_000))
```

Output:

```text
count_primes(10): 4 | primes: [2, 3, 5, 7]
count_primes(2): 0
count_primes(100): 25
count_primes(1_000): 168
```

**Complexity.** O(n log log n) time and O(n) space. A **linear** sieve (mark each composite once via its smallest prime factor) is the usual follow-up; the segmented sieve handles ranges far above 10⁶.

### Example 2 — Fast exponentiation, Pow(x, n) (Medium)

**Problem.** Compute `x^n` including negative exponents, in O(log n).

**Approach.** Binary exponentiation: square the base, halve the exponent, and multiply into the result whenever the current bit of the exponent is 1. A negative exponent means compute `x^|n|` and take the reciprocal. This is also the modular version used everywhere in combinatorics and crypto.

```python
def my_pow(x, n):
    """x ** n in O(log |n|)."""
    if n < 0:
        return 1.0 / my_pow(x, -n)
    result = 1.0
    base = x
    exponent = n
    while exponent:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    return result


def pow_mod(base, exponent, mod):
    """Same loop, reduced modulo `mod` at every step."""
    result = 1
    base %= mod
    while exponent:
        if exponent & 1:
            result = result * base % mod
        base = base * base % mod
        exponent >>= 1
    return result


if __name__ == "__main__":
    print("my_pow(2.0, 10):", my_pow(2.0, 10))
    print("my_pow(2.0, -2):", my_pow(2.0, -2))
    print("my_pow(2.1, 3):", round(my_pow(2.1, 3), 5))
    print("my_pow(5.0, 0):", my_pow(5.0, 0))
    print("pow_mod(2, 100, 1_000_000_007):", pow_mod(2, 100, 1_000_000_007))
    print("built-in agrees:", pow(2, 100, 1_000_000_007) == pow_mod(2, 100, 1_000_000_007))
```

Output:

```text
my_pow(2.0, 10): 1024.0
my_pow(2.0, -2): 0.25
my_pow(2.1, 3): 9.261
my_pow(5.0, 0): 1.0
pow_mod(2, 100, 1_000_000_007): 976371285
built-in agrees: True
```

**Complexity.** O(log n) time and O(1) space, versus O(n) for repeated multiplication. Taking the modulus at every step (not just at the end) is what keeps Python integers small and the loop fast.

### Example 3 — Trailing zeroes and factor-of-five counting (Medium)

**Problem.** How many trailing zeroes does `n!` have? And how many times does a
prime `p` divide `n!`?

**Approach.** Each trailing zero is a factor of 10 = 2 · 5, and factorials contain far more 2s than 5s, so the answer is the number of 5s in `n!`. Legendre's formula sums `⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + …` — count multiples of p, then of p² (which contribute a second factor), and so on. O(log n) instead of computing the factorial.

```python
def trailing_zeroes(n):
    """Number of trailing zeroes in n! (factors of 5)."""
    count = 0
    power = 5
    while power <= n:
        count += n // power
        power *= 5
    return count


def exponent_of_prime_in_factorial(n, p):
    """Legendre's formula: how many times does p divide n! ?"""
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count


def factor_of_sum_zeros(n, p):
    """Trailing zeroes of n! in base p (how many times p divides n!)."""
    return exponent_of_prime_in_factorial(n, p)


if __name__ == "__main__":
    for n in (5, 10, 25, 100):
        print(f"{n}! trailing zeroes: {trailing_zeroes(n)}")
    print("5s in 100!:", exponent_of_prime_in_factorial(100, 5))
    print("2s in 100!:", exponent_of_prime_in_factorial(100, 2))
    print("zeroes of 10! in base 2:", factor_of_sum_zeros(10, 2))
    print("0!:", trailing_zeroes(0))
```

Output:

```text
5! trailing zeroes: 1
10! trailing zeroes: 2
25! trailing zeroes: 6
100! trailing zeroes: 24
5s in 100!: 24
2s in 100!: 97
zeroes of 10! in base 2: 8
0!: 0
```

**Complexity.** O(log_p n) time and O(1) space. Counting factors instead of computing giant numbers is the recurring theme of number-theory problems: reduce the question to a prime's exponent.

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
