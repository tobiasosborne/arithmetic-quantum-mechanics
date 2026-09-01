#!/usr/bin/env python3
"""Blind exact checker for the five smallest commutative local rings.

There are no repository imports and no data imported from the orchestrator's
scratch computation.  Rings are full addition/multiplication tables.  Roots
of unity are integer coefficient vectors in Z[x]/(Phi_d), d=2,3,4,8.  Matrix
operators are exact monomial matrices (permutation, root exponent).  No float,
tolerance, numerical eigensolver, or ``assert`` occurs in an evidence gate.
"""

import itertools
import sys

import numpy as np


RING_NAMES = ("F2", "F3", "F4", "Z4", "F2[e]/e2")
MODES = {
    "green": "unmutated exhaustive checker",
    "--red-ring-soc": "claim |soc(F2)|=1",
    "--red-transpose-cocycle": "use beta0^T while retaining the UT3 orientation",
    "--red-order-profile": "replace the F4 involution fixture 27 by 26",
    "--red-class-count": "increase the Z4 class-count identity by one",
    "--red-gram": "declare one exact off-diagonal F3 Gram entry nonzero",
    "--red-catalogue": "claim five, rather than four, middle F2[e]/e2 irreps",
    "--red-middle-images": "claim seven, rather than eight, middle Z4 Weyl images",
    "--red-drop-nonfree": "discard the unique non-free F2[e]/e2 Lagrangian",
}
TARGET = {
    "--red-ring-soc": ("F2", "C1"),
    "--red-transpose-cocycle": ("F2", "C2"),
    "--red-order-profile": ("F4", "C3"),
    "--red-class-count": ("Z4", "C4"),
    "--red-gram": ("F3", "C5"),
    "--red-catalogue": ("F2[e]/e2", "C6"),
    "--red-middle-images": ("Z4", "C7"),
    "--red-drop-nonfree": ("F2[e]/e2", "C8"),
}
EXIT_GREEN, EXIT_RED_CAUGHT, EXIT_DEFECT = 0, 1, 2


class CycRing:
    """Exact Z[zeta_d], represented modulo Phi_d for d=2,3,4,8."""

    PHI = {
        2: (1, 1),
        3: (1, 1, 1),
        4: (1, 0, 1),
        8: (1, 0, 0, 0, 1),
    }

    def __init__(self, order):
        if order not in self.PHI:
            raise ValueError("unsupported exact cyclotomic order %s" % order)
        self.order = order
        self.phi = self.PHI[order]
        self.deg = len(self.phi) - 1
        self.zero = (0,) * self.deg
        self.one = (1,) + (0,) * (self.deg - 1)
        self.zeta = self.reduce((0, 1))
        self.zpow = [self.one]
        for _ in range(order):
            self.zpow.append(self.mul(self.zpow[-1], self.zeta))

    def reduce(self, coeffs):
        c = list(coeffs)
        if len(c) < self.deg:
            c += [0] * (self.deg - len(c))
        for k in range(len(c) - 1, self.deg - 1, -1):
            lead = c[k]
            if lead:
                c[k] = 0
                shift = k - self.deg
                for j in range(self.deg):
                    c[shift + j] -= lead * self.phi[j]
        return tuple(c[:self.deg])

    def add(self, x, y):
        return tuple(a + b for a, b in zip(x, y))

    def mul(self, x, y):
        out = [0] * (2 * self.deg - 1)
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                out[i + j] += a * b
        return self.reduce(out)


def verify_cyclotomic(C):
    if C.zpow[C.order] != C.one:
        return False, "zeta_%d^%d != 1" % (C.order, C.order)
    if len(set(C.zpow[:C.order])) != C.order:
        return False, "zeta_%d does not have exact order %d" % (C.order, C.order)
    # Directly verify Phi_d(zeta)=0 in the quotient representation.
    value = C.zero
    for k, coeff in enumerate(C.phi):
        if coeff:
            term = tuple(coeff * x for x in C.zpow[k])
            value = C.add(value, term)
    if value != C.zero:
        return False, "Phi_%d(zeta_%d) != 0" % (C.order, C.order)
    return True, "Phi_%d exact; zeta_%d has exact order %d" % (
        C.order, C.order, C.order)


