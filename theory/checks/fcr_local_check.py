#!/usr/bin/env python3
"""Pre-registered falsifier for finite commutative local rings (FCR-1).

Written in the independent check lane from briefs/fcr-local-target.md alone.
There are no repository imports.  Arithmetic is exact: finite rings are
explicit addition/multiplication tables and phases live in Z[zeta_n], encoded
as integer coefficient vectors modulo Phi_d for d in {3, 9, 27}.
The code writes ``n = |R|`` for ring order; ``q`` is reserved for ``|kappa|``.

No gate uses ``assert`` (``python3 -O`` must not weaken the checker), no
floating-point value is formed, and there is no tolerance.
"""

import itertools
import random
import sys

import numpy as np


SEED_NAMES = (
    "F3", "F9", "Z9", "F3[e]/e2", "Z27", "F3[t]/t3",
    "F3[x,y]/(x,y)^2",
)
FROBENIUS = set(SEED_NAMES[:-1])
LAGRANGIAN_SEEDS = {"Z9", "F3[e]/e2"}
LOW_ADM_CENSUS = {"F3", "Z9", "F3[e]/e2"}

MODES = {
    "green": "unmutated checker",
    "--red-nongenerating":
        "feed the Z/9 FCR-ALG pipeline psi_3, whose kernel ideal is (3)",
    "--red-transpose":
        "replace beta_0 by beta_0^T while retaining beta-beta^T=omega",
    "--red-frobenius-blind":
        "claim the least-degenerate character of the non-Frobenius seed generates",
    "--red-free-only":
        "claim every Lagrangian at Z/9 is free",
    "--red-torsor":
        "claim psi_u generates at Z/9 for the nonunit u=3",
    "--red-dim":
        "claim |R|^2+1 independent Weyl operators at F3",
    "--red-halfweyl-drop":
        "use s(v,v), not s(v,v)/2, in the G9 coboundary map",
    "--red-g6-arena-confusion":
        "claim the formal Weyl commutant has the matrix-image dimension",
    "--red-profile-drop-identity":
        "omit the identity from the G11 powering census",
}

TARGET = {
    "--red-nongenerating": ("Z9", "G5"),
    "--red-transpose": ("F3", "G2"),
    "--red-frobenius-blind": ("F3[x,y]/(x,y)^2", "G1"),
    "--red-free-only": ("Z9", "G7"),
    "--red-torsor": ("Z9", "G8"),
    "--red-dim": ("F3", "G5"),
    "--red-halfweyl-drop": ("F3", "G9"),
    "--red-g6-arena-confusion": ("Z9", "G6"),
    "--red-profile-drop-identity": ("Z9", "G11"),
}

EXIT_GREEN, EXIT_RED_CAUGHT, EXIT_DEFECT = 0, 1, 2


# ---------------------------------------------------------------------------
# Exact Z[zeta_d] arithmetic, d = 3, 9, 27.
# Phi_{3^k}(x) = x^(2*3^(k-1)) + x^(3^(k-1)) + 1.
# ---------------------------------------------------------------------------
class CycRing:
    def __init__(self, phase_order):
        if phase_order not in (3, 9, 27):
            raise ValueError("cyclotomic order must be 3, 9, or 27")
        self.phase_order = phase_order
        m = phase_order // 3
        self.deg = 2 * m
        self.phi = [0] * (self.deg + 1)
        self.phi[0] = self.phi[m] = self.phi[self.deg] = 1
        self.zero = (0,) * self.deg
        self.one = (1,) + (0,) * (self.deg - 1)
        self.zeta = self.reduce([0, 1])
        self.zpow = [self.one]
        for _ in range(phase_order):
            self.zpow.append(self.mul(self.zpow[-1], self.zeta))

    def reduce(self, coeffs):
        c = list(coeffs)
        if len(c) < self.deg:
            c += [0] * (self.deg - len(c))
        for d in range(len(c) - 1, self.deg - 1, -1):
            lead = c[d]
            if lead:
                c[d] = 0
                shift = d - self.deg
                for j in range(self.deg):
                    if self.phi[j]:
                        c[shift + j] -= lead * self.phi[j]
        c = c[:self.deg]
        if len(c) < self.deg:
            c += [0] * (self.deg - len(c))
        return tuple(c)

    def add(self, x, y):
        return tuple(a + b for a, b in zip(x, y))

    def mul(self, x, y):
        out = [0] * (2 * self.deg - 1)
        for i, a in enumerate(x):
            if a:
                for j, b in enumerate(y):
                    if b:
                        out[i + j] += a * b
        return self.reduce(out)


