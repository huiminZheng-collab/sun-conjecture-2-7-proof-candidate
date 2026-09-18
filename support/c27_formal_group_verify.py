"""Exact checks for the formal-group route to Z.-H. Sun's Conjecture 2.7.

Let
    ell(v) = sum_{n>=0} G_n v^(2n+1)/(2n+1),
    v(q)   = sqrt(lambda(4z))/4,  q = exp(2*pi*i*z).

The proof route uses
    q d/dq ell(v(q)) = eta(4z)^6.

This program verifies the identity by exact rational power-series arithmetic,
checks integrality of v(q), and checks the CM formula for prime coefficients
of eta(4z)^6.  It is an error detector, not a substitute for the modular-form
and formal-group arguments in c27_formal_group_proof.md.
"""

from fractions import Fraction
from math import comb


N = 100


def mul(a, b, n=N):
    out = [Fraction(0) for _ in range(n)]
    for i, ai in enumerate(a[:n]):
        if not ai:
            continue
        for j, bj in enumerate(b[: n - i]):
            if bj:
                out[i + j] += ai * bj
    return out


def inv(a, n=N):
    assert a[0] != 0
    out = [Fraction(0) for _ in range(n)]
    out[0] = Fraction(1) / a[0]
    for k in range(1, n):
        out[k] = -sum(a[j] * out[k - j] for j in range(1, k + 1)) / a[0]
    return out


def pow_series(a, exponent, n=N):
    if exponent < 0:
        return pow_series(inv(a, n), -exponent, n)
    out = [Fraction(0) for _ in range(n)]
    out[0] = 1
    base = a[:n]
    e = exponent
    while e:
        if e & 1:
            out = mul(out, base, n)
        base = mul(base, base, n)
        e //= 2
    return out


def factor(sign, step, exponent, n=N):
    """Return (1 + sign*q^step)^exponent."""
    a = [Fraction(0) for _ in range(n)]
    a[0] = Fraction(1)
    if step < n:
        a[step] = sign
    return pow_series(a, exponent, n)


def G_values(count):
    values = [1, 12]
    for n in range(1, count - 1):
        numerator = (32 * n * (n + 1) + 12) * values[n]
        numerator -= 256 * n * n * values[n - 1]
        denominator = (n + 1) ** 2
        assert numerator % denominator == 0
        values.append(numerator // denominator)
    return values[:count]


def v_series(n=N):
    # theta_2(4z)^2/(4 theta_3(4z)^2)
    # = q prod_{j>=1} ((1+q^(4j))/(1+q^(4j-2)))^4.
    product = [Fraction(0) for _ in range(n)]
    product[0] = Fraction(1)
    j = 1
    while 4 * j - 2 < n:
        product = mul(product, factor(1, 4 * j, 4, n), n)
        product = mul(product, factor(1, 4 * j - 2, -4, n), n)
        j += 1
    out = [Fraction(0) for _ in range(n)]
    for k in range(1, n):
        out[k] = product[k - 1]
    return out


def eta4_six(n=N):
    # eta(4z)^6 = q prod_{j>=1}(1-q^(4j))^6.
    product = [Fraction(0) for _ in range(n)]
    product[0] = Fraction(1)
    j = 1
    while 4 * j < n:
        product = mul(product, factor(-1, 4 * j, 6, n), n)
        j += 1
    out = [Fraction(0) for _ in range(n)]
    for k in range(1, n):
        out[k] = product[k - 1]
    return out


def compose_logarithm(v, n=N):
    g = G_values((n + 1) // 2 + 1)
    out = [Fraction(0) for _ in range(n)]
    power = v[:]
    v2 = mul(v, v, n)
    for k, gk in enumerate(g):
        degree = 2 * k + 1
        if degree >= n:
            break
        scale = Fraction(gk, degree)
        for j in range(n):
            out[j] += scale * power[j]
        power = mul(power, v2, n)
    return out


def q_derivative(a):
    return [Fraction(k) * a[k] for k in range(len(a))]


def x_for_split_prime(p):
    for y in range(1, int((p / 4) ** 0.5) + 1):
        x2 = p - 4 * y * y
        x = int(x2**0.5)
        if x * x == x2:
            return x
    raise AssertionError(f"no x^2+4y^2 representation for p={p}")


def primes_below(n):
    out = []
    for m in range(2, n):
        if all(m % d for d in range(2, int(m**0.5) + 1)):
            out.append(m)
    return out


v = v_series()
assert v[1] == 1
assert all(c.denominator == 1 for c in v)
assert all(v[k] == 0 for k in range(0, N, 2))

ell_of_v = compose_logarithm(v)
lhs = q_derivative(ell_of_v)
rhs = eta4_six()
assert lhs == rhs

eta_coeff = [int(c) for c in rhs]
for p in primes_below(N):
    if p == 2:
        continue
    expected = 0 if p % 4 == 3 else 4 * x_for_split_prime(p) ** 2 - 2 * p
    assert eta_coeff[p] == expected, (p, eta_coeff[p], expected)

print(f"v(q) integral and odd through q^{N-1}")
print(f"q*d/dq ell(v(q)) = eta(4z)^6 through q^{N-1}")
print(f"CM prime-coefficient formula checked for odd primes below {N}")
print("first v coefficients:", [int(c) for c in v[:16]])
print("first eta coefficients:", eta_coeff[:32])
