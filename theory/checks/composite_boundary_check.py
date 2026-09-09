#!/usr/bin/env python3
"""Independent exact C1--C9 finite falsifiers, standalone standard library + NumPy."""

# Consolidated unchanged from finite_support.py
"""Independent exact finite arithmetic and sparse linear algebra for the checker.

No imports from authoritative or candidate implementations. A graph vector is
stored as its unnormalized rational orbit sum; its squared norm is carried
explicitly. Fourier kernels omit sqrt(|E|), restored in every probability.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import gcd


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def count_polynomial(n):
    result = {n: 1}
    for d in divisors(n)[:-1]:
        for k, a in count_polynomial(d).items():
            result[k] = result.get(k, 0) - a
    return {k: a for k, a in result.items() if a}


def count(n, t):
    return sum(a * t ** k for k, a in count_polynomial(n).items())


def phi(n):
    return sum(gcd(n, k) == 1 for k in range(1, n + 1))


class FiniteField:
    """Polynomial quotient, validated directly as a field at construction."""
    def __init__(self, p, polynomial):
        self.p, self.poly, self.r = p, tuple(polynomial), len(polynomial) - 1
        self.size = p ** self.r
        self.digits = [tuple((a // p ** k) % p for k in range(self.r))
                       for a in range(self.size)]
        self.plus = [[self.encode([x + y for x, y in zip(a, b)])
                      for b in self.digits] for a in self.digits]
        self.times = [[self.raw_product(a, b) for b in range(self.size)]
                      for a in range(self.size)]
        assert all(self.power(a, self.size - 1) == 1
                   for a in range(1, self.size)), "quotient is not a field"
        self.absolute_period = {}
        for orbit in self.orbits(1):
            self.absolute_period.update({a: len(orbit) for a in orbit})

    def encode(self, digits):
        return sum((a % self.p) * self.p ** k for k, a in enumerate(digits))

    def raw_product(self, a, b):
        coefficients = [0] * (2 * self.r - 1)
        for i, j in product(range(self.r), repeat=2):
            coefficients[i + j] += self.digits[a][i] * self.digits[b][j]
        for k in range(len(coefficients) - 1, self.r - 1, -1):
            lead = coefficients[k] % self.p
            for j, coefficient in enumerate(self.poly):
                coefficients[k - self.r + j] -= lead * coefficient
        return self.encode(coefficients[:self.r])

    def add(self, a, b):
        return self.plus[a][b]

    def neg(self, a):
        return self.encode([-v for v in self.digits[a]])

    def mul(self, a, b):
        return self.times[a][b]

    def power(self, a, exponent):
        result = 1
        for _ in range(exponent):
            result = self.mul(result, a)
        return result

    def frobenius(self, a, s=1):
        return self.power(a, self.p ** s)

    def orbits(self, s):
        unused, result = set(range(self.size)), []
        while unused:
            a = min(unused)
            orbit, b = [], a
            while b not in orbit:
                orbit.append(b)
                b = self.frobenius(b, s)
            assert b == a
            unused.difference_update(orbit)
            result.append(tuple(orbit))
        return result

    def trace(self, a):
        result = 0
        for k in range(self.r):
            result = self.add(result, self.frobenius(a, k))
        assert result < self.p
        return result

    def reference(self, t):
        values = []
        for a in range(self.size):
            d = self.absolute_period[a]
            numerator = t - 1 if d == 1 else count(d, t)
            denominator = self.p - 1 if d == 1 else count(d, self.p)
            values.append((Q(1) if a == 0 else Q(numerator, denominator)) / t ** self.r)
        return values

    def leading(self, a):
        if a == 0:
            return Q(0)
        d = self.absolute_period[a]
        return Q(phi(d), self.p - 1 if d == 1 else count(d, self.p))


PRESENTATIONS = {(2, 1): [0, 1], (2, 2): [1, 1, 1],
                 (2, 3): [1, 1, 0, 1], (2, 4): [1, 1, 0, 0, 1],
                 (3, 1): [0, 1], (3, 2): [1, 0, 1], (3, 3): [1, 2, 0, 1]}


def clean(vector):
    return {a: v for a, v in vector.items() if v != 0}


def scale(vector, factor):
    return clean({a: factor * v for a, v in vector.items()})


def difference(a, b):
    out = dict(a)
    for x, value in b.items():
        out[x] = out.get(x, 0) - value
    return clean(out)


def push(vector, function):
    out = defaultdict(Q)
    for a, value in vector.items():
        out[function(a)] += value
    return clean(out)


def average(vector, function, n):
    result = defaultdict(Q)
    for _ in range(n):
        for a, value in vector.items():
            result[a] += value / n
        vector = push(vector, function)
    return clean(result)


def dot(a, b):
    return sum(value.conjugate() * b.get(x, 0) for x, value in a.items())


def norm(a):
    return dot(a, a)


def projection(vector, basis):
    result = {}
    for w in basis:
        coefficient = dot(w, vector) / norm(w)
        for a, value in w.items():
            result[a] = result.get(a, 0) + value * coefficient
    return clean(result)


def rank(rows):
    rows = [[Q(x) for x in row] for row in rows]
    used = 0
    for col in range(len(rows[0])):
        pivot = next((j for j in range(used, len(rows)) if rows[j][col]), None)
        if pivot is None:
            continue
        rows[used], rows[pivot] = rows[pivot], rows[used]
        a = rows[used][col]
        rows[used] = [v / a for v in rows[used]]
        for j in range(len(rows)):
            if j != used:
                a = rows[j][col]
                rows[j] = [v - a * w for v, w in zip(rows[j], rows[used])]
        used += 1
        if used == len(rows):
            break
    return used


class Cyclotomic:
    """Exact Q[zeta_p]/(1+zeta_p+...+zeta_p^(p-1)), p prime."""
    def __init__(self, p, coefficients=0):
        self.p = p
        self.coefficients = (tuple(map(Q, coefficients))
                             if isinstance(coefficients, (list, tuple)) else
                             (Q(coefficients),) + (Q(0),) * (p - 2))

    @classmethod
    def root(cls, p, exponent):
        exponent %= p
        return cls(p, [-1] * (p - 1) if exponent == p - 1 else
                   [int(j == exponent) for j in range(p - 1)])

    def coerce(self, value):
        if isinstance(value, Cyclotomic):
            assert value.p == self.p
            return value
        return Cyclotomic(self.p, value)

    def __add__(self, value):
        value = self.coerce(value)
        return Cyclotomic(self.p, [a + b for a, b in
                                 zip(self.coefficients, value.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return Cyclotomic(self.p, [-a for a in self.coefficients])

    def __sub__(self, value):
        return self + -self.coerce(value)

    def __rsub__(self, value):
        return self.coerce(value) + -self

    def __mul__(self, value):
        value = self.coerce(value)
        c = [Q(0)] * self.p
        for i, j in product(range(self.p - 1), repeat=2):
            c[(i + j) % self.p] += self.coefficients[i] * value.coefficients[j]
        return Cyclotomic(self.p, [a - c[-1] for a in c[:-1]])

    __rmul__ = __mul__

    def __truediv__(self, value):
        return Cyclotomic(self.p, [a / value for a in self.coefficients])

    def conjugate(self):
        return sum((a * self.root(self.p, -i)
                    for i, a in enumerate(self.coefficients)), Cyclotomic(self.p))

    def __eq__(self, value):
        return self.coefficients == self.coerce(value).coefficients

    def __repr__(self):
        return str(tuple(map(str, self.coefficients)))


def embeddings(source, target):
    """Enumerate ALL images of the polynomial generator, including twists."""
    def evaluate(coefficients, root):
        result = 0
        for a in reversed(coefficients):
            result = target.add(target.mul(result, root), a)
        return result
    return [tuple(evaluate(a, root) for a in source.digits)
            for root in range(target.size) if evaluate(source.poly, root) == 0]

# Consolidated unchanged from graph_gates.py
"""Exact arithmetic graph, preparation, instrument, Fourier and trace probes."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import gcd