def verify_cyclotomic(C):
    """Verify the prime-power formula and exact order without evaluation."""
    m, phase_order = C.phase_order // 3, C.phase_order
    # (x^(2m)+x^m+1)(x^m-1) = x^(3m)-1.
    lhs = [0] * (phase_order + 1)
    for i, a in enumerate(C.phi):
        if a:
            lhs[i + m] += a
            lhs[i] -= a
    rhs = [0] * (phase_order + 1)
    rhs[0], rhs[phase_order] = -1, 1
    if lhs != rhs:
        return False, "cyclotomic product identity failed"
    if C.zpow[phase_order] != C.one:
        return False, "zeta_%d^%d != 1" % (phase_order, phase_order)
    if len(set(C.zpow[:phase_order])) != phase_order:
        return False, "the first %d powers of zeta_%d are not distinct" % (
            phase_order, phase_order)
    return True, "Phi_%d=x^%d+x^%d+1; zeta has exact order %d" % (
        phase_order, 2 * m, m, phase_order)


# ---------------------------------------------------------------------------
# Explicit finite-ring tables.
# ---------------------------------------------------------------------------
class FiniteRing:
    def __init__(self, name, coord_mods, mul_coords, reference_param):
        self.name = name
        self.coord_mods = tuple(coord_mods)
        self.n = int(np.prod(np.array(coord_mods, dtype=np.int64)))
        self.reference_param = tuple(reference_param)
        self.elements = tuple(self._coords(i) for i in range(self.n))
        self.index = {x: i for i, x in enumerate(self.elements)}
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
            next(j for j in range(self.n) if self.ADD[i, j] == 0)
            for i in range(self.n)
        ], dtype=np.int64)
        self.units = tuple(i for i in range(self.n)
                           if np.any(self.MUL[i, :] == self.one))
        self.maximal = tuple(i for i in range(self.n) if i not in set(self.units))
        self.char_order = max(self.coord_mods)
        self.char_params = tuple(itertools.product(
            *[range(m) for m in self.coord_mods]))

    def _coords(self, i):
        out = []
        for m in self.coord_mods:
            out.append(i % m)
            i //= m
        return tuple(out)

    def char_table(self, param):
        phase_order = self.char_order
        return tuple(sum(param[k] * x[k] * (phase_order // self.coord_mods[k])
                         for k in range(len(param))) % phase_order
                     for x in self.elements)

    def scaled_character(self, param, u):
        base = self.char_table(param)
        return tuple(base[int(self.MUL[u, x])] for x in range(self.n))

    def ideal_in_kernel(self, char):
        return frozenset(r for r in range(self.n)
                         if all(char[int(self.MUL[r, x])] == 0
                                for x in range(self.n)))


def make_rings():
    def prime_mul(x, y):
        return ((x[0] * y[0]) % 3,)

    def f9_mul(x, y):
        # F3[t]/(t^2+1), so t^2=2.  Irreducibility is checked from the table.
        a, b = x
        c, d = y
        return ((a * c + 2 * b * d) % 3, (a * d + b * c) % 3)

    def dual_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c) % 3, (a * d + b * c) % 3)

    def trunc3_mul(x, y):
        a, b, c = x
        d, e, f = y
        return ((a * d) % 3,
                (a * e + b * d) % 3,
                (a * f + b * e + c * d) % 3)

    def nonfrob_mul(x, y):
        a, b, c = x
        d, e, f = y
        return ((a * d) % 3,
                (a * e + b * d) % 3,
                (a * f + c * d) % 3)

    def zn_mul(modulus):
        return lambda x, y: ((x[0] * y[0]) % modulus,)

    return {
        "F3": FiniteRing("F3", (3,), prime_mul, (1,)),
        "F9": FiniteRing("F9", (3, 3), f9_mul, (2, 0)),
        "Z9": FiniteRing("Z9", (9,), zn_mul(9), (1,)),
        "F3[e]/e2": FiniteRing("F3[e]/e2", (3, 3), dual_mul, (0, 1)),
        "Z27": FiniteRing("Z27", (27,), zn_mul(27), (1,)),
        "F3[t]/t3": FiniteRing("F3[t]/t3", (3, 3, 3), trunc3_mul, (0, 0, 1)),
        "F3[x,y]/(x,y)^2": FiniteRing(
            "F3[x,y]/(x,y)^2", (3, 3, 3), nonfrob_mul, (0, 0, 1)),
    }


def verify_ring(R):
    n, A, M = R.n, R.ADD, R.MUL
    idx = np.arange(n, dtype=np.int64)
    if not np.array_equal(A[R.zero, :], idx):
        return False, "additive identity failed"
    if not np.array_equal(M[R.one, :], idx):
        return False, "multiplicative identity failed"
    if not np.array_equal(A, A.T) or not np.array_equal(M, M.T):
        return False, "commutativity failed"
    J, K = np.meshgrid(idx, idx, indexing="ij")
    for i in range(n):
        if not np.array_equal(A[A[i, J], K], A[i, A[J, K]]):
            return False, "addition is not associative"
        if not np.array_equal(M[M[i, J], K], M[i, M[J, K]]):
            return False, "multiplication is not associative"
        if not np.array_equal(M[i, A[J, K]], A[M[i, J], M[i, K]]):
            return False, "distributivity failed"
    m = set(R.maximal)
    if R.zero not in m or R.one in m:
        return False, "nonunits do not form a proper candidate maximal ideal"
    if any(int(A[x, y]) not in m for x in m for y in m):
        return False, "nonunits not additively closed"
    if any(int(M[r, x]) not in m for r in range(n) for x in m):
        return False, "nonunits not an ideal"
    return True, "explicit %dx%d tables satisfy ring axioms; units=%d, |m|=%d" % (
        n, n, len(R.units), len(R.maximal))


