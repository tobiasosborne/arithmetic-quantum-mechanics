#!/usr/bin/env python3
"""Exact F3 stabilizer/relation falsifier, with limited F5 controls.

Passing finite checks does not prove SP-STAB-REL.  No floating-point value,
tolerance, normalized branch, CP map, or Choi operator occurs here.
"""

import argparse
from functools import lru_cache
import itertools
from pathlib import Path
import sys


MUTATIONS = {
    "weyl-sign": ("S1", "replace the D1703 negative momentum sign by positive"),
    "fourier-sign": ("S1", "reverse the Fourier kernel but retain its target label"),
    "drop-shear": ("S1", "omit the shear from actual Clifford generators"),
    "phase-only": ("S2", "quotient nonzero maps only by roots of unity"),
    "zero-collapse": ("S2", "identify zero with a nonzero projective class"),
    "average-sign": ("S3", "reverse the affine character in the group average"),
    "origin-dependent": ("S3", "add a coordinate-dot origin character"),
    "fixed-seed": ("S3", "use only the first projector column"),
    "empty-nonzero": ("S3", "send the empty relation to a nonzero matrix"),
    "projector-entry": ("S3", "change one rank-certificate projector entry"),
    "family-state-loss": ("S3", "delete one actual qutrit state ray"),
    "f5-state-loss": ("S3", "delete one actual F5 state ray"),
    "product-order": ("S4", "multiply images in source order"),
    "dagger-transpose": ("S4", "transpose without cyclotomic conjugation"),
    "zero-product": ("S4", "turn a zero product of nonempty maps into nonzero"),
    "tensor-order": ("S5", "reverse the Kronecker factor order"),
    "cup-singleton": ("S5", "replace the Bell cup by one basis vector"),
    "f5-cap-weight": ("S5", "change one F5 Bell-cap coefficient"),
}


class GateFailure(Exception):
    def __init__(self, gate, detail):
        super().__init__(detail)
        self.gate, self.detail = gate, detail


def need(gate, value, detail):
    if not value:
        raise GateFailure(gate, detail)


def locate_root(argv):
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--root")
    args, _ = pre.parse_known_args(argv[1:])
    if args.root:
        return Path(args.root).resolve()
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "theory/checks/wh_kappa_check.py").is_file():
            return parent
    raise SystemExit("cannot locate repository; supply --root /path/to/repo")


ROOT = locate_root(sys.argv)
sys.path.insert(0, str(ROOT / "theory/checks"))
sys.path.insert(1, str(ROOT / "theory/lanes/phantasm-relations/checker"))
try:
    from wh_kappa_check import CycRing
    from phantasm_relations_check import (
        Rel, affine_arrows, affine_data, catalog, compose, dagger, empty,
        graph, identity, omega, plane, span_n, tensor, vectors, zero,
    )
except ImportError as exc:
    raise SystemExit("cannot import exact checker APIs: %s" % exc)


@lru_cache(None)
def ring(p):
    return CycRing(p)


def rconj(r, value):
    out = r.zero
    for k, coeff in enumerate(value):
        if coeff:
            out = r.add(out, r.smul(coeff, r.zpow[(-k) % r.p]))
    return out


def mshape(a):
    return len(a), len(a[0]) if a else 0


def mzero(r, rows, cols):
    return tuple(tuple(r.zero for _ in range(cols)) for _ in range(rows))


def midentity(r, n):
    return tuple(tuple(r.one if i == j else r.zero for j in range(n))
                 for i in range(n))


def madd(r, a, b):
    return tuple(tuple(r.add(x, y) for x, y in zip(arow, brow))
                 for arow, brow in zip(a, b))


def mscale(r, scalar, a):
    return tuple(tuple(r.mul(scalar, x) for x in row) for row in a)


def mintscale(r, integer, a):
    return tuple(tuple(r.smul(integer, x) for x in row) for row in a)


def mmul(r, a, b):
    ra, ka = mshape(a)
    kb, cb = mshape(b)
    if ka != kb:
        raise ValueError("matrix product shape mismatch %s x %s" % (mshape(a), mshape(b)))
    out = [[r.zero for _ in range(cb)] for _ in range(ra)]
    for i in range(ra):
        for k in range(ka):
            if a[i][k] == r.zero:
                continue
            for j in range(cb):
                if b[k][j] != r.zero:
                    out[i][j] = r.add(out[i][j], r.mul(a[i][k], b[k][j]))
    return tuple(tuple(row) for row in out)


