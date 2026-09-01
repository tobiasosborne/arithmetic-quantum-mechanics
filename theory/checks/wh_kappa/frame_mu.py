#!/usr/bin/env python3
"""COMP-M: at which LEVEL does the polarizing cocycle matter?

Lane wh-repair.  Exact: phases are exponents in Z/4 (p=2) or Z/p (p odd); no
complex numbers are ever formed, no floats, no tolerance.

Fix admissible beta, beta' = beta + s (s symmetric kappa-bilinear).  A
FRAME ISOMORPHISM A_psi^beta -> A_psi^{beta'} over the identity of V is
    phi(W_beta(v)) = mu(v) W_{beta'}(v),   mu : V -> C^x,
and phi is multiplicative iff

    (F)   mu(v) mu(v') / mu(v+v')  =  psi(beta(v,v') - beta'(v,v')) = psi(-s(v,v')).

Gates:
  M1  p=2, q=2: EXHAUSTIVE search over all 2^{q^2} functions mu : V -> mu_2
      reproduces the criterion "a mu_2-valued solution of (F) exists iff
      psi(s(v,v)) = 1 for every v".  (Cross-check on M2/M3's algebra.)
  M2  p=2, all q: NECESSITY, mu(v)^2 = psi(s(v,v)) for any solution of (F)
      (verified as an identity on the constructed solutions), and SUFFICIENCY:
      when psi o s vanishes on the diagonal the explicit
      l(v) = sum_{i<j} c_i c_j sigma_ij gives a mu_2 solution -- verified on all
      pairs, for every admissible beta'.
  M3  p=2, all q: mu_4 ALWAYS suffices: m(v) = 2 sum_{i<j} c_i c_j sigma_ij
      + sum_i c_i sigma_ii  in Z/4 solves (F) for EVERY admissible beta', on all
      pairs; and m takes an odd value (a phase of exact order 4) exactly when no
      mu_2 solution exists.
  M4  p odd, all q: mu(v) = psi(s(v,v)/2) solves (F) for every admissible beta',
      so at odd p the frame isomorphism stays inside mu_p.

Consequence (this is the point): the pair (algebra, Weyl frame) does not depend
on beta at any characteristic; the mu_p-level structure -- the finite Heisenberg
group of Weyl operators -- does depend on beta at p = 2, and mu_4 is exactly the
price of moving between the two classes.

Red modes (each MUST exit non-zero):
  --red-drop-linear   omit the sum_i c_i sigma_ii term from m; M3 must fire
  --red-mu2-always    claim a mu_2 solution for every beta'; M1/M2 must fire
"""

import itertools
import sys

from ff import GF, factor_prime_power
from beta_census import Ctx

QS = (2, 3, 4, 5, 8, 9)
EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2
MODES = ("green", "--red-drop-linear", "--red-mu2-always")


def sym_tables(C):
    """(alpha,gamma,delta) -> symmetric kappa-bilinear s and its psi-exponent."""
    F, q, nV = C.F, C.q, C.nV
    out = {}
    for alpha in range(q):
        for gamma in range(q):
            for delta in range(q):
                S = []
                for i in range(nV):
                    a, b = C.A[i]
                    row = []
                    for j in range(nV):
                        ap, bp = C.A[j]
                        val = F.MUL[alpha][F.MUL[a][ap]]
                        val = F.ADD[val][F.MUL[gamma][F.ADD[F.MUL[a][bp]][F.MUL[ap][b]]]]
                        val = F.ADD[val][F.MUL[delta][F.MUL[b][bp]]]
                        row.append(val)
                    S.append(row)
                for i in range(nV):
                    for j in range(nV):
                        if S[i][j] != S[j][i]:
                            raise RuntimeError("s is not symmetric")
                out[(alpha, gamma, delta)] = S
    return out


def fp_basis(C):
    F, n = C.F, C.F.n
    e = [F.undigits([1 if t == k else 0 for t in range(n)]) for k in range(n)]
    return [C.IDX[(x, 0)] for x in e] + [C.IDX[(0, x)] for x in e]


