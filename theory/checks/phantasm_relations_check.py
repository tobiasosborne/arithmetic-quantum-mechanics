#!/usr/bin/env python3
"""Exact finite falsifier for SP-LREL and its separate compact-data follow-up.

Green checks do not prove either arbitrary-field statement.  All mathematical
arithmetic is exact in F2 or F3.  See adjacent EXPECTATIONS.md for scope.
"""

import argparse
from dataclasses import dataclass
from functools import lru_cache
import itertools
import sys


MUTATIONS = {
    "source-sign": ("G1", "use +omega on the source over F3"),
    "empty-loss": ("G1", "omit explicit empty arrows"),
    "middle-forall": ("G2", "replace exists-middle by forall-middle"),
    "dagger-order": ("G3", "do not exchange source and target blocks"),
    "tensor-order": ("G4", "retain native Cartesian-product coordinates"),
    "zero-unit": ("G4", "use the symplectic plane as tensor unit"),
    "graph-translation": ("G5", "omit graph translations"),
    "compact-dual": ("G6", "replace bar(V) by V in cup and cap data"),
    "cup-order": ("G6", "type eta as 0 -> V + bar(V)"),
    "dagger-swap": ("G6", "omit the swap from compact dagger compatibility"),
    "snake-wire": ("G6", "replace the first snake cap by an empty relation"),
    "empty-name": ("G7", "send the empty 0->0 arrow to the true named scalar"),
    "loop-multiplicity": ("G7", "retain the closed-loop witness count"),
    "name-order": ("G7", "swap the blocks of the named state"),
}


class GateFailure(Exception):
    def __init__(self, gate, detail):
        super().__init__(detail)
        self.gate, self.detail = gate, detail


def need(gate, value, detail):
    if not value:
        raise GateFailure(gate, detail)


@dataclass(frozen=True)
class Obj:
    p: int
    signs: tuple

    @property
    def dim(self):
        return 2 * len(self.signs)

    def dual(self):
        return Obj(self.p, tuple((-s) % self.p for s in self.signs))

    def __add__(self, other):
        assert self.p == other.p
        return Obj(self.p, self.signs + other.signs)


@dataclass(frozen=True)
class Rel:
    src: Obj
    tgt: Obj
    pts: frozenset

    def __post_init__(self):
        assert self.src.p == self.tgt.p
        assert all(len(x) == self.src.dim + self.tgt.dim for x in self.pts)


def zero(p):
    return Obj(p, ())


def plane(p):
    return Obj(p, (1,))


@lru_cache(None)
def vectors(p, n):
    return tuple(itertools.product(range(p), repeat=n))


def addv(x, y, p):
    return tuple((a + b) % p for a, b in zip(x, y))


def subv(x, y, p):
    return tuple((a - b) % p for a, b in zip(x, y))


