# Blind critic verdict: vector/polarization and type-C bridge

Date: 2026-09-07.  Prover: `gpt-5.6-sol`, `xhigh` (as recorded in the
review work order).  Critic: `gpt-5.6-sol`, `xhigh`.  This is a same-family
prover/critic review conducted in a blind lane.  I read the frozen artifact,
the current single sources and the registered local primary-source bodies; I
did not read the prover summary or scratch history.

## Objections

### O1 — MAJOR: arithmetic regularity does not make endpoint evaluation positive

**(a) Exact location.** `DEFINITIONS-PROPOSED.md`, D1249, especially lines
100--105, and D1258, especially lines 188--192; `reference-trace.md`
`<1>39`.  D1258 calls the operation an “evaluation functor”, but neither its
source category nor its morphisms/equality/composition are defined.  More
seriously, D1249's stated regularity test does not imply that an arithmetic
density evaluates to a positive endpoint density.

**(b) Independent counterexample.** Work in the included Hecke subalgebra
`H_2(q)`.  Let

`e_+=(T_1+1)/(q+1)` and `e_-=(q-T_1)/(q+1)`.

These are the two spectral projections, with coefficient-trace weights
`tau_q(e_+)=1/(q+1)` and `tau_q(e_-)=q/(q+1)`.  Define the orbit-basis-rational
family

`h(q)=(q-3/2)e_+ + (5/(2q))e_-`.

For every prime power `Q>=2`, both spectral coefficients are nonnegative, so
`h(Q)>=0`, and

`tau_Q(h(Q))=((Q-3/2)+Q(5/(2Q)))/(Q+1)=1`.

Its coefficients have finite evaluation at one and `tau_1(h(1))=1`, so it is
regular under D1249.  But

`h(1)=(-1/2)e_+ + (5/2)e_- = 1-(3/2)T_1`

has eigenvalue `-1/2` in the trivial summand of `C[S_2]`; it is not positive.
Thus positivity on all arithmetic fibres cannot be continued to one, because
the prime powers do not accumulate there.  The same example lies in `R_2(q)`
through `i_q`.  Separately, a state or Kraus list at one fixed fibre has no
well-typed “evaluation”: its scalar coefficients are data at that fibre, not a
section in a parameter category.

**FIX DEMAND.** Define the actual section/germ category and its operational
morphisms, and restrict evaluation to sections positive (and effects bounded)
on a real punctured neighbourhood of one, with regular coefficient limits;
define regular Kraus sections and prove that normalization, composition and
the GNS quotient are preserved.  Alternatively require endpoint positivity
explicitly rather than infer it from arithmetic fibres.

**SURVIVING WEAKER STATEMENT.** The based algebra and coefficient trace
specialize algebraically at `q=1`; their reference GNS quotient is `C[S_n]`.
A regular section which is positive for every real `q` sufficiently close to
one induces a positive normalized functional on that quotient by taking the
limit of `tau_q(x^*h(q)x)`.

### O2 — MAJOR: the asserted direct-sum monoidality ignores the flag register

**(a) Exact location.** `vector-mirabolic.md` `<1>28`, especially `<2>2`.
The sentence “It is monoidal under the canonical identifications for direct
sums of vector spaces” follows a construction containing both the Fourier
transform and the dual-flag unitary, but the justification treats only the
Fourier kernel.

**(b) Independent counterexample.** Take one-dimensional `L=M=F_2`.  Each
`Fl(L)` and `Fl(M)` is a singleton, while `Fl(L direct-sum M)` has three
elements (the three lines of `F_2^2`).  Therefore

`C[Fl(L direct-sum M)]` has dimension `3`, whereas
`C[Fl(L)] tensor C[Fl(M)]` has dimension `1`.

Even adjoining `Sh(1,1)` gives dimension `2`, the proper decomposable-flag
subspace, not the full dimension `3`.  The vector Fourier factor does satisfy
`F_(L direct-sum M)=F_L tensor F_M`, but the full unitary
`W=D tensor F` has no such direct-sum identification on complete-flag
registers.  D1256 and MIR-DEC correctly replace it by a proper
compression/shuffle correspondence.

