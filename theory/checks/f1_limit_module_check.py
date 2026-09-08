#!/usr/bin/env python3
"""Exact marked-register/right-Hecke action probes.

Sparse finite-field flag/vector operators at (m,n)=(1,2), plus independent
antichain basis and coherence checks. No theorem is inferred from sampling.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations, product


CHECKED, FAILED = {}, {}


def need(condition, gate, diagnostic):
    CHECKED[gate] = CHECKED.get(gate, 0)+1
    if not condition:
        FAILED.setdefault(gate, set()).add(diagnostic)


def add(*matrices):
    out = [{} for _ in matrices[0]]
    for a in matrices:
        for i, row in enumerate(a):
            for j, c in row.items():
                out[i][j] = out[i].get(j, F(0))+c
    return [{j: c for j, c in row.items() if c} for row in out]


def scale(c, a):
    return [{j: c*v for j, v in row.items() if c*v} for row in a]


def mul(a, b):
    out = [{} for _ in a]
    for i, row in enumerate(a):
        for k, c in row.items():
            for j, d in b[k].items():
                out[i][j] = out[i].get(j, F(0))+c*d
    return [{j: c for j, c in row.items() if c} for row in out]


def star(a):
    out = [{} for _ in a]
    for i, row in enumerate(a):
        for j, c in row.items():
            out[j][i] = c
    return out


def inner(a, b):
    return sum((c*b[i].get(j, 0) for i, row in enumerate(a) for j, c in row.items()), F(0))/len(a)


def trace(a):
    return sum((row.get(i, F(0)) for i, row in enumerate(a)), F(0))/len(a)


def field_operators(p, wrong_block=False):
    vectors = tuple(product(range(p), repeat=3))
    points = tuple(x for x in vectors if any(x) and next(a for a in x if a) == 1)
    flags = tuple((line, normal) for line in points for normal in points
                  if sum(a*b for a, b in zip(line, normal)) % p == 0)
    space = tuple(product(range(len(flags)), vectors))
    index = {x: i for i, x in enumerate(space)}
    identity = [{i: F(1)} for i in range(len(space))]
    t0, t1, t2 = [], [], []
    for f, x in space:
        line, normal = flags[f]
        t0.append({index[f, tuple((a+c*b) % p for a, b in zip(x, line))]: F(1)
                   for c in range(1, p)})
        t1.append({index[g, x]: F(1) for g, (other_line, other_normal) in enumerate(flags)
                   if g != f and other_normal == normal})
        which = 1 if wrong_block else 0
        t2.append({index[g, x]: F(1) for g, other in enumerate(flags)
                   if g != f and other[which] == flags[f][which]})
    return identity, t0, t1, t2


def operator_action(args):
    for p in (2, 3):
        identity, t0, t1, t2 = field_operators(p, args.red_module_shift)
        need(mul(t0, t0) == add(scale(p-2, t0), scale(p-1, identity)), 'M1', 'marked generator quadratic')
        need(mul(t2, t2) == add(scale(p-1, t2), scale(p, identity)), 'M1', 'right Hecke generator quadratic')
        need(mul(t0, t2) == mul(t2, t0), 'M1', 'marked generator commutes with the correctly shifted block')
        basis = [identity, t0, t2, mul(t0, t2)]
        norms = (F(1), F(p-1), F(p), F(p*(p-1)))
        for i, a in enumerate(basis):
            need(star(a) == a, 'M1', 'product basis star')
            for j, b in enumerate(basis):
                need(inner(a, b) == (norms[i] if i == j else 0), 'M1', 'module inclusion faithful factorized trace Gram')
        # Four minimal sectors of the commuting image, computed as matrices.
        marked = scale(F(1, p), add(identity, t0))
        ordinary = scale(F(1, p+1), add(identity, t2))
        source_factors = [marked, add(identity, scale(-1, marked))]
        right_factors = [ordinary, add(identity, scale(-1, ordinary))]
        weights = (F(1, p*(p+1)), F(1, p+1), F(p-1, p*(p+1)), F(p-1, p+1))
        for (a, b), weight in zip(product(source_factors, right_factors), weights):
            projection = mul(a, b)
            need(mul(projection, projection) == projection and star(projection) == projection
                 and trace(projection) == weight, 'M1', 'minimal marked-unmarked sector weight')
        x = add(identity, t1, mul(t0, t1))
        positive = mul(star(x), x)
        coefficients = [inner(b, positive)/norm for b, norm in zip(basis, norms)]
        if args.red_module_expect:
            coefficients[1] += 1
        expected = add(*(scale(c, b) for c, b in zip(coefficients, basis)))
        for b in basis:
            need(inner(b, expected) == inner(b, positive), 'M3', 'module expectation trace pairing')
        need(trace(expected) == trace(positive), 'M3', 'module expectation preserves the reference trace')
        for a, b in product((F(p-1), F(-1)), (F(p), F(-1))):
            value = coefficients[0]+coefficients[1]*a+coefficients[2]*b+coefficients[3]*a*b
            need(value >= 0, 'M3', 'conditional expectation of a positive ambient square')
        print(f'marked1 + Hecke2 over F{p}: {len(identity)} flag-vector basis states, image dimension4')


def inverse_permutation(w):
    return tuple(w.index(i) for i in range(len(w)))


def length(w):
    return sum(w[i] > w[j] for i in range(len(w)) for j in range(i+1, len(w)))


def block(u, v):
    return tuple(u)+tuple(len(u)+x for x in v)


def antichains(w):
    wi = inverse_permutation(w)
    positions = {(i, j) for i in range(len(w)) for j in range(i+1, len(w)) if wi[i] < wi[j]}
    for bits in product((False, True), repeat=len(w)):
        a = frozenset(i for i, bit in enumerate(bits) if bit)
        if not any(i in a and j in a for i, j in positions):
            yield a, a | frozenset(i for i, j in positions if j in a)


def basis_action(args):
    for m in range(4):
        for n in range(5-m):
            for u in permutations(range(m)):
                for a, down in antichains(u):
                    for v in permutations(range(n)):
                        combined = block(u, v)
                        image_a = frozenset(i+n for i in a) if args.red_module_marker else a
                        lookup = dict(antichains(combined))
                        valid = image_a in lookup and image_a <= set(range(m))
                        need(valid, 'M2', 'marked antichain stays in the first block')
                        if image_a in lookup:
                            for q in (2, 3, 5):
                                image_weight = q**(length(combined)+len(lookup[image_a])-len(image_a))*(q-1)**len(image_a)
                                product_weight = q**(length(u)+len(down)-len(a))*(q-1)**len(a)*q**length(v)
                                need(image_weight == product_weight, 'M2', 'all sampled basis valencies factor under module action')
                        need(combined[:m] == u and tuple(x-m for x in combined[m:]) == v,
                             'M2', 'block expectation decodes its included basis')
                        for k in range(5-m-n):
                            for z in permutations(range(k)):
                                need(block(block(u, v), z) == block(u, block(v, z)),
                                     'M2', 'right action associativity on ordered basis labels')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, description in {
        'module-shift': 'M1: use T1 instead of the shifted right-block T2',
        'module-marker': 'M2: move the marked antichain out of its source block',
        'module-expect': 'M3: alter the marked expectation coefficient',
    }.items():
        parser.add_argument('--red-'+name, action='store_true', help=description)
    args = parser.parse_args()
    print('MODE:', ','.join(k for k, v in vars(args).items() if v) or 'green')
    operator_action(args)
    basis_action(args)
    for gate in ('M1', 'M2', 'M3'):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED.get(gate, 0)} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL MARKED-REGISTER MODULE PROBES PASSED')


if __name__ == '__main__':
    main()