class Graph:
    def __init__(self, field, s):
        self.e, self.s, self.n = field, s, field.r // s
        self.orbits = field.orbits(s)
        self.basis, self.labels, self.support = [], [], {}
        for oi, orbit in enumerate(self.orbits):
            for k in range(len(orbit)):
                vector = {self.tuple(x, k): Q(1) for x in orbit}
                j = len(self.basis)
                self.basis.append(vector)
                self.labels.append((oi, len(orbit), k))
                for a in vector:
                    assert a not in self.support
                    self.support[a] = j

    def tuple(self, x, k):
        y = self.e.frobenius(x, self.s * k)
        return x, y, self.e.mul(x, y)

    def delta(self, a):
        return tuple(self.e.frobenius(x, self.s) for x in a)

    def multiplication(self, a, sign=1, corrupt=False):
        x, y, z = a
        value = self.e.mul(x, y)
        if corrupt and x == y == self.orbits[-1][0]:
            value = self.e.add(value, 1)
        return x, y, self.e.add(z, value if sign == 1 else self.e.neg(value))

    def relative(self, a):
        x, y, z = self.multiplication(a, -1)
        return self.multiplication((x, self.e.frobenius(y, self.s), z))

    def selected(self, d, k=None):
        return [w for w, (_, e, j) in zip(self.basis, self.labels)
                if e == d and (k is None or k == j)]


