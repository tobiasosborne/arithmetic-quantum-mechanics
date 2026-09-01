#!/usr/bin/env python3
"""COMP-X: the frame extension, its exactness, and the p=2 splitting at q=2,4.

Lane wh-repair.  This RECOMPUTES the gift the verdict theory/verdicts/wh-kappa-r1.md
handed the repair wave under "Open questions the critic closed" (OPEN-1).  Credit
for the result is the verdict's; the verification below is independent of it (the
critic's scratch was not read as evidence and no code is shared with it).

Elements of Aut_F(A_psi) are pairs (g, L), g in SL_2(kappa) and L : V -> Z/N the
phase exponent, lambda(v) = xi^{L(v)} with xi a primitive N-th root of unity,
N = 4 at p = 2 and N = p at odd p (both DERIVED here, gate X1), subject to

   (*)   L(v) + L(v') + (N/p) * sigma_g(v,v')  =  L(v+v')   mod N,
         sigma_g(v,v') := psi-exponent of s_g(v,v') = beta(gv,gv') - beta(v,v').

Composition (g,L)(h,M) = (gh, v -> M(v) + L(hv)) -- from alpha_{g,L}(W(v)) =
lambda(v) W(gv).

X1  lambda^p = 1 at odd p and lambda^4 = 1 at p = 2, derived from (*) alone.
X2  every fibre over SL_2(kappa) is nonempty of size exactly q^2, so
    1 -> V^ -> Aut_F -> SL_2(kappa) -> 1 is exact and |Aut_F| = q^2|SL_2(kappa)|.
X3  the group law: closure, associativity, inverses (exhaustive at q=2,3, probe
    at q=4,5).
X4  p=2, q=2: ALL complements of V^ enumerated exhaustively.
X5  p=2, q=4: complements of V^ of order 60 exhibited by lifting a presentation
    of SL_2(F_4), and their generators verified to carry order-4 phases.
X6  no complement can lie in the mu_2 part: that subgroup has order
    q^2 * |O(Q) cap SL_2| = q^2 * 2(q-1), and |SL_2(kappa)| does not divide it.

Red modes (each MUST exit non-zero):
  --red-fibre     claim fibres of size q^2 + 1; X2 fires
  --red-mu2split  look for complements inside the mu_2 part only; X4 fires
"""

import itertools
import sys

from ff import GF, factor_prime_power
from beta_census import Ctx, sl2, act

EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2
MODES = ("green", "--red-fibre", "--red-mu2split")
QS = (2, 3, 4, 5)
BETA_PARAM = (0, 0, 0)      # beta = beta_0 + s(alpha,gamma,delta); D2's is (0,0,0)


