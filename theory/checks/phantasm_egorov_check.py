#!/usr/bin/env python3
"""Exact falsifier for SP-EGOROV and affine SP-TENSOR naturality.

The repository is located automatically; a detached copy can use
--root /path/to/arithmetic-quantum-mechanics. It imports only the existing exact GF/CycRing
arithmetic API from wh_kappa_check.py.  No floating point value or tolerance
enters a mathematical check; floating point is used only for elapsed timing.
Passing finite checks does not prove or promote either claim.
"""

import argparse
import itertools
from pathlib import Path
import sys
import time


MODES = {
    "sp-enumeration": ("E1", "retain all invertible 2x2 matrices"),
    "semidir-order": ("E2", "replace s+h*t by s+t"),
    "alpha-phase": ("E3", "replace omega(t,g*v) by omega(t,v)"),
    "translation-sign": ("E4", "conjugate by W^s(-t)"),
    "fourier-sign": ("E5", "replace psi(x*y) by psi(-x*y)"),
    "shear-half": ("E6", "omit 1/2 in the quadratic shear phase"),
    "zero-qudit": ("E7", "replace the actual rank-zero Hilbert basis by F3"),
    "f9-character": ("E8", "substitute the absolute-trace character"),
    "tensor-phase": ("E9", "drop the second tensor-factor affine phase"),
}


def locate_root(argv):
    if "--root" in argv:
        i = argv.index("--root")
        if i + 1 >= len(argv):
            raise SystemExit("--root requires a repository path")
        return Path(argv[i + 1]).resolve()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "theory/checks/wh_kappa_check.py").is_file():
            return parent
    raise SystemExit("cannot locate repository; supply --root /path/to/repo")


REPO_ROOT = locate_root(sys.argv)
sys.path.insert(0, str(REPO_ROOT / "theory/checks"))
try:
    from wh_kappa_check import CycRing, GF
except ImportError as exc:
    raise SystemExit("cannot import exact arithmetic from theory/checks: %s" % exc)


class GateFailure(Exception):
    pass


def need(value, detail):
    if not value:
        raise GateFailure(detail)


# ---------------------------------------------------------------------------
# F3 affine geometry.  These routines do not call the operator implementation.
# ---------------------------------------------------------------------------
V3 = tuple(itertools.product(range(3), repeat=2))
I3 = (1, 0, 0, 1)
Z3 = (0, 0)


def vadd3(v, w):
    return ((v[0] + w[0]) % 3, (v[1] + w[1]) % 3)


def vneg3(v):
    return ((-v[0]) % 3, (-v[1]) % 3)


def omega3(v, w):
    return (v[0] * w[1] - w[0] * v[1]) % 3


def det3(g):
    return (g[0] * g[3] - g[1] * g[2]) % 3


def mvec3(g, v):
    return ((g[0] * v[0] + g[1] * v[1]) % 3,
            (g[2] * v[0] + g[3] * v[1]) % 3)


def mmul3(h, g):
    return ((h[0] * g[0] + h[1] * g[2]) % 3,
            (h[0] * g[1] + h[1] * g[3]) % 3,
            (h[2] * g[0] + h[3] * g[2]) % 3,
            (h[2] * g[1] + h[3] * g[3]) % 3)


def minv3(g):
    need(det3(g) == 1, "attempted inverse of a non-symplectic matrix")
    return (g[3] % 3, -g[1] % 3, -g[2] % 3, g[0] % 3)


def enumerate_sp3(invertible=False):
    out = []
    for g in itertools.product(range(3), repeat=4):
        d = det3(g)
        if (d != 0) if invertible else (d == 1):
            out.append(g)
    return tuple(out)


SP3 = enumerate_sp3()
AFF3 = tuple((t, g) for t in V3 for g in SP3)


def aff_apply3(arrow, v):
    t, g = arrow
    return vadd3(mvec3(g, v), t)


def aff_comp3(after, before, wrong=False):
    s, h = after
    t, g = before
    shift = vadd3(s, t if wrong else mvec3(h, t))
    return shift, mmul3(h, g)