def graph_gates(c, graph):
    e, n, s = graph.e, graph.n, graph.s
    census = Counter(len(o) for o in graph.orbits)
    for d in divisors(n):
        c.check('C2', d * census[d] == count(d, e.p ** s), 'actual relative orbit census')
    cube_count = 0
    for a in product(range(e.size), repeat=3):
        cube_count += 1
        actual = graph.multiplication(a, corrupt=c.red == 'product')
        expected = (a[0], a[1], e.add(a[2], e.mul(a[0], a[1])))
        c.check('C2', actual == expected, 'one actual multiplication-table entry')
        delta = ((e.frobenius(a[0], s), a[1], e.frobenius(a[2], s))
                 if c.red == 'diagonal-action' else graph.delta(a))
        c.check('C2', (a in graph.support) == (delta in graph.support),
                'diagonal graph predicate commutes with simultaneous Frobenius')
        if a in graph.support:
            w = graph.basis[graph.support[a]]
            image = average({a: Q(1)}, graph.delta, n)
            c.check('C2', image == scale(w, Q(1, len(w))),
                    'actual graph predicate followed by full diagonal average')
    c.check('C2', len(graph.basis) == e.size, 'collective code dimension')
    action = (lambda a: a) if c.red == 'identity' else (
        graph.delta if c.red == 'diagonal-relative' else graph.relative)
    for i, (w, (oi, d, k)) in enumerate(zip(graph.basis, graph.labels)):
        c.check('C3', norm(w) == d and push(w, graph.delta) == w,
                'normalized graph norm and diagonal invariance')
        shifted = graph.labels.index((oi, d, (k + 1) % d))
        c.check('C3', push(w, action) == graph.basis[shifted], 'actual relative graph shift')
        for j, v in enumerate(graph.basis):
            c.check('C3', dot(w, v) == (d if i == j else 0), 'normalized graph Gram matrix')
        for a, b in product(range(d), repeat=2):
            value = projection(w, graph.selected(d, b))
            for _ in range((a - b) % d):
                value = push(value, graph.relative)
            value = projection(value, graph.selected(d, a))
            expected = graph.basis[graph.labels.index((oi, d, a))] if k == b else {}
            c.check('C3', value == expected, 'common matrix units on every orbit copy')
    # Separate invariant descent of two orbit registers versus assembled descent.
    for orbit in graph.orbits:
        d = len(orbit)
        relative = [{(x, e.frobenius(x, s*k)): Q(1) for x in orbit} for k in range(d)]
        separate = {(x, y): Q(1, d) for x, y in product(orbit, repeat=2)}
        if c.red == 'separate-descent':
            relative = [average(average(w, lambda a: (e.frobenius(a[0], s), a[1]), d),
                                lambda a: (a[0], e.frobenius(a[1], s)), d) for w in relative]
        c.check('C3', all(dot(a, b) == (d if i == j else 0)
                         for i, a in enumerate(relative) for j, b in enumerate(relative)),
                'collectively descended relative graph retains d independent quantum states')
        c.check('C3', norm(separate) == 1 and
                all(dot(w, separate) == 1 for w in relative),
                'independent fixed vector is uniform over d collective relative states')
    return {'p': e.p, 'r': e.r, 's': s, 'n': n, 'cube_tuples': cube_count,
            'orbit_counts': dict(census), 'code_dimension': len(graph.basis),
            'common_algebra_dimension': sum(d*d for d in census)}


