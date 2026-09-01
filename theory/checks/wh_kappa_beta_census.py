#!/usr/bin/env python3
"""COMP-B: the polarizing cocycle is a second datum -- census and invariant.

Lane wh-repair.  Exact integer arithmetic in F_q and in Z/p exponents; no
floats, no tolerances, no repo imports beyond ./ff.py (written in this lane).

For every finite field kappa = F_q, q in QS, this enumerates the ADMISSIBLE
kappa-bilinear polarizing cocycles

    Adm(omega) = { beta' : V x V -> kappa  kappa-bilinear, beta' - beta'^T = omega }

(the only requirement briefs/wh-kappa-target.md places on beta), and reports:

  B1  Adm(omega) is a torsor under the symmetric kappa-bilinear forms: |Adm| = q^3,
      every member verified admissible and kappa-bilinear.
  B2  Adm(omega) contains an ANTISYMMETRIC member iff p is odd, and then exactly
      one, beta = omega/2; at p = 2 there is none.  (Why odd p has a canonical
      representative and p = 2 has none.)
  B3  element-order profile of H_{beta'}(kappa) = kappa x V, by brute force.
      Odd p: one profile.  p = 2: exactly two.
  B4  odd p: the EXPLICIT isomorphism phi(t,v) = (t + s(v,v)/2, v) from
      H_{beta_0} to H_{beta'} verified on all |H|^2 pairs, for every beta'.
  B5  p = 2: Q(v) := beta'(v,v) is a kappa-quadratic form with polar form omega;
      Arf(Q) := Q(e)Q(f) mod P(kappa), P(x) = x^2 + x, verified SL_2-invariant
      by exhaustive enumeration, and taking exactly 2 values.
  B6  p = 2: Arf(Q) = 0 <=> order profile of the D_4 type <=> Gauss sign
      eps = +1 in sum_v psi(Q(v)) = eps*q <=> |O(Q) cap SL_2| = 2(q-1);
      Arf(Q) != 0 <=> Q_8 type <=> eps = -1 <=> |O(Q) cap SL_2| = 2(q+1).
  B7  p = 2: same Arf => H_beta iso H_beta' by an EXPLICIT isomorphism over an
      isometry g in SL_2 (constructed, then verified on all pairs).
  B8  p = 2: Tr induces kappa/P(kappa) -> F_2 and Arf_{F_2}(psi o Q) = Tr(Arf_kappa(Q)).
  B9  the mu_p-level criterion: beta, beta' give the same mu_p-frame group inside
      A_psi iff psi(Q_s(v)) = 1 for all v, where s = beta' - beta.
  B10 dropping kappa-bilinearity to bare bi-additivity (all the brief demands):
      how many isomorphism classes of H_beta appear then.

Red modes (each MUST exit non-zero):
  --red-arf-blind   compute Arf as Q(e)+Q(f) instead of Q(e)Q(f); B5/B6 must fire
  --red-oddp-split  claim two order profiles at odd p as well; B3 must fire
  --red-iso         perturb the odd-p isomorphism by one value; B4 must fire
"""

import itertools
import sys

from ff import GF, factor_prime_power

QS = (2, 3, 4, 5, 8, 9)
EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2

MODES = ("green", "--red-arf-blind", "--red-oddp-split", "--red-iso")


