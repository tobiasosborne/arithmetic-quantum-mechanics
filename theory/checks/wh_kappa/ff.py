"""Exact finite-field arithmetic for lane wh-repair.  python3 only, no numpy,
no repo imports, no floats, no tolerances.  Written fresh in this lane; it
shares no code with theory/checks/wh_kappa_check.py or with the critic lane.

Elements of F_{p^n} are ints 0..q-1, base-p digits = polynomial coefficients,
reduced modulo a monic irreducible poly found and VERIFIED here by exhaustive
trial division.  Every table is built by definition and audited by axiom.
"""

import itertools


def _polymulmod(a, b, modpoly, p, n):
    """a,b: lists of n coeffs; modpoly: list of n coeffs of x^n = modpoly."""
    prod = [0] * (2 * n - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    prod[i + j] = (prod[i + j] + x * y) % p
    for d in range(2 * n - 2, n - 1, -1):
        c = prod[d]
        if c:
            prod[d] = 0
            for j in range(n):
                prod[d - n + j] = (prod[d - n + j] + c * modpoly[j]) % p
    return prod[:n]


def _is_irreducible(coeffs, p, n):
    """coeffs = [c0..c_{n-1}] of monic f = x^n - sum c_i x^i.  Exhaustive:
    f is irreducible over F_p iff no monic poly of degree 1..n//2 divides it."""
    f = [(-c) % p for c in coeffs] + [1]              # ascending, monic
    for d in range(1, n // 2 + 1):
        for tail in itertools.product(range(p), repeat=d):
            g = list(tail) + [1]
            r = list(f)
            for k in range(len(r) - 1, d - 1, -1):
                c = r[k]
                if c:
                    for j in range(d + 1):
                        r[k - d + j] = (r[k - d + j] - c * g[j]) % p
            if all(x == 0 for x in r):
                return False
    return True


class GF:
    def __init__(self, p, n):
        self.p, self.n, self.q = p, n, p ** n
        q = self.q
        self.modpoly = None
        for coeffs in itertools.product(range(p), repeat=n):
            if _is_irreducible(list(coeffs), p, n):
                self.modpoly = list(coeffs)
                break
        if self.modpoly is None:
            raise RuntimeError("no irreducible polynomial of degree %d over F_%d" % (n, p))
        self.dig = [self.digits(x) for x in range(q)]
        self.ADD = [[self.undigits([(u + v) % p for u, v in zip(self.dig[x], self.dig[y])])
                     for y in range(q)] for x in range(q)]
        self.NEG = [self.undigits([(-u) % p for u in self.dig[x]]) for x in range(q)]
        self.MUL = [[self.undigits(_polymulmod(self.dig[x], self.dig[y], self.modpoly, p, n))
                     for y in range(q)] for x in range(q)]
        self.one = 1 % q if n == 1 else self.undigits([1] + [0] * (n - 1))
        # absolute trace z + z^p + ... + z^{p^{n-1}}
        self.TR = []
        for x in range(q):
            acc, cur = 0, x
            for _ in range(n):
                acc = self.ADD[acc][cur]
                cur = self.pow(cur, p)
            self.TR.append(acc)
        self.INV = [None] * q
        for x in range(1, q):
            for y in range(1, q):
                if self.MUL[x][y] == self.one:
                    self.INV[x] = y
                    break

    def digits(self, x):
        d, p = [], self.p
        for _ in range(self.n):
            d.append(x % p)
            x //= p
        return d

    def undigits(self, d):
        acc = 0
        for u in reversed(d):
            acc = acc * self.p + (u % self.p)
        return acc

    def pow(self, x, k):
        r = self.one
        for _ in range(k):
            r = self.MUL[r][x]
        return r

    def sub(self, x, y):
        return self.ADD[x][self.NEG[y]]

    def audit(self):
        """Field axioms, exhaustively.  Returns (ok, message)."""
        p, n, q = self.p, self.n, self.q
        A, M, one = self.ADD, self.MUL, self.one
        for x in range(q):
            if A[x][0] != x or M[x][one] != x:
                return False, "identity fails at %d" % x
            if A[x][self.NEG[x]] != 0:
                return False, "additive inverse fails at %d" % x
            if x and self.INV[x] is None:
                return False, "no multiplicative inverse for %d" % x
        for x in range(q):
            for y in range(q):
                if A[x][y] != A[y][x] or M[x][y] != M[y][x]:
                    return False, "commutativity fails at (%d,%d)" % (x, y)
                for z in range(q):
                    if A[A[x][y]][z] != A[x][A[y][z]]:
                        return False, "additive associativity fails"
                    if M[M[x][y]][z] != M[x][M[y][z]]:
                        return False, "multiplicative associativity fails"
                    if M[x][A[y][z]] != A[M[x][y]][M[x][z]]:
                        return False, "distributivity fails"
        acc = 0
        for _ in range(p):
            acc = A[acc][one]
        if acc != 0:
            return False, "characteristic is not %d" % p
        # trace lands in the prime field and is F_p-linear and onto
        prime = set()
        acc = 0
        for _ in range(p):
            prime.add(acc)
            acc = A[acc][one]
        for x in range(q):
            if self.TR[x] not in prime:
                return False, "Tr(%d) is not in the prime field" % x
            for y in range(q):
                if self.TR[A[x][y]] != A[self.TR[x]][self.TR[y]]:
                    return False, "Tr is not additive"
        if len(set(self.TR)) != p:
            return False, "Tr is not onto the prime field"
        return True, ("F_%d^%d: %d elements, modpoly digits %s, axioms exhaustive, "
                      "Tr onto F_%d" % (p, n, q, self.modpoly, p))


def factor_prime_power(q):
    p = 2
    while p * p <= q:
        if q % p == 0:
            break
        p += 1
    else:
        p = q
    n, r = 0, q
    while r % p == 0:
        r //= p
        n += 1
    if r != 1:
        raise ValueError("%d is not a prime power" % q)
    return p, n