# ---------------------------------------------------------------------------
# Phase space and exact monomial matrices.
# ---------------------------------------------------------------------------
class Setting:
    def __init__(self, ring, cyc, mode):
        self.R, self.C, self.mode = ring, cyc, mode
        R, n = ring, ring.n
        self.n, self.nV = n, n * n
        self.VA = np.repeat(np.arange(n, dtype=np.int64), n)
        self.VB = np.tile(np.arange(n, dtype=np.int64), n)
        a, b = self.VA[:, None], self.VB[:, None]
        ap, bp = self.VA[None, :], self.VB[None, :]
        self.VADD = R.ADD[a, ap] * n + R.ADD[b, bp]
        self.OMEGA = R.ADD[R.MUL[a, bp], R.NEG[R.MUL[ap, b]]]
        self.BETA0 = R.MUL[a, bp]
        self.BETAT = R.MUL[ap, b]
        self.BETA = self.BETAT if mode == "--red-transpose" else self.BETA0
        self.char_records = []
        for param in R.char_params:
            table = R.char_table(param)
            self.char_records.append({
                "param": param,
                "table": table,
                "ideal": R.ideal_in_kernel(table),
            })
        self.nontrivial = [x for x in self.char_records
                           if any(e != 0 for e in x["table"])]
        self.generating = [x for x in self.nontrivial if x["ideal"] == {0}]
        self.reference = R.char_table(R.reference_param)

    def chosen_character(self):
        if self.mode == "--red-nongenerating" and self.R.name == "Z9":
            return self.R.scaled_character(self.R.reference_param, 3)
        return self.reference


def mono_mul(X, Y, phase_order):
    px, ex = X
    py, ey = Y
    return (tuple(px[k] for k in py),
            tuple((ex[py[k]] + ey[k]) % phase_order for k in range(len(py))))


def mono_scale(X, exponent, phase_order):
    return X[0], tuple((e + exponent) % phase_order for e in X[1])


def mono_equal(X, Y, C):
    return X[0] == Y[0] and all(C.zpow[x] == C.zpow[y]
                               for x, y in zip(X[1], Y[1]))


def build_model(S, char):
    R, n, phase_order = S.R, S.n, S.C.phase_order
    ops = []
    for v in range(S.nV):
        a, b = int(S.VA[v]), int(S.VB[v])
        perm, exps = [], []
        for y in range(n):
            ya = int(R.ADD[y, a])
            perm.append(ya)
            phase_arg = int(R.NEG[int(R.MUL[b, ya])])
            exps.append(char[phase_arg] % phase_order)
        ops.append((tuple(perm), tuple(exps)))
    return ops


def commutant_dimension(ops, C):
    """Exact union-find-with-potentials solution of TW=WT."""
    n, phase_order = len(ops[0][0]), C.phase_order
    count = n * n
    parent = list(range(count))
    potential = [0] * count
    dead = [False] * count

    def find(x):
        if parent[x] == x:
            return x, 0
        root, up = find(parent[x])
        potential[x] = (potential[x] + up) % phase_order
        parent[x] = root
        return root, potential[x]

    for perm, exps in ops:
        for row in range(n):
            for col in range(n):
                u = row * n + col
                w = perm[row] * n + perm[col]
                delta = (exps[col] - exps[row]) % phase_order
                ru, pu = find(u)
                rw, pw = find(w)
                if ru == rw:
                    if C.zpow[(pu - pw - delta) % phase_order] != C.one:
                        dead[ru] = True
                else:
                    # value(u)=z^delta value(w), potentials are value(node)=z^p value(root)
                    parent[rw] = ru
                    potential[rw] = (pu - delta - pw) % phase_order
                    dead[ru] = dead[ru] or dead[rw]
    roots = set()
    for x in range(count):
        root, _ = find(x)
        if not dead[root]:
            roots.add(root)
    return len(roots)


def exact_weyl_rank(ops, C):
    """Rank from exact character orthogonality inside disjoint supports."""
    classes = {}
    for perm, exps in ops:
        classes.setdefault(perm, set()).add(exps)
    perms = list(classes)
    n = len(perms[0])
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            if any(perms[i][x] == perms[j][x] for x in range(n)):
                return None, "different permutation classes have overlapping support"
    rank = 0
    for rows in classes.values():
        rows = list(rows)
        for i, x in enumerate(rows):
            for j, y in enumerate(rows):
                inner = C.zero
                for k in range(n):
                    inner = C.add(inner, C.zpow[(x[k] - y[k]) % C.phase_order])
                want = (n,) + (0,) * (C.deg - 1) if i == j else C.zero
                if inner != want:
                    return None, "phase rows are neither equal nor exactly orthogonal"
        rank += len(rows)
    return rank, "exact Gram matrices diagonal on every disjoint support class"


