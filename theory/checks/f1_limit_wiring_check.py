#!/usr/bin/env python3
"""Exact typed classical routing and quantum-instrument probes.

Finite rational matrices and an independent S3 convolution calculation.
These checks support the repaired circuit presentation; they do not prove
general monoidal coherence or continuous-germ theorems by sampling.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations, product
import numpy as np


CHECKED, FAILED = {}, {}


def need(condition, gate, diagnostic):
    CHECKED[gate] = CHECKED.get(gate, 0) + 1
    if not condition:
        FAILED.setdefault(gate, set()).add(diagnostic)


def matrix(rows):
    return np.array([[F(x) for x in row] for row in rows], dtype=object)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def zeros(m, n):
    return matrix([[0]*n for _ in range(m)])


def recorded(k, o, count):
    """Quantum output precedes one classical outcome wire."""
    tagged = zeros(k.shape[0]*count, k.shape[1])
    for i in range(k.shape[0]):
        tagged[i*count+o, :] = k[i, :]
    return tagged


def channel(ks, state):
    return sum((k @ state @ k.T for k in ks), zeros(ks[0].shape[0], ks[0].shape[0]))


def route(dimensions, order):
    source = tuple(product(*(range(d) for d in dimensions)))
    target = tuple(product(*(range(dimensions[i]) for i in order)))
    indices = {x: i for i, x in enumerate(target)}
    result = zeros(len(source), len(source))
    for j, x in enumerate(source):
        result[indices[tuple(x[i] for i in order)], j] = 1
    return result


def instruments():
    # K: C^2 -> C^3 with two outcomes; L: C^3 -> C^2 with three.
    v0 = matrix([[1, 0], [0, 1], [0, 0]])
    v1 = matrix([[0, 0], [1, 0], [0, 1]])
    ks = [F(3, 5)*v0, F(4, 5)*v1]
    ls = [matrix([[1, 0, 0], [0, 0, 0]]),
          matrix([[0, 0, 0], [0, 1, 0]]),
          matrix([[0, 0, F(3, 5)], [0, 0, F(4, 5)]])]
    return ks, ls


def sequential(args):
    ks, ls = instruments()
    need(np.array_equal(sum((k.T@k for k in ks), zeros(2, 2)), eye(2)),
         'W1', 'first instrument is complete')
    need(np.array_equal(sum((k.T@k for k in ls), zeros(3, 3)), eye(3)),
         'W1', 'second instrument is complete')
    rho = matrix([[F(9, 25), F(12, 25)], [F(12, 25), F(16, 25)]])
    first = channel([recorded(k, o, 2) for o, k in enumerate(ks)], rho)
    # Legal circuit: (L tensor id_O) after K. Output order is Q2,P3,O2.
    second = channel([np.kron(recorded(l, p, 3), eye(2)) for p, l in enumerate(ls)], first)
    routing = eye(12) if args.red_sequential_route else route((2, 3, 2), (0, 2, 1))
    joined = routing @ second @ routing.T
    # The fused list records lexicographic histories (o,p).
    fused = [recorded(l@k, 3*o+p, 6) for o, k in enumerate(ks) for p, l in enumerate(ls)]
    expected = channel(fused, rho)
    need(np.array_equal(joined, expected), 'W1', 'sequential history retyping')
    need(np.trace(joined) == 1, 'W1', 'recorded total probability')
    # Test the superoperator identity on all four matrix units as well.
    for i, j in product(range(2), repeat=2):
        unit = zeros(2, 2)
        unit[i, j] = 1
        a = channel([recorded(k, o, 2) for o, k in enumerate(ks)], unit)
        b = channel([np.kron(recorded(l, p, 3), eye(2)) for p, l in enumerate(ls)], a)
        need(np.array_equal(routing@b@routing.T, channel(fused, unit)),
             'W1', 'full sequential CP map equality')


def parallel(args):
    ks, ls = instruments()
    x = matrix([[F(3, 5)], [F(4, 5)]])
    y = matrix([[F(2, 3)], [F(1, 3)], [F(2, 3)]])
    rho = np.kron(x@x.T, y@y.T)
    # Separated outputs before routing: Q3,O2,Q2,P3.
    raw = [np.kron(recorded(k, o, 2), recorded(l, p, 3))
           for o, k in enumerate(ks) for p, l in enumerate(ls)]
    actual = channel(raw, rho)
    routing = eye(36) if args.red_parallel_route else route((3, 2, 2, 3), (0, 2, 1, 3))
    joint = routing@actual@routing.T
    fused = [recorded(np.kron(k, l), 3*o+p, 6)
             for o, k in enumerate(ks) for p, l in enumerate(ls)]
    need(np.array_equal(joint, channel(fused, rho)), 'W2', 'classical wire passes the second quantum output')
    need(np.array_equal(routing.T@routing, eye(36)), 'W2', 'routing is a unitary permutation')
    need(np.trace(joint) == 1, 'W2', 'parallel instrument total probability')
    # Outcome masses are compared independently with the product law.
    for o, k in enumerate(ks):
        for p, l in enumerate(ls):
            indices = [b*6+3*o+p for b in range(6)]
            mass = sum(joint[i, i] for i in indices)
            expected = np.trace(k@(x@x.T)@k.T)*np.trace(l@(y@y.T)@l.T)
            need(mass == expected, 'W2', 'paired classical outcome mass')


def classical_trace(args):
    ks, _ = instruments()
    rho = matrix([[F(9, 25), F(12, 25)], [F(12, 25), F(16, 25)]])
    source_density = 2*rho  # Reference trace is Tr_2/2.
    quantum_factor = F(3, 2)
    classical_factor = 1 if args.red_classical_trace else 2
    blocks = [classical_factor*quantum_factor*k@source_density@k.T for k in ks]
    normalized_trace = sum(np.trace(b) for b in blocks)/6
    need(normalized_trace == 1, 'W3', 'uniform classical trace requires its cardinality factor')
    for b, k in zip(blocks, ks):
        need(np.trace(b)/6 == np.trace(k@rho@k.T), 'W3', 'classical output density recovers branch mass')


def group_multiply(u, v):
    return tuple(u[v[i]] for i in range(3))


def group_add(*xs):
    result = {}
    for x in xs:
        for w, c in x.items():
            result[w] = result.get(w, F(0))+c
    return {w: c for w, c in result.items() if c}


def group_scale(c, x):
    return {w: c*a for w, a in x.items() if c*a}


def group_product(x, y):
    return group_add(*({group_multiply(u, v): a*b} for u, a in x.items() for v, b in y.items()))


def group_star(x):
    return {tuple(w.index(i) for i in range(3)): c for w, c in x.items()}


def luders(args):
    identity = {(0, 1, 2): F(1)}
    s, t = {(1, 0, 2): F(1)}, {(0, 2, 1): F(1)}
    cycle = group_product(s, t)
    z = group_scale(F(1, 3), group_add(group_scale(2, identity),
                                    group_scale(-1, cycle), group_scale(-1, group_star(cycle))))
    e = group_scale(F(1, 2), group_add(identity, t))
    p = group_product(z, e)
    h = group_scale(2, e)
    success_k = group_product(s, p) if args.red_backaction else p
    failure_k = group_add(identity, group_scale(-1, p))
    effects = [group_product(group_star(k), k) for k in (success_k, failure_k)]
    need(group_add(*effects) == identity and effects[0] == p, 'W4', 'instruments share the same complete POVM')
    branch = group_product(group_product(success_k, h), group_star(success_k))
    success = branch.get((0, 1, 2), F(0))
    conditional = group_scale(1/success, branch)
    moved = group_product(group_product(s, conditional), s)
    returned = group_product(moved, p).get((0, 1, 2), F(0))
    need(success == F(2, 3) and conditional == group_scale(3, p), 'W4', 'Luders Kraus data determine the successful density')
    need(returned == F(1, 4) and success*returned == F(1, 6), 'W4', 'Luders protocol joint endpoint probability')


def histories(args):
    for o, p, r in product(range(2), range(3), range(2)):
        left = ((o, p), r)
        right = (o, (p, r))
        flatten_left = (left[0][0], left[0][1], left[1])
        flatten_right = (right[0], right[1][0], right[1][1])
        if args.red_history:
            flatten_right = (right[0], 0, right[1][1])
        need(flatten_left == flatten_right, 'W5', 'associative history-product identification')
    source = tuple(product(product(range(2), range(3)), product(range(2), range(2))))
    image = {((a[0], b[0]), (a[1], b[1])) for a, b in source}
    target = set(product(product(range(2), range(2)), product(range(3), range(2))))
    need(image == target and len(image) == len(source), 'W5', 'interchange history bijection')
    singleton = {((o,), (0,)): (o,) for o in range(3)}
    need(len(set(singleton.values())) == 3, 'W5', 'singleton classical unit identification')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, description in {
        'sequential-route': 'W1: omit classical history routing after composition',
        'parallel-route': 'W2: omit classical routing past a quantum output',
        'classical-trace': 'W3: omit classical outcome-cardinality factor',
        'backaction': 'W4: apply a unitary in the successful Kraus branch',
        'history': 'W5: drop the middle classical outcome from an associator',
    }.items():
        parser.add_argument('--red-'+name, action='store_true', help=description)
    args = parser.parse_args()
    print('MODE:', ','.join(k for k, v in vars(args).items() if v) or 'green')
    sequential(args)
    parallel(args)
    classical_trace(args)
    luders(args)
    histories(args)
    for gate in sorted(CHECKED):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED[gate]} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL CLASSICAL WIRING AND INSTRUMENT PROBES PASSED')


if __name__ == '__main__':
    main()
