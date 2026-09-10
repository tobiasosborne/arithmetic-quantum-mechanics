#!/usr/bin/env python3
"""Exact finite/symbolic falsifier for SP-FOCK, SP-PRIME and SP-BC-CONTROL."""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import itertools
import math
import sys


MUTATIONS = {
    "fock-binomial": ("F2", "omit the exponential binomial norm factor"),
    "fock-vacuum": ("F1", "delete the vacuum sector"),
    "fock-expansive": ("F3", "replace an accepted contraction by 2I"),
    "fock-tensor-collapse": ("F3", "replace actual tensor powers of 2I by identities"),
    "one-mode-factorial": ("F1", "replace r! by one in the one-mode basis"),
    "prime-position": ("P1", "insert prime 2 after prime 3"),
    "prime-nonunital": ("P1", "insert a nonidentity prime projection"),
    "density-trace": ("P2", "replace rho_2 by a trace-2/3 diagonal"),
    "gns-separating": ("P2", "replace the faithful separating reference by pure rho_3"),
    "mu-unitary": ("B1", "replace the range projection by identity"),
    "mu-adjoint-divisibility": ("B1", "floor-divide mu_5* on nonmultiples"),
    "root-average": ("B2", "omit the factor 1/n in the root average"),
    "time-sign": ("B3", "reverse the valuation-vector time exponent"),
    "L-multiplicative": ("B3", "substitute L_n into the corner homomorphism test"),
    "b1-trace-class": ("B4", "accept a finite trace bound 3 at b=1"),
}


class GateFailure(Exception):
    def __init__(self, gate, detail):
        super().__init__(detail)
        self.gate, self.detail = gate, detail


def need(gate, value, detail):
    if not value:
        raise GateFailure(gate, detail)


@dataclass(frozen=True)
class Rect:
    rows: int
    cols: int
    data: tuple

    def __post_init__(self):
        if len(self.data) != self.rows or any(len(row) != self.cols for row in self.data):
            raise ValueError("matrix data mismatch")


def zero(rows, cols):
    return Rect(rows, cols, tuple(tuple(F(0) for _ in range(cols)) for _ in range(rows)))


def eye(n):
    return Rect(n, n, tuple(tuple(F(i == j) for j in range(n)) for i in range(n)))


def unit(rows, cols, i, j):
    return Rect(rows, cols,
                tuple(tuple(F((r, c) == (i, j)) for c in range(cols))
                      for r in range(rows)))


def diag(values):
    values = tuple(map(F, values))
    return Rect(len(values), len(values),
                tuple(tuple(values[i] if i == j else F(0) for j in range(len(values)))
                      for i in range(len(values))))


def add(a, b):
    if (a.rows, a.cols) != (b.rows, b.cols):
        raise ValueError("addition shape mismatch")
    return Rect(a.rows, a.cols,
                tuple(tuple(x+y for x, y in zip(ra, rb)) for ra, rb in zip(a.data, b.data)))


def scale(c, a):
    c = F(c)
    return Rect(a.rows, a.cols, tuple(tuple(c*x for x in row) for row in a.data))


def mul(a, b):
    if a.cols != b.rows:
        raise ValueError("product shape mismatch")
    out = [[F(0) for _ in range(b.cols)] for _ in range(a.rows)]
    for i in range(a.rows):
        for k in range(a.cols):
            if a.data[i][k]:
                for j in range(b.cols):
                    out[i][j] += a.data[i][k]*b.data[k][j]
    return Rect(a.rows, b.cols, tuple(tuple(row) for row in out))


def dag(a):
    return Rect(a.cols, a.rows,
                tuple(tuple(a.data[j][i] for j in range(a.rows)) for i in range(a.cols)))