# ---------------------------------------------------------------------------
# Gates G1--G11.
# ---------------------------------------------------------------------------
def gate_G1(S):
    R = S.R
    if len(S.nontrivial) != R.n - 1:
        return False, "|X(R)|=%d, expected %d" % (len(S.nontrivial), R.n - 1)
    tables = [x["table"] for x in S.char_records]
    if len(set(tables)) != R.n:
        return False, "the %d character parameters do not give distinct tables" % R.n
    for rec in S.char_records:
        t, I = rec["table"], rec["ideal"]
        if any(t[int(R.ADD[x, y])] != (t[x] + t[y]) % R.char_order
               for x in range(R.n) for y in range(R.n)):
            return False, "parameter %s is not additive" % (rec["param"],)
        if 0 not in I:
            return False, "I_psi omits zero"
        if any(int(R.ADD[x, y]) not in I for x in I for y in I):
            return False, "computed I_psi is not additively closed"
        if any(int(R.MUL[r, x]) not in I for r in range(R.n) for x in I):
            return False, "computed I_psi is not an ideal"
        if any(t[x] != 0 for x in I):
            return False, "computed I_psi is not contained in ker psi"
    if R.name in FROBENIUS:
        unit_chars = {R.scaled_character(R.reference_param, u) for u in R.units}
        gen_chars = {x["table"] for x in S.generating}
        if unit_chars != gen_chars:
            return False, "Gen(R) differs from {psi_u:u unit}"
        if len(gen_chars) != len(R.units):
            return False, "|Gen(R)|=%d, |R^x|=%d" % (len(gen_chars), len(R.units))
        return True, "X=%d; I_psi for all; Gen=%d=|R^x|" % (
            len(S.nontrivial), len(gen_chars))
    if S.generating:
        return False, "non-Frobenius probe has %d generating characters" % len(S.generating)
    m = set(R.maximal)
    for rec in S.nontrivial:
        if len(rec["ideal"]) <= 1 or not set(rec["ideal"]).issubset(m):
            return False, "character %s lacks an exhibited nonzero ideal in m" % (
                rec["param"],)
    if S.mode == "--red-frobenius-blind":
        chosen = min(S.nontrivial, key=lambda x: (len(x["ideal"]), x["param"]))
        if chosen["ideal"] != {0}:
            return False, ("forced generating claim fails: smallest I_psi has size %d, "
                           "witness ideal=%s" % (len(chosen["ideal"]),
                                                  sorted(chosen["ideal"])))
    sizes = {}
    for rec in S.nontrivial:
        sizes[len(rec["ideal"])] = sizes.get(len(rec["ideal"]), 0) + 1
    return True, "X=26; Gen=0 by exhaustion; kernel-ideal sizes=%s, all inside m" % sizes


def gate_G2(S):
    R, nV = S.R, S.nV
    diag = np.diag(S.OMEGA)
    if np.any(diag != 0):
        v = int(np.flatnonzero(diag != 0)[0])
        return False, "omega(v,v)=%d at v=%s" % (diag[v], divmod(v, S.n))
    for v in range(1, nV):
        if not np.any(S.OMEGA[v, :] != 0):
            return False, "R-radical contains v=%s" % (divmod(v, S.n),)
    e1, e2 = S.n, 1
    # Exhaust all pairs against the coordinate expansion; ring distributivity
    # (A0) then certifies additivity and homogeneity, without a cubic triple loop.
    first_expand = R.ADD[
        R.MUL[S.VA[:, None], S.OMEGA[e1, :][None, :]],
        R.MUL[S.VB[:, None], S.OMEGA[e2, :][None, :]],
    ]
    second_expand = R.ADD[
        R.MUL[S.OMEGA[:, e1][:, None], S.VA[None, :]],
        R.MUL[S.OMEGA[:, e2][:, None], S.VB[None, :]],
    ]
    if not np.array_equal(first_expand, S.OMEGA):
        return False, "omega is not R-linear in its first coordinate expansion"
    if not np.array_equal(second_expand, S.OMEGA):
        return False, "omega is not R-linear in its second coordinate expansion"
    diff = R.ADD[S.BETA, R.NEG[S.BETA.T]]
    if not np.array_equal(diff, S.OMEGA):
        bad = np.argwhere(diff != S.OMEGA)[0]
        i, j = int(bad[0]), int(bad[1])
        return False, "beta-beta^T != omega at %s,%s (%d vs %d)" % (
            divmod(i, S.n), divmod(j, S.n), diff[i, j], S.OMEGA[i, j])
    return True, "alternating on %d vectors; R-nondegenerate/bilinear; beta identity on %d pairs" % (
        nV, nV * nV)


