#!/usr/bin/env python3
"""COMP-F: functoriality in kappa -- the Frobenius obstruction and the sections
that do exist.  (OBJ-2, OBJ-7)

Lane wh-repair.  Exact: characters are recorded by their Z/p exponent tables.

F1  Tr_{kappa'/F_p} restricted to kappa equals n * Tr_{kappa/F_p} for
    [kappa':kappa] = n -- so the trace-normalised family restricts to
    psi_{zeta^n}, TRIVIAL exactly when p | n.  (WH-FUNCT-a, scoped to the
    trace-normalised family per OBJ-7.)
F2  Frobenius x -> x^p is an embedding kappa -> kappa, so any SECTION over the
    category of finite fields with all embeddings must pick a Frobenius-invariant
    character.  Those are exactly psi_c with c in F_p.
F3  For kappa = F_{p^p} every Frobenius-invariant character restricts TRIVIALLY
    to the prime field, so NO section exists over that category.  First instance
    F_2 subset F_4.
F4  Over the inclusion poset of subfields of a fixed algebraic closure a section
    is exactly a character Psi of the union with Psi|_{F_p} nontrivial: verified
    inside F_16 (p=2) and F_81 (p=3) by listing which characters restrict
    nontrivially to EVERY subfield and comparing with {c : Tr(c) != 0}.
F5  the functor itself: for an embedding iota with psi' o iota = psi, the map
    W(v) -> W'(V(iota) v) is unital, injective, and multiplicative -- all
    structure constants compared, for every character-compatible pair
    (F_2, psi) -> (F_4, psi_c) and (F_2,psi) -> (F_8, psi_c), and composition
    F_2 -> F_4 -> F_16 checked.

Red modes (each MUST exit non-zero):
  --red-section-exists   claim a Frobenius-compatible section exists; F3 fires
  --red-restrict         claim Tr_{kappa'} restricts to Tr_{kappa}; F1 fires
"""

import itertools
import sys

from ff import GF, factor_prime_power

EXIT_OK, EXIT_FIRED, EXIT_NOT_CAUGHT = 0, 1, 2
MODES = ("green", "--red-section-exists", "--red-restrict")


def prime_field(F):
    out, acc = [], 0
    for _ in range(F.p):
        out.append(acc)
        acc = F.ADD[acc][F.one]
    return out


def embed(Fsub, Fbig):
    """The (unique up to Galois) embedding F_{p^a} -> F_{p^b}, a | b: send a
    generator of the subfield.  Returned as a list indexed by Fsub elements.
    Built by finding a root of the subfield's modulus in the big field."""
    p, a, b = Fsub.p, Fsub.n, Fbig.n
    if b % a:
        raise ValueError("not a subfield")
    # subfield of F_{p^b} = { x : x^{p^a} = x }
    sub = [x for x in range(Fbig.q) if Fbig.pow(x, p ** a) == x]
    if len(sub) != Fsub.q:
        raise RuntimeError("subfield has %d elements, expected %d" % (len(sub), Fsub.q))
    # match by finding a root of Fsub's minimal polynomial for its generator g=x
    if a == 1:
        iota = {}
        acc_s, acc_b = 0, 0
        for _ in range(p):
            iota[acc_s] = acc_b
            acc_s = Fsub.ADD[acc_s][Fsub.one]
            acc_b = Fbig.ADD[acc_b][Fbig.one]
        return iota
    gen = Fsub.undigits([0, 1] + [0] * (a - 2))          # x
    for r in sub:
        # extend F_p-linearly by powers of the generator and test multiplicativity
        pw_s = [Fsub.one]
        pw_b = [Fbig.one]
        for _ in range(a - 1):
            pw_s.append(Fsub.MUL[pw_s[-1]][gen])
            pw_b.append(Fbig.MUL[pw_b[-1]][r])
        iota = {}
        for coeffs in itertools.product(range(p), repeat=a):
            xs, xb = 0, 0
            for c, (s, bb) in zip(coeffs, zip(pw_s, pw_b)):
                for _ in range(c):
                    xs = Fsub.ADD[xs][s]
                    xb = Fbig.ADD[xb][bb]
            iota[xs] = xb
        if len(iota) != Fsub.q:
            continue
        if all(iota[Fsub.MUL[x][y]] == Fbig.MUL[iota[x]][iota[y]]
               for x in range(Fsub.q) for y in range(Fsub.q)) and \
           all(iota[Fsub.ADD[x][y]] == Fbig.ADD[iota[x]][iota[y]]
               for x in range(Fsub.q) for y in range(Fsub.q)):
            return iota
    raise RuntimeError("no field embedding found")