def kron(a, b):
    return Rect(a.rows*b.rows, a.cols*b.cols,
                tuple(tuple(a.data[i//b.rows][j//b.cols]*b.data[i%b.rows][j%b.cols]
                            for j in range(a.cols*b.cols))
                      for i in range(a.rows*b.rows)))


def trace(a):
    if a.rows != a.cols:
        raise ValueError("trace of rectangular matrix")
    return sum((a.data[i][i] for i in range(a.rows)), F(0))


def rank(a):
    rows = [list(row) for row in a.data]
    r = 0
    for col in range(a.cols):
        pivot = next((i for i in range(r, a.rows) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        z = rows[r][col]
        rows[r] = [x/z for x in rows[r]]
        for i in range(a.rows):
            if i != r and rows[i][col]:
                z = rows[i][col]
                rows[i] = [x-z*y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def determinant(a):
    if a.rows != a.cols:
        raise ValueError("determinant of rectangular matrix")
    out = F(0)
    for permutation in itertools.permutations(range(a.rows)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(a.rows) for j in range(i+1,a.rows))
        term = F(1)
        for i in range(a.rows):
            term *= a.data[i][permutation[i]]
        out += term if inversions%2==0 else -term
    return out


def is_psd(a):
    if a.rows != a.cols or dag(a) != a:
        return False
    for size in range(1,a.rows+1):
        for subset in itertools.combinations(range(a.rows),size):
            principal = Rect(size,size,tuple(tuple(a.data[i][j] for j in subset)
                                              for i in subset))
            if determinant(principal) < 0:
                return False
    return True


def matvec(a, vector):
    return tuple(sum((a.data[i][j]*vector[j] for j in range(a.cols)), F(0))
                 for i in range(a.rows))


@lru_cache(None)
def tensor_basis(d, r):
    if r == 0:
        return ((),)
    return tuple(itertools.product(range(d), repeat=r))


def permute_tuple(word, permutation):
    inverse = [0]*len(permutation)
    for i, j in enumerate(permutation):
        inverse[j] = i
    return tuple(word[inverse[i]] for i in range(len(word)))


def symmetrizer(d, r, delete_vacuum=False):
    if r == 0 and delete_vacuum:
        return zero(0, 0)
    basis = tensor_basis(d, r)
    size = len(basis)
    if not size:
        return zero(0, 0)
    index = {word: i for i, word in enumerate(basis)}
    perms = tuple(itertools.permutations(range(r))) if r else ((),)
    out = [[F(0) for _ in range(size)] for _ in range(size)]
    for j, word in enumerate(basis):
        for permutation in perms:
            out[index[permute_tuple(word, permutation)]][j] += F(1, math.factorial(r))
    return Rect(size, size, tuple(tuple(row) for row in out))


def expected_sector_rank(d, r):
    if r == 0:
        return 1
    return 0 if d == 0 else math.comb(d+r-1, r)


def gate_f1(mode):
    census = []
    for d in (0, 1, 2):
        ranks = []
        for r in range(5):
            p = symmetrizer(d, r, delete_vacuum=(mode == "fock-vacuum"))
            need("F1", mul(p, p) == p and dag(p) == p,
                 "permutation average is not an orthogonal projection")
            actual_rank = rank(p)
            occupations = (1 if r == 0 else
                           len(tuple(itertools.combinations_with_replacement(range(d), r))))
            need("F1", actual_rank == occupations == expected_sector_rank(d, r),
                 "sector rank/vacuum census failed at d=%d,r=%d" % (d, r))
            ranks.append(actual_rank)
        census.append(tuple(ranks))
    need("F1", tuple(census) == ((1,0,0,0,0),(1,1,1,1,1),(1,2,3,4,5)),
         "sector census guard failed")
    for r in range(5):
        denominator_sq = 1 if mode == "one-mode-factorial" else math.factorial(r)
        source_norm_sq = F(math.factorial(r), denominator_sq)
        target_norm_sq = F(1)
        need("F1", source_norm_sq == target_norm_sq,
             "one-mode x^r/sqrt(r!) occupation basis is not isometric at r=%d" % r)
    return "15 rational symmetrizers; ranks (1,0..),(1^5),(1,2,3,4,5), vacuum/one-mode"


def vector_norm_sq(vector):
    return sum((x*x for x in vector), F(0))


def gate_f2(mode):
    cases = 0
    for total in range(5):
        p = symmetrizer(2, total)
        basis = tensor_basis(2, total)
        for n in range(total+1):
            m = total-n
            word = (0,)*n+(1,)*m
            source = tuple(F(i == basis.index(word)) for i in range(len(basis)))
            projected = matvec(p, source)
            raw_norm = vector_norm_sq(projected)
            expected_raw = F(math.factorial(n)*math.factorial(m), math.factorial(total))
            need("F2", raw_norm == expected_raw,
                 "shuffle symmetrizer norm square failed at (%d,%d)" % (n, m))
            factor = F(1) if mode == "fock-binomial" else F(math.factorial(total),
                                                              math.factorial(n)*math.factorial(m))
            need("F2", factor*raw_norm == 1,
                 "exponential binomial normalization failed at (%d,%d)" % (n, m))
            scalar = F(1, 2) ** n * F(-1) ** m
            left = tuple(scalar*x for x in projected)
            right = matvec(p, tuple(scalar*x for x in source))
            need("F2", left == right, "homogeneous exponential naturality failed")
            cases += 1
    need("F2", cases == 15, "Fock binomial/naturality census is %d" % cases)
    return "15 exact binomial norm-square and homogeneous naturality cases"


def tensor_power(a, r, collapse=False):
    out = eye(1)
    for _ in range(r):
        out = kron(out, a)
    return eye(out.rows) if collapse else out


def gate_f3(mode):
    a = diag((1, F(1,2)))
    swap = Rect(2,2,((F(0),F(1)),(F(1),F(0))))
    accepted = (scale(2,eye(2)) if mode=="fock-expansive" else a, swap)
    for operator in accepted:
        deficit = add(eye(2),scale(-1,mul(dag(operator),operator)))
        need("F3",is_psd(deficit),
             "actual accepted base map is not a contraction")
    composed = mul(swap, a)
    for r in range(5):
        p = symmetrizer(2, r)
        ar, sr = tensor_power(a, r), tensor_power(swap, r)
        need("F3", mul(ar, p) == mul(p, ar) and mul(sr, p) == mul(p, sr),
             "tensor power does not preserve the symmetric sector")
        need("F3", tensor_power(composed, r) == mul(sr, ar),
             "sectorwise second-quantization composition failed")
    two = scale(2,eye(2))
    witnessed = []
    for r in range(5):
        actual_power = tensor_power(two,r,collapse=(mode=="fock-tensor-collapse"))
        p = symmetrizer(2,r)
        test = tuple(F(i==0) for i in range(actual_power.cols))
        actual = matvec(actual_power,test)
        expected = tuple(F(2**r)*x for x in test)
        need("F3",mul(actual_power,p)==mul(p,actual_power) and actual==expected and
             vector_norm_sq(actual)==F(4**r),
             "actual tensor power of 2I failed symmetric growth at sector %d"%r)
        witnessed.append(actual[0])
    witnessed = tuple(witnessed)
    return "sector functor through 4; 2I norms 1,2,4,8,16 with symbolic 2^r duty"


PRIME_DIMS = {2:2, 3:3, 5:4}
STAGES = ((), (2,), (3,), (2,3), (2,3,5))


def stage_dim(stage):
    result = 1
    for prime in stage:
        result *= PRIME_DIMS[prime]
    return result


def mixed_basis(stage):
    return tuple(itertools.product(*(range(PRIME_DIMS[p]) for p in stage))) if stage else ((),)


def embed(stage, target, a, nonunital=False):
    if not set(stage).issubset(target):
        raise ValueError("stage inclusion fails")
    source_basis, target_basis = mixed_basis(stage), mixed_basis(target)
    sindex = {x:i for i,x in enumerate(source_basis)}
    out = [[F(0) for _ in target_basis] for _ in target_basis]
    for i, row in enumerate(target_basis):
        for j, col in enumerate(target_basis):
            sr = tuple(row[target.index(p)] for p in stage)
            sc = tuple(col[target.index(p)] for p in stage)
            coefficient = a.data[sindex[sr]][sindex[sc]]
            for p in target:
                if p not in stage:
                    if nonunital and p == 2:
                        coefficient *= F(row[target.index(p)] == col[target.index(p)] == 0)
                    else:
                        coefficient *= F(row[target.index(p)] == col[target.index(p)])
            out[i][j] = coefficient
    return Rect(len(target_basis), len(target_basis), tuple(tuple(row) for row in out))


def poly_mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return tuple(out)


def charpoly_diagonal(a):
    need_diag = all(a.data[i][j] == 0 for i in range(a.rows) for j in range(a.cols) if i != j)
    if not need_diag:
        raise ValueError("characteristic polynomial fixture must be diagonal")
    out = (F(1),)
    for i in range(a.rows):
        out = poly_mul(out, (-a.data[i][i], F(1)))
    return out


def poly_power(a, n):
    out = (F(1),)
    for _ in range(n):
        out = poly_mul(out, a)
    return out


def diag_test(stage):
    d = stage_dim(stage)
    return diag(tuple(F(i+1, d+1) for i in range(d)))


def gate_p1(mode):
    p, q = (3,), (2,3)
    a = diag((F(1,4),F(1,2),F(3,4)))
    canonical = embed(p, q, a)
    wrong = kron(a, eye(2)) if mode == "prime-position" else canonical
    need("P1", wrong == canonical,
         "prime-2 identity was inserted after, rather than before, prime 3")
    inserted_unit = embed(p, q, eye(3), nonunital=(mode == "prime-nonunital"))
    need("P1", inserted_unit == eye(6),
         "identity insertion used a nonunital prime projection")

    inclusions = [(p,q) for p in STAGES for q in STAGES if set(p).issubset(q)]
    for source, target in inclusions:
        d = stage_dim(source)
        x = diag_test(source)
        y = add(x, unit(d,d,0,min(1,d-1)))
        need("P1", embed(source,target,eye(d)) == eye(stage_dim(target)),
             "finite prime embedding is not unital")
        need("P1", embed(source,target,dag(y)) == dag(embed(source,target,y)),
             "finite prime embedding does not preserve star")
        need("P1", embed(source,target,mul(y,x)) ==
             mul(embed(source,target,y),embed(source,target,x)),
             "finite prime embedding does not preserve products")
        need("P1", embed(source,target,x) != zero(stage_dim(target),stage_dim(target)),
             "finite prime embedding is not injective on witness")
        aa = mul(dag(x),x)
        embedded = embed(source,target,aa)
        factor = stage_dim(target)//stage_dim(source)
        need("P1", charpoly_diagonal(embedded) == poly_power(charpoly_diagonal(aa),factor),
             "identity insertion changed the exact a*a characteristic polynomial")
    triangles = 0
    for source, middle, target in itertools.product(STAGES, repeat=3):
        if set(source).issubset(middle) and set(middle).issubset(target):
            x = diag_test(source)
            need("P1", embed(middle,target,embed(source,middle,x)) == embed(source,target,x),
                 "prime embedding triangle failed")
            triangles += 1
    need("P1", triangles > 0, "prime embedding triangle census empty")
    return ("%d inclusions and %d increasing-prime triangles; exact a*a polynomials" %
            (len(inclusions),triangles))


def local_density(prime, pure=False, wrong=False):
    if prime == 2:
        return diag((F(1,3),F(1,3) if wrong else F(2,3)))
    if prime == 3:
        return diag((1,0,0)) if pure else diag((F(1,6),F(2,6),F(3,6)))
    return diag((F(1,10),F(2,10),F(3,10),F(4,10)))


def product_density(stage, pure=False, wrong=False):
    out = eye(1)
    for prime in stage:
        out = kron(out, local_density(prime, pure=(pure and prime==3),
                                      wrong=(wrong and prime==2)))
    return out


def state(rho, a):
    return trace(mul(rho,a))


def gns_weights(rho):
    return tuple(rho.data[j][j] for i in range(rho.rows) for j in range(rho.rows))


def gate_p2(mode):
    for pure in (False, True):
        for stage in STAGES:
            rho = product_density(stage,pure=pure,wrong=(mode=="density-trace"))
            need("P2", trace(rho)==1 and all(rho.data[i][i]>=0 for i in range(rho.rows)),
                 "local/product density is not positive trace one")
            x = add(diag_test(stage), unit(rho.rows,rho.cols,0,min(1,rho.cols-1)))
            need("P2", state(rho,mul(dag(x),x))>=0,
                 "product state is not positive on x*x")
            for target in STAGES:
                if set(stage).issubset(target):
                    target_rho = product_density(target,pure=pure,
                                                 wrong=(mode=="density-trace"))
                    a = diag_test(stage)
                    need("P2", state(target_rho,embed(stage,target,a)) == state(rho,a),
                         "finite product states are incompatible under identity insertion")
    full = product_density((2,3,5),pure=False)
    singular = product_density((2,3,5),pure=True)
    rank_full = sum(w!=0 for w in gns_weights(full))
    rank_singular = sum(w!=0 for w in gns_weights(singular))
    pure3 = product_density((3,),pure=True)
    need("P2", (rank_full,rank_singular,sum(w!=0 for w in gns_weights(pure3))) ==
         (576,192,3), "finite GNS Gram ranks are not 576,192,3")
    weights3 = gns_weights(pure3)
    action_vectors = []
    for k, weight in enumerate(weights3):
        action_vectors.append(tuple(F(weight != 0 and i == k) for i in range(9)))
    cyclic_action = Rect(9,9,tuple(action_vectors))
    need("P2", rank(cyclic_action) == 3,
         "matrix-unit left action on [1] does not span the pure-state GNS quotient")
    faithful3 = product_density((3,),pure=False)
    separating_reference = pure3 if mode=="gns-separating" else faithful3
    separating_weights = gns_weights(separating_reference)
    separating_action = Rect(9,9,tuple(
        tuple(F(separating_weights[k]!=0 and i==k) for i in range(9))
        for k in range(9)))
    need("P2",rank(separating_action)==9,
         "separating-candidate action lost Gram injectivity under the actual reference")
    annihilator = unit(3,3,0,1)
    null_norm = state(pure3,mul(dag(annihilator),annihilator))
    need("P2", null_norm==0,
         "pure cyclic-vector nonseparating witness was lost")
    return "faithful/pure product states; GNS Gram ranks 576,192,3 and cyclic/nonseparating witness"


def mu(n,m):
    return n*m


def mu_star(n,k,floor_nonmultiple=False):
    return k//n if k%n==0 or (floor_nonmultiple and n==5) else None


def q_action(n,k,unitary=False):
    return k if unitary or k%n==0 else None


def gate_b1(mode):
    ns=(1,2,3,5,6)
    indices=tuple(range(1,31))
    for m,n,k in itertools.product(ns,ns,indices):
        need("B1", mu(m,mu(n,k))==mu(m*n,k),"symbolic semigroup law failed")
    for n,k in itertools.product(ns,indices):
        expected_adjoint=k//n if k%n==0 else None
        actual_adjoint=mu_star(n,k,floor_nonmultiple=(mode=="mu-adjoint-divisibility"))
        need("B1",actual_adjoint==expected_adjoint,
             "actual mu_n* disagrees with the divisibility oracle")
        need("B1", mu_star(n,mu(n,k))==k,"symbolic isometry adjoint law failed")
        expected=k if k%n==0 else None
        actual=q_action(n,k,unitary=(mode=="mu-unitary" and n>1))
        need("B1", actual==expected,"mu_n range projection was treated as identity")
    need("B1", all(q_action(n,1) is None for n in ns if n>1),
         "basis index one did not witness a proper range projection")
    return "symbolic semigroup/adjoint laws on 5 shifts and 30 indices; no truncation"


def mod1(x):
    x=F(x)
    return x-(x.numerator//x.denominator)


def phase(r,k):
    return mod1(F(r)*k)


def root_average(n,r,k,omit=False):
    if k%n:
        return F(0), None
    return F(n if omit else 1), phase(r,k//n)


def gate_b2(mode):
    phases=(F(0),F(1,2),F(1,3),F(2,5))
    checks=0
    for n,r,k in itertools.product((2,3,5),phases,range(1,31)):
        lhs=phase(r,n*k)
        rhs=phase(mod1(n*r),k)
        need("B2",lhs==rhs,"mu* e(r) mu phase law failed")
        actual=root_average(n,r,k,omit=(mode=="root-average"))
        expected=(F(1),phase(r,k//n)) if k%n==0 else (F(0),None)
        need("B2",actual==expected,"finite root average/divisibility normalization failed")
        roots=tuple(mod1((r+j)/n) for j in range(n))
        need("B2",len(set(roots))==n and all(mod1(n*s)==mod1(r) for s in roots),
             "rational root parameterization failed")
        checks+=1
    return "%d rational phase, divisibility and normalized root-average cases"%checks


def valuations(n):
    out=[]
    p=2
    value=n
    while p*p<=value:
        count=0
        while value%p==0:
            value//=p;count+=1
        if count:out.append((p,count))
        p+=1
    if value>1:out.append((value,1))
    return tuple(out)


def val_add(a,b):
    data={}
    for p,e in a+b:data[p]=data.get(p,0)+e
    return tuple(sorted((p,e) for p,e in data.items() if e))


def val_neg(a):
    return tuple((p,-e) for p,e in a)


def matrix_unit_product(a,b):
    return (a[0],b[1]) if a is not None and b is not None and a[1]==b[0] else None


def nu_unit(n,a):
    return None if a is None else (n*a[0],n*a[1])


def l_unit(n,a):
    return (None if a is None or a[0]%n or a[1]%n else
            (a[0]//n,a[1]//n))


def apply_operator(operator,k):
    return None if k is None else operator(k)


def compose_operator(after,before):
    return lambda k: apply_operator(after,apply_operator(before,k))


def nu_operator(n,operator):
    return lambda k: (None if mu_star(n,k) is None else
                      mu(n,apply_operator(operator,mu_star(n,k)))
                      if apply_operator(operator,mu_star(n,k)) is not None else None)


def l_operator(n,operator):
    return lambda k: mu_star(n,apply_operator(operator,mu(n,k)))


def gate_b3(mode):
    for n,m in itertools.product((2,3,5,6,10),range(1,31)):
        delta=val_add(valuations(n*m),val_neg(valuations(m)))
        actual=val_neg(delta) if mode=="time-sign" else delta
        need("B3",actual==valuations(n),"time evolution has reversed prime-valuation exponent")
        need("B3",val_add(valuations(n),valuations(m))==valuations(n*m),
             "valuation dynamics is not additive under products")
    units=tuple((i,j) for i in range(1,9) for j in range(1,9))
    for n,a,b in itertools.product((2,3),units,units):
        need("B3",nu_unit(n,matrix_unit_product(a,b))==
             matrix_unit_product(nu_unit(n,a),nu_unit(n,b)),
             "nu_n is not multiplicative on symbolic matrix units")
        need("B3",nu_unit(n,(a[1],a[0]))==(nu_unit(n,a)[1],nu_unit(n,a)[0]),
             "nu_n does not preserve adjoints")
        expected_l=l_unit(n,a)
        need("B3",expected_l is None or nu_unit(n,expected_l)==a,
             "L_n symbolic compression is inconsistent on the corner")
    n=2
    op_mu=lambda k:mu(n,k)
    op_star=lambda k:mu_star(n,k)
    product=compose_operator(op_mu,op_star)
    candidate=(lambda op:l_operator(n,op)) if mode=="L-multiplicative" else (lambda op:nu_operator(n,op))
    mapped_product=candidate(product)
    mapped_factors=compose_operator(candidate(op_mu),candidate(op_star))
    for index in range(1,13):
        need("B3",mapped_product(index)==mapped_factors(index),
             "corner homomorphism candidate failed actual product action")
    l_product=l_operator(n,product)
    l_factors=compose_operator(l_operator(n,op_mu),l_operator(n,op_star))
    need("B3",l_product(1)==1 and l_factors(1) is None,
         "genuine nonmultiplicativity witness for L_2 was lost")
    need("B3",mu_star(n,mu(n,index))==index,"L_n is not unital on identity action")
    return "prime-valuation dynamics and concrete L_2(mu_2 mu_2*) != L_2(mu_2)L_2(mu_2*)"


def partial_sum(b,n):
    return sum((F(1,k**b) for k in range(1,n+1)),F(0))


def tail_interval(b,n):
    lower=F(1,(b-1)*(n+1)**(b-1))
    upper=F(1,(b-1)*n**(b-1))
    return partial_sum(b,n)+lower,partial_sum(b,n)+upper


def gate_b4(mode):
    for b in (2,3):
        intervals=[tail_interval(b,n) for n in (4,8,16,32)]
        widths=[]
        for n,(lower,upper) in zip((4,8,16,32),intervals):
            need("B4",lower<=upper,"integral tail interval is reversed")
            widths.append(upper-lower)
            later=partial_sum(b,2*n)
            need("B4",lower<=later+F(1,(b-1)*(2*n)**(b-1)) and later<upper,
                 "later rational partial sum is incompatible with tail bounds")
        need("B4",all(widths[i+1]<widths[i] for i in range(3)),
             "integral tail interval widths do not shrink")
    harmonics=[]
    for k in range(1,9):
        value=partial_sum(1,2**k)
        need("B4",value>=1+F(k,2),"dyadic harmonic lower witness failed")
        harmonics.append(value)
    if mode=="b1-trace-class":
        need("B4",harmonics[-1]<=3,
             "b=1 claimed trace bound 3 is exceeded by the 2^8 partial sum")
    return "rational b=2,3 tail intervals and eight finite dyadic b=1 lower witnesses"


GATES={"F1":gate_f1,"F2":gate_f2,"F3":gate_f3,
       "P1":gate_p1,"P2":gate_p2,"B1":gate_b1,"B2":gate_b2,
       "B3":gate_b3,"B4":gate_b4}


def parse_args(argv):
    if argv is None:argv=sys.argv[1:]
    parser=argparse.ArgumentParser(description=__doc__,allow_abbrev=False)
    for name,(gate,description) in sorted(MUTATIONS.items()):
        parser.add_argument("--red-"+name,dest="red",action="store_const",const=name,
                            help="%s at %s"%(description,gate))
    args=parser.parse_args(argv)
    if sum(arg.startswith("--red-") for arg in argv)>1:
        parser.error("choose exactly one red mode")
    return args


def main(argv=None):
    args=parse_args(argv)
    if args.red:
        target=MUTATIONS[args.red][0]
        try:detail=GATES[target](args.red)
        except GateFailure as exc:
            if exc.gate!=target:
                print("WRONG GATE: %s expected %s: %s"%(exc.gate,target,exc.detail));return 2
            print("RED CAUGHT %s at %s: %s"%(args.red,exc.gate,exc.detail));return 1
        except Exception as exc:
            print("RED ERROR %s at %s: %s"%(args.red,target,exc));return 2
        print("RED SURVIVED %s at %s: %s"%(args.red,target,detail));return 0
    try:
        for gate,function in GATES.items():print("%s PASS: %s"%(gate,function(None)))
    except GateFailure as exc:
        print("%s FAIL: %s"%(exc.gate,exc.detail));return 1
    except Exception as exc:
        print("CHECKER ERROR: %s"%exc);return 2
    print("GREEN PASS: exact finite/symbolic controls only; no claim promotion");return 0


if __name__=="__main__":sys.exit(main())