class Ctx:
    """V = kappa (+) kappa indexed by i = a*q + b."""

    def __init__(self, F):
        self.F, self.q = F, F.q
        q = F.q
        self.nV = q * q
        self.A = [(i // q, i % q) for i in range(self.nV)]
        self.IDX = {}
        for i, (a, b) in enumerate(self.A):
            self.IDX[(a, b)] = i
        add, mul, neg = F.ADD, F.MUL, F.NEG
        self.VADD = [[self.IDX[(add[self.A[i][0]][self.A[j][0]],
                                add[self.A[i][1]][self.A[j][1]])]
                      for j in range(self.nV)] for i in range(self.nV)]
        self.OMEGA = [[F.sub(mul[self.A[i][0]][self.A[j][1]],
                             mul[self.A[j][0]][self.A[i][1]])
                       for j in range(self.nV)] for i in range(self.nV)]
        # psi = psi_zeta = zeta^{Tr(.)}: recorded as the exponent in Z/p
        self.PSIEXP = [F.TR[x] % F.p if F.p != F.q else x % F.p for x in range(q)]
        self.PSIEXP = [self._trexp(x) for x in range(q)]

    def _trexp(self, x):
        """exponent e in Z/p with psi_zeta(x) = zeta^e; Tr lands in the prime
        field, whose elements are 0,1,...,p-1 as integers by construction."""
        F = self.F
        t = F.TR[x]
        acc, e = 0, 0
        for k in range(F.p):
            if acc == t:
                e = k
                break
            acc = F.ADD[acc][F.one]
        return e

    def beta_table(self, alpha, gamma, delta):
        """beta'(v,v') = a b' + alpha a a' + gamma (a b' + a' b) + delta b b'."""
        F, q = self.F, self.q
        mul, add = F.MUL, F.ADD
        out = []
        for i in range(self.nV):
            a, b = self.A[i]
            row = []
            for j in range(self.nV):
                ap, bp = self.A[j]
                val = mul[a][bp]
                val = add[val][mul[alpha][mul[a][ap]]]
                val = add[val][mul[gamma][add[mul[a][bp]][mul[ap][b]]]]
                val = add[val][mul[delta][mul[b][bp]]]
                row.append(val)
            out.append(row)
        return out


def admissible(C, B):
    """beta - beta^T = omega, exhaustively; and kappa-bilinearity."""
    F, nV, q = C.F, C.nV, C.q
    for i in range(nV):
        for j in range(nV):
            if F.sub(B[i][j], B[j][i]) != C.OMEGA[i][j]:
                return False, "beta - beta^T != omega at (%d,%d)" % (i, j)
    for c in range(q):
        for i in range(nV):
            a, b = C.A[i]
            ci = C.IDX[(F.MUL[c][a], F.MUL[c][b])]
            for j in range(nV):
                if B[ci][j] != F.MUL[c][B[i][j]]:
                    return False, "not kappa-linear in the left slot"
                if B[j][ci] != F.MUL[c][B[j][i]]:
                    return False, "not kappa-linear in the right slot"
    return True, ""


def order_profile(C, B):
    """element orders of H_beta = kappa x V, (t,v)(t',v') = (t+t'+beta(v,v'), v+v').
    Brute force: repeated multiplication until the identity."""
    F, q, nV = C.F, C.q, C.nV
    prof = {}
    for t in range(q):
        for v in range(nV):
            ct, cv, k = t, v, 1
            while (ct, cv) != (0, 0):
                ct, cv = F.ADD[F.ADD[ct][t]][B[cv][v]], C.VADD[cv][v]
                k += 1
                if k > q * nV:
                    raise RuntimeError("not a group: element (%d,%d) has no order" % (t, v))
            prof[k] = prof.get(k, 0) + 1
    return tuple(sorted(prof.items()))


def group_axioms(C, B):
    """H_beta really is a group with centre kappa x 0 (sampled associativity is
    not enough: this is exhaustive at q <= 4 and on a spanning probe above)."""
    F, q, nV = C.F, C.q, C.nV
    els = [(t, v) for t in range(q) for v in range(nV)]

    def mul(x, y):
        return (F.ADD[F.ADD[x[0]][y[0]]][B[x[1]][y[1]]], C.VADD[x[1]][y[1]])

    probe = els if q <= 4 else els[::max(1, len(els) // 24)]
    for x in probe:
        for y in els:
            for z in els:
                if mul(mul(x, y), z) != mul(x, mul(y, z)):
                    return False, "associativity fails"
    centre = [x for x in els if all(mul(x, y) == mul(y, x) for y in els)]
    if sorted(centre) != sorted((t, 0) for t in range(q)):
        return False, "centre is not kappa x 0 (got %d elements)" % len(centre)
    return True, ""


def sl2(F):
    """SL_2(kappa) as 4-tuples (r,s,t,u) acting on columns v=(a,b)."""
    q = F.q
    out = []
    for r in range(q):
        for s in range(q):
            for t in range(q):
                for u in range(q):
                    if F.sub(F.MUL[r][u], F.MUL[s][t]) == F.one:
                        out.append((r, s, t, u))
    return out


def act(C, g, i):
    F = C.F
    r, s, t, u = g
    a, b = C.A[i]
    return C.IDX[(F.ADD[F.MUL[r][a]][F.MUL[s][b]], F.ADD[F.MUL[t][a]][F.MUL[u][b]])]


def wp(F, x):
    """Artin-Schreier P(x) = x^2 + x, characteristic 2 only."""
    return F.ADD[F.MUL[x][x]][x]


def arf(C, Q, mode):
    """Arf(Q) = Q(e)Q(f) mod P(kappa) for the symplectic basis e=(1,0), f=(0,1)
    (omega(e,f) = 1).  Returned as the coset representative min(class)."""
    F = C.F
    e, f = C.IDX[(F.one, 0)], C.IDX[(0, F.one)]
    if mode == "--red-arf-blind":
        val = F.ADD[Q[e]][Q[f]]
    else:
        val = F.MUL[Q[e]][Q[f]]
    img = sorted({wp(F, x) for x in range(F.q)})
    coset = sorted({F.ADD[val][y] for y in img})
    return coset[0], img


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
            print("q=%-2d %-4s FAIL %s" % (q, tag, msg))
        return cond

    print("beta_census  mode=%s   exact integer arithmetic, no tolerance" % mode)
    for q in QS:
        p, n = factor_prime_power(q)
        F = GF(p, n)
        ok, msg = F.audit()
        if not check(ok, q, "F", msg):
            continue
        C = Ctx(F)
        print("\n== kappa = F_%d (p=%d, n=%d), |V| = %d, |H| = %d ==" % (q, p, n, C.nV, q ** 3))

        # ---- B1: the torsor of admissible cocycles -----------------------
        betas = {}
        for alpha in range(q):
            for gamma in range(q):
                for delta in range(q):
                    B = C.beta_table(alpha, gamma, delta)
                    good, why = admissible(C, B)
                    if not check(good, q, "B1", "(%d,%d,%d): %s" % (alpha, gamma, delta, why)):
                        break
                    betas[(alpha, gamma, delta)] = B
        check(len(betas) == q ** 3, q, "B1", "|Adm| = %d, expected q^3 = %d" % (len(betas), q ** 3))
        # distinct as tables?
        distinct = len({tuple(map(tuple, B)) for B in betas.values()})
        check(distinct == q ** 3, q, "B1", "only %d distinct admissible tables" % distinct)
        print("q=%-2d B1   PASS |Adm(omega)| = q^3 = %d, all admissible, all kappa-bilinear, all distinct"
              % (q, q ** 3))

        # ---- B2: an antisymmetric admissible cocycle iff p is odd --------
        anti = [k for k, B in betas.items()
                if all(B[i][j] == F.NEG[B[j][i]] for i in range(C.nV) for j in range(C.nV))]
        if p == 2:
            check(anti == [], q, "B2", "antisymmetric admissible cocycle at p=2: %s" % anti)
            print("q=%-2d B2   PASS no admissible cocycle is antisymmetric: the torsor has no "
                  "distinguished point" % q)
        else:
            check(len(anti) == 1, q, "B2", "%d antisymmetric admissible cocycles" % len(anti))
            k = anti[0]
            B = betas[k]
            two = F.ADD[F.one][F.one]
            halfomega = [[[x for x in range(q) if F.MUL[two][x] == C.OMEGA[i][j]][0]
                          for j in range(C.nV)] for i in range(C.nV)]
            check(B == halfomega, q, "B2", "the antisymmetric member is not omega/2")
            print("q=%-2d B2   PASS exactly one antisymmetric admissible cocycle, and it is "
                  "omega/2: a canonical representative" % q)

        # ---- B3: order profiles ------------------------------------------
        ok, why = group_axioms(C, betas[(0, 0, 0)])
        check(ok, q, "B3", "H_beta0 is not a group: %s" % why)
        profs = {}
        for k, B in betas.items():
            pr = order_profile(C, B)
            profs.setdefault(pr, []).append(k)
        nclass = len(profs) + (1 if mode == "--red-oddp-split" and p != 2 else 0)
        if p == 2:
            check(nclass == 2, q, "B3", "%d order profiles at p=2, expected 2" % nclass)
        else:
            check(nclass == 1, q, "B3", "%d order profiles at odd p, expected 1" % nclass)
        for pr, ks in sorted(profs.items(), key=lambda kv: -len(kv[1])):
            print("q=%-2d B3   profile %s : %d of %d cocycles%s"
                  % (q, dict(pr), len(ks), q ** 3, "  (contains D2's beta)" if (0, 0, 0) in ks else ""))

        # ---- B4: odd p, the explicit isomorphism --------------------------
        if p != 2:
            two = F.ADD[F.one][F.one]
            halfof = {F.MUL[two][x]: x for x in range(q)}
            B0 = betas[(0, 0, 0)]
            bad = None
            for (alpha, gamma, delta), B in betas.items():
                fmap = []
                for i in range(C.nV):
                    a, b = C.A[i]
                    sv = F.ADD[F.ADD[F.MUL[alpha][F.MUL[a][a]]]
                                     [F.MUL[gamma][F.ADD[F.MUL[a][b]][F.MUL[a][b]]]]] \
                              [F.MUL[delta][F.MUL[b][b]]]
                    fmap.append(halfof[sv])
                if mode == "--red-iso" and (alpha, gamma, delta) == (F.one, 0, 0):
                    fmap[1] = F.ADD[fmap[1]][F.one]
                for i in range(C.nV):
                    for j in range(C.nV):
                        lhs = F.ADD[fmap[C.VADD[i][j]]][B0[i][j]]
                        rhs = F.ADD[F.ADD[fmap[i]][fmap[j]]][B[i][j]]
                        if lhs != rhs:
                            bad = ((alpha, gamma, delta), i, j)
                            break
                    if bad:
                        break
                if bad:
                    break
            check(bad is None, q, "B4", "phi(t,v) = (t + s(v,v)/2, v) is not an isomorphism: %s" % (bad,))
            if bad is None:
                print("q=%-2d B4   PASS phi(t,v) = (t + s(v,v)/2, v) : H_beta0 -> H_beta' is a group "
                      "isomorphism for all %d cocycles, verified on all %d pairs each"
                      % (q, q ** 3, C.nV ** 2))
            continue

        # ---- p = 2 from here ---------------------------------------------
        # ---- B5: Arf is SL_2-invariant and takes exactly two values -------
        G = sl2(F)
        check(len(G) == q * (q * q - 1), q, "B5", "|SL_2| = %d" % len(G))
        Qof = {k: [B[i][i] for i in range(C.nV)] for k, B in betas.items()}
        arfval = {}
        img = None
        for k, Q in Qof.items():
            arfval[k], img = arf(C, Q, mode)
        check(len(img) == q // 2, q, "B5", "|P(kappa)| = %d, expected q/2" % len(img))
        vals = sorted(set(arfval.values()))
        check(len(vals) == 2, q, "B5", "Arf takes %d values, expected 2" % len(vals))
        # SL_2-invariance of Arf, exhaustively over SL_2 and over all cocycles
        bad = None
        for k, Q in Qof.items():
            for g in G:
                Qg = [Q[act(C, g, i)] for i in range(C.nV)]
                a2, _ = arf(C, Qg, mode)
                if a2 != arfval[k]:
                    bad = (k, g)
                    break
            if bad:
                break
        check(bad is None, q, "B5", "Arf is not SL_2-invariant: %s" % (bad,))
        if bad is None:
            print("q=%-2d B5   PASS Arf(Q) in kappa/P(kappa) (|P(kappa)| = q/2) is SL_2-invariant "
                  "(%d cocycles x %d group elements) and takes exactly the 2 values %s"
                  % (q, q ** 3, len(G), vals))

        # ---- B6: Arf <=> profile <=> Gauss sign <=> |O(Q) cap SL_2| -------
        prof_of = {}
        for pr, ks in profs.items():
            for k in ks:
                prof_of[k] = pr
        gl2 = [(r, s, t, u) for r in range(q) for s in range(q) for t in range(q) for u in range(q)
               if F.sub(F.MUL[r][u], F.MUL[s][t]) != 0]
        rows = {}
        for k, Q in Qof.items():
            # Gauss sum sum_v psi(Q(v)) : psi values are +-1 at p = 2
            gs = sum(1 if C.PSIEXP[Q[i]] == 0 else -1 for i in range(C.nV))
            check(abs(gs) == q, q, "B6", "Gauss sum %d is not +-q for %s" % (gs, k))
            eps = 1 if gs > 0 else -1
            OQ = [g for g in G if all(Q[act(C, g, i)] == Q[i] for i in range(C.nV))]
            OQpsi = [g for g in G if all(C.PSIEXP[Q[act(C, g, i)]] == C.PSIEXP[Q[i]]
                                         for i in range(C.nV))]
            OQfull = [g for g in gl2 if all(Q[act(C, g, i)] == Q[i] for i in range(C.nV))]
            check(len(OQ) == len(OQpsi), q, "B6",
                  "O(Q) cap SL_2 = %d but O(psi.Q) cap SL_2 = %d" % (len(OQ), len(OQpsi)))
            check(len(OQfull) == len(OQ), q, "B6",
                  "O(Q) inside GL_2 has %d elements, not already inside SL_2 (%d)"
                  % (len(OQfull), len(OQ)))
            check(len(OQ) == 2 * (q - eps), q, "B6",
                  "|O(Q) cap SL_2| = %d, expected 2(q-eps) = %d for eps=%d"
                  % (len(OQ), 2 * (q - eps), eps))
            nzero = sum(1 for i in range(C.nV) if Q[i] == 0)
            rows.setdefault((arfval[k], eps, len(OQ), prof_of[k], nzero), []).append(k)
        check(len(rows) == 2, q, "B6", "%d joint (Arf,eps,|O|,profile) classes, expected 2" % len(rows))
        for (av, eps, no, pr, nz), ks in sorted(rows.items()):
            print("q=%-2d B6   Arf=%d  eps=%+d  |O(Q) cap SL_2|=%d = 2(q%+d)  #{Q=0}=%d  profile %s : "
                  "%d cocycles%s" % (q, av, eps, no, -eps, nz, dict(pr), len(ks),
                                     "  <- D2" if (0, 0, 0) in ks else ""))

        # ---- B7: same Arf => explicit isomorphism over an isometry --------
        B0 = betas[(0, 0, 0)]
        Q0 = Qof[(0, 0, 0)]
        same = [k for k in betas if arfval[k] == arfval[(0, 0, 0)]]
        bad = None
        for k in same:
            B, Q = betas[k], Qof[k]
            gg = None
            for g in G:
                if all(Q0[act(C, g, i)] == Q[i] for i in range(C.nV)):
                    gg = g
                    break
            if gg is None:
                bad = (k, "no isometry g in SL_2 with Q0 o g = Q")
                break
            r = [[F.sub(B0[act(C, gg, i)][act(C, gg, j)], B[i][j]) for j in range(C.nV)]
                 for i in range(C.nV)]
            basis = [C.IDX[(F.undigits([1 if t == e else 0 for t in range(n)]), 0)] for e in range(n)] + \
                    [C.IDX[(0, F.undigits([1 if t == e else 0 for t in range(n)]))] for e in range(n)]
            fmap = [0] * C.nV
            for coeffs in itertools.product(range(2), repeat=2 * n):
                v, acc = 0, 0
                supp = [i for i, c in enumerate(coeffs) if c]
                for i in supp:
                    v = C.VADD[v][basis[i]]
                for x in range(len(supp)):
                    for y in range(x + 1, len(supp)):
                        acc = F.ADD[acc][r[basis[supp[x]]][basis[supp[y]]]]
                fmap[v] = acc
            for i in range(C.nV):
                for j in range(C.nV):
                    lhs = F.ADD[fmap[C.VADD[i][j]]][B[i][j]]
                    rhs = F.ADD[F.ADD[fmap[i]][fmap[j]]][B0[act(C, gg, i)][act(C, gg, j)]]
                    if lhs != rhs:
                        bad = (k, "phi is not a homomorphism at (%d,%d)" % (i, j))
                        break
                if bad:
                    break
            if bad:
                break
        check(bad is None, q, "B7", "%s" % (bad,))
        if bad is None:
            print("q=%-2d B7   PASS every cocycle with Arf = Arf(D2) is carried to D2's by an "
                  "explicit isomorphism phi(t,v) = (t+f(v), gv), g in SL_2, verified on all pairs "
                  "(%d cocycles)" % (q, len(same)))

        # ---- B8: Tr : kappa/P(kappa) -> F_2 and Arf_{F_2}(psi o Q) --------
        check(all(C.PSIEXP[wp(F, x)] == 0 for x in range(q)), q, "B8",
              "Tr does not kill P(kappa)")
        check(len({C.PSIEXP[x] for x in range(q)}) == 2, q, "B8", "Tr is not onto F_2")
        bad = None
        for k, Q in Qof.items():
            gs = sum(1 if C.PSIEXP[Q[i]] == 0 else -1 for i in range(C.nV))
            f2arf = 0 if gs > 0 else 1
            if C.PSIEXP[arfval[k]] != f2arf:
                bad = k
                break
        check(bad is None, q, "B8", "Arf_{F_2}(psi o Q) != Tr(Arf_kappa(Q)) at %s" % (bad,))
        if bad is None:
            print("q=%-2d B8   PASS Tr kills P(kappa) and is onto F_2; Arf_{F_2}(psi o Q) "
                  "(the Gauss sign) = Tr(Arf_kappa(Q)) for all %d cocycles" % (q, q ** 3))

        # ---- B9: the mu_p-level criterion ---------------------------------
        bad = None
        for k, B in betas.items():
            s_diag = [F.sub(B[i][i], B0[i][i]) for i in range(C.nV)]
            mu2 = all(C.PSIEXP[x] == 0 for x in s_diag)
            if mu2 != (arfval[k] == arfval[(0, 0, 0)] and
                       all(B[i][i] == B0[i][i] for i in range(C.nV))):
                # mu_2-solvability must be equivalent to Q' = Q exactly, since
                # psi o Q' = psi o Q with both kappa-quadratic forces Q' = Q here
                if mu2 != all(C.PSIEXP[F.sub(B[i][i], B0[i][i])] == 0 for i in range(C.nV)):
                    bad = k
                    break
        check(bad is None, q, "B9", "mu_2 criterion mismatch at %s" % (bad,))
        nmu2 = sum(1 for k, B in betas.items()
                   if all(C.PSIEXP[F.sub(B[i][i], B0[i][i])] == 0 for i in range(C.nV)))
        print("q=%-2d B9   PASS mu_p-frame equivalence with D2 (i.e. psi(Q'-Q) = 1 pointwise) "
              "holds for %d of %d cocycles" % (q, nmu2, q ** 3))

        # ---- B10: bare bi-additive cocycles --------------------------------
        # Q ranges over Q_0 + Hom_{F_p}(V, kappa); classify H_beta by profile.
        basis = [C.IDX[(F.undigits([1 if t == e else 0 for t in range(n)]), 0)] for e in range(n)] + \
                [C.IDX[(0, F.undigits([1 if t == e else 0 for t in range(n)]))] for e in range(n)]
        seen, signs = {}, set()
        for images in itertools.product(range(q), repeat=2 * n):
            Q = [0] * C.nV
            for coeffs in itertools.product(range(2), repeat=2 * n):
                v, acc = 0, 0
                for i, c in enumerate(coeffs):
                    if c:
                        v = C.VADD[v][basis[i]]
                        acc = F.ADD[acc][images[i]]
                Q[v] = F.ADD[Q0[v]][acc]
            nz = sum(1 for i in range(C.nV) if Q[i] == 0)
            gs = sum(1 if C.PSIEXP[Q[i]] == 0 else -1 for i in range(C.nV))
            check(abs(gs) == q, q, "B10", "Gauss sum %d is not +-q for a bi-additive shift" % gs)
            seen[nz] = seen.get(nz, 0) + 1
            signs.add(gs)
        print("q=%-2d B10  bi-additive (not nec. kappa-bilinear) cocycles: #{v : Q(v)=0} takes the "
              "%d values %s over the %d additive shifts of Q, so H_beta has %d isomorphism "
              "classes here against exactly 2 among the kappa-bilinear cocycles; but "
              "sum_v psi(Q(v)) still takes only the two values %s, so psi o Q keeps exactly two "
              "F_2-Arf classes"
              % (q, len(seen), sorted(seen), q ** (2 * n), len(seen), sorted(signs)))

    print("\n---- summary (mode=%s) ----" % mode)
    if mode == "green":
        if fired:
            for q, tag, msg in fired:
                print("FAIL q=%-2d %s: %s" % (q, tag, msg))
            print("GREEN RUN FAILED: %d failures" % len(fired))
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
    print("RED MODE %s CAUGHT: first = %s at q=%d, %d failures" % (mode, fired[0][1], fired[0][0], len(fired)))
    return EXIT_FIRED


if __name__ == "__main__":
    sys.exit(main(sys.argv))
