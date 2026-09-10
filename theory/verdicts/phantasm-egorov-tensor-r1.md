# Blind hostile verdict — SP-EGOROV and SP-TENSOR

Date: 2026-09-10.

- Critic: `gpt-5.6-sol`, reasoning `xhigh`.
- Prover: `gpt-5.6-sol`, reasoning `xhigh`.
- Independence: same-family prover/critic, blind lane. I read the two proof
  artifacts, their lane-only labbook linearization, the single sources, the
  admitted F1 proofs, and the registered primary-source bodies. I did not read
  the prover's SUMMARY, PATCH, LABBOOK-SUMMARY, or hidden reasoning, and had no
  contact with the prover.
- Reviewed proof snapshots:
  `sp-egorov.md` SHA256
  `49f63c8f7008dd46945977fc87a12cd9dd0d3141e8e50cd37f0550d929a20021` and
  `sp-tensor.md` SHA256
  `d6404c6ad4b907a5efe950d25c5c8a27c4976dd5430d53bd405a221e20fa9ab5`.
- Dependency condition: `SP-WEYL` was still `SKETCH` during this review.
  The conclusions below establish conditional correctness of these drafts;
  they do not authorize promotion ahead of the recorded dependencies.

## Objections

### O1 — MINOR: the arbitrary-rank unitary-model type has no canonical owner

**(a) Exact location.**
`theory/lanes/phantasm-stage1/egorov-prover/sp-egorov.md`,
`<1>6.<2>1`--`<1>6.<2>3` and `<1>8`; and
`theory/lanes/phantasm-stage1/egorov-prover/sp-tensor.md`,
`<1>8.<2>1`--`<1>8.<2>4`. The missing owner is visible by comparing D9 with
D1703: D9 defines `Mod` and `PMod` only for the rank-one algebra on
`V(k)=k+ k`, while D1703 extends the Weyl algebra to arbitrary symplectic
rank but defines only the standard coordinate model and says that an
abstract-space model names coordinates. It does not extend D9's objects,
unitary intertwiners, or `U(1)` quotient to arbitrary rank.

**(b) Independent calculation.** Let the intended model mean a unital
irreducible star-representation `pi_V:A(V)->End(H_V)` in which the Weyl
generators act unitarily, and likewise for `W`. The reviewed algebra
calculation makes `rho=pi_W o alpha_(t,g)` an irreducible star-representation
of `A(V)`. Conditional `SP-WEYL` identifies `A(V)` with `M_d(C)`,
`d=|k|^n`. Simple-module uniqueness gives a nonzero intertwiner `T` from
`pi_V` to `rho`. Then `T^*T` commutes with `pi_V(A(V))`, so
`T^*T=cI`, `c>0`; `U=c^(-1/2)T` is a unitary intertwiner. If `U'` is another,
`U'^*U` lies in the scalar commutant and has modulus one. The identical
argument applies to `(pi_V tensor pi_W) o Theta_(V,W)`, since its image is
the full matrix algebra on `H_V tensor H_W`. Thus the proof is mathematically
correct once the quantified model class is stated, but the current single
source does not state that class.

**(c) FIX DEMAND.** Extend D1703 by explicitly reusing D9's
unitary-model/intertwiner/projectivization prescription for arbitrary-rank
`A_(psi,beta_V)(V)`, preserving D9's rank-one meaning, and make the claim and
proof use that owned type.

**(d) SURVIVING WEAKER STATEMENT.** All exact algebra statements survive,
and for every explicitly supplied pair of finite-dimensional irreducible
unitary star-representations the implementing unitary and tensor comparison
exist uniquely up to `U(1)` and transport as proved.

### O2 — MINOR: the advertised rank-zero mutant dies before the substantive data check

**(a) Exact location.**
`theory/lanes/phantasm-stage1/egorov-checker/egorov_tensor_check.py`, gate E7,
lines 457--459 in reviewed SHA256
`094d379aaff5deed013c135df53cb2e3a7301ac16bb0cfc2b98130ccc63dbdac`;
the red-mode declaration is lines 28 and 587--589.

