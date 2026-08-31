<!-- ROLE: gate reachability evidence for wh_kappa_check.py. Lane wh-check.
     Produced by running every mode and reading the failures back out of the
     saved run logs; nothing here is asserted from reading the source. -->

# RED-MATRIX — which gate actually killed which mutation

## How this was produced

    python3 -O wh_kappa_check.py                    > run-green.txt        # exit 0
    python3 -O wh_kappa_check.py --red-symmetric    > run-red-symmetric.txt    # exit 1
    python3 -O wh_kappa_check.py --red-trivial-char > run-red-trivial-char.txt # exit 1
    python3 -O wh_kappa_check.py --red-cocycle      > run-red-cocycle.txt      # exit 1
    python3 -O wh_kappa_check.py --red-nonisotropic > run-red-nonisotropic.txt # exit 1
    python3 -O wh_kappa_check.py --red-dim          > run-red-dim.txt          # exit 1
    python3 -O wh_kappa_check.py --red-halfweyl     > run-red-halfweyl.txt     # exit 1

Green run: 0.5 s for all six `q`. Every red mode exits non-zero. Exit code 2 is
reserved for "red mode NOT caught" (a checker defect) and for bad usage; no mode
produced it.

## The matrix

Entries are the `q` at which that gate fired. `-` = the gate ran and passed.

| gate \ mode | symmetric | trivial-char | cocycle | nonisotropic | dim | halfweyl (extra) |
|---|---|---|---|---|---|---|
| C1 beta-beta^T=omega | 2,3,4,5,8,9 | - | **3,5,9 only** | - | - | 2,4,8 (unevaluable) |
| C2 alternating/nondeg/bilinear | 2,3,4,5,8,9 | - | - | - | - | - |
| C3 Weyl relation | 2,3,4,5,8,9 | - | 2,3,4,5,8,9 | 4,8,9 | - | 2,3,4,5,8,9 |
| C4 commutation | 2,3,4,5,8,9 | - | - | 4,8,9 | - | - |
| C5 span dimension | 2,3,4,5,8,9 | 2,3,4,5,8,9 | - | - | 2,3,4,5,8,9 | - |
| C6 commutant | 2,3,4,5,8,9 | 2,3,4,5,8,9 | - | - | - | - |
| C7 isotropic lines | 2,3,4,5,8,9 | - | - | 4,8,9 | - | - |
| C8 characters | - | 2,3,4,5,8,9 | - | - | - | - |
| C9 no omega/2 at p=2 | - | - | - | - | - | **2,4,8** |
| first gate to report | C1 | C5 | C3 (q=2) | C3 (q=4) | C5 | C1 (q=2) |
| exit code | 1 | 1 | 1 | 1 | 1 | 1 |

The gate named by the brief for each mode did fire in every case: C2 for
`--red-symmetric`, C6 for `--red-trivial-char`, C1 for `--red-cocycle` (at odd
characteristic — see below), C3 **and** C7 for `--red-nonisotropic`, C5 for
`--red-dim`.

## Every gate is reachable — but C9 only because of an added mode

All nine gates fire under at least one mutation. **C9 is reached by no mode in
the brief.** The brief's five mutations leave it untouched, so as specified it
would have been decoration: a gate that reads as evidence while being unable to
fail. `--red-halfweyl` was added for exactly this reason and is flagged as an
addition wherever it appears. It replaces `beta` by the symmetrised `omega/2`;
at `p = 2` forming that value trips the C9 guard.

## Sub-checks that no mutation reaches (decoration, named as such)

Gates stop at their first failing sub-check, so gate-level reachability is
coarser than sub-check reachability. These sub-checks run and pass in green but
**no red mode can make them fail**:

| sub-check | what it asserts | what would reach it |
|---|---|---|
| C2b nondegeneracy | `form(v,.) != 0` for `v != 0` | a mutation to a degenerate form, e.g. `omega'((a,b),(a',b')) = a b' - a' b` composed with a non-injective rescaling |
| C2c bilinearity | additive and `kappa`-homogeneous in each slot | a mutation making the form only `F_p`-bilinear, e.g. `a b'^p - a' b^p` |
| C7d subgroup census | the pre-registered `(total, kappa-iso, psi-iso)` counts | a mutation of the subspace enumerator itself |
| C8 zeta-pair / all-characters / algebra-isomorphism | the three sub-checks after the torsor count | a mutation giving two distinct `zeta` the same central character, or breaking `W(a,b) -> W'(a/c,b)` |
| C9 odd-characteristic branch | `2` invertible and `2*half(y) = y` | a mutation of the halving routine |