def gate_e1(mode):
    group = enumerate_sp3(invertible=(mode == "sp-enumeration"))
    need(len(group) == 24, "symplectic census is %d, expected 24" % len(group))
    checks = 0
    for g in group:
        need(det3(g) == 1, "retained matrix has determinant %d" % det3(g))
        for v in V3:
            for w in V3:
                checks += 1
                need(omega3(mvec3(g, v), mvec3(g, w)) == omega3(v, w),
                     "matrix %s does not preserve omega at %s,%s" % (g, v, w))
    need(len({(t, g) for t in V3 for g in group}) == 216,
         "affine census is not 216")
    return checks, "24 symplectic matrices, 216 affine arrows; %d form checks" % checks


def gate_e2(mode):
    arrows = AFF3
    aset = set(arrows)
    identity = (Z3, I3)
    checks = 0
    for arrow in arrows:
        need(aff_comp3(identity, arrow) == arrow and
             aff_comp3(arrow, identity) == arrow, "affine identity law failed")
        t, g = arrow
        gi = minv3(g)
        candidate = (vneg3(mvec3(gi, t)), gi)
        matches = [other for other in arrows
                   if aff_comp3(other, arrow) == identity and
                   aff_comp3(arrow, other) == identity]
        need(matches == [candidate], "inverse search disagrees for %s" % (arrow,))
        checks += 3
    wrong = mode == "semidir-order"
    for after in arrows:
        for before in arrows:
            composite = aff_comp3(after, before, wrong=wrong)
            need(composite in aset, "semidirect formula is not closed")
            for v in V3:
                checks += 1
                expected = aff_apply3(after, aff_apply3(before, v))
                need(aff_apply3(composite, v) == expected,
                     "composition mismatch at %s o %s on %s" %
                     (after, before, v))
    return checks, "216 inverses; 46,656 products and 419,904 point checks"


# ---------------------------------------------------------------------------
# Abstract half-form Weyl terms zeta^e W(v), kept separate from matrices.
# ---------------------------------------------------------------------------
def term_mul3(left, right):
    e, v = left
    f, w = right
    return ((e + f + 2 * omega3(v, w)) % 3, vadd3(v, w))


def term_star3(term):
    e, v = term
    return (-e % 3, vneg3(v))


def alpha3(arrow, term, wrong=False):
    e, v = term
    t, g = arrow
    gv = mvec3(g, v)
    phase = omega3(t, v if wrong else gv)
    return ((e + phase) % 3, gv)


def gate_e3(mode):
    wrong = mode == "alpha-phase"
    identity = (Z3, I3)
    checks = 0
    for v in V3:
        checks += 1
        need(alpha3(identity, (0, v), wrong) == (0, v),
             "alpha identity failed at %s" % (v,))
    for arrow in AFF3:
        for v in V3:
            checks += 1
            lhs = alpha3(arrow, term_star3((0, v)), wrong)
            rhs = term_star3(alpha3(arrow, (0, v), wrong))
            need(lhs == rhs, "alpha does not preserve star at %s,%s" % (arrow, v))
        for v in V3:
            for w in V3:
                checks += 1
                lhs = alpha3(arrow, term_mul3((0, v), (0, w)), wrong)
                rhs = term_mul3(alpha3(arrow, (0, v), wrong),
                                alpha3(arrow, (0, w), wrong))
                need(lhs == rhs, "alpha does not preserve product at %s,%s,%s" %
                     (arrow, v, w))
    for after in AFF3:
        for before in AFF3:
            composite = aff_comp3(after, before)
            for v in V3:
                checks += 1
                lhs = alpha3(composite, (0, v), wrong)
                rhs = alpha3(after, alpha3(before, (0, v), wrong), wrong)
                need(lhs == rhs, "alpha composition mismatch at %s o %s on %s" %
                     (after, before, v))
    return checks, ("9 identity, 1,944 star, 17,496 product and "
                    "419,904 composition cases")


# ---------------------------------------------------------------------------
# Independent operator layer: monomial matrices and dense Z[zeta_p] matrices.
# A monomial maps e_y to zeta^exp[y] e_perm[y].
# ---------------------------------------------------------------------------
def mono_mul(left, right, p):
    lp, le = left
    rp, re = right
    return (tuple(lp[rp[y]] for y in range(len(rp))),
            tuple((re[y] + le[rp[y]]) % p for y in range(len(rp))))