**(b) Independent calculation.** The advertised `--red-zero-qudit` sets the
synthetic variable `claimed_dimension` to 3 and immediately compares it with
the literal 1. It therefore exits at E7 without reaching the separately
constructed `hilbert_basis`, `zero_op`, or tensor-unit checks. On a copied
checker I instead changed the actual rank-zero Hilbert-basis datum from
`product(F3, repeat=0)` to `product(F3, repeat=1)`. The copy exited 1 at E7
with `rank-zero Weyl model is not one-dimensional`, showing that the
substantive detector is reachable but is not the target of the advertised
mutant.

**(c) FIX DEMAND.** Make `--red-zero-qudit` mutate the actual
`hilbert_basis` datum (or the input rank used to build it), remove the
synthetic `claimed_dimension` precheck, and retain E7 as its first failure.

**(d) SURVIVING WEAKER STATEMENT.** The green E7 enumeration and operator/unit
comparisons are substantive, and an independent data mutation confirms that
they reject a three-dimensional replacement at E7; only the advertised red
path is weaker than claimed.

## Independently verified correct — do not churn in repair

<!-- VERIFIED-CORRECT-BEGIN -->

1. **Affine sign and semidirect order.** From D1703,
   `W(t)W(v)W(t)^*=psi(omega(t,v))W(v)`; both half-form factors contribute
   `omega(t,v)/2`. Hence the positive phase in `alpha_(t,g)` is forced. For
   `(s,h)o(t,g)`, symplecticity gives
   `omega_W(t,gv)=omega_Z(ht,hgv)`, so successive phases add to
   `omega_Z(s+ht,hgv)`. A concrete F3 witness rejects `s+t`: with
   `h=J=((0,1),(2,0))`, `s=0`, and `t=(0,1)`, the correct translated point is
   `ht=(1,0)`, not `(0,1)`.

2. **Algebra and involution.** Linearity of `v -> omega(t,gv)` makes the
   affine scalar a character, and symplecticity preserves the half-form
   cocycle, proving multiplicativity. Since values of `psi` lie in `U(1)`,
   conjugation replaces the exponent by its negative, exactly matching
   `W(v)^*=W(-v)`. The inverse is
   `(-g^(-1)t,g^(-1))` in both orders.

3. **Unitary existence, uniqueness, and model transport.** Conditional on
   `SP-WEYL`, the matrix-algebra/commutant calculation in O1 supplies a
   unitary implementer and proves uniqueness up to `U(1)`, including finite
   dimension. Conjugating by named endpoint model intertwiners gives
   `R_W U_(t,g) R_V^*`; changing any representative changes only its phase.
   Composition implements the already equal algebra composite, so it agrees
   in the projective quotient. No genuine Weil section is used.

4. **Tensor algebra and trace.** The direct-sum cocycle is the sum of the two
   factor cocycles. Additivity of `psi` therefore makes `Theta_(V,W)`
   multiplicative; it carries a Weyl basis bijectively to a tensor Weyl basis
   and preserves star and unit. Both coefficient traces are 1 only at the
   zero label and 0 otherwise, giving exact trace preservation.

5. **F1 tensor reuse.** The admitted `F1-FUNCT` proof is at one fixed level
   `N` and covers configuration isomorphisms, balanced smash, central product,
   the basis map `e_(x,y) -> e_x tensor e_y`, and its associativity, unit, and
   symmetry diagrams. Here `N=p` and `A=(k^m,+)`, `B=(k^n,+)` are within that
   scope. The half-form cochain factors because
   `psi((a1.b1+a2.b2)/2)=psi(a1.b1/2)psi(a2.b2/2)`.

6. **Arbitrary affine tensor naturality.** For factor arrows the direct-sum
   phase is
   `omega_(V')(t,gv)+omega_(W')(s,hw)`, exactly the product of the two factor
   phases. Both routes have label `(gv,hw)`. This proves the algebra square
   for arbitrary affine symplectic arrows, not only generators.

7. **Associator, units, and swap.** Rebracketing, inserting rank zero, and
   swapping factors send each source Weyl generator to the same ordered
   tensor along both algebra routes. At the model level each pair of routes
   implements that same exact full-matrix-algebra map; the scalar-commutant
   calculation therefore proves precisely the asserted projective diagrams.
   The displayed arrows and associators in `<1>6`--`<1>10` are type-correct.