class FiniteRing:
    def __init__(self, name, coord_mods, mul_coords, reference_param):
        self.name = name
        self.coord_mods = tuple(coord_mods)
        self.n = int(np.prod(np.array(coord_mods, dtype=np.int64)))
        self.elements = tuple(self._coords(i) for i in range(self.n))
        self.index = {x: i for i, x in enumerate(self.elements)}
        self.reference_param = tuple(reference_param)
        self.phase_order = max(coord_mods)
        self.char_params = tuple(itertools.product(
            *[range(m) for m in self.coord_mods]))
        self.ADD = np.zeros((self.n, self.n), dtype=np.int64)
        self.MUL = np.zeros((self.n, self.n), dtype=np.int64)
        for i, x in enumerate(self.elements):
            for j, y in enumerate(self.elements):
                self.ADD[i, j] = self.index[tuple(
                    (x[k] + y[k]) % self.coord_mods[k]
                    for k in range(len(self.coord_mods)))]
                self.MUL[i, j] = self.index[tuple(mul_coords(x, y))]
        self.zero = 0
        self.one = self.index[(1,) + (0,) * (len(coord_mods) - 1)]
        self.NEG = np.array([
            next(j for j in range(self.n) if self.ADD[i, j] == self.zero)
            for i in range(self.n)
        ], dtype=np.int64)
        self.units = tuple(i for i in range(self.n)
                           if np.any(self.MUL[i, :] == self.one))
        unit_set = set(self.units)
        self.maximal = tuple(i for i in range(self.n) if i not in unit_set)

    def _coords(self, i):
        coords = []
        for modulus in self.coord_mods:
            coords.append(i % modulus)
            i //= modulus
        return tuple(coords)

    def char_table(self, param):
        d = self.phase_order
        return tuple(sum(param[k] * x[k] * (d // self.coord_mods[k])
                         for k in range(len(param))) % d
                     for x in self.elements)

    def scaled_character(self, param, u):
        table = self.char_table(param)
        return tuple(table[int(self.MUL[u, x])] for x in range(self.n))

    def ideal_in_kernel(self, char):
        # r belongs to the largest ideal in ker(char) exactly when rR is there.
        return frozenset(r for r in range(self.n)
                         if all(char[int(self.MUL[r, x])] == 0
                                for x in range(self.n)))

    def annihilator(self, u):
        return frozenset(r for r in range(self.n)
                         if int(self.MUL[r, u]) == self.zero)


def make_rings():
    def fp(p):
        return lambda x, y: ((x[0] * y[0]) % p,)

    def f4_mul(x, y):
        # alpha^2=alpha+1, from the irreducible x^2+x+1 over F2.
        a, b = x
        c, d = y
        return ((a * c + b * d) % 2,
                (a * d + b * c + b * d) % 2)

    def dual_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c) % 2, (a * d + b * c) % 2)

    return {
        "F2": FiniteRing("F2", (2,), fp(2), (1,)),
        "F3": FiniteRing("F3", (3,), fp(3), (1,)),
        "F4": FiniteRing("F4", (2, 2), f4_mul, (0, 1)),
        "Z4": FiniteRing("Z4", (4,), fp(4), (1,)),
        "F2[e]/e2": FiniteRing("F2[e]/e2", (2, 2), dual_mul, (1, 1)),
    }


def verify_ring(R):
    n, A, M = R.n, R.ADD, R.MUL
    idx = np.arange(n, dtype=np.int64)
    if not np.array_equal(A[R.zero, :], idx) or not np.array_equal(M[R.one, :], idx):
        return False, "identity failure"
    if not np.array_equal(A, A.T) or not np.array_equal(M, M.T):
        return False, "commutativity failure"
    J, K = np.meshgrid(idx, idx, indexing="ij")
    for i in range(n):
        if not np.array_equal(A[A[i, J], K], A[i, A[J, K]]):
            return False, "addition is not associative"
        if not np.array_equal(M[M[i, J], K], M[i, M[J, K]]):
            return False, "multiplication is not associative"
        if not np.array_equal(M[i, A[J, K]], A[M[i, J], M[i, K]]):
            return False, "distributivity failure"
    maximal = set(R.maximal)
    if R.zero not in maximal or R.one in maximal:
        return False, "nonunits are not a proper candidate maximal ideal"
    if any(int(A[x, y]) not in maximal for x in maximal for y in maximal):
        return False, "nonunits are not additively closed"
    if any(int(M[r, x]) not in maximal for r in range(n) for x in maximal):
        return False, "nonunits are not an ideal"
    return True, "%dx%d tables satisfy commutative local-ring axioms" % (n, n)


class Setting:
    def __init__(self, ring, mode):
        self.R, self.mode = ring, mode
        R, n = ring, ring.n
        self.C = CycRing(R.phase_order)
        self.n, self.nV = n, n * n
        self.VA = np.repeat(np.arange(n, dtype=np.int64), n)
        self.VB = np.tile(np.arange(n, dtype=np.int64), n)
        a, b = self.VA[:, None], self.VB[:, None]
        ap, bp = self.VA[None, :], self.VB[None, :]
        self.VADD = R.ADD[a, ap] * n + R.ADD[b, bp]
        self.OMEGA = R.ADD[R.MUL[a, bp], R.NEG[R.MUL[ap, b]]]
        self.BETA0 = R.MUL[a, bp]
        self.BETAT = R.MUL[ap, b]
        self.BETA = (self.BETAT if mode == "--red-transpose-cocycle"
                     and R.name == "F2" else self.BETA0)
        self.char_records = []
        for param in R.char_params:
            table = R.char_table(param)
            self.char_records.append({
                "param": param,
                "table": table,
                "ideal": R.ideal_in_kernel(table),
            })
        self.nontrivial = [r for r in self.char_records
                           if any(x != 0 for x in r["table"])]
        self.generating = [r for r in self.nontrivial if r["ideal"] == {0}]
        self.reference = R.char_table(R.reference_param)
        self.cache = {}


def sym_form(S, alpha, gamma, delta):
    R = S.R
    a, b = S.VA[:, None], S.VB[:, None]
    ap, bp = S.VA[None, :], S.VB[None, :]
    aa = R.MUL[a, ap]
    cross = R.ADD[R.MUL[a, bp], R.MUL[ap, b]]
    bb = R.MUL[b, bp]
    return R.ADD[R.ADD[R.MUL[alpha, aa], R.MUL[gamma, cross]],
                 R.MUL[delta, bb]]


def admissible_tables(S):
    if "adm" not in S.cache:
        R = S.R
        S.cache["adm"] = [R.ADD[S.BETA0, sym_form(S, *triple)]
                          for triple in itertools.product(range(S.n), repeat=3)]
    return S.cache["adm"]


def mono_mul(X, Y, phase_order):
    px, ex = X
    py, ey = Y
    return (tuple(px[py[k]] for k in range(len(py))),
            tuple((ex[py[k]] + ey[k]) % phase_order for k in range(len(py))))


def mono_scale(X, exponent, phase_order):
    return X[0], tuple((e + exponent) % phase_order for e in X[1])


def mono_equal(X, Y, C):
    return X[0] == Y[0] and all(C.zpow[x] == C.zpow[y]
                               for x, y in zip(X[1], Y[1]))


