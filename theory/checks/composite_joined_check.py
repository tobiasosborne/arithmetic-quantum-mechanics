#!/usr/bin/env python3
"""Exact finite joined-limit falsifiers; no finite pass proves an infinite limit."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd
import json


MUTATIONS = {'omit-gap': 'J1', 'condition-zero': 'J1', 'drop-divisor': 'J2',
             'reset-copy': 'J2', 'drop-randomizer': 'J2', 'wrong-prior': 'J3',
             'wrong-normalizer': 'J3', 'lost-history': 'J3', 'vanishing-bound': 'J4',
             'operator-norm': 'J4', 'drop-grade': 'J5'}
TS = tuple(sorted({F(1), F(6, 5), F(3, 2), F(2)} |
                  {1+F(1, m) for m in (4, 8, 16, 32, 64)}))
BETAS, BASES, CUTOFFS = (2, 3, 4), (1, 2), (2, 4, 8, 16, 32)


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


def divisors(n):
    return [d for d in range(1, n+1) if n % d == 0]


@lru_cache(None)
def totient(n):
    return sum(gcd(a, n) == 1 for a in range(1, n+1))


@lru_cache(None)
def polynomial(n):
    coefficients = {n: 1}
    for d in divisors(n)[:-1]:
        for k, a in polynomial(d):
            coefficients[k] = coefficients.get(k, 0)-a
    return tuple(sorted((k, a) for k, a in coefficients.items() if a))


def count(n, x):
    return sum(a*x**k for k, a in polynomial(n))


@lru_cache(None)
def divided_polynomial(d, s):
    coefficients = [0]*(s*d+1)
    for k, a in polynomial(d):
        coefficients[s*k] = a
    quotient = [0]*(s*d)
    carried = 0
    for k in range(s*d, 0, -1):
        carried += coefficients[k]
        quotient[k-1] = carried
    assert coefficients[0]+quotient[0] == 0
    return tuple(quotient)


def w(d, s, t, mutation=None):
    return count(d, t**s)/((1 if mutation == 'drop-divisor' else d)*t**(s*d))


@lru_cache(None)
def v(d, s, t, mutation=None):
    if t == 1:
        return F(0) if mutation == 'condition-zero' else F(totient(d), d)
    denominator = s if mutation == 'omit-gap' else s*(t-1)
    return w(d, s, t, mutation)/denominator


def first_red(c):
    t = F(3, 2)
    # The actual F4 orbit {a,a+1} has two distinct copied graph tuples.
    # Each input label has POS probability (t^2-t)/(2t^2).
    graph = ((2, 2, 3), (3, 3, 2))
    probability = F(0)
    for _ in graph:
        image = {a: F(1, 2) for a in graph}
        probability += (t*t-t)/(2*t*t)*sum(a*a for a in image.values())
    c.check('J2', probability == w(2, 1, t, c.mutation),
            'actual copied F4 success requires the 1/d averaging factor')
    return str(probability)


def scalar_gates(c):
    for d, s in product(range(2, 65), BASES):
        q = divided_polynomial(d, s)
        c.check('J1', sum(q) == s*totient(d), 'synthetic division endpoint matches independently counted totient')
        for t in TS:
            value = v(d, s, t, c.mutation)
            independent = sum(F(a, s*d)*t**(k-s*d) for k, a in enumerate(q))
            c.check('J1', value == independent, 'v(t) agrees with exact polynomial division, including retained endpoint grade')
            c.check('J1', 0 < value <= 1, 'strict positivity and degree-uniform bound on v_d(t)')
            if t > 1:
                actual_count = count(d, t**s)
                geometric = (t-1)*sum(t**(-j) for j in range(1, s*d+1))
                c.check('J1', 0 < actual_count <= t**(s*d)-1 and
                        geometric == 1-t**(-s*d) and geometric <= s*d*(t-1),
                        'independent count and finite geometric bounds supporting the uniform estimate')
    normalizers = []
    for s, t in product(BASES, TS):
        actual = v(2, s, t)
        geometric = sum(t**(-j) for j in range(1, s+1))/(2*s)
        c.check('J1', actual == geometric and actual >= F(1, 2*2**s),
                'explicit v_2 identity and common lower normalizer on [1,2]')
        normalizers.append({'s': s, 't': str(t), 'v2': str(actual), 'lower_bound': str(F(1, 2*2**s))})
    return {'maximum_degree': 64, 't_values': list(map(str, TS)), 'normalizer_samples': normalizers}


def binary_product(a, b, modulus):
    result, leading = 0, 1 << (modulus.bit_length()-1)
    while b:
        if b % 2:
            result ^= a
        a <<= 1
        if a & leading:
            a ^= modulus
        b >>= 1
    return result


class Field:
    def __init__(self, degree):
        self.degree, self.size = degree, 2**degree
        # Named binary presentations, validated on every nonzero element.
        self.modulus = {2: 0b111, 3: 0b1011, 4: 0b10011,
                        6: 0b1000011, 8: 0b100011011}[degree]
        self.square = [self.mul(a, a) for a in range(self.size)]
        assert all(self.power(a, self.size-1) == 1 for a in range(1, self.size))
        self.period = {a: len(orbit) for orbit in self.orbits(1) for a in orbit}

    def mul(self, a, b):
        return binary_product(a, b, self.modulus)

    def power(self, a, exponent):
        answer = 1
        while exponent:
            if exponent % 2:
                answer = self.mul(answer, a)
            a, exponent = self.mul(a, a), exponent//2
        return answer

    def sigma(self, a, s):
        for _ in range(s):
            a = self.square[a]
        return a

    def orbits(self, s):
        unused, orbits = set(range(self.size)), []
        while unused:
            a, orbit = min(unused), []
            while a not in orbit:
                orbit.append(a)
                a = self.sigma(a, s)
            unused.difference_update(orbit)
            orbits.append(tuple(orbit))
        return orbits

    def reference(self, t):
        coefficients = {d: (t-1 if d == 1 else count(d, t)) /
                        (1 if d == 1 else count(d, 2)) for d in set(self.period.values())}
        return [(F(1) if a == 0 else coefficients[self.period[a]])/t**self.degree
                for a in range(self.size)]

    def first_coefficient(self, a):
        d = self.period[a]
        return F(0) if a == 0 else F(totient(d), 1 if d == 1 else count(d, 2))


def norm(vector):
    return sum((a*a for a in vector.values()), F(0))


def subtract(a, b):
    return {key: a.get(key, 0)-b.get(key, 0) for key in set(a)|set(b)
            if a.get(key, 0) != b.get(key, 0)}


def permute(vector, function):
    answer = defaultdict(F)
    for key, value in vector.items():
        answer[function(key)] += value
    return dict(answer)


def project(vector, orbit_sum):
    coefficient = sum((vector.get(a, 0) for a in orbit_sum), F(0))/len(orbit_sum)
    return {a: coefficient for a in orbit_sum} if coefficient else {}


class Experiment:
    def __init__(self, c, field, s, d):
        self.field, self.s, self.d = field, s, d
        self.primitive = [o for o in field.orbits(s) if len(o) == d]
        self.data = {}
        for orbit in self.primitive:
            basis = [{(a, field.sigma(a, s*k), field.mul(a, field.sigma(a, s*k)))
                      for a in orbit} for k in range(d)]
            for a in orbit:
                atom = {(a, a, field.mul(a, a)): F(1)}
                average, current = defaultdict(F), atom
                for _ in range(d):
                    for key, value in current.items():
                        average[key] += value/d
                    current = permute(current, lambda key: tuple(field.sigma(x, s) for x in key))
                vector = dict(average)
                success, avg_failure = norm(vector), norm(subtract(atom, vector))
                c.check('J2', success+avg_failure == 1 and vector == project(atom, basis[0]),
                        'actual copied field graph and simultaneous-average instrument')
                before, before_fail = self.comparisons(vector, basis[1])
                tags, after, after_fail = [], [F(0)]*3, [F(0)]*3
                for j in range(d):
                    matrix = {}
                    amplitudes = [sum(vector.get(key, 0) for key in b) for b in basis]
                    if not (c.mutation == 'drop-randomizer' and j == d-1):
                        matrix = {(u, z): amplitudes[u]*amplitudes[z]/(d*d)
                                  for u, z in product(range(d), repeat=2) if amplitudes[u]*amplitudes[z]}
                        probabilities, failures = self.comparisons(vector, basis[1])
                        for k in range(3):
                            after[k] += probabilities[k]/d
                            after_fail[k] += failures[k]/d
                    tags.append(matrix)
                    vector = permute(vector, self.relative)
                logical = defaultdict(F)
                for matrix in tags:
                    for key, value in matrix.items():
                        logical[key] += value
                c.check('J2', sum(logical.get((k, k), 0) for k in range(d)) == success,
                        'all randomizer outcomes retain the actual prepared trace')
                c.check('J2', dict(logical) == {(k, k): success/d for k in range(d)},
                        'discarding the randomizer tag gives the actual common tracial block')
                assert all(isinstance(value, F) for values in (before, before_fail, after, after_fail)
                           for value in values), 'probability arithmetic must remain rational, including zero'
                self.data[a] = {'success': success, 'average_failure': avg_failure,
                                'before': before, 'before_fail': before_fail,
                                'after': after, 'after_fail': after_fail,
                                'tags': tags, 'logical': dict(logical)}

    def relative(self, triple):
        a, b, z = triple
        shifted = self.field.sigma(b, self.s)
        return a, shifted, z ^ self.field.mul(a, b) ^ self.field.mul(a, shifted)

    def comparisons(self, vector, q1):
        moved = permute(vector, self.relative)
        projections = [project(moved, q1), project(vector, q1)]
        yes = [norm(projections[0]), norm(projections[1]), F(0)]
        no = [norm(subtract(moved, projections[0])), norm(subtract(vector, projections[1])), F(0)]
        for key, value in vector.items():
            atom = {self.relative(key): F(1)}
            projected = project(atom, q1)
            yes[2] += value*value*norm(projected)
            no[2] += value*value*norm(subtract(atom, projected))
        return yes, no

    def evaluate(self, c, t):
        reference, d = self.field.reference(t), self.d
        c.check('J2', sum(reference) == 1 and min(reference) >= 0, 'actual finite-field POS preparation is a normalized state')
        result = {'success': F(0), 'average_failure': F(0), 'primitive_failure':
                  1-sum(reference[a] for a in self.data), 'logical': defaultdict(F),
                  'randomizer_masses': [F(0)]*d}
        for name in ('before', 'before_fail', 'after', 'after_fail'):
            result[name] = [F(0)]*3
        for a, data in self.data.items():
            weight = reference[a]
            if c.mutation == 'reset-copy':
                weight *= reference[a]*reference[self.field.mul(a, a)]
            for name in ('success', 'average_failure'):
                result[name] += weight*data[name]
            for name in ('before', 'before_fail', 'after', 'after_fail'):
                for k in range(3):
                    result[name][k] += weight*data[name][k]
            for key, value in data['logical'].items():
                result['logical'][key] += weight*value
            for j, matrix in enumerate(data['tags']):
                result['randomizer_masses'][j] += weight*sum(matrix.get((k, k), 0) for k in range(d))
        expected = w(d, self.s, t, c.mutation)
        c.check('J2', result['success'] == expected, 'actual copied-reference probability versus c_d(t^s)/(d t^(sd))')
        for placement in ('before', 'after'):
            for k in range(3):
                c.check('J2', result['primitive_failure']+result['average_failure']+
                        result[placement][k]+result[placement+'_fail'][k] == 1,
                        'every degree retains primitive, average and final measurement histories')
        c.check('J2', sum(result['randomizer_masses']) == expected and
                all(a == expected/d for a in result['randomizer_masses']),
                'physical randomizer labels have complete normalized probabilities')
        if t > 1:
            c.check('J2', [a/expected for a in result['before']] == [1, 0, F(1, d)],
                    'unrandomized full/identity/dephased comparison is 1,0,1/d')
            c.check('J2', [a/expected for a in result['after']] == [F(1, d), F(1, d), F(1, d*d)],
                    'randomized full/identity/dephased comparison is 1/d,1/d,1/d^2')
        else:
            c.check('J2', expected == 0 and all(a == 0 for a in result['logical'].values()),
                    'raw endpoint is zero and is not physically conditioned')
        result['leading'] = sum(self.field.first_coefficient(a)*data['success'] for a, data in self.data.items())
        result['leading_logical'] = {(k, k): result['leading']/d for k in range(d)}
        return result


def physical_gates(c):
    fields = {r: Field(r) for r in (2, 3, 4, 6, 8)}
    values, records = {}, []
    for s, d in product(BASES, (2, 3, 4)):
        experiment = Experiment(c, fields[s*d], s, d)
        for t in TS:
            result = experiment.evaluate(c, t)
            values[s, d, t] = result
            records.append({'s': s, 'd': d, 'field_size': fields[s*d].size,
                            't': str(t), 'success': str(result['success']),
                            'first_coefficient': str(result['leading']),
                            'before_randomization_yes': list(map(str, result['before'])),
                            'after_randomization_yes': list(map(str, result['after'])),
                            'randomizer_masses': list(map(str, result['randomizer_masses'])),
                            'primitive_failure': str(result['primitive_failure']),
                            'average_failure': str(result['average_failure'])})
    return values, records


def density(D, beta, s, t, mutation=None):
    masses = {d: F(1, d**beta)*v(d, s, t) for d in range(2, D+1)}
    z = sum(masses.values())
    denominator = sum(F(1, d**beta) for d in masses) if mutation == 'wrong-normalizer' else z
    return z, {(d, k): masses[d]/(d*denominator) for d in masses for k in range(d)}


def mixture_gates(c, physical):
    records = []
    for s, beta, D, t in product(BASES, BETAS, (2, 3, 4), TS):
        specified_L = sum(F(1, d**beta) for d in range(2, D+1))
        exponent = beta+1 if c.mutation == 'wrong-prior' else beta
        normalizer = sum(F(1, d**exponent) for d in range(2, D+1))
        prior = {d: F(1, d**exponent)/normalizer for d in range(2, D+1)}
        c.check('J3', sum(prior.values()) == 1, 'actual finite classical degree prior normalizes')
        for d in prior:
            c.check('J3', prior[d]/prior[2] == F(2, d)**beta,
                    'degree prior has the declared relative d^(-beta) probabilities')
        z, state = density(D, beta, s, t, c.mutation)
        c.check('J3', sum(state.values()) == 1 and min(state.values()) > 0,
                'successful common mixture uses its actual Z_D normalizer in ordinary trace')
        success, history, logical = F(0), {}, defaultdict(F)
        for d, probability in prior.items():
            data = physical[s, d, t]
            success += probability*data['success']
            history[d, 'primitive-failure'] = probability*data['primitive_failure']
            history[d, 'average-failure'] = probability*data['average_failure']
            for j, mass in enumerate(data['randomizer_masses']):
                history[d, 'success', j] = probability*mass
            for (a, b), value in data['logical'].items():
                logical[(d, a), (d, b)] += probability*value
        if c.mutation == 'lost-history':
            history.pop((2, 'primitive-failure'))
        c.check('J3', sum(history.values()) == 1, 'all physical degree tags and stopped/randomizer histories sum to one')
        c.check('J3', success == s*(t-1)*z/specified_L, 'finite tagged preparation has the proposed total physical success')
        if t > 1:
            for a, b in logical:
                c.check('J3', logical[a, b]/success == (state[a] if a == b else 0),
                        'actual randomizer-discarded common responses equal the normalized mixture')
        actual_grade = sum(prior[d]*physical[s, d, t]['leading'] for d in prior)
        if c.mutation == 'drop-grade':
            actual_grade = F(0)
        z0, endpoint = density(D, beta, s, F(1))
        c.check('J5', actual_grade == s*z0/specified_L and actual_grade > 0,
                'actual copied POS first grade survives with rate s Z_D(beta,1)/L_D')
        for d in prior:
            data = physical[s, d, t]
            for k in range(d):
                c.check('J5', prior[d]*data['leading_logical'][k, k]/actual_grade == endpoint[d, k],
                        'retained first-grade conditional common state equals the endpoint density')
        if t in (F(1), F(6, 5), F(2)):
            records.append({'s': s, 'beta': beta, 'D': D, 't': str(t),
                            'L_D': str(specified_L), 'Z_D': str(z),
                            'success': str(success), 'h_first_coefficient': str(actual_grade),
                            'retained_history_count': len(history), 'history_trace': '1'})
    return records


def trace_distance(a, b):
    return sum(abs(a.get(k, 0)-b.get(k, 0)) for k in set(a)|set(b))


def matrix_product(a, b):
    answer = defaultdict(F)
    rows = defaultdict(list)
    for (i, j), value in b.items():
        rows[i].append((j, value))
    for (i, k), value in a.items():
        for j, other in rows[k]:
            answer[i, j] += value*other
    return {key: value for key, value in answer.items() if value}


def cutoff_gates(c):
    effect = {((d, a), (d, b)): F(1, 2) for d in (2, 3, 4) for a, b in product((0, 1), repeat=2)}
    c.check('J4', matrix_product(effect, effect) == effect,
            'named fixed non-diagonal effect is an actual orthogonal projection')
    records = []
    for s, beta, t, D in product(BASES, BETAS, TS, CUTOFFS):
        E = 2*D
        zd, small = density(D, beta, s, t)
        ze, large = density(E, beta, s, t)
        distance = trace_distance(small, large)
        if c.mutation == 'operator-norm':
            distance = max(abs(small.get(k, 0)-large.get(k, 0)) for k in set(small)|set(large))
        c.check('J4', distance == 2*(ze-zd)/ze,
                'actual ordinary trace norm equals twice normalized finite tail mass')
        bound = F(2**(beta+2)*2**s, (beta-1)*D**(beta-1))
        if c.mutation == 'vanishing-bound':
            bound *= t-1
        c.check('J4', distance <= bound, 'finite truncation comparison obeys the t-uniform cutoff estimate')
        fragment = sum(F(1, d**beta)*v(d, s, t) for d in range(D+1, E+1))
        integral = (F(1, D**(beta-1))-F(1, E**(beta-1)))/(beta-1)
        c.check('J4', fragment == ze-zd and fragment <= integral and ze >= F(1, 2**(beta+1+s)),
                'actual finite tail and explicit v_2 normalizer support the uniform bound')
        shifted_small = {(d, (k+1) % d): value for (d, k), value in small.items()}
        shifted_large = {(d, (k+1) % d): value for (d, k), value in large.items()}
        c.check('J4', shifted_small == small and shifted_large == large and
                trace_distance(shifted_small, shifted_large) == distance,
                'specified actual relative Frobenius preserves the common mixtures and their distance')
        effect_change = sum(value*(small.get(a, 0)-large.get(a, 0))
                            for (a, b), value in effect.items() if a == b)
        c.check('J4', abs(effect_change) <= distance,
                'named fixed bounded non-diagonal effect response obeys the actual trace distance')
        if t in (F(1), F(6, 5), F(2)):
            records.append({'s': s, 'beta': beta, 't': str(t), 'D': D, 'E': E,
                            'trace_distance': str(distance), 'uniform_bound': str(bound),
                            'fixed_effect_response_difference': str(effect_change)})
    continuity = []
    for s, beta, D in product(BASES, BETAS, CUTOFFS):
        _, endpoint = density(D, beta, s, F(1))
        lipschitz = sum(F(1, d**beta)*sum(F(abs(a)*(s*d-k), s*d)
                        for k, a in enumerate(divided_polynomial(d, s))) for d in range(2, D+1))
        errors = []
        for m in (4, 8, 16, 32, 64):
            t = 1+F(1, m)
            z, state = density(D, beta, s, t)
            error = trace_distance(state, endpoint)
            independent_bound = 2*(t-1)*lipschitz/z
            c.check('J4', error <= independent_bound,
                    'shrinking rational-step continuity obeys independent finite polynomial coefficient bound')
            errors.append({'m': m, 'trace_distance_to_endpoint': str(error),
                           'finite_continuity_bound': str(independent_bound)})
        continuity.append({'s': s, 'beta': beta, 'D': D, 'steps': errors})
    return {'cutoff_comparisons': records, 'shrinking_steps': continuity}


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--red', nargs='?', const='drop-divisor', choices=sorted(MUTATIONS), metavar='NAME')
    for name, gate in sorted(MUTATIONS.items()):
        parser.add_argument('--red-'+name, dest='red', action='store_const', const=name,
                            help=f'run the {name} mutation at {gate}')
    args = parser.parse_args()
    c = Checks(args.red)
    result = {'mutation': args.red, 'exact': True, 'finite_scope_only': True}
    try:
        result['first_actual_F4_success'] = first_red(c)
        result['scalars'] = scalar_gates(c)
        physical, result['physical_preparations'] = physical_gates(c)
        result['tagged_mixtures'] = mixture_gates(c, physical)
        result['finite_comparisons'] = cutoff_gates(c)
        result['status'] = 'PASS'
    except MathematicalFailure as error:
        result.update(status='FAIL', gate=error.gate, detail=error.detail)
    result['checks'] = dict(sorted(c.counts.items()))
    print(json.dumps(result, indent=2))
    return int(result['status'] == 'FAIL')


if __name__ == '__main__':
    raise SystemExit(main())
