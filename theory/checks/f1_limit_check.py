#!/usr/bin/env python3
"""Exact finite probes for the operational categorical limit.

Rational arithmetic only; samples are falsifiers, never continuity proofs.
Every mutation changes mathematical data and must produce a named FAIL.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import factorial


class Polynomial:
    """Small independent polynomial coefficient ring for base change probes."""
    def __init__(self, coefficients):
        if isinstance(coefficients, Polynomial):
            coefficients = coefficients.c
        elif isinstance(coefficients, (int, F)):
            coefficients = (coefficients,)
        c = list(map(F, coefficients))
        while c and not c[-1]:
            c.pop()
        self.c = tuple(c)

    def __add__(self, other):
        other = Polynomial(other)
        return Polynomial(tuple((self.c[i] if i < len(self.c) else 0)
                                + (other.c[i] if i < len(other.c) else 0)
                                for i in range(max(len(self.c), len(other.c)))))

    __radd__ = __add__

    def __neg__(self):
        return Polynomial(tuple(-x for x in self.c))

    def __sub__(self, other):
        return self + -Polynomial(other)

    def __rsub__(self, other):
        return Polynomial(other) + -self

    def __mul__(self, other):
        other = Polynomial(other)
        c = [F(0)] * max(0, len(self.c) + len(other.c) - 1)
        for i, x in enumerate(self.c):
            for j, y in enumerate(other.c):
                c[i+j] += x*y
        return Polynomial(c)

    __rmul__ = __mul__

    def __bool__(self):
        return bool(self.c)

    def __eq__(self, other):
        return self.c == Polynomial(other).c

    def evaluate(self, q):
        return sum((c*q**i for i, c in enumerate(self.c)), F(0))


def inv(w):
    return tuple(w.index(i) for i in range(len(w)))


def compose(u, v):
    return tuple(u[v[i]] for i in range(len(u)))


def length(w):
    return sum(w[i] > w[j] for i in range(len(w)) for j in range(i+1, len(w)))


def cycles(w):
    unseen, count = set(range(len(w))), 0
    while unseen:
        current = next(iter(unseen))
        count += 1
        while current in unseen:
            unseen.remove(current)
            current = w[current]
    return count


def reduced_word(w):
    a, moves = list(w), []
    for end in range(len(a)-1, 0, -1):
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                moves.append(i)
    return tuple(reversed(moves))


class Algebra:
    def __init__(self, n, q, bad_descent=False):
        self.n, self.q, self.bad_descent = n, q, bad_descent
        self.perms = tuple(permutations(range(n)))
        self.e = tuple(range(n))
        self.one = {self.e: F(1)}

    def add(self, *xs):
        out = {}
        for x in xs:
            for w, c in x.items():
                out[w] = out.get(w, 0) + c
        return {w: c for w, c in out.items() if c}

    def scale(self, c, x):
        return {w: c*v for w, v in x.items() if c*v}

    def sub(self, x, y):
        return self.add(x, self.scale(-1, y))

    def simple(self, i):
        s = list(self.e)
        s[i], s[i+1] = s[i+1], s[i]
        return {tuple(s): F(1)}

    @lru_cache(None)
    def basis_product(self, u, v):
        x = {u: F(1)}
        for i in reduced_word(v):
            terms = []
            for w, c in x.items():
                sw = list(w)
                sw[i], sw[i+1] = sw[i+1], sw[i]
                if w[i] < w[i+1]:
                    terms.append({tuple(sw): c})
                else:
                    terms.append({w: c*(self.q-1),
                                  tuple(sw): c*(self.q+int(self.bad_descent))})
            x = self.add(*terms)
        return x

    def mul(self, x, y):
        return self.add(*(self.scale(c*d, self.basis_product(u, v))
                          for u, c in x.items() for v, d in y.items()))

    def star(self, x):
        return {inv(w): c for w, c in x.items()}

    def tau(self, x):
        return x.get(self.e, F(0))

    def phi(self, ks, x):
        return self.add(*(self.mul(self.mul(self.star(k), x), k) for k in ks))


def embed(x, size, offset=0):
    out = {}
    for w, c in x.items():
        v = list(range(size))
        for i, value in enumerate(w):
            v[offset+i] = offset+value
        out[tuple(v)] = c
    return out


def sectors(h):
    q = h.q
    plus = {w: F(1)/sum(q**length(v) for v in h.perms) for w in h.perms}
    dm = sum(q**(-length(v)) for v in h.perms)
    minus = {w: (-q)**(-length(w))/dm for w in h.perms}
    return plus, minus, h.sub(h.sub(h.one, plus), minus)


def rank(rows):
    a = [list(map(F, row)) for row in rows]
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        lead = a[r][c]
        a[r] = [x/lead for x in a[r]]
        for i in range(len(a)):
            if i != r:
                lead = a[i][c]
                a[i] = [x-lead*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


CHECKED, FAILED = {}, {}


def need(condition, gate, diagnostic):
    CHECKED[gate] = CHECKED.get(gate, 0) + 1
    if not condition:
        FAILED.setdefault(gate, set()).add(diagnostic)


def base_change(args):
    formal = Algebra(3, Polynomial((0, 1)))
    for q in (F(1), F(3, 2), F(2), F(3)):
        actual = Algebra(3, q, args.red_descent)
        for u, v in product(formal.perms, repeat=2):
            symbolic = formal.basis_product(u, v)
            evaluated = {w: (c.evaluate(q) if isinstance(c, Polynomial) else c)
                         for w, c in symbolic.items()}
            evaluated = {w: c for w, c in evaluated.items() if c}
            need(evaluated == actual.basis_product(u, v), 'L1', 'product evaluation')
        little, big = Algebra(2, q), Algebra(4, q)
        for u, v in product(little.perms, repeat=2):
            left = embed(little.basis_product(u, v), 4)
            right = big.mul(embed({u: F(1)}, 4), embed({v: F(1)}, 4))
            need(left == right, 'L1', 'ordered block product')


def protocols(args):
    for q in (F(1), F(101, 100), F(11, 10), F(3, 2), F(2), F(3)):
        h = Algebra(3, q)
        pt, ps, z = sectors(h)
        es = [h.scale(1/(q+1), h.add(h.one, h.simple(i))) for i in (0, 1)]
        p = h.mul(z, es[1])
        gamma = q/(1+q+q*q)
        b = h.add(h.one, h.scale(q-1, h.simple(0)), h.simple(1))
        positive = h.mul(h.star(b), b)
        density = positive if args.red_density else h.scale(1/h.tau(positive), positive)
        need(h.tau(density) == 1 and h.tau(positive) > 0, 'L2', 'square-density normalization')
        us = [h.sub(h.scale(2, e), h.one) for e in es]
        ks = [h.scale(F(3, 5), us[0]), h.scale(F(4, 5), us[1])]
        outcomes = [es[1], h.sub(h.one, es[1])]
        joint = [h.mul(m, k) for k in ks for m in outcomes]
        if args.red_outcome:
            joint.pop()
        complete = h.add(*(h.mul(h.star(k), k) for k in joint))
        need(complete == h.one, 'L3', 'sequential instrument completeness')
        total = sum(h.tau(h.mul(density, h.mul(h.star(k), k))) for k in joint)
        need(total == 1, 'L3', 'total instrument probability')
        ratio = F(1) if args.red_corner_ratio else q+1
        refined = h.scale(ratio, es[1])
        need(h.tau(refined) == 1, 'L4', 'normalized corner-to-fine density')
        for w in h.perms:
            a = {w: F(1)}
            lhs = (q+1)*h.tau(h.mul(es[1], h.mul(h.mul(es[1], a), es[1])))
            rhs = h.tau(h.mul(refined, a))
            need(lhs == rhs, 'L4', 'typed refinement trace duality')
        success = h.tau(h.mul(refined, p))
        expected_success = (q+1)*gamma
        conditional = h.scale(1/gamma, p)
        actual_u = h.one if args.red_context else us[0]
        returned = h.tau(h.mul(conditional, h.phi([actual_u], p)))
        a = q/(q+1)**2
        expected_return = (1-2*a)**2
        need(success == expected_success and 0 < success <= 1, 'L5', 'refinement preparation success')
        need(h.tau(conditional) == 1 and returned == expected_return, 'L5', 'retained-context return')
        need(h.mul(p, p) == p and h.star(p) == p, 'L5', 'preparation is a projection outcome')
        if q == 1:
            need(success == F(2, 3) and returned == F(1, 4)
                 and success*returned == F(1, 6), 'L5', 'endpoint joint probability')
        defect = h.sub(h.mul(h.mul(us[0], us[1]), us[0]),
                       h.mul(h.mul(us[1], us[0]), us[1]))
        want = {} if args.red_braid else h.scale(-((q-1)/(q+1))**2, h.sub(us[0], us[1]))
        need(defect == want, 'L7', 'unitarized exchange defect')
        print(f'protocol q={q}: success={success}, return={returned}, joint={success*returned}')


def contexts(args):
    for n, q in product((2, 3), (F(1), F(101, 100), F(2))):
        size = 2*n-2 if args.red_ancilla else 2*n-1
        local, ambient = Algebra(n, q), Algebra(size, q)
        d = list(range(size))
        for i in range(1, n):
            j = n+i-1
            if j < size:
                d[i], d[j] = d[j], d[i]
        images = []
        for u, v in product(local.perms, repeat=2):
            value = ambient.mul(ambient.mul(embed({inv(u): F(1)}, size), {tuple(d): F(1)}),
                                embed({v: F(1)}, size))
            images.append(value)
        single = all(len(x) == 1 and next(iter(x.values())) == 1 for x in images)
        distinct = len({tuple(sorted(x.items())) for x in images}) == factorial(n)**2
        need(single and distinct, 'L6', 'unit minor recovering every Gram coefficient')


def schur_weyl(args):
    for n in range(1, 5):
        ps = tuple(permutations(range(n)))
        for d in range(1, 5):
            traces = {}
            for w in ps:
                fixed = sum(all(x[i] == x[w[i]] for i in range(n))
                            for x in product(range(d), repeat=n))
                exponent = cycles(w)-n-int(args.red_cycle)
                formula = F(d)**exponent
                need(F(fixed, d**n) == formula, 'L8', 'tensor fixed-point cycle trace')
                traces[w] = F(fixed, d**n)
            gram = [[traces[compose(inv(u), v)] for v in ps] for u in ps]
            r = rank(gram)
            need((r == factorial(n)) == (d >= n), 'L8', 'stable-rank faithfulness')
            antisym_weight = sum((-1)**length(w)*traces[w] for w in ps)/factorial(n)
            need((antisym_weight == 0) == (d < n), 'L8', 'alternating quotient sector')
    ps = tuple(permutations(range(3)))
    identity, s, t = (0, 1, 2), (1, 0, 2), (0, 2, 1)
    for d in (2, 3, 4, 10, 100):
        trace = lambda w: F(d)**(cycles(w)-3)
        candidate = {} if args.red_reference_trace else {identity: F(1, d)}
        for b in (identity, s):
            expected = trace(compose(inv(b), t))
            actual = sum(c*trace(compose(inv(b), w)) for w, c in candidate.items())
            need(actual == expected, 'L9', 'physical-trace conditional expectation')
        need(trace(t) == F(1, d) and trace(compose(s, t)) == F(1, d*d),
             'L9', 'finite dimension retains cycle contributions')


def singular_limits(args):
    for q in (2, 3, 5):
        a = [[int(i != j) for j in range(q)] for i in range(q)]
        for i, j in product(range(q), repeat=2):
            need(sum(a[i][k]*a[k][j] for k in range(q))
                 == (q-2)*a[i][j]+(q-1)*int(i == j), 'L10', 'mirabolic adjacency relation')
    for q in (F(1), F(101, 100), F(3, 2), F(2)):
        weights = (1/q, (q-1)/q)
        if args.red_null_weight and q == 1:
            weights = (F(1, 2), F(1, 2))
        need(sum(weights) == 1 and min(weights) >= 0, 'L10', 'mirabolic reference state')
        need((weights[1] == 0) == (q == 1), 'L10', 'limiting reference null sector')
        if q > 1:
            density = q/(q-1)
            need(weights[1]*density == 1 and density >= 1, 'L10', 'singular sector remains a normalized state')
    h = Algebra(3, F(1))
    _, _, z = sectors(h)
    e = h.scale(F(1, 2), h.add(h.one, h.simple(1)))
    p = h.mul(z, e)
    rho = h.scale(3, p)
    for n in range(2, 13):
        t, c = F(2*n, n*n+1), F(n*n-1, n*n+1)
        unitary = h.simple(0) if n % 2 else h.one
        k, failure = h.scale(t, unitary), h.scale(c, h.one)
        need(h.add(h.mul(h.star(k), k), h.mul(h.star(failure), failure)) == h.one,
             'L11', 'vanishing-success Kraus instrument completeness')
        success = h.tau(h.mul(rho, h.mul(h.star(k), k)))
        joint = h.tau(h.mul(rho, h.phi([k], p)))
        conditional = joint/(1 if args.red_postselection else success)
        need(success == t*t and conditional == (F(1, 4) if n % 2 else F(1)),
             'L11', 'distinct conditional subsequences require branch normalization')


def mirabolic_valencies(args):
    for n, p in product((1, 2, 3), (2, 3)):
        vectors = tuple(product(range(p), repeat=n))
        for w in permutations(range(n)):
            wi = inv(w)
            positions = [(i, j) for i in range(n) for j in range(i+1, n) if wi[i] < wi[j]]
            matrices = []
            for diagonal in product(range(1, p), repeat=n):
                for upper in product(range(p), repeat=len(positions)):
                    matrix = [[diagonal[i] if i == j else 0 for j in range(n)] for i in range(n)]
                    for (i, j), value in zip(positions, upper):
                        matrix[i][j] = value
                    matrices.append(matrix)
            covered = set()
            antichains = []
            for bits in product((False, True), repeat=n):
                a = {i for i, bit in enumerate(bits) if bit}
                if any(i in a and j in a for i, j in positions):
                    continue
                antichains.append(a)
                down = a | {i for i, j in positions if j in a}
                representative = tuple(int(i in a) for i in range(n))
                orbit = {tuple(sum(row[j]*representative[j] for j in range(n)) % p
                               for row in matrix) for matrix in matrices}
                predicted = {v for v in vectors if all(v[i] != 0 for i in a)
                             and all(v[i] == 0 for i in range(n) if i not in down)}
                exponent = len(down)-len(a)+int(args.red_valency)
                need(orbit == predicted and not (covered & orbit), 'L12', 'pattern-group antichain orbit')
                need(len(orbit) == (p-1)**len(a)*p**exponent, 'L12', 'mirabolic orbital valency factor')
                covered |= orbit
            need(covered == set(vectors), 'L12', 'antichain orbits partition the vector space')


@lru_cache(None)
def polar_longest(n, root):
    h = Algebra(n, F(root*root))
    longest = {tuple(reversed(range(n))): F(1)}
    if root == 1 or n < 2:
        return longest
    powers = {2: (2, 0), 3: (6, 3, 0), 4: (12, 8, 6, 4, 0)}[n]
    eigenvalues = [F(root)**power for power in powers]
    square = h.mul(longest, longest)
    projections = []
    for a in eigenvalues:
        projection = h.one
        for b in eigenvalues:
            if a != b:
                projection = h.mul(projection, h.scale(1/(a*a-b*b), h.sub(square, h.scale(b*b, h.one))))
        projections.append(projection)
        need(h.mul(projection, projection) == projection and h.star(projection) == projection,
             'L13', 'polar spectral projections are positive')
        need(h.mul(square, projection) == h.scale(a*a, projection), 'L13', 'polar spectral eigenvalue')
    need(h.add(*projections) == h.one, 'L13', 'polar spectral completeness')
    positive = h.add(*(h.scale(a, p) for a, p in zip(eigenvalues, projections)))
    inverse_positive = h.add(*(h.scale(1/a, p) for a, p in zip(eigenvalues, projections)))
    need(h.mul(positive, positive) == square, 'L13', 'positive absolute-value square')
    return h.mul(longest, inverse_positive)


def cactus(args):
    for root in (1, 2, 3):
        for size in (2, 3, 4):
            h = Algebra(size, F(root*root))
            intervals = [(i, j) for i in range(size) for j in range(i+1, size)]
            js = {}
            for i, j in intervals:
                n = j-i+1
                local = {tuple(reversed(range(n))): F(1)} if args.red_polar else polar_longest(n, root)
                js[i, j] = embed(local, size, i)
                need(h.star(js[i, j]) == js[i, j] and h.mul(js[i, j], js[i, j]) == h.one,
                     'L13', 'unitary interval reversal')
            for (i, j), (k, l) in product(intervals, repeat=2):
                if i <= k <= l <= j:
                    reflected = (i+j-l, i+j-k)
                    need(h.mul(js[i, j], js[k, l]) == h.mul(js[reflected], js[i, j]),
                         'L13', 'nested cactus relation')
                elif j < k or l < i:
                    need(h.mul(js[i, j], js[k, l]) == h.mul(js[k, l], js[i, j]),
                         'L13', 'disjoint cactus relation')
            for m in range(1, size):
                n = size-m
                local = h.mul(embed(polar_longest(m, root), size), embed(polar_longest(n, root), size, m))
                sigma = h.mul(js[0, size-1], local)
                for block, offset, shifted in ((m, 0, n), (n, m, 0)):
                    for i in range(block-1):
                        initial, final = h.simple(offset+i), h.simple(shifted+i)
                        need(h.mul(sigma, initial) == h.mul(final, sigma), 'L13', 'block commutor naturality')


def assembly_retraction(args):
    for q in (F(1), F(101, 100), F(2)):
        h = Algebra(3, q)
        def expect(x):
            return {w: c for w, c in x.items() if w[2] == 2}
        e = h.scale(1/(q+1), h.add(h.one, h.simple(0)))
        u = h.sub(h.scale(2, e), h.one)
        for w in h.perms:
            x = {w: F(1)}
            coarse = expect(x)
            need(expect(coarse) == coarse and h.tau(coarse) == h.tau(x),
                 'L14', 'assembly split is a trace-preserving retraction')
            need(expect(h.phi([u], x)) == h.phi([u], coarse),
                 'L14', 'retained local process respects assembly')
        outside = h.simple(1)
        demanded = outside if args.red_collective_identity else {}
        need(expect(outside) == demanded and outside != {},
             'L14', 'collective coarse graining differs from identity')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mutations = {
        'descent': 'L1: alter Hecke descent multiplication',
        'density': 'L2: omit normalization of a positive square',
        'outcome': 'L3: remove an instrument outcome',
        'corner-ratio': 'L4: omit normalized corner trace ratio',
        'context': 'L5: forget the ambient action of a local unitary',
        'ancilla': 'L6: use too few ancillary constituents',
        'braid': 'L7: force generic unitary exchanges to braid',
        'cycle': 'L8: drop a tensor cycle in the physical trace',
        'reference-trace': 'L9: use coefficient expectation at finite dimension',
        'null-weight': 'L10: retain positive reference weight in the null sector',
        'postselection': 'L11: omit normalization of a vanishing-success branch',
        'valency': 'L12: alter the vector-orbit power of the field size',
        'polar': 'L13: use the raw longest word as unitary interval reversal',
        'collective-identity': 'L14: identify collective coarse graining with identity',
    }
    for name, help_text in mutations.items():
        parser.add_argument('--red-'+name, action='store_true', help=help_text)
    args = parser.parse_args()
    print('MODE:', ','.join(k for k, v in vars(args).items() if v) or 'green')
    base_change(args)
    protocols(args)
    contexts(args)
    schur_weyl(args)
    singular_limits(args)
    mirabolic_valencies(args)
    cactus(args)
    assembly_retraction(args)
    for gate in sorted(CHECKED, key=lambda g: int(g[1:])):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED[gate]} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL CATEGORICAL LIMIT EXAMPLES PASSED (finite exact probes)')


if __name__ == '__main__':
    main()