def rref(rows, n, p):
    a = [[x % p for x in row[:n]] for row in rows if any(x % p for x in row[:n])]
    pivots, i = [], 0
    for j in range(n):
        k = next((k for k in range(i, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        z = pow(a[i][j], -1, p)
        a[i] = [(z * x) % p for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                z = a[k][j]
                a[k] = [(x - z * y) % p for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return tuple(tuple(row) for row in a[:i]), tuple(pivots)


def row_basis(rows, n, p):
    return rref(rows, n, p)[0]


def nullspace(rows, n, p):
    rr, piv = rref(rows, n, p)
    free = [j for j in range(n) if j not in piv]
    out = []
    for j in free:
        x = [0] * n
        x[j] = 1
        for i, c in enumerate(piv):
            x[c] = -rr[i][j] % p
        out.append(tuple(x))
    return tuple(out)


def solve_affine(equations, n, p):
    a = [[x % p for x in coeff] + [rhs % p] for coeff, rhs in equations]
    pivots, i = [], 0
    for j in range(n):
        k = next((k for k in range(i, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[i], a[k] = a[k], a[i]
        z = pow(a[i][j], -1, p)
        a[i] = [(z * x) % p for x in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                z = a[k][j]
                a[k] = [(x - z * y) % p for x, y in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
    if any(not any(row[:n]) and row[n] for row in a):
        return None
    x0 = [0] * n
    for k, j in enumerate(pivots):
        x0[j] = a[k][n]
    free, basis = [j for j in range(n) if j not in pivots], []
    for j in free:
        x = [0] * n
        x[j] = 1
        for k, c in enumerate(pivots):
            x[c] = -a[k][j] % p
        basis.append(tuple(x))
    return tuple(x0), tuple(basis)


def span_n(basis, n, p):
    if not basis:
        return (tuple([0] * n),)
    return tuple(tuple(sum(c * basis[i][j] for i, c in enumerate(cs)) % p
                       for j in range(n))
                 for cs in vectors(p, len(basis)))


@lru_cache(None)
def subspaces(p, n, d):
    if d == 0:
        return ((),)
    found = set()
    nonzero = vectors(p, n)[1:]
    for rows in itertools.combinations(nonzero, d):
        b = row_basis(rows, n, p)
        if len(b) == d:
            found.add(b)
    return tuple(sorted(found))


def omega(obj, x, y):
    p, total = obj.p, 0
    for i, s in enumerate(obj.signs):
        a, b = x[2 * i:2 * i + 2]
        c, d = y[2 * i:2 * i + 2]
        total += s * (a * d - c * b)
    return total % p


@lru_cache(None)
def affine_data(pts, n, p):
    if not pts:
        return None
    off = min(pts)
    basis = row_basis((subv(x, off, p) for x in pts), n, p)
    made = frozenset(addv(off, x, p) for x in span_n(basis, n, p))
    return off, basis, made


def is_affine_lagrangian(rel):
    if not rel.pts:
        return True
    p, n = rel.src.p, rel.src.dim + rel.tgt.dim
    data = affine_data(rel.pts, n, p)
    off, basis, made = data
    ambient = rel.src.dual() + rel.tgt
    return (made == rel.pts and 2 * len(basis) == n and
            all(omega(ambient, x, y) == 0 for x in basis for y in basis))


INTERN = {}


@lru_cache(None)
def catalog(p, si, ti, wrong_sign=False, keep_empty=True):
    src, tgt = (zero(p), plane(p))[si], (zero(p), plane(p))[ti]
    ambient = (src if wrong_sign else src.dual()) + tgt
    n, d, point_sets = ambient.dim, ambient.dim // 2, set()
    for basis in subspaces(p, n, d):
        if all(omega(ambient, x, y) == 0 for x in basis for y in basis):
            linear = span_n(basis, n, p)
            for off in vectors(p, n):
                point_sets.add(frozenset(addv(off, x, p) for x in linear))
    if keep_empty:
        point_sets.add(frozenset())
    out = tuple(Rel(src, tgt, pts) for pts in
                sorted(point_sets, key=lambda s: (len(s), tuple(sorted(s)))))
    if not wrong_sign and keep_empty:
        INTERN[(p, src, tgt)] = {r.pts: r for r in out}
    return out


def intern(rel):
    return INTERN.get((rel.src.p, rel.src, rel.tgt), {}).get(rel.pts, rel)


def identity(obj):
    return Rel(obj, obj, frozenset(x + x for x in vectors(obj.p, obj.dim)))


def empty(src, tgt):
    return Rel(src, tgt, frozenset())


@lru_cache(None)
def compose(after, before, universal=False):
    assert before.tgt == after.src
    p, a, b, c = before.src.p, before.src.dim, before.tgt.dim, after.tgt.dim
    if universal:
        pts = {x + z for x in vectors(p, a) for z in vectors(p, c)
               if all(x + w in before.pts and w + z in after.pts
                      for w in vectors(p, b))}
    elif not before.pts or not after.pts:
        pts = set()
    else:
        left, right = {}, {}
        for u in before.pts:
            left.setdefault(u[a:], []).append(u[:a])
        for u in after.pts:
            right.setdefault(u[:b], []).append(u[b:])
        pts = {x + z for w in left.keys() & right.keys()
               for x in left[w] for z in right[w]}
    return intern(Rel(before.src, after.tgt, frozenset(pts)))


def affine_equations(rel):
    n, p = rel.src.dim + rel.tgt.dim, rel.src.p
    off, basis, _ = affine_data(rel.pts, n, p)
    return tuple((u, sum(a * b for a, b in zip(u, off)) % p)
                 for u in nullspace(basis, n, p))


def compose_oracle(after, before):
    assert before.tgt == after.src
    if not before.pts or not after.pts:
        return empty(before.src, after.tgt), None
    p = before.src.p
    a, b, c = before.src.dim, before.tgt.dim, after.tgt.dim
    eqs = []
    for row, rhs in affine_equations(before):
        eqs.append((row + (0,) * c, rhs))
    for row, rhs in affine_equations(after):
        eqs.append(((0,) * a + row, rhs))
    solution = solve_affine(eqs, a + b + c, p)
    if solution is None:
        return empty(before.src, after.tgt), None
    off, basis = solution
    take = lambda x: x[:a] + x[a + b:]
    poff, pbasis = take(off), row_basis((take(x) for x in basis), a + c, p)
    pts = frozenset(addv(poff, x, p) for x in span_n(pbasis, a + c, p))
    return intern(Rel(before.src, after.tgt, pts)), len(pbasis)


def dagger(rel, wrong=False):
    a = rel.src.dim
    pts = rel.pts if wrong else frozenset(x[a:] + x[:a] for x in rel.pts)
    return intern(Rel(rel.tgt, rel.src, frozenset(pts)))


def tensor(left, right, wrong=False):
    assert left.src.p == right.src.p
    a, b, c = left.src.dim, left.tgt.dim, right.src.dim
    if not left.pts or not right.pts:
        pts = frozenset()
    elif wrong:
        pts = frozenset(x + y for x in left.pts for y in right.pts)
    else:
        pts = frozenset(x[:a] + y[:c] + x[a:] + y[c:]
                        for x in left.pts for y in right.pts)
    return Rel(left.src + right.src, left.tgt + right.tgt, pts)


def tensor_expected(left, right):
    """Independent Boolean-relation-matrix Kronecker oracle."""
    p = left.src.p
    ls, lt = vectors(p, left.src.dim), vectors(p, left.tgt.dim)
    rs, rt = vectors(p, right.src.dim), vectors(p, right.tgt.dim)
    lm = tuple(tuple(x + y in left.pts for x in ls) for y in lt)
    rm = tuple(tuple(x + y in right.pts for x in rs) for y in rt)
    rows, cols = len(lt) * len(rt), len(ls) * len(rs)
    kron = tuple(tuple(lm[i // len(rt)][j // len(rs)] and
                       rm[i % len(rt)][j % len(rs)]
                       for j in range(cols)) for i in range(rows))
    pts = set()
    for i, row in enumerate(kron):
        target = lt[i // len(rt)] + rt[i % len(rt)]
        for j, present in enumerate(row):
            if present:
                source = ls[j // len(rs)] + rs[j % len(rs)]
                pts.add(source + target)
    return Rel(left.src + right.src, left.tgt + right.tgt, frozenset(pts))


def swap(a, b):
    pts = frozenset(x + y + y + x for x in vectors(a.p, a.dim)
                    for y in vectors(a.p, b.dim))
    return Rel(a + b, b + a, pts)


def associator(a, b, c):
    src, tgt = (a + b) + c, a + (b + c)
    return Rel(src, tgt, frozenset(x + x for x in vectors(a.p, src.dim)))


def left_unitor(obj):
    src = zero(obj.p) + obj
    return Rel(src, obj, frozenset(x + x for x in vectors(obj.p, obj.dim)))


def right_unitor(obj):
    src = obj + zero(obj.p)
    return Rel(src, obj, frozenset(x + x for x in vectors(obj.p, obj.dim)))


def chain(first, *afters):
    out = first
    for after in afters:
        out = compose(after, out)
    return out


def mat_apply(g, x, p):
    return ((g[0] * x[0] + g[1] * x[1]) % p,
            (g[2] * x[0] + g[3] * x[1]) % p)


def affine_arrows(p):
    mats = tuple(g for g in vectors(p, 4)
                 if (g[0] * g[3] - g[1] * g[2]) % p == 1)
    return tuple((t, g) for t in vectors(p, 2) for g in mats)


def affine_comp(after, before, p):
    s, h = after
    t, g = before
    ht = mat_apply(h, t, p)
    hg = ((h[0] * g[0] + h[1] * g[2]) % p,
          (h[0] * g[1] + h[1] * g[3]) % p,
          (h[2] * g[0] + h[3] * g[2]) % p,
          (h[2] * g[1] + h[3] * g[3]) % p)
    return (addv(s, ht, p), hg)


def affine_inv(arrow, p):
    t, g = arrow
    gi = (g[3] % p, -g[1] % p, -g[2] % p, g[0] % p)
    return tuple(-x % p for x in mat_apply(gi, t, p)), gi


def graph(arrow, p, drop_translation=False):
    t, g = arrow
    pts = frozenset(x + addv(mat_apply(g, x, p), (0, 0) if drop_translation else t, p)
                    for x in vectors(p, 2))
    return Rel(plane(p), plane(p), pts)


def graph_sum(a, b, p):
    ta, ga = a
    tb, gb = b
    pts = frozenset(x + y + addv(mat_apply(ga, x, p), ta, p) +
                    addv(mat_apply(gb, y, p), tb, p)
                    for x in vectors(p, 2) for y in vectors(p, 2))
    pp = plane(p) + plane(p)
    return Rel(pp, pp, pts)


def cup(obj, wrong=False, omit_dual=False):
    dual = obj if omit_dual else obj.dual()
    target = (obj + dual) if wrong else (dual + obj)
    return Rel(zero(obj.p), target,
               frozenset(x + x for x in vectors(obj.p, obj.dim)))


def cap(obj, omit_dual=False):
    dual = obj if omit_dual else obj.dual()
    return Rel(obj + dual, zero(obj.p),
               frozenset(x + x for x in vectors(obj.p, obj.dim)))


def samples(lengths, count, salt):
    rates = (17, 31, 47, 61)
    return tuple(tuple((rates[j] * t + (j + 3) * salt + (j + 1) * t * t) % n
                       for j, n in enumerate(lengths)) for t in range(count))


def small_catalogs(p):
    return {(i, j): catalog(p, i, j) for i in range(2) for j in range(2)}


def gate_g1(mode):
    expected = {2: (2, 7, 7, 61), 3: (2, 13, 13, 361)}
    for p in (2, 3):
        cats = []
        for i, j in ((0, 0), (0, 1), (1, 0), (1, 1)):
            cats.append(catalog(p, i, j,
                                wrong_sign=(mode == "source-sign" and p == 3 and i == j == 1),
                                keep_empty=(mode != "empty-loss")))
        need("G1", tuple(map(len, cats)) == expected[p],
             "F%d Hom census %s, expected %s" % (p, tuple(map(len, cats)), expected[p]))
        need("G1", all(any(not r.pts for r in cat) for cat in cats),
             "F%d lost an explicit empty Hom arrow" % p)
        need("G1", identity(plane(p)) in cats[3],
             "F%d diagonal identity is absent (source-form sign/order defect)" % p)
        sizes = (1, p, p, p * p)
        for cat, size in zip(cats, sizes):
            need("G1", all(not r.pts or len(r.pts) == size for r in cat),
                 "F%d nonempty affine relation has wrong cardinality" % p)
            need("G1", all(is_affine_lagrangian(r) for r in cat),
                 "F%d catalog contains a non-Lagrangian relation" % p)
    return "F2/F3 censuses (2,7,7,61) and (2,13,13,361); states/effects and empties"


def gate_g2(mode):
    count = 0
    for p in (2, 3):
        o, v = zero(p), plane(p)
        state = Rel(o, v, frozenset((x, 0) for x in range(p)))
        effect = Rel(v, o, state.pts)
        parallel = Rel(v, o, frozenset((x, 1) for x in range(p)))
        got = compose(effect, state, universal=(mode == "middle-forall"))
        need("G2", got == identity(o),
             "F%d nontransverse line composite lost existential witnesses" % p)
        need("G2", sum(1 for w in vectors(p, 2) if w in state.pts and w in effect.pts) == p,
             "F%d nontransverse witness fiber is not size q" % p)
        need("G2", compose(parallel, state) == empty(o, o),
             "F%d disjoint affine state/effect composite is not empty" % p)
        cats = small_catalogs(p)
        for a, b, c in itertools.product(range(2), repeat=3):
            target = set(cats[a, c])
            for before in cats[a, b]:
                for after in cats[b, c]:
                    actual = compose(after, before)
                    oracle, dim = compose_oracle(after, before)
                    need("G2", actual == oracle,
                         "F%d existential composition disagrees with affine-equation oracle" % p)
                    need("G2", actual in target and is_affine_lagrangian(actual),
                         "F%d composition is outside the target Lagrangian catalog" % p)
                    if actual.pts:
                        need("G2", dim == (before.src.dim + after.tgt.dim) // 2,
                             "F%d oracle image has wrong Lagrangian dimension" % p)
                    count += 1
    need("G2", count == 144806, "composition comparison count is %d" % count)
    return "144,806 existential/oracle pairs; nontransverse fibers and empty composites"


def gate_g3(mode):
    count, assoc = 0, 0
    for p in (2, 3):
        cats, v = small_catalogs(p), plane(p)
        witness = graph(((1, 0), (1, 0, 0, 1)), p)
        need("G3", dagger(witness, wrong=(mode == "dagger-order")) ==
             graph(affine_inv(((1, 0), (1, 0, 0, 1)), p), p),
             "F%d converse failed to swap graph coordinate blocks" % p)
        for a, b in itertools.product(range(2), repeat=2):
            ia, ib = identity((zero(p), v)[a]), identity((zero(p), v)[b])
            for r in cats[a, b]:
                need("G3", compose(ib, r) == r and compose(r, ia) == r,
                     "F%d relation identity law failed" % p)
                dr = dagger(r)
                need("G3", is_affine_lagrangian(dr) and dagger(dr) == r,
                     "F%d converse dagger closure/involution failed" % p)
        for a, b, c in itertools.product(range(2), repeat=3):
            for r in cats[a, b]:
                for s in cats[b, c]:
                    need("G3", dagger(compose(s, r)) == compose(dagger(r), dagger(s)),
                         "F%d dagger reversed-composition law failed" % p)
                    count += 1
        for a, b, c, d in itertools.product(range(2), repeat=4):
            cr, cs, ct = cats[a, b], cats[b, c], cats[c, d]
            triples = itertools.product(cr, cs, ct) if p == 2 else (
                (cr[i], cs[j], ct[k]) for i, j, k in
                samples((len(cr), len(cs), len(ct)), 256, 8 * a + 4 * b + 2 * c + d))
            for r, s, t in triples:
                need("G3", compose(t, compose(s, r)) == compose(compose(t, s), r),
                     "F%d associativity failed" % p)
                assoc += 1
    need("G3", (count, assoc) == (144806, 294890),
         "dagger/associativity counts are %s" % ((count, assoc),))
    return "exhaustive identities/daggers; 290,794 F2 + 4,096 F3 associative triples"


def gate_g4(mode):
    total = 0
    for p in (2, 3):
        cats = small_catalogs(p)
        rels = tuple(r for key in sorted(cats) for r in cats[key])
        u = plane(p) if mode == "zero-unit" else zero(p)
        unit_data = identity(u)
        probe = graph(((1, 0), (1, 0, 0, 1)), p)
        need("G4", tensor(probe, unit_data) == probe and tensor(unit_data, probe) == probe,
             "F%d tensor unit is not the zero-space identity" % p)
        pairs = itertools.product(rels, repeat=2) if p == 2 else (
            (cats[a, b][i], cats[c, d][j])
            for a, b, c, d in itertools.product(range(2), repeat=4)
            for i, j in samples((len(cats[a, b]), len(cats[c, d])), 256,
                                8 * a + 4 * b + 2 * c + d))
        for r, s in pairs:
            actual = tensor(r, s, wrong=(mode == "tensor-order"))
            expected = tensor_expected(r, s)
            need("G4", actual == expected,
                 "G4a Boolean-Kronecker coordinate oracle failed over F%d" % p)
            need("G4", is_affine_lagrangian(actual),
                 "G4b tensor failed independent affine typing over F%d" % p)
            need("G4", dagger(actual) == tensor(dagger(r), dagger(s)),
                 "F%d tensor is incompatible with converse dagger" % p)
            natural = compose(swap(r.tgt, s.tgt), actual)
            need("G4", natural == compose(tensor(s, r), swap(r.src, s.src)),
                 "F%d swap naturality failed" % p)
            total += 1
        picks = rels[:16] if p == 2 else tuple(rels[i] for (i,) in samples((len(rels),), 16, 23))
        for r, s, t in zip(picks, picks[1:] + picks[:1], picks[2:] + picks[:2]):
            need("G4", tensor(tensor(r, s), t) == tensor(r, tensor(s, t)),
                 "F%d tensor associativity failed" % p)
        objs = (zero(p), plane(p))
        for a, b in itertools.product(objs, repeat=2):
            need("G4", compose(swap(b, a), swap(a, b)) == identity(a + b),
                 "F%d swap is not involutive" % p)
        for a, b, c in itertools.product(objs, repeat=3):
            lhs = swap(a, b + c)
            rhs = compose(tensor(identity(b), swap(a, c)),
                          tensor(swap(a, b), identity(c)))
            need("G4", lhs == rhs, "F%d symmetry hexagon failed" % p)
        for a, b, c, aa, bb, cc in itertools.product(range(2), repeat=6):
            c1, c2, d1, d2 = cats[a, b], cats[b, c], cats[aa, bb], cats[bb, cc]
            for i, j, k, l in samples((len(c1), len(c2), len(d1), len(d2)), 16,
                                      32*a+16*b+8*c+4*aa+2*bb+cc):
                lhs = tensor(compose(c2[j], c1[i]), compose(d2[l], d1[k]))
                rhs = compose(tensor(c2[j], d2[l]), tensor(c1[i], d1[k]))
                need("G4", lhs == rhs, "F%d tensor interchange failed" % p)
    need("G4", total == 10025, "tensor pair count is %d" % total)
    return "5,929 F2 + 4,096 F3 tensor pairs; zero unit, swap, associativity, interchange"


def gate_g5(mode):
    comps, tensors = 0, 0
    for p, expected in ((2, 24), (3, 216)):
        arrows, cat = affine_arrows(p), set(catalog(p, 1, 1))
        graphs = [graph(a, p, drop_translation=(mode == "graph-translation")) for a in arrows]
        need("G5", len(arrows) == expected and len(set(graphs)) == expected,
             "F%d affine graph data are not faithful (%d arrows, %d graphs)" %
             (p, len(arrows), len(set(graphs))))
        need("G5", all(g in cat and is_affine_lagrangian(g) for g in graphs),
             "F%d affine graph is not a catalogued Lagrangian" % p)
        for i, a in enumerate(arrows):
            need("G5", dagger(graphs[i]) == graph(affine_inv(a, p), p),
                 "F%d graph dagger does not give affine inverse" % p)
            for j, b in enumerate(arrows):
                need("G5", compose(graphs[i], graphs[j]) == graph(affine_comp(a, b, p), p),
                     "F%d graph composition failed" % p)
                comps += 1
        pairs = itertools.product(arrows, repeat=2) if p == 2 else (
            (arrows[i], arrows[j]) for i, j in samples((len(arrows), len(arrows)), 4096, 41))
        for a, b in pairs:
            need("G5", tensor(graph(a, p), graph(b, p)) == graph_sum(a, b, p),
                 "F%d graph functor does not preserve direct sum/tensor" % p)
            tensors += 1
        need("G5", graph(((0, 0), (1, 0, 0, 1)), p) == identity(plane(p)),
             "F%d graph functor does not preserve identity" % p)
    need("G5", (comps, tensors) == (47232, 4672), "graph counts are wrong")
    return "24/216 faithful graphs; 47,232 compositions and 4,672 tensor comparisons"


def gate_g6(mode):
    for p in (2, 3):
        for v in (zero(p), plane(p)):
            eta = cup(v, wrong=(mode == "cup-order"),
                      omit_dual=(mode == "compact-dual"))
            eps = cap(v, omit_dual=(mode == "compact-dual"))
            need("G6", is_affine_lagrangian(eta) and is_affine_lagrangian(eps),
                 "G6a dual-isotropy failed over F%d at rank %d" % (p, len(v.signs)))
            expected_eta = Rel(zero(p), v.dual() + v,
                               frozenset(x + x for x in vectors(p, v.dim)))
            expected_eps = Rel(v + v.dual(), zero(p), expected_eta.pts)
            need("G6", eta == expected_eta,
                 "G6b cup-factor-order failed over F%d at rank %d" % (p, len(v.signs)))
            need("G6", eps == expected_eps,
                 "G6b cap-factor-order failed over F%d at rank %d" % (p, len(v.signs)))
            dagger_rhs = (eps if mode == "dagger-swap" else
                          compose(cap(v), swap(v.dual(), v)))
            need("G6", dagger(eta) == dagger_rhs and
                 dagger(eps) == cup(v.dual()),
                 "G6c dagger-swap compatibility failed over F%d at rank %d" %
                 (p, len(v.signs)))
            snake_eps = (empty(eps.src, eps.tgt)
                         if mode == "snake-wire" and v.dim > 0 else eps)
            snake_v = chain(dagger(right_unitor(v)), tensor(identity(v), eta),
                            dagger(associator(v, v.dual(), v)),
                            tensor(snake_eps, identity(v)), left_unitor(v))
            snake_d = chain(dagger(left_unitor(v.dual())),
                            tensor(eta, identity(v.dual())),
                            associator(v.dual(), v, v.dual()),
                            tensor(identity(v.dual()), eps), right_unitor(v.dual()))
            need("G6", snake_v == identity(v),
                 "G6d first-snake relation failed over F%d at rank %d" %
                 (p, len(v.signs)))
            need("G6", snake_d == identity(v.dual()),
                 "G6e second-snake relation failed over F%d at rank %d" %
                 (p, len(v.signs)))
            need("G6", len(eta.pts) == p ** v.dim and len(eps.pts) == p ** v.dim,
                 "G6f cup/cap cardinality failed over F%d" % p)
    return "typed diagonal cups/caps, dagger order and both snakes for zero and one register"


def name_actual(rel, mode=None):
    if mode == "empty-name" and not rel.pts:
        n = rel.src.dim + rel.tgt.dim
        return Rel(zero(rel.src.p), rel.src.dual() + rel.tgt,
                   frozenset({tuple([0] * n)}))
    if mode == "name-order":
        a = rel.src.dim
        return Rel(zero(rel.src.p), rel.tgt + rel.src.dual(),
                   frozenset(x[a:] + x[:a] for x in rel.pts))
    return compose(tensor(identity(rel.src.dual()), rel), cup(rel.src))


def unname(state, src, tgt):
    return chain(dagger(right_unitor(src)), tensor(identity(src), state),
                 dagger(associator(src, src.dual(), tgt)),
                 tensor(cap(src), identity(tgt)), left_unitor(tgt))


def scalar_tensor(left, right):
    unit = left_unitor(zero(left.src.p))
    return chain(dagger(unit), tensor(left, right), unit)


def closed_loop(obj, multiplicity=False):
    relation = chain(cup(obj), swap(obj.dual(), obj), cap(obj))
    return len(vectors(obj.p, obj.dim)) if multiplicity else relation


def gate_g7(mode):
    count = 0
    for p in (2, 3):
        cats = small_catalogs(p)
        for a, b in itertools.product(range(2), repeat=2):
            src, tgt = (zero(p), plane(p))[a], (zero(p), plane(p))[b]
            for r in cats[a, b]:
                named = name_actual(r, mode=mode)
                expected = Rel(zero(p), src.dual() + tgt, r.pts)
                need("G7", named == expected,
                     "F%d named state changed relation or dual-input/output order" % p)
                need("G7", unname(named, src, tgt) == r,
                     "F%d unname(name(R)) != R, including affine/empty R" % p)
                count += 1
        f, t = empty(zero(p), zero(p)), identity(zero(p))
        need("G7", set(catalog(p, 0, 0)) == {f, t},
             "F%d unit scalars are not exactly false and true" % p)
        for x, y in itertools.product((f, t), repeat=2):
            want = t if x == t and y == t else f
            need("G7", compose(x, y) == want and scalar_tensor(x, y) == want,
                 "F%d unit scalar product is not Boolean conjunction" % p)
        for v in (zero(p), plane(p)):
            need("G7", closed_loop(v, multiplicity=(mode == "loop-multiplicity" and v.dim > 0)) == t,
                 "F%d closed cup/cap loop is not true" % p)
    need("G7", count == 466, "name/unname count is %d" % count)
    return "466 exhaustive names/unnames; Boolean unit scalars and true closed loops"


GATES = {"G1": gate_g1, "G2": gate_g2, "G3": gate_g3, "G4": gate_g4,
         "G5": gate_g5, "G6": gate_g6, "G7": gate_g7}


def parse_args(argv):
    if argv is None:
        argv = sys.argv[1:]
    ap = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    for name, (gate, description) in sorted(MUTATIONS.items()):
        ap.add_argument("--red-" + name, dest="red", action="store_const", const=name,
                        help="%s at %s" % (description, gate))
    args = ap.parse_args(argv)
    if sum(arg == "--red" or arg.startswith("--red-") for arg in argv) > 1:
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
    print("GREEN PASS: exact finite checks only; no claim promotion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
