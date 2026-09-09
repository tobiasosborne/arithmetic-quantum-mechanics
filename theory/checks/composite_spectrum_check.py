#!/usr/bin/env python3
"""Exact finite spectral-completion falsifiers; finite passes prove no infinite claim."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd
import json


MUTATIONS = {'corner-unit': 'S1', 'drop-divisor-weight': 'S2', 'reset-corner': 'S2',
             'identity': 'S3', 'central-dynamics': 'S3', 'density-factor': 'S4',
             'negative-density': 'S4', 'tail-exponent': 'S4', 'd1-subtraction': 'S5',
             'coprimality': 'S5', 'zero-moment': 'S6', 'channel-trace': 'S6',
             'negative-power': 'S6', 'tensor-cycle': 'S7'}
DEGREES, CUTOFFS, BETAS = (2, 3, 4, 6, 12), (2, 4, 8, 16, 32), (2, 3, 4)
MOMENTS = (-12, -6, -4, -3, -2, -1, 0, 1, 2, 3, 4, 6, 12)


class MathematicalFailure(Exception):
    def __init__(self, gate, detail):
        self.gate, self.detail = gate, detail


class Checks:
    def __init__(self, mutation):
        self.mutation, self.counts = mutation, Counter()

    def check(self, gate, condition, detail):
        self.counts[gate] += 1
        if not condition:
            raise MathematicalFailure(gate, detail)


def first_red(c):
    # F4=F2[a]/(a^2+a+1): Frobenius interchanges a and a+1.
    # Their POS first coefficients are each 1/2. Copy each label, then
    # average its two distinct graph tuples with actual rational amplitude 1/2.
    orbit = (2, 3)
    copies = {2: (2, 2, 3), 3: (3, 3, 2)}
    actual_weight = F(0)
    for x in orbit:
        vector = defaultdict(F)
        for y in (x, 5-x):
            vector[copies[y]] += F(1, 2)
        actual_weight += F(1, 2) * sum(a*a for a in vector.values())
    totient = sum(gcd(a, 2) == 1 for a in range(1, 3))
    expected = F(totient, 1 if c.mutation == 'drop-divisor-weight' else 2)
    c.check('S2', actual_weight == expected, 'actual copied F4 average requires phi(2)/2')
    return str(actual_weight)


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


def totient(n):
    return len([a for a in range(1, n+1) if gcd(a, n) == 1])


def period_polynomial(n):
    result = {n: 1}
    for d in divisors(n)[:-1]:
        for exponent, coefficient in period_polynomial(d).items():
            result[exponent] = result.get(exponent, 0) - coefficient
    return {k: a for k, a in result.items() if a}


def poly_remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def poly_gcd(a, b):
    while b:
        a, b = b, poly_remainder(a, b)
    return a


def quotient_product(a, b, modulus):
    result, top = 0, 1 << (modulus.bit_length()-1)
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & top:
            a ^= modulus
        b >>= 1
    return result


def irreducible(modulus, degree):
    x = 2
    for j in range(1, degree+1):
        x = quotient_product(x, x, modulus)
        if j <= degree//2 and poly_gcd(x ^ 2, modulus) != 1:
            return False
    return x == 2


class BinaryField:
    def __init__(self, degree):
        self.degree, self.size = degree, 1 << degree
        self.modulus = next(f for f in range(self.size+1, 2*self.size, 2)
                            if irreducible(f, degree))
        self.squares = [self.mul(x, x) for x in range(self.size)]
        self.orbits = self.relative_orbits(1)
        self.period = {x: len(orbit) for orbit in self.orbits for x in orbit}
        assert all(self.power(x, self.size-1) == 1 for x in range(1, self.size))

    def mul(self, a, b):
        return quotient_product(a, b, self.modulus)

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, a)
            a, exponent = self.mul(a, a), exponent >> 1
        return result

    def sigma(self, a, s=1):
        for _ in range(s):
            a = self.squares[a]
        return a

    def relative_orbits(self, s):
        unseen, result = set(range(self.size)), []
        while unseen:
            x, orbit = min(unseen), []
            while x not in orbit:
                orbit.append(x)
                x = self.sigma(x, s)
            unseen.difference_update(orbit)
            result.append(tuple(orbit))
        return result

    def evaluate(self, polynomial, x):
        result = 0
        for bit in reversed(range(polynomial.bit_length())):
            result = self.mul(result, x) ^ ((polynomial >> bit) & 1)
        return result


def adjoint(matrix):
    return {(b, a): x for (a, b), x in matrix.items()}


def multiply(a, b):
    result = defaultdict(F)
    rows = defaultdict(list)
    for (i, j), x in b.items():
        rows[i].append((j, x))
    for (i, k), x in a.items():
        for j, y in rows[k]:
            result[i, j] += x*y
    return {key: value for key, value in result.items() if value}


def identity(labels):
    return {(a, a): F(1) for a in labels}


def labels_of(blocks):
    return [(d, k) for d in blocks for k in range(d)]


def trace(matrix, density):
    return sum(density[a]*x for (a, b), x in matrix.items() if a == b)


def finite_weights(blocks):
    return {d: F(totient(d), d) for d in blocks}


def corner_gates(c, fields):
    algebra = {n: [d for d in divisors(n) if d > 1] for n in DEGREES}
    def include(matrix, n, m):
        result = dict(matrix)
        if c.mutation == 'corner-unit':
            result.update(identity(labels_of(set(algebra[m])-set(algebra[n]))))
        return result
    inclusions = []
    for n, m in product(DEGREES, repeat=2):
        if m % n:
            continue
        lower, upper = labels_of(algebra[n]), labels_of(algebra[m])
        c.check('S1', include({}, n, m) == {}, 'nonunital corner inclusion is linear at zero')
        corner = include(identity(lower), n, m)
        c.check('S1', multiply(corner, corner) == corner and
                len(corner) == len(lower), 'embedded identity is exactly the lower divisor corner')
        for d in algebra[n]:
            for a, b, k in product(range(d), repeat=3):
                x, y = {((d, a), (d, b)): F(1)}, {((d, b), (d, k)): F(1)}
                c.check('S1', include(multiply(x, y), n, m) ==
                        multiply(include(x, n, m), include(y, n, m)) and
                        include(adjoint(x), n, m) == adjoint(include(x, n, m)),
                        'actual corner matrix-unit product and dagger')
        for large in DEGREES:
            if large % m == 0:
                c.check('S1', include(include(identity(lower), n, m), m, large) ==
                        include(identity(lower), n, large), 'divisor-corner compositions')
                for d in algebra[n]:
                    for a, b in product(range(d), repeat=2):
                        unit = {((d, a), (d, b)): F(1)}
                        c.check('S1', include(include(unit, n, m), m, large) ==
                                include(unit, n, large), 'every corner matrix unit composes through each divisor tower')
        wn, wm = finite_weights(algebra[n]), finite_weights(algebra[m])
        theta_n, theta_m = sum(wn.values()), sum(wm.values())
        upper_density = {(d, k): wm[d]/(theta_m*d) for d, k in upper}
        actual_mass = trace(corner, upper_density)
        if c.mutation == 'reset-corner' and n != m:
            actual_mass = F(1)
        c.check('S2', actual_mass == theta_n/theta_m, 'normalized upper reference conditions with theta_N/theta_M')
        for d, k in lower:
            c.check('S2', wm[d]/d == wn[d]/d and
                    upper_density[d, k]/actual_mass == wn[d]/(theta_n*d),
                    'unnormalized trace restriction and conditional corner density')
        inclusions.append({'N': n, 'M': m, 'success': str(actual_mass)})
    arithmetic, embedding_maps = [], {}
    for n, m in product(DEGREES, repeat=2):
        if n >= m or m % n:
            continue
        lower, upper = fields[n], fields[m]
        roots = [x for x in range(upper.size) if upper.evaluate(lower.modulus, x) == 0]
        c.check('S1', len(roots) == n, 'all polynomial-generator embeddings actually enumerated')
        embedding_maps[n, m] = []
        target = {x for x in range(upper.size) if n % upper.period[x] == 0}
        for root in roots:
            mapping = [upper.evaluate(x, root) for x in range(lower.size)]
            embedding_maps[n, m].append(tuple(mapping))
            c.check('S1', set(mapping) == target and len(set(mapping)) == lower.size,
                    'whole upper period-dividing-N label set is the named encoder image')
            for a, b in product(range(lower.size), repeat=2):
                c.check('S1', mapping[lower.mul(a, b)] == upper.mul(mapping[a], mapping[b]),
                        'actual finite-field multiplication embedding')
            for orbit in lower.orbits:
                for k in range(len(orbit)):
                    actual, expected = set(), set()
                    for x in orbit:
                        y = lower.sigma(x, k)
                        actual.add((mapping[x], mapping[y], mapping[lower.mul(x, y)]))
                        z = upper.sigma(mapping[x], k)
                        expected.add((mapping[x], z, upper.mul(mapping[x], z)))
                    c.check('S1', actual == expected and len(actual) == len(orbit),
                            'whole normalized multiplication-graph orbit vector embeds')
            for d in algebra[n]:
                c.check('S1', {mapping[x] for x in range(lower.size) if lower.period[x] == d} ==
                        {x for x in range(upper.size) if upper.period[x] == d},
                        'every upper length-d orbit already belongs to the lower field')
        arithmetic.append({'N': n, 'M': m, 'generator_roots': roots})
    tower_paths = 0
    for n, m, large in product(DEGREES, repeat=3):
        if not (n < m < large and m % n == 0 and large % m == 0):
            continue
        for left, right in product(embedding_maps[n, m], embedding_maps[m, large]):
            composite = tuple(right[left[x]] for x in range(fields[n].size))
            c.check('S1', composite in embedding_maps[n, large],
                    'actual polynomial-generator embeddings compose through every named tower path')
            tower_paths += 1
    return {'corners': inclusions, 'arithmetic_embeddings': arithmetic, 'arithmetic_tower_paths': tower_paths}


def derived_weight_gates(c, fields):
    records = []
    for n, s in [(n, 1) for n in DEGREES] + [(4, 2)]:
        field, weights = fields[n], defaultdict(F)
        period_counts = Counter(field.period.values())
        derivatives = {d: sum(k*a for k, a in period_polynomial(d).items()) for d in divisors(n)}
        for d in divisors(n):
            expected_count = sum(a*2**k for k, a in period_polynomial(d).items())
            c.check('S2', period_counts[d] == expected_count and derivatives[d] == totient(d),
                    'actual absolute-period census and independent coprime derivative count')
        for orbit in field.relative_orbits(s):
            if len(orbit) == 1:
                continue
            for x in orbit:
                d = field.period[x]
                coefficient = F(derivatives[d], period_counts[d])
                copied, vector = (x, x, field.mul(x, x)), defaultdict(F)
                for _ in range(n//s):
                    vector[copied] += F(s, n)
                    copied = tuple(field.sigma(a, s) for a in copied)
                weights[len(orbit)] += coefficient*sum(a*a for a in vector.values())/s
        for d, actual in weights.items():
            expected = F(totient(d), 1 if c.mutation == 'drop-divisor-weight' else d)
            c.check('S2', actual == expected, 'actual copied-reference grade divided by base degree gives phi(d)/d')
            randomized = defaultdict(F)
            k = 0
            shift = [(a+1) % d for a in range(d)]
            for _ in range(d):
                randomized[k, k] += F(1, d)
                k = shift[k]
            c.check('S2', dict(randomized) == {(a, a): F(1, d) for a in range(d)},
                    'explicit relative-power randomization supplies normalized block trace')
        records.append({'absolute_degree': n, 'base_degree': s,
                        'modulus_binary': bin(field.modulus), 'period_counts': dict(period_counts),
                        'derived_weights': {d: str(value) for d, value in sorted(weights.items())}})
    return records


def dynamics_gates(c):
    records = []
    for d in range(2, 17):
        shift = [(k+1) % d for k in range(d)]
        if c.mutation in ('identity', 'central-dynamics'):
            shift = list(range(d))
        before, after = {(0, 0): F(1)}, {(shift[0], shift[0]): F(1)}
        difference = {k: after.get((k, k), 0)-before.get((k, k), 0) for k in range(d)}
        displacement = max(abs(x) for x in difference.values())
        c.check('S3', displacement == 1, 'actual Frobenius displaces rank-one test by operator norm one')
        extended = [F(0)]*5 + list(difference.values()) + [F(0)]*7
        c.check('S3', max(map(abs, extended)) == 1, 'rank-one displacement persists under finite direct-sum extension')
        for a, b in product(range(d), repeat=2):
            x = {(a, b): F(1)}
            inverse = {shift[k]: k for k in range(d)}
            transformed = {(shift[a], shift[b]): F(1)}
            c.check('S3', {(inverse[i], inverse[j]): v for (i, j), v in transformed.items()} == x,
                    'actual cyclic conjugation has an exact inverse on matrix units')
            for beta in BETAS:
                central = {(k, k): F(1, d**beta) for k in range(d)}
                phase = {(k, k): F((-1)**d) for k in range(d)}
                c.check('S3', multiply(central, x) == multiply(x, central) and
                        multiply(multiply(phase, x), adjoint(phase)) == x,
                        'degree-weight operator is central and central unitary conjugation is trivial')
        records.append({'d': d, 'rank_one_displacement_norm': str(displacement)})
    return records


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1)**j*matrix[0][j]*determinant(
        [row[:j]+row[j+1:] for row in matrix[1:]]) for j in range(len(matrix)))


def beta_density(c, cutoff, beta):
    blocks = list(range(2, cutoff+1))
    weights = finite_weights(blocks)
    z = sum(weights[d]*F(1, d**beta) for d in blocks)
    exponent = beta+1 if c.mutation == 'density-factor' else beta+2
    density = {(d, k): F(totient(d), d**exponent)/z for d, k in labels_of(blocks)}
    if c.mutation == 'negative-density':
        density[2, 0] *= -1
    c.check('S4', min(density.values()) > 0, 'finite ordinary density has strictly positive eigenvalues')
    c.check('S4', sum(density.values()) == 1, 'finite beta density normalized in ordinary Hilbert trace')
    c.check('S4', all(density[d, k] == density[d, (k+1) % d] for d, k in density),
            'finite state is invariant under the actual block cyclic permutation')
    return z, density


def beta_gates(c):
    records = []
    for cutoff, beta in product(CUTOFFS, BETAS):
        z, density = beta_density(c, cutoff, beta)
        labels = list(density)
        operations = [identity(labels), {((d, (k+1) % d), (d, k)): F(1) for d, k in labels},
                      {((d, 0), (d, 0)): F(d) for d in range(2, cutoff+1)}]
        gram = [[trace(multiply(adjoint(a), b), density) for b in operations] for a in operations]
        for subset in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)):
            minor = [[gram[i][j] for j in subset] for i in subset]
            c.check('S4', determinant(minor) >= 0, 'actual state matrix-valued Gram probe has nonnegative principal minors')
        for amplitude in operations:
            c.check('S4', trace(multiply(adjoint(amplitude), amplitude), density) > 0,
                    'nonzero actual arithmetic-block amplitude has positive squared expectation')
        fragment = sum(F(totient(d), d**(beta+1)) for d in range(cutoff+1, 129))
        integral = (F(1, cutoff**(beta-1))-F(1, 128**(beta-1)))/(beta-1)
        bound = F(1, cutoff**(beta if c.mutation == 'tail-exponent' else beta-1))/(beta-1)
        for d in range(cutoff+1, 129):
            interval = (F(1, (d-1)**(beta-1))-F(1, d**(beta-1)))/(beta-1)
            c.check('S4', F(totient(d), d**(beta+1)) <= F(1, d**beta) <= interval,
                    'exact finite tail summand bounded by its rational integral interval')
        c.check('S4', fragment <= integral <= bound, 'finite tail fragment respects stated degree cutoff bound')
        records.append({'D': cutoff, 'beta': beta, 'Z_D': str(z), 'trace_density': '1',
                        'gram_determinant': str(determinant(gram)), 'tail_fragment_end': 128,
                        'tail_fragment': str(fragment), 'tail_bound': str(bound)})
    return records


def convolution_gates(c):
    counted = {d: totient(d) for d in range(1, 121)}
    if c.mutation == 'coprimality':
        counted[6] += 1  # Incorrectly treat 2 as coprime to 6.
    coefficients = []
    for k in range(1, 121):
        pairs = [(d, k//d) for d in range(1, k+1) if k % d == 0]
        full = sum(counted[d] for d, e in pairs)
        moving = sum(counted[d] for d, e in pairs if d > 1 or c.mutation == 'd1-subtraction')
        c.check('S5', full == k, 'Dirichlet convolution coefficient from literal coprime counts')
        c.check('S5', moving == k-1 and counted[1] == 1, 'moving convolution removes exactly the d=1 coefficient')
        for beta in BETAS:
            actual = sum(F(counted[d], d**(beta+1))*F(1, e**(beta+1)) for d, e in pairs if d > 1)
            c.check('S5', actual == F(1, k**beta)-F(1, k**(beta+1)),
                    'finite weighted coefficients for (Z+1) zeta(beta+1)=zeta(beta)')
        if k <= 12:
            coefficients.append({'k': k, 'totient': counted[k], 'full': full, 'moving': moving})
    return {'bound': 120, 'first_coefficients': coefficients}


def permutation_power(permutation, exponent):
    if exponent < 0:
        inverse = [0]*len(permutation)
        for i, j in enumerate(permutation):
            inverse[j] = i
        return permutation_power(inverse, -exponent)
    result = list(range(len(permutation)))
    for _ in range(exponent):
        result = [permutation[i] for i in result]
    return result


def moment_gates(c):
    records = []
    for cutoff, beta in product(CUTOFFS, BETAS):
        z, density = beta_density(c, cutoff, beta)
        values = []
        for exponent in MOMENTS:
            moment, channel_trace = F(0), 0
            for d in range(2, cutoff+1):
                permutation = [(k+1) % d for k in range(d)]
                applied = 0 if c.mutation == 'negative-power' and exponent < 0 else exponent
                power = permutation_power(permutation, applied)
                fixed = sum(power[k] == k for k in range(d))
                pair_fixed = sum((power[a], power[b]) == (a, b) for a, b in product(range(d), repeat=2))
                c.check('S6', pair_fixed == fixed*fixed, 'actual conjugation matrix-unit trace is squared implementer trace')
                channel_trace += pair_fixed
                moment += density[d, 0]*(pair_fixed if c.mutation == 'channel-trace' else fixed)
            expected = F(1) if exponent == 0 and c.mutation != 'zero-moment' else sum(
                F(totient(d), d**(beta+1)) for d in divisors(abs(exponent)) if 2 <= d <= cutoff)/z
            c.check('S6', moment == expected, 'explicit regulated implementer moment, with j=0 separately normalized')
            values.append({'j': exponent, 'implementer_moment': str(moment),
                           'conjugation_linear_trace': channel_trace})
        records.append({'D': cutoff, 'beta': beta, 'moments': values})
    return records


def cycle_lengths(permutation):
    unseen, lengths = set(range(len(permutation))), []
    while unseen:
        k, orbit = min(unseen), []
        while k not in orbit:
            orbit.append(k)
            k = permutation[k]
        unseen.difference_update(orbit)
        lengths.append(len(orbit))
    return sorted(lengths)


def permutation_determinant(permutation):
    traces = [sum(j == k for j, k in enumerate(permutation_power(permutation, power)))
              for power in range(1, len(permutation)+1)]
    result = [F(1)]
    for degree in range(1, len(permutation)+1):
        result.append(-sum(traces[j-1]*result[degree-j] for j in range(1, degree+1))/degree)
    return result


def tensor_gates(c):
    two, four = [1, 0], [1, 2, 3, 0]
    tensor = [2*two[a]+two[b] for a, b in product(range(2), repeat=2)]
    if c.mutation == 'tensor-cycle':
        tensor = four
    c.check('S7', cycle_lengths(tensor) == [2, 2] and cycle_lengths(four) == [4],
            'actual tensor of two 2-cycles is two cycles, not one 4-cycle')
    c.check('S7', permutation_power(tensor, 2) == list(range(4)) and
            permutation_power(four, 2) != list(range(4)), 'tensor-cycle orders differ at the same Hilbert dimension')
    dt, df = permutation_determinant(tensor), permutation_determinant(four)
    c.check('S7', dt == [1, 0, -2, 0, 1] and df == [1, 0, 0, 0, -1],
            'actual tensor and four-cycle determinant polynomials from permutation traces')
    return {'tensor_permutation': tensor, 'four_cycle_permutation': four,
            'tensor_cycles': cycle_lengths(tensor), 'four_cycles': cycle_lengths(four),
            'tensor_det_I_minus_zU': list(map(str, dt)), 'four_det_I_minus_zU': list(map(str, df))}


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--red', nargs='?', const='drop-divisor-weight',
                        choices=sorted(MUTATIONS), metavar='NAME')
    for name, gate in sorted(MUTATIONS.items()):
        parser.add_argument('--red-' + name, dest='red', action='store_const',
                            const=name, help=('alias of --red-identity (same S3 data)' if name == 'central-dynamics' else f'mutate the {gate} comparison'))
    args = parser.parse_args()
    c = Checks(args.red)
    result = {'mutation': args.red, 'exact': True}
    try:
        result['first_average_weight'] = first_red(c)
        fields = {degree: BinaryField(degree) for degree in DEGREES}
        result['derived_weights'] = derived_weight_gates(c, fields)
        result['corners'] = corner_gates(c, fields)
        result['dynamics'] = dynamics_gates(c)
        result['beta_cutoffs'] = beta_gates(c)
        result['dirichlet_coefficients'] = convolution_gates(c)
        result['regulated_moments'] = moment_gates(c)
        result['tensor_comparison'] = tensor_gates(c)
        result['status'] = 'PASS'
    except MathematicalFailure as error:
        result.update(status='FAIL', gate=error.gate, detail=error.detail)
    result['checks'] = dict(sorted(c.counts.items()))
    print(json.dumps(result, indent=2))
    return int(result['status'] == 'FAIL')


if __name__ == '__main__':
    raise SystemExit(main())