def mono_dag(op, p):
    perm, exps = op
    inv = [0] * len(perm)
    for y, z in enumerate(perm):
        inv[z] = y
    return tuple(inv), tuple(-exps[inv[z]] % p for z in range(len(perm)))


def mono_scale(op, exponent, p):
    return op[0], tuple((e + exponent) % p for e in op[1])


def field_half(F, x):
    two = int(F.ADD[F.one, F.one])
    candidates = [y for y in range(F.q) if int(F.MUL[two, y]) == x]
    need(len(candidates) == 1, "2 is not uniquely invertible")
    return candidates[0]


def fadd(F, x, y):
    return int(F.ADD[x, y])


def fmul(F, x, y):
    return int(F.MUL[x, y])


def fneg(F, x):
    return int(F.NEG[x])


def fvadd(F, v, w):
    return fadd(F, v[0], w[0]), fadd(F, v[1], w[1])


def fvneg(F, v):
    return fneg(F, v[0]), fneg(F, v[1])


def fomega(F, v, w):
    return fadd(F, fmul(F, v[0], w[1]), fneg(F, fmul(F, w[0], v[1])))


def weyl_mono(F, char_exp, v):
    a, b = v
    half_ab = field_half(F, fmul(F, a, b))
    perm, exps = [], []
    for y in range(F.q):
        out = fadd(F, y, a)
        phase = fadd(F, fneg(F, fmul(F, b, out)), half_ab)
        perm.append(out)
        exps.append(char_exp(phase))
    return tuple(perm), tuple(exps)


def tensor_mono(left, right, p):
    lp, le = left
    rp, re = right
    nr = len(rp)
    perm, exps = [], []
    for x in range(len(lp)):
        for y in range(nr):
            perm.append(lp[x] * nr + rp[y])
            exps.append((le[x] + re[y]) % p)
    return tuple(perm), tuple(exps)


def rconj(R, value):
    out = R.zero
    for k, coeff in enumerate(value):
        if coeff:
            out = R.add(out, R.smul(coeff, R.zpow[(-k) % R.p]))
    return out