def build_weyl(S, char):
    R, d = S.R, S.R.phase_order
    ops = []
    for v in range(S.nV):
        a, b = int(S.VA[v]), int(S.VB[v])
        perm, exps = [], []
        for y in range(S.n):
            ya = int(R.ADD[y, a])
            perm.append(ya)
            arg = int(R.NEG[int(R.MUL[b, ya])])
            exps.append(char[arg] % d)
        ops.append((tuple(perm), tuple(exps)))
    return ops


def trace_inner(X, Y, C):
    px, ex = X
    py, ey = Y
    total = C.zero
    for k in range(len(px)):
        if px[k] == py[k]:
            total = C.add(total, C.zpow[(ey[k] - ex[k]) % C.order])
    return total


def scalar_normalize(X, d):
    perm, exps = X
    offset = exps[0]
    return perm, tuple((e - offset) % d for e in exps)


def commutant_dimension(ops, C):
    """Exact union-find-with-root-potentials solution of TW=WT."""
    n, d = len(ops[0][0]), C.order
    parent = list(range(n * n))
    potential = [0] * (n * n)
    dead = [False] * (n * n)

    def find(x):
        if parent[x] == x:
            return x, 0
        root, up = find(parent[x])
        potential[x] = (potential[x] + up) % d
        parent[x] = root
        return root, potential[x]

    for perm, exps in ops:
        for row in range(n):
            for col in range(n):
                u = row * n + col
                w = perm[row] * n + perm[col]
                delta = (exps[col] - exps[row]) % d
                ru, pu = find(u)
                rw, pw = find(w)
                if ru == rw:
                    if C.zpow[(pu - pw - delta) % d] != C.one:
                        dead[ru] = True
                else:
                    parent[rw] = ru
                    potential[rw] = (pu - delta - pw) % d
                    dead[ru] = dead[ru] or dead[rw]
    roots = set()
    for x in range(n * n):
        root, _ = find(x)
        if not dead[root]:
            roots.add(root)
    return len(roots)


def h_table(S, beta=None):
    B = S.BETA if beta is None else beta
    key = ("H", B.tobytes())
    if key not in S.cache:
        R, nV = S.R, S.nV
        size = S.n ** 3
        t = np.arange(size, dtype=np.int64) // nV
        v = np.arange(size, dtype=np.int64) % nV
        central = R.ADD[R.ADD[t[:, None], t[None, :]], B[v[:, None], v[None, :]]]
        vector = S.VADD[v[:, None], v[None, :]]
        S.cache[key] = central * nV + vector
    return S.cache[key]


def group_orders(H):
    size = H.shape[0]
    current = np.zeros(size, dtype=np.int64)
    orders = np.zeros(size, dtype=np.int64)
    elements = np.arange(size, dtype=np.int64)
    for k in range(1, size + 1):
        current = H[current, elements]
        hit = (orders == 0) & (current == 0)
        orders[hit] = k
        if np.all(orders != 0):
            break
    if np.any(orders == 0):
        return None
    return orders


def profile_from_orders(orders):
    return {int(k): int(np.sum(orders == k))
            for k in sorted(set(orders.tolist()))}


def group_stats(S, beta=None):
    B = S.BETA if beta is None else beta
    key = ("stats", B.tobytes())
    if key in S.cache:
        return S.cache[key]
    H = h_table(S, B)
    orders = group_orders(H)
    if orders is None:
        return None
    centre = tuple(g for g in range(H.shape[0])
                   if np.array_equal(H[g, :], H[:, g]))
    stats = {
        "H": H,
        "orders": orders,
        "profile": profile_from_orders(orders),
        "centre": centre,
        "centre_profile": profile_from_orders(orders[np.array(centre, dtype=np.int64)]),
        "exponent": int(np.max(orders)),
    }
    S.cache[key] = stats
    return stats


def group_inverses(H):
    return np.array([next(j for j in range(H.shape[0]) if H[i, j] == 0)
                     for i in range(H.shape[0])], dtype=np.int64)


def generated_subgroup(H, generators):
    inv = group_inverses(H)
    found = {0}
    queue = list(generators)
    while queue:
        x = queue.pop()
        if x in found:
            continue
        old = list(found)
        found.add(x)
        found.add(int(inv[x]))
        for y in old:
            queue.append(int(H[x, y]))
            queue.append(int(H[y, x]))
    return frozenset(found)


def conjugacy_classes(H):
    inv = group_inverses(H)
    remaining = set(range(H.shape[0]))
    classes = []
    while remaining:
        x = min(remaining)
        orbit = frozenset(int(H[H[g, x], inv[g]]) for g in range(H.shape[0]))
        classes.append(orbit)
        remaining.difference_update(orbit)
    return classes


EXPECTED = {
    "F2": {"soc": 2, "units": 1, "gen": 1, "adm": 8, "classes": 5,
           "profile": {1: 1, 2: 5, 4: 2}, "centre": {1: 1, 2: 1},
           "exp": 4, "lags": (3, 3, 0), "labels": 6,
           "catalogue": (4, 0, 1)},
    "F3": {"soc": 3, "units": 2, "gen": 2, "adm": 27, "classes": 11,
           "profile": {1: 1, 3: 26}, "centre": {1: 1, 3: 2},
           "exp": 3, "lags": (4, 4, 0), "labels": 12,
           "catalogue": (9, 0, 2)},
    "F4": {"soc": 4, "units": 3, "gen": 3, "adm": 64, "classes": 19,
           "profile": {1: 1, 2: 27, 4: 36}, "centre": {1: 1, 2: 3},
           "exp": 4, "lags": (5, 5, 0), "labels": 20,
           "catalogue": (16, 0, 3)},
    "Z4": {"soc": 2, "units": 2, "gen": 2, "adm": 64, "classes": 22,
           "profile": {1: 1, 2: 7, 4: 40, 8: 16},
           "centre": {1: 1, 2: 1, 4: 2}, "exp": 8,
           "lags": (7, 6, 1), "labels": 28,
           "catalogue": (16, 4, 2)},
    "F2[e]/e2": {"soc": 2, "units": 2, "gen": 2, "adm": 64,
                  "classes": 22,
                  "profile": {1: 1, 2: 31, 4: 32},
                  "centre": {1: 1, 2: 3}, "exp": 4,
                  "lags": (7, 6, 1), "labels": 28,
                  "catalogue": (16, 4, 2)},
}


