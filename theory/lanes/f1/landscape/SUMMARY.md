# F1 landscape for the arithmetic-quantum-mechanics sidequest

## Defensible conclusion

There are several mature F1 analogies, but they preserve different structures.
The literature supports three positive inputs to this campaign:

1. Direct “quantum F1” formalisms exist.  Chang--Lewis--Minic--Takeuchi obtain a
   classical, no-superposition `q=1` specialization of modal finite-field
   quantum mechanics.  Thas develops a richer absolute theory over
   `F_{1^ell}` with support orthogonality, monomial time evolutions and
   observables, a precise monomial unitary group, and cloning/deletion results.
2. A blueprint arithmetic-base model of the reference Heisenberg group exists:
   Lorscheid proves that standard-parabolic unipotent radicals in `GL_n` have
   Tits--Weyl models, and the `GL_3` maximal unipotent radical is the `UT_3`
   presentation of D5's `H_{beta_0}`.
3. Reductive symmetry has a rigorous F1 shadow: Tits--Weyl models recover
   ordinary Weyl groups, and split reductive models over `F_1^2` recover
   extended Weyl/Tits groups.
   Cyclotomic F1 extensions rigorously retain roots of unity in several related,
   but nonidentical, conventions.

None of these results alone supplies D3--D9.  The missing bridge is a realization
that takes the F1 arithmetic/geometric object to a finite ring or field and then
adds a named additive character, a complex embedding of phases, a cocycle, and
the resulting complex representation.  This is a gap with concrete construction
routes, not a universal no-go theorem about F1 geometry.

## Comparative map

| Literature lane | What is actually developed | Relevant payload | Boundary for this campaign |
|---|---|---|---|
| Deitmar monoid schemes | Multiplicative monoids, monoid-algebra base extension, toric geometry; `GL_n(F_1)=S_n` and symplectic F1-points give Weyl groups | A minimal combinatorial/base-extension skeleton | Native addition is absent; the paper gives no additive/Heisenberg group law or quantum representation |
| Cyclotomic `F_{1^n}` | Roots-of-unity monoids (Deitmar/Thas) or blueprints whose associated ring is `Z[zeta_n]` (Lorscheid) | A natural home for finite phase groups and Frobenius-like power maps | Does not select an additive character or a complex primitive root; conventions have different base extensions |
| Blueprints and Tits--Weyl models | Split reductive groups, parabolics/Levis, standard `GL_n` unipotent radicals; Weyl and base-extension functors | A real F1 model of `UT_3=H_{beta_0}` and of `Sp_2`; clean thick/thin symmetry comparison | Weyl extension of a unipotent group is trivial; representation means geometric action on F1 projective space |
| Bands/crowds | Partial additive relations, flag varieties over the Krasner hyperfield, relational algebraic-group actions | A current framework that exposes the failure of ordinary matrix multiplication over F1; restricting its `SL_3` crowd yields a concrete candidate Heisenberg crowd | The Heisenberg specialization is this lane's derivation, not a theorem in LT23; no central character or Hilbert realization follows |
| Borger Lambda geometry | Frobenius-lift descent data on ordinary schemes over `Z` | A route for asking whether a global arithmetic quantization descends compatibly at all primes | Different notion of F1; even `GL_n` requires an automorphism-object construction |
| Chang et al. quantum `F_un` | Projective finite-field model specialized combinatorially to `q=1` | Explicit disappearance of superposition and entanglement in the basic two-level example | Physical state coefficients are changed to F1; there is no complex Hilbert realization or Heisenberg algebra |
| Thas absolute quantum theory | `F_{1^ell}` frames, partial Hermitian form, support orthogonality, monomial unitaries/observables, cloning/deletion analysis | Developed quantum-information analogies and a finite phase-permutation operator skeleton | “Unitary” is monomial over F1 coefficients; no D3 additive phase datum or D4 twisted algebra |
| Bejleri--Marcolli QFT over F1 | Torifications and motives of varieties attached to Feynman integrals | A genuine F1/QFT geometry connection | Explicitly not a physical Lagrangian or Feynman-rule theory over F1 |

## Claim--source map

| Claim | Status and exact source |
|---|---|
| The `q=1` modal model loses superposition and, for two levels, all entangled states. | Direct: CHANG14 section 2.4, eqs. (17)--(23), pp. 8--9; section 3.2, eqs. (32)--(34), pp. 11--12. |
| Thas's absolute theory has an inner-product analogue and monomial dynamics. | Direct: THAS18 sections 3.3--3.5, eqs. (6)--(11), pp. 5--6; Theorem 4.2, pp. 6--7. |
| Its cloning result is nuanced: all frame states cannot be cloned, but simple projective rays can. | Direct: THAS18 section 6, pp. 8--9. |
| Deitmar's F1 linear automorphisms recover `S_n`, and his `Sp_{2n}(F_1)` recovers the Weyl group. | Direct: DEITMAR06A section 5.1, pp. 14--16; section 5.2, p. 16. |
| Cyclotomic-extension conventions differ materially. | Direct: THAS16 section 1.3, pp. 2--3; LORSCHEID13 section 1.1.4, pp. 14--15. |
| Tits--Weyl models recover `N(T)/C(T)` and F1^2 points recover the Tits extension. | Direct: LORSCHEID12 Definition 3.13 and Theorem 3.14, pp. 49--51. |
| Standard-parabolic unipotent radicals in `GL_n` have Tits--Weyl models, while general unipotent-radical existence was left open there. | Direct: LORSCHEID12 Remark 5.4 and Proposition 5.5, pp. 78--79. |
| The reference Heisenberg group D5 is covered by that result. | Derived: specialize Proposition 5.5 to `UT_3` and use the displayed coordinate multiplication in `evidence/tits-weyl-unipotent.md`. |
| Tits “unitary representations” yield Weyl-group permutation actions on F1 projective geometry. | Direct: LORSCHEID13 section 3.2, pp. 27--28. |
| Newer band geometry replaces problematic group multiplication by crowd relations. | Direct: LT23 introduction pp. 3--5 and section 5, pp. 10--11. |
| QFT-over-F1 motives are not amplitudes-over-F1. | Direct and explicitly scoped: BM12 introduction pp. 1--2; positive construction Theorem 4.6, pp. 16--17. |