def coords(C, basis, v):
    """F_p-coordinates of v on `basis` (p = 2 here: subset sum)."""
    for coeffs in itertools.product(range(C.F.p), repeat=len(basis)):
        w = 0
        for c, bvec in zip(coeffs, basis):
            for _ in range(c):
                w = C.VADD[w][bvec]
        if w == v:
            return coeffs
    raise RuntimeError("basis does not span V")


def main(argv):
    mode = "green"
    for a in argv[1:]:
        if a in MODES:
            mode = a
        else:
            print("unknown mode %r; modes: %s" % (a, " ".join(MODES)))
            return EXIT_NOT_CAUGHT
    fired = []

    def check(cond, q, tag, msg):
        if not cond:
            fired.append((q, tag, msg))
            print("q=%-2d %-3s FAIL %s" % (q, tag, msg))
        return cond

    print("frame_mu  mode=%s   phases as exponents in Z/4 or Z/p; no floats" % mode)
    for q in QS:
        p, n = factor_prime_power(q)
        F = GF(p, n)
        ok, msg = F.audit()
        if not check(ok, q, "F", msg):
            continue
        C = Ctx(F)
        nV = C.nV
        print("\n== kappa = F_%d (p=%d, n=%d) ==" % (q, p, n))
        SS = sym_tables(C)
        basis = fp_basis(C)
        CO = {v: coords(C, basis, v) for v in range(nV)} if p == 2 else None

        if p == 2:
            # ---- M1: exhaustive mu_2 search at q = 2 ----------------------
            if q == 2:
                for k, S in SS.items():
                    sigma = [[C.PSIEXP[S[i][j]] for j in range(nV)] for i in range(nV)]
                    found = None
                    for l in itertools.product(range(2), repeat=nV):
                        if l[0] != 0:
                            continue
                        if all((l[i] + l[j] + sigma[i][j]) % 2 == l[C.VADD[i][j]]
                               for i in range(nV) for j in range(nV)):
                            found = l
                            break
                    diag_ok = all(sigma[i][i] == 0 for i in range(nV))
                    if mode == "--red-mu2-always":
                        diag_ok = True
                    check((found is not None) == diag_ok, q, "M1",
                          "beta'=%s: exhaustive mu_2 search says %s, criterion says %s"
                          % (k, found is not None, diag_ok))
                nsol = sum(1 for k, S in SS.items()
                           if all(C.PSIEXP[S[i][i]] == 0 for i in range(nV)))
                print("q=%-2d M1  PASS exhaustive search over all 2^%d functions mu : V -> mu_2, "
                      "for all %d admissible beta': a solution exists for exactly the %d with "
                      "psi(s(v,v)) = 1 pointwise" % (q, nV, q ** 3, nsol))

            # ---- M2: necessity + explicit mu_2 solution -------------------
            bad = None
            nmu2 = 0
            for k, S in SS.items():
                sigma = [[C.PSIEXP[S[i][j]] for j in range(nV)] for i in range(nV)]
                if any(sigma[i][i] for i in range(nV)):
                    if mode == "--red-mu2-always":
                        bad = (k, "claimed a mu_2 solution but psi(s(v,v)) != 1 somewhere")
                        break
                    continue
                nmu2 += 1
                l = [0] * nV
                for v in range(nV):
                    c = CO[v]
                    acc = 0
                    supp = [i for i, x in enumerate(c) if x]
                    for x in range(len(supp)):
                        for y in range(x + 1, len(supp)):
                            acc ^= sigma[basis[supp[x]]][basis[supp[y]]]
                    l[v] = acc
                for i in range(nV):
                    for j in range(nV):
                        if (l[i] + l[j] + sigma[i][j]) % 2 != l[C.VADD[i][j]]:
                            bad = (k, "constructed mu_2 fails (F) at (%d,%d)" % (i, j))
                            break
                    if bad:
                        break
                if bad:
                    break
            check(bad is None, q, "M2", "%s" % (bad,))
            if bad is None:
                print("q=%-2d M2  PASS a mu_2 frame isomorphism exists for exactly the %d of %d "
                      "admissible beta' with psi o s diagonal-free, and the explicit l is verified "
                      "on all %d pairs" % (q, nmu2, q ** 3, nV ** 2))

            # ---- M3: mu_4 always ------------------------------------------
            bad = None
            nord4 = 0
            for k, S in SS.items():
                sigma = [[C.PSIEXP[S[i][j]] for j in range(nV)] for i in range(nV)]
                m = [0] * nV
                for v in range(nV):
                    c = CO[v]
                    supp = [i for i, x in enumerate(c) if x]
                    acc = 0
                    for x in range(len(supp)):
                        for y in range(x + 1, len(supp)):
                            acc = (acc + 2 * sigma[basis[supp[x]]][basis[supp[y]]]) % 4
                    if mode != "--red-drop-linear":
                        for x in supp:
                            acc = (acc + sigma[basis[x]][basis[x]]) % 4
                    m[v] = acc
                for i in range(nV):
                    for j in range(nV):
                        if (m[i] + m[j] - m[C.VADD[i][j]]) % 4 != (2 * sigma[i][j]) % 4:
                            bad = (k, "constructed mu_4 fails (F) at (%d,%d)" % (i, j))
                            break
                    if bad:
                        break
                if bad:
                    break
                odd = any(x % 2 for x in m)
                if odd:
                    nord4 += 1
                if odd == all(sigma[i][i] == 0 for i in range(nV)):
                    bad = (k, "order-4 phase present iff mu_2 solvable -- backwards")
                    break
                # necessity of order 4: mu(v)^2 = psi(s(v,v))
                for v in range(nV):
                    if (2 * m[v]) % 4 != (2 * sigma[v][v]) % 4:
                        bad = (k, "mu(v)^2 != psi(s(v,v)) at v=%d" % v)
                        break
                if bad:
                    break
            check(bad is None, q, "M3", "%s" % (bad,))
            if bad is None:
                print("q=%-2d M3  PASS a mu_4 frame isomorphism exists for ALL %d admissible beta' "
                      "(verified on all %d pairs each); it needs a phase of exact order 4 for "
                      "exactly the %d beta' with no mu_2 solution"
                      % (q, q ** 3, nV ** 2, nord4))
            continue

        # ---- M4: odd p, mu_p suffices -----------------------------------
        two = F.ADD[F.one][F.one]
        halfof = {F.MUL[two][x]: x for x in range(q)}
        bad = None
        for k, S in SS.items():
            mu = [C.PSIEXP[halfof[S[v][v]]] for v in range(nV)]
            for i in range(nV):
                for j in range(nV):
                    if (mu[i] + mu[j] - mu[C.VADD[i][j]]) % p != (-C.PSIEXP[S[i][j]]) % p:
                        bad = (k, "(F) fails at (%d,%d)" % (i, j))
                        break
                if bad:
                    break
            if bad:
                break
        check(bad is None, q, "M4", "%s" % (bad,))
        if bad is None:
            print("q=%-2d M4  PASS mu(v) = psi(s(v,v)/2) is a mu_p-valued frame isomorphism for all "
                  "%d admissible beta' (all %d pairs each): at odd p nothing leaves mu_p"
                  % (q, q ** 3, nV ** 2))

    print("\n---- summary (mode=%s) ----" % mode)
    if mode == "green":
        if fired:
            for q, tag, msg in fired:
                print("FAIL q=%-2d %s: %s" % (q, tag, msg))
            return EXIT_FIRED
        print("GREEN: every check passed for q in %s" % (list(QS),))
        return EXIT_OK
    if not fired:
        print("RED MODE NOT CAUGHT: no check fired. Checker defect, not a pass.")
        return EXIT_NOT_CAUGHT
    bytag = {}
    for q, tag, msg in fired:
        bytag.setdefault(tag, []).append(q)
    for tag in sorted(bytag):
        print("KILLED BY %s at q = %s" % (tag, sorted(set(bytag[tag]))))
    print("RED MODE %s CAUGHT: first = %s at q=%d, %d failures"
          % (mode, fired[0][1], fired[0][0], len(fired)))
    return EXIT_FIRED


if __name__ == "__main__":
    sys.exit(main(sys.argv))