def mdag(r, a, transpose_only=False):
    rows, cols = mshape(a)
    return tuple(tuple(a[j][i] if transpose_only else rconj(r, a[j][i])
                       for j in range(rows)) for i in range(cols))


def mkron(r, a, b):
    ra, ca = mshape(a)
    rb, cb = mshape(b)
    return tuple(tuple(r.mul(a[i // rb][j // cb], b[i % rb][j % cb])
                       for j in range(ca * cb)) for i in range(ra * rb))


def mvec(r, a, v):
    return tuple(sum_ring(r, (r.mul(x, y) for x, y in zip(row, v))) for row in a)


def sum_ring(r, values):
    out = r.zero
    for value in values:
        out = r.add(out, value)
    return out


def is_zero(r, a):
    return all(x == r.zero for row in a for x in row)


def bump_entry(r, matrix, row=0, col=0):
    out = [list(values) for values in matrix]
    out[row][col] = r.add(out[row][col], r.one)
    return tuple(tuple(values) for values in out)


def projective_equal(p, a, b, mode=None):
    r = ring(p)
    if mshape(a) != mshape(b):
        return False
    za, zb = is_zero(r, a), is_zero(r, b)
    if mode == "zero-collapse" and za != zb:
        return True
    if za or zb:
        return za and zb
    if mode == "phase-only":
        return any(a == mscale(r, r.zpow[e], b) for e in range(p))
    flat_a = tuple(x for row in a for x in row)
    flat_b = tuple(x for row in b for x in row)
    anchor = next(i for i, x in enumerate(flat_a) if x != r.zero)
    if flat_b[anchor] == r.zero:
        return False
    return all(r.mul(x, flat_b[anchor]) == r.mul(y, flat_a[anchor])
               for x, y in zip(flat_a, flat_b))


def proj_unique(p, items):
    out = []
    for item in items:
        if not any(projective_equal(p, item, old) for old in out):
            out.append(item)
    return tuple(out)


def half(p, x):
    return x * pow(2, -1, p) % p


@lru_cache(None)
def hilbert_basis(p, rank):
    return tuple(itertools.product(range(p), repeat=rank))


def vadd(x, y, p):
    return tuple((a + b) % p for a, b in zip(x, y))


@lru_cache(None)
def weyl(p, rank, label, wrong_sign=False):
    r, basis = ring(p), hilbert_basis(p, rank)
    index = {x: i for i, x in enumerate(basis)}
    a, b = label[0::2], label[1::2]
    out = [list(row) for row in mzero(r, p ** rank, p ** rank)]
    for j, y in enumerate(basis):
        z = vadd(y, a, p)
        sign = 1 if wrong_sign else -1
        exponent = sum(sign * bi * (yi + ai) + half(p, ai * bi)
                       for ai, bi, yi in zip(a, b, y)) % p
        out[index[z]][j] = r.zpow[exponent]
    return tuple(tuple(row) for row in out)


def form(label, other, p):
    return sum(label[2*i] * other[2*i+1] - other[2*i] * label[2*i+1]
               for i in range(len(label) // 2)) % p


def label_add(x, y, p):
    return tuple((a + b) % p for a, b in zip(x, y))


def fourier(p, reverse=False):
    r = ring(p)
    sign = -1 if reverse else 1
    return tuple(tuple(r.zpow[(sign * x * y) % p] for y in range(p))
                 for x in range(p))


def shear(p, value=1):
    r = ring(p)
    return tuple(tuple(r.zpow[(-half(p, value * x * x)) % p] if x == y else r.zero
                       for y in range(p)) for x in range(p))


def generator_matrices(p, wrong_weyl=False, reverse_fourier=False, drop_shear=False):
    x = weyl(p, 1, (1, 0), wrong_weyl)
    z = weyl(p, 1, (0, 1), wrong_weyl)
    f = fourier(p, reverse_fourier)
    d = shear(p)
    generators = [x, z, f]
    if not drop_shear:
        generators.append(d)
    generators += [mdag(ring(p), g) for g in tuple(generators)]
    return tuple(generators)


@lru_cache(None)
def clifford_group(p, drop_shear=False):
    r, reps, queue = ring(p), [midentity(ring(p), p)], []
    queue.append(reps[0])
    gens = generator_matrices(p, drop_shear=drop_shear)
    while queue:
        current = queue.pop(0)
        for gen in gens:
            candidate = mmul(r, gen, current)
            if not any(projective_equal(p, candidate, old) for old in reps):
                reps.append(candidate)
                queue.append(candidate)
                if len(reps) > 4000:
                    raise RuntimeError("projective generator closure exceeded guard")
    return tuple(reps)


def delta_zero(p):
    r = ring(p)
    return tuple((r.one,) if i == 0 else (r.zero,) for i in range(p))


def state_orbit(p):
    r, reps, queue = ring(p), [delta_zero(p)], [delta_zero(p)]
    gens = generator_matrices(p)
    while queue:
        state = queue.pop(0)
        for gen in gens:
            candidate = tuple((x,) for x in mvec(r, gen, tuple(row[0] for row in state)))
            if not any(projective_equal(p, candidate, old) for old in reps):
                reps.append(candidate)
                queue.append(candidate)
                if len(reps) > p * (p + 1) + 10:
                    raise RuntimeError("stabilizer-state orbit exceeded guard")
    return tuple(reps)


def outer(p, left, right):
    return mmul(ring(p), left, mdag(ring(p), right))


@lru_cache(None)
def actual_families(p):
    r = ring(p)
    cliffs = clifford_group(p)
    states = state_orbit(p)
    effects = tuple(mdag(r, state) for state in states)
    rank_one = proj_unique(p, (outer(p, s, t) for s in states for t in states))
    endos = proj_unique(p, cliffs + rank_one)
    return cliffs, states, effects, rank_one, endos


def gate_s1(mode):
    for p in (3, 5):
        r = ring(p)
        wrong_weyl = mode == "weyl-sign"
        labels = tuple(vectors(p, 2))
        ops = {v: weyl(p, 1, v, wrong_weyl) for v in labels}
        for v in labels:
            for w in labels:
                lhs = mmul(r, ops[v], ops[w])
                rhs = mscale(r, r.zpow[half(p, form(v, w, p))],
                             ops[label_add(v, w, p)])
                need("S1", lhs == rhs, "F%d D1703 Weyl product failed at %s,%s" % (p, v, w))
        f = fourier(p, reverse=(mode == "fourier-sign"))
        fd = mdag(r, f)
        need("S1", mmul(r, fd, f) == mintscale(r, p, midentity(r, p)),
             "F%d unnormalized Fourier Gram is not pI" % p)
        for a, b in labels:
            lhs = mmul(r, f, mmul(r, ops[(a, b)], fd))
            rhs = mintscale(r, p, ops[(b, -a % p)])
            need("S1", lhs == rhs, "F%d Fourier covariance sign failed at %s" % (p, (a, b)))
        d = shear(p)
        dd = mdag(r, d)
        for a, b in labels:
            need("S1", mmul(r, d, mmul(r, ops[(a, b)], dd)) == ops[(a, (b + a) % p)],
                 "F%d shear covariance failed at %s" % (p, (a, b)))
    group = clifford_group(3, drop_shear=(mode == "drop-shear"))
    need("S1", len(group) == 216, "qutrit projective Clifford census is %d, expected 216" % len(group))
    need("S1", len(state_orbit(3)) == 12, "qutrit stabilizer-state orbit is not 12")
    need("S1", len(state_orbit(5)) == 30, "F5 stabilizer-state orbit is not 30")
    return "exact F3/F5 generators; 216 qutrit Cliffords and 12/30 state rays"


def gate_s2(mode):
    p, r = 3, ring(3)
    a = fourier(p)
    two_a = mintscale(r, 2, a)
    need("S2", projective_equal(p, a, two_a, mode=mode if mode == "phase-only" else None),
         "D1705 failed to identify two distinct nonzero norms")
    need("S2", not projective_equal(p, mzero(r, 3, 3), a,
                                    mode=mode if mode == "zero-collapse" else None),
         "D1705 collapsed zero with a nonzero map")
    cliffs, states, effects, rank_one, endos = actual_families(3)
    need("S2", (len(cliffs), len(states), len(effects), len(rank_one), len(endos)) ==
         (216, 12, 12, 144, 360),
         "actual qutrit family census is %s" %
         ((len(cliffs), len(states), len(effects), len(rank_one), len(endos)),))
    need("S2", all(not any(projective_equal(3, c, a) for a in rank_one) for c in cliffs),
         "a full-rank Clifford class collided with a rank-one amplitude")
    return "C^times quotient, zero separation; actual Hom nonzero counts 1,12,12,360"


# D1715 relation-to-operator controls.


@lru_cache(None)
def weyl_monomial(p, rank, label):
    basis = hilbert_basis(p, rank)
    index = {x: i for i, x in enumerate(basis)}
    a, b = label[0::2], label[1::2]
    perm, exponents = [], []
    for y in basis:
        z = vadd(y, a, p)
        exponent = sum(-bi * (yi + ai) + half(p, ai * bi)
                       for ai, bi, yi in zip(a, b, y)) % p
        perm.append(index[z])
        exponents.append(exponent)
    return tuple(perm), tuple(exponents)


def omega_relation(rel, origin, direction):
    return omega(rel.src.dual() + rel.tgt, origin, direction)


def projector_column(rel, origin, seed, mode=None):
    p, r = rel.src.p, ring(rel.src.p)
    m, n = len(rel.src.signs), len(rel.tgt.signs)
    dm, dn, size = p ** m, p ** n, p ** (m + n)
    x, y = seed // dn, seed % dn
    _, basis, _ = affine_data(rel.pts, 2 * (m + n), p)
    directions = span_n(basis, 2 * (m + n), p)
    out = [r.zero] * size
    for direction in directions:
        v, w = direction[:2 * m], direction[2 * m:]
        pm, em = weyl_monomial(p, m, v)
        pn, en = weyl_monomial(p, n, w)
        exponent = omega_relation(rel, origin, direction)
        if mode == "average-sign":
            exponent = -exponent
        elif mode == "origin-dependent":
            exponent += sum(a * b for a, b in zip(origin, direction))
        exponent = (exponent - em[x] + en[y]) % p
        target = pm[x] * dn + pn[y]
        out[target] = r.add(out[target], r.zpow[exponent])
    return tuple(out)


@lru_cache(None)
def projector_matrix(rel, origin, mode=None):
    p = rel.src.p
    size = p ** (len(rel.src.signs) + len(rel.tgt.signs))
    columns = tuple(projector_column(rel, origin, j, mode) for j in range(size))
    return tuple(tuple(columns[j][i] for j in range(size)) for i in range(size))


def unvectorize(p, vec, m, n):
    dm, dn = p ** m, p ** n
    return tuple(tuple(vec[x * dn + y] for x in range(dm)) for y in range(dn))


def vectorize(matrix):
    rows, cols = mshape(matrix)
    return tuple((matrix[y][x],) for x in range(cols) for y in range(rows))


@lru_cache(None)
def relation_operator(rel, mode=None, origin=None):
    p, r = rel.src.p, ring(rel.src.p)
    m, n = len(rel.src.signs), len(rel.tgt.signs)
    dm, dn = p ** m, p ** n
    if not rel.pts:
        if mode == "empty-nonzero":
            out = [list(row) for row in mzero(r, dn, dm)]
            out[0][0] = r.one
            return tuple(tuple(row) for row in out)
        return mzero(r, dn, dm)
    if origin is None:
        origin = affine_data(rel.pts, 2 * (m + n), p)[0]
    projector = projector_matrix(rel, origin,
                                 mode if mode in ("average-sign", "origin-dependent") else None)
    seeds = (0,) if mode == "fixed-seed" else range(dm * dn)
    for seed in seeds:
        column = tuple(projector[i][seed] for i in range(dm * dn))
        if any(x != r.zero for x in column):
            return unvectorize(p, column, m, n)
    return mzero(r, dn, dm)


def mtrace(r, matrix):
    rows, cols = mshape(matrix)
    if rows != cols:
        raise ValueError("trace of non-square matrix")
    return sum_ring(r, (matrix[i][i] for i in range(rows)))


def relation_equations_hold(rel, operator):
    if not rel.pts:
        return is_zero(ring(rel.src.p), operator)
    p, r = rel.src.p, ring(rel.src.p)
    m, n = len(rel.src.signs), len(rel.tgt.signs)
    _, basis, _ = affine_data(rel.pts, 2 * (m + n), p)
    directions = span_n(basis, 2 * (m + n), p)
    for origin in rel.pts:
        for direction in directions:
            v, w = direction[:2 * m], direction[2 * m:]
            lhs = mmul(r, weyl(p, n, w),
                       mmul(r, operator, mdag(r, weyl(p, m, v))))
            rhs = mscale(r, r.zpow[(-omega_relation(rel, origin, direction)) % p],
                         operator)
            if lhs != rhs:
                return False
    return True


def family_with_zero(p, rows, cols, nonzero):
    return (mzero(ring(p), rows, cols),) + tuple(nonzero)


def same_projective_family(p, left, right):
    return (len(proj_unique(p, left)) == len(proj_unique(p, right)) and
            all(any(projective_equal(p, x, y) for y in right) for x in left) and
            all(any(projective_equal(p, y, x) for x in left) for y in right))


def vertical_state(p, position):
    return Rel(zero(p), plane(p),
               frozenset((position % p, b) for b in range(p)))


def horizontal_state(p, momentum=0):
    return Rel(zero(p), plane(p),
               frozenset((a, momentum % p) for a in range(p)))


def gate_s3(mode):
    p, r = 3, ring(3)
    cats = {(a, b): catalog(p, a, b) for a in range(2) for b in range(2)}
    mapped = {}
    expected_counts = {(0, 0): 2, (0, 1): 13, (1, 0): 13, (1, 1): 361}
    for key, rels in cats.items():
        images = []
        for rel in rels:
            active = mode if mode in ("average-sign", "fixed-seed", "empty-nonzero") else None
            operator = relation_operator(rel, mode=active)
            if rel.pts:
                need("S3", not is_zero(r, operator),
                     "S3a nonzero-image failed for actual F3 catalog relation in Hom%s" % (key,))
                need("S3", relation_equations_hold(rel, operator),
                     "S3b all-origin D1715 equations failed for actual F3 catalog relation in Hom%s" %
                     (key,))
                origin, _, _ = affine_data(rel.pts, rel.src.dim + rel.tgt.dim, p)
                projector = projector_matrix(rel, origin)
                if mode == "projector-entry":
                    projector = bump_entry(r, projector)
                size = p ** (sum(key))
                need("S3", mmul(r, projector, projector) == mintscale(r, size, projector),
                     "S3c projector-square P^2=|L|P failed for actual F3 data in Hom%s" %
                     (key,))
                need("S3", mtrace(r, projector) == r.smul(size, r.one),
                     "S3d projector-trace failed for actual F3 data in Hom%s" % (key,))
                origin_mode = "origin-dependent" if mode == "origin-dependent" else None
                chosen = relation_operator(rel, mode=origin_mode, origin=origin)
                for alternate in rel.pts:
                    other = relation_operator(rel, mode=origin_mode, origin=alternate)
                    need("S3", other == chosen,
                         "S3e origin-independence failed at %s in actual F3 Hom%s" %
                         (alternate, key))
            else:
                need("S3", is_zero(r, operator),
                     "S3f empty-zero failed for actual F3 catalog relation in Hom%s" % (key,))
            images.append(operator)
        need("S3", len(proj_unique(p, images)) == expected_counts[key],
             "S3g projective-injectivity failed in F3 Hom%s" % (key,))
        mapped[key] = tuple(images)

    cliffs, states, effects, rank_one, endos = actual_families(p)
    if mode == "family-state-loss":
        states = states[:-1]
    actual_homs = {
        (0, 0): family_with_zero(p, 1, 1, (midentity(r, 1),)),
        (0, 1): family_with_zero(p, 3, 1, states),
        (1, 0): family_with_zero(p, 1, 3, effects),
        (1, 1): family_with_zero(p, 3, 3, endos),
    }
    for key in mapped:
        need("S3", same_projective_family(p, mapped[key], actual_homs[key]),
             "S3h actual-family equality failed for F3 Hom%s" % (key,))
    graph_images = tuple(relation_operator(graph(a, p)) for a in affine_arrows(p))
    need("S3", same_projective_family(p, graph_images, cliffs),
         "S3i graph/Clifford split failed over F3")
    graph_set = set(graph(a, p) for a in affine_arrows(p))
    nongraph_images = tuple(relation_operator(rel) for rel in cats[(1, 1)]
                            if rel.pts and rel not in graph_set)
    need("S3", same_projective_family(p, nongraph_images, rank_one),
         "S3j nongraph/rank-one split failed over F3")

    p5 = 5
    states5 = catalog(p5, 0, 1)
    images5 = tuple(relation_operator(rel) for rel in states5)
    orbit5 = state_orbit(p5)
    if mode == "f5-state-loss":
        orbit5 = orbit5[:-1]
    actual5 = family_with_zero(p5, 5, 1, orbit5)
    need("S3", len(states5) == 31 and same_projective_family(p5, images5, actual5),
         "S3k F5-state equality failed against the actual Clifford orbit")
    need("S3", all(relation_equations_hold(rel, op)
                   for rel, op in zip(states5, images5)),
         "S3l F5 state image failed a D1715 equation")
    return "all 389 F3 relation lines/censuses and 31 F5 states; all-origin equations"


def gate_s4(mode):
    p, r = 3, ring(3)
    cats = {(a, b): catalog(p, a, b) for a in range(2) for b in range(2)}
    count = 0
    for a, b, c in itertools.product(range(2), repeat=3):
        for before in cats[a, b]:
            for after in cats[b, c]:
                composite = compose(after, before)
                lhs = relation_operator(composite)
                after_op, before_op = relation_operator(after), relation_operator(before)
                rhs = mmul(r, after_op, before_op)
                if mode == "product-order" and a == b == c == 1:
                    rhs = mmul(r, before_op, after_op)
                if (mode == "zero-product" and before.pts and after.pts and
                        not composite.pts and is_zero(r, rhs)):
                    rhs = bump_entry(r, rhs)
                    need("S4", projective_equal(p, lhs, rhs),
                         "S4b bulk-zero composition failed for nonempty factors %d->%d->%d" %
                         (a, b, c))
                need("S4", projective_equal(p, lhs, rhs),
                     "S4a bulk functoriality failed in typed composition %d->%d->%d" %
                     (a, b, c))
                count += 1
    daggers = 0
    for rels in cats.values():
        for rel in rels:
            actual_dagger = mdag(r, relation_operator(rel),
                                 transpose_only=(mode == "dagger-transpose"))
            need("S4", projective_equal(p, relation_operator(dagger(rel)),
                                        actual_dagger),
                 "S4c bulk dagger compatibility failed for an actual F3 relation")
            daggers += 1

    s0, s1, sh = vertical_state(p, 0), vertical_state(p, 1), horizontal_state(p, 0)
    e0, eh = dagger(s0), dagger(sh)
    need("S4", compose(e0, s1) == empty(zero(p), zero(p)) and
         is_zero(r, mmul(r, relation_operator(e0), relation_operator(s1))),
         "orthogonal state/effect did not give matching zero scalars")
    scalars = (mmul(r, relation_operator(e0), relation_operator(s0)),
               mmul(r, relation_operator(eh), relation_operator(s0)))
    need("S4", not is_zero(r, scalars[0]) and not is_zero(r, scalars[1]) and
         scalars[0] != scalars[1] and projective_equal(p, *scalars),
         "distinct nonzero overlap magnitudes did not give one C^times scalar class")
    need("S4", (count, daggers) == (140101, 389),
         "composition/dagger census is %s" % ((count, daggers),))
    return "all 140,101 F3 compositions, 389 daggers, zero and unequal nonzero scalars"


def tensor_check(p, left, right, reverse=False):
    relation_image = relation_operator(tensor(left, right))
    first, second = relation_operator(left), relation_operator(right)
    actual = mkron(ring(p), second, first) if reverse else mkron(ring(p), first, second)
    return projective_equal(p, relation_image, actual)


def bell(p, singleton=False):
    r = ring(p)
    return tuple((r.one if (i == j and (not singleton or i == 0)) else r.zero,)
                 for i in range(p) for j in range(p))


def gate_s5(mode):
    p = 3
    translation = graph(((1, 0), (1, 0, 0, 1)), p)
    fourier_graph = graph(((0, 0), (0, 1, -1 % p, 0)), p)
    states = catalog(p, 0, 1)
    effects = catalog(p, 1, 0)
    for left, right in itertools.product(states, repeat=2):
        need("S5", tensor_check(p, left, right, reverse=(mode == "tensor-order")),
             "S5a bulk F3 state tensor failed")
    for left, right in itertools.product(effects, repeat=2):
        need("S5", tensor_check(p, left, right, reverse=(mode == "tensor-order")),
             "S5b bulk F3 effect tensor failed")
    selected = (
        empty(zero(p), zero(p)), identity(zero(p)), vertical_state(p, 0),
        horizontal_state(p, 0), dagger(vertical_state(p, 0)),
        dagger(horizontal_state(p, 0)), empty(plane(p), plane(p)),
        identity(plane(p)), translation, fourier_graph,
        graph(((0, 0), (1, 0, 1, 1)), p),
        tensor(dagger(vertical_state(p, 0)), vertical_state(p, 0)),
    )
    selected_count = 0
    for left, right in itertools.product(selected, repeat=2):
        need("S5", tensor_check(p, left, right, reverse=(mode == "tensor-order")),
             "S5c selected mixed F3 tensor failed")
        selected_count += 1

    for q in (3, 5):
        r = ring(q)
        ident = identity(plane(q))
        vector = vectorize(relation_operator(ident))
        cup_vector = bell(q, singleton=(mode == "cup-singleton"))
        need("S5", projective_equal(q, vector, cup_vector),
             "S5d F%d operator vectorization does not give the Bell cup" % q)
        cap_vector = mdag(r, bell(q))
        if mode == "f5-cap-weight" and q == 5:
            cap_vector = bump_entry(r, cap_vector)
        closed = mmul(r, cap_vector, bell(q))
        need("S5", closed == ((r.smul(q, r.one),),),
             "S5e F%d unnormalized cup/cap scalar is not p" % q)
    return "169 state + 169 effect + %d mixed tensors; F3/F5 Bell cups and scalar p" % selected_count


GATES = {"S1": gate_s1, "S2": gate_s2, "S3": gate_s3,
         "S4": gate_s4, "S5": gate_s5}


def parse_args(argv):
    if argv is None:
        argv = sys.argv[1:]
    ap = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    ap.add_argument("--root", help="repository root (normally auto-detected)")
    for name, (gate, description) in sorted(MUTATIONS.items()):
        ap.add_argument("--red-" + name, dest="red", action="store_const", const=name,
                        help="%s at %s" % (description, gate))
    args = ap.parse_args(argv)
    if sum(arg.startswith("--red-") for arg in argv) > 1:
        ap.error("choose exactly one red mode")
    return args


def main(argv=None):
    args = parse_args(argv)
    if args.red:
        target = MUTATIONS[args.red][0]
        try:
            detail = GATES[target](args.red)
        except GateFailure as exc:
            if exc.gate != target:
                print("WRONG GATE: %s expected %s: %s" % (exc.gate, target, exc.detail))
                return 2
            print("RED CAUGHT %s at %s: %s" % (args.red, exc.gate, exc.detail))
            return 1
        except Exception as exc:
            print("RED ERROR %s at %s: %s" % (args.red, target, exc))
            return 2
        print("RED SURVIVED %s at %s: %s" % (args.red, target, detail))
        return 0
    try:
        for gate, fn in GATES.items():
            print("%s PASS: %s" % (gate, fn(None)))
    except GateFailure as exc:
        print("%s FAIL: %s" % (exc.gate, exc.detail))
        return 1
    except Exception as exc:
        print("CHECKER ERROR: %s" % exc)
        return 2
    print("GREEN PASS: exact finite checks only; no claim promotion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
