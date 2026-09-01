#!/usr/bin/env python3
"""Pre-registered falsifier for the FCR-2 residue-characteristic-2 increment.

Written in the independent check lane from ``briefs/fcr2-target.md`` and the
explicitly permitted house-style/regression files.  There are no repository
imports.  Every finite ring is an explicit pair of integer addition and
multiplication tables.  Phases are exact: the mixed-characteristic families
use integer coefficient vectors in Z[zeta_8] = Z[x]/(x^4+1), while the
characteristic-two Gauss sums use ordinary integers.  No float or tolerance is
formed anywhere.

The complete |R|^3 admissible-cocycle torsor is exhausted at every seed of
order at most eight.  At GR(4,2), G1--G3 use a fixed 128-member sample (with
beta_0 forced into it); G4 still evaluates epsilon for all 4096 cocycles.
"""

import itertools
import random
import sys

import numpy as np


SEED_NAMES = (
    "F2", "F4", "Z4", "F2[e]/e2", "Z8", "F2[t]/t3",
    "GR(4,2)", "F2[x,y]/(x,y)^2",
)
FROBENIUS = set(SEED_NAMES[:-1])
FIELD_SEEDS = {"F2", "F4"}
THICKENED_FROBENIUS = {"Z4", "F2[e]/e2", "Z8", "F2[t]/t3"}
CHAR2_NAMES = {"F2", "F4", "F2[e]/e2", "F2[t]/t3", "F2[x,y]/(x,y)^2"}

MODES = {
    "green": "unmutated checker",
    "--red-fake-epsilon": "replace one exact Z/4 epsilon value by a different eighth root",
    "--red-collapse": "claim the two Z/4 H_beta classes have collapsed to one",
    "--red-transpose": "transpose beta_0 over Z/4 while retaining beta-beta^T=omega",
    "--red-halfweyl": "claim that doubling is invertible and omega/2 exists over Z/4",
    "--red-profile": "replace the dual-number order-profile fixture by the other profile",
    "--red-field": "replace the F4 40:24 field split by one class of size 64",
    "--red-square": "double Q_beta in the asserted Z/8 square law",
    "--red-model-sign": "use Z(+b)X(a), rather than Z(-b)X(a), over Z/4",
    "--red-frobenius-blind": "claim a generating character at the non-Frobenius probe",
}

TARGET = {
    "--red-fake-epsilon": ("Z4", "G4"),
    "--red-collapse": ("Z4", "G3"),
    "--red-transpose": ("Z4", "G1"),
    "--red-halfweyl": ("Z4", "G7"),
    "--red-profile": ("F2[e]/e2", "G3"),
    "--red-field": ("F4", "G5"),
    "--red-square": ("Z8", "G2"),
    "--red-model-sign": ("Z4", "G6"),
    "--red-frobenius-blind": ("F2[x,y]/(x,y)^2", "G8"),
}

EXIT_GREEN, EXIT_RED_CAUGHT, EXIT_DEFECT = 0, 1, 2


# ---------------------------------------------------------------------------
# Exact Z[zeta_8] = Z[x]/(x^4+1).
# ---------------------------------------------------------------------------
class Zeta8:
    def __init__(self):
        self.zero = (0, 0, 0, 0)
        self.one = (1, 0, 0, 0)
        self.zeta = (0, 1, 0, 0)
        self.zpow = [self.one]
        for _ in range(8):
            self.zpow.append(self.mul(self.zpow[-1], self.zeta))

    @staticmethod
    def add(x, y):
        return tuple(a + b for a, b in zip(x, y))

    @staticmethod
    def neg(x):
        return tuple(-a for a in x)

    @staticmethod
    def mul(x, y):
        raw = [0] * 7
        for i, a in enumerate(x):
            for j, b in enumerate(y):
                raw[i + j] += a * b
        for degree in range(6, 3, -1):
            raw[degree - 4] -= raw[degree]
        return tuple(raw[:4])

    @staticmethod
    def scale(k, x):
        return tuple(k * a for a in x)


Z8C = Zeta8()


def verify_zeta8():
    if Z8C.zpow[8] != Z8C.one:
        return False, "zeta_8^8 != 1"
    if len(set(Z8C.zpow[:8])) != 8:
        return False, "zeta_8 does not have exact order eight"
    if Z8C.mul((1, 0, 0, 0), (1, 0, 0, 0)) != Z8C.one:
        return False, "coefficient-vector multiplication lacks an identity"
    if Z8C.mul((0, 0, 0, 1), Z8C.zeta) != (-1, 0, 0, 0):
        return False, "x^4=-1 reduction failed"
    return True, "Z[zeta_8]=Z[x]/(x^4+1); zeta_8 has exact order 8"


