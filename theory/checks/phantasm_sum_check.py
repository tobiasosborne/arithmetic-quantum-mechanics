#!/usr/bin/env python3
"""Exact finite falsifier for SP-SUM.

Dense matrices retain explicit rectangular shapes, including 0xn and nx0.
Passing U1--U8 does not prove the arbitrary-prime/rank/list claim.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import itertools
from pathlib import Path
import sys


MUTATIONS = {
    "matrix-unit-loss": ("U1", "delete the last rank-two preparation"),
    "census-loss": ("U2", "truncate the imported qutrit endomorphism census"),
    "pure-two-unit": ("U2", "insert diag(1,1,0) into the pure qutrit census"),
    "coherent-tagged": ("U3", "erase off-diagonal coherent blocks"),
    "merge-repeated": ("U4", "merge repeated equal-rank list positions"),
    "empty-vacuum": ("U5", "realize the empty list as C"),
    "dephase-offdiag": ("U6", "retain the P0 A P1 cross term"),
    "projection-loss": ("U7", "omit the second summand projection"),
    "dephase-average": ("U7", "divide dephasing by the block count"),
    "normalized-trace": ("U8", "use normalized summand traces"),
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
sys.path.insert(1, str(ROOT / "theory/lanes/phantasm-stabilizer/checker"))
try:
    from phantasm_stabilizer_check import actual_families, projective_equal, ring
except ImportError as exc:
    raise SystemExit("cannot import exact qutrit census: %s" % exc)


@dataclass(frozen=True)
class Rect:
    rows: int
    cols: int
    data: tuple

    def __post_init__(self):
        if len(self.data) != self.rows or any(len(row) != self.cols for row in self.data):
            raise ValueError("entry data do not match explicit shape %dx%d" %
                             (self.rows, self.cols))


def rz(rows, cols):
    return Rect(rows, cols, tuple(tuple(F(0) for _ in range(cols)) for _ in range(rows)))


def rid(n):
    return Rect(n, n, tuple(tuple(F(i == j) for j in range(n)) for i in range(n)))


def rfrom(entries):
    rows = len(entries)
    cols = len(entries[0]) if rows else 0
    return Rect(rows, cols, tuple(tuple(F(x) for x in row) for row in entries))


def runit(rows, cols, i, j):
    return Rect(rows, cols,
                tuple(tuple(F((r, c) == (i, j)) for c in range(cols))
                      for r in range(rows)))


def radd(a, b):
    if (a.rows, a.cols) != (b.rows, b.cols):
        raise ValueError("addition shape mismatch")
    return Rect(a.rows, a.cols,
                tuple(tuple(x + y for x, y in zip(ra, rb))
                      for ra, rb in zip(a.data, b.data)))


def rscale(c, a):
    c = F(c)
    return Rect(a.rows, a.cols, tuple(tuple(c * x for x in row) for row in a.data))


def rmul(a, b):
    if a.cols != b.rows:
        raise ValueError("product shape mismatch %dx%d times %dx%d" %
                         (a.rows, a.cols, b.rows, b.cols))
    out = [[F(0) for _ in range(b.cols)] for _ in range(a.rows)]
    for i in range(a.rows):
        for k in range(a.cols):
            for j in range(b.cols):
                out[i][j] += a.data[i][k] * b.data[k][j]
    return Rect(a.rows, b.cols, tuple(tuple(row) for row in out))


def rdag(a):
    return Rect(a.cols, a.rows,
                tuple(tuple(a.data[j][i] for j in range(a.rows))
                      for i in range(a.cols)))


def rkron(a, b):
    return Rect(a.rows * b.rows, a.cols * b.cols,
                tuple(tuple(a.data[i // b.rows][j // b.cols] *
                            b.data[i % b.rows][j % b.cols]
                            for j in range(a.cols * b.cols))
                      for i in range(a.rows * b.rows)))


def rtrace(a):
    if a.rows != a.cols:
        raise ValueError("trace of rectangular matrix")
    return sum((a.data[i][i] for i in range(a.rows)), F(0))


def rvec(a):
    return tuple(x for row in a.data for x in row)


def rank_rows(rows):
    if not rows:
        return 0
    a = [list(map(F, row)) for row in rows]
    ncols, rank = len(a[0]), 0
    for col in range(ncols):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        z = a[rank][col]
        a[rank] = [x / z for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                z = a[i][col]
                a[i] = [x - z * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def rrank(a):
    return rank_rows(a.data)


def rmatvec(a, vector):
    if a.cols != len(vector):
        raise ValueError("matrix/vector shape mismatch")
    return tuple(sum((a.data[i][j] * vector[j] for j in range(a.cols)), F(0))
                 for i in range(a.rows))


def tuples(rank):
    return tuple(itertools.product(range(3), repeat=rank))


def shift_one(amount):
    return Rect(3, 3, tuple(tuple(F(i == (j + amount) % 3) for j in range(3))
                            for i in range(3)))


def preparation(rank, point):
    if rank == 0:
        return Rect(1, 1, ((F(1),),))
    shift = shift_one(point[0])
    vacuum = Rect(3, 1, ((F(1),), (F(0),), (F(0),)))
    for coordinate in point[1:]:
        shift = rkron(shift, shift_one(coordinate))
        vacuum = rkron(vacuum, Rect(3, 1, ((F(1),), (F(0),), (F(0),))))
    return rmul(shift, vacuum)


def preparations(rank, lose=False):
    points = tuples(rank)
    if lose and rank == 2:
        points = points[:-1]
    return tuple((point, preparation(rank, point)) for point in points)


def matrix_unit_words(mrank, nrank, lose=False):
    outputs = preparations(mrank, lose=lose)
    inputs = preparations(nrank, lose=lose)
    return tuple((y, x, rmul(ket, rdag(bra)))
                 for y, ket in outputs for x, bra in inputs)


@dataclass(frozen=True)
class HList:
    ranks: tuple

    @property
    def dims(self):
        return tuple(3 ** n for n in self.ranks)

    @property
    def dim(self):
        return sum(self.dims)


@dataclass(frozen=True)
class BlockArrow:
    src: HList
    tgt: HList
    blocks: tuple

    def __post_init__(self):
        if len(self.blocks) != len(self.tgt.ranks):
            raise ValueError("wrong target block-row count")
        for j, row in enumerate(self.blocks):
            if len(row) != len(self.src.ranks):
                raise ValueError("wrong source block-column count")
            for i, block in enumerate(row):
                if (block.rows, block.cols) != (self.tgt.dims[j], self.src.dims[i]):
                    raise ValueError("ill-typed block (%d,%d)" % (j, i))


def zero_arrow(src, tgt):
    return BlockArrow(src, tgt,
                      tuple(tuple(rz(dj, di) for di in src.dims) for dj in tgt.dims))


def offsets(dims):
    out, total = [], 0
    for dim in dims:
        out.append(total)
        total += dim
    return tuple(out)


def realize(arrow, tagged_only=False):
    so, to = offsets(arrow.src.dims), offsets(arrow.tgt.dims)
    data = [[F(0) for _ in range(arrow.src.dim)] for _ in range(arrow.tgt.dim)]
    for j, row in enumerate(arrow.blocks):
        for i, block in enumerate(row):
            if tagged_only and arrow.src == arrow.tgt and i != j:
                continue
            for u in range(block.rows):
                for v in range(block.cols):
                    data[to[j] + u][so[i] + v] = block.data[u][v]
    return Rect(arrow.tgt.dim, arrow.src.dim, tuple(tuple(row) for row in data))


def block_apply(arrow, inputs):
    outputs = []
    for j, row in enumerate(arrow.blocks):
        out = [F(0)] * arrow.tgt.dims[j]
        for i, block in enumerate(row):
            value = rmatvec(block, inputs[i])
            out = [x + y for x, y in zip(out, value)]
        outputs.append(tuple(out))
    return tuple(outputs)


def flatten(parts):
    return tuple(x for part in parts for x in part)


def compose_blocks(after, before):
    if before.tgt != after.src:
        raise ValueError("block composition mismatch")
    rows = []
    for k in range(len(after.tgt.ranks)):
        row = []
        for i in range(len(before.src.ranks)):
            value = rz(after.tgt.dims[k], before.src.dims[i])
            for j in range(len(before.tgt.ranks)):
                value = radd(value, rmul(after.blocks[k][j], before.blocks[j][i]))
            row.append(value)
        rows.append(tuple(row))
    return BlockArrow(before.src, after.tgt, tuple(rows))


def dagger_blocks(arrow):
    return BlockArrow(arrow.tgt, arrow.src,
                      tuple(tuple(rdag(arrow.blocks[j][i])
                                  for j in range(len(arrow.tgt.ranks)))
                            for i in range(len(arrow.src.ranks))))


def deterministic_block(rows, cols, seed):
    return Rect(rows, cols,
                tuple(tuple(F(((seed + 2*i + 3*j) % 7) - 3, 5)
                            for j in range(cols)) for i in range(rows)))


def block_fixture(src, tgt, seed=1):
    return BlockArrow(src, tgt,
                      tuple(tuple(deterministic_block(dj, di, seed + 5*j + i)
                                  for i, di in enumerate(src.dims))
                            for j, dj in enumerate(tgt.dims)))


def summand_projections(hlist):
    off = offsets(hlist.dims)
    result = []
    for position, dim in enumerate(hlist.dims):
        entries = [[F(0) for _ in range(hlist.dim)] for _ in range(hlist.dim)]
        for i in range(off[position], off[position] + dim):
            entries[i][i] = F(1)
        result.append(Rect(hlist.dim, hlist.dim, tuple(tuple(row) for row in entries)))
    return tuple(result)


def dephase(operator, projections, retain_cross=False, average=False):
    out = rz(operator.rows, operator.cols)
    for projection in projections:
        out = radd(out, rmul(projection, rmul(operator, projection)))
    if retain_cross and len(projections) >= 2:
        out = radd(out, rmul(projections[0], rmul(operator, projections[1])))
    return rscale(F(1, len(projections)), out) if average else out


def membership(hlist):
    return tuple(position for position, dim in enumerate(hlist.dims)
                 for _ in range(dim))


def tagged_coordinate_units(hlist):
    owner = membership(hlist)
    return tuple(runit(hlist.dim, hlist.dim, i, j)
                 for i, j in itertools.product(range(hlist.dim), repeat=2)
                 if owner[i] == owner[j])


def coherent_coordinate_units(hlist):
    return tuple(runit(hlist.dim, hlist.dim, i, j)
                 for i, j in itertools.product(range(hlist.dim), repeat=2))


def gate_u1(mode):
    total = 0
    for mrank, nrank in itertools.product(range(3), repeat=2):
        words = matrix_unit_words(mrank, nrank, lose=(mode == "matrix-unit-loss"))
        rows, cols = 3 ** mrank, 3 ** nrank
        for y, x, unit in words:
            yi, xi = tuples(mrank).index(y), tuples(nrank).index(x)
            need("U1", unit == runit(rows, cols, yi, xi),
                 "actual preparation/adjoint word has wrong rectangular entry pattern")
        rank = rank_rows(tuple(rvec(unit) for _, _, unit in words))
        need("U1", rank == rows * cols,
             "rectangular matrix-unit words span rank %d of shape dimension %d" %
             (rank, rows * cols))
        total += len(words)
    need("U1", total == 169, "matrix-unit word census changed to %d" % total)
    return "169 actual preparation/adjoint words; full rank for all nine rank pairs"


def gate_u2(mode):
    exact_ring = ring(3)
    diag = ((exact_ring.one, exact_ring.zero, exact_ring.zero),
            (exact_ring.zero, exact_ring.one, exact_ring.zero),
            (exact_ring.zero, exact_ring.zero, exact_ring.zero))
    cliffs, _, _, rank_one, endos = actual_families(3)
    if mode == "census-loss":
        endos = endos[:-1]
    distinct = all(not projective_equal(3, endos[i], endos[j])
                   for i in range(len(endos)) for j in range(i + 1, len(endos)))
    need("U2", (len(cliffs), len(rank_one), len(endos)) == (216, 144, 360) and distinct,
         "U2a imported-census guard failed: expected 216 Clifford, 144 rank-one, 360 distinct endomorphism rays")
    actual = endos + ((diag,) if mode == "pure-two-unit" else ())
    need("U2", not any(projective_equal(3, diag, candidate) for candidate in actual),
         "U2b diag(1,1,0) was misclassified as an actual pure stabilizer amplitude")
    units = matrix_unit_words(1, 1)
    e00 = next(unit for y, x, unit in units if y == (0,) and x == (0,))
    e11 = next(unit for y, x, unit in units if y == (1,) and x == (1,))
    rational_diag = rfrom(((1, 0, 0), (0, 1, 0), (0, 0, 0)))
    need("U2", radd(e00, e11) == rational_diag and rrank(rational_diag) == 2,
         "two-unit coherent span witness was not reconstructed independently")
    return "diag(1,1,0) is a rank-two coherent sum outside 360 pure qutrit classes"


def gate_u3(mode):
    simple = HList((0, 1))
    cross = zero_arrow(simple, simple)
    rows = [list(row) for row in cross.blocks]
    rows[0][1] = rfrom(((1, 0, 0),))
    cross = BlockArrow(simple, simple, tuple(tuple(row) for row in rows))
    actual = realize(cross, tagged_only=(mode == "coherent-tagged"))
    need("U3", actual == realize(cross) and rrank(actual) == 1,
         "coherent block action erased an off-diagonal summand map")

    x, y, z = HList((0, 1, 1)), HList((1, 0)), HList((0, 1))
    first, second = block_fixture(x, y, 2), block_fixture(y, z, 11)
    basis_vectors = []
    for position, dim in enumerate(x.dims):
        for index in range(dim):
            parts = tuple(tuple(F(k == index) for k in range(d)) if i == position
                          else tuple(F(0) for _ in range(d))
                          for i, d in enumerate(x.dims))
            basis_vectors.append(parts)
    for parts in basis_vectors:
        need("U3", rmatvec(realize(first), flatten(parts)) == flatten(block_apply(first, parts)),
             "dense block placement disagrees with D1707 tuple action")
    composite = compose_blocks(second, first)
    need("U3", realize(composite) == rmul(realize(second), realize(first)),
         "block-matrix composition does not realize as dense composition")
    need("U3", realize(dagger_blocks(first)) == rdag(realize(first)),
         "block adjoint-transpose does not realize as dense adjoint")
    return "coherent cross block, repeated-position tuple action, composition and dagger"


def gate_u4(mode):
    cases = ((0, 1), (0, 0, 1), (1, 1), (2,))
    observed = []
    for ranks in cases:
        actual_ranks = (tuple(dict.fromkeys(ranks))
                        if mode == "merge-repeated" else ranks)
        actual = HList(actual_ranks)
        canonical = HList(ranks)
        coherent = coherent_coordinate_units(actual)
        tagged = tagged_coordinate_units(actual)
        crank = rank_rows(tuple(rvec(unit) for unit in coherent))
        trank = rank_rows(tuple(rvec(unit) for unit in tagged))
        expected_coherent = canonical.dim * canonical.dim
        expected_tagged = sum(d*d for d in canonical.dims)
        need("U4", actual.dim == canonical.dim and
             crank == expected_coherent and trank == expected_tagged,
             "repeated list positions or coherent/tagged coordinate dimensions were merged")
        observed.append((crank, trank, crank - trank))
    need("U4", tuple(observed) == ((16, 10, 6), (25, 11, 14),
                                    (36, 18, 18), (81, 81, 0)),
         "derived coherent/tagged dimension table changed")
    return "derived dimensions 16/10,25/11,36/18,81/81 with repeated positions"


def gate_u5(mode):
    empty_list, y = HList(()), HList((0, 1))
    canonical_to = realize(zero_arrow(empty_list, y))
    canonical_from = realize(zero_arrow(y, empty_list))
    canonical_end = realize(zero_arrow(empty_list, empty_list))
    empty_dim = 1 if mode == "empty-vacuum" else empty_list.dim
    to_y = rz(y.dim, empty_dim)
    from_y = rz(empty_dim, y.dim)
    end = rz(empty_dim, empty_dim)
    need("U5", to_y == canonical_to and from_y == canonical_from and end == canonical_end and
         (to_y.rows, to_y.cols, from_y.rows, from_y.cols,
                end.rows, end.cols) == (4, 0, 0, 4, 0, 0),
         "empty-list realization was confused with rank-zero H_(F3,0)=C")
    need("U5", rdag(to_y) == from_y and rmul(from_y, to_y) == end and
         rmul(to_y, from_y) == rz(4, 4),
         "typed empty matrices fail dagger/composition")
    h0 = HList((0,))
    need("U5", h0.dim == 1 and rid(1) != end and
         rank_rows((rvec(rid(1)),)) == 1,
         "singleton rank-zero object did not retain its one-dimensional algebra")
    return "typed 4x0,0x4,0x0 maps; empty list 0 differs from rank-zero C"


def gate_u6(mode):
    hlist = HList((0, 1))
    projections = summand_projections(hlist)
    owner = membership(hlist)
    fixed, killed = 0, 0
    for i, j in itertools.product(range(4), repeat=2):
        unit = runit(4, 4, i, j)
        actual = dephase(unit, projections, retain_cross=(mode == "dephase-offdiag"))
        expected = unit if owner[i] == owner[j] else rz(4, 4)
        need("U6", actual == expected,
             "block dephasing disagrees at matrix unit E_(%d,%d)" % (i, j))
        fixed += owner[i] == owner[j]
        killed += owner[i] != owner[j]
    need("U6", (fixed, killed) == (10, 6), "dephasing fixed/killed census changed")
    return "all 16 matrix units: ten diagonal-block fixed, six off-diagonal killed"


def gate_u7(mode):
    hlist = HList((0, 1))
    projections = summand_projections(hlist)
    used = projections[:-1] if mode == "projection-loss" else projections
    completeness = rz(4, 4)
    for projection in used:
        completeness = radd(completeness, rmul(rdag(projection), projection))
    need("U7", completeness == rid(4),
         "U7a summand-projection Kraus family is incomplete")
    average = mode == "dephase-average"
    image_identity = dephase(rid(4), used, average=average)
    need("U7", image_identity == rid(4), "U7b block dephasing is not unital")
    images = tuple(dephase(unit, used, average=average)
                   for unit in coherent_coordinate_units(hlist))
    need("U7", all(dephase(image, used, average=average) == image
                   for image in images),
         "U7c block dephasing is not idempotent")
    image_rank = rank_rows(tuple(rvec(image) for image in images))
    tagged = tagged_coordinate_units(hlist)
    need("U7", image_rank == rank_rows(tuple(rvec(unit) for unit in tagged)) and
         all(dephase(unit, used, average=average) == unit for unit in tagged),
         "U7d dephasing range is not exactly the tagged block algebra")
    return "projection completeness, unitality, idempotence and rank-ten tagged range"


def block_trace(operator, hlist, normalized=False):
    off = offsets(hlist.dims)
    total = F(0)
    for start, dim in zip(off, hlist.dims):
        value = sum((operator.data[start+i][start+i] for i in range(dim)), F(0))
        total += value / dim if normalized else value
    return total


def gate_u8(mode):
    hlist = HList((0, 1))
    projections = summand_projections(hlist)
    tests = list(coherent_coordinate_units(hlist))
    tests += [rid(4), rfrom(((1, F(1, 2), 0, 0),
                             (F(1, 3), 2, 0, 0),
                             (0, 0, 3, F(2, 5)),
                             (0, 0, F(1, 7), 4)))]
    for operator in tests:
        image = dephase(operator, projections)
        actual = block_trace(image, hlist, normalized=(mode == "normalized-trace"))
        need("U8", actual == rtrace(operator),
             "ordinary trace preservation was replaced by normalized block traces")
        need("U8", block_trace(image, hlist) == rtrace(image),
             "independent diagonal-block trace sum disagrees with coherent trace")
    need("U8", block_trace(rid(4), hlist, normalized=True) == 2 and rtrace(rid(4)) == 4,
         "normalized/ordinary identity trace witness changed")
    return "all matrix units plus rational dense controls; ordinary trace, not 2 versus 4"


GATES = {"U1": gate_u1, "U2": gate_u2, "U3": gate_u3, "U4": gate_u4,
         "U5": gate_u5, "U6": gate_u6, "U7": gate_u7, "U8": gate_u8}


def parse_args(argv):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--root", help="repository root (normally auto-detected)")
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