def gate_A0(S, world):
    del world
    ok, detail = verify_cyclotomic(S.C)
    if not ok:
        return False, detail
    ok, ring_detail = verify_ring(S.R)
    if not ok:
        return False, ring_detail
    return True, "%s; %s [decoration: table-integrity precondition]" % (detail, ring_detail)


def gate_C1(S, world):
    del world
    R, E = S.R, EXPECTED[S.R.name]
    soc = frozenset(r for r in range(R.n)
                    if all(int(R.MUL[r, x]) == 0 for x in R.maximal))
    claimed_soc = 1 if S.mode == "--red-ring-soc" and R.name == "F2" else E["soc"]
    if len(soc) != claimed_soc:
        return False, "|soc|=%d, claimed %d; soc=%s" % (
            len(soc), claimed_soc, [R.elements[x] for x in sorted(soc)])
    if len(R.units) != E["units"]:
        return False, "|R^x|=%d, expected %d" % (len(R.units), E["units"])
    tables = [rec["table"] for rec in S.char_records]
    if len(S.char_records) != R.n or len(set(tables)) != R.n:
        return False, "additive-character parameterization is not exhaustive/distinct"
    for rec in S.char_records:
        table = rec["table"]
        if any(table[int(R.ADD[x, y])] != (table[x] + table[y]) % R.phase_order
               for x in range(R.n) for y in range(R.n)):
            return False, "character %s is not additive" % (rec["param"],)
    if len(S.generating) != E["gen"]:
        return False, "|Gen|=%d, expected %d" % (len(S.generating), E["gen"])
    if S.R.ideal_in_kernel(S.reference) != {0}:
        return False, "the named reference character is not generating"
    unit_orbit = {R.scaled_character(R.reference_param, u) for u in R.units}
    gen_tables = {rec["table"] for rec in S.generating}
    if unit_orbit != gen_tables or len(unit_orbit) != len(R.units):
        return False, "Gen is not the free unit-scaled orbit of the reference character"
    adm = admissible_tables(S)
    distinct = {B.tobytes() for B in adm}
    if len(distinct) != E["adm"]:
        return False, "|Adm|=%d, expected %d" % (len(distinct), E["adm"])
    for B in adm:
        if not np.array_equal(R.ADD[B, R.NEG[B.T]], S.OMEGA):
            return False, "enumerated beta is not admissible"
    antisym = sum(1 for B in adm if np.array_equal(B, R.NEG[B.T]))
    want_antisym = 1 if R.name == "F3" else 0
    if antisym != want_antisym:
        return False, "antisymmetric Adm members=%d, expected %d" % (
            antisym, want_antisym)
    return True, "|soc|=%d |R^x|=%d |Gen|=%d (all %d chars); |Adm|=%d; antisym=%d" % (
        len(soc), len(R.units), len(S.generating), R.n, len(distinct), antisym)


def gate_C2(S, world):
    del world
    R, B = S.R, S.BETA
    diff = R.ADD[B, R.NEG[B.T]]
    if not np.array_equal(diff, S.OMEGA):
        bad = np.argwhere(diff != S.OMEGA)[0]
        return False, "beta-beta^T orientation fails at v=%d,w=%d" % (
            int(bad[0]), int(bad[1]))
    for u in range(S.nV):
        for v in range(S.nV):
            for w in range(S.nV):
                lhs = int(R.ADD[B[u, v], B[int(S.VADD[u, v]), w]])
                rhs = int(R.ADD[B[v, w], B[u, int(S.VADD[v, w])]])
                if lhs != rhs:
                    return False, "cocycle identity fails at (%d,%d,%d)" % (u, v, w)
    # UT3 coordinate map (t,a,b) is checked on every ordered pair.
    H = h_table(S)
    for g in range(H.shape[0]):
        t, v = divmod(g, S.nV)
        a, b = divmod(v, S.n)
        for h in range(H.shape[0]):
            s, w = divmod(h, S.nV)
            ap, bp = divmod(w, S.n)
            ut_t = int(R.ADD[R.ADD[t, s], R.MUL[a, bp]])
            ut_v = int(S.VADD[v, w])
            if int(H[g, h]) != ut_t * S.nV + ut_v:
                return False, "H_beta law != UT3 product at g=%d,h=%d" % (g, h)
    transports = 0
    if R.name == "F3":
        two = int(R.ADD[R.one, R.one])
        half = next(x for x in range(R.n) if int(R.MUL[two, x]) == R.one)
        for triple in itertools.product(range(R.n), repeat=3):
            s = sym_form(S, *triple)
            f = R.MUL[half, np.diag(s)]
            if not np.array_equal(f[S.VADD], R.ADD[R.ADD[f[:, None], f[None, :]], s]):
                return False, "F3 beta transport coboundary fails for s=%s" % (triple,)
            transports += 1
    return True, "2-cocycle on %d triples; UT3 identity on %d pairs; F3 transports=%d" % (
        S.nV ** 3, S.n ** 6, transports)


