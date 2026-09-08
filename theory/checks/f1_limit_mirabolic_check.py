#!/usr/bin/env python3
"""Exact rank-two affine, vector expectation and decomposable-flag probes.

Prime-field arithmetic, integer orbital matrices and rational coefficients.
Endpoint multiplication is cubic interpolation with the stated counting
degree bound; no floating point or positivity-by-sampling claim is used.
"""
import argparse
from fractions import Fraction as F
from itertools import product
import numpy as np


CHECKED, FAILED = {}, {}
LABELS = ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3))


def need(condition, gate, diagnostic):
    CHECKED[gate] = CHECKED.get(gate, 0)+1
    if not condition:
        FAILED.setdefault(gate, set()).add(diagnostic)


def rank(rows):
    a = [list(map(F, row)) for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        lead = a[r][j]
        a[r] = [x/lead for x in a[r]]
        for i in range(len(a)):
            if i != r:
                lead = a[i][j]
                a[i] = [x-lead*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def canonical_line(x, p):
    lead = next(a for a in x if a)
    return tuple(a*pow(lead, -1, p) % p for a in x)


def action(g, x, p):
    return ((g[0]*x[0]+g[1]*x[1]) % p,
            (g[2]*x[0]+g[3]*x[1]) % p)


def inverse(g, p):
    d = pow((g[0]*g[3]-g[1]*g[2]) % p, -1, p)
    return (d*g[3] % p, -d*g[1] % p, -d*g[2] % p, d*g[0] % p)


class Affine:
    def __init__(self, p):
        self.p = p
        self.lines = tuple((1, a) for a in range(p))+((0, 1),)
        self.vectors = tuple(product(range(p), repeat=2))
        self.points = tuple(product(range(p+1), self.vectors))
        self.index = {x: i for i, x in enumerate(self.points)}
        self.line_index = {x: i for i, x in enumerate(self.lines)}
        self.size = len(self.points)
        self.ref = self.index[0, (0, 0)]
        self.types = np.empty((self.size, self.size), dtype=np.int64)
        for i, (f, x) in enumerate(self.points):
            a, b = self.lines[f]
            g = (a, 0, b, 1) if a else (0, 1, 1, 0)
            gi = inverse(g, p)
            for j, (ff, xx) in enumerate(self.points):
                line = canonical_line(action(gi, self.lines[ff], p), p)
                v = action(gi, ((xx[0]-x[0]) % p, (xx[1]-x[1]) % p), p)
                self.types[i, j] = LABELS.index(self.reference_label(line, v))
        self.mats = tuple((self.types == k).astype(np.int64) for k in range(7))
        self.reps = tuple(int(np.flatnonzero(self.mats[k][self.ref])[0]) for k in range(7))
        self.constants = tuple(tuple(tuple(int(self.mats[i][self.ref] @ self.mats[j][:, r])
                                           for r in self.reps) for j in range(7)) for i in range(7))

    def reference_label(self, line, v):
        p = self.p
        if line == (1, 0):
            return (0, 2 if v[1] else (1 if v[0] else 0))
        a, b = line
        bi = pow(b, -1, p)
        y = ((v[0]-a*bi*v[1]) % p, bi*v[1] % p)
        return (1, int(bool(y[0]))+2*int(bool(y[1])))

    def coefficients(self, matrix):
        return tuple(F(matrix[self.ref, r]) for r in self.reps)

    def reconstruct(self, coefficients):
        result = np.zeros((self.size, self.size), dtype=object)
        for c, a in zip(coefficients, self.mats):
            result += c*a
        return result

    def zero_vector_part(self, a):
        return np.array([[a[i, j] if x == xx else 0 for j, (_, xx) in enumerate(self.points)]
                         for i, (_, x) in enumerate(self.points)], dtype=object)


def kernel_and_generators(model, args):
    p, size, ref = model.p, model.size, model.ref
    identity = np.eye(size, dtype=np.int64)
    need(np.array_equal(model.mats[0], identity), 'B1', 'diagonal affine orbital is the unit')
    expected_valencies = (1, p-1, p*(p-1), p, p*(p-1), p*(p-1), p*(p-1)**2)
    for k, a in enumerate(model.mats):
        need(np.all(a.sum(axis=1) == expected_valencies[k]), 'B1', 'constant affine orbital valency')
        need(any(np.array_equal(a.T, b) for b in model.mats), 'B1', 'orbital adjoint closes')
        for j, b in enumerate(model.mats):
            value = F(int(np.trace(a.T@b)), size)
            need(value == (expected_valencies[k] if k == j else 0), 'B1', 'physical orbital trace Gram')
    for i, j in product(range(7), repeat=2):
        a, b = model.mats[i], model.mats[j]
        matrix_product_row = a[ref]@b
        for target, (ff, v) in enumerate(model.points):
            total = 0
            for h in range(p+1):
                for u in model.vectors:
                    difference = v if args.red_mir_kernel else ((v[0]-u[0]) % p, (v[1]-u[1]) % p)
                    total += int(a[ref, model.index[h, u]])*int(b[model.index[h, (0, 0)], model.index[ff, difference]])
            need(total == matrix_product_row[target], 'B1', 'vector-addition convolution equals kernel composition')
    t0, t1 = model.mats[1], model.mats[3]
    need(np.array_equal(t0@t0, (p-2)*t0+(p-1)*identity), 'B2', 'mirabolic boundary-generator quadratic')
    need(np.array_equal(t1@t1, (p-1)*t1+p*identity), 'B2', 'flag-generator quadratic')
    controlled = np.zeros((size, size), dtype=object)
    for i, (f, x) in enumerate(model.points):
        line = model.lines[0 if args.red_mir_line else f]
        for c in range(p):
            xx = ((x[0]+c*line[0]) % p, (x[1]+c*line[1]) % p)
            controlled[i, model.index[f, xx]] += F(1, p)
    expected = F(1, p)*(identity+t0)
    need(np.array_equal(controlled, expected), 'B2', 'controlled flag-line translation is Rosso projection')
    need(np.array_equal(controlled@controlled, controlled)
         and F(np.trace(controlled), size) == F(1, p), 'B2', 'controlled projection and physical trace')
    basis = [identity]
    coordinate_rows = [model.coefficients(identity)]
    for candidate in basis:
        for generator in (t0, t1):
            value = candidate@generator
            coefficients = model.coefficients(value)
            need(np.array_equal(value, model.reconstruct(coefficients)), 'B2', 'generator word remains invariant')
            if rank(coordinate_rows+[coefficients]) > len(basis):
                basis.append(value)
                coordinate_rows.append(coefficients)
    need(len(basis) == 7, 'B2', 'Hecke and controlled line generate the whole commutant')


def expectation(model, args):
    p, size = model.p, model.size
    diagonal_projections = [np.diag([int(x == v) for _, x in model.points]) for v in model.vectors]
    need(np.array_equal(sum(diagonal_projections), np.eye(size)), 'B4', 'vector dephasing has complete projection Kraus list')
    for k, a in enumerate(model.mats):
        keep = k in (0, 3) or args.red_mir_expect
        coefficients = a if keep else np.zeros((size, size), dtype=np.int64)
        dephased = sum(d@a@d for d in diagonal_projections)
        need(np.array_equal(coefficients, dephased), 'B4', 'vector expectation equals Weyl dephasing')
        need(np.trace(coefficients) == np.trace(a), 'B4', 'vector expectation preserves physical trace')
        for left, right in product((model.mats[0], model.mats[3]), repeat=2):
            need(np.array_equal(model.zero_vector_part(left@a@right), left@dephased@right),
                 'B4', 'Hecke bimodule identity')


def endpoint(models, args):
    primes = tuple(m.p for m in models)
    weights = [np.prod([F(1-r, p-r) for r in primes if r != p]) for p in primes]
    constants = [[[sum(w*m.constants[i][j][k] for w, m in zip(weights, models))
                   for k in range(7)] for j in range(7)] for i in range(7)]
    # Structure coefficients are polynomial and bounded by |Y|=q^2(q+1),
    # so degree <=3. Four arithmetic values therefore determine evaluation1.
    for i, j in product(range(7), repeat=2):
        projected = [constants[i][j][0], constants[i][j][3]]
        expected = [F(0), F(0)]
        if i in (0, 3) and j in (0, 3):
            expected[int((i == 3) != (j == 3))] = 1
        if args.red_mir_expect and (i, j) == (1, 1):
            projected[0] += 1
        need(projected == expected, 'B4', 'rank-two reference quotient multiplies as C[S2]')
    transpose = [next(j for j, b in enumerate(models[0].mats) if np.array_equal(a.T, b))
                 for a in models[0].mats]
    for i, j in product(range(7), repeat=2):
        gram = constants[transpose[i]][j][0]
        need(gram == int(i == j and i in (0, 3)), 'B4', 'endpoint Gram has exactly the five vector-null directions')


def affine_decomposable(model, args):
    p, size = model.p, model.size
    axes = (model.line_index[(1, 0)], model.line_index[(0, 1)])
    indices = [model.index[axes[s], (x, y)] for x, y, s in product(range(p), range(p), range(2))]
    d = len(indices)
    fraction = F(d, size)
    projector = np.zeros((size, size), dtype=np.int64)
    projector[indices, indices] = 1
    local = (np.eye(p, dtype=np.int64), np.ones((p, p), dtype=np.int64)-np.eye(p, dtype=np.int64))
    arenas = []
    for a, b, row, col in product(local, local, range(2), range(2)):
        unit = np.zeros((2, 2), dtype=np.int64)
        unit[row, col] = 1
        arenas.append(np.kron(np.kron(a, b), unit))
    need(d == 2*p*p and size == (p+1)*p*p and len(arenas) == 16,
         'B7', 'affine product-shuffle corner dimensions')
    sums = [int(a.sum()) for a in model.mats]
    def average_coefficients(x):
        return [F(sum(x[i, j] for i, j in zip(*np.nonzero(a))), count)
                for a, count in zip(model.mats, sums)]
    averaged_p = average_coefficients(projector)
    need(averaged_p == [fraction]+[F(0)]*6, 'B7', 'affine transitive average of decomposable projection')
    scale = F(1) if args.red_affine_dec else 1/fraction
    need([scale*x for x in averaged_p] == [F(1)]+[F(0)]*6, 'B7', 'scaled affine preparation is unital')
    for a in model.mats:
        compressed = a[np.ix_(indices, indices)]
        reconstructed = np.zeros_like(compressed)
        for b in arenas:
            row, col = next(zip(*np.nonzero(b)))
            reconstructed += int(compressed[row, col])*b
        need(np.array_equal(compressed, reconstructed), 'B7', 'compressed affine observable belongs to product-shuffle arena')
        for b in arenas:
            extended = np.zeros((size, size), dtype=np.int64)
            extended[np.ix_(indices, indices)] = b
            coefficients = [scale*x for x in average_coefficients(extended)]
            lhs = F(int(np.trace(compressed.T@b)), d)
            rhs = sum(c*F(int(np.trace(a.T@v)), size) for c, v in zip(coefficients, model.mats))
            need(lhs == rhs, 'B7', 'affine compression and averaging are normalized trace adjoints')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name, help_text in {
        'mir-kernel': 'B1: omit the intermediate vector from convolution',
        'mir-line': 'B2: use a fixed coordinate line instead of the flag line',
        'mir-expect': 'B4: retain nonzero-vector coefficients in expectation',
        'affine-dec': 'B7: omit the affine decomposable-fraction inverse',
    }.items():
        parser.add_argument('--red-'+name, action='store_true', help=help_text)
    args = parser.parse_args()
    print('MODE:', ','.join(k for k, v in vars(args).items() if v) or 'green')
    models = [Affine(p) for p in (2, 3, 5, 7)]
    for model in models[:2]:
        kernel_and_generators(model, args)
        expectation(model, args)
        affine_decomposable(model, args)
    endpoint(models, args)
    for gate in ('B1', 'B2', 'B4', 'B7'):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED.get(gate, 0)} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL AFFINE AND MIRABOLIC PROBES PASSED')


if __name__ == '__main__':
    main()