def preparation_gates(c, graph):
    e, n, s = graph.e, graph.n, graph.s
    primitive = {x for o in graph.orbits if len(o) == n for x in o}
    q0, q1 = graph.selected(n, 0), graph.selected(n, 1)
    event_records = []
    for t in sorted({Q(1), Q(6, 5), Q(3, 2), Q(e.p)}):
        reference = e.reference(t)
        c.check('C4', sum(reference) == 1 and min(reference) >= 0, 'actual POS input state')
        primitive_mass = sum(reference[x] for x in primitive)
        success, average_failure = Q(0), Q(0)
        final = [Q(0), Q(0), Q(0)]
        full_fail, identity_fail, dephased_fail = Q(0), Q(0), Q(0)
        for x in primitive:
            copied = {graph.multiplication((x, x, 0)): Q(1)}
            projected = average(copied, graph.delta, n)
            c.check('C4', projected == projection(copied, q0), 'C followed by actual A_delta')
            input_weight = reference[x]
            if c.red == 'reset-reference':
                input_weight *= reference[x] * reference[e.mul(x, x)]
            event_mass = input_weight * norm(projected)
            success += event_mass
            average_failure += reference[x] * norm(difference(copied, projected))
            evolved = push(projected, graph.relative)
            if c.red == 'dephase':
                # Actual computational dephasing removes density cross terms.
                full_probability = sum(v*v*norm(projection({graph.relative(a): Q(1)}, q1))
                                       for a, v in projected.items())
            else:
                full_probability = norm(projection(evolved, q1))
            if c.red == 'normalizer':
                full_probability /= n
            final[0] += reference[x] * full_probability
            final[1] += reference[x] * norm(projection(projected, q1))
            identity_fail += reference[x] * norm(difference(projected, projection(projected, q1)))
            dephased = Q(0)
            for a, v in projected.items():
                atom = {graph.relative(a): Q(1)}
                if c.red == 'omit-invariant':
                    dephased += v*v*int(next(iter(atom)) in set().union(*(set(w) for w in q1)))
                else:
                    dephased += v*v*norm(projection(atom, q1))
                dephased_fail += reference[x]*v*v*norm(difference(atom, projection(atom, q1)))
            final[2] += reference[x] * dephased
            full_fail += reference[x] * norm(difference(evolved, projection(evolved, q1)))
        expected = count(n, t ** s) / (n * t ** e.r)
        c.check('C4', success == expected, 'copied one-reference preparation norm')
        histories = [1 - primitive_mass, average_failure, final[0], full_fail]
        if c.red == 'omit-outcome':
            histories = histories[1:]
        if t > 1:
            probabilities = [value / success for value in final]
            c.check('C5', probabilities == [Q(1), Q(0), Q(1, n)],
                    'full / identity / computational-dephased conditional probabilities')
        else:
            c.check('C4', final == [0, 0, 0], 'raw endpoint has zero success')
        c.check('C6', sum(histories) == 1, 'all primitive, averaging and final failure histories')
        c.check('C6', 1-primitive_mass+average_failure+final[1]+identity_fail == 1 and
                1-primitive_mass+average_failure+final[2]+dephased_fail == 1,
                'identity and dephased comparison instruments retain every outcome')
        event_records.append({'t': str(t), 'preparation': str(success),
                              'final_full_identity_dephased': list(map(str, final)),
                              'full_histories': list(map(str, histories))})
    leading = sum(e.leading(x) * norm(average({graph.tuple(x, 0): Q(1)}, graph.delta, n))
                  for x in primitive)
    if c.red == 'drop-grade':
        leading = Q(0)
    c.check('C4', leading == Q(s * phi(n), n), 'actual POS grade-one coefficient')
    # Directly compute every orbit-block reference weight, including d=1 and zero.
    for t in (Q(1), Q(6, 5), Q(e.p)):
        for d in divisors(n):
            weight = sum(e.reference(t)[x] / d for o in graph.orbits if len(o) == d for x in o)
            c.check('C4', weight == count(d, t ** s) / (d * t ** e.r),
                    'all copied-and-averaged block reference weights')
    for d in divisors(n)[1:]:
        actual = sum(e.leading(x) / d for o in graph.orbits if len(o) == d for x in o)
        c.check('C4', actual == Q(s * phi(d), d), 'moving-sector leading randomization weight')
    return {'events': event_records, 'leading': str(leading),
            'dephased_leading': str(leading / n)}