def gate_C3(S, world):
    E = EXPECTED[S.R.name]
    stats = group_stats(S)
    if stats is None:
        return False, "an element did not return to identity"
    claimed = dict(E["profile"])
    if S.mode == "--red-order-profile" and S.R.name == "F4":
        claimed[2] = 26
    if stats["profile"] != claimed:
        return False, "order profile=%s, claimed %s" % (stats["profile"], claimed)
    if len(stats["H"]) != S.n ** 3 or stats["exponent"] != E["exp"]:
        return False, "(|H|,exponent)=(%d,%d), expected (%d,%d)" % (
            len(stats["H"]), stats["exponent"], S.n ** 3, E["exp"])
    if stats["centre_profile"] != E["centre"] or len(stats["centre"]) != S.n:
        return False, "centre profile=%s, expected %s" % (
            stats["centre_profile"], E["centre"])
    expected_centre = tuple(t * S.nV for t in range(S.n))
    if stats["centre"] != expected_centre:
        return False, "centre is not exactly R x 0"
    witness = ""
    if S.R.name == "F2":
        H, orders = stats["H"], stats["orders"]
        found = None
        for r in range(len(H)):
            if orders[r] != 4:
                continue
            rinv = next(x for x in range(len(H)) if H[r, x] == 0)
            for s in range(len(H)):
                if orders[s] == 2 and int(H[H[s, r], s]) == rinv:
                    if len(generated_subgroup(H, (r, s))) == 8:
                        found = (r, s)
                        break
            if found is not None:
                break
        if found is None:
            return False, "no D4 presentation witness r^4=s^2=1, srs=r^-1"
        witness = "; D4 witness=(%d,%d)" % found
    if S.R.name == "F3":
        # Extraspecial plus witness: exponent 3, derived subgroup=center of order 3.
        if stats["exponent"] != 3 or stats["centre_profile"] != {1: 1, 3: 2}:
            return False, "F3 extraspecial exponent-3 witness failed"
        witness = "; extraspecial 3^(1+2)_+ invariants"
    if S.R.name == "Z4":
        for g, order in enumerate(stats["orders"]):
            _, v = divmod(g, S.nV)
            a, b = divmod(v, S.n)
            ab_odd = a in S.R.units and b in S.R.units
            if (order == 8) != ab_odd:
                return False, "order-8 iff ab odd fails at g=%d" % g
        witness = "; order 8 iff a,b odd (16 elements)"
    if S.R.name == "F2[e]/e2":
        if any(int(S.R.ADD[v, v]) != 0 for v in range(S.n)):
            return False, "equal-characteristic additive doubling did not vanish"
        witness = "; 2v=0 and no order 8"
    if S.R.name in ("F2", "F4"):
        frequencies = {}
        for beta in admissible_tables(S):
            profile = tuple(sorted(group_stats(S, beta)["profile"].items()))
            frequencies[profile] = frequencies.get(profile, 0) + 1
        if S.R.name == "F2":
            want = {
                ((1, 1), (2, 5), (4, 2)): 6,
                ((1, 1), (2, 1), (4, 6)): 2,
            }
        else:
            want = {
                ((1, 1), (2, 27), (4, 36)): 40,
                ((1, 1), (2, 3), (4, 60)): 24,
            }
        if frequencies != want:
            return False, "beta-profile census=%s, expected %s" % (frequencies, want)
        witness += "; beta profile types=%s" % sorted(frequencies.values())
    # The three order-64 signatures are pairwise separated by the named invariants.
    if S.R.name in ("F4", "Z4", "F2[e]/e2"):
        signatures = {}
        for name in ("F4", "Z4", "F2[e]/e2"):
            st = group_stats(world[name])
            signatures[name] = (st["centre_profile"], st["exponent"], st["profile"])
        if len({repr(value) for value in signatures.values()}) != 3:
            return False, "named order-64 signatures do not separate all groups"
    return True, "|H|=%d centre=%s exponent=%d profile=%s%s" % (
        S.n ** 3, stats["centre_profile"], stats["exponent"], stats["profile"], witness)


def gate_C4(S, world):
    del world
    R = S.R
    stats = group_stats(S)
    H = stats["H"]
    inv = group_inverses(H)
    commutators = set()
    for g in range(len(H)):
        _, v = divmod(g, S.nV)
        for h in range(len(H)):
            _, w = divmod(h, S.nV)
            comm = int(H[H[H[g, h], inv[g]], inv[h]])
            want = int(S.OMEGA[v, w]) * S.nV
            if comm != want:
                return False, "commutator formula fails at g=%d,h=%d" % (g, h)
            commutators.add(comm)
    derived = frozenset(t * S.nV for t in range(S.n))
    if frozenset(commutators) != derived:
        return False, "commutators do not exhaust R x 0"
    classes = conjugacy_classes(H)
    rhs = S.n ** 2 + sum(len(R.annihilator(u)) ** 2 for u in range(1, S.n))
    claimed_rhs = rhs + 1 if S.mode == "--red-class-count" and R.name == "Z4" else rhs
    if len(classes) != claimed_rhs or len(classes) != EXPECTED[R.name]["classes"]:
        return False, "classes=%d; identity claims %d; fixture=%d" % (
            len(classes), claimed_rhs, EXPECTED[R.name]["classes"])
    S.cache["classes"] = len(classes)
    return True, "[H,H]=R x 0; |H^ab|=%d; classes=%d=%d+sum Ann(u)^2" % (
        S.n ** 2, len(classes), S.n ** 2)


def basic_XZ(S, char):
    R, d = S.R, S.R.phase_order
    X = (tuple(int(R.ADD[y, R.one]) for y in range(R.n)), (0,) * R.n)
    Z = (tuple(range(R.n)), tuple(char[int(R.MUL[R.one, y])] % d
                                  for y in range(R.n)))
    return X, Z


def matrix_group(generators, d):
    n = len(generators[0][0])
    identity = (tuple(range(n)), (0,) * n)
    found, queue = {identity}, list(generators)
    while queue:
        x = queue.pop()
        if x in found:
            continue
        old = list(found)
        found.add(x)
        for y in old + [x]:
            queue.append(mono_mul(x, y, d))
            queue.append(mono_mul(y, x, d))
    return found