# ---------------------------------------------------------------------------
# Explicit finite rings.
# ---------------------------------------------------------------------------
class FiniteRing:
    def __init__(self, name, coord_mods, mul_coords, reference_param):
        self.name = name
        self.coord_mods = tuple(coord_mods)
        self.phase_order = max(coord_mods)
        self.n = 1
        for modulus in coord_mods:
            self.n *= modulus
        self.elements = tuple(self._coords(i) for i in range(self.n))
        self.index = {x: i for i, x in enumerate(self.elements)}
        self.zero = 0
        self.one = self.index[(1,) + (0,) * (len(coord_mods) - 1)]
        self.reference_param = tuple(reference_param)
        self.ADD = np.zeros((self.n, self.n), dtype=np.int64)
        self.MUL = np.zeros((self.n, self.n), dtype=np.int64)
        for i, x in enumerate(self.elements):
            for j, y in enumerate(self.elements):
                self.ADD[i, j] = self.index[tuple(
                    (x[k] + y[k]) % coord_mods[k] for k in range(len(coord_mods)))]
                self.MUL[i, j] = self.index[tuple(mul_coords(x, y))]
        self.NEG = np.array([
            next(j for j in range(self.n) if self.ADD[i, j] == self.zero)
            for i in range(self.n)
        ], dtype=np.int64)
        self.units = tuple(i for i in range(self.n)
                           if np.any(self.MUL[i, :] == self.one))
        unit_set = set(self.units)
        self.maximal = tuple(i for i in range(self.n) if i not in unit_set)
        self.char_params = tuple(itertools.product(
            *[range(modulus) for modulus in self.coord_mods]))

    def _coords(self, value):
        out = []
        for modulus in self.coord_mods:
            out.append(value % modulus)
            value //= modulus
        return tuple(out)

    def char_table(self, param):
        d = self.phase_order
        return tuple(sum(param[k] * x[k] * (d // self.coord_mods[k])
                         for k in range(len(param))) % d
                     for x in self.elements)

    def scaled_character(self, param, unit):
        base = self.char_table(param)
        return tuple(base[int(self.MUL[unit, x])] for x in range(self.n))

    def ideal_in_kernel(self, char):
        return frozenset(r for r in range(self.n)
                         if all(char[int(self.MUL[r, x])] == 0
                                for x in range(self.n)))

    def additive_order(self, x):
        cur = self.zero
        for k in range(1, self.n + 1):
            cur = int(self.ADD[cur, x])
            if cur == self.zero:
                return k
        raise RuntimeError("additive order did not divide |R|")


def make_rings():
    def f2_mul(x, y):
        return ((x[0] * y[0]) % 2,)

    def f4_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c + b * d) % 2,
                (a * d + b * c + b * d) % 2)

    def dual_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c) % 2, (a * d + b * c) % 2)

    def trunc3_mul(x, y):
        a, b, c = x
        d, e, f = y
        return ((a * d) % 2,
                (a * e + b * d) % 2,
                (a * f + b * e + c * d) % 2)

    def nonfrob_mul(x, y):
        a, b, c = x
        d, e, f = y
        return ((a * d) % 2,
                (a * e + b * d) % 2,
                (a * f + c * d) % 2)

    def gr42_mul(x, y):
        a, b = x
        c, d = y
        return ((a * c - b * d) % 4,
                (a * d + b * c - b * d) % 4)

    def zn_mul(modulus):
        return lambda x, y: ((x[0] * y[0]) % modulus,)

    return {
        "F2": FiniteRing("F2", (2,), f2_mul, (1,)),
        "F4": FiniteRing("F4", (2, 2), f4_mul, (0, 1)),
        "Z4": FiniteRing("Z4", (4,), zn_mul(4), (1,)),
        "F2[e]/e2": FiniteRing("F2[e]/e2", (2, 2), dual_mul, (0, 1)),
        "Z8": FiniteRing("Z8", (8,), zn_mul(8), (1,)),
        "F2[t]/t3": FiniteRing("F2[t]/t3", (2, 2, 2), trunc3_mul, (0, 0, 1)),
        "GR(4,2)": FiniteRing("GR(4,2)", (4, 4), gr42_mul, (0, 1)),
        "F2[x,y]/(x,y)^2": FiniteRing(
            "F2[x,y]/(x,y)^2", (2, 2, 2), nonfrob_mul, (0, 0, 1)),
    }


def verify_ring(R):
    n, A, M = R.n, R.ADD, R.MUL
    idx = np.arange(n, dtype=np.int64)
    if not np.array_equal(A[R.zero, :], idx) or not np.array_equal(M[R.one, :], idx):
        return False, "identity law failed"
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
    maximal = set(R.maximal)
    if R.zero not in maximal or R.one in maximal:
        return False, "nonunits are not a proper candidate maximal ideal"
    if any(int(A[x, y]) not in maximal for x in maximal for y in maximal):
        return False, "nonunits are not additively closed"
    if any(int(M[r, x]) not in maximal for r in range(n) for x in maximal):
        return False, "nonunits are not an ideal"
    return True, "explicit %dx%d tables satisfy the commutative local-ring axioms" % (n, n)


