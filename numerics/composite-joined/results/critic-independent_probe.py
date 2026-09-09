#!/usr/bin/env python3
"""Independent exact hostile probes; no checker/prover imports.

Only finite samples are certified here. The all-degree/all-real convergence
argument is audited in VERDICT.md. Rational beta=2 and rational t are exact.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import gcd


def require(ok, label):
    if not ok:
        raise AssertionError(label)


@lru_cache(None)
def mu(n):
    return 1 if n == 1 else -sum(mu(d) for d in range(1, n) if n % d == 0)


def phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def c(n, x):
    return sum(mu(n // d) * x**d for d in range(1, n + 1) if n % d == 0)


def b(n, x):
    return x - 1 if n == 1 else c(n, x)


def v(n, s, t):
    return F(phi(n), n) if t == 1 else c(n, t**s) / (n * t**(s*n) * s * (t-1))


def remainder(poly, divisor, p):
    out = list(poly)
    while len(out) >= len(divisor):
        coefficient = out[-1]
        shift = len(out) - len(divisor)
        for j, value in enumerate(divisor):
            out[shift + j] = (out[shift + j] - coefficient * value) % p
        out.pop()
    return out


class Field:
    def __init__(self, p, r):
        self.p, self.r, self.q = p, r, p**r
        for low in product(range(p), repeat=r):
            candidate = low + (1,)
            if all(any(remainder(candidate, factor + (1,), p))
                   for degree in range(1, r//2 + 1)
                   for factor in product(range(p), repeat=degree)):
                self.modulus = candidate
                break
        else:
            raise AssertionError("no irreducible polynomial")

    def digits(self, x):
        result = []
        for _ in range(self.r):
            result.append(x % self.p)
            x //= self.p
        return result

    @lru_cache(None)
    def multiply(self, x, y):
        aa, bb = self.digits(x), self.digits(y)
        value = [0] * (2*self.r - 1)
        for i in range(self.r):
            for j in range(self.r):
                value[i+j] = (value[i+j] + aa[i]*bb[j]) % self.p
        reduced = remainder(value, self.modulus, self.p)
        return sum(a*self.p**i for i, a in enumerate(reduced))

    def power(self, x, n):
        result = 1
        while n:
            if n % 2:
                result = self.multiply(result, x)
            x = self.multiply(x, x)
            n //= 2
        return result

    def orbit(self, x, s):
        result = [x]
        y = self.power(x, self.p**s)
        while y != x:
            result.append(y)
            y = self.power(y, self.p**s)
        return tuple(result)


def physical_case(p, s, d, t, mutant):
    field = Field(p, s*d)
    rho = []
    for x in range(field.q):
        e = len(field.orbit(x, 1))
        rho.append(t**(-s*d) if x == 0 else b(e, t)/b(e, F(p))*t**(-s*d))
    require(sum(rho) == 1 and min(rho) > 0, "P1 actual reference normalization")
    if mutant:
        rho[1] += F(1, 100)  # falsifies actual field-label probability data
    primitive_mass = F(0)
    success = F(0)
    visited = set()
    common = [[F(0) for _ in range(d)] for _ in range(d)]
    for x in range(field.q):
        if x in visited:
            continue
        orbit = field.orbit(x, s)
        visited.update(orbit)
        if len(orbit) != d:
            continue
        require(len(set(rho[y] for y in orbit)) == 1, "P1 orbit-uniform reference")
        primitive_mass += sum(rho[y] for y in orbit)
        # Build actual multiplication graph tuples; distinct relative k matter.
        graphs = [tuple((y, orbit[(i+k) % d],
                         field.multiply(y, orbit[(i+k) % d]))
                        for i, y in enumerate(orbit)) for k in range(d)]
        require(len(set(z for row in graphs for z in row)) == d*d,
                "P1 graph orthogonality")
        # T C |y> has d amplitudes 1/d. Form its physical density explicitly.
        copied_density = {(a, z): sum(rho[y] for y in orbit)/d**2
                          for a in graphs[0] for z in graphs[0]}
        mass = sum(value for (a, z), value in copied_density.items() if a == z)
        success += mass
        restricted = [[sum(copied_density.get((a, z), F(0))
                           for a in graphs[k] for z in graphs[ell])/d
                       for ell in range(d)] for k in range(d)]
        require(restricted[0][0] == mass and
                sum(sum(row) for row in restricted) == mass,
                "P1 actual common pure restriction")
        # Frobenius advances second control and recomputes multiplication.
        moved = [tuple((a, field.power(y, p**s),
                        field.multiply(a, field.power(y, p**s)))
                       for a, y, _ in row) for row in graphs]
        require(all(moved[k] == graphs[(k+1) % d] for k in range(d)),
                "P1 actual relative Frobenius")
        full = sum(copied_density.values())/d
        identity = sum(copied_density.get((a, z), F(0))
                       for a in graphs[1] for z in graphs[1])/d
        dephased = sum(value for (a, z), value in copied_density.items() if a == z)/d
        require((full, identity, dephased) == (mass, 0, mass/d),
                "P1 coherent/dephased witness")
        for j in range(d):
            for k in range(d):
                for ell in range(d):
                    common[(k+j) % d][(ell+j) % d] += restricted[k][ell]/d
    cut_fail = sum(rho[x] for x in range(field.q) if len(field.orbit(x, s)) != d)
    avg_fail = primitive_mass - success
    require(cut_fail + avg_fail + success == 1, "P1 retained-history total")
    require(success == c(d, t**s)/(d*t**(s*d)), "P1 field vs period success")
    require(all(common[k][ell] == (success/d if k == ell else 0)
                for k in range(d) for ell in range(d)), "P1 twirled scalar block")
    return success, (cut_fail, avg_fail, success)


def p1(red):
    results = {}
    for p, s, d in [(2,1,2),(2,1,3),(3,1,2),(3,1,3),(2,2,2),(2,2,3),(3,2,2)]:
        results[p,s,d] = physical_case(p,s,d,F(3,2),red == "field")
    prior = {2:F(9,13), 3:F(4,13)}  # beta=2, D=3, independently reduced
    for p, s in [(2,1),(3,1),(2,2)]:
        histories = [prior[d]*rate for d in [2,3] for rate in results[p,s,d][1]]
        require(sum(histories) == 1, "P1 finite tagged history normalization")
        total = sum(prior[d]*results[p,s,d][0] for d in [2,3])
        require(total == s*F(1,2)*sum(F(1,d*d)*v(d,s,F(3,2)) for d in [2,3])/
                (F(1,4)+F(1,9)), "P1 assembled rescaled event rate")
    print("P1 PASS: actual fields p=2,3; s=1,2; copied density, coherence, tags, twirl")


def p2(red):
    for s in [1,2,3]:
        for t in [F(1), F(1001,1000), F(6,5), F(2), F(3)]:
            for d in range(2,121):
                value = v(d,s,t)
                if red == "coefficient" and d == 6:
                    value += 1  # falsifies the observed coefficient data
                require(0 < value <= 1, "P2 all-sampled-degree coefficient bound")
                derivative = sum(mu(d//e)*s*e for e in range(1,d+1) if d % e == 0)
                require(derivative == s*phi(d), "P2 derivative vs residue count")
            value2 = v(2,s,t)
            require(value2 == sum(t**(-j) for j in range(1,s+1))/(2*s),
                    "P2 degree-two finite-sum identity")
            require(value2 >= F(1,2)*F(3)**(-s), "P2 uniform normalizer floor")
    print("P2 PASS: exact rational degrees 2..120; s=1,2,3; near-one and finite t")


def p3(red):
    for s in [1,2]:
        for t in [F(1),F(101,100),F(6,5)]:
            gs = {d:F(1,d*d)*v(d,s,t) for d in range(2,161)}
            zn = sum(gs.values())
            for cutoff in [2,8,32,80]:
                zd = sum(value for d,value in gs.items() if d <= cutoff)
                eigen_distance = sum(d*abs(value/(d*zd) - value/(d*zn))
                                     if d <= cutoff else d*abs(value/(d*zn))
                                     for d,value in gs.items())
                tail_identity = 2*(zn-zd)/zn
                if red == "tail":
                    tail_identity /= 2
                require(eigen_distance == tail_identity, "P3 exact trace-norm tail")
                require(eigen_distance <= 16*F(6,5)**s/cutoff,
                        "P3 uniform integer-cutoff constant")
                eigen_total = sum(d*gs[d]/(d*zd) for d in gs if d <= cutoff)
                require(eigen_total == 1, "P3 normalized ordinary trace")
    # Nonstationary hypothetical scalar probe cannot distinguish R from identity:
    # the twirled matrix is I/d, while |0><0| is moved orthogonally.
    print("P3 PASS: exact normalized block eigenvalues, factor-two tails, uniform bound")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--red", choices=["field","coefficient","tail"])
    args = parser.parse_args()
    p1(args.red)
    p2(args.red)
    p3(args.red)


if __name__ == "__main__":
    main()