def fourier_gates(c, graph):
    e, n = graph.e, graph.n
    basis = graph.selected(n)
    phases = set()
    for w in basis:
        output = {}
        for (x, y, z), value in w.items():
            for a in range(e.size):
                sign = 1 if c.red == 'fourier-phase' else -1
                phase = Cyclotomic.root(e.p, sign * e.trace(e.mul(a, x)))
                key = (a, y, z)
                output[key] = output.get(key, 0) + value * phase
        projected = projection(output, basis)
        x = next(iter(w))[0]
        exponent = -e.trace(e.mul(x, x)) % e.p
        phases.add(exponent)
        expected_phase = Cyclotomic.root(e.p, exponent)
        c.check('C8', all(-e.trace(e.mul(a[0], a[0])) % e.p == exponent for a in w),
                'actual absolute-trace phase is orbit independent')
        c.check('C8', projected == scale(w, expected_phase), 'exact field Fourier compression phase')
        c.check('C8', norm(output) == e.size * norm(w), 'actual unscaled Fourier vector norm')
        success = norm(projected) / (e.size * norm(w))
        failure = norm(difference(output, projected)) / (e.size * norm(w))
        if c.red == 'fourier-outcome':
            failure = Cyclotomic(e.p, 0)
        c.check('C8', success == Q(1, e.size) and success + failure == 1,
                'Fourier return and actual ambient failure complete the instrument')
    return {'compressed_phase_exponents': sorted(phases), 'return': str(Q(1, e.size))}