class Setting:
    def __init__(self, ring, mode):
        self.R, self.mode = ring, mode
        n = ring.n
        self.n, self.nV = n, n * n
        self.VA = np.repeat(np.arange(n, dtype=np.int64), n)
        self.VB = np.tile(np.arange(n, dtype=np.int64), n)
        a, b = self.VA[:, None], self.VB[:, None]
        ap, bp = self.VA[None, :], self.VB[None, :]
        self.VADD = ring.ADD[a, ap] * n + ring.ADD[b, bp]
        self.OMEGA = ring.ADD[ring.MUL[a, bp], ring.NEG[ring.MUL[ap, b]]]
        self.BETA0 = ring.MUL[a, bp]
        self._census = None
        self._qcache = {}
        self.char_records = []
        for param in ring.char_params:
            table = ring.char_table(param)
            self.char_records.append({
                "param": param, "table": table,
                "ideal": ring.ideal_in_kernel(table),
            })
        self.nontrivial = [r for r in self.char_records
                           if any(x != 0 for x in r["table"])]
        self.generating = [r for r in self.nontrivial if r["ideal"] == {0}]
        self.reference = ring.char_table(ring.reference_param)

    def beta_table(self, param):
        alpha, gamma, delta = param
        R = self.R
        a, b = self.VA[:, None], self.VB[:, None]
        ap, bp = self.VA[None, :], self.VB[None, :]
        aa = R.MUL[a, ap]
        cross = R.ADD[R.MUL[a, bp], R.MUL[ap, b]]
        bb = R.MUL[b, bp]
        B = R.ADD[R.ADD[self.BETA0, R.MUL[alpha, aa]],
                  R.ADD[R.MUL[gamma, cross], R.MUL[delta, bb]]]
        if self.mode == "--red-transpose" and R.name == "Z4":
            B = B.T.copy()
        return B

    def qdiag(self, param):
        """Q_beta on V, computed directly rather than via an |V|^2 table."""
        if param in self._qcache:
            return self._qcache[param]
        alpha, gamma, delta = param
        R = self.R
        aa = R.MUL[self.VA, self.VA]
        ab = R.MUL[self.VA, self.VB]
        bb = R.MUL[self.VB, self.VB]
        twice_ab = R.ADD[ab, ab]
        Q = R.ADD[R.ADD[ab, R.MUL[alpha, aa]],
                  R.ADD[R.MUL[gamma, twice_ab], R.MUL[delta, bb]]]
        self._qcache[param] = Q
        return Q

    def all_params(self):
        return list(itertools.product(range(self.n), repeat=3))

    def gate_params(self):
        if self.n <= 8:
            return self.all_params()
        rng = random.Random(0xFC220 + self.n)
        chosen = {(0, 0, 0)}
        while len(chosen) < 128:
            chosen.add((rng.randrange(self.n), rng.randrange(self.n), rng.randrange(self.n)))
        return sorted(chosen)


# ---------------------------------------------------------------------------
# Group data and exact equivalence orbits.
# ---------------------------------------------------------------------------
def quotient_orders(S):
    orders = []
    for v in range(S.nV):
        cur = 0
        for k in range(1, 2 * S.n + 1):
            cur = int(S.VADD[cur, v])
            if cur == 0:
                orders.append(k)
                break
        else:
            raise RuntimeError("quotient order was not found")
    return np.array(orders, dtype=np.int64)


def group_invariants(S, Q):
    """Order profile plus section-independent lift-power distributions."""
    R, n, nV = S.R, S.n, S.nV
    ts = np.repeat(np.arange(n, dtype=np.int64), nV)
    vs = np.tile(np.arange(nV, dtype=np.int64), n)
    cur_t = np.zeros(len(ts), dtype=np.int64)
    cur_v = np.zeros(len(ts), dtype=np.int64)
    orders = np.zeros(len(ts), dtype=np.int64)
    for k in range(1, 4 * n + 1):
        # beta(cur_v, v) = k_previous * Q(v) by bilinearity.  Recover the
        # scalar through repeated addition, independently of an off-diagonal
        # cocycle table.
        scalar_q = np.zeros(len(ts), dtype=np.int64)
        for _ in range(k - 1):
            scalar_q = R.ADD[scalar_q, Q[vs]]
        cur_t = R.ADD[R.ADD[cur_t, ts], scalar_q]
        cur_v = S.VADD[cur_v, vs]
        hit = (orders == 0) & (cur_t == R.zero) & (cur_v == 0)
        orders[hit] = k
        if np.all(orders != 0):
            break
    if np.any(orders == 0):
        raise RuntimeError("an H_beta element did not return to the identity")
    profile = tuple((int(k), int(np.sum(orders == k)))
                    for k in sorted(set(orders.tolist())))

    qorders = quotient_orders(S)
    exact, abstract = {}, {}
    for t in range(n):
        for v in range(nV):
            d = int(qorders[v])
            ct, cv = R.zero, 0
            for j in range(d):
                jq = R.zero
                for _ in range(j):
                    jq = int(R.ADD[jq, Q[v]])
                ct = int(R.ADD[R.ADD[ct, t], jq])
                cv = int(S.VADD[cv, v])
            if cv != 0:
                raise RuntimeError("quotient power failed to land in the centre")
            exact[(d, ct)] = exact.get((d, ct), 0) + 1
            key = (d, R.additive_order(ct))
            abstract[key] = abstract.get(key, 0) + 1
    return profile, tuple(sorted(exact.items())), tuple(sorted(abstract.items()))


class DSU:
    def __init__(self, count):
        self.parent = list(range(count))

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parent[y] = x


