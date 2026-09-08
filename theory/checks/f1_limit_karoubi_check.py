#!/usr/bin/env python3
"""Exact finite falsifiers for the full traced completion. No analytic theorem by samples."""
import argparse
from fractions import Fraction as F
from math import factorial


def mat(rows):
    return tuple(tuple(F(x) for x in row) for row in rows)


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(r, s)) for r, s in zip(a, b))


def mul(a, b):
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
                       for j in range(len(b[0]))) for i in range(len(a)))


def star(a):
    return tuple(zip(*a))


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


I = mat([[1, 0], [0, 1]])
P = mat([[1, 0], [0, 0]])
ZERO = scale(F(0), I)
CHECKED, FAILED = {}, {}


def need(condition, gate, diagnostic):
    CHECKED[gate] = CHECKED.get(gate, 0) + 1
    if not condition:
        FAILED.setdefault(gate, set()).add(diagnostic)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    names = ('grading', 'density-ratio', 'cutoff', 'normalization', 'gram', 'classical')
    for name in names:
        parser.add_argument('--red-'+name, action='store_true')
    args = parser.parse_args()

    degrees = (0, 1)
    pairs = {k: [(m, n) for m in degrees for n in degrees if m+n == k]
             for k in range(3)}
    collective_dim = sum((len(v) if args.red_grading else len(v)**2)*factorial(k)
                         for k, v in pairs.items())
    need(collective_dim == 7 and len(degrees)**2 == 4,
         'K1', 'same-total components form full matrix corners')
    need(sum(len(v) for v in pairs.values()) == len(degrees)**2,
         'K1', 'unnormalized identity trace is multiplicative')
    source = tuple(map(F, (2, 3, 5, 7)))
    collective = (source[0], mat([[source[1], 0], [0, source[2]]]), source[3])
    expect = lambda a: (a[0], a[1][0][0], a[1][1][1], a[2])
    need(expect(collective) == source, 'K1', 'assembly split fixes separated algebra')
    offdiag = (F(0), mat([[0, 1], [0, 0]]), F(0))
    need(offdiag[1] != ZERO and expect(offdiag) == (F(0),)*4,
         'K1', 'collective off-diagonal observable survives and is coarsened')

    p3 = mat([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    factor = F(1) if args.red_density_ratio else F(3)
    transported = scale(factor, p3)
    need(tr(transported)/3 == tr(p3), 'K2', 'dimension-ratio density normalization')
    for a in (mat([[1, 2, 0], [3, 4, 5], [0, 6, 7]]), p3):
        need(tr(mul(transported, a))/3 == tr(mul(p3, mul(mul(p3, a), p3))),
             'K2', 'rectangular Kraus trace duality')

    for t in (F(-1, 3), F(0), F(1, 3)):
        rotation = scale(1/(1+t*t), mat([[1-t*t, -2*t], [2*t, 1-t*t]]))
        p = mul(mul(rotation, P), star(rotation))
        complement = add(I, scale(-1, p))
        raw = add(p, scale(t*t, I))
        cutoff = complement if args.red_cutoff else p
        need(mul(p, p) == p and star(p) == p and tr(p) == 1,
             'K3', 'continuous rational projection family')
        need(mul(raw, cutoff) == scale(1+t*t, cutoff) and t*t < F(1, 2),
             'K3', 'spectral cutoff selects the upper band')
        if t == 0:
            need(cutoff == P, 'K3', 'cutoff lifts the prescribed endpoint object')
        v = mul(rotation, P)
        need(mul(star(v), v) == P and mul(v, star(v)) == p,
             'K3', 'unitary between moving projection objects')

        c = 2+t*t
        raw_k = scale(c, p)
        k = raw_k if args.red_normalization else mul(raw_k, scale(1/c, p))
        need(mul(star(k), k) == p, 'K4', 'raw Kraus normalization in its source corner')

        a = mat([[1, 2], [3, 4]])
        gram_inverse = F(1) if args.red_gram else F(2)
        actual = add(scale(gram_inverse*tr(mul(p, a))/2, p),
                     scale(gram_inverse*tr(mul(complement, a))/2, complement))
        rotated = mul(mul(star(rotation), a), rotation)
        diagonal = mat([[rotated[0][0], 0], [0, rotated[1][1]]])
        expected = mul(mul(rotation, diagonal), star(rotation))
        need(actual == expected and tr(actual) == tr(a),
             'K5', 'local Gram inverse recovers the traced expectation')

        rho = scale(F(2), P)
        branches = [mul(mul(k0, rho), k0) for k0 in (p, complement)]
        classical_factor = F(1) if args.red_classical else F(2)
        full_trace = sum(tr(scale(classical_factor, branch))/2 for branch in branches)/2
        need(full_trace == 1, 'K6', 'uniform classical trace needs the outcome-count factor')

    for gate in sorted(CHECKED):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED[gate]} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL KAROUBI EXAMPLES PASSED (finite exact probes only)')


if __name__ == '__main__':
    main()
