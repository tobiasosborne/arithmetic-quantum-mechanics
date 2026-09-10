#!/usr/bin/env python3
"""Exact interface probes between admitted finite-abelian models and D1703.

Reuses the existing Abelian operator code; the proposed wavefunction is
evaluated independently. No floats; no finite pass promotes a theorem.
"""
import argparse
from collections import Counter
from fractions import Fraction
from itertools import product

from f1_check import Abelian, compose, scale, phase_sum
from wh_kappa.ff import GF


MUTATIONS = {'dual-sign': 'R1', 'trivial-character': 'R1',
             'rephase': 'R2', 'position-labels': 'R2',
             'cocycle': 'R3', 'central-injective': 'R3',
             'trace-normalization': 'R4', 'vacuum': 'R4',
             'tensor-phase': 'R5', 'character-conflation': 'R6',
             'relative-frobenius': 'R6'}


class Failure(Exception):
    def __init__(self, gate, detail):
        self.gate, self.detail = gate, detail


class Checks:
    def __init__(self, mutation):
        self.mutation, self.counts = mutation, Counter()

    def check(self, gate, value, detail):
        self.counts[gate] += 1
        if not value:
            raise Failure(gate, detail)


class Model:
    def __init__(self, field, rank, parameter):
        self.f, self.rank, self.parameter = field, rank, parameter
        self.g = Abelian((field.p,) * (field.n * rank), field.p)
        self.coords = {x: tuple(field.undigits(x[j:j+field.n])
                               for j in range(0, len(x), field.n))
                       for x in self.g.elements}
        self.half = pow(2, -1, field.p)
        self.ops = {}

    def dot(self, a, b):
        acc = 0
        for x, y in zip(self.coords[a], self.coords[b]):
            acc = self.f.ADD[acc][self.f.MUL[x][y]]
        return acc

    def psi(self, x):
        return self.f.TR[self.f.MUL[self.parameter][x]]

    def cochain(self, a, b):
        return self.psi(self.f.MUL[self.half][self.dot(a, b)])

    def wave(self, a, b, reverse=False):
        # Evaluate delta_y at x-a (or the deliberately changed x+a).
        result = []
        for y in self.g.elements:
            entries = []
            for x in self.g.elements:
                arg = tuple((u + (v if reverse else -v)) % self.f.p
                            for u, v in zip(x, a))
                if arg == y:
                    exponent = (-self.psi(self.dot(b, x)) + self.cochain(a, b)) % self.f.p
                    entries.append((x, exponent))
            assert len(entries) == 1
            result.append(entries[0])
        return tuple(result)


def finite_model(c, f, rank, parameter):
    m = Model(f, rank, parameter)
    g = m.g
    c.check('R1', {m.psi(x) for x in range(f.q)} == set(range(f.p)),
            'the named additive character must be nontrivial, including at rank zero')
    basis = [tuple(int(i == j) for i in range(f.n * rank))
             for j in range(f.n * rank)]
    duals = {}
    for b in g.elements:
        sign = 1 if c.mutation == 'dual-sign' else -1
        k = tuple(sign*m.psi(m.dot(b, e)) % f.p for e in basis)
        for x in g.elements:
            c.check('R1', g.ev(k, x) == -m.psi(m.dot(b, x)) % f.p,
                    f'dual evaluation q={f.q}, rank={rank}, b={b}, x={x}')
        duals[b] = k
    c.check('R1', len(set(duals.values())) == len(g.elements),
            f'character pairing not bijective q={f.q}, rank={rank}')
    for a, b in product(g.elements, repeat=2):
        inherited = g.operator(a, duals[b])
        phase = m.cochain(a, b) * (-1 if c.mutation == 'rephase' else 1)
        transported = scale(g, inherited, phase)
        proposed = m.wave(a, b, c.mutation == 'position-labels')
        c.check('R2', proposed == transported,
                f'labeled wave/reference conversion q={f.q}, rank={rank}, a={a}, b={b}')
        m.ops[a, b] = proposed
    for (a, b), (ap, bp) in product(m.ops, repeat=2):
        omega = f.ADD[m.dot(a, bp)][f.NEG[m.dot(ap, b)]]
        exponent = m.psi(f.MUL[m.half][omega])
        if c.mutation == 'cocycle':
            exponent = -exponent
        expected = scale(g, m.ops[g.add(a, ap), g.add(b, bp)], exponent)
        c.check('R3', compose(g, m.ops[a, b], m.ops[ap, bp]) == expected,
                f'half-form multiplication q={f.q}, rank={rank}')
    kernel = {t for t in range(f.q) if m.psi(t) == 0}
    expected_kernel_size = 1 if c.mutation == 'central-injective' else f.q // f.p
    c.check('R3', len(kernel) == expected_kernel_size,
            f'raw-center kernel q={f.q}: actual {len(kernel)}, expected {expected_kernel_size}')
    # Check the actual central quotient map on every t and every phase label.
    for a, b in m.ops:
        image = {(m.psi(t) + m.cochain(a, b)) % f.p for t in range(f.q)}
        c.check('R3', image == set(range(f.p)), 'central quotient not onto')
    dim = len(g.elements)
    zero_label = (g.zero, g.zero)
    zero_operator = m.ops[zero_label]
    if c.mutation == 'vacuum' and rank == 0:
        zero_operator = scale(g, zero_operator, 1)
    identity = tuple((x, 0) for x in g.elements)
    c.check('R4', zero_operator == identity,
            f'actual zero-label operator is not identity q={f.q}, rank={rank}')
    for label, op in m.ops.items():
        actual_trace = phase_sum([e for x, (y, e) in zip(g.elements, op) if x == y], f.p)
        normalized_trace = [Fraction(coefficient, dim) for coefficient in actual_trace]
        coefficient_trace = int(label == zero_label)
        if c.mutation == 'trace-normalization' and label == zero_label:
            coefficient_trace = dim
        c.check('R4', normalized_trace == [coefficient_trace],
                f'entry-derived normalized trace versus coefficient trace q={f.q}, rank={rank}, label={label}')
    family = list(m.ops.values())
    for i, op in enumerate(family):
        for j, oq in enumerate(family):
            trace = phase_sum([e2-e1 for (x,e1),(y,e2) in zip(op,oq) if x == y], f.p)
            c.check('R4', trace == ([dim] if i == j else [0]), 'operator trace Gram')
    return m


