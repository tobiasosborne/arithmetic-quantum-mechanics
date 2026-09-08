#!/usr/bin/env python3
"""Exact falsifiers for the mirabolic Fourier and type-C bridge.

No floats are used.  F_3 Fourier entries live in Q[z]/(z^2+z+1).
Finite checks support the written uniform proofs; they do not replace them.
"""
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, factorial


CHECKED, FAILED = {}, {}


def need(condition, gate, message):
    CHECKED[gate] = CHECKED.get(gate, 0) + 1
    if not condition:
        FAILED.setdefault(gate, set()).add(message)


@dataclass(frozen=True)
class Zeta:
    """a+b*z in Q[z]/(z^2+z+1); rationals use b=0."""
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = zeta(other)
        return Zeta(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Zeta(-self.a, -self.b)

    def __sub__(self, other):
        return self + -zeta(other)

    def __mul__(self, other):
        other = zeta(other)
        return Zeta(self.a*other.a-self.b*other.b,
                    self.a*other.b+self.b*other.a-self.b*other.b)

    __rmul__ = __mul__

    def conj(self):
        return Zeta(self.a-self.b, -self.b)

    def scale(self, c):
        return Zeta(F(c)*self.a, F(c)*self.b)


def zeta(x):
    return x if isinstance(x, Zeta) else Zeta(F(x), F(0))


def root(p, exponent):
    exponent %= p
    if p == 2:
        return zeta(1 if exponent == 0 else -1)
    return (zeta(1), Zeta(0, 1), Zeta(-1, -1))[exponent]


def vectors(p, n):
    return tuple(product(range(p), repeat=n))


def addv(x, y, p):
    return tuple((a+b) % p for a, b in zip(x, y))


def scalev(c, x, p):
    return tuple(c*a % p for a in x)


def dot(x, y, p):
    return sum(a*b for a, b in zip(x, y)) % p


def subspaces(p, n):
    vs = vectors(p, n)
    zero = (0,)*n
    spaces = {frozenset((zero,)), frozenset(vs)}
    for v in vs[1:]:
        spaces.add(frozenset(scalev(c, v, p) for c in range(p)))
    return tuple(sorted(spaces, key=lambda u: (len(u), sorted(u))))


def matmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), zeta(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def star(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def matscale(c, a):
    return [[x.scale(c) for x in row] for row in a]


def fourier_tests(args):
    for p in (2, 3):
        for n in (1, 2):
            vs = vectors(p, n)
            index = {v: i for i, v in enumerate(vs)}
            fourier = [[root(p, -dot(lam, x, p)) for x in vs] for lam in vs]
            for u in subspaces(p, n):
                px = [[zeta(F(1, len(u))) if addv(x, scalev(-1, y, p), p) in u
                       else zeta(0) for y in vs] for x in vs]
                annihilator = {lam for lam in vs if all(dot(lam, x, p) == 0 for x in u)}
                if args.red_fourier and n == 1 and len(u) == p:
                    annihilator = set(vs)
                pz = [[zeta(int(i == j and vs[i] in annihilator))
                       for j in range(len(vs))] for i in range(len(vs))]
                conjugated = matscale(F(1, p**n), matmul(matmul(fourier, px), star(fourier)))
                need(conjugated == pz, 'B3', f'Fourier constraint p={p}, n={n}, |U|={len(u)}')
            if n == 1:
                whole = frozenset(vs)
                zero = frozenset(((0,),))
                need(len(whole) == p and len(zero) == 1, 'B3', 'index-zero endpoint constraint')
                # The n=1 source C_1^X maps to target C_0^Z=|0><0|.
                need({lam for lam in vs if all(dot(lam, x, p) == 0 for x in whole)} == set(zero),
                     'B3', 'rank-one C1X to C0Z')
            square = matmul(fourier, fourier)
            expected_square = [[zeta(p**n if y == scalev(-1, x, p) else 0) for y in vs] for x in vs]
            need(square == expected_square, 'B3', 'named Fourier square is vector negation')
        lines = [u for u in subspaces(p, 2) if len(u) == p]
        dual_lines = []
        for u in lines:
            dual_lines.append(frozenset(lam for lam in vectors(p, 2)
                                        if all(dot(lam, x, p) == 0 for x in u)))
        need(set(dual_lines) == set(lines) and len(set(dual_lines)) == p+1,
             'B3', f'dual flag reversal p={p}')


def dual_flag_tests(args):
    # Coordinate flags provide exact rank matrices over every field.
    for n in range(1, 6):
        universe = set(range(n))
        reversal = tuple(reversed(range(n)))
        for w in permutations(range(n)):
            predicted = tuple(reversal[w[reversal[i]]] for i in range(n))
            for i, j in product(range(n+1), repeat=2):
                first_index = i if args.red_dual_reversal else n-i
                left = universe-set(range(first_index))
                right = universe-set(w[:n-j])
                actual = len(left & right)
                expected = len(set(range(i)) & set(predicted[:j]))
                need(actual == expected, 'B3', 'dual flag reversal conjugates relative position by w0')


def parity(x):
    return x.bit_count() & 1


def matvec(matrix, vector):
    return sum(parity(row & vector) << i for i, row in enumerate(matrix))


def omega(vector, other, dim):
    return sum((((vector >> (2*i)) & 1) * ((other >> (2*i+1)) & 1)
                + ((vector >> (2*i+1)) & 1) * ((other >> (2*i)) & 1))
               for i in range(dim//2)) & 1


def symplectic_group(dim):
    out = []
    for data in range(1 << (dim*dim)):
        matrix = tuple((data >> (dim*i)) & ((1 << dim)-1) for i in range(dim))
        images = [matvec(matrix, 1 << j) for j in range(dim)]
        if all(omega(images[i], images[j], dim) == omega(1 << i, 1 << j, dim)
               for i in range(dim) for j in range(dim)):
            out.append(matrix)
    return tuple(out)


def span2(a, b):
    return frozenset((0, a, b, a ^ b))


def isotropic_flags_4():
    planes = {span2(a, b) for a in range(1, 16) for b in range(a+1, 16)
              if b != a and omega(a, b, 4) == 0 and len(span2(a, b)) == 4}
    flags = []
    for plane in planes:
        for a in sorted(plane-{0}):
            flags.append((frozenset((0, a)), plane))
    return tuple(flags), tuple(planes)


def apply_subspace(matrix, space):
    return frozenset(matvec(matrix, x) for x in space)


def apply_flag(matrix, flag):
    return tuple(apply_subspace(matrix, u) for u in flag)


def embed_block(a, b):
    return (a[0], a[1], b[0] << 2, b[1] << 2)


def permutation_action(group, flags):
    index = {flag: i for i, flag in enumerate(flags)}
    return tuple(tuple(index[apply_flag(g, flag)] for flag in flags) for g in group)


def pair_orbits(actions, size, subset=None):
    domain = set(product(range(size), repeat=2)) if subset is None else set(product(subset, repeat=2))
    orbits = []
    while domain:
        seed = next(iter(domain))
        orbit = {(g[seed[0]], g[seed[1]]) for g in actions}
        need(orbit <= domain | set().union(*orbits) if orbits else orbit <= domain,
             'B5', 'group pair orbit remains in domain')
        domain -= orbit
        orbits.append(frozenset(orbit))
    return tuple(orbits)


def shuffle_words(counts):
    total = sum(counts)
    labels = tuple(range(len(counts)))
    return tuple(w for w in product(labels, repeat=total)
                 if tuple(w.count(i) for i in labels) == tuple(counts))


def type_c_tests(args):
    sp2, sp4 = symplectic_group(2), symplectic_group(4)
    flags, planes = isotropic_flags_4()
    need(len(sp2) == 6 and len(sp4) == 720, 'B5', 'symplectic group orders 6 and 720')
    need(len(planes) == 15 and len(flags) == 45, 'B5', '15 Lagrangians and 45 flags')
    local_lines = tuple(frozenset((0, v)) for v in (1, 2, 3))
    dec, labels = [], {}
    for u, z, word in product(local_lines, local_lines, ((0, 1), (1, 0))):
        eu = frozenset(u)
        ez = frozenset(x << 2 for x in z)
        plane = frozenset(x ^ y for x in eu for y in ez)
        first = eu if word[0] == 0 else ez
        flag = (first, plane)
        labels[flag] = (u, z, word)
        dec.append(flag)
    dec = tuple(dec)
    need(len(set(dec)) == 18 and set(dec) <= set(flags), 'B5', '18 unique decomposable flags')
    flag_index = {flag: i for i, flag in enumerate(flags)}
    dec_indices = tuple(flag_index[flag] for flag in dec)
    hgroup = tuple(embed_block(a, b) for a, b in product(sp2, repeat=2))
    for h in hgroup:
        for flag in dec:
            moved = apply_flag(h, flag)
            need(moved in labels and labels[moved][2] == labels[flag][2],
                 'B5', 'local action preserves decomposability and shuffle')
    g_actions = permutation_action(sp4, flags)
    h_actions_global = permutation_action(hgroup, flags)
    orbit = {g[0] for g in g_actions}
    need(len(orbit) == 45, 'B5', 'Sp4 acts transitively on isotropic flags')
    counts = []
    dec_set = set(dec_indices)
    for target in range(45):
        counts.append(sum(g[target] in dec_set for g in g_actions))
    wanted = 288 if not args.red_typec_scale else 720
    need(all(c == wanted for c in counts), 'B5', 'group average p=(18/45)I')
    g_orbits = pair_orbits(g_actions, 45)
    h_orbits = pair_orbits(h_actions_global, 45, dec_indices)
    need(len(g_orbits) == 8 and len(h_orbits) == 16, 'B5', 'type-C and product-shuffle commutant dimensions')
    pair_to_g = {pair: i for i, orb in enumerate(g_orbits) for pair in orb}
    ratio = F(5, 2) if not args.red_typec_scale else F(1)
    p_support = {(i, i) for i in dec_indices}
    averaged_p = []
    for orb in g_orbits:
        averaged_p.append(ratio * F(len(orb & p_support), len(orb)))
    diag_orbit = next(i for i, orb in enumerate(g_orbits) if (0, 0) in orb)
    need(averaged_p[diag_orbit] == 1 and all(c == 0 for i, c in enumerate(averaged_p) if i != diag_orbit),
         'B5', 'scaled preparation is unital')
    for ga in g_orbits:
        for hx in h_orbits:
            left = F(len(ga & frozenset((j, i) for i, j in hx)), 18)
            right_sum = F(0)
            for i, j in ga:
                rev_orbit = g_orbits[pair_to_g[(j, i)]]
                right_sum += ratio * F(len(rev_orbit & hx), len(rev_orbit))
            right = right_sum / 45
            need(left == right, 'B5', 'compression and preparation trace pairing')


def expand_left(inner, outer, red=False):
    out, cursor = [], 0
    for letter in outer:
        if letter == 0:
            value = inner[cursor]
            cursor += 1
            out.append(2 if red and len(out) == 0 else value)
        else:
            out.append(2)
    return tuple(out)


def expand_right(inner, outer):
    out, cursor = [], 0
    for letter in outer:
        if letter == 0:
            out.append(0)
        else:
            out.append(inner[cursor] + 1)
            cursor += 1
    return tuple(out)


def shuffle_tests(args):
    for l, m, n in ((1, 1, 1), (1, 1, 2), (1, 2, 1)):
        ternary = set(shuffle_words((l, m, n)))
        left = {expand_left(inner, outer, args.red_shuffle)
                for inner in shuffle_words((l, m))
                for outer in shuffle_words((l+m, n))}
        right = {expand_right(inner, outer)
                 for inner in shuffle_words((m, n))
                 for outer in shuffle_words((l, m+n))}
        need(left == ternary and right == ternary and len(left) == len(right),
             'B6', f'ternary shuffle coherence {(l,m,n)}')


def thin_type_c_tests(args):
    for m, n in ((1, 1), (1, 2), (2, 2), (1, 3)):
        size = m+n
        representatives = set()
        count = 0
        for w in permutations(range(1, size+1)):
            for signs in product((-1, 1), repeat=size):
                g = tuple(a*b for a, b in zip(w, signs))
                subset = sorted(abs(x) for x in g[:m])
                s = tuple(subset+[x for x in range(1, size+1) if x not in subset])
                representatives.add(s)
                inverse_s = {x: i+1 for i, x in enumerate(s)}
                h = tuple((1 if x > 0 else -1)*inverse_s[abs(x)] for x in g)
                if args.red_thin_block:
                    h = (-h[0],)+h[1:]
                restored = tuple((1 if x > 0 else -1)*s[abs(x)-1] for x in h)
                need(restored == g and set(abs(x) for x in h[:m]) == set(range(1, m+1)),
                     'B6', 'signed block factorization through an unsigned shuffle')
                count += 1
        local_order = 2**size*factorial(m)*factorial(n)
        need(count == 2**size*factorial(size) and len(representatives) == comb(size, m)
             and count == local_order*len(representatives), 'B6', 'thin type-C index and normalized endpoint fraction')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--red-fourier', action='store_true',
                        help='B3: replace the rank-one annihilator by the whole dual')
    parser.add_argument('--red-dual-reversal', action='store_true',
                        help='B3: omit reversal of the first dual flag index')
    parser.add_argument('--red-typec-scale', action='store_true',
                        help='B5: omit the inverse decomposable-fraction scale')
    parser.add_argument('--red-shuffle', action='store_true',
                        help='B6: send the first left-expanded letter to the wrong summand')
    parser.add_argument('--red-thin-block', action='store_true',
                        help='B6: change a sign in the recovered block factor')
    args = parser.parse_args()
    print('MODE:', ','.join(k for k, v in vars(args).items() if v) or 'green')
    fourier_tests(args)
    dual_flag_tests(args)
    type_c_tests(args)
    shuffle_tests(args)
    thin_type_c_tests(args)
    for gate in ('B3', 'B5', 'B6'):
        if gate in FAILED:
            print('FAIL '+gate+': '+'; '.join(sorted(FAILED[gate])))
        else:
            print(f'{gate} PASS: {CHECKED.get(gate, 0)} exact probes')
    if FAILED:
        raise SystemExit(1)
    print('ALL BRIDGE EXAMPLES PASSED (finite exact probes)')


if __name__ == '__main__':
    main()
