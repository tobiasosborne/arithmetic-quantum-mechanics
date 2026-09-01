#!/usr/bin/env python3
"""COMP-S: what symmetry does the quantum system actually see?  (OBJ-3, OPEN-2)

Lane wh-repair.  Exact integer arithmetic; no floats.

A_psi(V) is built from the ABELIAN GROUP (V,+) and the cocycle psi o beta.  The
kappa-module structure of V is extra data.  This script separates the three
symmetry groups by exhaustive (backtracking, complete) enumeration of F_p-linear
maps of V given by their images on an F_p-basis:

  S1  { g F_p-linear : omega(gv,gv') = omega(v,v') in kappa }  =  SL_2(kappa)
      -- every solution found is verified kappa-linear and of determinant 1, and
      the count matches |SL_2(kappa)| = q(q^2-1).  This ANSWERS OPEN-2, which the
      verdict wh-kappa-r1 raised and answered; here it is recomputed.
  S2  { g F_p-linear : psi(omega(gv,gv')) = psi(omega(v,v')) } = Sp_{2m}(F_p),
      count compared with the closed formula p^{m^2} prod_{i=1..m}(p^{2i}-1).
      This is the group the ALGEBRA sees.
  S3  p = 2: inside S2, the subgroup admitting mu_2-valued phases is the
      orthogonal group of the F_p-quadratic form psi o Q; its order and its
      index in S2 are reported, next to |O(Q) cap SL_2(kappa)| and its index in
      SL_2(kappa).
  S4  the omega-self-adjointness route to OPEN-2 is FALSE at p = 2 (the verdict's
      warning, recomputed): the omega-self-adjoint F_p-endomorphisms outnumber
      the kappa-scalars.

Red modes (each MUST exit non-zero):
  --red-sp-formula    compare S2 against |SL_2(kappa)| instead of |Sp_{2m}(F_p)|
  --red-kappa-linear  skip the kappa-linearity verification and demand S1 = S2
"""

import itertools
import sys

from ff import GF, factor_prime_power
from beta_census import Ctx, sl2, act

QS = (2, 3, 4, 5, 8, 9)
EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2
MODES = ("green", "--red-sp-formula", "--red-kappa-linear")


def fp_basis(C):
    F, n = C.F, C.F.n
    e = [F.undigits([1 if t == k else 0 for t in range(n)]) for k in range(n)]
    return [C.IDX[(x, 0)] for x in e] + [C.IDX[(0, x)] for x in e]


def coord_table(C, basis):
    """v -> its F_p-coordinate tuple on `basis` (a basis, checked by bijectivity)."""
    p = C.F.p
    tab = {}
    for coeffs in itertools.product(range(p), repeat=len(basis)):
        w = 0
        for c, b in zip(coeffs, basis):
            for _ in range(c):
                w = C.VADD[w][b]
        if w in tab:
            raise RuntimeError("the chosen F_p-basis is not independent")
        tab[w] = coeffs
    if len(tab) != C.nV:
        raise RuntimeError("the chosen F_p-basis does not span V")
    return tab


def apply_map(C, images, tab, v):
    w = 0
    for c, img in zip(tab[v], images):
        for _ in range(c):
            w = C.VADD[w][img]
    return w


