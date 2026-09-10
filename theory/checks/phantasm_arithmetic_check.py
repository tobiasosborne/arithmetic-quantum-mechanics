#!/usr/bin/env python3
"""Exact finite falsifier for SP-TRACE, SP-FROB and SP-SUBSYS.

Rank-two extension-field operators are sparse actions, never dense matrices.
Passing A1--A12 proves no arbitrary-rank or all-extension statement.
"""

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import itertools
from pathlib import Path
import sys


MUTATIONS = {
    "trace-degree": ("A1", "replace F27 trace by degree multiplication"),
    "character-conflation": ("A2", "use the restricted absolute character"),
    "tower-order": ("A3", "use x+x^3 for the F81/F9 trace stage"),
    "half-form-trace": ("A4", "omit half on the restricted-form side"),
    "absolute-frobenius": ("A5", "use cube instead of ninth power over F81/F9"),
    "half-coordinate": ("A6", "apply Frobenius only to translation labels"),
    "covariance-census-loss": ("A6", "truncate the F81 rank-two state census"),
    "rank-zero": ("A7", "replace the empty tensor identity by a qutrit"),
    "degenerate-subsystem": ("A8", "use the configuration-half injection"),
    "decoder-normalized-trace": ("A9", "divide actual partial trace by three"),
    "decoder-direction": ("A10", "trace the retained subsystem factor"),
    "decoder-phase": ("A11", "phase only one occurrence of J/J*"),
    "decoder-tower-order": ("A12", "retain the first discarded tower factor"),
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
try:
    from f1_check import Abelian
    from phantasm_egorov_check import GF as MonoGF, weyl_mono
    from wh_kappa_check import CycRing
    from wh_kappa.ff import GF
except ImportError as exc:
    raise SystemExit("cannot import exact GF tables: %s" % exc)


@lru_cache(None)
def field(degree):
    return GF(3, degree)


def fa(f, x, y):
    return f.ADD[x][y]


def fm(f, x, y):
    return f.MUL[x][y]


def fn(f, x):
    return f.NEG[x]


def fsum(f, values):
    out = 0
    for value in values:
        out = fa(f, out, value)
    return out


def trace27(x):
    f = field(3)
    return fsum(f, (x, f.pow(x, 3), f.pow(x, 9)))


def trace27_degree(x):
    f = field(3)
    return fsum(f, (x, x, x))


def base81():
    f = field(4)
    return tuple(x for x in range(81) if f.pow(x, 9) == x)


def trace81_9(x, wrong=False):
    f = field(4)
    return fa(f, x, f.pow(x, 3 if wrong else 9))


def trace9_3(y):
    f = field(4)
    return fa(f, y, f.pow(y, 3))


def trace81_3_direct(x):
    f = field(4)
    return fsum(f, (x, f.pow(x, 3), f.pow(x, 9), f.pow(x, 27)))


def parameter9():
    f = field(4)
    return next(x for x in base81() if f.pow(x, 3) != x)


def chi9(y):
    f = field(4)
    return trace9_3(fm(f, parameter9(), y))


def chi81_relative(x):
    return chi9(trace81_9(x))


def basis_over_subfield(f, base):
    if len(base) == 3:
        basis = tuple(3 ** i for i in range(f.n))
        made = {fsum(f, (fm(f, c, b) for c, b in zip(coeffs, basis)))
                for coeffs in itertools.product(base, repeat=len(basis))}
        if len(made) != f.q:
            raise ValueError("prime coefficient basis did not span")
        return basis
    beta = next(x for x in range(f.q) if x not in base)
    basis = (f.one, beta)
    made = {fa(f, a, fm(f, b, beta)) for a in base for b in base}
    if len(made) != f.q:
        raise ValueError("quadratic subfield basis did not span uniquely")
    return basis


def mod_rank(matrix, p=3):
    if not matrix:
        return 0
    a = [[x % p for x in row] for row in matrix]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv*x) % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                z = a[i][col]
                a[i] = [(x-z*y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def gram_restricted(rank, trace):
    f = field(3)
    ebasis = basis_over_subfield(f, (0, 1, 2))
    labels = []
    for half in range(2):
        for coordinate in range(rank):
            for scalar in ebasis:
                a, b = [0]*rank, [0]*rank
                (a if half == 0 else b)[coordinate] = scalar
                labels.append((tuple(a), tuple(b)))
    def omega(v, w):
        a, b = v
        c, d = w
        return fsum(f, (fa(f, fm(f, x, y), fn(f, fm(f, z, q)))
                         for x, y, z, q in zip(a, d, c, b)))
    return tuple(tuple(trace(omega(v, w)) for w in labels) for v in labels)


def gate_a1(mode):
    f = field(3)
    ok, message = f.audit()
    need("A1", ok, message)
    actual_trace = trace27_degree if mode == "trace-degree" else trace27
    image = {actual_trace(x) for x in range(27)}
    fibers = Counter(actual_trace(x) for x in range(27))
    witness = next((x for x in range(27) if actual_trace(x) == 1), None)
    need("A1", image == {0, 1, 2} and fibers == Counter({0: 9, 1: 9, 2: 9}) and
         actual_trace(f.one) == 0 and witness is not None,
         "F27/F3 trace image/kernel/fibers or trace-one witness failed")
    ranks = []
    for rank in (0, 1, 2):
        gram = gram_restricted(rank, trace27)
        ranks.append((len(gram), mod_rank(gram)))
    need("A1", tuple(ranks) == ((0, 0), (6, 6), (12, 12)),
         "restricted F27/F3 symplectic Gram ranks are not 0,6,12")
    return "F27 trace image 3/kernel 9/fibers 9; Gram ranks 0,6,12"


def gate_a2(mode):
    f, base = field(4), base81()
    ok, message = f.audit()
    need("A2", ok and len(base) == 9, message)
    canonical = chi9
    actual = (lambda y: f.TR[y]) if mode == "character-conflation" else canonical
    for x, y in itertools.product(base, repeat=2):
        need("A2", actual(fa(f, x, y)) == (actual(x)+actual(y)) % 3,
             "named F9 character is not additive")
    witness = next((x for x in base if canonical(x) != f.TR[x]), None)
    need("A2", set(actual(x) for x in base) == {0, 1, 2} and witness is not None and
         actual(witness) == canonical(witness) and actual(witness) != f.TR[witness],
         "nonstandard F9 character was conflated with the fixed absolute character")
    need("A2", set(actual(trace81_9(x)) for x in range(81)) == {0, 1, 2},
         "relative character on F81 is trivial")
    f27 = field(3)
    need("A2", {f27.TR[x] for x in (0, 1, 2)} == {0} and {x for x in (0, 1, 2)} == {0, 1, 2},
         "F27 restricted absolute character/base character boundary failed")
    return "nonstandard F9 character and F81 composite separated; F27 restriction trivial"


def gate_a3(mode):
    f = field(4)
    wrong = mode == "tower-order"
    for x in range(81):
        middle = trace81_9(x, wrong=wrong)
        direct = trace81_3_direct(x)
        need("A3", middle in base81() and trace9_3(middle) == direct,
             "F3/F9/F81 trace routes disagree or wrong stage misses F9")
        direct_character = trace81_3_direct(fm(f, parameter9(), x))
        need("A3", chi9(middle) == direct_character,
             "tower character routes disagree")
    return "81 direct/iterated trace and nonstandard-character comparisons"


def label_zero(rank):
    return (tuple(0 for _ in range(rank)), tuple(0 for _ in range(rank)))


def label_add(f, v, w):
    return (tuple(fa(f, x, y) for x, y in zip(v[0], w[0])),
            tuple(fa(f, x, y) for x, y in zip(v[1], w[1])))


def label_neg(f, v):
    return tuple(tuple(fn(f, x) for x in half) for half in v)


def omega_label(f, v, w):
    return fsum(f, (fa(f, fm(f, a, d), fn(f, fm(f, c, b)))
                    for a, b, c, d in zip(v[0], v[1], w[0], w[1])))


def label_basis(rank, ebasis):
    out = []
    for half in range(2):
        for coordinate in range(rank):
            for scalar in ebasis:
                a, b = [0]*rank, [0]*rank
                (a if half == 0 else b)[coordinate] = scalar
                out.append((tuple(a), tuple(b)))
    return tuple(out)


def label_samples(f, rank, ebasis):
    base = [label_zero(rank)] + list(label_basis(rank, ebasis))
    if rank:
        values = tuple(dict.fromkeys((f.one,) + ebasis + tuple(range(min(f.q, 5)))))
        for k in range(min(4, len(values))):
            a = tuple(values[(k+i) % len(values)] for i in range(rank))
            b = tuple(values[(2*k+i+1) % len(values)] for i in range(rank))
            base.append((a, b))
    return tuple(dict.fromkeys(base))


def weyl_action(f, char, label, state):
    a, b = label
    half = 2
    out = tuple(fa(f, y, x) for y, x in zip(state, a))
    terms = []
    for ai, bi, zi in zip(a, b, out):
        terms.append(fa(f, fn(f, fm(f, bi, zi)), fm(f, half, fm(f, ai, bi))))
    return out, char(fsum(f, terms)) % 3


def actual_trace_counts(f, char, label):
    counts = [0, 0, 0]
    for state in itertools.product(range(f.q), repeat=len(label[0])):
        out, exponent = weyl_action(f, char, label, state)
        if out == state:
            counts[exponent] += 1
    return tuple(counts)


def extension_cases():
    f27 = field(3)
    f81 = field(4)
    return (
        ("F27/F3", f27, (0, 1, 2), basis_over_subfield(f27, (0, 1, 2)),
         trace27, lambda x: x % 3, lambda x: trace27(x)),
        ("F81/F9", f81, base81(), basis_over_subfield(f81, base81()),
         trace81_9, chi9, chi81_relative),
    )


def gate_a4(mode):
    comparisons = 0
    for name, f, base, ebasis, trace, base_char, relative_char in extension_cases():
        for rank in (0, 1, 2):
            labels = label_samples(f, rank, ebasis)
            for v, w in itertools.product(labels, repeat=2):
                value = omega_label(f, v, w)
                left = relative_char(fm(f, 2, value))
                traced = trace(value)
                right_value = traced if mode == "half-form-trace" else fm(f, 2, traced)
                right = base_char(right_value)
                need("A4", left == right,
                     "%s rank-%d half-form trace exponent mismatch" % (name, rank))
                comparisons += 1
            states = list(itertools.product(range(f.q), repeat=rank))
            probes = states if rank < 2 else states[:min(12, len(states))]
            for v in labels:
                neg = label_neg(f, v)
                for state in probes:
                    z, e = weyl_action(f, relative_char, v, state)
                    back, d = weyl_action(f, relative_char, neg, z)
                    need("A4", back == state and (e+d) % 3 == 0,
                         "%s sparse Weyl star failed" % name)
                counts = actual_trace_counts(f, relative_char, v)
                if v == label_zero(rank):
                    need("A4", counts == (f.q ** rank, 0, 0),
                         "%s zero-label actual trace/unit failed" % name)
                else:
                    need("A4", counts[0] == counts[1] == counts[2],
                         "%s nonzero-label actual cyclotomic trace failed" % name)
            pair_labels = labels[:min(8, len(labels))]
            for v, w in itertools.product(pair_labels, repeat=2):
                target = label_add(f, v, w)
                cocycle = relative_char(fm(f, 2, omega_label(f, v, w)))
                for state in probes:
                    z, ew = weyl_action(f, relative_char, w, state)
                    zz, ev = weyl_action(f, relative_char, v, z)
                    expected_z, expected_e = weyl_action(f, relative_char, target, state)
                    need("A4", zz == expected_z and (ew+ev) % 3 == (cocycle+expected_e) % 3,
                         "%s sparse half-form product failed" % name)
    return "%d half-form exponent pairs plus sparse product/star/unit/trace" % comparisons


def frobenius_cases(mode=None):
    return (("F27/F3", field(3), (0, 1, 2), trace27, lambda x: x % 3, 3, 3),
            ("F81/F9", field(4), base81(), trace81_9, chi9,
             3 if mode == "absolute-frobenius" else 9, 2))


def gate_a5(mode):
    for name, f, base, trace, char, power, order in frobenius_cases(mode):
        sigma = lambda x: f.pow(x, power)
        for k in base:
            for x in range(f.q):
                need("A5", sigma(fm(f, k, x)) == fm(f, k, sigma(x)),
                     "%s relative Frobenius is not K-linear" % name)
        for x in range(f.q):
            need("A5", trace(sigma(x)) == trace(x) and char(trace(sigma(x))) == char(trace(x)),
                 "%s trace/character is not relative-Frobenius invariant" % name)
            y = x
            for _ in range(order):
                y = sigma(y)
            need("A5", y == x, "%s declared Frobenius power is not identity" % name)
        ebasis = basis_over_subfield(f, base)
        labels = label_samples(f, 1, ebasis)
        for v, w in itertools.product(labels, repeat=2):
            sv = tuple(tuple(sigma(x) for x in half) for half in v)
            sw = tuple(tuple(sigma(x) for x in half) for half in w)
            need("A5", omega_label(f, sv, sw) == sigma(omega_label(f, v, w)),
                 "%s Frobenius is not symplectic-semilinear" % name)
    return "F27 cube/order3 and F81 ninth-power/order2 K-linearity/invariance"


def covariance_case(name, f, ebasis, char, power, order, mode):
    sigma = lambda x: f.pow(x, power)
    inverse = lambda x: f.pow(x, power ** (order-1))
    rank_counts = []
    for rank in (1, 2):
        labels = (tuple(itertools.product(range(f.q), repeat=2)) if rank == 1 else
                  label_samples(f, rank, ebasis))
        if rank == 1:
            labels = tuple(((a,), (b,)) for a, b in labels)
        states = tuple(itertools.product(range(f.q), repeat=rank))
        if mode == "covariance-census-loss" and name == "F81/F9" and rank == 2:
            states = states[:-1]
        need("A6", len(states) > 0,
             "%s rank-%d covariance state census is empty" % (name, rank))
        comparisons = 0
        for state in states:
            pre = tuple(inverse(y) for y in state)
            for label in labels:
                z, exponent = weyl_action(f, char, label, pre)
                actual = tuple(sigma(x) for x in z), exponent
                a = tuple(sigma(x) for x in label[0])
                b = (label[1] if mode == "half-coordinate" else
                     tuple(sigma(x) for x in label[1]))
                expected = weyl_action(f, char, (a, b), state)
                need("A6", actual == expected,
                     "%s rank-%d sparse Frobenius covariance failed" % (name, rank))
                comparisons += 1
        rank_counts.append(comparisons)
    return tuple(rank_counts)


def gate_a6(mode):
    f27, f81 = field(3), field(4)
    observed = covariance_case("F27/F3", f27, basis_over_subfield(f27, (0, 1, 2)),
                               trace27, 3, 3, mode)
    observed += covariance_case("F81/F9", f81, basis_over_subfield(f81, base81()),
                                chi81_relative, 9, 2, mode)
    expected = (19683, 12393, 531441, 85293)
    need("A6", observed == expected,
         "A6 covariance census %s, expected per-field/rank %s" % (observed, expected))
    total = sum(observed)
    return "%d exhaustive-rank1/sparse-rank2 monomial covariance cases" % total


def tuple_index(values, q):
    out = 0
    for value in values:
        out = out*q + value
    return out


def gate_a7(mode):
    zero_basis = tuple(range(3)) if mode == "rank-zero" else ((),)
    zero_perm = tuple(range(len(zero_basis)))
    need("A7", len(zero_basis) == 1 and zero_perm == (0,),
         "rank-zero empty tensor is not the identity channel on C")
    checks = 0
    for name, f, _, _, _, power, order in frobenius_cases():
        sigma = lambda x: f.pow(x, power)
        inverse = lambda x: f.pow(x, power ** (order-1))
        for rank in (1, 2):
            basis = tuple(itertools.product(range(f.q), repeat=rank))
            perm = tuple(tuple(sigma(x) for x in state) for state in basis)
            need("A7", len(set(perm)) == len(basis), "%s rank-%d permutation not bijective" % (name, rank))
            for state in basis:
                y = state
                for _ in range(order):
                    y = tuple(sigma(x) for x in y)
                need("A7", y == state and tuple(inverse(sigma(x)) for x in state) == state,
                     "%s permutation period/inverse failed" % name)
            sample = tuple(range(min(8, len(basis))))
            for i, j in itertools.product(sample, repeat=2):
                pi, pj = basis.index(perm[i]), basis.index(perm[j])
                need("A7", (i == j) == (pi == pj),
                     "%s unitary channel did not preserve ordinary matrix-unit trace" % name)
                checks += 1
    return "rank-zero identity plus %d rank1/2 permutation-channel controls" % checks


def omega_f3(v, w):
    half = len(v)//2
    return sum(v[i]*w[half+i]-w[i]*v[half+i] for i in range(half)) % 3


def jmap(u, bad=False):
    a, b = u
    return (a, b, 0, 0) if bad else (a, a, b, 0)


def kmap(w):
    u, v = w
    return (0, u, -v % 3, v)


def gate_a8(mode):
    labels = Abelian((3, 3), 3).elements
    j = lambda u: jmap(u, bad=(mode == "degenerate-subsystem"))
    need("A8", len({j(u) for u in labels}) == 9 and len({kmap(w) for w in labels}) == 9,
         "subsystem maps are not injective")
    for u, v in itertools.product(labels, repeat=2):
        need("A8", omega_f3(j(u), j(v)) == omega_f3(u, v),
             "non-coordinate subsystem injection is not symplectic")
        need("A8", omega_f3(kmap(u), kmap(v)) == omega_f3(u, v),
             "complement injection is not symplectic")
        need("A8", omega_f3(j(u), kmap(v)) == 0,
             "subsystem and complement are not orthogonal")
    sums = {tuple((a+b) % 3 for a, b in zip(j(u), kmap(w)))
            for u in labels for w in labels}
    need("A8", len(sums) == 81, "subsystem/complement sum is not unique and onto V2")
    return "non-coordinate j,k symplectic/orthogonal/injective with 81 unique sums"


def qzero(n, m):
    return tuple(tuple(F(0) for _ in range(m)) for _ in range(n))


def qeye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def qunit(n, m, i, j):
    return tuple(tuple(F((r, c) == (i, j)) for c in range(m)) for r in range(n))


def qadd(a, b):
    return tuple(tuple(x+y for x, y in zip(ra, rb)) for ra, rb in zip(a, b))


def qscale(c, a):
    return tuple(tuple(F(c)*x for x in row) for row in a)


def qmul(a, b):
    out = [[F(0) for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):
                out[i][j] += a[i][k]*b[k][j]
    return tuple(tuple(row) for row in out)


def qdag(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))


def qkron(a, b):
    return tuple(tuple(a[i//len(b)][j//len(b[0])] * b[i%len(b)][j%len(b[0])]
                       for j in range(len(a[0])*len(b[0])))
                 for i in range(len(a)*len(b)))


def qtrace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def basis_tuples(rank):
    return tuple(itertools.product(range(3), repeat=rank))


def permutation(rank, transform):
    basis = basis_tuples(rank)
    index = {x: i for i, x in enumerate(basis)}
    return tuple(index[transform(x)] for x in basis)


def j2_perm():
    return permutation(2, lambda x: (x[0], (x[0]+x[1]) % 3))


def pull_matrix(rho, perm):
    return tuple(tuple(rho[perm[i]][perm[j]] for j in range(len(perm)))
                 for i in range(len(perm)))


def push_matrix(rho, perm):
    inv = [0]*len(perm)
    for i, j in enumerate(perm):
        inv[j] = i
    return tuple(tuple(rho[inv[i]][inv[j]] for j in range(len(perm)))
                 for i in range(len(perm)))


def partial_trace2(rho, retain=0):
    out = [[F(0) for _ in range(3)] for _ in range(3)]
    for x, y in itertools.product(range(3), repeat=2):
        for e in range(3):
            row = (x, e) if retain == 0 else (e, x)
            col = (y, e) if retain == 0 else (e, y)
            out[x][y] += rho[tuple_index(row, 3)][tuple_index(col, 3)]
    return tuple(tuple(row) for row in out)


def decoder_kraus():
    perm = j2_perm()
    rows = []
    for e in range(3):
        operator = [[F(0) for _ in range(9)] for _ in range(3)]
        for x in range(3):
            factor_index = tuple_index((x, e), 3)
            operator[x][perm[factor_index]] = F(1)
        rows.append(tuple(tuple(row) for row in operator))
    return tuple(rows)


def decode_kraus(rho, normalized=False):
    out = qzero(3, 3)
    for operator in decoder_kraus():
        out = qadd(out, qmul(operator, qmul(rho, qdag(operator))))
    return qscale(F(1, 3), out) if normalized else out


def decode_index(rho, retain=0):
    return partial_trace2(pull_matrix(rho, j2_perm()), retain=retain)


def iota(a):
    return push_matrix(qkron(a, qeye(3)), j2_perm())


def hs(a, b):
    return qtrace(qmul(qdag(a), b))


def weyl_f3(label, state):
    a, b = label
    out = (state+a) % 3
    exponent = (-b*out + 2*a*b) % 3
    return out, exponent


def gate_a9(mode):
    labels = tuple(itertools.product(range(3), repeat=2))
    mono_field = MonoGF(3, 1)
    for label in labels:
        imported = weyl_mono(mono_field, lambda x: x, label)
        for state in range(3):
            ours = weyl_f3(label, state)
            need("A9", ours == (imported[0][state], imported[1][state]),
                 "imported F3 monomial Weyl convention disagrees")
    for u, w, state in itertools.product(labels, labels, basis_tuples(2)):
        inv = (state[0], (state[1]-state[0]) % 3)
        x, eu = weyl_f3(u, inv[0])
        y, ew = weyl_f3(w, inv[1])
        actual = (x, (x+y) % 3), (eu+ew) % 3
        combined = tuple((a+b) % 3 for a, b in zip(jmap(u), kmap(w)))
        a = combined[:2]
        b = combined[2:]
        target = tuple((state[i]+a[i]) % 3 for i in range(2))
        exponent = sum(-b[i]*target[i]+2*a[i]*b[i] for i in range(2)) % 3
        need("A9", actual == (target, exponent), "J failed a Weyl compatibility action")
    complete = qzero(9, 9)
    for operator in decoder_kraus():
        complete = qadd(complete, qmul(qdag(operator), operator))
    need("A9", complete == qeye(9), "decoder Kraus rows are incomplete")
    for i, j in itertools.product(range(9), repeat=2):
        rho = qunit(9, 9, i, j)
        actual = decode_kraus(rho, normalized=(mode == "decoder-normalized-trace"))
        expected = decode_index(rho)
        need("A9", actual == expected and qtrace(actual) == qtrace(rho),
             "ordinary decoder disagrees with index partial trace at E_(%d,%d)" % (i, j))
    for u, v in itertools.product(range(3), repeat=2):
        a = qunit(3, 3, u, v)
        for i, j in itertools.product(range(9), repeat=2):
            rho = qunit(9, 9, i, j)
            need("A9", hs(decode_kraus(rho), a) == hs(rho, iota(a)),
                 "decoder/inclusion ordinary-trace duality failed")
    return "729 Weyl actions, 81 decoder units, completeness/trace and 729 dualities"


def factor_states():
    product_state = qunit(9, 9, tuple_index((0, 1), 3), tuple_index((0, 1), 3))
    classical = qzero(9, 9)
    bell = qzero(9, 9)
    for x in range(3):
        idx = tuple_index((x, x), 3)
        classical = qadd(classical, qscale(F(1, 3), qunit(9, 9, idx, idx)))
        for y in range(3):
            jdx = tuple_index((y, y), 3)
            bell = qadd(bell, qscale(F(1, 3), qunit(9, 9, idx, jdx)))
    return product_state, classical, bell


def gate_a10(mode):
    transported = tuple(push_matrix(rho, j2_perm()) for rho in factor_states())
    actual = tuple(decode_index(rho, retain=1 if mode == "decoder-direction" else 0)
                   for rho in transported)
    expected = (qunit(3, 3, 0, 0), qscale(F(1, 3), qeye(3)),
                qscale(F(1, 3), qeye(3)))
    need("A10", actual == expected,
         "decoder traced the retained factor or corrupted correlated-state outputs")
    return "asymmetric product, classical correlation and Bell density decoder direction"


@dataclass(frozen=True)
class C3:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = cc(other)
        return C3(self.a+other.a, self.b+other.b)

    def __mul__(self, other):
        other = cc(other)
        return C3(self.a*other.a-self.b*other.b,
                  self.a*other.b+self.b*other.a-self.b*other.b)

    def conj(self):
        return C3(self.a-self.b, -self.b)


def cc(x=0):
    return x if isinstance(x, C3) else C3(F(x), F(0))


CZ = (C3(1, 0), C3(0, 1), C3(-1, -1))


def expectation(rho, rank, label):
    basis = basis_tuples(rank)
    total = C3()
    for i, state in enumerate(basis):
        out = []
        exponent = 0
        for coordinate in range(rank):
            z, e = weyl_f3((label[0][coordinate], label[1][coordinate]), state[coordinate])
            out.append(z)
            exponent += e
        j = basis.index(tuple(out))
        total = total + cc(rho[i][j]) * CZ[exponent % 3]
    return total


def cmat(matrix):
    return tuple(tuple(cc(x) for x in row) for row in matrix)


def cmul(a, b):
    out = [[C3() for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for k in range(len(b)):
            for j in range(len(b[0])):
                out[i][j] = out[i][j] + a[i][k]*b[k][j]
    return tuple(tuple(row) for row in out)


def cdag(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a))) for i in range(len(a[0])))


def cscale(z, a):
    return tuple(tuple(z*x for x in row) for row in a)


def perm_matrix(perm):
    return tuple(tuple(C3(1, 0) if i == perm[j] else C3()
                       for j in range(len(perm))) for i in range(len(perm)))


def gate_a11(mode):
    imported_ring = CycRing(3)
    need("A11", tuple(C3(F(x[0]), F(x[1])) for x in imported_ring.zpow[:3]) == CZ,
         "imported cyclotomic root convention disagrees with Eisenstein layer")
    states = tuple(push_matrix(rho, j2_perm()) for rho in factor_states())
    for rho in states:
        decoded = decode_index(rho)
        for a, b in itertools.product(range(3), repeat=2):
            left = expectation(decoded, 1, ((a,), (b,)))
            jlabel = jmap((a, b))
            right = expectation(rho, 2, (jlabel[:2], jlabel[2:]))
            need("A11", left == right, "Weyl characteristic restriction failed")
    jmat = perm_matrix(j2_perm())
    phased = cscale(CZ[1], jmat)
    test = cmat(qunit(9, 9, 1, 5))
    canonical = cmul(cdag(jmat), cmul(test, jmat))
    right_factor = jmat if mode == "decoder-phase" else phased
    actual = cmul(cdag(phased), cmul(test, right_factor))
    need("A11", actual == canonical, "overall phase did not cancel from decoder data")
    a = cmat(qunit(3, 3, 1, 2))
    ai = cmat(qkron(qunit(3, 3, 1, 2), qeye(3)))
    canonical_iota = cmul(jmat, cmul(ai, cdag(jmat)))
    actual_iota = cmul(phased, cmul(ai, cdag(phased)))
    need("A11", actual_iota == canonical_iota,
         "overall phase did not cancel from observable inclusion")
    return "27 Weyl-characteristic restrictions and exact J phase cancellation"


def direct3_perm():
    return permutation(3, lambda x: (x[0], (x[0]+x[1]) % 3,
                                      (x[0]+x[1]+x[2]) % 3))


def step1_perm():
    return permutation(3, lambda x: (x[0], (x[0]+x[1]) % 3, x[2]))


def step2_perm():
    return permutation(3, lambda x: (x[0], x[1], (x[1]+x[2]) % 3))


def compose_perm(after, before):
    return tuple(after[before[i]] for i in range(len(before)))


def partial_trace_last(rho, factors, retain=0):
    out = [[F(0) for _ in range(3)] for _ in range(3)]
    discarded = [i for i in range(factors) if i != retain]
    for x, y in itertools.product(range(3), repeat=2):
        for env in itertools.product(range(3), repeat=len(discarded)):
            row, col, k = [0]*factors, [0]*factors, 0
            row[retain], col[retain] = x, y
            for position in discarded:
                row[position] = col[position] = env[k]
                k += 1
            out[x][y] += rho[tuple_index(row, 3)][tuple_index(col, 3)]
    return tuple(tuple(row) for row in out)


def direct_decode3(rho, wrong=False):
    return partial_trace_last(pull_matrix(rho, direct3_perm()), 3, retain=1 if wrong else 0)


def sequential_decode3(rho):
    factor_after_step2 = pull_matrix(rho, step2_perm())
    middle = [[F(0) for _ in range(9)] for _ in range(9)]
    for a, b, c, d in itertools.product(range(3), repeat=4):
        for e in range(3):
            i, j = tuple_index((a, b), 3), tuple_index((c, d), 3)
            middle[i][j] += factor_after_step2[tuple_index((a, b, e), 3)][tuple_index((c, d, e), 3)]
    return partial_trace2(pull_matrix(tuple(tuple(row) for row in middle), j2_perm()))


def decode_unit3(row, col, wrong=False):
    perm = direct3_perm()
    inv = [0]*27
    for i, j in enumerate(perm):
        inv[j] = i
    r, c = basis_tuples(3)[inv[row]], basis_tuples(3)[inv[col]]
    retain = 1 if wrong else 0
    discarded = [i for i in range(3) if i != retain]
    if any(r[i] != c[i] for i in discarded):
        return qzero(3, 3)
    return qunit(3, 3, r[retain], c[retain])


def sequential_unit3(row, col):
    r, c = basis_tuples(3)[row], basis_tuples(3)[col]
    pre_r = (r[0], r[1], (r[2]-r[1]) % 3)
    pre_c = (c[0], c[1], (c[2]-c[1]) % 3)
    if pre_r[2] != pre_c[2]:
        return qzero(3, 3)
    first_r = (pre_r[0], (pre_r[1]-pre_r[0]) % 3)
    first_c = (pre_c[0], (pre_c[1]-pre_c[0]) % 3)
    if first_r[1] != first_c[1]:
        return qzero(3, 3)
    return qunit(3, 3, first_r[0], first_c[0])


def complement_route_perm():
    def j_perp(pair):
        return pair[0], (pair[0]+pair[1]) % 3
    def j_composite(u, pair):
        return u, (u+pair[0]) % 3, (u+pair[1]) % 3
    return permutation(3, lambda x: j_composite(x[0], j_perp(x[1:])))


def tower_states():
    basis = basis_tuples(3)
    product_state = qunit(27, 27, basis.index((0, 1, 2)), basis.index((0, 1, 2)))
    classical = qzero(27, 27)
    ghz = qzero(27, 27)
    for x in range(3):
        i = basis.index((x, x, x))
        classical = qadd(classical, qscale(F(1, 3), qunit(27, 27, i, i)))
        for y in range(3):
            j = basis.index((y, y, y))
            ghz = qadd(ghz, qscale(F(1, 3), qunit(27, 27, i, j)))
    return tuple(push_matrix(rho, direct3_perm()) for rho in
                 (product_state, classical, ghz))


def gate_a12(mode):
    direct = direct3_perm()
    staged = compose_perm(step2_perm(), step1_perm())
    need("A12", direct == staged, "M3 direct unitary is not the two-stage compatible route")
    right = complement_route_perm()
    need("A12", right == direct,
         "D1710 complement/reassociation route does not match direct J at phase one")
    for row, col in itertools.product(range(27), repeat=2):
        actual = decode_unit3(row, col, wrong=(mode == "decoder-tower-order"))
        expected = sequential_unit3(row, col)
        need("A12", actual == expected,
             "direct/iterated decoder mismatch at tower matrix unit E_(%d,%d)" % (row, col))
    for rho in tower_states():
        need("A12", direct_decode3(rho) == sequential_decode3(rho),
             "direct/iterated decoder mismatch on correlated tower state")
    return "explicit D1710 M3 compatibility, 729 matrix units and three tower states"


GATES = {"A1": gate_a1, "A2": gate_a2, "A3": gate_a3,
         "A4": gate_a4, "A5": gate_a5, "A6": gate_a6,
         "A7": gate_a7, "A8": gate_a8, "A9": gate_a9,
         "A10": gate_a10, "A11": gate_a11, "A12": gate_a12}


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