def tensors(c, models):
    for r, s in ((0, 1), (1, 0), (1, 1)):
        left, right, whole = [models[3, 1, n, 1] for n in (r, s, r+s)]
        for (a,b), (ap,bp) in product(left.ops, right.ops):
            op1, op2 = left.ops[a,b], right.ops[ap,bp]
            dropped = right.cochain(ap, bp) if c.mutation == 'tensor-phase' else 0
            tensored = tuple((x+y, (e+f-dropped) % 3)
                             for x,e in op1 for y,f in op2)
            c.check('R5', whole.ops[a+ap,b+bp] == tensored,
                    f'inherited product comparison ranks {r}+{s}')


def relative_character(c):
    f = GF(3, 4)
    add, mul, neg = f.ADD, f.MUL, f.NEG
    base = [x for x in range(f.q) if f.pow(x, 9) == x]
    parameter = next(x for x in base if f.pow(x, 3) != x)
    def base_character(x):
        y = mul[parameter][x]
        return add[y][f.pow(y, 3)]
    def trace(x):
        return add[x][f.pow(x, 9)]
    def character(x):
        return f.TR[x] if c.mutation == 'character-conflation' else f.TR[mul[parameter][x]]
    c.check('R6', len(base) == 9, 'wrong fixed subfield')
    c.check('R6', {base_character(x) for x in base} == {0,1,2}, 'base character nontriviality')
    for x in range(f.q):
        c.check('R6', trace(x) in base and character(x) == base_character(trace(x)),
                'relative character confused with fixed absolute-trace character')
    c.check('R6', any(character(x) != f.TR[x] for x in range(f.q)),
            'nonstandard character witness lost')
    power = 3 if c.mutation == 'relative-frobenius' else 9
    inverse_power = 27 if power == 3 else 9
    def action(a, b, y):
        e = character(add[neg[mul[b][y]]][neg[mul[2][mul[a][b]]]])
        return add[y][a], e
    labels = (0, 1, parameter, next(x for x in range(f.q) if x not in base))
    for a, b, y in product(labels, labels, range(f.q)):
        z, phase = action(a, b, f.pow(y, inverse_power))
        actual = f.pow(z, power), phase
        expected = action(f.pow(a, power), f.pow(b, power), y)
        c.check('R6', actual == expected, 'absolute power substituted for relative Frobenius')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    red = parser.add_mutually_exclusive_group()
    for name, gate in MUTATIONS.items():
        red.add_argument('--red-' + name, dest='mutation', action='store_const', const=name,
                         help='must fail at ' + gate)
    args = parser.parse_args()
    c = Checks(args.mutation)
    try:
        models = {}
        for p, degree, ranks in ((3,1,(0,1,2)), (5,1,(0,1)), (3,2,(0,1))):
            f = GF(p, degree)
            for rank in ranks:
                for parameter in range(1, f.q):
                    chosen = 0 if args.mutation == 'trivial-character' else parameter
                    models[p,degree,rank,parameter] = finite_model(c, f, rank, chosen)
        tensors(c, models)
        relative_character(c)
        for gate, count in sorted(c.counts.items()):
            print(f'{gate} PASS: {count} exact comparisons')
        print('PASS: finite reuse interfaces only; no claim promotion')
        return 0
    except Failure as e:
        print(f'{e.gate} FAIL: {e.detail}')
        if args.mutation and MUTATIONS[args.mutation] != e.gate:
            print('WRONG GATE: expected ' + MUTATIONS[args.mutation])
            return 2
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
