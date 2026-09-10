#!/usr/bin/env python3
"""Exact finite falsifier for SP-SCALAR and SP-CP.

All scalars lie in Q(i), represented by Fraction pairs.  Passing P1--P11
does not prove either arbitrary-dimensional claim or promote any status.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import itertools
import sys


MUTATIONS = {
    "scalar-modulus": ("P1", "replace |c|^2 by c^2"),
    "projective-branch": ("P1", "identify CP maps of T and 2T"),
    "contraction-reverse": ("P2", "reverse the contraction criterion"),
    "zero-conditioning": ("P2", "attempt conditioning at probability zero"),
    "kraus-adjoint-order": ("P3", "use adjoint Kraus maps in the forward type"),
    "kraus-forward-transpose": ("P3", "transpose the x1 input in actual forward action"),
    "kraus-overcomplete": ("P3", "replace (1/2)I2 by 2I2 on x1->y0"),
    "block-normalized-trace": ("P4", "normalize only the M2 output trace"),
    "kraus-list-equality": ("P5", "use list equality instead of CP-map equality"),
    "composite-index-loss": ("P6", "omit the intermediate block from path labels"),
    "tensor-tag-order": ("P6", "reverse actual tensor target tags"),
    "retained-drop-outcome": ("P7", "merge retained outcome blocks"),
    "retained-outcome-factor": ("P7", "multiply retained trace by outcome count"),
    "sequential-hide-first": ("P8", "sum away the earlier outcome"),
    "sequential-pair-order": ("P8", "emit later/earlier outcome pairs"),
    "tensor-outcome-order": ("P9", "reverse tensor outcome pairs"),
    "adjoint-direction": ("P10", "keep the forward K y K* type"),
    "adjoint-is-branch": ("P10", "classify discard's adjoint as TNI"),
    "source-equals-cp": ("P11", "replace source equality by CP-map equality"),
}


class GateFailure(Exception):
    def __init__(self, gate, detail):
        super().__init__(detail)
        self.gate, self.detail = gate, detail


def need(gate, value, detail):
    if not value:
        raise GateFailure(gate, detail)


@dataclass(frozen=True)
class G:
    re: F = F(0)
    im: F = F(0)

    def __add__(self, other):
        other = gg(other)
        return G(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        other = gg(other)
        return G(self.re - other.re, self.im - other.im)

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, other):
        other = gg(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def conj(self):
        return G(self.re, -self.im)

    def inv(self):
        norm = self.re * self.re + self.im * self.im
        if norm == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        return G(self.re / norm, -self.im / norm)

    def __truediv__(self, other):
        return self * gg(other).inv()


def gg(real=0, imag=0):
    if isinstance(real, G):
        return real
    return G(F(real), F(imag))


ZERO, ONE, II = gg(0), gg(1), gg(0, 1)


def shape(a):
    return len(a), len(a[0]) if a else 0


def mzero(rows, cols):
    return tuple(tuple(ZERO for _ in range(cols)) for _ in range(rows))


def eye(n):
    return tuple(tuple(ONE if i == j else ZERO for j in range(n)) for i in range(n))


def m(entries):
    return tuple(tuple(gg(x) for x in row) for row in entries)


def madd(a, b):
    return tuple(tuple(x + y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def mscale(c, a):
    c = gg(c)
    return tuple(tuple(c * x for x in row) for row in a)


def mmul(a, b):
    ra, ka = shape(a)
    kb, cb = shape(b)
    if ka != kb:
        raise ValueError("matrix shape mismatch %s times %s" % (shape(a), shape(b)))
    out = [[ZERO for _ in range(cb)] for _ in range(ra)]
    for i in range(ra):
        for k in range(ka):
            if a[i][k] == ZERO:
                continue
            for j in range(cb):
                out[i][j] = out[i][j] + a[i][k] * b[k][j]
    return tuple(tuple(row) for row in out)


def mdag(a):
    rows, cols = shape(a)
    return tuple(tuple(a[j][i].conj() for j in range(rows)) for i in range(cols))


def mtranspose(a):
    rows, cols = shape(a)
    return tuple(tuple(a[j][i] for j in range(rows)) for i in range(cols))


def mkron(a, b):
    ra, ca = shape(a)
    rb, cb = shape(b)
    return tuple(tuple(a[i // rb][j // cb] * b[i % rb][j % cb]
                       for j in range(ca * cb)) for i in range(ra * rb))


def mtrace(a):
    rows, cols = shape(a)
    if rows != cols:
        raise ValueError("trace of rectangular matrix")
    out = ZERO
    for i in range(rows):
        out = out + a[i][i]
    return out


def munit(n, i, j):
    return tuple(tuple(ONE if (r, c) == (i, j) else ZERO for c in range(n))
                 for r in range(n))


def determinant(a):
    n = len(a)
    if n == 0:
        return ONE
    out = ZERO
    for perm in itertools.permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i + 1, n))
        term = ONE
        for i in range(n):
            term = term * a[i][perm[i]]
        out = out + (term if inversions % 2 == 0 else -term)
    return out


def is_psd(a):
    rows, cols = shape(a)
    if rows != cols or a != mdag(a):
        return False
    for size in range(1, rows + 1):
        for subset in itertools.combinations(range(rows), size):
            principal = tuple(tuple(a[i][j] for j in subset) for i in subset)
            value = determinant(principal)
            if value.im != 0 or value.re < 0:
                return False
    return True


def outer(vector):
    return mmul(vector, mdag(vector))


def projective_matrix_equal(a, b):
    if shape(a) != shape(b):
        return False
    aa = tuple(x for row in a for x in row)
    bb = tuple(x for row in b for x in row)
    za, zb = all(x == ZERO for x in aa), all(x == ZERO for x in bb)
    if za or zb:
        return za and zb
    k = next(i for i, x in enumerate(aa) if x != ZERO)
    return bb[k] != ZERO and all(x * bb[k] == y * aa[k] for x, y in zip(aa, bb))


@dataclass(frozen=True)
class System:
    tags: tuple
    dims: tuple

    def dim(self, tag):
        return self.dims[self.tags.index(tag)]


@dataclass
class CPMap:
    src: System
    tgt: System
    kraus: dict


def kmap(src, tgt, entries):
    """entries are (out_tag,in_tag,label,matrix)."""
    data = {}
    for b, a, label, operator in entries:
        if shape(operator) != (tgt.dim(b), src.dim(a)):
            raise ValueError("ill-typed Kraus operator at %s,%s" % (b, a))
        data.setdefault((b, a), []).append((label, operator))
    return CPMap(src, tgt, {key: tuple(value) for key, value in data.items()})


def zero_blocks(system):
    return {tag: mzero(system.dim(tag), system.dim(tag)) for tag in system.tags}


def apply_map(phi, blocks, transpose_component=None):
    out = zero_blocks(phi.tgt)
    for (b, a), terms in phi.kraus.items():
        input_block = (mtranspose(blocks[a]) if transpose_component == (b, a)
                       else blocks[a])
        for _, operator in terms:
            out[b] = madd(out[b], mmul(operator, mmul(input_block, mdag(operator))))
    return out


def basis_inputs(system):
    for tag in system.tags:
        for i, j in itertools.product(range(system.dim(tag)), repeat=2):
            blocks = zero_blocks(system)
            blocks[tag] = munit(system.dim(tag), i, j)
            yield tag, i, j, blocks


def maps_equal(left, right):
    if left.src != right.src or left.tgt != right.tgt:
        return False
    return all(apply_map(left, blocks) == apply_map(right, blocks)
               for _, _, _, blocks in basis_inputs(left.src))


def coefficient_action(phi, blocks):
    """Independent superoperator-coefficient evaluation."""
    out = zero_blocks(phi.tgt)
    for b in phi.tgt.tags:
        db = phi.tgt.dim(b)
        values = [[ZERO for _ in range(db)] for _ in range(db)]
        for a in phi.src.tags:
            da = phi.src.dim(a)
            terms = phi.kraus.get((b, a), ())
            for u, v in itertools.product(range(db), repeat=2):
                total = ZERO
                for i, j in itertools.product(range(da), repeat=2):
                    coefficient = ZERO
                    for _, operator in terms:
                        coefficient = coefficient + operator[u][i] * operator[v][j].conj()
                    total = total + coefficient * blocks[a][i][j]
                values[u][v] = values[u][v] + total
        out[b] = tuple(tuple(row) for row in values)
    return out


def choi_component(phi, input_tag, output_tag):
    da, db = phi.src.dim(input_tag), phi.tgt.dim(output_tag)
    size = da * db
    out = [[ZERO for _ in range(size)] for _ in range(size)]
    for i, j in itertools.product(range(da), repeat=2):
        blocks = zero_blocks(phi.src)
        blocks[input_tag] = munit(da, i, j)
        image = apply_map(phi, blocks)[output_tag]
        for u, v in itertools.product(range(db), repeat=2):
            out[u * da + i][v * da + j] = image[u][v]
    return tuple(tuple(row) for row in out)


def completeness(phi, input_tag):
    d = phi.src.dim(input_tag)
    out = mzero(d, d)
    for b in phi.tgt.tags:
        for _, operator in phi.kraus.get((b, input_tag), ()):
            out = madd(out, mmul(mdag(operator), operator))
    return out


def is_branch(phi):
    return all(is_psd(madd(eye(phi.src.dim(a)), mscale(-ONE, completeness(phi, a))))
               for a in phi.src.tags)


def is_channel(phi):
    return all(completeness(phi, a) == eye(phi.src.dim(a)) for a in phi.src.tags)


def block_trace(system, blocks, normalize_tags=()):
    out = ZERO
    for tag in system.tags:
        value = mtrace(blocks[tag])
        if tag in normalize_tags:
            value = value / gg(system.dim(tag))
        out = out + value
    return out


def identity_blocks(system):
    return {tag: eye(system.dim(tag)) for tag in system.tags}


def single_map(operator):
    src = System(("x",), (shape(operator)[1],))
    tgt = System(("y",), (shape(operator)[0],))
    return kmap(src, tgt, (("y", "x", "k", operator),))


def sum_maps(maps, prefixes=()):
    first = maps[0]
    entries = []
    for pos, phi in enumerate(maps):
        if phi.src != first.src or phi.tgt != first.tgt:
            raise ValueError("cannot sum differently typed maps")
        prefix = prefixes[pos] if prefixes else pos
        for (b, a), terms in phi.kraus.items():
            for label, operator in terms:
                entries.append((b, a, (prefix, label), operator))
    return kmap(first.src, first.tgt, entries)


def compose_maps(after, before, lose_middle=False):
    if before.tgt != after.src:
        raise ValueError("composition type mismatch")
    entries = {}
    for c in after.tgt.tags:
        for a in before.src.tags:
            for b in before.tgt.tags:
                for j, first in before.kraus.get((b, a), ()):
                    for t, second in after.kraus.get((c, b), ()):
                        label = (j, t) if lose_middle else (b, j, t)
                        entries[(c, a, label)] = mmul(second, first)
    return kmap(before.src, after.tgt,
                ((c, a, label, operator) for (c, a, label), operator in entries.items()))


def tensor_system(left, right, reverse=False):
    tags = tuple((b, a) if reverse else (a, b) for a in left.tags for b in right.tags)
    dims = tuple(left.dim(a) * right.dim(b) for a in left.tags for b in right.tags)
    return System(tags, dims)


def tensor_maps(left, right, reverse_target=False):
    src = tensor_system(left.src, right.src)
    tgt = tensor_system(left.tgt, right.tgt, reverse=reverse_target)
    entries = []
    for (b, a), lterms in left.kraus.items():
        for (d, c), rterms in right.kraus.items():
            out_tag = (d, b) if reverse_target else (b, d)
            for j, first in lterms:
                for t, second in rterms:
                    entries.append((out_tag, (a, c), (j, t), mkron(first, second)))
    return kmap(src, tgt, entries)


def adjoint_map(phi, wrong_direction=False):
    if wrong_direction:
        return CPMap(phi.src, phi.tgt, dict(phi.kraus))
    entries = []
    for (b, a), terms in phi.kraus.items():
        for label, operator in terms:
            entries.append((a, b, label, mdag(operator)))
    return kmap(phi.tgt, phi.src, entries)


def hs_blocks(system, left, right):
    out = ZERO
    for tag in system.tags:
        out = out + mtrace(mmul(mdag(left[tag]), right[tag]))
    return out


def qutrit_operators():
    return (eye(3), m(((1, 0, 0), (0, 0, 0), (0, 0, 0))),
            m(((1, 0, 0), (0, F(1, 2), 0), (0, 0, 0))))


def gate_p1(mode):
    scalars = (ZERO, gg(F(1, 2)), gg(2), II)
    checks = 0
    for operator in qutrit_operators():
        base = single_map(operator)
        for scalar in scalars:
            actual = single_map(mscale(scalar, operator))
            factor = scalar * scalar if mode == "scalar-modulus" else scalar.conj() * scalar
            for _, _, _, blocks in basis_inputs(base.src):
                lhs = apply_map(actual, blocks)
                rhs = {tag: mscale(factor, value)
                       for tag, value in apply_map(base, blocks).items()}
                need("P1", lhs == rhs,
                     "scalar modulus law failed on actual qutrit matrix-unit data at c=%s" %
                     (scalar,))
                checks += 1
    operator = qutrit_operators()[1]
    doubled = mscale(gg(2), operator)
    equal = (projective_matrix_equal(operator, doubled) if mode == "projective-branch"
             else maps_equal(single_map(operator), single_map(doubled)))
    need("P1", not equal,
         "projective amplitude equivalence was incorrectly used as CP-map equality")
    need("P1", projective_matrix_equal(operator, doubled),
         "nonzero scalar representatives are not projectively equal")
    return "%d exact scalar/matrix-unit comparisons; projective class separated" % checks


def rank_vectors():
    base = [tuple(gg(x) for x in values)
            for values in itertools.product((-1, 0, 1), repeat=3)
            if values != (0, 0, 0)]
    base += [(gg(1), gg(F(1, 2)), ZERO), (ONE, II, gg(-1))]
    return tuple(base)


def column(values):
    return tuple((value,) for value in values)


def conditional_state(output, probability, attempt_zero=False):
    if probability == ZERO:
        return ("attempted-zero-conditioning" if attempt_zero else
                "undefined-at-zero-probability")
    return {tag: tuple(tuple(x / probability for x in row) for row in value)
            for tag, value in output.items()}


def gate_p2(mode):
    operators = qutrit_operators() + (mscale(gg(2), eye(3)), mzero(3, 3))
    expected = (True, True, True, False, True)
    vectors_ = rank_vectors()
    for operator, wanted in zip(operators, expected):
        deficit = madd(eye(3), mscale(-ONE, mmul(mdag(operator), operator)))
        contraction = is_psd(deficit)
        empirical = True
        phi = single_map(operator)
        for vector in vectors_:
            rho = outer(column(vector))
            inp = {"x": rho}
            if block_trace(phi.tgt, apply_map(phi, inp)).re > mtrace(rho).re:
                empirical = False
                break
        classified = not contraction if mode == "contraction-reverse" else contraction
        need("P2", classified == wanted and empirical == wanted,
             "contraction iff failed on actual rank-one probability data")
    zero_phi = single_map(mzero(3, 3))
    rho = {"x": mscale(gg(F(1, 3)), eye(3))}
    out = apply_map(zero_phi, rho)
    probability = block_trace(zero_phi.tgt, out)
    result = conditional_state(out, probability, attempt_zero=(mode == "zero-conditioning"))
    need("P2", probability == ZERO and result == "undefined-at-zero-probability",
         "zero-probability conditioning was not explicitly rejected")
    nonzero = single_map(mscale(gg(F(1, 2)), eye(3)))
    out2 = apply_map(nonzero, rho)
    prob2 = block_trace(nonzero.tgt, out2)
    conditioned = conditional_state(out2, prob2)
    need("P2", block_trace(nonzero.tgt, conditioned) == ONE,
         "positive-probability conditional state is not normalized")
    return "five contraction cases and %d exact rank-one inputs; zero conditioning rejected" % len(vectors_)


def block_fixture(overcomplete=False):
    x = System(("x0", "x1"), (1, 2))
    y = System(("y0", "y1"), (2, 1))
    middle = mscale(gg(2), eye(2)) if overcomplete else mscale(gg(F(1, 2)), eye(2))
    return kmap(x, y, (
        ("y0", "x0", "a", m(((F(3, 5),), (0,)))),
        ("y1", "x0", "b", m(((F(4, 5),),))),
        ("y0", "x1", "c", middle),
        ("y1", "x1", "d", m(((F(1, 3), 0),))),
    ))


def phased_block_fixture():
    x = System(("x0", "x1"), (1, 2))
    y = System(("y0", "y1"), (2, 1))
    return kmap(x, y, (
        ("y0", "x0", "a", ((gg(0, F(3, 5)),), (ZERO,))),
        ("y1", "x0", "b", m(((F(4, 5),),))),
        ("y0", "x1", "c", m(((F(1, 2), 0), (0, F(1, 2))))),
        ("y1", "x1", "d", m(((F(1, 3), 0),))),
    ))


def gate_p3(mode):
    phi = block_fixture(overcomplete=(mode == "kraus-overcomplete"))
    if mode == "kraus-adjoint-order":
        wrong = adjoint_map(phi)
        need("P3", wrong.src == phi.src and wrong.tgt == phi.tgt,
             "rectangular K* rho K construction has reverse type Y->X, expected X->Y")
    checks = 0
    for tag, i, j, blocks in basis_inputs(phi.src):
        actual = apply_map(phi, blocks,
                           transpose_component=(("y0", "x1")
                                                if mode == "kraus-forward-transpose" else None))
        need("P3", actual == coefficient_action(phi, blocks),
             "P3a coefficient-action failed at %s:E_(%d,%d)" % (tag, i, j))
        checks += 1
    for a in phi.src.tags:
        for b in phi.tgt.tags:
            need("P3", is_psd(choi_component(phi, a, b)),
                 "P3b Choi PSD failed for component %s->%s" % (a, b))
    deficits = {a: madd(eye(phi.src.dim(a)), mscale(-ONE, completeness(phi, a)))
                for a in phi.src.tags}
    need("P3", all(is_psd(value) for value in deficits.values()) and
         deficits["x0"] == mzero(1, 1) and deficits["x1"] != mzero(2, 2),
         "P3c per-input block completeness/strictness failed")
    return "%d block matrix units, four independent Choi PSD tests, per-input completeness" % checks


def trace_channel():
    x, y = System(("q",), (2,)), System(("q", "c"), (2, 1))
    return kmap(x, y, (
        ("q", "q", "keep", mscale(gg(F(3, 5)), eye(2))),
        ("c", "q", "e0", m(((F(4, 5), 0),))),
        ("c", "q", "e1", m(((0, F(4, 5)),))),
    ))


def gate_p4(mode):
    phi = trace_channel()
    need("P4", is_channel(phi), "rational block fixture is not a channel")
    densities = (
        m(((F(1, 2), 0), (0, F(1, 2)))),
        m(((1, 0), (0, 0))),
        m(((F(2, 3), F(1, 6)), (F(1, 6), F(1, 3)))),
    )
    for rho in densities:
        output = apply_map(phi, {"q": rho})
        normalize = ("q",) if mode == "block-normalized-trace" else ()
        need("P4", block_trace(phi.tgt, output, normalize) == mtrace(rho),
             "ordinary block trace was replaced by a normalized M2 trace")
    rho = densities[0]
    output = apply_map(phi, {"q": rho})
    need("P4", mtrace(output["q"]) == gg(F(9, 25)) and
         mtrace(output["c"]) == gg(F(16, 25)),
         "channel block weights are not 9/25 and 16/25")
    return "ordinary trace channel; block weights 9/25+16/25=1"


def identity_kraus_pair():
    system = System(("q",), (2,))
    one = kmap(system, system, (("q", "q", "one", eye(2)),))
    two = kmap(system, system, (
        ("q", "q", "three", mscale(gg(F(3, 5)), eye(2))),
        ("q", "q", "four", mscale(gg(F(4, 5)), eye(2))),
    ))
    return one, two


def gate_p5(mode):
    one, two = identity_kraus_pair()
    actual_equal = (one.kraus == two.kraus if mode == "kraus-list-equality"
                    else maps_equal(one, two))
    need("P5", actual_equal,
         "equal CP maps were distinguished by their nonunique Kraus lists")
    need("P5", one.kraus != two.kraus and
         all(apply_map(one, blocks) == apply_map(two, blocks)
             for _, _, _, blocks in basis_inputs(one.src)),
         "identity Kraus fixtures lost their list/map distinction")
    return "{I} equals {(3/5)I,(4/5)I} as maps on four matrix units"


def scalar_path_fixture():
    x = System(("in",), (1,))
    y = System(("mid0", "mid1"), (1, 1))
    z = System(("out",), (1,))
    before = kmap(x, y, (
        ("mid0", "in", "j", m(((F(3, 5),),))),
        ("mid1", "in", "j", m(((F(4, 5),),))),
    ))
    after = kmap(y, z, (
        ("out", "mid0", "t", ((ONE,),)),
        ("out", "mid1", "t", ((ONE,),)),
    ))
    return before, after


def independent_tensor_units(left, right, tensor_map):
    if (tensor_map.src != tensor_system(left.src, right.src) or
            tensor_map.tgt != tensor_system(left.tgt, right.tgt)):
        return False
    for (a, c) in tensor_map.src.tags:
        da, dc = left.src.dim(a), right.src.dim(c)
        for row, col in itertools.product(range(da * dc), repeat=2):
            i, k = divmod(row, dc)
            j, l = divmod(col, dc)
            lb, rb = zero_blocks(left.src), zero_blocks(right.src)
            lb[a], rb[c] = munit(da, i, j), munit(dc, k, l)
            actual_input = zero_blocks(tensor_map.src)
            actual_input[(a, c)] = munit(da * dc, row, col)
            actual = apply_map(tensor_map, actual_input)
            lo, ro = apply_map(left, lb), apply_map(right, rb)
            expected = {(b, d): mkron(lo[b], ro[d])
                        for b in left.tgt.tags for d in right.tgt.tags}
            if actual != expected:
                return False
    return True


def gate_p6(mode):
    before, after = scalar_path_fixture()
    composed = compose_maps(after, before, lose_middle=(mode == "composite-index-loss"))
    for _, _, _, blocks in basis_inputs(before.src):
        expected = apply_map(after, apply_map(before, blocks))
        need("P6", apply_map(composed, blocks) == expected,
             "composite Kraus data lost an intermediate-block path")
    need("P6", is_channel(composed), "two-path scalar composite is not a channel")

    q = System(("q",), (2,))
    dephase = kmap(q, q, (
        ("q", "q", "p0", m(((1, 0), (0, 0)))),
        ("q", "q", "p1", m(((0, 0), (0, 1)))),
    ))
    prep = kmap(System(("u",), (1,)), q,
                (("q", "u", "ket0", m(((1,), (0,)))),))
    discard = kmap(q, System(("u",), (1,)), (
        ("u", "q", "bra0", m(((1, 0),))),
        ("u", "q", "bra1", m(((0, 1),))),
    ))
    triple = compose_maps(discard, compose_maps(dephase, prep))
    need("P6", maps_equal(triple, kmap(prep.src, discard.tgt,
                                       (("u", "u", "id", ((ONE,),)),))),
         "preparation/dephasing/discard composition failed")

    left = trace_channel()
    right_system = System(("r0", "r1"), (1, 2))
    right = kmap(right_system, right_system, (
        ("r0", "r0", "i0", ((ONE,),)),
        ("r1", "r1", "i1", eye(2)),
    ))
    product = tensor_maps(left, right, reverse_target=(mode == "tensor-tag-order"))
    need("P6", independent_tensor_units(left, right, product),
         "tensor map has wrong Cartesian block tags or matrix-unit action")
    return "two-path composition, prep/dephase/discard, and full tensor matrix units"


def weighted_instrument(weights, outcomes, system):
    return {outcome: kmap(system, system,
                          ((system.tags[0], system.tags[0], outcome,
                            mscale(gg(weight), eye(system.dims[0]))),))
            for outcome, weight in zip(outcomes, weights)}


def retain_instrument(instrument, drop=False):
    outcomes = tuple(instrument)
    first = instrument[outcomes[0]]
    if drop:
        return sum_maps(tuple(instrument[o] for o in outcomes), outcomes)
    tags = tuple((o, b) for o in outcomes for b in first.tgt.tags)
    dims = tuple(first.tgt.dim(b) for o in outcomes for b in first.tgt.tags)
    target = System(tags, dims)
    entries = []
    for o in outcomes:
        for (b, a), terms in instrument[o].kraus.items():
            for label, operator in terms:
                entries.append(((o, b), a, (o, label), operator))
    return kmap(first.src, target, entries)


def gate_p7(mode):
    system = System(("q",), (2,))
    inst = weighted_instrument((F(3, 5), F(4, 5)), ("red", "blue"), system)
    channel = sum_maps(tuple(inst.values()), tuple(inst))
    need("P7", is_channel(channel) and maps_equal(channel,
         kmap(system, system, (("q", "q", "id", eye(2)),))),
         "instrument branches do not sum to identity channel")
    retained = retain_instrument(inst, drop=(mode == "retained-drop-outcome"))
    expected_tags = (("red", "q"), ("blue", "q"))
    need("P7", retained.tgt.tags == expected_tags,
         "retained construction erased outcome-first external blocks")
    densities = (m(((1, 0), (0, 0))),
                 m(((F(1, 2), F(1, 4)), (F(1, 4), F(1, 2)))))
    for rho in densities:
        output = apply_map(retained, {"q": rho})
        traced = block_trace(retained.tgt, output)
        if mode == "retained-outcome-factor":
            traced = gg(2) * traced
        need("P7", traced == mtrace(rho),
             "retained instrument trace gained an outcome-count factor")
    return "two outcome-first M2 blocks; channel sum and retained trace one"


def sequential_instruments(first, second, hide_first=False, reverse=False):
    output = {}
    for o, phi in first.items():
        for r, psi in second.items():
            key = r if hide_first else ((r, o) if reverse else (o, r))
            composite = compose_maps(psi, phi)
            if key in output:
                output[key] = sum_maps((output[key], composite), ("old", o))
            else:
                output[key] = composite
    return output


def instrument_probability(phi, rho):
    return block_trace(phi.tgt, apply_map(phi, rho))


def gate_p8(mode):
    system = System(("q",), (2,))
    first = weighted_instrument((F(3, 5), F(4, 5)), ("red", "blue"), system)
    second = weighted_instrument((F(5, 13), F(12, 13)), ("left", "right"), system)
    seq = sequential_instruments(first, second,
                                 hide_first=(mode == "sequential-hide-first"),
                                 reverse=(mode == "sequential-pair-order"))
    expected = (("red", "left"), ("red", "right"),
                ("blue", "left"), ("blue", "right"))
    need("P8", tuple(seq) == expected,
         "sequential outcomes are not retained in earlier/later order")
    rho = {"q": m(((1, 0), (0, 0)))}
    probabilities = tuple(instrument_probability(seq[key], rho) for key in expected)
    wanted = (gg(F(9, 169)), gg(F(1296, 4225)),
              gg(F(16, 169)), gg(F(2304, 4225)))
    need("P8", probabilities == wanted and sum((x.re for x in probabilities), F(0)) == 1,
         "sequential branch probabilities or channel sum failed")
    return "four earlier/later outcomes with exact probabilities summing to one"


def tensor_instruments(first, second, reverse=False):
    return {((s, o) if reverse else (o, s)): tensor_maps(phi, theta)
            for o, phi in first.items() for s, theta in second.items()}


def gate_p9(mode):
    system = System(("q",), (2,))
    first = weighted_instrument((F(3, 5), F(4, 5)), ("red", "blue"), system)
    second = weighted_instrument((F(5, 13), F(12, 13)), ("left", "right"), system)
    product = tensor_instruments(first, second, reverse=(mode == "tensor-outcome-order"))
    expected = (("red", "left"), ("red", "right"),
                ("blue", "left"), ("blue", "right"))
    need("P9", tuple(product) == expected,
         "tensor instrument outcomes are not in listed-factor order")
    rho = {("q", "q"): mkron(m(((1, 0), (0, 0))),
                                m(((F(1, 2), 0), (0, F(1, 2)))))}
    probabilities = tuple(instrument_probability(product[key], rho) for key in expected)
    need("P9", sum((x.re for x in probabilities), F(0)) == 1 and
         all(independent_tensor_units(first[o], second[s], product[(o, s)])
             for o in first for s in second),
         "tensor instrument map equality or trace normalization failed")
    return "four listed-factor tensor outcomes; independent map action and trace one"


def gate_p10(mode):
    phi = phased_block_fixture()
    adj = adjoint_map(phi, wrong_direction=(mode == "adjoint-direction"))
    need("P10", adj.src == phi.tgt and adj.tgt == phi.src,
         "rectangular adjoint has forward type X->Y instead of reverse Y->X")
    checks = 0
    for _, _, _, x in basis_inputs(phi.src):
        for _, _, _, y in basis_inputs(phi.tgt):
            need("P10", hs_blocks(phi.tgt, y, apply_map(phi, x)) ==
                 hs_blocks(phi.src, apply_map(adj, y), x),
                 "ordinary Hilbert-Schmidt pairing failed on rectangular block units")
            checks += 1
    need("P10", all(is_psd(choi_component(adj, b, a))
                    for b in adj.src.tags for a in adj.tgt.tags),
         "trace adjoint is not CP in reconstructed Choi oracle")
    subunit = apply_map(adj, identity_blocks(phi.tgt))
    need("P10", all(is_psd(madd(eye(phi.src.dim(a)), mscale(-ONE, subunit[a])))
                    for a in phi.src.tags),
         "branch adjoint is not subunital")

    channel = trace_channel()
    cadj = adjoint_map(channel)
    need("P10", apply_map(cadj, identity_blocks(channel.tgt)) == identity_blocks(channel.src),
         "channel adjoint is not unital")
    q, scalar = System(("q",), (2,)), System(("u",), (1,))
    discard = kmap(q, scalar, (
        ("u", "q", "e0", m(((1, 0),))),
        ("u", "q", "e1", m(((0, 1),))),
    ))
    dadj = adjoint_map(discard)
    output = apply_map(dadj, {"u": ((ONE,),)})
    actual_tni = block_trace(dadj.tgt, output).re <= 1
    claimed_tni = True if mode == "adjoint-is-branch" else actual_tni
    need("P10", output["q"] == eye(2) and not actual_tni and claimed_tni == actual_tni,
         "discard adjoint was incorrectly classified as a reverse TNI branch")
    return "%d rectangular pairing checks; CP/subunital adjoint and non-TNI discard adjoint" % checks


@dataclass(frozen=True)
class SourceArrow:
    name: str
    hidden_labels: tuple
    realized: object


def source_equal(left, right, mode=None):
    if mode == "source-equals-cp":
        return maps_equal(left.realized, right.realized)
    return left.name == right.name and left.hidden_labels == right.hidden_labels


def gate_p11(mode):
    unit, q = System(("u",), (1,)), System(("q",), (2,))
    prep0 = kmap(unit, q, (("q", "u", "ket0", m(((1,), (0,)))),))
    prep1 = kmap(unit, q, (("q", "u", "ket1", m(((0,), (1,)))),))
    discard = kmap(q, unit, (
        ("u", "q", "bra0", m(((1, 0),))),
        ("u", "q", "bra1", m(((0, 1),))),
    ))
    ident_scalar = kmap(unit, unit, (("u", "u", "one", ((ONE,),)),))
    need("P11", maps_equal(compose_maps(discard, prep0), ident_scalar) and
         maps_equal(compose_maps(discard, prep1), ident_scalar),
         "D1327 basis preparation/discard failed in ambient formulas")

    projectors = {
        "success": kmap(q, q, (("q", "q", "p0", m(((1, 0), (0, 0)))),)),
        "failure": kmap(q, q, (("q", "q", "p1", m(((0, 0), (0, 1)))),)),
    }
    retained = retain_instrument(projectors)
    need("P11", retained.tgt.tags == (("success", "q"), ("failure", "q")) and
         is_channel(sum_maps(tuple(projectors.values()), tuple(projectors))),
         "D1327-style retained decoder lost tags or normalization")

    one, two = identity_kraus_pair()
    source_one = SourceArrow("source-one", ("one",), one)
    source_two = SourceArrow("source-two", ("three", "four"), two)
    need("P11", maps_equal(one, two) and
         not source_equal(source_one, source_two,
                          mode=mode if mode == "source-equals-cp" else None),
         "distinct D1325 source arrows were identified by equal CP realization")
    return "basis preparations/discard, retained decoder tags, and finer source equality"


GATES = {"P1": gate_p1, "P2": gate_p2, "P3": gate_p3,
         "P4": gate_p4, "P5": gate_p5, "P6": gate_p6,
         "P7": gate_p7, "P8": gate_p8, "P9": gate_p9,
         "P10": gate_p10, "P11": gate_p11}


def parse_args(argv):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    for name, (gate, description) in sorted(MUTATIONS.items()):
        parser.add_argument("--red-" + name, dest="red", action="store_const", const=name,
                            help="%s at %s" % (description, gate))
    args = parser.parse_args(argv)
    if sum(arg.startswith("--red-") for arg in argv) > 1:
        parser.error("choose exactly one red mode")
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
        for gate, function in GATES.items():
            print("%s PASS: %s" % (gate, function(None)))
    except GateFailure as exc:
        print("%s FAIL: %s" % (exc.gate, exc.detail))
        return 1
    except Exception as exc:
        print("CHECKER ERROR: %s" % exc)
        return 2
    print("GREEN PASS: exact finite controls only; no claim promotion")
    return 0


if __name__ == "__main__":
    sys.exit(main())