def dense_mul(R, left, right):
    n = len(left)
    out = [[R.zero for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if left[i][k] == R.zero:
                continue
            for j in range(n):
                if right[k][j] != R.zero:
                    out[i][j] = R.add(out[i][j], R.mul(left[i][k], right[k][j]))
    return out


def dense_dag(R, matrix):
    n = len(matrix)
    return [[rconj(R, matrix[j][i]) for j in range(n)] for i in range(n)]


def dense_from_mono(R, op):
    perm, exps = op
    n = len(perm)
    out = [[R.zero for _ in range(n)] for _ in range(n)]
    for y in range(n):
        out[perm[y]][y] = R.zpow[exps[y] % R.p]
    return out


def dense_int_scale(R, integer, matrix):
    return [[R.smul(integer, value) for value in row] for row in matrix]


def dense_identity(R, n, scalar=1):
    return [[R.smul(scalar, R.one) if i == j else R.zero
             for j in range(n)] for i in range(n)]


def fourier_matrix(F, R, char_exp, reverse=False):
    out = []
    for x in range(F.q):
        row = []
        for y in range(F.q):
            xy = fmul(F, x, y)
            if reverse:
                xy = fneg(F, xy)
            row.append(R.zpow[char_exp(xy)])
        out.append(row)
    return out


def check_fourier_covariance(F, R, char_exp, labels, reverse=False):
    fourier = fourier_matrix(F, R, char_exp, reverse=reverse)
    adjoint = dense_dag(R, fourier)
    need(dense_mul(R, adjoint, fourier) == dense_identity(R, F.q, F.q),
         "unnormalized Fourier Gram is not qI")
    for v in labels:
        a, b = v
        lhs = dense_mul(R, fourier,
                        dense_mul(R, dense_from_mono(R, weyl_mono(F, char_exp, v)),
                                  adjoint))
        target = (b, fneg(F, a))
        rhs = dense_int_scale(R, F.q,
                              dense_from_mono(R, weyl_mono(F, char_exp, target)))
        need(lhs == rhs, "Fourier covariance failed at %s" % (v,))


def shear_mono(F, char_exp, r, omit_half=False):
    exps = []
    for x in range(F.q):
        square = fmul(F, x, x)
        value = fmul(F, r, square)
        if not omit_half:
            value = field_half(F, value)
        exps.append(char_exp(fneg(F, value)))
    return tuple(range(F.q)), tuple(exps)


def gate_e4(mode):
    F = GF(3, 1)
    char = lambda x: int(F.TR[x]) % 3
    labels = tuple(itertools.product(range(3), repeat=2))
    checks = 0
    for t in labels:
        used = fvneg(F, t) if mode == "translation-sign" else t
        unitary = weyl_mono(F, char, used)
        adjoint = mono_dag(unitary, 3)
        for v in labels:
            lhs = mono_mul(unitary, mono_mul(weyl_mono(F, char, v), adjoint, 3), 3)
            rhs = mono_scale(weyl_mono(F, char, v), char(fomega(F, t, v)), 3)
            checks += 1
            need(lhs == rhs, "translation covariance failed at t=%s,v=%s" % (t, v))
    return checks, "81 independent monomial conjugation equalities"


def gate_e5(mode):
    F, R = GF(3, 1), CycRing(3)
    need(len(set(R.zpow[:3])) == 3 and R.zpow[3] == R.one,
         "cyclotomic root does not have exact order three")
    char = lambda x: int(F.TR[x]) % 3
    labels = tuple(itertools.product(range(3), repeat=2))
    check_fourier_covariance(F, R, char, labels, reverse=(mode == "fourier-sign"))
    return 10, "F*F=3I and 9 exact Fourier covariance equalities"


def check_shears(F, char, labels, rs, omit_half=False):
    checks = 0
    for r in rs:
        unitary = shear_mono(F, char, r, omit_half=omit_half)
        adjoint = mono_dag(unitary, F.p)
        ident = (tuple(range(F.q)), (0,) * F.q)
        need(mono_mul(unitary, adjoint, F.p) == ident,
             "quadratic phase is not unitary")
        for a, b in labels:
            lhs = mono_mul(unitary,
                           mono_mul(weyl_mono(F, char, (a, b)), adjoint, F.p),
                           F.p)
            target = (a, fadd(F, b, fmul(F, r, a)))
            need(lhs == weyl_mono(F, char, target),
                 "shear covariance failed at r=%s,v=%s" % (r, (a, b)))
            checks += 1
    return checks


def gate_e6(mode):
    F = GF(3, 1)
    char = lambda x: int(F.TR[x]) % 3
    labels = tuple(itertools.product(range(3), repeat=2))
    checks = check_shears(F, char, labels, (1, 2), omit_half=(mode == "shear-half"))
    return checks + 2, "2 unitary and 18 exact shear covariance checks"


def gate_e7(mode):
    points = tuple(itertools.product(range(3), repeat=0))
    linear_maps = tuple(itertools.product(range(3), repeat=0))
    arrows = tuple((t, g) for t in points for g in linear_maps)
    need(len(points) == 1, "zero symplectic space does not have one point")
    need(len(linear_maps) == 1, "zero space does not have one linear symmetry")
    need(len(arrows) == 1, "zero space does not have one affine arrow")
    def zero_apply(arrow, point):
        t, g = arrow
        need(len(t) == len(g) == len(point) == 0, "ill-typed zero affine action")
        return tuple(g[i] + point[i] + t[i] for i in range(len(point)))

    def zero_comp(after, before):
        need(after in arrows and before in arrows, "unknown rank-zero arrow")
        return (tuple(), tuple())

    zero_arrow = arrows[0]
    need(zero_apply(zero_arrow, points[0]) == points[0],
         "rank-zero affine action failed")
    need(zero_comp(zero_arrow, zero_arrow) == zero_arrow,
         "rank-zero affine identity/composition failed")
    inverses = [candidate for candidate in arrows
                if zero_comp(candidate, zero_arrow) == zero_arrow and
                zero_comp(zero_arrow, candidate) == zero_arrow]
    need(inverses == [zero_arrow], "rank-zero affine inverse is not unique")

    hilbert_basis = tuple(itertools.product(range(3), repeat=1 if mode == "zero-qudit" else 0))
    zero_op = (tuple(range(len(hilbert_basis))), (0,) * len(hilbert_basis))
    need(len(hilbert_basis) == 1 and len(zero_op[0]) == 1,
         "rank-zero Weyl model is not one-dimensional")
    need(mono_mul(zero_op, zero_op, 3) == zero_op,
         "rank-zero Weyl action failed")
    F = GF(3, 1)
    char = lambda x: int(F.TR[x]) % 3
    for v in V3:
        op = weyl_mono(F, char, v)
        need(tensor_mono(zero_op, op, 3) == op, "left tensor unit failed")
        need(tensor_mono(op, zero_op, 3) == op, "right tensor unit failed")
    return 26, "enumerated rank-zero affine/Weyl object and both tensor units"


def gate_e8(mode):
    F, R = GF(3, 2), CycRing(3)
    need(F.f == [1, 0, 1], "F9 builder polynomial changed from u^2+1")
    u = 3
    canonical = lambda x: int(F.TR[fmul(F, u, x)]) % 3
    standard = lambda x: int(F.TR[x]) % 3
    char = standard if mode == "f9-character" else canonical
    expected = (0, 0, 0, 1, 1, 1, 2, 2, 2)
    standard_expected = (0, 2, 1, 0, 2, 1, 0, 2, 1)
    table = tuple(char(x) for x in range(9))
    need(table == expected, "F9 character table %s != %s" % (table, expected))
    need(tuple(standard(x) for x in range(9)) == standard_expected,
         "F9 absolute-trace control table changed")
    need(table != standard_expected and set(table) == {0, 1, 2},
         "nonstandard F9 character collapsed")
    checks = 4
    for x in range(9):
        for y in range(9):
            checks += 1
            need(char(fadd(F, x, y)) == (char(x) + char(y)) % 3,
                 "F9 character is not additive")
    labels = tuple(itertools.product(range(9), repeat=2))
    ops = {v: weyl_mono(F, char, v) for v in labels}
    for v in labels:
        for w in labels:
            lhs = mono_mul(ops[v], ops[w], 3)
            exponent = char(field_half(F, fomega(F, v, w)))
            rhs = mono_scale(ops[fvadd(F, v, w)], exponent, 3)
            checks += 1
            need(lhs == rhs, "F9 Weyl product failed at %s,%s" % (v, w))
    for t in labels:
        unitary = ops[t]
        adjoint = mono_dag(unitary, 3)
        for v in labels:
            lhs = mono_mul(unitary, mono_mul(ops[v], adjoint, 3), 3)
            rhs = mono_scale(ops[v], char(fomega(F, t, v)), 3)
            checks += 1
            need(lhs == rhs, "F9 translation covariance failed")
    check_fourier_covariance(F, R, char, labels)
    checks += 82
    checks += check_shears(F, char, labels, (F.one, u)) + 2
    return checks, ("psi_u table, 81 additivity, 6,561 Weyl products, 6,561 "
                    "translations, 81 Fourier and 162 shear covariances")


# ---------------------------------------------------------------------------
# Rank-two D1703 operator and affine naturality, independent implementations.
# ---------------------------------------------------------------------------
def rank2_weyl3(v):
    a1, a2, b1, b2 = v
    perm, exps = [], []
    for x1 in range(3):
        for x2 in range(3):
            y1, y2 = (x1 + a1) % 3, (x2 + a2) % 3
            perm.append(3 * y1 + y2)
            phase = (-b1 * y1 - b2 * y2 + 2 * (a1 * b1 + a2 * b2)) % 3
            exps.append(phase)
    return tuple(perm), tuple(exps)


def gate_e9(mode):
    F = GF(3, 1)
    char = lambda x: int(F.TR[x]) % 3
    rank1 = {v: weyl_mono(F, char, v) for v in V3}
    checks = 0
    for v1 in V3:
        for v2 in V3:
            v = (v1[0], v2[0], v1[1], v2[1])
            need(rank2_weyl3(v) == tensor_mono(rank1[v1], rank1[v2], 3),
                 "rank-two operator/tensor mismatch at %s,%s" % (v1, v2))
            checks += 1
    swap = (tuple(3 * (i % 3) + i // 3 for i in range(9)), (0,) * 9)
    swap_dag = mono_dag(swap, 3)
    for v1 in V3:
        for v2 in V3:
            original = rank2_weyl3((v1[0], v2[0], v1[1], v2[1]))
            target = rank2_weyl3((v2[0], v1[0], v2[1], v1[1]))
            need(mono_mul(swap, mono_mul(original, swap_dag, 3), 3) == target,
                 "rank-two symmetry mismatch")
            checks += 1

    # Factor tables use alpha3.  The direct-sum side below expands the
    # four-coordinate block form inline and does not call alpha3/omega3.
    alpha_table = {}
    for ai, arrow in enumerate(AFF3):
        alpha_table[ai] = tuple(alpha3(arrow, (0, v)) for v in V3)
    drop_second = mode == "tensor-phase"
    for i, arrow1 in enumerate(AFF3):
        t1, g1 = arrow1
        for j, arrow2 in enumerate(AFF3):
            t2, g2 = arrow2
            for vi, v1 in enumerate(V3):
                x1 = ((g1[0] * v1[0] + g1[1] * v1[1]) % 3,
                      (g1[2] * v1[0] + g1[3] * v1[1]) % 3)
                direct1 = (t1[0] * x1[1] - x1[0] * t1[1]) % 3
                e1, out1 = alpha_table[i][vi]
                for wi, v2 in enumerate(V3):
                    x2 = ((g2[0] * v2[0] + g2[1] * v2[1]) % 3,
                          (g2[2] * v2[0] + g2[3] * v2[1]) % 3)
                    direct2 = (t2[0] * x2[1] - x2[0] * t2[1]) % 3
                    e2, out2 = alpha_table[j][wi]
                    left = ((direct1 + direct2) % 3,
                            (x1[0], x2[0], x1[1], x2[1]))
                    right = ((e1 + (0 if drop_second else e2)) % 3,
                             (out1[0], out2[0], out1[1], out2[1]))
                    checks += 1
                    need(left == right, "rank-two affine naturality failed")
    return checks, ("81 operator tensors, 81 swaps and 3,779,136 all-factor "
                    "affine naturality cases")


GATES = (("E1", gate_e1), ("E2", gate_e2), ("E3", gate_e3),
         ("E4", gate_e4), ("E5", gate_e5), ("E6", gate_e6),
         ("E7", gate_e7), ("E8", gate_e8), ("E9", gate_e9))


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="repository root (needed for a detached lane copy)")
    red = parser.add_mutually_exclusive_group()
    for name, (gate, description) in MODES.items():
        red.add_argument("--red-" + name, dest="mode", action="store_const", const=name,
                         help="%s: %s; must exit nonzero at %s" % (gate, description, gate))
    parser.set_defaults(mode=None)
    return parser.parse_args(argv[1:])


def main(argv):
    args = parse_args(argv)
    mode = args.mode
    label = "green" if mode is None else "--red-" + mode
    intended = None if mode is None else MODES[mode][0]
    started = time.perf_counter()
    print("phantasm_egorov_check mode=%s" % label)
    print("exact arithmetic only; finite success does not prove or promote a claim")
    try:
        for gate, fn in GATES:
            tick = time.perf_counter()
            count, detail = fn(mode)
            print("%s PASS: %s [%d checks; %.3fs]" %
                  (gate, detail, count, time.perf_counter() - tick))
    except GateFailure as exc:
        elapsed = time.perf_counter() - started
        print("%s FAIL: %s [%.3fs total]" % (gate, exc, elapsed))
        if mode is None:
            return 1
        if gate != intended:
            print("WRONG GATE: %s intended, %s fired" % (intended, gate))
            return 2
        print("RED MODE %s CAUGHT AT INTENDED GATE %s" % (label, gate))
        return 1
    elapsed = time.perf_counter() - started
    if mode is not None:
        print("RED MODE %s NOT CAUGHT (intended %s)" % (label, intended))
        # The session-close runner rejects a red that exits zero.
        return 0
    print("PASS: SP-EGOROV / affine SP-TENSOR finite falsifier [%.3fs total]" % elapsed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