def gate_G3(S):
    nV = S.nV
    for rec in S.nontrivial:
        table, I = rec["table"], rec["ideal"]
        exp_omega = np.take(np.array(table, dtype=np.int64), S.OMEGA)
        actual = frozenset(int(v) for v in range(nV)
                           if np.all(exp_omega[v, :] == 0))
        expected = frozenset(a * S.n + b for a in I for b in I)
        if actual != expected:
            return False, "rad(psi o omega) size %d != |I x I|=%d for %s" % (
                len(actual), len(expected), rec["param"])
    if S.mode == "--red-frobenius-blind" and S.R.name not in FROBENIUS:
        rec = min(S.nontrivial, key=lambda x: (len(x["ideal"]), x["param"]))
        actual_size = len(rec["ideal"]) ** 2
        if actual_size != 1:
            return False, "forced nondegeneracy fails: radical has size %d" % actual_size
    work = len(S.nontrivial) * nV * nV
    return True, "all %d nontrivial psi; full radical rows exhausted (%d phase lookups)" % (
        len(S.nontrivial), work)


def gate_G4(S):
    if S.R.name not in FROBENIUS:
        return True, "N/A: no generating character at this seed"
    char = S.chosen_character()
    ops, phase_order, nV = build_model(S, char), S.C.phase_order, S.nV
    bad_weyl = bad_comm = 0
    first_weyl = first_comm = None
    for i in range(nV):
        for j in range(nV):
            lhs = mono_mul(ops[i], ops[j], phase_order)
            rhs = mono_scale(ops[int(S.VADD[i, j])], char[int(S.BETA[i, j])], phase_order)
            if not mono_equal(lhs, rhs, S.C):
                bad_weyl += 1
                if first_weyl is None:
                    first_weyl = (i, j)
            rhs_comm = mono_scale(mono_mul(ops[j], ops[i], phase_order),
                                  char[int(S.OMEGA[i, j])], phase_order)
            if not mono_equal(lhs, rhs_comm, S.C):
                bad_comm += 1
                if first_comm is None:
                    first_comm = (i, j)
    if bad_weyl:
        return False, "Weyl relation fails in %d/%d pairs; first=%s" % (
            bad_weyl, nV * nV, tuple(divmod(x, S.n) for x in first_weyl))
    if bad_comm:
        return False, "commutation relation fails in %d/%d pairs; first=%s" % (
            bad_comm, nV * nV, tuple(divmod(x, S.n) for x in first_comm))
    return True, "Z(-b)X(a): Weyl and commutation identities exact on %d pairs" % (
        nV * nV)


def gate_G5(S):
    if S.R.name not in FROBENIUS:
        return True, "N/A: FCR-ALG assumes a generating character"
    char = S.chosen_character()
    ops = build_model(S, char)
    rank, note = exact_weyl_rank(ops, S.C)
    if rank is None:
        return False, note
    comm = commutant_dimension(ops, S.C)
    claimed = S.nV + 1 if S.mode == "--red-dim" and S.R.name == "F3" else S.nV
    if rank != claimed or comm != 1:
        return False, "exact Weyl rank=%d (claimed %d); commutant dimension=%d" % (
            rank, claimed, comm)
    return True, "%d Weyl operators independent; commutant dimension 1; %s" % (
        rank, note)


def gate_G6(S):
    if S.R.name != "Z9":
        return True, "N/A: designated non-generating probe is Z/9"
    R = S.R
    char = R.scaled_character(R.reference_param, 3)
    I = R.ideal_in_kernel(char)
    ops = build_model(S, char)
    matrix_comm = commutant_dimension(ops, S.C)
    # G6's |I|^2 quantity is the commutant of the formal Weyl basis inside
    # C_psi[V], i.e. its centre.  The non-faithful Schrodinger image has a
    # different commutant (dimension 3 here), recorded as an independent
    # diagnostic and used by the G5 red pipeline.
    central = [v for v in range(S.nV)
               if all(char[int(S.OMEGA[v, w])] == 0 for w in range(S.nV))]
    comm = len(central)
    if I != frozenset((0, 3, 6)):
        return False, "psi_3 has I=%s, expected (3)={0,3,6}" % sorted(I)
    formal_claim = (matrix_comm if S.mode == "--red-g6-arena-confusion"
                    else len(I) ** 2)
    if comm <= 1 or comm != formal_claim:
        return False, ("formal Weyl commutant dimension=%d, claimed %d; "
                       "matrix-image dimension=%d") % (
            comm, formal_claim, matrix_comm)
    if matrix_comm != 3:
        return False, "matrix-image commutant dimension=%d, expected 3" % matrix_comm
    return True, ("psi_3: I=(3), |I|=3; formal Weyl commutant dimension=9=|I|^2; "
                  "matrix-image commutant dimension=%d" % matrix_comm)


def cyclic_submodule(S, v):
    R, n = S.R, S.n
    a, b = divmod(v, n)
    return frozenset(int(R.MUL[r, a]) * n + int(R.MUL[r, b])
                     for r in range(n))


def all_submodules(S):
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
    return sorted(found, key=lambda x: (len(x), tuple(sorted(x))))