None of these is load-bearing for the brief's five mutations; they are recorded
here so that nobody reads a green `PASS` on them as tested behaviour. The
census (C7d) is worth singling out: it is *binding* in green — the numbers are
pre-registered in `EXPECTATIONS.md` and asserted in the source — but it is not
*red-tested*.

## No two modes are bit-identical

Checked mechanically by comparing the sets of `(q, gate)` failures parsed out of
the six logs: all 15 pairs differ, minimum symmetric difference 9. Firing sets:

    symmetric     {C1,C2,C3,C4,C5,C6,C7} x {2,3,4,5,8,9}   42 failures
    trivial-char  {C5,C6,C8}             x {2,3,4,5,8,9}   18
    cocycle       {C3} x all q, {C1} x {3,5,9}              9
    nonisotropic  {C3,C4,C7}             x {4,8,9}          9
    dim           {C5}                   x {2,3,4,5,8,9}    6
    halfweyl      {C3} x all q, {C1,C9} x {2,4,8}          12

## Findings the red runs produced

1. **C1 is blind to `--red-cocycle` at characteristic 2, and this is not a bug.**
   `beta^T - beta = -omega`, and `-omega = omega` when `p = 2`, so the
   transposed convention satisfies the C1 identity exactly at `q = 2, 4, 8`.
   The mode is caught there by C3 alone. Pre-registered as D-g; confirmed by the
   run. A checker carrying only C1 would certify the wrong cocycle convention in
   precisely the characteristic the brief says the campaign exists to protect.
2. **`--red-nonisotropic` is not constructible for `q` prime, by a theorem.**
   `omega` is alternating, so every line — and for `q` prime every order-`q`
   subgroup — is isotropic. "A non-isotropic line" does not exist for any `q`.
   The mode therefore mutates the polarization to a non-isotropic order-`q`
   *subgroup*, which exists only for `n >= 2`, and reports NOT CONSTRUCTIBLE at
   `q = 2, 3, 5` instead of silently testing nothing. The checker verifies the
   non-existence rather than asserting it: the C7 census enumerates all order-`q`
   subgroups (3, 4, 6 for `q = 2, 3, 5`) and finds every one isotropic.
3. **`--red-dim` mutates a claim, not an object.** The computed rank stays `q^2`;
   only the number it is compared against changes. It fires everywhere, but all
   it establishes is that C5 compares against a real computation rather than
   restating a constant. It is the weakest of the six.
4. **`--red-symmetric` is blunt**: it fires seven of nine gates. `sigma = a a' + b b'`
   had to be used rather than the obvious symmetrisation `a b' + a' b`, which
   *equals* `omega` at `p = 2` and would have been a silent no-op at `q = 2,4,8`
   — a mutation that mutates nothing is the failure mode the brief warns about.
5. **`--red-nonisotropic` is the sharpest mode**: exactly C3, C4, C7 fire while
   C5 (rank `q^2`) and C6 (commutant 1) still pass. Keeping the complement `Q`
   Lagrangian preserves irreducibility, so the mutation isolates the cocycle and
   the polarization instead of destroying the model wholesale.

## Deviation from the pre-registration

One, and it is cosmetic. `EXPECTATIONS.md` predicted the first gate to report
for `--red-halfweyl` at `p = 2` would be C9; the run reports C1 first, because
gates run in numeric order and C1 needs `beta`, which cannot be formed. The
cause is the same C9 guard (the failure text says so) and C9 does fire. Recorded
rather than edited away. Every other prediction — every PASS, every FAIL, and
every number: ranks, commutant dimensions, line counts `1, 0, 1, 2, 1, 2` under
`--red-symmetric`, the census triples, and the non-constructibility set
`{2, 3, 5}` — matched the pre-registration exactly.