def gate_C5(S, world):
    del world
    R, C, n = S.R, S.C, S.n
    checked = 0
    for rec in S.generating:
        ops = build_weyl(S, rec["table"])
        for i in range(S.nV):
            for j in range(S.nV):
                actual = trace_inner(ops[i], ops[j], C)
                expected = ((n,) + (0,) * (C.deg - 1)) if i == j else C.zero
                if (S.mode == "--red-gram" and S.R.name == "F3"
                        and i == 0 and j == 1):
                    expected = C.one
                if actual != expected:
                    return False, "Gram[%d,%d]=%s, claimed %s" % (
                        i, j, actual, expected)
        if commutant_dimension(ops, C) != 1:
            return False, "generating Weyl image has non-scalar commutant"
        checked += 1
    X, Z = basic_XZ(S, S.reference)
    lhs = mono_mul(Z, X, S.R.phase_order)
    rhs = mono_scale(mono_mul(X, Z, S.R.phase_order),
                     S.reference[S.R.one], S.R.phase_order)
    if not mono_equal(lhs, rhs, C):
        return False, "clock-shift relation ZX=psi(1)XZ fails"
    fingerprint = ""
    if S.R.name == "F2":
        image = matrix_group((X, Z), 2)
        if len(image) != 8:
            return False, "Pauli pair image has order %d, expected 8" % len(image)
        fingerprint = "; Pauli image order 8 (D4)"
    elif S.R.name == "F4":
        R = S.R
        shifts = []
        for a in (R.one, R.index[(0, 1)]):
            shifts.append((tuple(int(R.ADD[y, a]) for y in range(n)), (0,) * n))
        if len(matrix_group(tuple(shifts), 2)) != 4:
            return False, "two F4 basis shifts do not generate C2 x C2"
        fingerprint = "; two independent qubit shifts"
    elif S.R.name == "Z4":
        if Z[1] != (0, 1, 2, 3):
            return False, "Z4 clock is not diag(1,i,-1,-i)"
        fingerprint = "; ququart clock exponents=(0,1,2,3)"
    return True, "%d generating characters: exact Gram=%d I_%d and commutant=1; span=M_%d%s" % (
        checked, S.nV, n, n, fingerprint)


def additive_character_tables(R):
    return [R.char_table(p) for p in R.char_params]


def catalogue_data(S):
    rows = []
    square_sum = 0
    irrep_count = 0
    for u in range(S.n):
        ann = len(S.R.annihilator(u))
        count = ann ** 2
        dim = S.n // ann
        rows.append((S.R.elements[u], ann, count, dim))
        square_sum += count * dim * dim
        irrep_count += count
    return rows, irrep_count, square_sum


def gate_C6(S, world):
    del world
    R = S.R
    # Exhaust the n^2 bottom characters and their homomorphism law on V.
    chars = additive_character_tables(R)
    bottom = set()
    for ca in chars:
        for cb in chars:
            table = tuple((ca[int(S.VA[v])] + cb[int(S.VB[v])]) % R.phase_order
                          for v in range(S.nV))
            if any(table[int(S.VADD[v, w])] != (table[v] + table[w]) % R.phase_order
                   for v in range(S.nV) for w in range(S.nV)):
                return False, "a bottom-stratum table is not a character of V"
            bottom.add(table)
    if len(bottom) != S.n ** 2:
        return False, "bottom characters=%d, expected %d" % (len(bottom), S.n ** 2)
    rows, count, squares = catalogue_data(S)
    classes = len(conjugacy_classes(group_stats(S)["H"]))
    if S.mode == "--red-catalogue" and R.name == "F2[e]/e2":
        claimed_middle = 5
    else:
        claimed_middle = EXPECTED[R.name]["catalogue"][1]
    aggregate = (
        next(row[2] for row in rows if row[3] == 1),
        sum(row[2] for row in rows if row[3] not in (1, S.n)),
        sum(row[2] for row in rows if row[3] == S.n),
    )
    claimed = (EXPECTED[R.name]["catalogue"][0], claimed_middle,
               EXPECTED[R.name]["catalogue"][2])
    if aggregate != claimed:
        return False, "catalogue (bottom,middle,top)=%s, claimed %s" % (
            aggregate, claimed)
    if count != classes or squares != S.n ** 3:
        return False, "irrep count/squares=(%d,%d), expected (classes=%d,|H|=%d)" % (
            count, squares, classes, S.n ** 3)
    unit_rows = [row for row in rows if row[1] == 1]
    if len(unit_rows) != len(S.generating):
        return False, "top rows do not match exhaustive Gen census"
    row_text = "; ".join("u=%s: %dx%d" % (u, multiplicity, dim)
                         for u, _, multiplicity, dim in rows)
    return True, "%s; irreps=%d=classes; sum dim^2=%d" % (
        row_text, count, squares)


def phase_radical(S, char):
    exp_omega = np.take(np.array(char, dtype=np.int64), S.OMEGA)
    return frozenset(v for v in range(S.nV) if np.all(exp_omega[v, :] == 0))


