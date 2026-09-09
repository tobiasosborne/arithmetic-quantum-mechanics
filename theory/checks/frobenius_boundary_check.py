#!/usr/bin/env python3
"""Exact finite falsifiers for D1331--D1334 and the FRL sketches."""

import argparse
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm, prod

import numpy as np


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def primes(n):
    out = []
    for a in range(2, n + 1):
        if n % a == 0:
            out.append(a)
            while n % a == 0:
                n //= a
    return out


def mobius(n):
    ps = primes(n)
    return 0 if any(n % (p * p) == 0 for p in ps) else (-1) ** len(ps)


def totient(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def count_poly(d, t, bad=False):
    return sum(mobius(d // e) * t ** e for e in divisors(d)) + int(bad and d == 2)


def weight(r, d, t, bad=False):
    if t == 1:
        return F(d if bad else totient(d), r - 1)
    return count_poly(d, t) / (t ** r - t)


def check(ok, name, detail):
    if not ok:
        raise AssertionError(f"{name}: {detail}")


def mm(a, b):
    return a @ b


def unit(n, i, j):
    a = np.zeros((n, n), dtype=object)
    a[i, j] = 1
    return a


def shift(n, bad=False):
    a = np.zeros((n, n), dtype=object)
    for i in range(n):
        a[(i + (0 if bad else 1)) % n, i] = 1
    return a


def field_mul(a, b, polynomial):
    out = 0
    top = 1 << (polynomial.bit_length() - 1)
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & top:
            a ^= polynomial
    return out


def period(action, x):
    y, n = action(x), 1
    while y != x:
        y, n = action(y), n + 1
        if n > 100:
            raise AssertionError("nonperiodic test action")
    return n


def b1(args):
    for p in (2, 3):
        for r in range(1, 7):
            words = list(product(range(p), repeat=r))
            rotate = lambda w: w[1:] + w[:1]
            counts = {d: 0 for d in divisors(r)}
            for w in words:
                counts[period(rotate, w)] += 1
            for d, actual in counts.items():
                check(actual == count_poly(d, p, args.red_count), "B1", (p, r, d))
            for k in range(r):
                fixed = sum(w[k:] + w[:k] == w for w in words)
                check(fixed == p ** gcd(r, k), "B1", "power fixed count")
    for r, polynomial in ((2, 0b111), (4, 0b10011)):
        q = 2 ** r
        frob = lambda x: field_mul(x, x, polynomial)
        # Invertibility is checked directly for these concrete quotient models.
        for a in range(1, q):
            check(any(field_mul(a, b, polynomial) == 1 for b in range(q)), "B1", "field inverse")
        for d in divisors(r):
            actual = sum(period(frob, x) == d for x in range(q))
            check(actual == count_poly(d, 2, args.red_count), "B1", "field orbit count")
    print("B1 PASS: word census, F4/F16 field orbits and fixed powers")


def b2(args):
    for d in range(2, 49):
        for k in range(1, 7):
            derivative = sum(mobius(d // e) * e ** k for e in divisors(d))
            jordan = F(d ** k) * prod(1 - F(1, p ** k) for p in primes(d))
            check(derivative == jordan > 0, "B2", "log derivative")
        check(sum(mobius(d // e) * e for e in divisors(d)) == totient(d), "B2", "first derivative")
    for r in range(2, 25):
        ds = [d for d in divisors(r) if d > 1]
        for t in (F(1), F(1001, 1000), F(3, 2), F(2), F(3)):
            ws = [weight(r, d, t, args.red_weight) for d in ds]
            check(all(w > 0 for w in ws) and sum(ws) == 1, "B2", (r, t, ws))
            for k in range(r):
                expected = F(gcd(r, k) - 1, r - 1) if t == 1 else (t ** gcd(r, k) - t) / (t ** r - t)
                actual = sum(w for d, w in zip(ds, ws) if k % d == 0)
                check(actual == expected, "B2", "conditional character")
    print("B2 PASS: Jordan derivatives, positive rational weights, all conditional moments")


def b3(args):
    for d in range(2, 13):
        u = shift(d, args.red_frobenius)
        e = unit(d, 0, 0)
        after = mm(mm(u, e), u.T)
        check(np.trace(mm(e, e)) == 1 and np.trace(mm(e, after)) == 0, "B3", "Born distinction")
        check(not np.array_equal(mm(e, u), mm(u, e)), "B3", "noncommutativity")
        check(np.array_equal(np.linalg.matrix_power(u, d), np.eye(d, dtype=object)), "B3", "order")
    print("B3 PASS: exact state/effect witness and noncommutative cycle blocks")


def pair_map(d, e):
    g, n = gcd(d, e), lcm(d, e)
    return {(a, k): (k % d, (a + k) % e) for a in range(g) for k in range(n)}


def b4(args):
    for d, e in product(range(1, 9), repeat=2):
        f = pair_map(d, e)
        check(len(f) == d * e == len(set(f.values())), "B4", "CRT bijection")
        for (a, k), (i, j) in f.items():
            check(f[a, (k + 1) % lcm(d, e)] == ((i + 1) % d, (j + 1) % e), "B4", "shift intertwining")
    for d, e, h in product(range(1, 5), repeat=3):
        left, right = {}, {}
        for a in range(gcd(d, e)):
            for (b, k), (s, z) in pair_map(lcm(d, e), h).items():
                x, y = pair_map(d, e)[a, s]
                left[a, b, k] = (x, y, z)
        for b in range(gcd(e, h)):
            for (a, k), (x, s) in pair_map(d, lcm(e, h)).items():
                y, z = pair_map(e, h)[b, s]
                right[a, b, k] = (x, y, z)
        check(set(left.values()) == set(right.values()) == set(product(range(d), range(e), range(h))), "B4", "triple transport")
        # In each route the final cycle index must advance by one.
        for table in (left, right):
            for (a, b, k), coords in table.items():
                shifted = tuple((v + 1) % n for v, n in zip(coords, (d, e, h)))
                check(table[a, b, (k + 1) % lcm(d, e, h)] == shifted, "B4", "transported ternary action")
    v = np.array([1, 1, 0, 0], dtype=object)  # |00>+|01>, different diagonal orbits.
    rho = np.outer(v, v)
    reblock = np.zeros((4, 4), dtype=object)
    for (a, k), (i, j) in pair_map(2, 2).items():
        reblock[2 * i + j, 2 * a + k] = 1

    def transport(x, dephase=False):
        inside = reblock.T @ x @ reblock
        if dephase:
            inside = np.array([[inside[i, j] if i // 2 == j // 2 else 0
                                for j in range(4)] for i in range(4)], dtype=object)
        return reblock @ inside @ reblock.T

    out = transport(rho, args.red_coherence)
    check(F(int(v @ out @ v), 4) == 1, "B4", "actual reblocking Born return must equal one")
    for i, j in product(range(4), repeat=2):
        check(np.array_equal(transport(unit(4, i, j)), unit(4, i, j)), "B4", "actual matrix-unit transport")
    check(F(int(v @ transport(rho, True) @ v), 4) == F(1, 2), "B4", "classicalization loses half the return probability")
    print("B4 PASS: coherent CRT reblocking, ternary transport and dephasing sentinel")


def b5(args):
    for t in (F(1), F(1001, 1000), F(3, 2), F(2)):
        ratio = lambda r, s: F(r - 1, s - 1) if t == 1 else (t ** r - t) / (t ** s - t)
        check(ratio(2, 4) * ratio(4, 8) == ratio(2, 8), "B5", "tower reference weights")
        for r, s in ((2, 4), (4, 8), (2, 8)):
            prob = sum(weight(s, d, t) for d in divisors(r) if d > 1)
            check(prob == ratio(r, s), "B5", "reference success probability")
    # Actual inclusion Kraus matrices in H_2 subset H_4 subset H_8,
    # with H_r = direct sum of C^d for d|r,d>1.
    j24 = np.eye(6, 2, dtype=object)
    j48 = np.eye(14, 6, dtype=object)
    j28 = np.eye(14, 2, dtype=object)
    check(np.array_equal(j48 @ j24, j28), "B5", "inclusion tower matrices")
    p28 = j28 @ j28.T
    q28 = np.eye(14, dtype=object) - p28
    failure = np.zeros_like(q28) if args.red_decoder else q28
    check(np.array_equal(j28 @ j28.T + failure.T @ failure, np.eye(14, dtype=object)), "B5", "decoder Kraus completeness")
    offset = 0
    for d in (2, 4, 8):
        for i, j in product(range(d), repeat=2):
            x = unit(14, offset + i, offset + j)
            success = j28.T @ x @ j28
            out = j28 @ success @ j28.T + failure @ x @ failure.T
            check(np.array_equal(out, x), "B5", "retained decoder matrix-unit reconstruction")
            staged = j24.T @ (j48.T @ x @ j48) @ j24
            check(np.array_equal(success, staged), "B5", "tower success on matrix units")
        offset += d
    tags = set()
    p24 = j24 @ j24.T
    q24 = np.eye(6, dtype=object) - p24
    ks = (j24.T, q24)
    completeness = np.zeros((36, 36), dtype=object)
    for a, b in product(ks, repeat=2):
        k = np.kron(a, b)
        completeness += k.T @ k
    check(np.array_equal(completeness, np.eye(36, dtype=object)), "B5", "four-outcome Kraus completeness")
    branch_kraus = {(a, b): np.kron(ks[not a], ks[not b]) for a, b in product((True, False), repeat=2)}
    for d, e in product((2, 4), repeat=2):
        tag = (2 % d == 0, 2 % e == 0)
        tags.add(tag)
        for i, j, k, h in product(range(d), range(d), range(e), range(e)):
            ii, jj = (0 if d == 2 else 2) + i, (0 if d == 2 else 2) + j
            kk, hh = (0 if e == 2 else 2) + k, (0 if e == 2 else 2) + h
            source_i, source_j = ii * 6 + kk, jj * 6 + hh
            for output_tag, kmat in branch_kraus.items():
                actual = np.outer(kmat[:, source_i], kmat[:, source_j])
                target_width = 2 if output_tag[1] else 6
                expected = unit(len(kmat), ii * target_width + kk, jj * target_width + hh) if output_tag == tag else np.zeros_like(actual)
                check(np.array_equal(actual, expected), "B5", "four-branch tensor matrix-unit channel")
    check(len(tags) == 4, "B5", "all four outcomes")
    print("B5 PASS: conditional inclusion weights, tower success and four retained tensor branches")


def b6(args):
    for q in (2, 3, 4):
        mul = (lambda a, b: field_mul(a, b, 0b111)) if q == 4 else (lambda a, b: a * b % q)
        add = (lambda a, b: a ^ b) if q == 4 else (lambda a, b: (a + b) % q)
        for d in range(1, 4):
            active = fixed = active_fixed = 0
            for xs in product(range(q), repeat=d):
                m = 1
                for x in xs:
                    m = mul(m, x)
                for z in range(q):
                    nz = all(xs)
                    is_fixed = add(z, m) == z
                    active += int(nz)
                    fixed += int(is_fixed)
                    active_fixed += int(nz and is_fixed)
            w = F((q - 1) ** d, q ** d)
            check(F(active, q ** (d + 1)) == w, "B6", "active mass")
            check(F(fixed, q ** (d + 1)) == 1 - w and active_fixed == 0, "B6", "multiplication trace")
        a, b = {0, 1}, {1, 2}
        exponent = len(a) + len(b) if args.red_overlap else len(a | b)
        observed = sum(all(xs[j] != 0 for j in a | b) for xs in product(range(q), repeat=3))
        check(F(observed, q ** 3) == F(q - 1, q) ** exponent, "B6", "overlap uses union")
    # sqrt(2) V|0> = |0>+|1>; comparing unnormalized columns avoids radicals.
    v0 = np.array([1, 1, 0, 0], dtype=object)
    check(any(v0 * np.array([0, 1, 1, 1], dtype=object)), "B6", "nonzero-sector V counterexample")
    # All of alpha, alpha, alpha^2 are nonfixed; target becomes zero.
    check(field_mul(2, 2, 0b111) ^ 3 == 0, "B6", "multiplication leaves all-active orbit corner")
    # F4 Fourier is this integer character matrix divided by two.
    fourier = np.zeros((4, 4), dtype=object)
    for x, y in product(range(4), repeat=2):
        z = field_mul(x, y, 0b111)
        tr = z ^ field_mul(z, z, 0b111)
        fourier[x, y] = 1 - 2 * tr
    cut = np.diag(np.array([0, 0, 1, 1], dtype=object))
    check(np.array_equal(fourier @ fourier.T, 4 * np.eye(4, dtype=object)), "B6", "exact Fourier orthogonality")
    overlap = F(int(np.trace(cut @ fourier @ cut @ fourier.T)), 16)
    check(overlap == F(1, 4), "B6", "F4 Fourier active overlap")
    print("B6 PASS: multiplication counts, overlap filtration and mixed-gate scope sentinels")


def main():
    parser = argparse.ArgumentParser(description=__doc__ + " All arithmetic is exact; no tolerances.")
    for name in ("count", "weight", "frobenius", "coherence", "decoder", "overlap"):
        parser.add_argument("--red-" + name, action="store_true", help="mutate the named mathematical gate")
    args = parser.parse_args()
    try:
        for gate in (b1, b2, b3, b4, b5, b6):
            gate(args)
    except AssertionError as error:
        print("FAIL", error)
        return 1
    print("PASS: B1--B6. Finite evidence only; general statements rely on the reviewed written proofs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