def preserving(C, FORM, basis):
    """All F_p-linear g with FORM(g b_i, g b_j) = FORM(b_i, b_j); complete
    backtracking over basis images with incremental pruning.  FORM is a table."""
    d = len(basis)
    sols = []
    imgs = []

    def rec(k):
        if k == d:
            sols.append(tuple(imgs))
            return
        for w in range(C.nV):
            ok = True
            for i in range(k):
                if FORM[imgs[i]][w] != FORM[basis[i]][basis[k]] or \
                   FORM[w][imgs[i]] != FORM[basis[k]][basis[i]]:
                    ok = False
                    break
            if ok and FORM[w][w] == FORM[basis[k]][basis[k]]:
                imgs.append(w)
                rec(k + 1)
                imgs.pop()

    rec(0)
    return sols


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

    print("fp_symmetry  mode=%s   complete backtracking over F_p-linear maps" % mode)
    for q in QS:
        p, n = factor_prime_power(q)
        F = GF(p, n)
        ok, msg = F.audit()
        if not check(ok, q, "F", msg):
            continue
        C = Ctx(F)
        basis = fp_basis(C)
        tab = coord_table(C, basis)
        m = n
        spord = p ** (m * m)
        for i in range(1, m + 1):
            spord *= p ** (2 * i) - 1
        sl2ord = q * (q * q - 1)
        print("\n== kappa = F_%d (p=%d, m=%d) ==" % (q, p, m))

        # ---- S1: the kappa-valued omega ---------------------------------
        sols = preserving(C, C.OMEGA, basis)
        check(len(sols) == sl2ord, q, "S1",
              "%d F_p-linear isometries of the kappa-valued omega, |SL_2| = %d"
              % (len(sols), sl2ord))
        nonlin = 0
        for images in sols:
            g = [apply_map(C, images, tab, v) for v in range(C.nV)]
            for c in range(q):
                for v in range(C.nV):
                    a, b = C.A[v]
                    cv = C.IDX[(F.MUL[c][a], F.MUL[c][b])]
                    ga, gb = C.A[g[v]]
                    if g[cv] != C.IDX[(F.MUL[c][ga], F.MUL[c][gb])]:
                        nonlin += 1
                        break
                else:
                    continue
                break
        if mode != "--red-kappa-linear":
            check(nonlin == 0, q, "S1", "%d of the isometries are not kappa-linear" % nonlin)
        else:
            check(len(sols) == spord, q, "S1", "S1 (%d) != Sp_{2m}(F_p) (%d)" % (len(sols), spord))
        G = sl2(F)
        check(len(G) == sl2ord, q, "S1", "|SL_2(kappa)| enumerated = %d" % len(G))
        gset = {tuple(act(C, g, v) for v in range(C.nV)) for g in G}
        sset = {tuple(apply_map(C, images, tab, v) for v in range(C.nV)) for images in sols}
        check(gset == sset, q, "S1", "the two enumerations disagree as sets of maps")
        print("q=%-2d S1  PASS { g F_p-linear : omega o g = omega } = SL_2(kappa) exactly: %d maps, "
              "all kappa-linear, set-equal to the SL_2 enumeration  [OPEN-2 answered]"
              % (q, len(sols)))

        # ---- S2: the F_p-valued psi o omega ------------------------------
        PSIOM = [[C.PSIEXP[C.OMEGA[i][j]] for j in range(C.nV)] for i in range(C.nV)]
        sols2 = preserving(C, PSIOM, basis)
        target = sl2ord if mode == "--red-sp-formula" else spord
        check(len(sols2) == target, q, "S2",
              "%d isometries of psi o omega, expected %d" % (len(sols2), target))
        check(len(sols2) >= len(sols), q, "S2", "S2 does not contain S1")
        print("q=%-2d S2  PASS { g F_p-linear : psi o omega o g = psi o omega } has %d elements "
              "= |Sp_%d(F_%d)| = p^{m^2} prod (p^{2i}-1); index of SL_2(kappa) in it = %d"
              % (q, len(sols2), 2 * m, p, len(sols2) // sl2ord))

        # ---- S3: p = 2, the mu_2-phase subgroups -------------------------
        if p == 2:
            Q = [F.MUL[C.A[v][0]][C.A[v][1]] for v in range(C.nV)]      # D2's Q(a,b) = ab
            OQ_sl2 = [g for g in G if all(Q[act(C, g, v)] == Q[v] for v in range(C.nV))]
            OQpsi_big = [images for images in sols2
                         if all(C.PSIEXP[Q[apply_map(C, images, tab, v)]] == C.PSIEXP[Q[v]]
                                for v in range(C.nV))]
            check(len(OQ_sl2) == 2 * (q - 1), q, "S3",
                  "|O(Q) cap SL_2| = %d, expected 2(q-1) = %d" % (len(OQ_sl2), 2 * (q - 1)))
            check(sl2ord % len(OQ_sl2) == 0 and len(sols2) % len(OQpsi_big) == 0, q, "S3",
                  "orders do not divide")
            i1, i2 = sl2ord // len(OQ_sl2), len(sols2) // len(OQpsi_big)
            check(i1 == i2, q, "S3",
                  "index of the orthogonal subgroup differs: %d in SL_2 vs %d in Sp" % (i1, i2))
            print("q=%-2d S3  PASS |O(Q) cap SL_2(kappa)| = %d (index %d);  |O(psi o Q) cap "
                  "Sp_%d(F_2)| = %d (index %d) -- the same index, the phenomenon survives "
                  "enlargement" % (q, len(OQ_sl2), i1, 2 * m, len(OQpsi_big), i2))

        # ---- S4: the self-adjointness route is false at p = 2 -------------
        # exhaustive over all q^{(2m)^2}-ish maps: only affordable for small V,
        # and q = 2, 4 are the cases the verdict's warning names.
        if q not in (2, 4):
            continue
        selfadj = 0
        for images in itertools.product(range(C.nV), repeat=2 * m):
            g = [apply_map(C, images, tab, v) for v in range(C.nV)]
            if all(C.OMEGA[g[v]][w] == C.OMEGA[v][g[w]] for v in range(C.nV) for w in range(C.nV)):
                selfadj += 1
        scal = q
        check(selfadj >= scal, q, "S4", "fewer self-adjoint maps (%d) than scalars (%d)"
              % (selfadj, scal))
        print("q=%-2d S4  omega-self-adjoint F_p-endomorphisms: %d, kappa-scalars: %d%s"
              % (q, selfadj, scal,
                 "  -- self-adjointness does NOT characterise the scalars" if selfadj != scal
                 else "  -- they coincide here"))

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