**FIX DEMAND.** Restrict `<1>28`'s monoidal sentence to the vector Fourier
factor, and state any compatibility of the full flag/Fourier bridge only
through the D1256 decomposable corner and its shuffle isometry.

**SURVIVING WEAKER STATEMENT.** MIR-FOURIER's fibrewise unitary conjugation and
naturality for linear isomorphisms are correct.  Direct sum gives a monoidal
Fourier transform on vector registers and a coherent decomposable-flag
correspondence, not a monoidal identification of full flag registers.

### O3 — MAJOR: the executable checker does not meet its own B1--B7 acceptance contract

**(a) Exact location.** `CHECKER-SPEC.md` B1 lines 44--63, B2 lines 65--80,
B3 lines 82--104, B4 lines 106--126, B7 lines 181--196, and the acceptance
record at lines 198--204; `bridge_check.py` functions `fourier_tests`,
`type_c_tests`, `shuffle_tests`, and `main` (lines 103--132, 211--266,
292--324).  `CLAIMS-PROPOSED.md` rows `F1-MIR-EXPECT`, `F1-MIR-END`,
`F1-TC-ONE`, and `F1-MIR-DEC` accurately say the missing tests are merely
requested, so those rows have not fabricated a pass; the proposed promotion
record nevertheless does not satisfy L1 or the checker's own acceptance text.

**(b) Independent reachability test.** The executable has only B3, B5 and B6.
The specified modes `--red-mir-kernel`, `--red-mir-line`,
`--red-dual-reversal`, `--red-mir-expect`, and `--red-affine-dec` each exit
`2` at argument parsing and reach no mathematical gate.  B1, B2, B4 and B7
do not exist in the code.  The implemented B3 also samples `p=2,3`,
`n=1,2`, while `CHECKER-SPEC.md` lines 89--90 say `F_2`, `n=2,3`; its
`--red-fourier` mutation changes the annihilator projector, not the specified
dual-flag reversal or relative-position map.  Hence the claimed B3 flag part
has no mutation reachability either.

I independently filled only selected audit samples, which cannot substitute
for the frozen checker's contract: for `n=2`, `Q=2,3` I found seven affine
pair orbitals and exact generated-algebra dimension seven from `T_0,T_1`,
with the stated quadratic relation and projection; for `n=4`, `Q=2,3`, every
one of the 24 antichain-valency sums was `Q^4`; and the thin indices for
`(m,n)=(1,1),(1,2),(2,2),(1,3)` were `2,3,6,4`, equal to the shuffle counts.

**FIX DEMAND.** Implement B1, B2, B4 and B7 with their named data mutations,
implement the specified dual-reversal/relative-position B3 mutation, align
B3's sample declaration with its code, and record the exit path of every
mutation before promotion.

**SURVIVING WEAKER STATEMENT.** The present checker is valid evidence for its
implemented subclaims: exact Fourier projection conjugation including index
zero, the `Sp_4(F_2)` corner scale and trace pairing, and three shuffle-set
coherence samples.  Root L10 and L12 remain valid rank-one endpoint and
`n<=3`, `Q=2,3` valency falsifiers.

### O4 — MINOR: the proposed definitions are not notation- and star-complete

**(a) Exact location.** `DEFINITIONS-PROPOSED.md` D1241 line 11, D1246 lines
68--76, D1242--D1244 lines 23--55, and D1259 lines 194--201.

**(b) Independent check.** D1241 reuses `A_L` for `GL(L) semidirect L`, while
the current `notation.md` and D8/D16 already reserve `A_L` for a Weyl
subalgebra.  D1246 calls its structure a star-trace family without defining
the conjugate-linear star which MIR-POS assumes.  `C_i^Z` is used in the claim
and proof but is not explicitly introduced in D1242--D1244.  Finally, D1259
requires preservation of a “phase-labelled Fourier square” without stating
it.  Direct calculation from the chosen negative Fourier kernel gives

`W_(L^vee,psi) W_(L,psi) e_(F,x)=e_(F,-x)`

under the canonical double-dual identification (the identity on vectors in
characteristic two).  This missing formula is exactly where the sign and phase
convention should be pinned.