## Weyl groups are not Weyl operators

The same word labels different objects here.

- In Tits--Weyl geometry, `W(G)=N(T)/C(T)` is the finite reflection group of a
  reductive group scheme.  For a unipotent radical it is trivial.
- In D4, `W_beta(v)` is a basis element/operator in a complex twisted group
  algebra indexed by the additive phase space.  Its multiplication uses the
  chosen additive character `psi` and cocycle `beta`.
- For `G=Sp_2=SL_2`, the nontrivial F1 Weyl-group element is a combinatorial
  reflection.  After base extension and a chosen Weil representation, a chosen
  lift can act by a Fourier-type operator.  That last step requires `psi`, phase
  normalization, and often a metaplectic/projective lift; it is not contained in
  the F1 Weyl-group theorem.
- The F1^2 Tits group is a promising carrier of lift/sign information because it
  retains toral 2-torsion, but it is still a group-scheme statement, not an
  operator construction.

## Additive characters and `q -> 1`

The inspected frameworks give no canonical limit of nontrivial additive
characters.

- Finite fields exist only at prime powers.  CHANG14 explicitly calls literal
  substitution `q=1` illegitimate and then performs a direct combinatorial
  specialization.
- Tits/Lorscheid `q -> 1` arguments use counting polynomials, Gaussian
  coefficients, buildings and Coxeter complexes.  They retain incidence/Weyl
  data, not a continuous family of fields or characters.
- `F_{1^n}` retains `mu_n` multiplicatively.  An additive character
  `(F_q,+) -> C^x` needs the additive group after realization and a choice of
  complex root.  The phase group alone is insufficient.
- Thus the honest interface is stratified: an F1 combinatorial/arithmetic
  skeleton; base extension to a finite arithmetic object; then a separate phase
  realization `(psi,beta,zeta)` into complex operators.  Any theorem of
  canonicity must state which layer supplies each choice.

## Constructive routes, ordered by proximity to D3--D9

1. **Blueprint Heisenberg realization.** Start from the Tits--Weyl model of the
   `GL_3` maximal unipotent radical.  Verify base extension to `UT_3(kappa)`, use
   the coordinate identification with `H_{beta_0}(kappa)`, then apply D3--D9 as
   a complex realization functor.  The first research question is whether this
   construction is functorial in blueprint/semiring maps and how nonreference
   cocycles `beta` should be represented.
2. **Symplectic reflection to Fourier operator.** Start with the Tits--Weyl model
   of `Sp_2`.  Compare its Weyl reflection and F1^2 Tits lift, after finite-field
   base extension, with the projective Weil operator implementing the Fourier
   transform.  Record the additive character and Gauss-factor normalization as
   realization data.  This route tests exactly how much of a quantum symmetry is
   already present over F1.
3. **Cyclotomic phase object.** Test Lorscheid's cyclotomic blueprint
   `F_{1^p}` as the source of the universal `mu_p` phase and compare its complex
   embeddings with the explicit `zeta` choice in D3.  Do not use the notation
   `F_{1^p}` without fixing whether its base extension is `Z[mu_p]` or
   `Z[zeta_p]`.
4. **Complex shadow of Thas's monomial theory.** Embed
   `mu_ell wr S_m` into the monomial unitaries of `C^m` and compare it with the
   frame-preserving automorphisms in D7/D11.  This can identify the exact
   combinatorial symmetry retained by absolute quantum theory without claiming
   that it is the Heisenberg/Weyl operator group.
5. **Tensor/entanglement comparison.** Contrast Chang's loss of entanglement at
   amplitude base F1 with the complex tensor products produced after arithmetic
   realization.  A worked two-site example would sharply distinguish
   “amplitudes over F1” from “arithmetic base over F1, amplitudes over C.”
6. **Heisenberg crowd.** Develop the candidate in
   `HEISENBERG-CROWD-CANDIDATE.md`: restrict LT23's `SL_3` algebraic crowd to
   upper-unitriangular matrices.  Its ring-valued points recover `UT_3`, and
   over the regular partial field its partial products already retain the
   central cross-term.  The next question is how a central-character
   realization interacts with the crowd relation.

## Remaining gaps

- No inspected primary source constructs a nontrivial additive character over
  F1, a canonical `q -> 1` degeneration of such characters, or a Stone--von
  Neumann theorem in an F1 category.
- LORSCHEID12 covers the reference `UT_3` group law, but not the full cocycle
  torsor of D2 or the characteristic-two distinctions central to this repo.
- The Tits--Weyl model generally depends on a chosen linear representation
  (LORSCHEID13 Remark 2.6).  A north-star claim of canonicity would have to
  control that dependence.
- The direct F1 quantum papers develop projective/monomial kinematics and
  quantum-information analogies, not a functor from arbitrary arithmetic schemes
  to complex quantum systems.
- This lane did not adjudicate Bost--Connes/arithmetic-site, quantum-torus,
  Poisson, tropical, or Lambda-global routes beyond the narrow BORGER09
  comparison; those belong to the coordinating landscape.

The consequential landscape claims now have primary evidence.  No claim here
asserts a universal obstruction across all F1 frameworks.