def perpendicular(S, L, char):
    return frozenset(w for w in range(S.nV)
                     if all(char[int(S.OMEGA[l, w])] == 0 for l in L))


def gate_G7(S):
    if S.R.name not in LAGRANGIAN_SEEDS:
        return True, "N/A: full Lagrangian census is registered only at the two order-9 chain rings"
    modules = all_submodules(S)
    hist = {}
    lags = []
    for L in modules:
        hist[len(L)] = hist.get(len(L), 0) + 1
        P = perpendicular(S, L, S.reference)
        if len(L) * len(P) != S.nV:
            return False, "|L||L^perp|=%d, expected %d at L=%s" % (
                len(L) * len(P), S.nV, sorted(L))
        if L == P:
            lags.append(L)
    if hist != {1: 1, 3: 4, 9: 13, 27: 4, 81: 1}:
        return False, "submodule size histogram=%s" % hist
    free = [L for L in lags if any(cyclic_submodule(S, v) == L for v in L)]
    nonfree = [L for L in lags if L not in free]
    if any(len(L) != S.n for L in lags):
        return False, "a self-perpendicular submodule does not have |R| elements"
    if len(lags) != 13 or len(free) != 12 or len(nonfree) != 1:
        return False, "Lagrangians total/free/nonfree=%s, expected (13,12,1)" % (
            (len(lags), len(free), len(nonfree)),)
    if S.mode == "--red-free-only" and nonfree:
        return False, "free-only claim killed by nonfree L=%s" % sorted(nonfree[0])
    return True, "23 submodules %s; Lagrangians=13 (12 free, 1 nonfree); dual-size identity throughout" % hist


def gate_G8(S):
    if S.R.name not in FROBENIUS:
        return True, "N/A: Gen(R) is empty"
    R = S.R
    unit_tables = []
    for u in R.units:
        char = R.scaled_character(R.reference_param, u)
        if R.ideal_in_kernel(char) != {0}:
            return False, "unit u=%d gives a non-generating psi_u" % u
        unit_tables.append(char)
    if len(set(unit_tables)) != len(R.units):
        return False, "distinct units do not have distinct central characters"
    for u in R.maximal:
        char = R.scaled_character(R.reference_param, u)
        if R.ideal_in_kernel(char) == {0}:
            return False, "nonunit u=%d unexpectedly gives a generating psi_u" % u
    if S.mode == "--red-torsor" and R.name == "Z9":
        I = R.ideal_in_kernel(R.scaled_character(R.reference_param, 3))
        if I != {0}:
            return False, "forced torsor claim at u=3 fails: I_psi=(3), size %d" % len(I)
    return True, "%d unit-scaled generating characters, all distinct; %d elements of m non-generating" % (
        len(R.units), len(R.maximal))


def sym_form_table(S, alpha, gamma, delta):
    R = S.R
    a, b = S.VA[:, None], S.VB[:, None]
    ap, bp = S.VA[None, :], S.VB[None, :]
    aa = R.MUL[a, ap]
    cross = R.ADD[R.MUL[a, bp], R.MUL[ap, b]]
    bb = R.MUL[b, bp]
    return R.ADD[R.ADD[R.MUL[alpha, aa], R.MUL[gamma, cross]], R.MUL[delta, bb]]


def seeded_symmetric_parameters(n, count):
    rng = random.Random(0xF0C100 + n)
    chosen = set()
    while len(chosen) < count:
        chosen.add((rng.randrange(n), rng.randrange(n), rng.randrange(n)))
    return sorted(chosen)


def gate_G9(S):
    R, n = S.R, S.n
    two = int(R.ADD[R.one, R.one])
    invs = [x for x in range(n) if int(R.MUL[two, x]) == R.one]
    if len(invs) != 1:
        return False, "2 has %d inverses" % len(invs)
    half = invs[0]
    halfomega = R.MUL[half, S.OMEGA]
    if not np.array_equal(halfomega, R.NEG[halfomega.T]):
        return False, "omega/2 is not antisymmetric"
    if not np.array_equal(R.ADD[halfomega, R.NEG[halfomega.T]], S.OMEGA):
        return False, "omega/2 is not admissible"

    all_params = list(itertools.product(range(n), repeat=3))
    antisym = 0
    low_full = S.R.name in LOW_ADM_CENSUS
    if low_full:
        params = all_params
    elif n <= 9:
        params = all_params
    else:
        params = seeded_symmetric_parameters(n, 128)

    # At high order, census uniqueness by the coefficient equations.  At the
    # three registered low seeds, also compare every full table.
    for alpha, gamma, delta in all_params:
        coeff_antisym = (int(R.ADD[alpha, alpha]) == 0 and
                         int(R.ADD[delta, delta]) == 0 and
                         int(R.ADD[R.ADD[R.one, gamma], gamma]) == 0)
        if coeff_antisym:
            antisym += 1
        if low_full:
            s = sym_form_table(S, alpha, gamma, delta)
            B = R.ADD[S.BETA0, s]
            if not np.array_equal(R.ADD[B, R.NEG[B.T]], S.OMEGA):
                return False, "beta+s left Adm at parameters %s" % ((alpha, gamma, delta),)
            table_antisym = np.array_equal(B, R.NEG[B.T])
            if table_antisym != coeff_antisym:
                return False, "coefficient/table antisymmetry disagreement"
            if table_antisym and not np.array_equal(B, halfomega):
                return False, "an antisymmetric admissible member differs from omega/2"
    if antisym != 1:
        return False, "Adm has %d antisymmetric coefficient triples, expected 1" % antisym

    for alpha, gamma, delta in params:
        s = sym_form_table(S, alpha, gamma, delta)
        diag = np.diag(s)
        if S.mode == "--red-halfweyl-drop":
            quad = diag
        else:
            quad = R.MUL[half, diag]
        lhs = quad[S.VADD]
        rhs = R.ADD[R.ADD[quad[:, None], quad[None, :]], s]
        if not np.array_equal(lhs, rhs):
            bad = np.argwhere(lhs != rhs)[0]
            return False, "phi_s coboundary fails for s=%s at v=%d,w=%d" % (
                (alpha, gamma, delta), int(bad[0]), int(bad[1]))
    kind = "all" if n <= 9 else "seeded"
    return True, "2 inverse=%d; |Adm|=%d, unique antisymmetric omega/2; phi_s identity for %s %d s" % (
        half, n ** 3, kind, len(params))


