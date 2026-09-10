# Completion controls — bounded work order for SP-FOCK, SP-PRIME, SP-BC-CONTROL

Date: 2026-09-10. Planning model: `gpt-5.6-sol`, reasoning `xhigh`.

This is one bounded campaign for the three remaining formulated completion
claims. It does not construct the global phantasm, identify modular and
physical flows, classify factors, or attach any operator to zeta zeros. Keep
all three claims SKETCH through proof and checker work.

**Completed 2026-09-10:** SP-FOCK, SP-PRIME and SP-BC-CONTROL are admitted
through `theory/verdicts/phantasm-completions-adjudication.md`. The planning
instructions below are preserved as their work order; current statuses live
in CLAIMS and the DAG. The next work order is `briefs/phantasm-char2-target.md`.

## Canonical ownership gate

The exact proposed D1708/D1711 replacements are in
`briefs/phantasm-completions-interfaces.md`. They were registered before proof work on 2026-09-10. D1708 additionally
spells out the space superscript on P and the algebraic tensor symbol;
D1711 uses the explicit phrase separating reference vector. This ownership
registration carries no property admission.

Two formulas should be owned before a proof calls them canonical.

1. D1708 defines `Gamma_s(H)` and `Gamma_s(T)` but does not prescribe the
   exponential-law unitary or its direction. Add a name and the homogeneous
   formula

       U_(H,K):Gamma_s(H) tensor Gamma_s(K) -> Gamma_s(H direct-sum K),
       U_(H,K)(xi_n tensor eta_m)
         =sqrt((n+m)!/(n!m!)) P_(n+m)
            (i_H^tensor-n xi_n tensor i_K^tensor-m eta_m).

   Here the displayed tensor is ordered with all `H` slots before all `K`
   slots. The CLAIMS direction uses `U_(H,K)^*`. Record the vacuum and zero
   unit convention. Do not label this a strong symmetric monoidal structure
   or add coherence claims not present in SP-FOCK.

2. D1711's phrase “with the required coordinate reordering” should be expanded
   on increasing-prime simple tensors:

       iota_QP(tensor_(p in P) a_p)=tensor_(q in Q) b_q,
       b_q=a_q if q in P, and b_q=1_(H_q) otherwise.

   This owns the insertion order used by the proof and checker. It introduces
   no inter-prime arithmetic map.

D1712 already owns the represented operators, the maximal diagonal domain of
`H_log`, the flow, `nu_n`, `L_n`, and the Gibbs density. A proof-local
`q_n=mu_n mu_n^*` suffices to describe the corner; add a canonical name only
if later claims will reuse it. D1713 owns GNS and makes a separating reference vector an
additional modular hypothesis, so SP-PRIME must not infer it.

## Exact source ledger

- SP-DER06 lines 1814--1829 define the completed Hilbert tensor Fock space and
  vacuum; 1843--1851 state `Gamma(p)` and the exact boundedness boundary
  `||p||<=1`; 1871--1875 give composition; 1911--1964 define symmetric Fock
  sectors; 2019--2038 restrict second quantization to them; 2051--2090 give
  the normalized exponential unitary, vacuum, and natural operator square.
- SP-WAT18 lines 3029--3039, equation (2.18), support finite product density
  operators. They do not prove an infinite prime-indexed state extension.
- SP-CM08 lines 30474--30493, equations (4.117)--(4.119), give norm completion
  and the GNS quotient/completion/double commutant. Its nearby separating
  phrase is not valid input for arbitrary nonfaithful chosen densities;
  D1713 correctly separates that modular hypothesis.
- No exact SP-CM08/SP-WAT18 locator was found for D1711's specified unital
  prime-set inductive system. Prove that elementary construction in full; do
  not attribute it to a stronger source theorem.