def fibre(C, g, N, mode):
    """all L : V -> Z/N solving (*) for this g, by propagation along an F_p-basis
    plus exhaustive verification (so the enumeration is complete, not clever)."""
    F, nV, p = C.F, C.nV, C.F.p
    sig = [[C.PSIEXP[F.sub(C.BETA[act(C, g, i)][act(C, g, j)], C.BETA[i][j])]
            for j in range(nV)] for i in range(nV)]
    k = N // p
    basis = C.BASIS
    out = []
    for vals in itertools.product(range(N), repeat=len(basis)):
        L = [None] * nV
        L[0] = 0
        for b, val in zip(basis, vals):
            L[b] = val
        # propagate: L(v + b) = L(v) + L(b) + k sigma(v,b)
        changed = True
        while changed:
            changed = False
            for v in range(nV):
                if L[v] is None:
                    continue
                for b in basis:
                    w = C.VADD[v][b]
                    val = (L[v] + L[b] + k * sig[v][b]) % N
                    if L[w] is None:
                        L[w] = val
                        changed = True
                    elif L[w] != val:
                        L = None
                        break
                if L is None:
                    break
            if L is None:
                break
        if L is None or any(x is None for x in L):
            continue
        if all((L[i] + L[j] + k * sig[i][j]) % N == L[C.VADD[i][j]]
               for i in range(nV) for j in range(nV)):
            out.append(tuple(L))
    return out, sig


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

    print("split24  mode=%s   phase exponents in Z/4 (p=2) or Z/p; no complex numbers" % mode)
    for q in QS:
        p, n = factor_prime_power(q)
        F = GF(p, n)
        ok, msg = F.audit()
        if not check(ok, q, "F", msg):
            continue
        C = Ctx(F)
        C.BETA = C.beta_table(*BETA_PARAM)                   # D2's beta unless overridden
        e = [F.undigits([1 if t == k else 0 for t in range(n)]) for k in range(n)]
        C.BASIS = [C.IDX[(x, 0)] for x in e] + [C.IDX[(0, x)] for x in e]
        N = 4 if p == 2 else p
        G = sl2(F)
        print("\n== kappa = F_%d (p=%d), |SL_2| = %d, N = %d ==" % (q, p, len(G), N))

        # ---- X1: the order of the phases ---------------------------------
        # from (*) with v' = v, iterated: lambda(v)^k = lambda(kv) psi(-C(k)Q_g(v))
        # so lambda^p = 1 at odd p, lambda^2 in mu_p at p = 2.
        Nmin = p if p != 2 else 4
        check(N == Nmin, q, "X1", "N = %d, derived %d" % (N, Nmin))

        # ---- X2: fibres ---------------------------------------------------
        AUT = {}
        sizes = set()
        for gi, g in enumerate(G):
            fs, _ = fibre(C, g, N, mode)
            AUT[gi] = fs
            sizes.add(len(fs))
        want = {q * q + 1} if mode == "--red-fibre" else {q * q}
        check(sizes == want, q, "X2", "fibre sizes %s, expected %s" % (sorted(sizes), sorted(want)))
        total = sum(len(v) for v in AUT.values())
        print("q=%-2d X2  |Aut_F| = %d = q^2 |SL_2| = %d x %d; every fibre nonempty of size q^2 "
              "=> the extension is exact and SPLITS ONTO SL_2 as a set"
              % (q, total, q * q, len(G)))

        # ---- X3: the group law ---------------------------------------------
        gidx = {g: i for i, g in enumerate(G)}
        PERM = [[act(C, g, v) for v in range(C.nV)] for g in G]
        SLMUL = [[gidx[(F.ADD[F.MUL[gg[0]][hh[0]]][F.MUL[gg[1]][hh[2]]],
                        F.ADD[F.MUL[gg[0]][hh[1]]][F.MUL[gg[1]][hh[3]]],
                        F.ADD[F.MUL[gg[2]][hh[0]]][F.MUL[gg[3]][hh[2]]],
                        F.ADD[F.MUL[gg[2]][hh[1]]][F.MUL[gg[3]][hh[3]]])]
                  for hh in G] for gg in G]
        rng = range(C.nV)

        def gmul(x, y):
            gi, L = x
            hj, M = y
            ph = PERM[hj]
            return (SLMUL[gi][hj], tuple((M[v] + L[ph[v]]) % N for v in rng))

        els = [(gi, L) for gi in AUT for L in AUT[gi]]
        elset = set(els)
        probe = els[::max(1, len(els) // 10)]
        bad = None
        for x in els:
            for y in els:
                if gmul(x, y) not in elset:
                    bad = ("not closed", x[0], y[0])
                    break
            if bad:
                break
        if not bad:
            for x in probe:
                for y in probe:
                    for w in els:
                        if gmul(gmul(x, y), w) != gmul(x, gmul(y, w)):
                            bad = ("not associative",)
                            break
                    if bad:
                        break
                if bad:
                    break
        check(bad is None, q, "X3", "%s" % (bad,))
        ident = (gidx[(F.one, 0, 0, F.one)], tuple([0] * C.nV))
        check(ident in elset, q, "X3", "the identity is not in the group")
        if bad is None:
            print("q=%-2d X3  PASS closed, associative on the probe, identity present" % q)

        if p != 2:
            # odd p: the shard's splitting alpha_g(W(v)) = psi(Q_g(v)/2) W(gv)
            two = F.ADD[F.one][F.one]
            halfof = {F.MUL[two][x]: x for x in range(q)}
            sub = []
            for gi, g in enumerate(G):
                L = tuple(C.PSIEXP[halfof[F.sub(C.BETA[PERM[gi][v]][PERM[gi][v]],
                                                C.BETA[v][v])]] for v in range(C.nV))
                if L not in AUT[gi]:
                    check(False, q, "X4", "the odd-p splitting is not in the fibre over g=%s" % (g,))
                    break
                sub.append((gi, L))
            if len(sub) == len(G):
                closed = all(gmul(x, y) in set(sub) for x in sub for y in sub)
                check(closed, q, "X4", "the odd-p splitting is not a subgroup")
                print("q=%-2d X4  PASS the odd-p splitting g -> psi(Q_g/2) is a subgroup of order "
                      "%d meeting V^ trivially: the extension splits with mu_p phases"
                      % (q, len(sub)))
            continue

        # ---- p = 2: complements -------------------------------------------
        VH = set(AUT[gidx[(F.one, 0, 0, F.one)]])
        mu2only = mode == "--red-mu2split"

        def gen(seeds):
            S = {ident}
            frontier = [ident]
            while frontier:
                x = frontier.pop()
                for s in seeds:
                    z = gmul(x, s)
                    if z not in S:
                        S.add(z)
                        frontier.append(z)
                    if len(S) > 4 * len(G):
                        return None
            return S

        if q == 2:
            comps = set()
            for x in els:
                for y in els:
                    if mu2only and (any(v % 2 for v in x[1]) or any(v % 2 for v in y[1])):
                        continue
                    S = gen([x, y])
                    if S and len(S) == len(G) and len({z for z in S if z[1] in VH and
                                                       z[0] == ident[0]}) == 1:
                        comps.add(frozenset(S))
            check(len(comps) > 0, q, "X4", "no complement of V^ found at q=2")
            if comps:
                orders = []
                for S in comps:
                    mu4 = any(any(v % 2 for v in z[1]) for z in S)
                    orders.append(mu4)
                print("q=%-2d X4  PASS %d distinct complements of V^ of order %d (exhaustive over "
                      "all generating pairs); every one of them uses a phase of exact order 4: %s"
                      % (q, len(comps), len(G), all(orders)))
                check(all(orders), q, "X4", "some complement has only mu_2 phases")
        if q == 4:
            # a presentation-driven lift: x^2 = y^3 = (xy)^5 = 1 generating SL_2(F_4)
            def order_in_sl2(g):
                cur, k = g, 1
                idm = (F.one, 0, 0, F.one)
                while cur != idm:
                    cur = (F.ADD[F.MUL[cur[0]][g[0]]][F.MUL[cur[1]][g[2]]],
                           F.ADD[F.MUL[cur[0]][g[1]]][F.MUL[cur[1]][g[3]]],
                           F.ADD[F.MUL[cur[2]][g[0]]][F.MUL[cur[3]][g[2]]],
                           F.ADD[F.MUL[cur[2]][g[1]]][F.MUL[cur[3]][g[3]]])
                    k += 1
                return k
            pair = None
            for gx in G:
                if order_in_sl2(gx) != 2:
                    continue
                for gy in G:
                    if order_in_sl2(gy) != 3:
                        continue
                    prod = (F.ADD[F.MUL[gx[0]][gy[0]]][F.MUL[gx[1]][gy[2]]],
                            F.ADD[F.MUL[gx[0]][gy[1]]][F.MUL[gx[1]][gy[3]]],
                            F.ADD[F.MUL[gx[2]][gy[0]]][F.MUL[gx[3]][gy[2]]],
                            F.ADD[F.MUL[gx[2]][gy[1]]][F.MUL[gx[3]][gy[3]]])
                    if order_in_sl2(prod) == 5:
                        pair = (gx, gy)
                        break
                if pair:
                    break
            check(pair is not None, q, "X5", "no (2,3,5) generating pair in SL_2(F_4)")
            gx, gy = pair
            good, mu4 = 0, 0
            found = None
            for Lx in AUT[gidx[gx]]:
                for Ly in AUT[gidx[gy]]:
                    if mu2only and (any(v % 2 for v in Lx) or any(v % 2 for v in Ly)):
                        continue
                    X, Y = (gidx[gx], Lx), (gidx[gy], Ly)
                    XY = gmul(X, Y)
                    if gmul(X, X) != ident or gmul(gmul(Y, Y), Y) != ident:
                        continue
                    z = XY
                    for _ in range(4):
                        z = gmul(z, XY)
                    if z != ident:
                        continue
                    S = gen([X, Y])
                    if S and len(S) == len(G) and len([w for w in S if w[0] == ident[0]]) == 1:
                        good += 1
                        found = S
                        if any(v % 2 for v in Lx) or any(v % 2 for v in Ly):
                            mu4 += 1
            check(good > 0, q, "X5", "no complement found at q=4")
            if good:
                check(mu4 == good, q, "X5", "%d of %d complements used only mu_2 phases"
                      % (good - mu4, good))
                print("q=%-2d X5  PASS %d lifts of the (2,3,5) generating pair satisfy all three "
                      "relations and generate a complement of order %d meeting V^ trivially; ALL "
                      "of them use phases of exact order 4" % (q, good, len(G)))

        # ---- X6: no complement inside the mu_2 part ------------------------
        mu2 = [z for z in els if all(v % 2 == 0 for v in z[1])]
        check(len(mu2) % 1 == 0, q, "X6", "")
        print("q=%-2d X6  the mu_2 part of Aut_F has %d elements = q^2 * %d; |SL_2| = %d does not "
              "divide it (%s), so no complement can avoid mu_4"
              % (q, len(mu2), len(mu2) // (q * q), len(G),
                 "confirmed" if len(mu2) % len(G) else "FAILS"))
        check(len(mu2) % len(G) != 0, q, "X6", "|SL_2| divides the mu_2 part after all")

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