8. **Quantifiers and reliance.** The proofs use a fixed finite field and one
   common nontrivial character, cover arbitrary symplectic rank, include the
   zero space, and consistently exclude characteristic two. The F9 control
   uses the genuinely non-prime character with exponent table
   `(0,0,0,1,1,1,2,2,2)`. No step depends on the sole REFUTED row
   `WH-FUNCT-b-SEC`, an unregistered source, or `v0.1`.

9. **Source scope.** `F1-REAL` sections 2 `<1>5`--`<1>8` and its Prasad
   source body cover the finite Abelian fixed-central-character
   Stone--von Neumann result used here. `F1-FUNCT` section 3 covers the
   configuration product at fixed `N`. SP-GH07/GH09 are only comparisons:
   their functor is contravariant and uses oriented models. SP-GROSS06's
   affine Clifford lemma has the same `w(a)mu(S)` order. The drafts do not
   import any stronger genuine-lift or canonical-model conclusion.

10. **Labbook lockstep.** The lane-only `labbook-stage1.tex` linearizes the
    same product, star, affine-composition, tensor-naturality, trace, and
    projective-coherence arguments without strengthening the proposition or
    scope blocks. It retains `SKETCH` and labels each insertion `Proof draft`.

<!-- VERIFIED-CORRECT-END -->

## Checker and mutation audit

The frozen lane checker passed all E1--E9 gates exactly: 24 matrices in
`Sp(2,F3)`, 216 affine arrows, all 46,656 affine pairs, all 419,904 affine
point/action cases at the relevant gates, translation/Fourier/shear matrix
covariance, rank zero, the F9 non-prime-character control, 81 rank-two Weyl
tensor and swap cases, and 3,779,136 affine tensor-naturality cases.

Every advertised red mode exited 1 at its intended first gate:

| gate | red mode | actual first exit |
|---|---|---|
| E1 | `--red-sp-enumeration` | E1, census 48 rather than 24 |
| E2 | `--red-semidir-order` | E2, concrete point-composition mismatch |
| E3 | `--red-alpha-phase` | E3, affine-action composition mismatch |
| E4 | `--red-translation-sign` | E4, `t=(0,1),v=(1,0)` |
| E5 | `--red-fourier-sign` | E5, label `(0,1)` |
| E6 | `--red-shear-half` | E6, `r=1,v=(1,0)` |
| E7 | `--red-zero-qudit` | E7, synthetic claimed dimension; see O2 |
| E8 | `--red-f9-character` | E8, absolute-trace table mismatch |
| E9 | `--red-tensor-phase` | E9, rank-two affine naturality mismatch |

Independent copied-data mutations also exited 1 at the intended gates:
deleting one point from the F3 phase-space census at E1; replacing the
rank-zero Hilbert-basis datum by the three-element F3 basis at E7; and
changing the F9 character multiplier from `u` to `1` at E8.

The bridge checker `theory/checks/phantasm_reuse_check.py` passed R1--R6
(141,939 reported comparisons after the repaired R4 probes). All eleven
advertised mutations exited 1 at their intended first gates: dual sign and
trivial character at R1; rephase and position labels at R2; cocycle and
central injectivity at R3; entry-derived trace normalization and actual
zero-label identity at R4; tensor phase at R5; character conflation and
relative Frobenius at R6.

The Phantasm contract checker passed G1--G8. All 21 advertised data-copy
mutations exited 1 at their named gates, including the repaired promotion
guard at G4 and inherited/reuse gates at G8. This checks recorded contracts,
not the mathematics.

## Status register check

The proof headers, canonical rows, DAG, current labbook blocks, and lane-only
labbook insertion all retain `SKETCH` and expose `SP-WEYL` (and, for
`SP-TENSOR`, `SP-EGOROV`) as dependencies. That is the honest register during
this review. The admitted comparison rows `F1-REAL` and `F1-FUNCT` are used
only at their proved finite scopes. After O1 and O2 are repaired, promotion
still requires the dependency-order and integration/adjudication records;
this PASS does not itself promote either claim.

PASS