**FIX DEMAND.** Rename the affine group symbol, define the conjugate-linear
orbit-basis star and `C_i^Z`, and state the Fourier-square formula with its
double-dual identification before integrating D1241--D1259 into the single
sources.

**SURVIVING WEAKER STATEMENT.** The proof shards make the intended affine
group, physical star and controlled-Z operators recoverable, and the chosen
Fourier sign is internally consistent in every characteristic.

### O5 — MINOR: the type-C shard cites stale proposed-definition numbers

**(a) Exact location.** `type-c-correspondence.md` introductory line 5 and
ASSUME steps `<1>1`, `<1>10`, `<1>20`, `<1>28`, and `<1>37` (lines 15--16,
105--106, 195, 252--253, and 317--318).

**(b) Independent register comparison.** The actual proposal puts the type-C
context, decomposable flags, arena, CP maps, coherence, thin block and affine
arena at D1250--D1256.  The shard instead invokes D1249 in TC-DEC and TC-CP,
D1252 in TC-COH, D1253 in TC-ONE, and D1254 alone in MIR-DEC.  D1249 is the
unrelated density-specialization definition.  The claims table uses the
correct references, and each proof section restates enough data that this is
a reference defect rather than a mathematical counterexample.

**FIX DEMAND.** Replace the stale ASSUME/header references by the exact
D1250--D1256 dependencies used in each section.

**SURVIVING WEAKER STATEMENT.** The type-C and affine correspondence arguments
remain well typed from their displayed local data; the root/proposal pointers
do not yet certify that typing.

## VERIFIED CORRECT — do not churn in repair

The following items were independently recomputed or reduced to the displayed
finite-group/operator identities.  These conclusions exclude only the scopes
identified in O1--O5.

1. `vector-mirabolic.md` MIR-AFF `<1>1`--`<1>9`: `A/B ~= Fl(L) times L`,
   diagonal affine invariance gives the difference kernel, matrix composition
   is Rosso's equation (6), the physical adjoint is flag swap plus vector
   negation, and normalized matrix trace is faithful.  Rosso Section 3 and
   Theorem 3.6 in the local primary source support exactly the convolution,
   orbit basis, Hecke inclusion and generation used here.
2. MIR-GEN `<1>10`--`<1>17`: the zero-vector Hecke orbital is
   `A_w tensor I`, `(T_0+I)/Q=C_1^X`, its trace is `1/Q`, and the quadratic
   relation and generation follow.  Independent full matrices at
   `(n,Q)=(2,2),(2,3)` gave commutant and generated dimensions `7=7`.
3. `reference-trace.md` MIR-VAL `<1>1`--`<1>10`: the intersection-of-Borels
   pattern group has antichain-labelled vector orbits of size
   `(Q-1)^|A| Q^(|down_w(A)|-|A|)`, giving the stated orbital valency after
   the `Q^ell(w)` flag factor.  The argument uses no division by two and covers
   all finite fields, including characteristic two.  In addition to root L12,
   I checked the partition identity for every `w in S_4` at `Q=2,3`.
4. MIR-POS `<1>11`--`<1>19`: disjoint orbital supports give the diagonal Gram
   polynomial; equality at infinitely many prime powers is a valid Laurent-
   polynomial identity; all entries are strictly positive for real `q>1` and
   semidefinite at one.  This is a proof from the polynomial Gram formula, not
   an inference from arithmetic samples.
5. MIR-EXPECT `<1>20`--`<1>25`: coefficient deletion is the tracial
   orthogonal projection onto the Hecke star subalgebra and hence its
   trace-preserving UCP conditional expectation.  The inclusion preserves
   Hecke densities, effects and normalized Kraus relations at each fixed
   `q>1`.
6. MIR-END `<1>26`--`<1>38` and `<1>40`: the specialized reference radical is
   exactly the span of nonempty-antichain orbitals, it is a two-sided star
   ideal, the quotient is the traced star algebra `H_n(1)=C[S_n]`, and the
   displayed pole-density family correctly shows why the full algebraic and
   GNS endpoints differ.
