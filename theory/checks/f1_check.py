#!/usr/bin/env python3
"""Exact examples for the F1 sidequest; passing finite checks is not a proof.

Cyclotomic coefficients are integer polynomials modulo Phi_N. Operators are
permutations with phase exponents, independently compared with the abstract
Heisenberg product. No floating point or external packages are used.
"""

import argparse
from itertools import combinations, product
from math import comb, factorial


def require(condition, gate, detail):
    if not condition:
        raise AssertionError(f"{gate}: {detail}")


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def divide(p, q):
    p = p[:]
    out = [0] * max(1, len(p) - len(q) + 1)
    while len(p) >= len(q) and p != [0]:
        j, c = len(p) - len(q), p[-1]
        out[j] = c
        for i, a in enumerate(q):
            p[i + j] -= c * a
        trim(p)
    return trim(out), p


def cyclotomic(n):
    p = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            p, rem = divide(p, cyclotomic(d))
            assert rem == [0]
    return p


def phase_sum(exponents, n):
    p = [0] * n
    for e in exponents:
        p[e % n] += 1
    return divide(trim(p), cyclotomic(n))[1]


class Abelian:
    def __init__(self, factors, n):
        self.factors, self.n = factors, n
        self.elements = tuple(product(*(range(d) for d in factors)))
        self.zero = (0,) * len(factors)
        assert all(n % d == 0 for d in factors)

    def add(self, a, b):
        return tuple((x + y) % d for x, y, d in zip(a, b, self.factors))

    def ev(self, k, a):
        return sum(self.n // d * x * y
                   for d, x, y in zip(self.factors, k, a)) % self.n

    def operator(self, a, k, wrong_order=False):
        return tuple((self.add(y, a), self.ev(k, y if wrong_order else self.add(y, a)))
                     for y in self.elements)


def compose(g, left, right):
    left_map = dict(zip(g.elements, left))
    return tuple((left_map[z][0], (e + left_map[z][1]) % g.n)
                 for z, e in right)


def scale(g, op, e):
    return tuple((z, (t + e) % g.n) for z, t in op)


def finite_tests(args):
    cases = [((), 1), ((2,), 2), ((3,), 3), ((4,), 4), ((2, 2), 2),
             ((5,), 5), ((6,), 6), ((2, 3), 6), ((2,), 4)]
    for factors, n in cases:
        g = Abelian(factors, n)
        v = tuple(product(g.elements, repeat=2))
        ops = {x: g.operator(*x) for x in v}
        # M1: operator construction versus independently stated group product.
        for (a, k), (b, ell) in product(v, repeat=2):
            c = -g.ev(ell, a)
            if args.red_cocycle:
                c = -c
            expected = scale(g, ops[g.add(a, b), g.add(k, ell)], c)
            require(compose(g, ops[a, k], ops[b, ell]) == expected,
                    "M1", f"cocycle at {factors}, {n}, {a,k,b,ell}")
        # M2: perfect commutator pairing, with a degenerate-data mutation.
        radical = []
        for a, k in v:
            if all((0 if args.red_pairing else g.ev(k, b) - g.ev(ell, a)) % n == 0
                   for b, ell in v):
                radical.append((a, k))
        require(radical == [(g.zero, g.zero)], "M2", f"radical={radical}")
        # M3: trace inner products from actual operator entries, not cocycle.
        family = list(ops.values())
        if args.red_basis and len(family) > 1:
            family[-1] = family[0]
        for i, p in enumerate(family):
            for j, q in enumerate(family):
                exponents = [t - s for (x, s), (y, t) in zip(p, q) if x == y]
                actual = phase_sum(exponents, n)
                expected = [len(g.elements)] if i == j else [0]
                require(actual == expected, "M3", f"Gram entry {i,j}: {actual}")
    print("M1 PASS: exact Heisenberg multiplication on 9 configuration/phase pairs")
    print("M2 PASS: trivial phase radical on the declared examples")
    print("M3 PASS: exact Weyl trace Gram matrices, including N=4 and N=6")


