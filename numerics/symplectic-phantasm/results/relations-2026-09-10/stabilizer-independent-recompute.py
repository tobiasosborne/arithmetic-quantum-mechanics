#!/usr/bin/env python3
"""Independent exact F3 convention probes for the SP-STAB-REL blind review.

This file imports neither repository checker nor prover code.  Eisenstein
integers use z^2+z+1=0.  The probes are examples, not a general proof.
"""

import itertools


ZERO, ONE, ZETA = (0, 0), (1, 0), (0, 1)
ZPOW = (ONE, ZETA, (-1, -1))


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def smul(n, x):
    return n * x[0], n * x[1]


def conj(x):
    return x[0] - x[1], -x[1]


def matrix(rows, cols, entries=()):
    out = [[ZERO for _ in range(cols)] for _ in range(rows)]
    for i, j, value in entries:
        out[i][j] = value
    return tuple(tuple(row) for row in out)


def ident(n):
    return matrix(n, n, ((i, i, ONE) for i in range(n)))


def madd(a, b):
    return tuple(tuple(add(x, y) for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def scale(c, a):
    return tuple(tuple(mul(c, x) for x in row) for row in a)


def mmul(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == inner
    out = [[ZERO for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for k in range(inner):
            for j in range(cols):
                out[i][j] = add(out[i][j], mul(a[i][k], b[k][j]))
    return tuple(tuple(row) for row in out)


def dag(a):
    return tuple(tuple(conj(a[j][i]) for j in range(len(a)))
                 for i in range(len(a[0])))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def kron(a, b):
    return tuple(tuple(mul(a[i // len(b)][j // len(b[0])],
                               b[i % len(b)][j % len(b[0])])
                       for j in range(len(a[0]) * len(b[0])))
                 for i in range(len(a) * len(b)))


def mconj(a):
    return tuple(tuple(conj(x) for x in row) for row in a)


def projective(a, b):
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        return False
    aa = tuple(x for row in a for x in row)
    bb = tuple(x for row in b for x in row)
    za, zb = all(x == ZERO for x in aa), all(x == ZERO for x in bb)
    if za or zb:
        return za and zb
    k = next(i for i, x in enumerate(aa) if x != ZERO)
    return bb[k] != ZERO and all(mul(x, bb[k]) == mul(y, aa[k])
                                 for x, y in zip(aa, bb))


def omega(x, y):
    return (x[0] * y[1] - y[0] * x[1]) % 3


def half(x):
    return 2 * x % 3


def weyl(label):
    a, b = label
    return matrix(3, 3, (((y + a) % 3, y,
                          ZPOW[(-b * (y + a) + half(a * b)) % 3])
                         for y in range(3)))


def wrank(rank, label):
    return ((ONE,),) if rank == 0 else weyl(label)


def vec(t):
    return tuple((t[y][x],) for x in range(len(t[0])) for y in range(len(t)))


def unvec(column, m, n):
    dm, dn = 3 ** m, 3 ** n
    return tuple(tuple(column[x * dn + y][0] for x in range(dm)) for y in range(dn))


def ambient(m, n, x, y):
    total = 0
    if m:
        total -= omega(x[:2], y[:2])
    if n:
        total += omega(x[2*m:2*m+2], y[2*m:2*m+2])
    return total % 3


def rho(m, n, direction):
    v, w = direction[:2*m], direction[2*m:]
    return kron(mconj(wrank(m, v)), wrank(n, w))


def projector(m, n, origin, directions, reverse_character=False):
    size = 3 ** (m + n)
    out = matrix(size, size)
    for direction in directions:
        exponent = ambient(m, n, origin, direction)
        if reverse_character:
            exponent = -exponent
        out = madd(out, scale(ZPOW[exponent % 3], rho(m, n, direction)))
    return out


def representative(m, n, origin, directions, reverse_character=False):
    p = projector(m, n, origin, directions, reverse_character)
    for j in range(len(p)):
        column = tuple((p[i][j],) for i in range(len(p)))
        if any(row[0] != ZERO for row in column):
            return unvec(column, m, n)
    return matrix(3 ** n, 3 ** m)


def trace(a):
    out = ZERO
    for i in range(len(a)):
        out = add(out, a[i][i])
    return out


def main():
    labels = tuple(itertools.product(range(3), repeat=2))

    # Opposite-space vectorization, recomputed on every Weyl pair and matrix unit.
    vec_checks = 0
    for v in labels:
        for w in labels:
            action = kron(mconj(weyl(v)), weyl(w))
            for i, j in itertools.product(range(3), repeat=2):
                unit = matrix(3, 3, ((i, j, ONE),))
                lhs = vec(mmul(weyl(w), mmul(unit, dag(weyl(v)))))
                assert lhs == mmul(action, vec(unit))
                vec_checks += 1

    # Identity graph average: unnormalized rank-one projector on vec(I).
    graph_direction = tuple(v + v for v in labels)
    pg = projector(1, 1, (0, 0, 0, 0), graph_direction)
    assert mmul(pg, pg) == tuple(tuple(smul(9, x) for x in row) for row in pg)
    assert trace(pg) == (9, 0)
    assert (representative(1, 1, (0, 0, 0, 0), graph_direction) ==
            tuple(tuple((3, 0) if i == j else ZERO for j in range(3))
                  for i in range(3)))

    # Computational states and an exact empty/nonempty overlap pair.
    vertical = tuple((0, b) for b in range(3))
    ket0 = representative(0, 1, (0, 0), vertical)
    ket1 = representative(0, 1, (1, 0), vertical)
    assert ket0 == (((3, 0),), ((0, 0),), ((0, 0),))
    assert ket1 == (((0, 0),), ((3, 0),), ((0, 0),))
    assert mmul(dag(ket0), ket1) == ((ZERO,),)
    assert mmul(dag(ket0), ket0) == (((9, 0),),)

    # A nonfunctional relation has the predicted initial/final supports.
    horizontal = tuple((a, 0) for a in range(3))
    product_direction = tuple(v + w for v in vertical for w in horizontal)
    t = representative(1, 1, (0, 0, 0, 0), product_direction)
    pout = projector(0, 1, (0, 0), horizontal)
    pin = projector(0, 1, (0, 0), vertical)
    assert projective(mmul(t, dag(t)), pout)
    assert projective(mmul(dag(t), t), pin)

    # Bare converse is Hilbert adjoint for a genuinely complex affine state.
    state_direction = horizontal
    state_origin = (0, 1)
    state = representative(0, 1, state_origin, state_direction)
    effect = representative(1, 0, state_origin, state_direction)
    assert projective(effect, dag(state))
    assert not projective(effect, transpose(state))

    # Independent bad-data witnesses.
    conjugation_witness = None
    for v in labels:
        good_action = kron(mconj(weyl(v)), ident(3))
        bad_action = kron(weyl(v), ident(3))
        for i, j in itertools.product(range(3), repeat=2):
            unit = matrix(3, 3, ((i, j, ONE),))
            if mmul(good_action, vec(unit)) != mmul(bad_action, vec(unit)):
                conjugation_witness = (v, i, j)
                break
        if conjugation_witness:
            break
    assert conjugation_witness is not None
    bad_ket1 = representative(0, 1, (1, 0), vertical, reverse_character=True)
    assert not projective(bad_ket1, ket1)

    print("R1 PASS: %d exact opposite-space vectorization cases" % vec_checks)
    print("R2 PASS: identity projector Q^2=9Q, trace 9, first column 3I")
    print("R3 PASS: supports, zero/nonzero overlaps, and bare-converse adjoint")
    print("R4 PASS: missing conjugation detected at %s; reversed affine character detected" %
          (conjugation_witness,))


if __name__ == "__main__":
    main()
