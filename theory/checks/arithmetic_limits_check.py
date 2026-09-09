#!/usr/bin/env python3
"""Independent finite G/F/R/M falsifiers; exact stdlib + numpy arithmetic.

--red NAME exits 1 at a mathematical gate. --matrix runs reds before green.
Finite enumeration is evidence only for the explicitly recorded samples.
"""
import argparse
from fractions import Fraction as F
from itertools import permutations, product
from math import comb
import json
import numpy as np

MUTATIONS = {
    'coset-label': 'G1', 'omit-normalization': 'G1', 'cyclic-only-image': 'G1',
    'omit-tensor-outcome': 'G2', 'erase-orbit-coherence': 'G2',
    'merge-tower-histories': 'G2', 'admit-nonuniform': 'G3',
    'trace-fibre-label': 'F1', 'wrong-gram-branch': 'F1',
    'omit-degree-scaling': 'F2', 'fourier-sign': 'F2',
    'fourier-scaling': 'F2', 'wrong-failure-projector': 'F2',
    'physical-support-rank': 'R1', 'compress-mixed-transition': 'M1',
    'omit-tangent-normalization': 'R2', 'collapse-tangent-algebra': 'R2',
    'tangent-fourier': 'R2', 'incomplete-tangent-instrument': 'R2',
    'tower-degree-scaling': 'F3', 'tower-connector-coefficient': 'R3',
    'residual-fourier-reflection': 'F2',
}


class Failure(Exception):
    def __init__(self, gate, detail):
        self.gate, self.detail = gate, detail


class Checks:
    def __init__(self, red=None):
        self.red, self.counts, self.records = red, {}, {}

    def check(self, gate, condition, detail):
        self.counts[gate] = self.counts.get(gate, 0) + 1
        if not condition:
            raise Failure(gate, detail)


def eq(a, b):
    return np.array_equal(a, b)


def eye(n):
    return np.eye(n, dtype=np.int64)


def inc(mapping, n):
    a = np.zeros((len(mapping), n), dtype=np.int64)
    for y, x in enumerate(mapping):
        a[y, x] = 1
    return a


def perm(mapping):
    return inc(mapping, len(mapping)).T


def outer(x, y):
    return np.outer(x, y)


def inverse(a):
    n = len(a)
    b = [[F(a[i, j]) for j in range(n)] + [F(i == j) for j in range(n)]
         for i in range(n)]
    for j in range(n):
        k = next(k for k in range(j, n) if b[k][j])
        b[j], b[k] = b[k], b[j]
        z = b[j][j]
        b[j] = [x / z for x in b[j]]
        for k in range(n):
            if k != j:
                z = b[k][j]
                b[k] = [x - z*y for x, y in zip(b[k], b[j])]
    return np.array([row[n:] for row in b], dtype=object)