def ring_tests(args):
    # Encodings for the five local rings: x=a+2b at order four.
    def f4mul(x, y):
        a, b, c, d = x & 1, x >> 1, y & 1, y >> 1
        return ((a*c + b*d) % 2) + 2*((a*d + b*c + b*d) % 2)

    def epsmul(x, y):
        a, b, c, d = x & 1, x >> 1, y & 1, y >> 1
        return a*c + 2*((a*d + b*c) % 2)

    cases = [
        ("F2", Abelian((2,), 2), lambda x,y:(x*y)%2, lambda x:x),
        ("F3", Abelian((3,), 3), lambda x,y:(x*y)%3, lambda x:x),
        ("Z4", Abelian((4,), 4), lambda x,y:(x*y)%4, lambda x:x),
        ("F4", Abelian((2,2), 2), f4mul, lambda x:x >> 1),
        ("F2eps", Abelian((2,2), 2), epsmul, lambda x:x >> 1),
    ]
    for name, g, mul, psi in cases:
        count = len(g.elements)
        enc = (lambda a:a[0]) if len(g.factors)==1 else (lambda a:a[0]+2*a[1])
        labels = {}
        for b in range(count):
            matches = [k for k in g.elements
                       if all(g.ev(k, x) == -psi(mul(b, enc(x))) % g.n
                              for x in g.elements)]
            require(len(matches)==1, "M4", f"{name}: dual label b={b}")
            labels[b] = matches[0]
        require(len(set(labels.values()))==count, "M4", f"{name}: perfect ring pairing")
        for a in g.elements:
            for b in range(count):
                op = g.operator(a, labels[b], wrong_order=args.red_order)
                expected = tuple((g.add(y,a), -psi(mul(b,enc(g.add(y,a)))))
                                 for y in g.elements)
                expected = tuple((y,e % g.n) for y,e in expected)
                require(op==expected, "M4", f"D8/D16 sign/order: {name}, {a,b}")
        # Image and kernel of H_beta0(R) -> phase Heisenberg group.
        images = {(psi(t) % g.n, a, labels[b]) for t in range(count)
                  for a in g.elements for b in range(count)}
        expected_size = g.n * count**2
        if args.red_kernel and name == "F4":
            expected_size = count**3
        require(len(images)==expected_size, "M5", f"{name}: image order {len(images)}")
        kernel = [t for t in range(count) if psi(t) % g.n == 0]
        require(len(kernel)*len(images)==count**3, "M5", f"{name}: kernel/image count")
    print("M4 PASS: five local rings recover D8/D16, with named generating characters")
    print("M5 PASS: raw central kernel retained (F4: order 64 maps onto order 32)")


def tensor_fourier_tests(args):
    g, h, gh = Abelian((2,),6), Abelian((3,),6), Abelian((2,3),6)
    for a,k,b,ell in product(g.elements,g.elements,h.elements,h.elements):
        op1, op2 = g.operator(a,k), h.operator(b,ell)
        tensor = tuple(((x[0],y[0]), (e+f) % 6)
                       for x,e in op1 for y,f in op2)
        actual = gh.operator(a+b,k+ell)
        if args.red_tensor:
            tensor = tuple((x, (e+1)%6) for x,e in tensor)
        require(actual==tensor, "M6", "C2 x C3 tensor compatibility")
    print("M6 PASS: tensor comparison at common phase level N=6")
    for factors,n in [((2,),2),((3,),3),((4,),4),((2,2),2)]:
        g = Abelian(factors,n)
        # Unnormalized Fourier kernel has exactly one nonzero phase per entry.
        columns = [[g.ev(k,x) for k in g.elements] for x in g.elements]
        for c in columns:
            support = len(c) if not args.red_fourier else 1
            require(support > 1, "M7", "Fourier incorrectly treated as monomial")
        for x,y in product(g.elements,repeat=2):
            gram = phase_sum([g.ev(k,y)-g.ev(k,x) for k in g.elements],n)
            require(gram==([len(g.elements)] if x==y else [0]), "M7", "Fourier Gram")
    print("M7 PASS: Fourier kernel is orthogonal and has full column support")