def trexp(F, x):
    """the exponent e in Z/p with psi_zeta(x) = zeta^e, psi_zeta = zeta^Tr."""
    t, acc = F.TR[x], 0
    for k in range(F.p):
        if acc == t:
            return k
        acc = F.ADD[acc][F.one]
    raise RuntimeError("trace not in the prime field")


def main(argv):
    mode = "green"
    for a in argv[1:]:
        if a in MODES:
            mode = a
        else:
            print("unknown mode %r; modes: %s" % (a, " ".join(MODES)))
            return EXIT_NOT_CAUGHT
    fired = []

    def check(cond, tag, msg):
        if not cond:
            fired.append((tag, msg))
            print("%-3s FAIL %s" % (tag, msg))
        return cond

    print("funct_sections  mode=%s   exact character exponents in Z/p" % mode)

    # ---- F1 -------------------------------------------------------------
    print("\n-- F1: Tr_{kappa'/F_p}|_kappa = n Tr_{kappa/F_p} --")
    for (p, a, b) in ((2, 1, 2), (2, 1, 3), (2, 2, 4), (3, 1, 2), (3, 1, 3), (2, 1, 4), (3, 2, 4)):
        Fs, Fb = GF(p, a), GF(p, b)
        iota = embed(Fs, Fb)
        n = b // a
        bad = [x for x in range(Fs.q)
               if trexp(Fb, iota[x]) % p != (n * trexp(Fs, x)) % p]
        if mode == "--red-restrict":
            bad = [x for x in range(Fs.q) if trexp(Fb, iota[x]) % p != trexp(Fs, x) % p]
            check(not bad, "F1", "restriction is not n*Tr for F_%d^%d < F_%d^%d" % (p, a, p, b))
            continue
        check(not bad, "F1", "Tr_{F_%d^%d}|_{F_%d^%d} != %d Tr  (%d witnesses)"
              % (p, b, p, a, n, len(bad)))
        triv = all(trexp(Fb, iota[x]) % p == 0 for x in range(Fs.q))
        print("   F_%d^%d < F_%d^%d, n=%d : restriction of psi_zeta is psi_{zeta^%d}, %s "
              "(p|n is %s)" % (p, a, p, b, n, n % p,
                               "TRIVIAL" if triv else "nontrivial", p % max(n, 1) == 0 or n % p == 0))

    # ---- F2, F3 ----------------------------------------------------------
    print("\n-- F2/F3: Frobenius-invariant characters, and the section obstruction --")
    for (p, b) in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3)):
        F = GF(p, b)
        pf = prime_field(F)
        # psi_c(x) = zeta^{Tr(cx)}; Frobenius invariance: psi_c(x^p) = psi_c(x) for all x
        inv = [c for c in range(F.q)
               if all(trexp(F, F.MUL[c][F.pow(x, p)]) == trexp(F, F.MUL[c][x])
                      for x in range(F.q))]
        check(sorted(inv) == sorted(pf), "F2",
              "Frobenius-invariant characters of F_%d^%d are %s, expected the prime field %s"
              % (p, b, sorted(inv), sorted(pf)))
        nontriv_on_pf = [c for c in inv if c != 0 and
                         any(trexp(F, F.MUL[c][y]) != 0 for y in pf)]
        if mode == "--red-section-exists" and b == p:
            nontriv_on_pf = [1]
        if b == p:
            check(not nontriv_on_pf, "F3",
                  "F_%d^%d: a Frobenius-invariant character is nontrivial on F_%d (%s) -- "
                  "a section would exist" % (p, b, p, nontriv_on_pf))
            print("   F_%d^%d (b = p): %d Frobenius-invariant characters, %d of them nontrivial "
                  "on F_%d  => NO SECTION over {finite fields, all embeddings}"
                  % (p, b, len(inv), len(nontriv_on_pf), p))
        else:
            print("   F_%d^%d: %d Frobenius-invariant characters, %d nontrivial on F_%d"
                  % (p, b, len(inv), len(nontriv_on_pf), p))

    # ---- F4 --------------------------------------------------------------
    print("\n-- F4: sections over the inclusion poset of subfields --")
    for (p, b) in ((2, 4), (3, 4), (2, 6)):
        F = GF(p, b)
        divs = [d for d in range(1, b + 1) if b % d == 0]
        subs = {}
        for d in divs:
            subs[d] = [x for x in range(F.q) if F.pow(x, p ** d) == x]
            check(len(subs[d]) == p ** d, "F4", "subfield of size %d not found" % (p ** d))
        good = []
        for c in range(1, F.q):
            if all(any(trexp(F, F.MUL[c][x]) != 0 for x in subs[d]) for d in divs):
                good.append(c)
        onprime = [c for c in range(1, F.q) if any(trexp(F, F.MUL[c][x]) != 0 for x in subs[1])]
        check(sorted(good) == sorted(onprime), "F4",
              "F_%d^%d: characters nontrivial on every subfield (%d) != those nontrivial on "
              "the prime field (%d)" % (p, b, len(good), len(onprime)))
        print("   F_%d^%d: %d of %d nontrivial characters restrict nontrivially to EVERY "
              "subfield, and they are exactly the %d nontrivial on F_%d"
              % (p, b, len(good), F.q - 1, len(onprime), p))

    # ---- F5 --------------------------------------------------------------
    print("\n-- F5: the functor on character-compatible embeddings --")
    for (p, a, b) in ((2, 1, 2), (2, 1, 3), (2, 2, 4)):
        Fs, Fb = GF(p, a), GF(p, b)
        iota = embed(Fs, Fb)
        pairs = 0
        for c in range(1, Fb.q):
            # psi'_c o iota = psi_1 ?  (psi_1 = the trace character of the subfield)
            if all(trexp(Fb, Fb.MUL[c][iota[x]]) == trexp(Fs, x) for x in range(Fs.q)):
                pairs += 1
                bad = None
                for i in range(Fs.q * Fs.q):
                    a1, b1 = divmod(i, Fs.q)
                    for j in range(Fs.q * Fs.q):
                        a2, b2 = divmod(j, Fs.q)
                        lhs = trexp(Fs, Fs.MUL[a1][b2])                       # psi(beta(v,v'))
                        rhs = trexp(Fb, Fb.MUL[c][Fb.MUL[iota[a1]][iota[b2]]])  # psi'(beta'(iv,iv'))
                        if lhs != rhs:
                            bad = (c, i, j)
                            break
                        if Fb.ADD[iota[a1]][iota[a2]] != iota[Fs.ADD[a1][a2]] or \
                           Fb.ADD[iota[b1]][iota[b2]] != iota[Fs.ADD[b1][b2]]:
                            bad = (c, "V(iota) not additive")
                            break
                    if bad:
                        break
                check(bad is None, "F5", "structure constants differ: %s" % (bad,))
        check(pairs > 0, "F5", "no character-compatible embedding F_%d^%d -> F_%d^%d"
              % (p, a, p, b))
        print("   F_%d^%d -> F_%d^%d : %d character-compatible pairs, all %d^2 structure "
              "constants agree (unital, multiplicative, basis -> distinct basis => injective)"
              % (p, a, p, b, pairs, Fs.q ** 2))
    # composition F_2 -> F_4 -> F_16
    F2, F4, F16 = GF(2, 1), GF(2, 2), GF(2, 4)
    i24, i416, i216 = embed(F2, F4), embed(F4, F16), embed(F2, F16)
    check(all(i416[i24[x]] == i216[x] for x in range(F2.q)), "F5",
          "the embeddings do not compose: F_2 -> F_4 -> F_16 != F_2 -> F_16")
    print("   composition F_2 -> F_4 -> F_16 agrees with F_2 -> F_16 on the nose; identities "
          "are identities")

    print("\n---- summary (mode=%s) ----" % mode)
    if mode == "green":
        if fired:
            for tag, msg in fired:
                print("FAIL %s: %s" % (tag, msg))
            return EXIT_FIRED
        print("GREEN: every check passed")
        return EXIT_OK
    if not fired:
        print("RED MODE NOT CAUGHT: no check fired. Checker defect, not a pass.")
        return EXIT_NOT_CAUGHT
    for tag, msg in fired:
        print("KILLED BY %s: %s" % (tag, msg))
    print("RED MODE %s CAUGHT: %d failures" % (mode, len(fired)))
    return EXIT_FIRED


if __name__ == "__main__":
    sys.exit(main(sys.argv))