- SP-CM04 lines 1763--1783 give the BC generator relations, corner average,
  and time action; lines 1829--1837 identify the low-temperature partition
  function as zeta. SP-CM08 lines 23015--23025 and 23106--23114 give the same
  presentation and dynamics; lines 23930--23947 give the represented basis,
  `H delta_m=log(m)delta_m`, and `Tr(e^-bH)=sum m^-b=zeta(b)`.
- SP-BC95 is historical primary provenance but its pinned scan has no readable
  formula extraction. SP-SPECTOR98 concerns arithmetic-gas analogies and is
  unnecessary for the exact represented BC proof. SP-JOY81 belongs only to
  the later DG-RIG comparison.

## SP-FOCK proof shard

Write `theory/symplectic-phantasm/fock.md` with these leaves.

1. Show `T^tensor-r` commutes with permutations and maps `Sym^r H` to
   `Sym^r K`. For a contraction, its sector norm is at most `||T||^r<=1`;
   hence the Hilbert direct sum is bounded. Because the vacuum sector is the
   identity, `||Gamma_s(T)||=1`, including strict contractions.
2. Prove sectorwise identity and composition for the category whose objects
   are complex Hilbert spaces and arrows are contractions. Do not extend the
   functor to arbitrary bounded expansive maps: for `||T||>1`, sector norms
   grow as `||T||^r`.
3. For homogeneous symmetric `xi_n,eta_m`, split `S_(n+m)` into
   `(n,m)`-shuffle cosets and prove

       ||P_(n+m)(i_H xi_n tensor i_K eta_m)||^2
         = n!m!/(n+m)! ||xi_n||^2 ||eta_m||^2.

   This proves the prescribed normalization is isometric. The mutually
   orthogonal occupation summands exhaust every `Sym^r(H direct-sum K)`, so
   the map extends to a unitary on the completions.
4. Prove naturality for contractions `S:H->H'`, `T:K->K'` first on homogeneous
   finite-particle tensors and then by density and boundedness.
5. Compute `Gamma_s(0)=C`. For a unit vector `e in C`, send the D1010
   orthonormal basis `x^r/sqrt(r!)` to `e^tensor-r`; extend to
   `F_bos ~= ell^2(N_0)`. Under this unitary, the D1708 number operator has
   eigenvalue `r` and its stated weighted-square-summability domain.

## SP-PRIME proof shard

Write `theory/symplectic-phantasm/prime-tensor.md`.

1. Use finite prime sets ordered by inclusion and increasing prime order.
   Check the explicit insertion maps are injective unital star-homomorphisms,
   obey `iota_RQ iota_QP=iota_RP`, and preserve the operator norm. Include
   `P=empty`, where `A_empty=C`.
2. Form the algebraic direct limit using the isometric maps. Its norm is
   independent of stage, multiplication and star are continuous, its unit is
   common to all stages, and the completion is a unital C-star algebra.
3. At stage `P`, put `rho_P=tensor_p rho_p` and
   `phi_P(a)=Tr(rho_P a)`. Prove positivity, `phi_P(1)=1`, and compatibility
   under identity insertion. The compatible functional on the algebraic union
   has norm one and therefore extends uniquely and positively to `A_pr`.
4. Give the standard GNS construction from D1713: prove Cauchy--Schwarz,
   boundedness of left multiplication, cyclicity of `[1]`, and set
   `M_pr=pi_phi(A_pr)''`. Assert neither a separating reference vector nor extra faithfulness
   conclusions: allowed `rho_p` may be rank deficient. Keep state faithfulness,
   representation faithfulness, and the separating-vector property distinct.

Local choices are exactly every `d_p>=1`, every positive trace-one `rho_p`,
increasing prime order, and the identity-insertion embeddings. This is not an
all-prime Weyl assignment, factor classification, or arithmetic coupling.

## SP-BC-CONTROL proof shard

Write `theory/symplectic-phantasm/bc-control.md`.

1. On basis vectors derive `mu_m mu_n=mu_(mn)`, `mu_n^*mu_n=1`, and
   `mu_n^*delta_k=[n divides k]delta_(k/n)`. Exhibit
   `mu_n mu_n^* !=1` for `n>1`.