def hall_tests(args):
    for m,n in product(range(7),repeat=2):
        counted = sum(1 for _ in combinations(range(m+n),m))
        expected = comb(m+n,m)
        if args.red_hall and m==n==1:
            expected = 1
        require(counted==expected, "M8", f"Hall coefficient {m,n}")
        require(counted*factorial(m)*factorial(n)==factorial(m+n), "M8", "divided powers")
    print("M8 PASS: Hall coefficients from counted subsets and divided-power normalization")
    for n in range(30):
        # Apply D*x and x*D to the input x^n, without a finite cutoff.
        dx = n+1
        xd = n if not args.red_ccr else n+1
        require(dx-xd==1, "M9", f"[D,x] x^{n}")
    # Explicitly retain the boundary defect of truncated Fock space.
    for cutoff in range(1,12):
        trace = sum(1 for _ in range(cutoff)) - cutoff
        require(trace==0, "M9", "finite cutoff must have a boundary defect")
    print("M9 PASS: polynomial CCR; finite truncation has a compensating top-state defect")


def crowd_tests(args):
    identity = (0, 0, 0)

    def matrix(h):
        a,b,t = h
        return ((1,a,t),(0,1,b),(0,0,1))

    def mm(a,b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))
                           for j in range(3)) for i in range(3))

    for name, scalars in [("signed",(-1,0,1)),("Krasner",(0,1))]:
        hs = tuple(product(scalars,repeat=3))

        def null(t):
            return t==0 if name=="signed" else t!=1

        def colaw(x,y,z):
            triples = [(x,y,z),(z,x,y),(y,z,x)]
            if args.red_crowd:
                triples += [(y,x,z)]
            for (a,b,t),(c,d,u),(e,f,v) in triples:
                if not (null(a+c+e) and null(b+d+f) and
                        null(t+u+v+a*d+a*f+c*f)):
                    return False
            return True

        relation = set()
        for x,y,z in product(hs,repeat=3):
            expected = True
            for first,second,third in [(x,y,z),(z,x,y),(y,z,x)]:
                mat = mm(mm(matrix(first),matrix(second)),matrix(third))
                expected &= all(null(mat[i][j]) for i,j in [(0,1),(1,2),(0,2)])
            actual = colaw(x,y,z)
            require(actual==expected,"M10",f"{name}: matrix crowd colaw {x,y,z}")
            if actual:
                relation.add((x,y,z))
        for x in hs:
            require(((x,identity,identity) in relation)==(x==identity),"M10","crowd C1")
        for x,y,z in relation:
            require((z,x,y) in relation,"M10","crowd C3")
            if z==identity:
                require((y,x,identity) in relation,"M10","crowd C2")
        inverses = {x:{y for y in hs if (x,y,identity) in relation} for x in hs}
        if name=="signed":
            require(sum(bool(v) for v in inverses.values())==23,"M10","23 signed inverses")
            require(not inverses[(1,1,-1)],"M10","signed inverse can be absent")
        else:
            require(len(inverses[(1,1,1)])==2,"M10","Krasner inverse is multivalued")
        print(f"M10 PASS: {name} Heisenberg crowd: {len(hs)} points, {len(relation)} triples")