def spectral_gates(c, graph):
    e, n = graph.e, graph.n
    permutation = [graph.basis.index(push(w, graph.relative)) for w in graph.basis]
    active = list(range(len(permutation)))
    if c.red == 'multiplicity':
        seen, active = set(), []
        for i, (oi, d, k) in enumerate(graph.labels):
            if (d, k) not in seen:
                seen.add((d, k))
                active.append(i)
    traces = []
    powers = list(range(len(permutation)))
    for j in range(e.size + 1):
        actual = sum(powers[i] == i for i in active)
        c.check('C9', actual == (e.p ** graph.s) ** gcd(n, j), 'ordinary implementer trace with orbit multiplicity')
        traces.append(actual)
        powers = [permutation[i] for i in powers]
    # Recover det(I-zR) from actual permutation traces via Newton recurrence.
    determinant = [Q(1)]
    for k in range(1, e.size + 1):
        determinant.append(-sum(traces[j] * determinant[k-j] for j in range(1, k+1)) / k)
    expected = [1]
    for d in divisors(n):
        for _ in range(count(d, e.p ** graph.s) // d):
            out = expected + [0] * d
            for j, a in enumerate(expected):
                out[j+d] -= a
            expected = out
    c.check('C9', determinant == expected, 'full determinant from actual trace recurrence')
    # On M_n matrix units, conjugation is the actual simultaneous pair shift.
    first_orbit = next(oi for oi, d, k in graph.labels if d == n)
    one_block = [graph.basis[graph.labels.index((first_orbit, n, k))] for k in range(n)]
    implementer = [one_block.index(push(w, graph.relative)) for w in one_block]
    channel = [(implementer[a], implementer[b]) for a, b in product(range(n), repeat=2)]
    common_traces, pure_expectations = [], []
    evolved = list(range(n))
    for j in range(n+1):
        common_traces.append(sum(evolved[k] == k for k in range(n)))
        pure_expectations.append(int(evolved[0] == 0))
        c.check('C9', common_traces[-1] == n * int(j % n == 0) and
                pure_expectations[-1] == int(j % n == 0),
                'common ordinary trace versus prepared-state implementer expectation')
        evolved = [implementer[k] for k in evolved]
    actual_channel_cycles, unused = [], set(product(range(n), repeat=2))
    while unused:
        start = min(unused)
        cycle, a = [], start
        while a not in cycle:
            cycle.append(a)
            a = channel[a[0] * n + a[1]]
        unused.difference_update(cycle)
        actual_channel_cycles.append(len(cycle))
    predicted_channel_cycles = [n] if c.red == 'channel-spectrum' else [n] * n
    c.check('C9', actual_channel_cycles == predicted_channel_cycles and len(implementer) == n,
            'channel has n copies of each root while implementer has one')
    # Uniform randomization of the actual relative orbit of |0><0| gives I_n/n.
    probability = [Q(0)] * n
    k = 0
    for _ in range(n):
        probability[k] += Q(1, n)
        k = implementer[k]
    c.check('C9', probability == [Q(1, n)] * n, 'retained relative-power randomization is tracial')
    return {'trace_powers_0_through_n': traces[:n+1],
            'common_block_traces': common_traces, 'prepared_pure_expectations': pure_expectations,
            'determinant_coefficients': list(map(str, determinant)),
            'implementer_root_multiplicity': 1, 'channel_root_multiplicity': n}

# Consolidated unchanged from comparison_gates.py
"""Exact composition controls, coherent sums, embeddings and J/V comparisons."""
from fractions import Fraction as Q
from itertools import permutations, product
from math import factorial
import numpy as np


def control_gates(c):
    dimensions = []
    for n in range(1, 5):
        group = list(permutations(range(n)))
        dimensions.append(len(group))
        compose = lambda a, b: tuple(a[b[i]] for i in range(n))
        c.check('C1', len(group) == factorial(n), 'actual permutation-basis group-algebra dimension')
        for a, b, d in product(group, repeat=3):
            c.check('C1', compose(compose(a, b), d) == compose(a, compose(b, d)),
                    'level-four and lower composition reassociation')
    # Actual permutation representation of S3, restricted by the sum-zero projector.
    matrices = []
    for permutation in permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=object)
        for i, j in enumerate(permutation):
            matrix[j, i] = Q(1)
        matrices.append(matrix)
    standard = np.eye(3, dtype=object) - np.full((3, 3), Q(1, 3), dtype=object)
    s1, s2 = matrices[2], matrices[1]  # (01), (12), respectively.
    c.check('C1', np.array_equal(s1 @ s1, np.eye(3)) and
            np.array_equal(s2 @ s2, np.eye(3)), 'actual adjacent exchange involutions')
    if c.red == 'collective':
        s2 = s1
    words = [standard, standard @ s1, standard @ s2, standard @ s1 @ s2]
    c.check('C1', rank([list(a.flat) for a in words]) == 4,
            'collective M2 matrix block versus local diagonal image')
    vector = np.array([Q(-2), Q(1), Q(1)], dtype=object)
    probability = Q(vector @ s1 @ vector, vector @ vector) ** 2
    c.check('C1', probability == Q(1, 4), 'standard-block actual 1/4 return')
    # Center of C[S3] has three class sums; dimensions 1^2+1^2+2^2=6.
    cycle_types = set()
    for permutation in permutations(range(3)):
        unseen, lengths = set(range(3)), []
        while unseen:
            a, orbit = min(unseen), []
            while a not in orbit:
                orbit.append(a)
                a = permutation[a]
            unseen.difference_update(orbit)
            lengths.append(len(orbit))
        cycle_types.add(tuple(sorted(lengths)))
    c.check('C1', len(cycle_types) == 3 and 1+1+4 == dimensions[2],
            'level-three scalar, scalar, M2 decomposition dimensions')
    # Actual coherent duplicate C⊕C has all rectangular Hom blocks.
    units = []
    for a, b in product(range(2), repeat=2):
        matrix = np.zeros((2, 2), dtype=object)
        if c.red != 'off-diagonal' or a == b:
            matrix[a, b] = Q(1)
        units.append(matrix)
    coherent_density = np.full((2, 2), Q(1, 2), dtype=object)
    tag_density = np.diag([Q(1, 2), Q(1, 2)])
    c.check('C6', rank([list(a.flat) for a in units]) == 4,
            'coherent duplicate retains actual rectangular off-diagonal Hom maps')
    c.check('C6', np.trace(coherent_density @ coherent_density) == 1 and
            np.trace(coherent_density @ tag_density) == Q(1, 2),
            'coherent duplicate versus classical tagged alternative return')
    return {'dimensions_n1_to_n4': dimensions, 'standard_return': str(probability),
            'coherent_return': '1', 'tagged_return': '1/2'}