2. Compute `mu_n^*e(r)mu_n=e(nr)`. For the other corner, parameterize the
   solutions of `ns=r` by `(r+j)/n` and use the finite root average to prove

       mu_n e(r) mu_n^*=(1/n) sum_(ns=r)e(s).

3. Let `q_n=mu_nmu_n^*`. Show `nu_n(a)=mu_n a mu_n^*` maps the represented
   algebra star-homomorphically onto `q_n A q_n`; its inverse on the corner is
   the restriction of `L_n`. Show `L_n(a)=mu_n^*a mu_n` preserves the algebra,
   is one-Kraus CP, and is unital. Do not call `L_n` multiplicative.
4. Prove the diagonal multiplication operator `H_log` is self-adjoint on the
   D1712 domain. Functional calculus gives
   `exp(iuH_log)mu_n exp(-iuH_log)=n^(iu)mu_n` and fixes `e(r)`. Extend from
   the generator star-algebra by density to invariant automorphisms and prove
   point-norm continuity.
5. For real `b>1`, compute `e^(-bH_log)delta_m=m^(-b)delta_m`. Use the integral
   test to prove trace-class convergence, not a numerical truncation. Its
   trace is D1712's `zeta(b)`, so `rho_(BC,b)` is positive with trace one.

This shard proves no KMS classification, universal-presentation faithfulness,
factor type, modular-flow equality, Frobenius comparison, global arithmetic
map, or zeta-zero spectrum.

## Exact checker lane

Pre-register `phantasm_completions_EXPECTATIONS.md`, then implement one exact
`phantasm_completions_check.py`. Passing it is finite evidence only.

- F1: rational permutation symmetrizers through sector 4 for dimensions
  zero, one, and two; projection, sector dimensions, vacuum, and one-mode
  occupation basis. F2: verify the binomial norm-square identity and
  exponential naturality without floating square roots. F3: sectorwise
  contraction composition and the norm growth of `2I`.
- P1: for `empty,{2},{3},{2,3},{2,3,5}`, use unequal dimensions and check all
  embedding triangles, units, stars, products, and exact characteristic
  polynomials of `a^*a` under identity tensoring. P2: use rational faithful
  diagonal and pure densities; check state compatibility, positivity on
  `x^*x`, GNS Gram ranks, cyclicity, and a concrete failure of separating for
  a pure local state.
- B1: use symbolic basis indices, never truncated shift matrices, for the
  semigroup and adjoint laws. B2: represent rational phases modulo one and
  the root-average by exact divisibility. B3: represent logarithms by prime
  valuation vectors to check dynamics and map closure. B4: use exact rational
  partial sums and integral upper/lower tail bounds for integer `b=2,3`, plus
  dyadic harmonic lower bounds at `b=1`.

Required distinct reds: omit the Fock binomial factor; delete the vacuum;
accept `2I` as bounded second quantization; replace `r!` by `1` in the one-mode
basis; insert a prime factor in the wrong position; use `a tensor q` with
`q!=1`; use a non-trace-one density; infer separating from cyclic; treat
`mu_n` as unitary; omit `1/n` in the root average; reverse the time exponent;
make `L_n` multiplicative; and accept `b=1` as trace class. Each advertised
red must exit 1 at its own first named gate; unexpected errors exit 2 and a
disabled-gate survivor exits 0.

## Exit discipline

Use three proof shards, one checker lane, one blind critic pass, one repair
wave, and mechanical adjudication. Promote claims independently: a defect in
one shard need not block a correct sibling. Written analytic arguments carry
boundedness, completion, GNS, point-norm continuity, and trace-class results;
finite tests cannot carry them. Completion supplies only these three local
interfaces before any DG-RIG, DG-GLOBAL, DG-MODULAR, or DG-SPECTRUM work.
