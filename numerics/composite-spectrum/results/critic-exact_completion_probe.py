#!/usr/bin/env python3
"""Critic-owned finite falsifiers, without candidate/checker imports.

Integer/Fraction calculations only. These cannot certify norm completions,
semifiniteness, infinite spectra, trace-class operators, or infinite series.
Each --red MODE changes input data and must die at its named gate.
"""
import argparse
from fractions import Fraction as Q
from itertools import product
from math import gcd


def demand(condition, gate, detail):
    if not condition:
        raise AssertionError(f"{gate}: {detail}")


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    return sum(gcd(n, k) == 1 for k in range(1, n + 1))


def mobius(n):
    sign, p = 1, 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            sign = -sign
            if n % p == 0:
                return 0
        p += 1
    return -sign if n > 1 else sign


def rem(a, b, p):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    while len(a) >= len(b):
        scalar, offset = a[-1], len(a) - len(b)
        for k, c in enumerate(b):
            a[offset + k] = (a[offset + k] - scalar * c) % p
        while a and a[-1] == 0:
            a.pop()
    return a


class Field:
    def __init__(self, p, r):
        self.p, self.r, self.size = p, r, p ** r
        for candidate in product(range(p), repeat=r):
            if candidate[0] == 0:
                continue
            f = candidate + (1,)
            reducible = any(
                not rem(f, coefficients + (1,), p)
                for degree in range(1, r // 2 + 1)
                for coefficients in product(range(p), repeat=degree))
            if not reducible:
                self.f = f
                break
        else:
            raise AssertionError("No irreducible polynomial found")

    def digits(self, x):
        return [(x // self.p ** k) % self.p for k in range(self.r)]

    def mul(self, x, y):
        a, b = self.digits(x), self.digits(y)
        result = [0] * (2 * self.r - 1)
        for i in range(self.r):
            for j in range(self.r):
                result[i + j] = (result[i + j] + a[i] * b[j]) % self.p
        return sum(c * self.p ** k for k, c in enumerate(rem(result, self.f, self.p)))

    def power(self, x, n):
        result = 1
        while n:
            if n & 1:
                result = self.mul(result, x)
            n >>= 1
            x = self.mul(x, x)
        return result


def arithmetic_corners(red):
    gate, records = "P1_ARITHMETIC_CORNER", []
    # Includes p=2, p=3, composite degree, and nonprime fixed base q=4.
    for p, s, n, m in [(2, 1, 2, 4), (2, 1, 2, 6),
                       (2, 1, 3, 6), (3, 1, 2, 4), (2, 2, 2, 4)]:
        field, q = Field(p, s * m), p ** s
        sigma = {x: field.power(x, q) for x in range(field.size)}
        lower = {x for x in sigma if field.power(x, q ** n) == x}
        demand(len(lower) == q ** n, gate, "wrong fixed-field cardinality")
        unused, orbits = set(sigma), []
        while unused:
            x, orbit = min(unused), []
            while x not in orbit:
                orbit.append(x)
                x = sigma[x]
            demand(x == orbit[0], gate, "Frobenius did not give a cycle")
            unused.difference_update(orbit)
            orbits.append(tuple(orbit))
        # Mutate an actual arithmetic image, not the expected divisor formula.
        if red == "corner_image":
            lower.remove(next(x for x in lower if sigma[x] != x))
        included = [orbit for orbit in orbits if set(orbit) <= lower]
        for orbit in orbits:
            demand((len(orbit) in divs(n)) == (orbit in included), gate,
                   "one degree block is not saturated by the embedded field")
            d = len(orbit)
            for k in range(d):
                graph = set()
                for x in orbit:
                    y = x
                    for _ in range(k):
                        y = sigma[y]
                    graph.add((x, y, field.mul(x, y)))
                demand(len(graph) == d, gate, "graph normalization changed")
                demand(all((x in lower) == (y in lower) == (z in lower)
                           for x, y, z in graph) if orbit in included else True,
                       gate, "embedded multiplication graph escaped subfield")
        counts = {d: sum(len(o) == d for o in orbits) for d in divs(m)}
        records.append((q, n, m, counts))
    print(gate, records)


def coefficients(red):
    gate = "P2_FIRST_GRADE"
    for d in range(2, 65):
        for s in [1, 2, 3]:
            # Differentiation of the exact finite exponential polynomial at 0.
            derivative = sum(mobius(d // e) * s * e for e in divs(d))
            actual = Q(derivative, s * d)
            eta_data = Q(phi(d), d)
            if red == "coefficient":
                eta_data *= d
            demand(actual == eta_data, gate, f"d={d}, s={s}: copied coefficient")
    for n, m in [(2, 6), (3, 12), (6, 30), (12, 60)]:
        lower = {d: Q(sum(mobius(d // e) * e for e in divs(d)), d)
                 for d in divs(n) if d > 1}
        upper = {d: Q(phi(d), d) for d in divs(m) if d > 1}
        trace_lower = sum(weight * Q(d + 1, 2) for d, weight in lower.items())
        trace_image = sum(upper[d] * Q(d + 1, 2) for d in lower)
        demand(trace_lower == trace_image, gate, "corner trace incompatible")
        success = sum(upper[d] for d in lower) / sum(upper.values())
        demand(success == sum(lower.values()) / sum(upper.values()), gate,
               "normalized success ratio differs")
    print(gate, "exact d=2..64, s=1,2,3; four divisor corners")


def shifts(red):
    gate = "P3_SHIFT_WITNESS"
    for d in range(2, 65):
        permutation = [(k + 1) % d for k in range(d)]
        if red == "shift":
            permutation = list(range(d))
        diagonal = [int(k == permutation[0]) - int(k == 0) for k in range(d)]
        demand(max(map(abs, diagonal)) == 1, gate, "outerness witness lost")
        for j in range(-12, 13):
            # Count the fixed labels of the actual permutation power.
            traced = 0
            for k in range(d):
                image = k
                for _ in range(j % d):
                    image = permutation[image]
                traced += image == k
            demand(traced == (d if j % d == 0 else 0), gate,
                   f"d={d}, j={j}: implementer trace mismatch")
    print(gate, "d=2..64; powers -12..12; exact norm-one projections")


def density_moments(red):
    gate = "P4_DENSITY_MOMENTS"
    for beta in [2, 3, 4]:
        degrees = range(2, 65)
        zcut = sum(Q(phi(d), d ** (beta + 1)) for d in degrees)
        eigenvalues = {d: Q(phi(d), d ** (beta + 2)) / zcut for d in degrees}
        if red == "density":
            eigenvalues = {d: d * value for d, value in eigenvalues.items()}
        total = sum(d * eigenvalues[d] for d in degrees)
        demand(total == 1, gate, "ordinary Hilbert trace of density is not one")
        for j in range(-12, 13):
            literal = sum(eigenvalues[d] * sum((k + j) % d == k for k in range(d))
                          for d in degrees)
            if j:
                predicted = sum(Q(phi(d), d ** (beta + 1))
                                for d in divs(abs(j)) if d > 1) / zcut
            else:
                predicted = Q(0) if red == "zero_moment" else Q(1)
            demand(literal == predicted, gate, f"j={j}: wrong moment scope")
        # A positive block observable with independently summed ordinary trace.
        hilbert = sum(eigenvalues[d] * sum(k * k for k in range(d)) for d in degrees)
        weighted = sum(Q(phi(d), d) * Q(1, d ** beta) *
                       Q(sum(k * k for k in range(d)), d) for d in degrees) / zcut
        demand(hilbert == weighted, gate, "theta(D_beta a) / Z != density state")
    print(gate, "beta=2,3,4; 63 blocks; integer powers -12..12")


def convolution_tail(red):
    gate = "P5_CONVOLUTION_TAIL"
    for k in range(1, 129):
        coefficients_data = {d: phi(d) for d in divs(k)}
        if red == "dirichlet_data":
            coefficients_data[1] = 0
        demand(sum(coefficients_data.values()) == k, gate,
               f"k={k}: independent Dirichlet coefficient mismatch")
    for beta in [2, 3, 4]:
        for cutoff in [1, 2, 5, 20]:
            finite_tail = sum(Q(phi(d), d ** (beta + 1))
                              for d in range(cutoff + 1, 129))
            bound = Q(1, (beta - 1) * cutoff ** (beta - 1))
            if red == "tail_bound":
                bound = Q(0)
            demand(0 < finite_tail <= bound, gate, "finite tail violates integral bound")
    print(gate, "128 exact convolution coefficients; 12 rational tail comparisons")


def main():
    modes = ["corner_image", "coefficient", "shift", "density", "zero_moment",
             "dirichlet_data", "tail_bound"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--red", choices=modes)
    args = parser.parse_args()
    for probe in [arithmetic_corners, coefficients, shifts, density_moments,
                  convolution_tail]:
        probe(args.red)
    print("PASS: finite falsifiers only; no infinite theorem certified")


if __name__ == "__main__":
    main()
