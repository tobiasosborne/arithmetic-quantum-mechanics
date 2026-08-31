#!/usr/bin/env python3
"""Pre-registered falsifier for the Weyl-Heisenberg system of Spec kappa.

Written by lane wh-check from briefs/wh-kappa-target.md ALONE, before and
independently of any proof shard: this lane did not read the prover's lane or
v0.1/report/. Expectations for every gate were fixed in EXPECTATIONS.md before
this file was written.

Destination: theory/checks/wh_kappa_check.py (runs from anywhere; no repo
imports, python3 + numpy only).

EXACT ARITHMETIC ONLY. Z[zeta_p] is represented as integer vectors modulo the
p-th cyclotomic polynomial Phi_p = 1 + x + ... + x^(p-1); finite fields are
built from an irreducible polynomial verified in code; every comparison is an
integer comparison. There is no tolerance anywhere, and no floating point value
is ever formed.

Note on `python3 -O`: `assert` is stripped under -O, so no gate uses `assert`.

Gates (from the brief's table):
  C1  beta(v,v') - beta(v',v) = omega(v,v') for all pairs, exhaustively
  C2  omega(v,v) = 0 for all v (checked, not inferred); omega nondegenerate;
      (C2c) omega kappa-bilinear
  C3  W(v)W(v') = psi(beta(v,v')) W(v+v') exactly in the Schrodinger model
  C4  W(v)W(v') = psi(omega(v,v')) W(v')W(v)
  C5  the q^2 Weyl operators are linearly independent over C
  C6  the commutant of {W(v)} is the scalars
  C7  the isotropic kappa-lines number exactly q+1 (+ polarization validity,
      + the pre-registered subgroup census)
  C8  distinct characters give distinct central characters, while the algebras
      stay abstractly isomorphic
  C9  at p=2 the symmetrized cocycle is unavailable: 2 is not invertible and no
      code path may form omega/2
A0 is an arithmetic self-test layer (ring, field, model), NOT one of the nine.
"""

import sys
import itertools
import numpy as np

QS = (2, 3, 4, 5, 8, 9)

MODES = {
    "green": "no mutation; every gate must pass and the run exits 0",
    "--red-symmetric":
        "replace omega by the symmetric nondegenerate form sigma(v,v')=a a' + b b' "
        "(NOT a b' + a' b, which equals omega at p=2 and would be a no-op); C2 must fire",
    "--red-trivial-char":
        "take zeta = 1, i.e. the trivial additive character; C6 must fire",
    "--red-cocycle":
        "use beta(v,v') = a' b while still claiming beta - beta^T = omega; C1 must fire",
    "--red-nonisotropic":
        "feed a non-isotropic polarization to the model builder; C3 or C7 must fire "
        "(not constructible for q prime - see EXPECTATIONS.md D-f)",
    "--red-dim":
        "assert q^2+1 independent Weyl operators; C5 must fire",
    "--red-halfweyl":
        "EXTRA, not one of the brief's five: use the symmetrized cocycle omega/2; "
        "C9 must fire at p=2. Added because no mode in the brief reaches C9",
}

EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2


class CharTwoError(Exception):
    """Raised when a code path tries to form omega/2 in characteristic 2."""


