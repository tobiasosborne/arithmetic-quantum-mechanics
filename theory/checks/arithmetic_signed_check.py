#!/usr/bin/env python3
"""Exact bounded evidence for LIM-SIGNED; this is not its general proof."""
import argparse
from fractions import Fraction
from math import comb, gcd, prod


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def primes(n):
    out = []
    for d in range(2, n + 1):
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
    return out


def mu(n):
    ps = primes(n)
    return 0 if any(n % (p * p) == 0 for p in ps) else (-1) ** len(ps)


def candidate(d, internal):
    out = {}

    def add(e, a):
        out[e] = out.get(e, 0) + a

    if d % 2:
        if not internal:
            for e in divisors(d):
                add(e, mu(d // e))
            if d == 1:
                add(0, -1)
    else:
        m, scale = d, 1
        while m % 2 == 0:
            m //= 2
            scale *= 2
        scale //= 2
        for e in divisors(m):
            a, j = mu(m // e), scale * e
            if internal:
                add(j, a)
                add(0, -a)
            else:
                add(2 * j, a)
                add(j, -2 * a)
                add(0, a)
    return out


def evaluate(poly, t):
    return sum(a * t ** e for e, a in poly.items())


def check(ok, gate, detail):
    if not ok:
        raise AssertionError(f"{gate}: {detail}")


def field_census(p, modulus, red):
    r = len(modulus) - 1
    q = p ** r
    digits = [tuple((x // p ** j) % p for j in range(r)) for x in range(q)]
    encode = lambda cs: sum(a * p ** j for j, a in enumerate(cs))

    def mul(x, y):
        cs = [0] * (2 * r - 1)
        for i, a in enumerate(digits[x]):
            for j, b in enumerate(digits[y]):
                cs[i + j] += a * b
        for j in range(2 * r - 2, r - 1, -1):
            for i in range(r):
                cs[j - r + i] -= cs[j] * modulus[i]
        return encode([a % p for a in cs[:r]])

    def power(x, n):
        out = 1
        while n:
            if n % 2:
                out = mul(out, x)
            x, n = mul(x, x), n // 2
        return out

    for x in range(1, q):
        check(power(x, q - 1) == 1, "S1", "quotient field inverse")
    counts = {d: [0, 0] for d in divisors(r)}
    for x in range(1, q):
        orbit, y = [x], power(x, p)
        while y != x:
            orbit.append(y)
            check(len(orbit) <= r, "S1", "Frobenius period bound")
            y = power(y, p)
        negative = x if red else encode([(-a) % p for a in digits[x]])
        internal = negative in orbit
        counts[len(orbit)][0 if internal else 1] += 1
    for d, pair in counts.items():
        expected = [evaluate(candidate(d, inside), p) for inside in (True, False)]
        check(pair == expected, "S1", (p, r, d, pair, expected))
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--red-sign', action='store_true', help='replace odd-characteristic negation by identity')
    parser.add_argument('--red-order', action='store_true', help='falsely give even external sectors first order')
    args = parser.parse_args()
    try:
        for p, mod in [(3, [0, 1]), (3, [1, 0, 1]), (3, [1, 2, 0, 1]),
                       (3, [2, 1, 0, 0, 1]), (5, [0, 1]), (5, [2, 0, 1])]:
            print(f"S1 F_{p}^{len(mod)-1}:", field_census(p, mod, args.red_sign))
        for d in range(1, 49):
            for inside in (True, False):
                poly = candidate(d, inside)
                if inside and d % 2:
                    check(not poly, 'S2', 'odd internal count is zero')
                    continue
                coeff = [sum(a * comb(e, j) for e, a in poly.items() if e >= j) for j in range(3)]
                if d % 2 or inside:
                    order, leading = 1, sum(gcd(x, d) == 1 for x in range(1, d + 1))
                else:
                    m, scale = d, 1
                    while m % 2 == 0:
                        m //= 2
                        scale *= 2
                    order = 1 if args.red_order else 2
                    leading = Fraction((scale // 2) ** 2 * m * m) * prod(1 - Fraction(1, p * p) for p in primes(m))
                check(all(coeff[j] == 0 for j in range(order)) and coeff[order] == leading,
                      'S2', (d, inside, order, coeff, leading))
                for t in (Fraction(1001, 1000), Fraction(3, 2), Fraction(2)):
                    check(evaluate(poly, t) > 0, 'S2', 'positive sampled count polynomial')
        print('PASS S1--S2: exact finite evidence; LIM-SIGNED remains CONJECTURE.')
        return 0
    except AssertionError as err:
        print('FAIL', err)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