def additive_linear_maps(R):
    """All GL maps of the elementary-2 additive group, as element tables."""
    k = len(R.coord_mods)
    basis = [R.index[tuple(1 if i == j else 0 for i in range(k))] for j in range(k)]
    maps = []
    for images in itertools.product(range(1, R.n), repeat=k):
        span = {0}
        independent = True
        for image in images:
            if image in span:
                independent = False
                break
            span |= {int(R.ADD[x, image]) for x in tuple(span)}
        if not independent or len(span) != R.n:
            continue
        table = []
        for x in R.elements:
            value = 0
            for i, bit in enumerate(x):
                if bit:
                    value = int(R.ADD[value, images[i]])
            table.append(value)
        maps.append(tuple(table))
    return basis, maps


def pseudoisometry_orbits_char2(S, abstract):
    """Exhaust every F2-linear pseudo-isometry of the R-valued commutator.

    Since [H,H]=Z(H)=R x 0, any abstract group isomorphism induces exactly a
    pair (h,g) with h omega = omega(g.,g.) and h Q = Q' g.  Conversely such a
    pair gives an isomorphism of these exponent-four central extensions.
    This search therefore classifies abstract (all h) and centre-fixed (h=id)
    equivalence without assuming R-linearity of g.
    """
    R, n = S.R, S.n
    rbasis, hmaps = additive_linear_maps(R)
    if not abstract:
        hmaps = [tuple(range(n))]
    wbasis = [x * n for x in rbasis] + [x for x in rbasis]
    dsu = DSU(n * n)
    map_count = 0

    def qvalue(alpha, delta, v):
        a, b = divmod(v, n)
        return int(R.ADD[R.ADD[R.MUL[alpha, R.MUL[a, a]], R.MUL[a, b]],
                         R.MUL[delta, R.MUL[b, b]]])

    for h in hmaps:
        images = []
        span = {0}

        def rec(pos):
            nonlocal map_count, span
            if pos == len(wbasis):
                g = [0] * S.nV
                for v in range(S.nV):
                    a, b = divmod(v, n)
                    bits = R.elements[a] + R.elements[b]
                    value = 0
                    for i, bit in enumerate(bits):
                        if bit:
                            value = int(S.VADD[value, images[i]])
                    g[v] = value
                inv = [0] * S.nV
                for i, value in enumerate(g):
                    inv[value] = i
                pre_e, pre_f = inv[R.one * n], inv[R.one]
                for alpha in range(n):
                    for delta in range(n):
                        a2 = h[qvalue(alpha, delta, pre_e)]
                        d2 = h[qvalue(alpha, delta, pre_f)]
                        dsu.union(alpha * n + delta, a2 * n + d2)
                map_count += 1
                return
            source = wbasis[pos]
            old_span = span
            for candidate in range(1, S.nV):
                if candidate in old_span:
                    continue
                good = True
                for j, image in enumerate(images):
                    want = h[int(S.OMEGA[source, wbasis[j]])]
                    if int(S.OMEGA[candidate, image]) != want:
                        good = False
                        break
                if not good:
                    continue
                images.append(candidate)
                span = old_span | {int(S.VADD[x, candidate]) for x in old_span}
                rec(pos + 1)
                images.pop()
                span = old_span

        rec(0)

    orbits = {}
    for pair in range(n * n):
        orbits.setdefault(dsu.find(pair), []).append(divmod(pair, n))
    return sorted((tuple(sorted(v)) for v in orbits.values()), key=lambda x: x[0]), map_count


def orbit_index(orbits):
    out = {}
    for i, orbit in enumerate(orbits):
        for value in orbit:
            out[value] = i
    return out