# --------------------------------------------------------------------------
# A0.1  Exact arithmetic in Z[zeta_p] = Z[x]/Phi_p(x), Phi_p = 1+x+...+x^(p-1)
# --------------------------------------------------------------------------
class CycRing:
    """Integer vectors of length p-1, reduced modulo Phi_p. Exact, no floats."""

    def __init__(self, p):
        self.p = p
        self.deg = p - 1
        self.zero = (0,) * self.deg
        self.one = tuple([1] + [0] * (self.deg - 1))
        self.zeta = self.reduce([0, 1])
        self.zpow = [self.one]
        for _ in range(p):
            self.zpow.append(self.mul(self.zpow[-1], self.zeta))

    def reduce(self, coeffs):
        """Reduce an integer polynomial mod Phi_p: x^(p-1) = -(1+x+...+x^(p-2))."""
        c = list(coeffs)
        for d in range(len(c) - 1, self.deg - 1, -1):
            k = c[d]
            if k:
                c[d] = 0
                for j in range(self.deg):
                    c[d - self.deg + j] -= k
        c = c[:self.deg] + [0] * (self.deg - len(c))
        return tuple(c[:self.deg])

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def mul(self, a, b):
        prod = [0] * (2 * self.deg - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        prod[i + j] += x * y
        return self.reduce(prod)

    def smul(self, k, a):
        return tuple(k * x for x in a)


def poly_mul_int(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_divmod_monic(f, g):
    """Divide integer polys, g monic. Returns (quotient, remainder), exact."""
    f = list(f)
    dg = len(g) - 1
    if len(f) < len(g):
        return [0], f
    quot = [0] * (len(f) - dg)
    for d in range(len(f) - 1, dg - 1, -1):
        c = f[d]
        if c:
            quot[d - dg] = c
            for j in range(len(g)):
                f[d - dg + j] -= c * g[j]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return quot, f


def verify_cyclotomic(p, log):
    """A0.1: (x-1)*Phi_p = x^p - 1, and Phi_p has no proper monic integer factor.

    The second search is exhaustive given the coefficient bound: Phi_p divides
    x^p - 1, so all its complex roots have modulus 1, so a monic degree-d factor
    has coefficients bounded by binomial(d,j) <= 2^d. The reduction from
    rational to integer factors (Gauss) is a mathematical input this checker
    does NOT verify; it is named here rather than hidden. No PASS in the green
    run depends on it: f == 0 mod Phi_p always implies f(zeta) = 0. It is the
    NON-zero tests (rank, and every FAIL report) that need Phi_p minimal.
    """
    phi = [1] * p                                     # 1 + x + ... + x^(p-1)
    prod = poly_mul_int([-1, 1], phi)                 # (x-1)*Phi_p
    target = [0] * p + [1]
    target[0] = -1                                    # x^p - 1
    if prod != target:
        return False, "(x-1)*Phi_p != x^p - 1"
    for d in range(1, (p - 1) // 2 + 1):
        bound = 2 ** d
        for tail in itertools.product(range(-bound, bound + 1), repeat=d):
            g = list(tail) + [1]
            if g[0] == 0:
                continue
            _, rem = poly_divmod_monic(phi, g)
            if rem == [0]:
                return False, "Phi_%d has proper monic factor %s" % (p, g)
    log("A0.1 ring   Phi_%d verified: (x-1)Phi=x^%d-1, no proper monic integer "
        "factor (bounded exhaustive search)" % (p, p))
    return True, ""


def verify_zeta_order(R, log):
    """A0.2: zeta has exact order p in the ring (so zeta^k, k=0..p-1, differ)."""
    if R.zpow[R.p] != R.one:
        return False, "zeta^p != 1"
    for k in range(1, R.p):
        if R.zpow[k] == R.one:
            return False, "zeta^%d == 1: zeta not primitive" % k
    seen = set(R.zpow[:R.p])
    if len(seen) != R.p:
        return False, "zeta powers not distinct"
    log("A0.2 ring   zeta_%d has exact order %d; the %d powers are distinct "
        "vectors in Z[zeta_%d]" % (R.p, R.p, R.p, R.p))
    return True, ""


# --------------------------------------------------------------------------
# A0.3  Finite fields F_q, built here and verified here (no recalled tables)
# --------------------------------------------------------------------------
class GF:
    """F_q = F_p[t]/(f), f monic irreducible of degree n, found by search.

    Elements are integers 0..q-1 read as base-p digit vectors (little-endian).
    """

    def __init__(self, p, n):
        self.p, self.n, self.q = p, n, p ** n
        self.f = self._find_irreducible()
        q = self.q
        self.ADD = np.zeros((q, q), dtype=np.int64)
        self.MUL = np.zeros((q, q), dtype=np.int64)
        for i in range(q):
            di = self.digits(i)
            for j in range(q):
                dj = self.digits(j)
                self.ADD[i, j] = self.undigits([(x + y) % p for x, y in zip(di, dj)])
                self.MUL[i, j] = self.undigits(self._polymul(di, dj))
        self.one = self.undigits([1] + [0] * (n - 1))
        self.NEG = np.array([[j for j in range(q) if self.ADD[i, j] == 0][0]
                             for i in range(q)], dtype=np.int64)
        self.prime_sub = []
        acc = 0
        for _ in range(p):
            self.prime_sub.append(acc)
            acc = int(self.ADD[acc, self.one])
        self.TR = np.array([self._trace(i) for i in range(q)], dtype=np.int64)

    def digits(self, i):
        d, p = [], self.p
        for _ in range(self.n):
            d.append(i % p)
            i //= p
        return d

    def undigits(self, d):
        v, m = 0, 1
        for x in d:
            v += (x % self.p) * m
            m *= self.p
        return v

    def _polymul(self, x, y):
        p, n, f = self.p, self.n, self.f
        prod = [0] * (2 * n - 1)
        for i in range(n):
            for j in range(n):
                prod[i + j] = (prod[i + j] + x[i] * y[j]) % p
        for d in range(2 * n - 2, n - 1, -1):
            c = prod[d]
            if c:
                prod[d] = 0
                for k in range(n):                    # t^n = -(f_0 + ... + f_{n-1} t^{n-1})
                    prod[d - n + k] = (prod[d - n + k] - c * f[k]) % p
        return prod[:n]

    def _find_irreducible(self):
        """Monic degree-n polys over F_p in order; irreducibility by exhaustive
        trial division against every monic poly of degree 1..n//2."""
        p, n = self.p, self.n
        if n == 1:
            return [0, 1]
        for tail in itertools.product(range(p), repeat=n):
            f = list(tail) + [1]
            if self._is_irreducible(f):
                return f
        raise SystemExit("no irreducible polynomial found for p=%d n=%d" % (p, n))

    def _is_irreducible(self, f):
        p, n = self.p, len(f) - 1
        for d in range(1, n // 2 + 1):
            for tail in itertools.product(range(p), repeat=d):
                g = list(tail) + [1]
                if all(c == 0 for c in self._poly_rem(f, g)):
                    return False
        return True

    def _poly_rem(self, f, g):
        p = self.p
        r = [c % p for c in f]
        dg = len(g) - 1
        for d in range(len(r) - 1, dg - 1, -1):
            c = r[d]
            if c:
                for j in range(len(g)):
                    r[d - dg + j] = (r[d - dg + j] - c * g[j]) % p
        return [c % p for c in r[:dg]] or [0]

    def _trace(self, i):
        s, x = 0, i
        for _ in range(self.n):
            s = int(self.ADD[s, x])
            xp = self.one
            for _ in range(self.p):
                xp = int(self.MUL[xp, x])
            x = xp
        for k, e in enumerate(self.prime_sub):
            if e == s:
                return k
        return -1                                      # caught by A0.3


def verify_field(F, log):
    """A0.3: exhaustive field axioms + trace properties, from the tables built."""
    q, p = F.q, F.p
    A, M = F.ADD, F.MUL
    idx = np.arange(q)
    if not (A[0, :] == idx).all() or not (M[F.one, :] == idx).all():
        return False, "0 or 1 is not an identity"
    if F.one == 0:
        return False, "1 == 0"
    if not (A == A.T).all() or not (M == M.T).all():
        return False, "addition or multiplication not commutative"
    J, K = np.meshgrid(idx, idx, indexing="ij")
    for i in range(q):
        if not (A[A[i, J], K] == A[i, A[J, K]]).all():
            return False, "addition not associative"
        if not (M[M[i, J], K] == M[i, M[J, K]]).all():
            return False, "multiplication not associative"
        if not (M[i, A[J, K]] == A[M[i, J], M[i, K]]).all():
            return False, "not distributive"
    for i in range(1, q):
        if not (M[i, :] == F.one).any():
            return False, "element %d has no multiplicative inverse" % i
    if (F.TR < 0).any():
        return False, "trace value outside the prime subfield"
    if not (F.TR[A] == (F.TR[J] + F.TR[K]) % p).all():
        return False, "trace not additive"
    if not (F.TR != 0).any():
        return False, "trace identically zero"
    for c in range(1, q):
        if not any(F.TR[M[c, x]] != 0 for x in range(q)):
            return False, "pairing (c,x) -> Tr(cx) degenerate at c=%d" % c
    log("A0.3 field  F_%d = F_%d[t]/(%s) verified: field axioms exhaustive, "
        "Tr additive onto F_%d, Tr(1)=%d, pairing Tr(cx) nondegenerate"
        % (F.q, F.p, "".join(str(c) for c in F.f), F.p, F.TR[F.one]))
    return True, ""


# --------------------------------------------------------------------------
# V = kappa (+) kappa, the forms, and the halving guard (C9)
# --------------------------------------------------------------------------
class Setting:
    """All mutable-by-mutation data of the construction lives here."""

    def __init__(self, F, R, mode):
        self.F, self.R, self.mode = F, R, mode
        q = F.q
        self.q = q
        self.nV = q * q
        self.half_attempts = 0
        self.half_probe = False
        # V index i <-> (a,b) with i = a*q + b
        self.VA = np.array([i // q for i in range(self.nV)], dtype=np.int64)
        self.VB = np.array([i % q for i in range(self.nV)], dtype=np.int64)
        A, M = F.ADD, F.MUL
        a, b = self.VA[:, None], self.VB[:, None]
        ap, bp = self.VA[None, :], self.VB[None, :]
        self.OMEGA_TRUE = A[M[a, bp], F.NEG[M[ap, b]]]
        self.SIGMA = A[M[a, ap], M[b, bp]]              # symmetric, not alternating
        self.FORM = self.SIGMA if mode == "--red-symmetric" else self.OMEGA_TRUE
        self.VADD = (A[a, ap] * q + A[b, bp])
        self.BETA_STD = M[a, bp]                        # beta(v,v') = a b'
        self.BETA_T = M[ap, b]                          # a' b
        # zeta of the character (mutated by --red-trivial-char)
        self.zroot = R.one if mode == "--red-trivial-char" else R.zeta
        self.zpow = [R.one]
        for _ in range(F.p):
            self.zpow.append(R.mul(self.zpow[-1], self.zroot))
        self.claimed_span_dim = q * q + 1 if mode == "--red-dim" else q * q

    # ---- psi -------------------------------------------------------------
    def psi_exp(self, x):
        """exponent e with psi(x) = zroot^e; exact, no evaluation needed."""
        return int(self.F.TR[x]) % self.F.p

    def psi(self, x):
        return self.zpow[self.psi_exp(x)]

    # ---- the halving guard, C9 ------------------------------------------
    def half(self, y):
        """The unique x with 2x = y. Fires the C9 guard in characteristic 2."""
        if self.F.p == 2:
            if not self.half_probe:
                self.half_attempts += 1
            raise CharTwoError("omega/2 has no value at p=2 (2 is not invertible)")
        two = int(self.F.ADD[self.F.one, self.F.one])
        for x in range(self.F.q):
            if int(self.F.MUL[two, x]) == y:
                return x
        raise CharTwoError("2 not invertible")

    # ---- beta, as declared by the mode ----------------------------------
    def beta(self, i, j):
        if self.mode == "--red-cocycle":
            return int(self.BETA_T[i, j])
        if self.mode == "--red-halfweyl":
            return self.half(int(self.OMEGA_TRUE[i, j]))
        return int(self.BETA_STD[i, j])

    def beta_table(self):
        if self.mode == "--red-cocycle":
            return self.BETA_T
        if self.mode == "--red-halfweyl":
            out = np.zeros_like(self.BETA_STD)
            for i in range(self.nV):
                for j in range(self.nV):
                    out[i, j] = self.half(int(self.OMEGA_TRUE[i, j]))
            return out
        return self.BETA_STD


# --------------------------------------------------------------------------
# Monomial matrices over Z[zeta_p]: exact, O(q) products, no dense fallback
# needed in the hot loops.  A matrix is (perm, exps): entry (perm[x], x) is
# zroot^exps[x], all other entries are 0.
# --------------------------------------------------------------------------
def mono_mul(A, B, p):
    permA, expA = A
    permB, expB = B
    perm = tuple(permA[y] for y in permB)
    exps = tuple((expA[permB[x]] + expB[x]) % p for x in range(len(permB)))
    return (perm, exps)


def mono_eq(A, B, zpow):
    if A[0] != B[0]:
        return False
    return all(zpow[e] == zpow[f] for e, f in zip(A[1], B[1]))


def mono_scale(A, e, p):
    return (A[0], tuple((x + e) % p for x in A[1]))


def mono_dense(A, zpow, R):
    q = len(A[0])
    M = [[R.zero] * q for _ in range(q)]
    for x in range(q):
        M[A[0][x]][x] = zpow[A[1][x]]
    return M


def dense_mul(A, B, R):
    q = len(A)
    C = [[R.zero] * q for _ in range(q)]
    for i in range(q):
        for k in range(q):
            a = A[i][k]
            if a != R.zero:
                for j in range(q):
                    b = B[k][j]
                    if b != R.zero:
                        C[i][j] = R.add(C[i][j], R.mul(a, b))
    return C


def conj(R, a):
    """Complex conjugation on Z[zeta_p]: zeta -> zeta^-1. Exact."""
    out = R.zero
    for k, c in enumerate(a):
        if c:
            out = R.add(out, R.smul(c, R.zpow[(R.p - k) % R.p]))
    return out


class Model:
    """Schrodinger model built from a splitting V = P (+) Q:
         W(u+w) e_y = psi(form(u,y)) e_{y+w},   u in P, w, y in Q.
    For P = kappa e1, Q = kappa e2 this is W(a,b) e_x = psi(ax) e_{x+b} and the
    cocycle is exactly beta(v,v') = a b' (EXPECTATIONS.md D-d)."""

    def __init__(self, S, P, Q):
        self.S, self.P, self.Q = S, P, Q
        self.ok, self.err = True, ""
        q, nV = S.q, S.nV
        self.qidx = {y: k for k, y in enumerate(Q)}
        decomp = {}
        for u in P:
            for w in Q:
                decomp[int(S.VADD[u, w])] = (u, w)
        if len(decomp) != nV:
            self.ok = False
            self.err = "V is not the direct sum of the fed P and Q (%d/%d)" % (
                len(decomp), nV)
            return
        for y in Q:
            for w in Q:
                if int(S.VADD[y, w]) not in self.qidx:
                    self.ok = False
                    self.err = "Q is not closed under addition"
                    return
        self.ops = []
        for v in range(nV):
            u, w = decomp[v]
            perm = [0] * q
            exps = [0] * q
            for k, y in enumerate(Q):
                perm[k] = self.qidx[int(S.VADD[y, w])]
                exps[k] = S.psi_exp(int(S.FORM[u, y]))
            self.ops.append((tuple(perm), tuple(exps)))


def standard_polarization(S):
    """P = kappa e1 = {(a,0)}, Q = kappa e2 = {(0,b)} as V-indices."""
    q = S.q
    return [a * q for a in range(q)], [b for b in range(q)]


def fp_linear_maps(F):
    """All F_p-linear g: kappa -> kappa, as tables, given by basis images."""
    p, n, q = F.p, F.n, F.q
    basis = [p ** k for k in range(n)]                 # digit vectors e_k
    for images in itertools.product(range(q), repeat=n):
        g = [0] * q
        for x in range(q):
            d = F.digits(x)
            acc = 0
            for k in range(n):
                for _ in range(d[k]):
                    acc = int(F.ADD[acc, images[k]])
            g[x] = acc
        yield images, g


def nonisotropic_polarization(S):
    """P = graph of an F_p-linear g with Tr(omega|_P) != 0, keeping Q = kappa e2
    Lagrangian.  Returns (P, Q, description) or (None, None, reason)."""
    F, q = S.F, S.q
    Q = [b for b in range(q)]
    for images, g in fp_linear_maps(F):
        P = [a * q + g[a] for a in range(q)]
        bad = None
        for u in P:
            for u2 in P:
                if int(F.TR[int(S.OMEGA_TRUE[u, u2])]) != 0:
                    bad = (u, u2)
                    break
            if bad:
                break
        if bad:
            return P, Q, "P = graph of the F_p-linear map with basis images %s; " \
                         "Tr(omega(u,u')) != 0 at u=%s u'=%s" % (
                             list(images), divmod(bad[0], q), divmod(bad[1], q))
    return None, None, ("no F_p-linear graph over Q = kappa e2 is non-isotropic; "
                        "for q prime this is a theorem, not a gap (EXPECTATIONS D-f)")


def subspaces_dim(p, m, k):
    """Every k-dim F_p-subspace of F_p^m exactly once, by RREF canonical form."""
    for piv in itertools.combinations(range(m), k):
        free = [(i, j) for i in range(k) for j in range(m)
                if j not in piv and j > piv[i]]
        for vals in itertools.product(range(p), repeat=len(free)):
            R = [[0] * m for _ in range(k)]
            for i in range(k):
                R[i][piv[i]] = 1
            for (pos, val) in zip(free, vals):
                R[pos[0]][pos[1]] = val
            yield R


def subgroup_census(S):
    """All additive subgroups of V of order q, classified by isotropy.
    Returns (total, n_kappa_isotropic, n_psi_isotropic, an example non-isotropic)."""
    F, q = S.F, S.q
    p, n = F.p, F.n
    total = kiso = tiso = 0
    for B in subspaces_dim(p, 2 * n, n):
        elems = []
        for coeffs in itertools.product(range(p), repeat=n):
            vec = [0] * (2 * n)
            for i in range(n):
                if coeffs[i]:
                    for j in range(2 * n):
                        vec[j] = (vec[j] + coeffs[i] * B[i][j]) % p
            a = F.undigits(vec[:n])
            b = F.undigits(vec[n:])
            elems.append(a * q + b)
        total += 1
        ok_k = all(int(S.OMEGA_TRUE[x, y]) == 0 for x in elems for y in elems)
        ok_t = all(int(F.TR[int(S.OMEGA_TRUE[x, y])]) == 0 for x in elems for y in elems)
        kiso += ok_k
        tiso += ok_t
    return total, kiso, tiso


def kappa_lines(S):
    """The kappa-lines of V, each as a sorted tuple of V-indices."""
    F, q = S.F, S.q
    lines = set()
    for v in range(S.nV):
        if v == 0:
            continue
        a, b = divmod(v, q)
        L = tuple(sorted(int(F.MUL[l, a]) * q + int(F.MUL[l, b]) for l in range(q)))
        lines.add(L)
    return sorted(lines)


# --------------------------------------------------------------------------
# Exact rank over Z[zeta_p] (a domain by A0.1), division-free elimination.
# --------------------------------------------------------------------------
def rank_ring(rows, R):
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    ncols = len(rows[0])
    rank = 0
    for c in range(ncols):
        piv = None
        for i in range(rank, len(rows)):
            if rows[i][c] != R.zero:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pv = rows[rank][c]
        for i in range(rank + 1, len(rows)):
            f = rows[i][c]
            if f != R.zero:
                rows[i] = [R.sub(R.mul(pv, rows[i][j]), R.mul(f, rows[rank][j]))
                           for j in range(ncols)]
        rank += 1
        if rank == len(rows):
            break
    return rank


# --------------------------------------------------------------------------
# The gates
# --------------------------------------------------------------------------
EXPECTED_CENSUS = {                 # pre-registered in EXPECTATIONS.md, [S]
    2: (3, 3, 3), 3: (4, 4, 4), 4: (35, 5, 15),
    5: (6, 6, 6), 8: (1395, 9, 135), 9: (130, 10, 40),
}


def gate_C1(S, M):
    """beta(v,v') - beta(v',v) = omega(v,v'), exhaustively over all q^4 pairs."""
    F = S.F
    B = S.beta_table()
    SUB = F.ADD[np.arange(F.q)[:, None], F.NEG[np.arange(F.q)][None, :]]
    diff = SUB[B, B.T]
    bad = np.argwhere(diff != S.FORM)
    if len(bad):
        i, j = int(bad[0][0]), int(bad[0][1])
        return False, ("beta-beta^T != form at v=%s v'=%s: %d vs %d (%d pairs bad)"
                       % (divmod(i, S.q), divmod(j, S.q), int(diff[i, j]),
                          int(S.FORM[i, j]), len(bad)))
    return True, "exhaustive on %d ordered pairs" % (S.nV ** 2)


def gate_C2(S, M):
    """C2a alternating (checked, not inferred), C2b nondegenerate, C2c bilinear."""
    F, q, nV = S.F, S.q, S.nV
    diag = np.array([S.FORM[i, i] for i in range(nV)])
    if (diag != 0).any():
        i = int(np.argwhere(diag != 0)[0][0])
        return False, ("C2a alternating FAILS: form(v,v)=%d != 0 at v=%s "
                       "(%d of %d vectors)" % (int(diag[i]), divmod(i, q),
                                               int((diag != 0).sum()), nV))
    for v in range(1, nV):
        if not (S.FORM[v, :] != 0).any():
            return False, "C2b nondegenerate FAILS: form(v,.)=0 at v=%s" % (divmod(v, q),)
    for k in range(nV):
        col = S.FORM[:, k]
        if not (S.FORM[S.VADD, k] == F.ADD[col[:, None], col[None, :]]).all():
            return False, "C2c bilinear FAILS: not additive in the first argument"
        row = S.FORM[k, :]
        if not (S.FORM[k, S.VADD] == F.ADD[row[:, None], row[None, :]]).all():
            return False, "C2c bilinear FAILS: not additive in the second argument"
    for l in range(q):
        SC = np.array([int(F.MUL[l, i // q]) * q + int(F.MUL[l, i % q])
                       for i in range(nV)])
        if not (S.FORM[SC, :] == F.MUL[l, S.FORM]).all():
            return False, "C2c bilinear FAILS: not kappa-homogeneous at l=%d" % l
    return True, ("alternating on all %d vectors, nondegenerate, kappa-bilinear "
                  "(additivity on %d triples)" % (nV, nV ** 3))


def gate_C3(S, M):
    """W(v)W(v') = psi(beta(v,v')) W(v+v') exactly, all q^4 pairs."""
    p, nV = S.F.p, S.nV
    ops, VADD = M.ops, S.VADD
    B = S.beta_table()
    nbad = 0
    first = None
    for i in range(nV):
        Wi = ops[i]
        for j in range(nV):
            lhs = mono_mul(Wi, ops[j], p)
            rhs = mono_scale(ops[int(VADD[i, j])], S.psi_exp(int(B[i, j])), p)
            if not mono_eq(lhs, rhs, S.zpow):
                nbad += 1
                if first is None:
                    first = (i, j)
    if first:
        return False, ("Weyl relation fails at v=%s v'=%s (%d of %d pairs)"
                       % (divmod(first[0], S.q), divmod(first[1], S.q), nbad, nV ** 2))
    return True, "exact on all %d ordered pairs" % (nV ** 2)


def gate_C4(S, M):
    """W(v)W(v') = psi(omega(v,v')) W(v')W(v), all q^4 pairs."""
    p, nV = S.F.p, S.nV
    ops = M.ops
    nbad, first = 0, None
    for i in range(nV):
        for j in range(nV):
            lhs = mono_mul(ops[i], ops[j], p)
            rhs = mono_scale(mono_mul(ops[j], ops[i], p),
                             S.psi_exp(int(S.FORM[i, j])), p)
            if not mono_eq(lhs, rhs, S.zpow):
                nbad += 1
                if first is None:
                    first = (i, j)
    if first:
        return False, ("commutation fails at v=%s v'=%s (%d of %d pairs)"
                       % (divmod(first[0], S.q), divmod(first[1], S.q), nbad, nV ** 2))
    return True, "exact on all %d ordered pairs" % (nV ** 2)


def gate_C5(S, M):
    """rank of span{W(v)} over C, exactly; compared with the claimed dimension.

    Operators with different permutations have disjoint supports (verified),
    so the rank is the sum of the ranks of the permutation classes."""
    R, q = S.R, S.q
    classes = {}
    for op in M.ops:
        classes.setdefault(op[0], []).append(op[1])
    perms = list(classes)
    for i in range(len(perms)):
        for j in range(i + 1, len(perms)):
            if any(perms[i][x] == perms[j][x] for x in range(q)):
                return False, ("rank premise violated: two permutation classes "
                               "share a support position; no exact rank routine applies")
    total = 0
    for perm, expsl in classes.items():
        rows = [[S.zpow[e] for e in exps] for exps in expsl]
        total += rank_ring(rows, R)
    if total != S.claimed_span_dim:
        return False, ("span of the %d Weyl operators has exact dimension %d, "
                       "claimed %d" % (S.nV, total, S.claimed_span_dim))
    return True, ("%d Weyl operators, exact span dimension %d = claimed"
                  % (S.nV, total))


def gate_C6(S, M):
    """dim of the commutant {X : X W(v) = W(v) X for all v}, exactly.

    Each equation links exactly two unknowns:
        X[x,c] = z^(E[c]-E[x]) X[P[x], P[c]]
    so the solution space is computed by union-find with potentials mod p; a
    component carrying an inconsistent potential is forced to zero."""
    q, p = S.q, S.F.p
    n = q * q
    parent = list(range(n))
    pot = [0] * n
    dead = [False] * n

    def find(a):
        acc = 0
        r = a
        while parent[r] != r:
            acc += pot[r]
            r = parent[r]
        # path compression with accumulated potential
        cur, curpot = a, acc
        while parent[cur] != cur:
            nxt, npot = parent[cur], pot[cur]
            parent[cur], pot[cur] = r, curpot % p
            curpot -= npot
            cur = nxt
        return r, acc % p

    for (perm, exps) in M.ops:
        for x in range(q):
            for c in range(q):
                u = x * q + c
                w = perm[x] * q + perm[c]
                d = (exps[c] - exps[x]) % p          # X[u] = z^d X[w]
                ru, pu = find(u)
                rw, pw = find(w)
                if ru == rw:
                    if S.zpow[(pu - pw - d) % p] != S.zpow[0]:
                        dead[ru] = True
                else:
                    parent[rw] = ru
                    pot[rw] = (pu - d - pw) % p
                    if dead[rw]:
                        dead[ru] = True
                    dead[rw] = False
    dim = 0
    for i in range(n):
        r, _ = find(i)
        if r == i and not dead[i]:
            dim += 1
    if dim != 1:
        return False, ("commutant has exact dimension %d, not 1: the "
                       "representation is not irreducible" % dim)
    return True, "commutant is exactly the scalars (dimension 1)"


def gate_C7(S, M, pol):
    """isotropic kappa-lines = q+1; the fed polarization is a valid isotropic
    splitting; and the pre-registered subgroup census."""
    F, q = S.F, S.q
    FORM = S.FORM.tolist()
    TR = F.TR.tolist()
    lines = kappa_lines(S)
    iso = [L for L in lines if all(FORM[x][y] == 0 for x in L for y in L)]
    if len(iso) != q + 1:
        return False, ("isotropic kappa-lines: %d, expected q+1 = %d (of %d lines)"
                       % (len(iso), q + 1, len(lines)))
    P, Q = pol
    for name, G in (("P", P), ("Q", Q)):
        if len(set(G)) != q:
            return False, "polarization %s does not have q elements" % name
        for x in G:
            for y in G:
                if int(S.VADD[x, y]) not in set(G):
                    return False, "polarization %s is not a subgroup" % name
                if FORM[x][y] != 0:
                    return False, ("polarization %s is not isotropic: form = %d "
                                   "at (%s,%s)" % (name, FORM[x][y],
                                                   divmod(x, q), divmod(y, q)))
                if TR[FORM[x][y]] != 0:
                    return False, "polarization %s is not psi-isotropic" % name
    census = subgroup_census(S)
    if census != EXPECTED_CENSUS[q]:
        return False, ("subgroup census %s != pre-registered %s "
                       "(total, kappa-isotropic, psi-isotropic)"
                       % (census, EXPECTED_CENSUS[q]))
    return True, ("%d isotropic kappa-lines = q+1; polarization is an isotropic "
                  "splitting; census (total,kappa-iso,psi-iso) = %s as pre-registered"
                  % (len(iso), census))


def gate_C8(S, M):
    """distinct characters -> distinct central characters (so inequivalent
    representations), while the twisted algebras stay abstractly isomorphic."""
    F, R, q, p = S.F, S.R, S.q, S.F.p
    notes = []
    # (i) the brief's literal statement, over primitive p-th roots of unity
    prim = list(range(1, p))
    if len(prim) < 2:
        notes.append("zeta-pair test VACUOUS at p=2 (exactly one primitive "
                     "square root of unity)")
    else:
        for k in prim:
            for m in prim:
                if k == m:
                    continue
                wit = None
                for t in range(q):
                    if R.zpow[(k * int(F.TR[t])) % p] != R.zpow[(m * int(F.TR[t])) % p]:
                        wit = t
                        break
                if wit is None:
                    return False, ("zeta^%d and zeta^%d give the same central "
                                   "character" % (k, m))
        notes.append("all %d ordered pairs of distinct primitive zeta separated"
                     % (len(prim) * (len(prim) - 1)))
    # (ii) the kappa^x-torsor of nontrivial additive characters
    tables = {}
    for c in range(q):
        tables[c] = tuple(S.zpow[S.psi_exp(int(F.MUL[c, x]))] for x in range(q))
    triv = tables[0]
    nontrivial = [c for c in range(1, q) if tables[c] != triv]
    if len(nontrivial) != q - 1:
        return False, ("nontrivial additive characters: %d, expected q-1 = %d "
                       "(the kappa^x-torsor has collapsed)" % (len(nontrivial), q - 1))
    if len(set(tables.values())) != q:
        return False, "c -> psi_c is not injective: not a kappa^x-torsor"
    # every additive character of (kappa,+) is some psi_c: count them exactly
    basis = [p ** k for k in range(F.n)]
    allchars = 0
    for expo in itertools.product(range(p), repeat=F.n):
        e = [0] * q
        for x in range(q):
            d = F.digits(x)
            e[x] = sum(d[k] * expo[k] for k in range(F.n)) % p
        if all(e[int(F.ADD[x, y])] == (e[x] + e[y]) % p for x in range(q) for y in range(q)):
            allchars += 1
    if allchars != q:
        return False, "additive characters of (kappa,+) number %d, not q" % allchars
    # (iii) distinct central characters => not unitarily equivalent
    for c in nontrivial:
        wit = [t for t in range(q) if tables[c][t] != triv[t]]
        if not wit:
            return False, "psi_%d agrees with the trivial character everywhere" % c
    # (iv) the algebras are abstractly isomorphic, by an explicit iso
    for c in range(1, q):
        cinv = [x for x in range(q) if int(F.MUL[c, x]) == F.one][0]
        for i in range(S.nV):
            a, b = divmod(i, q)
            for j in range(S.nV):
                a2, b2 = divmod(j, q)
                lhs = S.zpow[S.psi_exp(int(S.BETA_STD[i, j]))]
                ta, tb = int(F.MUL[cinv, a]), b
                ta2, tb2 = int(F.MUL[cinv, a2]), b2
                rhs = tables[c][int(F.MUL[ta, tb2])]
                if lhs != rhs:
                    return False, ("no algebra isomorphism for c=%d: structure "
                                   "constants differ at %s,%s" % (c, (a, b), (a2, b2)))
    return True, ("%d nontrivial additive characters = q-1, simply transitive "
                  "kappa^x action, all %d characters accounted for; W(a,b) -> "
                  "W'(a/c,b) is an algebra isomorphism for every c; %s"
                  % (len(nontrivial), allchars, "; ".join(notes)))


def gate_C9(S, M):
    """at p=2 the symmetrized cocycle is unavailable and no code path formed it."""
    F, q, p = S.F, S.q, S.F.p
    two = int(F.ADD[F.one, F.one])
    inverses = [x for x in range(q) if int(F.MUL[two, x]) == F.one]
    S.half_probe = True
    try:
        val = S.half(F.one)
        probe = "half(1) = %d" % val
        raised = False
    except CharTwoError as exc:
        probe = "half(1) raised: %s" % exc
        raised = True
    S.half_probe = False
    if p == 2:
        if two != 0:
            return False, "1+1 != 0 at p=2"
        if inverses:
            return False, "2 has an inverse %s at p=2" % inverses
        if not raised:
            return False, "the halving guard did not fire at p=2 (%s)" % probe
        if S.half_attempts:
            return False, ("a code path formed omega/2 at p=2: %d attempt(s) "
                           "outside the sanctioned probe" % S.half_attempts)
        return True, ("2 = 0 is not invertible (exhaustive), omega/2 has no value, "
                      "guard armed and untripped by the run (%s)" % probe)
    if len(inverses) != 1:
        return False, "2 has %d inverses at p=%d" % (len(inverses), p)
    if raised:
        return False, "halving raised at odd characteristic: %s" % probe
    for y in range(q):
        if int(F.MUL[two, S.half(y)]) != y:
            return False, "half() is not a right inverse of doubling at y=%d" % y
    if S.half_attempts:
        return False, ("halving attempts counted at odd characteristic: %d"
                       % S.half_attempts)
    return True, ("p=%d odd: 2 is invertible (inverse %d, exhaustive), 2*half(y)=y "
                  "for all y; the p=2 branch is not exercised" % (p, inverses[0]))


# --------------------------------------------------------------------------
# A0.4  Model self-tests: monomiality, dense cross-check, unitarity
# --------------------------------------------------------------------------
def verify_model(S, M, log):
    R, q, p = S.R, S.q, S.F.p
    for k, (perm, exps) in enumerate(M.ops):
        if sorted(perm) != list(range(q)):
            return False, "W(%s) is not monomial: permutation is not a bijection" % (
                divmod(k, q),)
        for e in exps:
            if S.zpow[e] not in S.zpow[:p]:
                return False, "W(%s) has an entry that is not a power of the root" % (
                    divmod(k, q),)
    probe = list(range(min(3, S.nV)))
    for i in probe:
        Di = mono_dense(M.ops[i], S.zpow, R)
        for j in range(S.nV):
            Dj = mono_dense(M.ops[j], S.zpow, R)
            if dense_mul(Di, Dj, R) != mono_dense(mono_mul(M.ops[i], M.ops[j], p),
                                                  S.zpow, R):
                return False, "monomial product disagrees with dense product"
        star = [[conj(R, Di[b][a]) for b in range(q)] for a in range(q)]
        ident = [[R.one if a == b else R.zero for b in range(q)] for a in range(q)]
        if dense_mul(Di, star, R) != ident:
            return False, "W(%s) is not unitary" % (divmod(i, q),)
    log("A0.4 model  all %d operators monomial with root-of-unity entries; "
        "monomial x dense products agree on %d x %d pairs; W W* = I on the probe"
        % (S.nV, len(probe), S.nV))
    return True, ""


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------
def factor_prime_power(q):
    p = 2
    while p * p <= q:
        if q % p == 0:
            break
        p += 1
    else:
        p = q
    n, r = 0, q
    while r % p == 0:
        r //= p
        n += 1
    if r != 1:
        raise SystemExit("q=%d is not a prime power" % q)
    return p, n


def usage():
    print("usage: python3 -O wh_kappa_check.py [MODE]\n")
    print("Pre-registered falsifier for the Weyl-Heisenberg system of Spec kappa,")
    print("kappa = F_q for q in %s. Exact arithmetic in Z[zeta_p]; no tolerances.\n"
          % (list(QS),))
    print("MODES (green exits 0; every red mode must exit non-zero):")
    for name in ("green", "--red-symmetric", "--red-trivial-char", "--red-cocycle",
                 "--red-nonisotropic", "--red-dim", "--red-halfweyl"):
        print("  %-20s %s" % (name, MODES[name]))
    print("\nexit codes: 0 all gates passed | 1 at least one gate fired "
          "| 2 red mode NOT caught (checker defect) or bad usage")


def main(argv):
    mode = "green"
    for a in argv[1:]:
        if a in ("-h", "--help", "help"):
            usage()
            return EXIT_OK
        if a in MODES and a != "green":
            mode = a
        else:
            print("unknown argument %r" % a)
            usage()
            return EXIT_NOT_CAUGHT

    out = []

    def log(s):
        out.append(s)
        print(s)

    log("wh_kappa_check  mode=%s" % mode)
    log("  %s" % MODES[mode])
    log("  exact: Z[zeta_p] as integer vectors mod Phi_p; no tolerance anywhere")
    fired = []       # (q, gate)
    failed = []      # (q, gate, detail) - same thing, green naming
    notes = []

    for q in QS:
        p, n = factor_prime_power(q)
        log("")
        log("== kappa = F_%d  (p=%d, n=%d, |V| = %d) ==" % (q, p, n, q * q))
        R = CycRing(p)
        ok, err = verify_cyclotomic(p, log)
        if not ok:
            log("q=%-2d A0.1 FAIL %s" % (q, err))
            failed.append((q, "A0.1", err))
            continue
        ok, err = verify_zeta_order(R, log)
        if not ok:
            log("q=%-2d A0.2 FAIL %s" % (q, err))
            failed.append((q, "A0.2", err))
            continue
        F = GF(p, n)
        ok, err = verify_field(F, log)
        if not ok:
            log("q=%-2d A0.3 FAIL %s" % (q, err))
            failed.append((q, "A0.3", err))
            continue
        S = Setting(F, R, mode)

        constructible = True
        if mode == "--red-nonisotropic":
            P, Q, desc = nonisotropic_polarization(S)
            if P is None:
                constructible = False
                P, Q = standard_polarization(S)
                log("q=%-2d MUTATION NOT CONSTRUCTIBLE: %s" % (q, desc))
                notes.append((q, desc))
            else:
                log("q=%-2d mutation: %s" % (q, desc))
        else:
            P, Q = standard_polarization(S)

        M = Model(S, P, Q)
        if M.ok:
            ok, err = verify_model(S, M, log)
            if not ok:
                log("q=%-2d A0.4 FAIL %s" % (q, err))
                failed.append((q, "A0.4", err))
        else:
            log("q=%-2d A0.4 model not built: %s" % (q, M.err))

        gates = [("C1", gate_C1), ("C2", gate_C2), ("C3", gate_C3),
                 ("C4", gate_C4), ("C5", gate_C5), ("C6", gate_C6),
                 ("C7", lambda s, m: gate_C7(s, m, (P, Q))),
                 ("C8", gate_C8), ("C9", gate_C9)]
        for name, fn in gates:
            if not M.ok and name in ("C3", "C4", "C5", "C6"):
                detail = "model not built: %s" % M.err
                good = False
            else:
                try:
                    good, detail = fn(S, M)
                except CharTwoError as exc:
                    good, detail = False, ("unevaluable in characteristic 2 "
                                           "(C9 guard): %s" % exc)
                except Exception as exc:                  # noqa: BLE001
                    good, detail = False, "gate raised %s: %s" % (type(exc).__name__, exc)
            log("q=%-2d %s %s %s" % (q, name, "PASS" if good else "FAIL", detail))
            if not good:
                fired.append((q, name))
                failed.append((q, name, detail))

    log("")
    log("---- summary (mode=%s) ----" % mode)
    if mode == "green":
        if failed:
            for q, g, d in failed:
                log("FAIL q=%-2d %s: %s" % (q, g, d))
            log("GREEN RUN FAILED: %d gate failures" % len(failed))
            return EXIT_FIRED
        log("GREEN: every gate passed for q in %s" % (list(QS),))
        return EXIT_OK
    if not fired:
        log("RED MODE NOT CAUGHT: no gate fired anywhere. This is a checker "
            "defect (or a mutation with no effect), not a pass.")
        return EXIT_NOT_CAUGHT
    bygate = {}
    for q, g in fired:
        bygate.setdefault(g, []).append(q)
    for g in sorted(bygate):
        log("KILLED BY %s at q = %s" % (g, bygate[g]))
    if notes:
        for q, d in notes:
            log("NOT CONSTRUCTIBLE at q=%-2d: %s" % (q, d))
    log("RED MODE %s CAUGHT: first gate to fire = %s at q=%d; %d (q,gate) "
        "failures total" % (mode, fired[0][1], fired[0][0], len(fired)))
    return EXIT_FIRED


if __name__ == "__main__":
    sys.exit(main(sys.argv))