F3_MODEL = (
    ((0, 1, 2), (0, 0, 0)), ((0, 1, 2), (0, 2, 1)),
    ((0, 1, 2), (0, 1, 2)), ((1, 2, 0), (0, 0, 0)),
    ((1, 2, 0), (2, 1, 0)), ((1, 2, 0), (1, 2, 0)),
    ((2, 0, 1), (0, 0, 0)), ((2, 0, 1), (1, 0, 2)),
    ((2, 0, 1), (2, 0, 1)),
)


def h_profile(S, beta=None):
    R = S.R
    B = S.BETA0 if beta is None else beta
    ts = np.repeat(np.arange(S.n, dtype=np.int64), S.nV)
    vs = np.tile(np.arange(S.nV, dtype=np.int64), S.n)
    if S.mode == "--red-profile-drop-identity":
        keep = (ts != R.zero) | (vs != 0)
        ts, vs = ts[keep], vs[keep]
    cur_t = np.zeros(len(ts), dtype=np.int64)
    cur_v = np.zeros(len(vs), dtype=np.int64)
    orders = np.zeros(len(ts), dtype=np.int64)
    for k in range(1, S.n ** 3 + 1):
        cur_t = R.ADD[R.ADD[cur_t, ts], B[cur_v, vs]]
        cur_v = S.VADD[cur_v, vs]
        hit = (orders == 0) & (cur_t == 0) & (cur_v == 0)
        orders[hit] = k
        if np.all(orders != 0):
            break
    if np.any(orders == 0):
        return None
    return {int(k): int(np.sum(orders == k)) for k in sorted(set(orders.tolist()))}


def gate_G10(S):
    if S.R.name != "F3":
        return True, "N/A: field-regression seed is F3"
    data = {
        "X": len(S.nontrivial), "Gen": len(S.generating), "units": len(S.R.units),
        "V": S.nV, "pairs": S.nV ** 2,
    }
    if data != {"X": 2, "Gen": 2, "units": 2, "V": 9, "pairs": 81}:
        return False, "F3 count regression=%s" % data
    if sorted(len(x["ideal"]) ** 2 for x in S.nontrivial) != [1, 1]:
        return False, "F3 radical regression is not [1,1]"
    if np.any(np.diag(S.OMEGA) != 0):
        return False, "F3 alternating-form regression failed"
    if not np.array_equal(S.R.ADD[S.BETA, S.R.NEG[S.BETA.T]], S.OMEGA):
        return False, "F3 beta regression failed"
    model = tuple(build_model(S, S.reference))
    if model != F3_MODEL:
        return False, "F3 Z(-b)X(a) matrices differ from wh_kappa_check.py"
    lines = set()
    for v in range(1, S.nV):
        a, b = divmod(v, S.n)
        lines.add(tuple(sorted(int(S.R.MUL[r, a]) * S.n + int(S.R.MUL[r, b])
                               for r in range(S.n))))
    if len(lines) != 4:
        return False, "F3 line count=%d, wh regression expects 4" % len(lines)
    two = int(S.R.ADD[S.R.one, S.R.one])
    inv_two = [x for x in range(S.n) if int(S.R.MUL[two, x]) == S.R.one]
    antisym = sum(1 for alpha, gamma, delta in itertools.product(range(3), repeat=3)
                  if int(S.R.ADD[alpha, alpha]) == 0
                  and int(S.R.ADD[delta, delta]) == 0
                  and int(S.R.ADD[S.R.ADD[S.R.one, gamma], gamma]) == 0)
    if inv_two != [2] or antisym != 1:
        return False, "F3 half-Weyl regression=(inverse %s, antisym %d)" % (
            inv_two, antisym)
    rank, _ = exact_weyl_rank(list(model), S.C)
    comm = commutant_dimension(list(model), S.C)
    prof = h_profile(S)
    if (rank, comm, prof) != (9, 1, {1: 1, 3: 26}):
        return False, "F3 algebra/group regression=%s" % ((rank, comm, prof),)
    return True, ("WH regression exact: X=Gen=units=2; radicals=1; 4 lines; "
                  "rank=9; comm=1; Adm=27/unique half; fixed 9 matrices; H={1:1,3:26}")