def presentation_orbits_zn(S, abstract):
    """Exhaust generator images for H_beta over Z/4 and Z/8.

    With x=(0,e), y=(0,f), z=[x,y], every group has the presentation
    z central, |z|=n, [x,y]=z, and
    x^n=z^(n alpha/2), y^n=z^(n delta/2).  A candidate image pair (X,Y)
    generates exactly when its quotient determinant is a unit.  Requiring
    determinant one fixes the centre pointwise; allowing every unit gives
    abstract equivalence.  Exhausting all quotient image pairs therefore
    computes the four parity-presentation orbits without an Arf fixture.
    """
    R, n = S.R, S.n
    dsu = DSU(4)
    candidate_count = 0
    half_n = n // 2
    choose = {R.zero: 0, R.index[(half_n,)]: 1}
    for target_alpha in range(2):
        for target_delta in range(2):
            target = target_alpha * 2 + target_delta
            Q = S.qdiag((target_alpha, 0, target_delta))
            for v in range(S.nV):
                for w in range(S.nV):
                    determinant = int(S.OMEGA[v, w])
                    if abstract:
                        if determinant not in R.units:
                            continue
                    elif determinant != R.one:
                        continue
                    cx = R.zero
                    cy = R.zero
                    # binom(n,2) Q; repeated addition is deliberately used so
                    # the presentation audit depends only on explicit tables.
                    for _ in range(n * (n - 1) // 2):
                        cx = int(R.ADD[cx, Q[v]])
                        cy = int(R.ADD[cy, Q[w]])
                    if cx not in choose or cy not in choose:
                        raise RuntimeError("generator nth power left {0,n/2}")
                    source = choose[cx] * 2 + choose[cy]
                    dsu.union(target, source)
                    candidate_count += 1
    orbits = {}
    for parity in range(4):
        orbits.setdefault(dsu.find(parity), []).append(divmod(parity, 2))
    return sorted((tuple(sorted(v)) for v in orbits.values()), key=lambda x: x[0]), candidate_count


def compute_census(S):
    if S._census is not None:
        return S._census
    R, n = S.R, S.n
    params = S.all_params() if n <= 8 else S.gate_params()
    sampled = n > 8
    records = {}

    if R.name in CHAR2_NAMES:
        centre_orbits, centre_maps = pseudoisometry_orbits_char2(S, False)
        abstract_orbits, abstract_maps = pseudoisometry_orbits_char2(S, True)
        cidx, aidx = orbit_index(centre_orbits), orbit_index(abstract_orbits)
        inv_cache = {}
        for alpha, gamma, delta in params:
            pair = (alpha, delta)
            if pair not in inv_cache:
                inv_cache[pair] = group_invariants(S, S.qdiag((alpha, 0, delta)))
            records[(alpha, gamma, delta)] = {
                "centre": cidx[pair], "abstract": aidx[pair],
                "invariants": inv_cache[pair],
            }
        centre_sizes = sorted((len(x) * n for x in centre_orbits), reverse=True)
        abstract_sizes = sorted((len(x) * n for x in abstract_orbits), reverse=True)
        method = ("exhaustive F2-linear pseudo-isometries: centre=%d, abstract=%d"
                  % (centre_maps, abstract_maps))
    elif R.name in {"Z4", "Z8"}:
        centre_orbits, centre_maps = presentation_orbits_zn(S, False)
        abstract_orbits, abstract_maps = presentation_orbits_zn(S, True)
        cidx, aidx = orbit_index(centre_orbits), orbit_index(abstract_orbits)
        inv_cache = {}
        for param in params:
            alpha, gamma, delta = param
            parity = (R.elements[alpha][0] % 2, R.elements[delta][0] % 2)
            if parity not in inv_cache:
                inv_cache[parity] = group_invariants(S, S.qdiag(param))
            records[param] = {"centre": cidx[parity], "abstract": aidx[parity],
                              "invariants": inv_cache[parity]}
        population = n ** 3 // 4
        centre_sizes = sorted((len(x) * population for x in centre_orbits), reverse=True)
        abstract_sizes = sorted((len(x) * population for x in abstract_orbits), reverse=True)
        method = ("exhaustive generator-presentation images: centre=%d, abstract=%d"
                  % (centre_maps, abstract_maps))
    else:
        # GR(4,2): the work order explicitly permits deterministic sampling.
        ckeys, akeys = {}, {}
        for param in params:
            inv = group_invariants(S, S.qdiag(param))
            ck = (inv[0], inv[1])
            ak = (inv[0], inv[2])
            ckeys.setdefault(ck, len(ckeys))
            akeys.setdefault(ak, len(akeys))
            records[param] = {"centre": ckeys[ck], "abstract": akeys[ak],
                              "invariants": inv}
        centre_sizes = sorted((sum(1 for r in records.values() if r["centre"] == i)
                               for i in range(len(ckeys))), reverse=True)
        abstract_sizes = sorted((sum(1 for r in records.values() if r["abstract"] == i)
                                 for i in range(len(akeys))), reverse=True)
        method = "128-member deterministic invariant sample (not a complete orbit classification)"

    # Every exact equivalence class must have constant registered invariants.
    for kind in ("centre", "abstract"):
        seen = {}
        which = 1 if kind == "centre" else 2
        for record in records.values():
            sig = (record["invariants"][0], record["invariants"][which])
            seen.setdefault(record[kind], set()).add(sig)
        if any(len(values) != 1 for values in seen.values()):
            raise RuntimeError("%s equivalence orbit split by registered invariants" % kind)

    S._census = {
        "params": params, "sampled": sampled, "records": records,
        "centre_sizes": centre_sizes, "abstract_sizes": abstract_sizes,
        "centre_classes": len(set(r["centre"] for r in records.values())),
        "abstract_classes": len(set(r["abstract"] for r in records.values())),
        "method": method,
    }
    return S._census


# ---------------------------------------------------------------------------
# Gates G1--G8.
# ---------------------------------------------------------------------------
def gate_G1(S):
    R = S.R
    params = S.gate_params()
    for param in params:
        B = S.beta_table(param)
        diff = R.ADD[B, R.NEG[B.T]]
        if not np.array_equal(diff, S.OMEGA):
            bad = np.argwhere(diff != S.OMEGA)[0]
            return False, "beta-beta^T!=omega for %s at (%d,%d)" % (
                param, int(bad[0]), int(bad[1]))
        Q = np.diag(B)
        lhs = R.ADD[R.ADD[Q[S.VADD], R.NEG[Q[:, None]]], R.NEG[Q[None, :]]]
        twoB = R.ADD[B, B]
        rhs = R.ADD[twoB, R.NEG[S.OMEGA]]
        if not np.array_equal(lhs, rhs):
            bad = np.argwhere(lhs != rhs)[0]
            return False, "corrected polarization fails for %s at (%d,%d)" % (
                param, int(bad[0]), int(bad[1]))
    scope = "all" if S.n <= 8 else "deterministic sample"
    return True, "%s %d beta: admission and corrected polarization on %d pairs each" % (
        scope, len(params), S.nV ** 2)


def gate_G2(S):
    R = S.R
    params = S.gate_params()
    ts = np.repeat(np.arange(S.n, dtype=np.int64), S.nV)
    vs = np.tile(np.arange(S.nV, dtype=np.int64), S.n)
    for param in params:
        B = S.beta_table(param)
        actual_t = R.ADD[R.ADD[ts, ts], B[vs, vs]]
        actual_v = S.VADD[vs, vs]
        claimed_q = B[vs, vs]
        if S.mode == "--red-square" and R.name == "Z8":
            claimed_q = R.ADD[claimed_q, claimed_q]
        claimed_t = R.ADD[R.ADD[ts, ts], claimed_q]
        claimed_v = S.VADD[vs, vs]
        if not np.array_equal(actual_t, claimed_t) or not np.array_equal(actual_v, claimed_v):
            bad = int(np.flatnonzero((actual_t != claimed_t) | (actual_v != claimed_v))[0])
            return False, "square law fails for beta=%s at (t,v)=(%d,%d)" % (
                param, int(ts[bad]), int(vs[bad]))
    scope = "all" if S.n <= 8 else "deterministic sample"
    return True, "%s %d beta x %d H-elements: (t,v)^2=(2t+Q(v),2v)" % (
        scope, len(params), S.n ** 3)


def gate_G3(S):
    C = compute_census(S)
    claimed_centre = C["centre_classes"]
    if S.mode == "--red-collapse" and S.R.name == "Z4":
        claimed_centre = 1
    if claimed_centre != C["centre_classes"]:
        return False, "centre-fixed classes=%d, collapsed claim=%d" % (
            C["centre_classes"], claimed_centre)
    if S.mode == "--red-profile" and S.R.name == "F2[e]/e2":
        profiles = sorted({r["invariants"][0] for r in C["records"].values()})
        wrong = ((1, 1), (2, 1), (4, S.n ** 3 - 2))
        if wrong not in profiles:
            return False, "wrong-profile fixture %s; discovered profiles=%s" % (dict(wrong), [dict(x) for x in profiles])
    if sum(C["centre_sizes"]) != len(C["params"]) or sum(C["abstract_sizes"]) != len(C["params"]):
        return False, "class sizes do not sum to the censused beta population"
    qualifier = "SAMPLED SIGNATURE TYPES" if C["sampled"] else "FULL ORBIT CLASSES"
    return True, ("%s: centre-fixed=%d sizes=%s; abstract=%d sizes=%s; %s; "
                  "order/power/centre-quotient invariants constant on every type") % (
        qualifier, C["centre_classes"], C["centre_sizes"],
        C["abstract_classes"], C["abstract_sizes"], C["method"])


def epsilon_exact(S, char, param):
    Q = S.qdiag(param)
    if S.R.name in CHAR2_NAMES:
        total = sum(1 if char[int(q)] == 0 else -1 for q in Q)
        if total % S.n:
            raise RuntimeError("characteristic-two Gauss sum not divisible by |R|")
        return total // S.n
    d = S.R.phase_order
    total = Z8C.zero
    for q in Q:
        total = Z8C.add(total, Z8C.zpow[(8 // d) * char[int(q)]])
    if any(x % S.n for x in total):
        raise RuntimeError("Z[zeta_8] Gauss sum not coefficientwise divisible by |R|")
    return tuple(x // S.n for x in total)


def epsilon_label(value):
    if isinstance(value, int):
        return "%+d" % value
    if value in Z8C.zpow[:8]:
        return "zeta8^%d" % Z8C.zpow[:8].index(value)
    return str(value)


def gate_G4(S):
    if S.R.name not in FROBENIUS:
        return True, "N/A: epsilon requires psi in Gen(R), which is empty"
    C = compute_census(S)
    all_params = S.all_params()
    reference_values = None
    reference_constancy = reference_separates = None
    all_sets = []
    for rec in S.generating:
        char = rec["table"]
        values = {param: epsilon_exact(S, char, param) for param in all_params}
        # Independent histogram route: count Q-values first, then sum phases.
        for param in all_params:
            Q = S.qdiag(param)
            counts = {q: int(np.sum(Q == q)) for q in set(Q.tolist())}
            if S.R.name in CHAR2_NAMES:
                total = sum(count * (1 if char[q] == 0 else -1)
                            for q, count in counts.items())
                other = total // S.n
            else:
                total = Z8C.zero
                for q, count in counts.items():
                    total = Z8C.add(total, Z8C.scale(
                        count, Z8C.zpow[(8 // S.R.phase_order) * char[q]]))
                other = tuple(x // S.n for x in total)
            reported = values[param]
            if (S.mode == "--red-fake-epsilon" and S.R.name == "Z4"
                    and rec["param"] == S.R.reference_param and param == (0, 0, 0)):
                reported = Z8C.zpow[1]
            if reported != other:
                return False, "epsilon direct/histogram mismatch at psi=%s beta=%s: %s vs %s" % (
                    rec["param"], param, epsilon_label(reported), epsilon_label(other))
            if isinstance(other, int):
                if other not in (-1, 1):
                    return False, "epsilon=%d is not in mu_8" % other
            elif other not in Z8C.zpow[:8]:
                return False, "epsilon=%s is not an eighth root" % (other,)
        value_set = sorted({epsilon_label(x) for x in values.values()})
        all_sets.append("%s:%s" % (rec["param"], value_set))
        if rec["param"] == S.R.reference_param:
            reference_values = values

    if reference_values is None:
        return False, "reference generating character was not enumerated"
    class_sets = {}
    for param in C["params"]:
        cls = C["records"][param]["centre"]
        class_sets.setdefault(cls, set()).add(reference_values[param])
    reference_constancy = all(len(x) == 1 for x in class_sets.values())
    singleton_values = [next(iter(x)) for x in class_sets.values() if len(x) == 1]
    reference_separates = (reference_constancy and
                           len(set(singleton_values)) == len(class_sets))
    return True, ("all %d beta x %d generating psi exact; value sets %s; reference "
                  "centre-class constancy=%s, separates=%s%s") % (
        len(all_params), len(S.generating), "; ".join(all_sets),
        reference_constancy, reference_separates,
        " (on G3 sample)" if C["sampled"] else "")


def gate_G5(S):
    if S.R.name not in FIELD_SEEDS:
        return True, "N/A: field regression is registered only at F2 and F4"
    C = compute_census(S)
    q = S.n
    want_sizes = sorted((q * q * (q + 1) // 2, q * q * (q - 1) // 2), reverse=True)
    # q(q+/-1)/2 quadratic forms, with q cocycles per quadratic form.
    got_sizes = sorted(C["centre_sizes"], reverse=True)
    claimed = [q ** 3] if S.mode == "--red-field" and S.R.name == "F4" else want_sizes
    if got_sizes != claimed:
        return False, "field class sizes=%s, claimed=%s (expected=%s)" % (
            got_sizes, claimed, want_sizes)
    rows = {}
    for param, record in C["records"].items():
        alpha, _, delta = param
        Q = S.qdiag(param)
        nzero = int(np.sum(Q == 0))
        eps = epsilon_exact(S, S.reference, param)
        rows.setdefault(record["centre"], set()).add((nzero, eps, record["invariants"][0]))
        # Basis Arf product is only a convenient census label; the zero count
        # and Gauss sum independently cross-check it.
        _arf = int(S.R.MUL[alpha, delta])
    if any(len(x) != 1 for x in rows.values()):
        return False, "field Arf classes are not constant in (zeros,epsilon,profile)"
    expected_zeros = {1, 2 * q - 1}
    if {next(iter(x))[0] for x in rows.values()} != expected_zeros:
        return False, "field Q-zero counts do not equal {1,2q-1}"
    if {next(iter(x))[1] for x in rows.values()} != {-1, 1}:
        return False, "field epsilon set is not {-1,+1}"
    if q == 2 and got_sizes != [6, 2]:
        return False, "F2 regression is not the 6:2 D4/Q8 split"
    return True, ("F%d: cocycle classes=%s = q times form classes [%d,%d]; "
                  "#{Q=0}={1,%d}; epsilon={-1,+1}; profiles=%s") % (
        q, got_sizes, q * (q + 1) // 2, q * (q - 1) // 2,
        2 * q - 1, [dict(next(iter(x))[2]) for x in rows.values()])


def mono_mul(X, Y, phase_order):
    px, ex = X
    py, ey = Y
    return (tuple(px[k] for k in py),
            tuple((ex[py[k]] + ey[k]) % phase_order for k in range(len(py))))


def mono_scale(X, exponent, phase_order):
    return X[0], tuple((x + exponent) % phase_order for x in X[1])


def build_model(S, char, plus_sign=False):
    R, n, d = S.R, S.n, S.R.phase_order
    ops = []
    for v in range(S.nV):
        a, b = int(S.VA[v]), int(S.VB[v])
        perm, exps = [], []
        for y in range(n):
            ya = int(R.ADD[y, a])
            perm.append(ya)
            phase_arg = int(R.MUL[b, ya])
            if not plus_sign:
                phase_arg = int(R.NEG[phase_arg])
            exps.append((8 // d) * char[phase_arg])
        ops.append((tuple(perm), tuple(exps)))
    return ops


def gate_G6(S):
    if S.R.name not in THICKENED_FROBENIUS:
        return True, "N/A: trace-Gram/model gate is registered at the four thickened Frobenius seeds"
    plus = S.mode == "--red-model-sign" and S.R.name == "Z4"
    for rec in S.generating:
        char = rec["table"]
        ops = build_model(S, char, plus_sign=plus)
        for i in range(S.nV):
            for j in range(S.nV):
                lhs = mono_mul(ops[i], ops[j], 8)
                rhs = mono_scale(ops[int(S.VADD[i, j])],
                                 (8 // S.R.phase_order) * char[int(S.BETA0[i, j])], 8)
                if lhs != rhs:
                    return False, "Z(-b)X(a) model relation fails for psi=%s at (%d,%d)" % (
                        rec["param"], i, j)
                gram = Z8C.zero
                if ops[i][0] == ops[j][0]:
                    for y in range(S.n):
                        gram = Z8C.add(gram, Z8C.zpow[
                            (ops[j][1][y] - ops[i][1][y]) % 8])
                want = Z8C.scale(S.n, Z8C.one) if i == j else Z8C.zero
                if gram != want:
                    return False, "trace-Gram entry (%d,%d)=%s, expected %s" % (
                        i, j, gram, want)
    return True, ("beta0 model exact for every %d generating psi; %dx%d trace-Gram is "
                  "|R| I over Z[zeta_8], hence rank |R|^2 and scalar commutant") % (
        len(S.generating), S.nV, S.nV)


def gate_G7(S):
    R = S.R
    two = int(R.ADD[R.one, R.one])
    inverses = [x for x in range(S.n) if int(R.MUL[two, x]) == R.one]
    claimed_inverses = [R.one] if S.mode == "--red-halfweyl" and R.name == "Z4" else inverses
    if claimed_inverses != inverses:
        return False, "half-Weyl claim invents an inverse of 2; exhaustive table gives none"
    if inverses:
        return False, "2 unexpectedly has an inverse"
    anti = []
    for alpha, gamma, delta in S.all_params():
        if (int(R.ADD[alpha, alpha]) == 0 and
                int(R.ADD[delta, delta]) == 0 and
                int(R.ADD[R.ADD[R.one, gamma], gamma]) == 0):
            anti.append((alpha, gamma, delta))
    if anti:
        return False, "Adm(omega) has antisymmetric coefficient triples %s" % anti[:4]
    return True, "2 noninvertible; full %d-member Adm census has no antisymmetric member" % (S.n ** 3)


def gate_G8(S):
    if S.R.name != "F2[x,y]/(x,y)^2":
        return True, "N/A: designated non-Frobenius probe only"
    gen = [rec for rec in S.nontrivial if rec["ideal"] == {0}]
    claimed = 1 if S.mode == "--red-frobenius-blind" else 0
    if len(gen) != claimed:
        sizes = {}
        for rec in S.nontrivial:
            sizes[len(rec["ideal"])] = sizes.get(len(rec["ideal"]), 0) + 1
        return False, "Gen size=%d by exhaustion, claimed=%d; kernel-ideal sizes=%s" % (
            len(gen), claimed, sizes)
    if any(len(rec["ideal"]) <= 1 for rec in S.nontrivial):
        return False, "a nontrivial character lacks a nonzero kernel ideal"
    sizes = {}
    for rec in S.nontrivial:
        sizes[len(rec["ideal"])] = sizes.get(len(rec["ideal"]), 0) + 1
    return True, "all 7 nontrivial characters exhausted; Gen=empty; kernel-ideal sizes=%s" % sizes


GATES = (
    ("G1", gate_G1), ("G2", gate_G2), ("G3", gate_G3), ("G4", gate_G4),
    ("G5", gate_G5), ("G6", gate_G6), ("G7", gate_G7), ("G8", gate_G8),
)


def usage():
    print("usage: python3 fcr2_beta_check.py [MODE]")
    print("green runs G1--G8 at all eight seeds; red modes must exit nonzero")
    for mode, detail in MODES.items():
        print("  %-27s %s" % (mode, detail))


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
    order = list(SEED_NAMES) if mode == "green" else [TARGET[mode][0]]
    failures = []
    print("fcr2_beta_check mode=%s" % mode)
    print("exact arithmetic: explicit ring tables; integers and Z[zeta_8] vectors; no floats/tolerances")
    ok, detail = verify_zeta8()
    print("A0-CYC %s %s" % ("PASS" if ok else "FAIL", detail))
    if not ok:
        failures.append(("global", "A0-CYC", detail))
    for name in order:
        R = rings[name]
        ok, detail = verify_ring(R)
        print("seed=%-24s A0-RING %s %s" % (name, "PASS" if ok else "FAIL", detail))
        if not ok:
            failures.append((name, "A0-RING", detail))
            continue
        S = Setting(R, mode)
        for gate, fn in GATES:
            try:
                ok, detail = fn(S)
            except Exception as exc:  # a raised gate is a checker failure
                ok, detail = False, "raised %s: %s" % (type(exc).__name__, exc)
            print("seed=%-24s %-2s %s %s" % (
                name, gate, "PASS" if ok else "FAIL", detail))
            if not ok:
                failures.append((name, gate, detail))
        if mode != "green" and failures:
            break
    print("---- summary ----")
    if mode == "green":
        if failures:
            for seed, gate, detail in failures:
                print("FAILED %s %s: %s" % (seed, gate, detail))
            print("GREEN RUN FAILED: %d failures" % len(failures))
            return EXIT_RED_CAUGHT
        print("GREEN: G1--G8 passed at every applicable seed; N/A scopes explicit")
        return EXIT_GREEN
    if not failures:
        print("RED MODE NOT CAUGHT: mutation reached no failing gate (checker defect)")
        return EXIT_DEFECT
    seed, gate, detail = failures[0]
    intended = TARGET[mode][1]
    print("KILLED BY %s at %s: %s" % (gate, seed, detail))
    if gate != intended:
        print("FIRST GATE DIFFERS FROM PRE-REGISTRATION: expected %s" % intended)
        return EXIT_DEFECT
    print("RED MODE %s CAUGHT by pre-registered %s" % (mode, gate))
    return EXIT_RED_CAUGHT


if __name__ == "__main__":
    sys.exit(main(sys.argv))