7. MIR-FOURIER `<1>18`--`<1>27` and the isomorphism-naturality part of
   `<1>28`: the named negative-kernel Fourier transform is unitary and sends
   `P_U^X` to the diagonal projection indexed by `U^perp`; dual flag reversal
   sends `i` to `n-i` and relative position `w` to `w_0 w w_0`.  I checked the
   rank-matrix formula for every permutation through `n=5`.  The endpoint
   `C_1^X -> C_0^Z` in rank one and all characteristic-two signs are correct.
8. `type-c-correspondence.md` TC-DEC and TC-CP `<1>1`--`<1>19`: component
   flags plus a shuffle biject with decomposable flags; the local commutant
   corner is the tensor product with the full shuffle matrix algebra;
   compression is UCP and normalized-trace preserving; and
   `r^(-1)E_G` is its UCP, trace-preserving trace adjoint.  The scale follows
   from `E_G(p)=rI`; in the checked `Sp_4(F_2)` case it is `5/2`.
9. TC-COH `<1>20`--`<1>27`: both nested shuffle expansions identify with the
   same ternary word, both restrictions are compression to the same projection,
   and uniqueness of normalized-trace adjoints gives coherent preparations
   with the product of rank fractions.
10. TC-ONE `<1>28`--`<1>36`: `B_m times B_n` is a proper full-rank
    nonparabolic subgroup, its coset representatives are unsigned shuffles,
    and the left-regular restriction has commutant
    `C[B_m] tensor C[B_n] tensor M_Sh` up to the stated opposite convention.
    The Poincare ratio evaluates to one.  Independent ranks through total rank
    four gave the expected indices `2,3,6,4`.
11. MIR-DEC `<1>37`--`<1>43`: retaining every vector label gives the asserted
    exterior-product local representation; affine transitivity yields the same
    scaled-average UCP pair, and the ternary shuffle argument supplies
    arithmetic three-factor coherence.  For `F_2 direct-sum F_2`, the full
    flag-vector rank is `12`, the decomposable rank is `8`, and the averaging
    fraction is `2/3`.

## Statement/proposal register check

All twelve proposed rows remain `SKETCH`; none is yet present in the root
`claims/CLAIMS.md`, and D1241--D1259 are not yet in root `definitions.md`.
That is honest pre-admission register separation.  No proposed dependency is a
REFUTED root row.  At the exact scopes written in `CLAIMS-PROPOSED.md`, the
twelve theorem statements survive my mathematical recomputation.  O1 defeats
the stronger operational-evaluation language in D1249/D1258 and
`reference-trace.md` `<1>39`; O2 defeats an extra monoidality sentence not
needed by the MIR-FOURIER row.  O3 blocks promotion under L1 until the declared
computationally reachable gates exist.  O4--O5 must be corrected when copying
the proposals into the single sources.

## Checker and mutation reachability record

* `python3 theory/lanes/f1-limit/bridge/bridge_check.py`: exit `0`; B3 `21`,
  B5 `807`, B6 `3` exact probes.
* `--red-fourier`: exit `1` at B3's Fourier-constraint comparison for
  `(p,n)=(2,1),(3,1)`; B5 and B6 still passed.
* `--red-typec-scale`: exit `1` at B5's group-average, unit and trace-pairing
  paths; B3 and B6 still passed.
* `--red-shuffle`: exit `1` at B6 for all three rank triples; B3 and B5 still
  passed.
* The five mutations named in O3: exit `2` in argument parsing, with no gate
  reached.
* `python3 theory/checks/f1_limit_check.py`: exit `0`; all L1--L14 passed,
  including L10 `49` and L12 `190` probes.
* Root `--red-null-weight`: exit `1` specifically at L10's `limiting reference
  null sector`; L1--L9 and L11--L14 passed.
* Root `--red-valency`: exit `1` specifically at L12's `mirabolic orbital
  valency factor`; all other gates passed.

The executed B3, B5, B6, L10 and L12 equalities compare independently built
finite data and do not simplify to identities of textually identical
expressions.  The missing B1/B2/B4/B7 paths and dual-reversal path are
unreachable, as recorded in O3.

FAIL(O1,O2,O3)