def gate_G11(S):
    prof = h_profile(S)
    if prof is None:
        return False, "some H_beta0 element failed to return to identity"
    defects = []
    if sum(prof.values()) != S.n ** 3:
        defects.append("profile sum=%d, expected |R|^3=%d" % (
            sum(prof.values()), S.n ** 3))
    if prof.get(1) != 1:
        defects.append("identity count=%s, expected 1" % prof.get(1))
    if any((S.n ** 3) % order != 0 for order in prof):
        defects.append("an observed element order does not divide |H|")
    if defects:
        return False, "; ".join(defects)
    return True, "H_beta0 element-order profile=%s; sum=%d=|R|^3" % (
        prof, sum(prof.values()))


GATES = (
    ("G1", gate_G1), ("G2", gate_G2), ("G3", gate_G3),
    ("G4", gate_G4), ("G5", gate_G5), ("G6", gate_G6),
    ("G7", gate_G7), ("G8", gate_G8), ("G9", gate_G9),
    ("G10", gate_G10), ("G11", gate_G11),
)


def usage():
    print("usage: python3 fcr_local_check.py [MODE]")
    print("green runs G1--G11 at all seven seeds; every red mode must exit nonzero")
    for mode, text in MODES.items():
        print("  %-25s %s" % (mode, text))


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] not in MODES and
                         argv[1] not in ("-h", "--help", "help")):
        usage()
        return EXIT_DEFECT
    if len(argv) == 2 and argv[1] in ("-h", "--help", "help"):
        usage()
        return EXIT_GREEN
    mode = argv[1] if len(argv) == 2 else "green"
    rings = make_rings()
    if mode in ("green", "--red-transpose"):
        order = list(SEED_NAMES)
    else:
        order = [TARGET[mode][0]]
    failures = []
    print("fcr_local_check mode=%s" % mode)
    print("exact arithmetic: explicit ring tables; Z[zeta_d] integer vectors; no floats/tolerances")
    for name in order:
        R = rings[name]
        C = CycRing(R.char_order)
        ok, detail = verify_cyclotomic(C)
        print("seed=%-20s A0-CYC %s %s" % (name, "PASS" if ok else "FAIL", detail))
        if not ok:
            failures.append((name, "A0-CYC", detail))
            if mode != "green":
                break
        ok, detail = verify_ring(R)
        print("seed=%-20s A0-RING %s %s" % (name, "PASS" if ok else "FAIL", detail))
        if not ok:
            failures.append((name, "A0-RING", detail))
            if mode != "green":
                break
        S = Setting(R, C, mode)
        for gate, fn in GATES:
            try:
                ok, detail = fn(S)
            except Exception as exc:  # noqa: BLE001 - a raised gate is a failure
                ok, detail = False, "raised %s: %s" % (type(exc).__name__, exc)
            print("seed=%-20s %-3s %s %s" % (
                name, gate, "PASS" if ok else "FAIL", detail))
            if not ok:
                failures.append((name, gate, detail))
        if mode not in ("green", "--red-transpose") and failures:
            break
    print("---- summary ----")
    if mode == "green":
        if failures:
            for seed, gate, detail in failures:
                print("FAILED %s %s: %s" % (seed, gate, detail))
            print("GREEN RUN FAILED: %d failures" % len(failures))
            return EXIT_RED_CAUGHT
        print("GREEN: G1--G11 passed at every applicable seed; N/A scope lines shown explicitly")
        return EXIT_GREEN
    if not failures:
        print("RED MODE NOT CAUGHT: mutation produced no failing gate (checker defect)")
        return EXIT_DEFECT
    seed, gate, detail = failures[0]
    intended = TARGET[mode][1]
    print("KILLED BY %s at %s: %s" % (gate, seed, detail))
    by_gate = {}
    for failed_seed, failed_gate, _ in failures:
        by_gate.setdefault(failed_gate, []).append(failed_seed)
    for failed_gate in sorted(by_gate):
        print("FIRED %-3s at %s" % (failed_gate, by_gate[failed_gate]))
    if gate != intended:
        print("RED MODE CAUGHT, but first gate differs from pre-registration: expected %s" % intended)
        return EXIT_DEFECT
    print("RED MODE %s CAUGHT by pre-registered %s" % (mode, gate))
    return EXIT_RED_CAUGHT


if __name__ == "__main__":
    sys.exit(main(sys.argv))