def embedding_gates(c, fields):
    samples = [(2, 1, 2), (2, 1, 4), (2, 2, 4), (3, 1, 2), (3, 1, 3)]
    records = []
    for p, small, large in samples:
        lower, upper = fields[p, small], fields[p, large]
        for index, mapping in enumerate(embeddings(lower, upper)):
            c.check('C7', len(set(mapping)) == lower.size and all(
                mapping[lower.add(a, b)] == upper.add(mapping[a], mapping[b]) and
                mapping[lower.mul(a, b)] == upper.mul(mapping[a], mapping[b])
                for a, b in product(range(lower.size), repeat=2)),
                'actual embedding preserves field operations')
            g, h = Graph(lower, 1), Graph(upper, 1)
            map3 = lambda a: tuple(mapping[x] for x in a)
            if c.red == 'embedding':
                map3 = lambda a: (mapping[a[0]], mapping[a[1]], upper.add(mapping[a[2]], 1))
            for w, (oi, d, k) in zip(g.basis, g.labels):
                embedded = push(w, map3)
                target_period = (large if c.red == 'wrong-sector' and small > 1 and d == small else d)
                expected_basis = h.selected(target_period, k)
                c.check('C7', projection(embedded, expected_basis) == embedded,
                        'lower-period graph embeds into same upper period, including twists')
                c.check('C7', push(push(w, g.relative), map3) == push(embedded, h.relative),
                        'graph embedding intertwines actual relative unitary')
            for x in range(lower.size):
                c.check('C7', map3(g.tuple(x, 0)) == h.tuple(mapping[x], 0),
                        'copying-and-multiplication preparation embedding square')
            # The non-prime-base F4→F16 comparison uses sigma=x^4 on both sides.
            if small == 2 and large == 4:
                relative_lower, relative_upper = Graph(lower, 2), Graph(upper, 2)
                for w, (_, d, k) in zip(relative_lower.basis, relative_lower.labels):
                    embedded = push(w, map3)
                    c.check('C7', projection(embedded, relative_upper.selected(d, k)) == embedded and
                            push(push(w, relative_lower.relative), map3) ==
                            push(embedded, relative_upper.relative),
                            'non-prime-base embedding preserves relative graph and actual action')
            # Full averaging projector and its complementary outcome on every lower cube ket.
            for a in product(range(lower.size), repeat=3):
                vector = {a: Q(1)}
                image = {map3(a): Q(1)}
                good_lower = average(vector, g.delta, g.n)
                good_upper = average(image, h.delta, h.n)
                c.check('C7', push(good_lower, map3) == good_upper and
                        push(difference(vector, good_lower), map3) == difference(image, good_upper),
                        'both invariant measurement histories commute with embedding')
            # Actual trace fibres give BOTH unscaled field Fourier/J/V squares.
            inverse = {b: a for a, b in enumerate(mapping)}
            trace = []
            for x in range(upper.size):
                value = 0
                for j in range(large // small):
                    value = upper.add(value, upper.frobenius(x, small * j))
                trace.append(inverse[value])
            kap = upper.size // lower.size
            for a, x in product(range(lower.size), range(upper.size)):
                kernel = lambda f, u, v: Cyclotomic.root(f.p, -f.trace(f.mul(u, v)))
                c.check('C7', kernel(upper, x, mapping[a]) == kernel(lower, trace[x], a),
                        'actual negative-kernel Fourier times J equals V times lower Fourier')
                actual = sum((kernel(upper, x, y) for y in range(upper.size) if trace[y] == a),
                             Cyclotomic(p))
                expected = kap * kernel(lower, inverse[x], a) if x in inverse else Cyclotomic(p)
                c.check('C7', actual == expected, 'actual Fourier times V equals J times lower Fourier')
            for x in range(upper.size):
                # P_V=BB*/kap; physically orthogonal outcomes on every computational input.
                projected = {y: Q(1, kap) for y in range(upper.size) if trace[y] == trace[x]}
                c.check('C7', norm(projected) + norm(difference({x: Q(1)}, projected)) == 1,
                        'both actual trace-transfer decoder outcomes normalized')
            records.append({'p': p, 'degrees': [small, large], 'embedding_index': index,
                            'generator_images': list(mapping), 'trace_fibre_size': kap,
                            'relative_base_degrees_tested': [1, 2] if small == 2 else [1]})
    # All actual F2→F4→F16 embedding choices and all F16 automorphisms.
    f2, f4, f16 = fields[2, 1], fields[2, 2], fields[2, 4]
    tower_count = 0
    for a, b, u in product(embeddings(f2, f4), embeddings(f4, f16), embeddings(f16, f16)):
        composite = tuple(u[b[a[x]]] for x in range(f2.size))
        c.check('C7', composite in embeddings(f2, f16), 'all named twisted tower composites')
        for x in range(f4.size):
            direct = tuple(u[b[z]] for z in Graph(f4, 1).tuple(x, 1))
            actual = Graph(f16, 1).tuple(u[b[x]], 1)
            c.check('C7', direct == actual, 'twisted tower graph maps compose on every coefficient')
        tower_count += 1
    return {'embeddings': records, 'twisted_tower_paths': tower_count}

# Consolidated unchanged from composite_boundary_check.py
"""Independent exact C1--C9 finite falsifiers; no finite pass promotes a claim."""
import argparse
from collections import Counter
import json


MUTATIONS = {
    'collective': 'C1', 'product': 'C2', 'diagonal-action': 'C2',
    'identity': 'C3', 'diagonal-relative': 'C3', 'separate-descent': 'C3', 'drop-grade': 'C4',
    'reset-reference': 'C4', 'dephase': 'C5', 'omit-invariant': 'C5',
    'normalizer': 'C5', 'off-diagonal': 'C6', 'omit-outcome': 'C6',
    'embedding': 'C7', 'wrong-sector': 'C7', 'fourier-phase': 'C8',
    'fourier-outcome': 'C8', 'multiplicity': 'C9', 'channel-spectrum': 'C9',
}


class MathematicalFailure(Exception):
    def __init__(self, gate, detail):
        self.gate, self.detail = gate, detail
        super().__init__(f'{gate}: {detail}')


class Checks:
    def __init__(self, red):
        self.red, self.counts = red, Counter()

    def check(self, gate, condition, detail):
        self.counts[gate] += 1
        if not condition:
            raise MathematicalFailure(gate, detail)


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--red', nargs='?', const='collective', choices=sorted(MUTATIONS),
                        metavar='NAME', help='run a mutation; without NAME use collective')
    for mutation, gate in sorted(MUTATIONS.items()):
        parser.add_argument('--red-' + mutation, dest='red', action='store_const',
                            const=mutation, help=f'run the {mutation} mutation ({gate})')
    args = parser.parse_args()
    c = Checks(args.red)
    result = {'red': args.red, 'exact': True, 'floating_point_tolerance': None}
    try:
        result['control'] = control_gates(c)
        fields = {key: FiniteField(key[0], value) for key, value in PRESENTATIONS.items()}
        result['fibres'] = []
        for p, r, s in [(2, 2, 1), (3, 2, 1), (2, 4, 1),
                        (2, 4, 2), (3, 3, 1), (2, 3, 1)]:
            graph = Graph(fields[p, r], s)
            record = graph_gates(c, graph)
            record['preparation'] = preparation_gates(c, graph)
            record['fourier'] = fourier_gates(c, graph)
            record['spectral'] = spectral_gates(c, graph)
            result['fibres'].append(record)
        result['comparisons'] = embedding_gates(c, fields)
        result['status'] = 'PASS'
    except MathematicalFailure as error:
        result.update(status='FAIL', gate=error.gate, detail=error.detail)
    result['checks'] = dict(sorted(c.counts.items()))
    print(json.dumps(result, indent=2))
    return int(result['status'] == 'FAIL')


if __name__ == '__main__':
    raise SystemExit(main())