def pivots(a):
    a = [[F(x) for x in row] for row in a]
    row, cols = 0, []
    for j in range(len(a[0])):
        k = next((k for k in range(row, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[row], a[k] = a[k], a[row]
        z = a[row][j]
        a[row] = [x/z for x in a[row]]
        for k in range(row + 1, len(a)):
            z = a[k][j]
            a[k] = [x-z*y for x, y in zip(a[k], a[row])]
        cols.append(j)
        row += 1
        if row == len(a):
            break
    return cols


def galois(c):
    G = list(permutations(range(3)))
    ident = tuple(range(3))
    mul = lambda g, h: tuple(g[h[i]] for i in range(3))
    inv = lambda g: tuple(g.index(i) for i in range(3))
    H = {ident, (1, 0, 2)}
    cosets = sorted({tuple(sorted(mul(g, h) for h in H)) for g in G})
    quotient = [next(i for i, x in enumerate(cosets) if g in x) for g in G]
    B = inc(quotient, 3)
    if c.red == 'coset-label':
        B[[0, 1]] = B[[1, 0]]
    r = 1 if c.red == 'omit-normalization' else 2
    c.check('G1', eq(B.T @ B, r*eye(3)), 'S3 pullback squared norm')
    core = set.intersection(*[{mul(mul(g, h), inv(g)) for h in H} for g in G])
    actions = []
    for g in G:
        gy = perm([G.index(mul(g, h)) for h in G])
        gx = perm([cosets.index(tuple(sorted(mul(g, h) for h in x))) for x in cosets])
        actions.append(tuple(gx.ravel()))
        c.check('G1', eq(gy @ B, B @ gx), 'S3 regular/coset equivariance')
    if c.red == 'cyclic-only-image':
        rotation = (1, 2, 0)
        cyclic = {ident, rotation, mul(rotation, rotation)}
        actions = [action for g, action in zip(G, actions) if g in cyclic]
    image_order = len(set(actions))
    c.check('G1', core == {ident} and image_order == 6, 'S3 normal core and image')
    Pnum = B @ B.T
    c.check('G1', F(int(np.trace(Pnum)), 2*6) == F(1, 2), 'S3 reference success')
    tower_count = 0
    for z in range(1, 13):
        for y in range(1, z+1):
            for x in range(1, y+1):
                if z % y or y % x:
                    continue
                byz = inc([k % y for k in range(z)], y)
                bxy = inc([k % x for k in range(y)], x)
                bxz = inc([k % x for k in range(z)], x)
                c.check('G1', eq(byz @ bxy, bxz), f'cyclic tower {x}|{y}|{z}')
                c.check('G1', eq(bxz.T @ bxz, (z//x)*eye(x)), 'cyclic norm')
                c.check('G1', eq(perm([(k+1) % z for k in range(z)]) @ bxz,
                                     bxz @ perm([(k+1) % x for k in range(x)])), 'cyclic action')
                tower_count += 1
    # Numerator Kraus matrices with squared amplitude denominators.
    branches = {'s': (B.T, 2), 'f': (2*eye(6)-Pnum, 4)}
    for i, j in product(range(6), repeat=2):
        outputs = [outer(a[:, i], a[:, j])*F(1, d) for a, d in branches.values()]
        c.check('G2', sum(np.trace(x) for x in outputs) == (i == j), 'decoder matrix-unit trace')
    for g in G:
        gy = perm([G.index(mul(g, h)) for h in G])
        gx = perm([cosets.index(tuple(sorted(mul(g, h) for h in x))) for x in cosets])
        for tag, (A, denom) in branches.items():
            output_action = gx if tag == 's' else gy
            for i, j in product(range(6), repeat=2):
                c.check('G2', eq(outer((A @ gy)[:, i], (A @ gy)[:, j]),
                                 output_action @ outer(A[:, i], A[:, j]) @ output_action.T),
                        'S3 decoder equivariance on every matrix unit and both tags')
    c.check('G2', eq(B.T @ B, 2*eye(3)) and not np.any(branches['f'][0] @ B),
            'encoded inputs decode identically with zero failure')
    parallel = {a+b: (np.kron(x, y), d*e)
                for a, (x, d) in branches.items() for b, (y, e) in branches.items()}
    if c.red == 'omit-tensor-outcome':
        del parallel['sf']
    c.check('G2', set(parallel) == {'ss', 'sf', 'fs', 'ff'}, 'four typed outcomes')
    completeness = sum(a.T @ a * F(1, d) for a, d in parallel.values())
    c.check('G2', eq(completeness, eye(36)), 'tensor Kraus completeness')
    for i, j in product(range(36), repeat=2):
        c.check('G2', sum(F(int(a[:, j] @ a[:, i]), d) for a, d in parallel.values())
                == (i == j), 'independent matrix-unit trace')
        ii, iii = divmod(i, 6)
        jj, jjj = divmod(j, 6)
        for tag, (a, d) in parallel.items():
            left, dl = branches[tag[0]]
            right, dr = branches[tag[1]]
            c.check('G2', d == dl*dr and eq(outer(a[:, i], a[:, j]),
                    np.kron(outer(left[:, ii], left[:, jj]),
                            outer(right[:, iii], right[:, jjj]))), 'tensor matrix-unit CP map')
    probs = {t: str(F(int(np.trace(a.T @ a)), d*36)) for t, (a, d) in parallel.items()}
    c.check('G2', set(probs.values()) == {'1/4'}, 'independent reference probabilities')
    factors = [inc([0, 0], 1), inc([0, 1, 0, 1], 2), inc([0, 0], 1)]
    tensor = np.kron(np.kron(*factors[:2]), factors[2])
    direct = inc([j % 2 for i, j, k in product(range(2), range(4), range(2))], 2)
    c.check('G2', eq(tensor, direct) and eq(tensor, np.kron(factors[0], np.kron(*factors[1:]))),
            'ternary Cartesian comparisons')
    lower = [inc([0, 0], 1), inc([0, 0, 0], 1), inc([0, 0], 1)]
    upper = [inc([0, 1, 0, 1], 2), inc([0, 1, 2, 0, 1, 2], 3), eye(2)]
    kron3 = lambda xs: np.kron(np.kron(xs[0], xs[1]), xs[2])
    c.check('G2', eq(kron3(upper) @ kron3(lower), kron3([u @ l for u, l in zip(upper, lower)])),
            'ternary tensor of two-stage towers')
    # Coherence across simultaneous-shift orbits {00,11}, {01,10}.
    v = np.array([1, 1, 0, 0]); rho = outer(v, v)*F(1, 2)
    orbit = [0, 1, 1, 0]
    dephased = np.array([[rho[i, j] if orbit[i] == orbit[j] else F(0)
                         for j in range(4)] for i in range(4)], dtype=object)
    actual = dephased if c.red == 'erase-orbit-coherence' else rho
    c.check('G2', np.trace(rho @ actual) == 1 and np.trace(rho @ dephased) == F(1, 2),
            'cross-orbit Born coherence')
    # Strict 1|2|4 tower, all calculations on the common four-point register.
    t = inc([0, 1, 0, 1], 2); s = inc([0, 0], 1)
    pt = t @ t.T * F(1, 2); pc = t @ s @ s.T @ t.T * F(1, 4)
    R, Q = pt-pc, eye(4)-pt
    histories_kraus = [(s.T @ t.T, 4), ((2*eye(2)-s @ s.T) @ t.T, 8), (2*eye(4)-t @ t.T, 4)]
    c.check('G2', eq(sum(A.T @ A*F(1, d) for A, d in histories_kraus), eye(4)),
            'actual typed stopped-history Kraus completeness')
    c.check('G2', eq(histories_kraus[0][0], (t @ s).T), 'tower final success amplitude composes')
    c.check('G2', eq(pc + R @ R + Q @ Q, eye(4)), 'three stopped-history completeness')
    v = np.array([2, -1, 0, -1]); rho = outer(v, v)*F(1, 6)
    stopped = R @ rho @ R + Q @ rho @ Q
    binary = (R+Q) @ rho @ (R+Q)
    actual = binary if c.red == 'merge-tower-histories' else stopped
    c.check('G2', not eq(actual, binary) and np.trace(stopped) == np.trace(binary),
            'tower merged failures lose cross terms')
    c.check('G2', np.trace(rho @ stopped) == F(5, 9) and np.trace(rho @ binary) == 1,
            'tower retained-history versus binary Born return')
    # Nonuniform 3->2->1: separate normalization does not compose.
    fibres = [1, 2]
    if c.red == 'admit-nonuniform':
        fibres = [F(3, 2), F(3, 2)]
    local_squares = [F(1, 2)/fibres[k] for k in [0, 1, 1]]
    c.check('G3', len(set(fibres)) > 1 and local_squares != [F(1, 3)]*3,
            'nonuniform normalized pullbacks fail composition')
    c.check('G3', sum(local_squares) == 1, 'nonuniform individual pullback remains isometric')
    c.records['G'] = {'S3_core_order': len(core), 'S3_action_order': image_order,
        'cyclic_towers_max_order': 12, 'cyclic_towers': tower_count,
        'tensor_probabilities': probs, 'tensor_matrix_units': 36**2,
        'nonuniform_composite_squared_column': list(map(str, local_squares)),
        'direct_squared_column': ['1/3']*3, 'tower_failure_cross_terms': 'distinct'}
    c.records['G']['tower_history_Born_return'] = '5/9'
    c.records['G']['binary_composite_Born_return'] = '1'


class Field:
    """Polynomial quotient, labels are little-endian base-p coefficients."""
    def __init__(self, p, modulus):
        self.p, self.mod = p, modulus
        self.d, self.q = len(modulus)-1, p**(len(modulus)-1)
        self.coeff = [tuple((x//p**i) % p for i in range(self.d)) for x in range(self.q)]
        self.add = [[self.encode([(a+b) % p for a, b in zip(x, y)])
                     for y in self.coeff] for x in self.coeff]
        self.mul = [[self.multiply(x, y) for y in self.coeff] for x in self.coeff]
        assert all(any(self.mul[x][y] == 1 for y in range(1, self.q)) for x in range(1, self.q))

    def encode(self, cs):
        return sum(x*self.p**i for i, x in enumerate(cs))

    def multiply(self, x, y):
        cs = [0]*(2*self.d-1)
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                cs[i+j] = (cs[i+j]+a*b) % self.p
        for j in range(len(cs)-1, self.d-1, -1):
            for i in range(self.d):
                cs[j-self.d+i] = (cs[j-self.d+i]-cs[j]*self.mod[i]) % self.p
        return self.encode(cs[:self.d])

    def power(self, x, n):
        out = 1
        while n:
            if n % 2:
                out = self.mul[out][x]
            x, n = self.mul[x][x], n//2
        return out

    def summation(self, xs):
        out = 0
        for x in xs:
            out = self.add[out][x]
        return out

    def absolute_trace(self, x):
        return self.summation(self.power(x, self.p**i) for i in range(self.d))


def embedding(k, e):
    for root in range(e.q):
        value = e.summation(e.mul[a][e.power(root, i)] for i, a in enumerate(k.mod))
        if value == 0:
            out = [e.summation(e.mul[a][e.power(root, i)] for i, a in enumerate(cs))
                   for cs in k.coeff]
            if len(set(out)) == k.q:
                return out
    raise ValueError('no embedding found')


class Zeta:
    """Exact Q(omega), omega^2+omega+1=0; Q and p=2 included."""
    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)
    @staticmethod
    def cast(x):
        return x if isinstance(x, Zeta) else Zeta(x)
    def __add__(self, x):
        x = self.cast(x); return Zeta(self.a+x.a, self.b+x.b)
    __radd__ = __add__
    def __neg__(self):
        return Zeta(-self.a, -self.b)
    def __sub__(self, x):
        return self + (-self.cast(x))
    def __rsub__(self, x):
        return self.cast(x) + (-self)
    def __mul__(self, x):
        x = self.cast(x)
        return Zeta(self.a*x.a-self.b*x.b, self.a*x.b+self.b*x.a-self.b*x.b)
    __rmul__ = __mul__
    def __eq__(self, x):
        x = self.cast(x); return (self.a, self.b) == (x.a, x.b)
    def __bool__(self):
        return bool(self.a or self.b)
    def conjugate(self):
        return Zeta(self.a-self.b, -self.b)
    def __repr__(self):
        return f'({self.a}+{self.b}w)'


def dagger(a):
    return np.array([[x.conjugate() if isinstance(x, Zeta) else x for x in row]
                     for row in a.T], dtype=object)


def characters(k, sign=-1):
    roots = [Zeta(1), Zeta(-1)] if k.p == 2 else [Zeta(1), Zeta(0, 1), Zeta(-1, -1)]
    return np.array([[roots[(sign*k.absolute_trace(k.mul[x][y])) % k.p]
                      for y in range(k.q)] for x in range(k.q)], dtype=object)


def finite_fields(c):
    f2, f3 = Field(2, [0, 1]), Field(3, [0, 1])
    f4, f8 = Field(2, [1, 1, 1]), Field(2, [1, 1, 0, 1])
    f9, f16 = Field(3, [1, 0, 1]), Field(2, [1, 1, 0, 0, 1])
    f27 = Field(3, [1, 2, 0, 1])
    samples = [(f2, f4), (f2, f8), (f3, f9), (f4, f16), (f3, f27)]
    records = []
    for k, e in samples:
        n, kap, q, Q = e.d//k.d, e.q//k.q, k.q, e.q
        emb = embedding(k, e)
        trace = [emb.index(e.summation(e.power(x, q**j) for j in range(n))) for x in range(Q)]
        J, B = inc(list(range(q)), q), inc(trace, q)
        J = np.zeros((Q, q), dtype=np.int64)
        for x, y in enumerate(emb):
            J[y, x] = 1
        if c.red == 'trace-fibre-label' and Q == 4:
            B = np.roll(B, 1, axis=1)
        c.check('F1', eq(J.T @ J, eye(q)) and eq(B.T @ B, kap*eye(q)), 'field isometries')
        nx = [k.mul[n % k.p][x] for x in range(q)]
        expected = inc(nx, q)
        gram = J.T @ B
        c.check('F1', eq(gram, expected), f'actual F{q}->F{Q} trace-fibre Gram')
        invertible = n % k.p != 0
        gram_square = gram @ gram.T * F(1, kap)
        lam = F(1, kap) if invertible else F(q, kap)
        if c.red == 'wrong-gram-branch' and not invertible:
            lam = F(1, kap)
        c.check('F1', eq(gram_square @ gram_square, lam*gram_square), 'squared singular spectrum')
        c.check('F1', len(pivots(gram)) == (q if invertible else 1), 'Gram rank')
        P, R = J @ J.T, B @ B.T * F(1, kap)
        both = np.concatenate([J, B], axis=1)
        W = both[:, pivots(both)]
        support = W @ inverse(W.T @ W) @ W.T
        rank = len(W.T)
        expected_rank = 2*q - (1 if not invertible and q == kap else 0)
        c.check('F1', rank == expected_rank and eq(support @ support, support), 'joint support rank')
        c.check('F1', eq(support @ P, P) and eq(support @ R, R), 'joint support projection')
        c.check('F1', eq(P @ R @ P @ R @ P, lam*(P @ R @ P)), 'projection principal-angle relation')
        # Generate the rational algebra from the actual ambient projections.
        basis = [eye(Q), P, R]
        while True:
            candidates = basis+[X @ Y for X in basis for Y in [P, R]]
            selected = pivots(np.array([X.ravel() for X in candidates], dtype=object).T)
            extended = [candidates[i] for i in selected]
            if len(extended) == len(basis):
                break
            basis = extended
        expected_algebra = 5 if invertible else (4 if q == kap else 7)
        c.check('F1', len(basis) == expected_algebra, 'actual generated projection algebra dimension')
        if invertible:
            central = [support, eye(Q)-support]
            expected_weights = [F(2*q, Q), F(Q-2*q, Q)]
        elif q == kap:
            a = J @ np.ones(q, dtype=np.int64)
            common = outer(a, a)*F(1, q)
            central = [common, P-common, R-common, eye(Q)-support]
            expected_weights = [F(1, Q), F(q-1, Q), F(q-1, Q), F(Q-2*q+1, Q)]
        else:
            plane = np.array([J @ np.ones(q, dtype=np.int64), B[:, 0]]).T
            C = plane @ inverse(plane.T @ plane) @ plane.T
            central = [C, P-C @ P, R-C @ R, eye(Q)-support]
            expected_weights = [F(2, Q), F(q-1, Q), F(q-1, Q), F(Q-2*q, Q)]
        c.check('F1', eq(sum(central), eye(Q)), 'central block identities sum to ambient identity')
        for i, Z in enumerate(central):
            c.check('F1', eq(Z @ Z, Z) and eq(Z @ P, P @ Z) and eq(Z @ R, R @ Z)
                    and F(np.trace(Z), Q) == expected_weights[i], 'actual central block physical trace')
        ce, ck = characters(e, 1 if c.red == 'fourier-sign' and k.p == 3 else -1), characters(k)
        c.check('F2', eq(ce @ dagger(ce), Q*eye(Q)), 'exact Fourier orthogonality')
        c.check('F2', eq(ce @ J, B @ ck), 'F_E J = V F_K character/scalar equality')
        scale = 1 if c.red == 'fourier-scaling' else kap
        c.check('F2', eq(ce @ B, scale*J @ ck), 'F_E V = J F_K character/scalar equality')
        ue, uk = perm([e.power(x, e.p) for x in range(Q)]), perm([k.power(x, k.p) for x in range(q)])
        c.check('F2', eq(ue @ J, J @ uk) and eq(ue @ B, B @ uk), 'Frobenius transfers')
        c.check('F2', eq(ue @ ce, ce @ ue), 'Frobenius Fourier commutation')
        c.check('F2', eq(np.linalg.matrix_power(ue, k.d) @ support, support),
                'joint chart support sees only lower-field Frobenius order')
        c.check('F2', np.trace(ue @ support) == 2*np.trace(uk)-(2*q-rank),
                'joint-support Frobenius character including common invariant line')
        # CP success branches on every ambient matrix unit, with denominators
        # Q and kap*q equal. Comparing actual scaled Kraus columns is exact.
        success_left, success_right = B.T @ ce, ck @ J.T
        c.check('F2', eq(success_left, kap*success_right), 'Fourier decoder success amplitudes')
        failure = eye(Q)-P if c.red == 'wrong-failure-projector' else eye(Q)-R
        left, right = failure @ ce, ce @ (eye(Q)-P)
        c.check('F2', eq(left, right), 'Fourier decoder retained failure amplitude')
        for i, j in product(range(Q), repeat=2):
            c.check('F2', eq(outer(success_left[:, i], dagger(success_left[:, j:j+1])[0]),
                             kap**2*outer(success_right[:, i], dagger(success_right[:, j:j+1])[0])),
                    'Fourier success CP matrix unit')
        if invertible:
            D = eye(q) if c.red == 'omit-degree-scaling' else perm(nx)
            Lnum = B @ D
            c.check('F2', eq(J.T @ Lnum, eye(q)), 'logical D_n correction')
            N, H = Lnum-J, D.T @ ck
            c.check('F2', not np.any(J.T @ N) and eq(N.T @ N, (kap-1)*eye(q)),
                    'actual Gram-orthonormalized frame')
            c.check('F2', eq(ce @ J, (J+N) @ H)
                    and eq(ce @ N, ((kap-1)*J-N) @ H),
                    'actual Fourier chart factor with logical D_n inverse F_K')
        else:
            logical_ones = np.ones(q, dtype=np.int64)
            alpha_num, beta_num = J @ logical_ones, B[:, 0]
            c.check('F2', eq(ce @ alpha_num, q*beta_num)
                    and eq(ce @ beta_num, kap*alpha_num), 'p-divides-degree Fourier overlap plane')
            Nline = beta_num-alpha_num
            c.check('F2', int(Nline @ Nline) == kap-q, 'overlap plane degeneration norm')
            if kap == q:
                c.check('F2', eq(alpha_num, beta_num), 'quadratic characteristic-two common line')
            else:
                c.check('F2', eq(ce @ Nline, (kap-q)*alpha_num-q*Nline), 'generic overlap-plane Fourier')
            A = eye(q)[:, 1:]-eye(q)[:, 0:1]
            JA, residual = J @ A, B @ ck @ A
            reflection = perm([k.mul[k.p-1][x] for x in range(q)])
            if c.red == 'residual-fourier-reflection' and k.p == 3:
                reflection = eye(q)
            c.check('F2', eq(dagger(residual) @ residual, Q*(A.T @ A))
                    and not np.any(JA.T @ residual), 'orthogonal residual Fourier frame')
            c.check('F2', eq(ce @ JA, residual)
                    and eq(ce @ residual, Q*J @ reflection @ A), 'residual Fourier block retains logical reflection')
        records.append({'K': q, 'E': Q, 'degree': n, 'kappa': kap,
            'branch': 'invertible' if invertible else 'p-divides-degree',
            'Gram_numerator': gram.tolist(), 'Gram_denominator_squared': kap,
            'nonzero_singular_square': str(lam), 'Gram_rank': len(pivots(gram)),
            'support_rank': rank, 'physical_support_trace': str(F(rank, Q)),
            'generated_algebra_dimension': len(basis),
            'central_physical_weights': list(map(str, expected_weights)),
            'embedding': emb, 'relative_trace_fibres': [[i for i, x in enumerate(trace) if x == a] for a in range(q)]})
    c.check('G3', f4.q == 4 and len([x for x in range(4) if f4.power(x, 2) != x]) == 2,
            'quadratic embedding atom is two-dimensional, cardinality register four-dimensional')
    c.records['F'] = records
    return f4


def tangent(c):
    P, I = np.diag([1, 0]), eye(2)
    X, Z = np.array([[0, 1], [1, 0]]), np.diag([1, -1])
    records = []
    for t in [F(1, 2), F(1, 3), F(1, 4), F(1, 10), F(0)]:
        co, si = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        Q = np.array([[co*co, co*si], [co*si, si*si]], dtype=object)
        Fourier = np.array([[co, si], [si, -co]], dtype=object)
        D = np.array([[-si, co], [co, si]], dtype=object)
        if c.red == 'omit-tangent-normalization':
            D = Q-P
        if c.red == 'collapse-tangent-algebra':
            D = np.diag(np.diag(D))
        if c.red == 'tangent-fourier':
            Fourier = I
        c.check('R2', eq(D @ D, I) and eq(Fourier @ Fourier, I), 'tangent/Fourier involutions')
        c.check('R2', eq(si*D, Q-P), 'explicit normalized difference')
        c.check('R2', eq(Fourier @ P @ Fourier, Q) and eq(Fourier @ Q @ Fourier, P),
                'induced chart Fourier interchanges the two projections')
        c.check('R2', eq(Fourier @ D, -D @ Fourier), 'tangent Fourier anticommutation')
        c.check('R2', len(pivots(np.array([I.ravel(), Fourier.ravel(), D.ravel(),
                         (Fourier @ D).ravel()]).T)) == 4, 'faithful full M2 span')
        rho = (I+D)*F(1, 2)
        c.check('R2', eq(rho @ rho, rho) and np.trace(rho) == 1,
                'positive ordinary-density rank-one state')
        c.check('R2', np.trace(rho @ rho) == 1 and np.trace(rho @ Fourier @ rho @ Fourier) == 0,
                'Born distinction survives chart Fourier')
        # Normalized-trace density is 2*rho, ordinary density is rho.
        c.check('R2', np.trace(2*rho)*F(1, 2) == 1 and
                np.trace(2*rho @ rho)*F(1, 2) == 1, 'normalized reference trace density convention')
        branches = {'+': rho, '-': I-rho}
        if c.red == 'incomplete-tangent-instrument':
            del branches['-']
        c.check('R2', eq(sum(A.T @ A for A in branches.values()), I), 'tangent instrument completeness')
        tensor = {a+b: np.kron(A, B) for a, A in branches.items() for b, B in branches.items()}
        c.check('R2', set(tensor) == {'++', '+-', '-+', '--'}
                and eq(sum(A.T @ A for A in tensor.values()), eye(4)), 'all independent tangent outcomes')
        for i, j in product(range(4), repeat=2):
            c.check('R2', sum(np.trace(outer(A[:, i], A[:, j])) for A in tensor.values()) == (i == j),
                    'tensor instrument CP maps preserve every matrix-unit trace')
        if t == 0:
            c.check('R2', eq(Q, P) and eq(Fourier, Z) and eq(D, X), 'coalesced endpoint with retained tangent')
        records.append({'c': str(co), 's': str(si), 'angle_square': str(co*co),
                        'Born_before': '1', 'Born_after': '0'})
    c.records['R2'] = {'samples': records, 'reference_trace': 'Tr/2',
                        'ordinary_density': '(I+D)/2', 'reference_density': 'I+D'}


def tower(c):
    k, l, e = Field(3, [0, 1]), Field(3, [1, 0, 1]), Field(3, [2, 1, 0, 0, 1])
    il, je = embedding(k, l), embedding(l, e)
    def data(a, b, emb):
        n = b.d//a.d
        trace = [emb.index(b.summation(b.power(x, a.q**j) for j in range(n))) for x in range(b.q)]
        J = np.zeros((b.q, a.q), dtype=np.int64)
        for x, y in enumerate(emb):
            J[y, x] = 1
        B = inc(trace, a.q)
        D = perm([a.mul[n % a.p][x] for x in range(a.q)])
        return J, B @ D, b.q//a.q
    Ji, Li, ki = data(k, l, il)
    Jj, Lj, kj = data(l, e, je)
    Jd, Ld, kd = data(k, e, [je[x] for x in il])
    if c.red == 'tower-degree-scaling':
        Lj = Lj @ perm([l.mul[2][x] for x in range(l.q)])
    c.check('F3', eq(Jj @ Ji, Jd) and eq(Lj @ Li, Ld) and ki*kj == kd,
            'actual F3->F9->F81 corrected transfers compose')
    Ni, Nj, Nd = Li-Ji, Lj-Jj, Ld-Jd
    c.check('F3', eq(Jj @ Ni + Nj @ Ji + Nj @ Ni, Nd), 'actual arithmetic four-path connector')
    paths = [Jj @ Ji, Jj @ Ni, Nj @ Ji, Nj @ Ni]
    norms = [1, ki-1, kj-1, (ki-1)*(kj-1)]
    for a, b in product(range(4), repeat=2):
        c.check('F3', eq(paths[a].T @ paths[b], norms[a]*eye(k.q) if a == b else 0*eye(k.q)),
                'four actual tower paths form orthogonal frame')
    CE, CK = characters(e), characters(k)
    logical = perm([k.mul[4 % k.p][x] for x in range(k.q)]).T @ CK
    coefficients = np.kron(np.array([[1, kj-1], [1, -1]]), np.array([[1, ki-1], [1, -1]]))
    for b in range(4):
        c.check('F3', eq(CE @ paths[b], sum(coefficients[a, b]*paths[a] @ logical for a in range(4))),
                'actual F81 Fourier on the four-path arithmetic frame')
    # All coefficients are nonnegative: squared coefficients determine them.
    samples = []
    for kappas in [(F(3), F(9)), (F(3, 2), F(5, 4), F(7, 6))]:
        prod_k = np.prod(kappas)
        weights = {}
        for bits in product([0, 1], repeat=len(kappas)):
            if not any(bits):
                continue
            weights[''.join(map(str, bits))] = np.prod([kap-1 if bit else F(1)
                                                  for kap, bit in zip(kappas, bits)])/(prod_k-1)
        if c.red == 'tower-connector-coefficient':
            weights[next(iter(weights))] *= 2
        c.check('R3', sum(weights.values()) == 1, 'connector squared coefficients normalize')
        if len(kappas) == 3:
            ka, kb, kc = kappas
            # Build both bracketings from the binary connector probabilities.
            def binary(a, b):
                return {(0, 1): (b-1)/(a*b-1), (1, 0): (a-1)/(a*b-1),
                        (1, 1): (a-1)*(b-1)/(a*b-1)}
            left, right = {}, {}
            for (ab, z), w in binary(ka*kb, kc).items():
                for (x, y), v in (binary(ka, kb) if ab else {(0, 0): F(1)}).items():
                    left[f'{x}{y}{z}'] = w*v
            for (x, bc), w in binary(ka, kb*kc).items():
                for (y, z), v in (binary(kb, kc) if bc else {(0, 0): F(1)}).items():
                    right[f'{x}{y}{z}'] = w*v
            c.check('R3', left == right == weights, 'ternary connector associativity by nonnegative squares')
        samples.append({key: str(v) for key, v in weights.items()})
    # Independently multiply numerator polynomials in h=t-1 and divide their
    # first nonzero coefficient by the denominator's linear coefficient.
    exponents = (1, 2, 4)
    endpoint = {''.join(map(str, bits)): F(exponents[bits.index(1)], sum(exponents))
                if sum(bits) == 1 else F(0) for bits in product([0, 1], repeat=3) if any(bits)}
    c.check('R3', sum(endpoint.values()) == 1, 'one-excitation endpoint connector norm')
    for bits in product([0, 1], repeat=3):
        if not any(bits):
            continue
        polynomial = [1]
        for a, bit in zip(exponents, bits):
            if bit:
                polynomial = np.convolve(polynomial, [0]+[comb(a, j) for j in range(1, a+1)]).tolist()
        limit = F(polynomial[1], sum(exponents)) if len(polynomial) > 1 else F(0)
        c.check('R3', limit == endpoint[''.join(map(str, bits))], 'boundary connector from actual polynomial coefficients')
    # The binary/ternary Fourier connector equations use unnormalized N,
    # avoiding its single positive square root while retaining its exact norm.
    for angles in [[(F(3, 5), F(4, 5)), (F(4, 5), F(3, 5))],
                   [(F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(15, 17), F(8, 17))]]:
        U, v, prod_c = np.array([[1]]), np.array([1]), F(1)
        for co, si in angles:
            U = np.kron(U, np.array([[co, si], [si, -co]], dtype=object))
            v, prod_c = np.kron(v, np.array([co, si], dtype=object)), prod_c*co
        zero = eye(len(v))[:, 0]; N = v-prod_c*zero
        c.check('R3', N @ N == 1-prod_c**2 and zero @ N == 0, 'connector exact positive norm')
        c.check('R3', eq(U @ zero, prod_c*zero+N)
                and eq(U @ N, (1-prod_c**2)*zero-prod_c*N), 'tensor Fourier intertwines connector')
    signs = np.diag(np.kron(np.kron(np.diag([1, -1]), np.diag([1, -1])), np.diag([1, -1])))
    c.check('R3', all(signs[int(bits, 2)] == -1 for bits, weight in endpoint.items() if weight),
            'endpoint tensor Fourier is negative on retained one-excitation vector')
    c.records['F3'] = {'tower': 'F3->F9->F81', 'kappas': [ki, kj, kd], 'four_path_norm_squares': norms}
    c.records['R3'] = {'squared_coefficients': samples, 'boundary_exponents': exponents,
                        'boundary_squared_coefficients': {k: str(v) for k, v in endpoint.items()}}


def physical(c):
    records = []
    for t in [F(1, 3), F(1, 4), F(1, 10)]:
        co, si = (1-t*t)/(1+t*t), 2*t/(1+t*t)
        P, Q = np.diag([1, 0]), np.array([[co*co, co*si], [co*si, si*si]], dtype=object)
        kap = 1/(co*co)
        if c.red == 'physical-support-rank':
            Q = P
        block_rank = len(pivots(np.concatenate([P, Q], axis=1)))
        complement = 1-F(block_rank, 1)/kap
        c.check('R1', complement < 0, 'generic physical support complement must be negative near one')
        records.append({'kappa': str(kap), 'support_weight': str(block_rank/kap), 'complement': str(complement)})
    c.records['R1'] = records


def mixed(c, f4):
    moving = {x for x in range(4) if f4.power(x, 2) != x}
    state = (2, 2, 3)
    gate = lambda s: (s[0], s[1], f4.add[s[2]][f4.mul[s[0]][s[1]]])
    midpoint, final = gate(state), gate(gate(state))
    c.check('M1', all(x in moving for x in state) and not all(x in moving for x in midpoint),
            'F4 moving-sector multiplication leakage')
    coherent_return = int(final == state)
    compressed_return = int(all(x in moving for x in midpoint) and final == state)
    actual = compressed_return if c.red == 'compress-mixed-transition' else coherent_return
    c.check('M1', actual == 1 and compressed_return == 0, 'intermediate compression changes M^2 return')
    histories = {'success': compressed_return, 'failure': coherent_return-compressed_return}
    c.check('M1', histories == {'success': 0, 'failure': 1}, 'retained sector history preserves return path')
    v0 = np.array([1, 1, 0, 0]); nonzero = np.diag([0, 1, 1, 1])
    c.check('M1', np.any(nonzero @ v0), 'nonzero cut does not intertwine trace pullback')
    C, P = characters(f4), np.diag([int(x in moving) for x in range(4)])
    overlap = np.trace(P @ C @ P @ dagger(C))*F(1, 16)
    c.check('M1', overlap == F(1, 4), 'actual Fourier moving-cut overlap')
    c.records['M1'] = {'state': state, 'midpoint': midpoint, 'final': final,
                       'uncompressed_return': coherent_return, 'compressed_return': compressed_return,
                       'retained_histories': histories, 'Fourier_overlap': '1/4'}


def run(red=None):
    c = Checks(red)
    target = MUTATIONS.get(red)
    try:
        if target is None or target in {'G1', 'G2', 'G3'}:
            galois(c)
        if target is None or target in {'F1', 'F2'}:
            finite_fields(c)
        if target is None or target == 'R1':
            physical(c)
        if target is None or target == 'R2':
            tangent(c)
        if target is None or target in {'F3', 'R3'}:
            tower(c)
        if target is None or target == 'M1':
            mixed(c, Field(2, [1, 1, 1]))
    except Failure as e:
        return {'status': 'FAIL', 'mutation': red, 'failed_gate': e.gate,
                'detail': e.detail, 'counts': c.counts}
    return {'status': 'PASS', 'mutation': red, 'counts': c.counts, 'records': c.records,
            'scope': 'Exact bounded finite tests only; Fourier characters only p=2,3.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    red_options = parser.add_mutually_exclusive_group()
    red_options.add_argument('--red', choices=MUTATIONS, nargs='?',
                             const='omit-normalization',
                             help='named mutation; the bare option selects omitted normalization')
    for name, gate in MUTATIONS.items():
        red_options.add_argument('--red-' + name, dest='red', action='store_const',
                                 const=name, help='mutate mathematical data for ' + gate)
    parser.add_argument('--matrix', action='store_true')
    args = parser.parse_args()
    if args.matrix:
        reds = {name: run(name) for name in MUTATIONS}
        green = run()
        ok = all(r['status'] == 'FAIL' and r['failed_gate'] == MUTATIONS[n] for n, r in reds.items())
        print(json.dumps({'red': reds, 'green': green, 'matrix_pass': ok and green['status'] == 'PASS'}, indent=2))
        return 0 if ok and green['status'] == 'PASS' else 1
    result = run(args.red)
    print(json.dumps(result, indent=2))
    return 0 if result['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