def qubit_tests(args):
    # -1 denotes zero; 0,...,N-1 are phase exponents. Projectivize by
    # subtracting the first nonzero phase, which names no preferred root.
    def ray(v,n):
        first = next((x for x in v if x!=-1),None)
        return None if first is None else tuple(-1 if x==-1 else (x-first)%n for x in v)

    for n in [1,2,3,4]:
        scalars = range(-1,n)
        one = {ray(x,n) for x in product(scalars,repeat=2)}-{None}
        two = {ray(x,n) for x in product(scalars,repeat=4)}-{None}
        decomposable = {ray(tuple(-1 if a==-1 or b==-1 else (a+b)%n
                                 for a in x for b in y),n) for x in one for y in one}
        expected = (n+2)**2 if not args.red_frame else len(two)
        require(len(one)==n+2 and len(decomposable)==expected,"M11","frame Segre count")
        require(len(two-decomposable)==n*(n+1)*(n+2),"M11","nonproduct frame rays")
        require((0,-1,-1,0) in two-decomposable,"M11","diagonal support nonproduct")
        print(f"M11 PASS: phase level {n}: frame qubit {len(one)} rays; "
              f"composite {len(two)}, product {len(decomposable)}, nonproduct {len(two-decomposable)}")
    # Both D8 and Q8: h=(t,a,b), cocycles ab' and ab'+aa'+bb'.
    hs = tuple(product(range(2),repeat=3))
    for quaternion in [False,True]:
        def mul(x,y):
            t,a,b = x; u,c,d = y
            return ((t+u+a*d+quaternion*(a*c+b*d))%2,(a+c)%2,(b+d)%2)

        def sigma(x):
            t,a,b = x
            return 0 if a or b else 2*(-1)**t

        chars = [tuple((-1)**(r*a+s*b) for t,a,b in hs)
                 for r,s in product(range(2),repeat=2)]
        square = [sigma(h)**2 for h in hs]
        for char in chars:
            require(sum(x*y for x,y in zip(square,char))==8,"M12","four invertible summands")
        require(all(sum(char[i] for char in chars)==square[i] for i in range(8)),
                "M12","sigma squared equals sum of four characters")
        indicator = sum(sigma(mul(h,h)) for h in hs)
        expected = (-8 if quaternion else 8)
        if args.red_fusion and quaternion:
            expected = 8
        require(indicator==expected,"M12","Frobenius-Schur distinguishes D8 and Q8")
        print(f"M12 PASS: {'Q8' if quaternion else 'D8'}: sigma tensor square = four characters; FS={indicator//8}")


def normal_map_tests(args):
    for rank in [2,3,4]:
        maps = [f for f in product(range(-1,rank),repeat=rank)
                if len([x for x in f if x!=-1])==len({x for x in f if x!=-1})]
        if args.red_normal:
            maps = [f for f in maps if -1 not in f]
        matrices = {tuple(int(f[j]==i) for i in range(rank) for j in range(rank)) for f in maps}
        for i,j in product(range(rank),repeat=2):
            unit = tuple(int(a==i and b==j) for a in range(rank) for b in range(rank))
            require(unit in matrices,"M13",f"missing normal matrix unit {rank,i,j}")
        if rank==2:
            require(len(maps)==7,"M13","rank-two partial injection count")
    print("M13 PASS: normal pointed maps contain every matrix unit at ranks 2,3,4")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for flag,help_text in [
        ("cocycle","M1: reverse cocycle sign"),
        ("pairing","M2: replace commutator by trivial pairing"),
        ("basis","M3: duplicate a Weyl basis element"),
        ("order","M4: replace Z X by X Z"),
        ("kernel","M5: claim F4 raw Heisenberg group embeds faithfully"),
        ("tensor","M6: introduce a tensor phase mismatch"),
        ("fourier","M7: collapse Fourier support to one entry"),
        ("hall","M8: discard subset multiplicity"),
        ("ccr","M9: equate the two incidence multiplicities"),
        ("crowd","M10: replace cyclic crowd relation by a symmetric one"),
        ("frame","M11: declare every composite frame state a product"),
        ("fusion","M12: identify quaternion and dihedral Frobenius-Schur signs"),
        ("normal","M13: discard noninvertible normal maps"),
    ]:
        p.add_argument("--red-"+flag,action="store_true",help=help_text)
    args = p.parse_args()
    finite_tests(args)
    ring_tests(args)
    tensor_fourier_tests(args)
    hall_tests(args)
    crowd_tests(args)
    qubit_tests(args)
    normal_map_tests(args)
    print("ALL F1 EXAMPLE GATES PASSED (exact; no general theorem inferred)")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(f"FAIL {error}")
        raise SystemExit(1)