def middle_induced_ops(S, char, radical_element, eigen_bit):
    """Restrict the 4-d model to the +/- eigenspace of X(radical_element)."""
    R, r = S.R, radical_element
    ideal = frozenset((R.zero, r))
    remaining = set(range(R.n))
    reps = []
    decomposition = {}
    while remaining:
        y = min(remaining)
        reps.append(y)
        coset = {int(R.ADD[y, i]) for i in ideal}
        for value in coset:
            decomposition[value] = (len(reps) - 1,
                                    0 if value == y else 1)
        remaining.difference_update(coset)
    ops = build_weyl(S, char)
    induced = []
    sign_step = R.phase_order // 2
    for op in ops:
        perm, exps = op
        sign_exps = tuple((e // sign_step) % 2 for e in exps)
        out_perm, out_exps = [], []
        for y in reps:
            target0 = perm[y]
            target1 = perm[int(R.ADD[y, r])]
            j0, k0 = decomposition[target0]
            j1, k1 = decomposition[target1]
            scalar = (sign_exps[y] - eigen_bit * k0) % 2
            second = (eigen_bit + sign_exps[int(R.ADD[y, r])]) % 2
            if j0 != j1 or second != (scalar + eigen_bit * k1) % 2:
                return None, "eigenspace is not invariant"
            out_perm.append(j0)
            out_exps.append(scalar)
        induced.append((tuple(out_perm), tuple(out_exps)))
    return induced, None


def middle_data(S):
    if "middle" in S.cache:
        return S.cache["middle"]
    if S.R.name not in ("Z4", "F2[e]/e2"):
        return None
    R = S.R
    u = R.index[(2,)] if R.name == "Z4" else R.index[(0, 1)]
    char = R.scaled_character(R.reference_param, u)
    I = R.ideal_in_kernel(char)
    ann = R.annihilator(u)
    radical = phase_radical(S, char)
    expected_rad = frozenset(a * S.n + b for a in ann for b in ann)
    ops = build_weyl(S, char)
    exact_images = len(set(ops))
    projective_images = len({scalar_normalize(op, R.phase_order) for op in ops})
    group_images = set()
    for t in range(R.n):
        for op in ops:
            group_images.add(mono_scale(op, char[t], R.phase_order))
    r = next(x for x in ann if x != 0)
    blocks = []
    pairs = []
    for eigen_bit in (0, 1):
        induced, error = middle_induced_ops(S, char, r, eigen_bit)
        if error is not None:
            S.cache["middle"] = {"error": error}
            return S.cache["middle"]
        normalized = {scalar_normalize(op, 2) for op in induced}
        C2 = CycRing(2)
        if len(normalized) != 4:
            S.cache["middle"] = {"error": "block projective Weyl count is %d" % len(normalized)}
            return S.cache["middle"]
        norm_list = list(normalized)
        gram_ok = all(trace_inner(norm_list[i], norm_list[j], C2) ==
                      (((2,) if i == j else C2.zero))
                      for i in range(4) for j in range(4))
        if not gram_ok or commutant_dimension(induced, C2) != 1:
            S.cache["middle"] = {"error": "a 2-d block is not an exact M2 image"}
            return S.cache["middle"]
        rx = r * S.n
        rz = r
        rx_op, rz_op = induced[rx], induced[rz]
        want_rx = mono_scale((tuple(range(2)), (0, 0)), eigen_bit, 2)
        want_rz = (tuple(range(2)), (0, 0))
        if rx_op != want_rx or rz_op != want_rz:
            S.cache["middle"] = {"error": "radical scalar labels in a block are wrong"}
            return S.cache["middle"]
        blocks.append((2, 1))
        pairs.append((eigen_bit, 0))
    restrictions = set()
    for pa in R.char_params:
        ca = R.char_table(pa)
        for pb in R.char_params:
            cb = R.char_table(pb)
            xa = ca[r]
            zb = cb[r]
            xbit = (xa // (R.phase_order // 2)) % 2
            zbit = (zb // (R.phase_order // 2)) % 2
            restrictions.add((xbit, zbit))
    total_pairs = {(base_x ^ tx, base_z ^ tz)
                   for base_x, base_z in pairs for tx, tz in restrictions}
    data = {
        "u": u, "char": char, "I": I, "ann": ann,
        "radical": radical, "expected_radical": expected_rad,
        "exact_images": exact_images,
        "projective_images": projective_images,
        "group_images": len(group_images),
        "blocks": tuple(blocks), "model_pairs": tuple(pairs),
        "all_pairs": frozenset(total_pairs),
    }
    S.cache["middle"] = data
    return data


def gate_C7(S, world):
    del world
    if S.R.name not in ("Z4", "F2[e]/e2"):
        return True, "N/A: field has no nonzero maximal-ideal stratum"
    data = middle_data(S)
    if "error" in data:
        return False, data["error"]
    if data["I"] != data["ann"] or data["radical"] != data["expected_radical"]:
        return False, "I_psi, Ann(u), and phase radical disagree"
    claimed_images = (7 if S.mode == "--red-middle-images" and S.R.name == "Z4"
                      else 8)
    if data["exact_images"] != claimed_images or data["projective_images"] != 8:
        return False, "Weyl images exact/projective=(%d,%d), claimed exact=%d" % (
            data["exact_images"], data["projective_images"], claimed_images)
    if data["blocks"] != ((2, 1), (2, 1)):
        return False, "4-d model decomposition=%s" % (data["blocks"],)
    if data["model_pairs"] != ((0, 0), (1, 0)) or len(data["all_pairs"]) != 4:
        return False, "radical-character pairs model=%s total=%s" % (
            data["model_pairs"], sorted(data["all_pairs"]))
    return True, "I=Ann(u), rad=I^2 size 4; Weyl images=8 (projective=8), H image=16; model=2+2, multiplicity 1 each, 2 of 4 inequivalent 2-d irreps"


def cyclic_submodule(S, v):
    R = S.R
    a, b = divmod(v, S.n)
    return frozenset(int(R.MUL[r, a]) * S.n + int(R.MUL[r, b])
                     for r in range(S.n))


def all_submodules(S):
    if "submodules" in S.cache:
        return S.cache["submodules"]
    zero = frozenset((0,))
    found, queue = {zero}, [zero]
    cyclic = [cyclic_submodule(S, v) for v in range(S.nV)]
    while queue:
        L = queue.pop(0)
        for v in range(S.nV):
            if v in L:
                continue
            N = frozenset(int(S.VADD[x, y]) for x in L for y in cyclic[v])
            if N not in found:
                found.add(N)
                queue.append(N)
    result = sorted(found, key=lambda x: (len(x), tuple(sorted(x))))
    S.cache["submodules"] = result
    return result


def perpendicular(S, L):
    return frozenset(w for w in range(S.nV)
                     if all(S.reference[int(S.OMEGA[l, w])] == 0 for l in L))


def algebra_character_count(S, L, group_exponent):
    """Exhaust all A_L characters in roots allowed by the H exponent."""
    R, m = S.R, group_exponent
    if m % R.phase_order != 0:
        return None
    elems = sorted(L)
    pos = {v: k for k, v in enumerate(elems)}
    nonzero = [v for v in elems if v != 0]
    count = 0
    for values in itertools.product(range(m), repeat=len(nonzero)):
        lam = {0: 0}
        lam.update({v: values[k] for k, v in enumerate(nonzero)})
        good = True
        for v in elems:
            for w in elems:
                phase = S.reference[int(S.BETA0[v, w])] * (m // R.phase_order)
                vw = int(S.VADD[v, w])
                if (lam[v] + lam[w] - phase - lam[vw]) % m != 0:
                    good = False
                    break
            if not good:
                break
        if good:
            count += 1
    return count


def gate_C8(S, world):
    del world
    modules = all_submodules(S)
    lags = []
    for L in modules:
        P = perpendicular(S, L)
        if len(L) * len(P) != S.nV:
            return False, "dual-size identity fails at L=%s" % sorted(L)
        if L == P:
            lags.append(L)
    free = [L for L in lags if any(cyclic_submodule(S, v) == L for v in L)]
    nonfree = [L for L in lags if L not in free]
    observed = (len(lags), len(free), len(nonfree))
    if S.mode == "--red-drop-nonfree" and S.R.name == "F2[e]/e2":
        claimed = (7, 7, 0)
    else:
        claimed = EXPECTED[S.R.name]["lags"]
    if observed != claimed:
        return False, "Lagrangians total/free/nonfree=%s, claimed %s" % (
            observed, claimed)
    if any(len(L) != S.n for L in lags):
        return False, "a Lagrangian does not have |R| elements"
    if S.R.name in ("Z4", "F2[e]/e2"):
        ideal = frozenset(S.R.maximal)
        witness = frozenset(a * S.n + b for a in ideal for b in ideal)
        if nonfree != [witness]:
            return False, "unique non-free Lagrangian is not m+m"
    exponent = group_stats(S)["exponent"]
    ok, detail = verify_cyclotomic(CycRing(exponent))
    if not ok:
        return False, "A_L phase arena failed: %s" % detail
    counts = [algebra_character_count(S, L, exponent) for L in lags]
    if any(c != S.n for c in counts):
        return False, "A_L character counts=%s, expected %d each" % (counts, S.n)
    labels = sum(counts)
    if labels != EXPECTED[S.R.name]["labels"]:
        return False, "model labels=%d, expected %d" % (
            labels, EXPECTED[S.R.name]["labels"])
    histogram = {}
    for L in modules:
        histogram[len(L)] = histogram.get(len(L), 0) + 1
    return True, "submodules=%d %s; Lagrangians=%s; %d exact A_L characters/model labels" % (
        len(modules), histogram, observed, labels)


GATES = (
    ("A0", gate_A0),
    ("C1", gate_C1),
    ("C2", gate_C2),
    ("C3", gate_C3),
    ("C4", gate_C4),
    ("C5", gate_C5),
    ("C6", gate_C6),
    ("C7", gate_C7),
    ("C8", gate_C8),
)


def usage():
    print("usage: python3 small_rings_catalogue_check.py [MODE]")
    print("green runs all gates at all five rings; red modes must exit nonzero")
    for mode, description in MODES.items():
        print("  %-28s %s" % (mode, description))


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] not in MODES
                         and argv[1] not in ("-h", "--help", "help")):
        usage()
        return EXIT_DEFECT
    if len(argv) == 2 and argv[1] in ("-h", "--help", "help"):
        usage()
        return EXIT_GREEN
    mode = argv[1] if len(argv) == 2 else "green"
    rings = make_rings()
    world = {name: Setting(rings[name], mode) for name in RING_NAMES}
    order = RING_NAMES if mode == "green" else (TARGET[mode][0],)
    failures = []
    print("small_rings_catalogue_check mode=%s" % mode)
    print("exact arithmetic: finite tables + Z[zeta_d] vectors; no floats/tolerances")
    for name in order:
        S = world[name]
        for gate, fn in GATES:
            try:
                ok, detail = fn(S, world)
            except Exception as exc:  # a raised evidence gate is a checker failure
                ok, detail = False, "raised %s: %s" % (type(exc).__name__, exc)
            print("ring=%-11s %-2s %s %s" % (
                name, gate, "PASS" if ok else "FAIL", detail))
            if not ok:
                failures.append((name, gate, detail))
    print("---- summary ----")
    if mode == "green":
        if failures:
            for name, gate, detail in failures:
                print("FAILED %s %s: %s" % (name, gate, detail))
            print("GREEN RUN FAILED: %d failures" % len(failures))
            return EXIT_RED_CAUGHT
        print("GREEN: C1--C8 passed at all five rings; A0 is named decoration/precondition")
        return EXIT_GREEN
    if not failures:
        print("RED MODE NOT CAUGHT: checker defect")
        return EXIT_DEFECT
    first_name, first_gate, detail = failures[0]
    intended = TARGET[mode][1]
    print("KILLED BY %s at %s: %s" % (first_gate, first_name, detail))
    if first_gate != intended:
        print("RED CAUGHT AT WRONG FIRST GATE: expected %s" % intended)
        return EXIT_DEFECT
    print("RED MODE %s CAUGHT by pre-registered %s" % (mode, intended))
    return EXIT_RED_CAUGHT


if __name__ == "__main__":
    sys.exit(main(sys.argv))
