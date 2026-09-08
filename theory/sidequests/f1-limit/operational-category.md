# The typed operational envelope of the continuous corner family

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

The key type distinction is visible in the notation:

    [alpha] [beta]       separated register word,
    [alpha concat beta]  one collective Hecke-corner atom.

Their observable algebras are respectively `A_alpha tensor A_beta` and
`A_(alpha concat beta)`.  The former embeds properly in the latter in general.

## Proposition OPLIM-1 (register algebras and the Heisenberg target)

**ASSUME** a positive fibre `q`, an interval `I`, or an endpoint germ as in
CLIM-1--3.

**PROVE** D1205--D1206 define honest ordered register objects, normalized
traces, and a strict monoidal Heisenberg process target.

<1>1. For every nonempty composition `alpha`, put

    A_alpha(q)=e_alpha(q)H_|alpha|(q)e_alpha(q),
    tau_alpha,q=P_alpha(q)tau_|alpha|,q.

<2>1. CLIM-2 proves that this is a nonzero finite C*-algebra whose unit is
`e_alpha(q)` and whose displayed trace is faithful and normalized.

<2>2. The empty wire has algebra `C` and its usual state.

<1>2. A quantum register word `X=[alpha_1]... [alpha_r]` has algebra

    A_q(X)=A_(alpha_1)(q) tensor ... tensor A_(alpha_r)(q)

with the spatial tensor product and product trace.

<2>1. All factors are finite dimensional, so the algebraic and spatial
C*-tensor products coincide.

<2>2. Concatenation of words gives equality
`A_q(XY)=A_q(X) tensor A_q(Y)` under the fixed left-associated convention.

<2>3. A nonempty finite classical outcome wire `underline(O)` has algebra
`C^O` and reference trace
`tau_O(f)=|O|^(-1)sum_(o in O)f(o)`.  It may be tensored onto a register word
in the same way.  The empty outcome set is excluded from deterministic
instruments because its zero algebra has no unit or normalized state.

<2>4. A mixed operational word uses these quantum and classical factors in
its displayed order.  Its algebra and trace are the corresponding ordered
spatial tensor products; no permutation of factors is implicit.

<1>3. Define `HCPU_fd` as follows.

<2>1. Its objects are finite-dimensional unital C*-algebras.

<2>2. An arrow `A -> B` is, in Heisenberg orientation, a UCP map
`B -> A`.

<2>3. If arrows `A -> B -> C` are represented by `Phi:B->A` and
`Psi:C->B`, their composite is `Phi o Psi:C->A`.

<2>4. The identity is the identity UCP map.

<2>5. Ordered tensor is the spatial tensor of maps.

<1>4. These rules make `HCPU_fd` a strict monoidal category after the fixed
finite-dimensional tensor associators are strictified.

<2>1. Composition of UCP maps is UCP.

<2>2. Tensor products of CP maps are CP: finite-dimensional Kraus forms
`Phi(a)=sum_i V_i^*aV_i` and `Psi(b)=sum_j W_j^*bW_j` give Kraus operators
`V_i tensor W_j` for `Phi tensor Psi`.

<2>3. Units tensor to units, so the tensor map is unital.

<2>4. Bilinearity gives the interchange equation

    (Phi_2 o Phi_1) tensor (Psi_2 o Psi_1)
      =(Phi_2 tensor Psi_2) o (Phi_1 tensor Psi_1).

<2>5. Thus identities, composition, and ordered assembly are actual category
operations, rather than an untyped collection of maps.

<1>5. A process `X->Y` represented by `Phi:A(Y)->A(X)` sends a density
`rho` on `X` to the unique density `Phi_*(rho)` on `Y` satisfying

    tau_Y(Phi_*(rho)a)=tau_X(rho Phi(a)).

<2>1. Finite-dimensional faithful trace duality gives existence and
uniqueness.

<2>2. Positivity follows from positivity of the functional on the right.

<2>3. Unitality gives `tau_Y(Phi_*(rho))=tau_X(rho)=1`.

<1>6. Steps <1>1--<1>5 prove OPLIM-1. **QED**

## Proposition OPLIM-2 (operational generators)

**ASSUME** D1207--D1209 and a fixed positive fibre `q`.

**PROVE** every proposed generator is typed and has the claimed UCP
realization, with the correct normalized density transport.

<1>7. Every normalized state is an allowed preparation.

<2>1. For any register word `X`, choose any `h>=0` in `A_q(X)` with
`tau_X(h)=1`.

<2>2. The formula `omega_h(a)=tau_X(ha)` is positive and sends the unit to
one.

<2>3. It therefore represents a UCP arrow `prep_h:1->X` in Heisenberg
orientation.

<2>4. The discard `disc_X:X->1` is represented by the unital star-map
`lambda |->lambda 1_X`.

<2>5. Hence preparations and discards exist across arbitrary ranks; no
degree-zero amplitude in `Gamma_q` is required.

<1>8. Every effect and every finite POVM on every register word is allowed.

<2>1. A POVM is a family `e_o>=0` in `A_q(X)` with `sum_o e_o=1_X`.

<2>2. Define `M_e:C^O->A_q(X)` by

    M_e(f)=sum_(o in O) f(o)e_o.

<2>3. If `[f_ij]>=0` in `M_r(C^O)`, then every scalar matrix
`[f_ij(o)]` is positive.

<2>4. Each `[f_ij(o)] tensor e_o` is positive in
`M_r(C) tensor A_q(X)`, so their sum `[M_e(f_ij)]` is positive.

<2>5. Thus every amplification is positive, and the sum condition gives
unitality.

<2>6. This realizes a measurement arrow `X->underline(O)`.  A single effect
`0<=e<=1` is the two-outcome POVM `(e,1-e)`.

<1>9. A normalized corner Kraus instrument from `alpha` to `beta`, where
`|alpha|=|beta|=n`, consists of finite lists

    K_(o,i) in e_beta H_n(q)e_alpha,
    sum_(o,i) K_(o,i)^*K_(o,i)=e_alpha.

Its circuit type retains both outputs:

    K:[alpha]->[beta]underline(O).

<2>1. It represents the map

    Phi_K:A_beta(q) tensor C^O -> A_alpha(q),
    Phi_K((a_o)_o)=sum_(o,i)K_(o,i)^*a_oK_(o,i).

<2>2. Each summand is CP and the total normalization sends the output unit
`(e_beta)_o` to `e_alpha`.

<2>3. Hence `Phi_K` is UCP.

<2>4. The effect of outcome `o` is
`f_o=sum_i K_(o,i)^*K_(o,i)`, and the effects sum to the unit.

<1>10. The branch density transport has a necessary corner-trace ratio.

<2>1. If `rho` is a density in `A_alpha`, define

    T_o(rho)=(P_alpha(q)/P_beta(q))
             sum_i K_(o,i)rho K_(o,i)^*.

<2>2. For `a in A_beta`, cyclicity of the ambient coefficient trace gives

    tau_beta(T_o(rho)a)
      =tau_alpha(rho sum_i K_(o,i)^*aK_(o,i)).

<2>3. At `a=e_beta`, the left side is the branch mass and the right side is
the Born probability `tau_alpha(rho f_o)`.

<2>4. `T_o(rho)` is the unnormalized density on the quantum branch, measured
with `tau_beta`.  Relative to the product reference trace
`tau_beta tensor tau_O`, the density of the full quantum-classical output has
`o`-block `|O|T_o(rho)`.

<2>5. Its total trace is `sum_o tau_beta(T_o(rho))=1` because the total
Heisenberg map is unital.

<2>6. Omitting `P_alpha/P_beta` would give the wrong density whenever the
corner trace normalizations differ.

<1>11. Fibre coefficient-Gram equality is the exact equality of Kraus labels.

<2>1. Expand each fixed-outcome list in the normalized Hecke basis.  Two
labels are equal when the coefficient Grams agree for every outcome.

<2>2. The finite Gram lemma says this is equivalent, at this fixed fibre, to
zero padding and a scalar-unitary Kraus mixing within each outcome.  The
identity `sum_j conjugate(U_(ji))U_(jk)=delta_(ik)` shows every branch CP map
is unchanged.

<2>3. D1218 does not identify differently typed classical outputs.  It
defines sequential and parallel instrument operations by explicit routing,
product, and relabeling boxes, after which the product lists have the claimed
types.

<2>4. Fibrewise unitary cancellation proves that Gram equality is preserved
by those product lists.  This proof is pointwise and requires no continuous
choice of the mixing unitary.

<1>12. A retained right collective context is different from a separated
tensor.

<2>1. For a composition `gamma` of `k`, define

    K_(o,i) triangleleft gamma
      =iota_(n,k)(K_(o,i) tensor e_gamma)
      in e_(beta concat gamma)H_(n+k)e_(alpha concat gamma).

<2>2. Since `iota` is a star-homomorphism,

    sum_(o,i)(K_(o,i) triangleleft gamma)^*
                (K_(o,i) triangleleft gamma)
      =e_(alpha concat gamma).

<2>3. It therefore defines a UCP instrument on the full collective corner,
including observables outside the separated product subalgebra.

<2>4. Coherence of `iota` gives the well-typed nesting identity

    (K triangleleft gamma) triangleleft delta
      =K triangleleft (gamma concat delta).

Compatibility with sequential instruments is stated only through D1218's
routed `Seq` operation, which retains and then products the classical wires.

<2>5. These are equalities of retained lists up to the fixed lexicographic
Kraus indexing, not conclusions drawn from isolated CP shadows.

<1>13. Direct ordered collective parallel composition is coherent.

<2>1. For `K:[alpha]->[beta]underline(O)` and
`L:[alpha']->[beta']underline(P)`, put

    K boxtimes_c L
      =(iota(K_(o,i) tensor L_(p,j)))_((o,p),(i,j)).

It has type

    [alpha concat alpha']->[beta concat beta']underline(O times P).

<2>2. Normalization follows from the star-homomorphism property and gives
the source unit `e_(alpha concat alpha')`.

<2>3. Associativity follows from three-block inclusion coherence after the
explicit Cartesian history associator of D1218.

<2>4. For composable pairs `K,K'` and `L,L'`, multiplicativity of `iota`
gives the branch operator equality.  The arrow equality uses D1218's
specified history bijection between
`((o,p),(o',p'))` and `((o,o'),(p,p'))`.

<2>5. The right-context construction is the special case of collective
parallel composition with the one-outcome identity instrument, followed by
D1218's singleton classical unitor.

<2>6. No formula swaps the two blocks; order is preserved for `q!=1`.

<1>14. Steps <1>7--<1>13 prove OPLIM-2. **QED**

## Proposition OPLIM-3 (assembly and split are typed process retractions)

**ASSUME** the corner inclusion and expectation of CLIM-2.

**PROVE** the collective atom has associative operational assembly, and is
not silently identified with the separated register.

<1>15. Define two arrows

    asm_(alpha,beta):[alpha][beta] -> [alpha concat beta],
    spl_(alpha,beta):[alpha concat beta] -> [alpha][beta].

<2>1. In Heisenberg orientation `asm` is realized by

    E_(alpha,beta):A_(alpha concat beta)->A_alpha tensor A_beta.

<2>2. The arrow `spl` is realized by

    j_(alpha,beta):A_alpha tensor A_beta->A_(alpha concat beta).

<2>3. CLIM-2 proves both maps UCP and normalized-trace preserving.

<1>16. The separated register is a retract of the collective atom:

    spl_(alpha,beta) o asm_(alpha,beta)=id_([alpha][beta]).

<2>1. The Heisenberg realization of the left side is `E o j`.

<2>2. Conditional expectation fixes its included subalgebra, so `Eo j=id`.

<2>3. In the other order, `asm o spl` realizes `j o E` on the collective
algebra.

<2>4. This is generally a proper coarse graining, so no inverse relation is
imposed.

<1>17. Collective assembly and split are associative.

<2>1. The two processes from `[alpha][beta][gamma]` to
`[alpha concat beta concat gamma]` realize the two three-block expectation
composites.

<2>2. They are equal by F1-HCK-TOWER restricted to the corners in CLIM-2.

<2>3. The two reverse split processes realize the two three-block inclusion
composites and are equal by the same theorem.

<2>4. Thus collective assembly is genuine and coherent even though its
comparison map is not an isomorphism.

<1>18. Product preparation has the expected collective density.

<2>1. Prepare densities `h` and `k` on the separated word, then apply `asm`.

<2>2. The resulting functional on `A_(alpha concat beta)` is
`(omega_h tensor omega_k)o E_(alpha,beta)`.

<2>3. Trace pairing from F1-HCK-TOWER identifies its density as
`j_(alpha,beta)(h tensor k)`.

<2>4. Product trace preservation makes that density normalized and positive.

<1>19. A contextual preparation to the right is the typed circuit

    [gamma] --prep_h tensor id--> [alpha][gamma]
            --asm_(alpha,gamma)--> [alpha concat gamma].

<2>1. Its Heisenberg map is
`(omega_h tensor id)o E_(alpha,gamma)`.

<2>2. A contextual discard is `spl_(alpha,gamma)` followed by
`disc_alpha tensor id`; its map is
`a |->j_(alpha,gamma)(e_alpha tensor a)`.

<2>3. These are UCP maps between different ranks and use no nonexistent
degree-changing morphism of `Gamma_q`.

<1>20. Steps <1>15--<1>19 prove OPLIM-3. **QED**

## Theorem OPLIM-4 (the presented circuit category and realization)

**ASSUME** the generators above.

**PROVE** D1210--D1211 define operational categories, continuous and germ
versions, and evaluation functors with honest equality.

<1>21. Define `Op_q` to be the strict ordered monoidal category presented by
the register objects and the following generator boxes:

    all preparations and discards of <1>7;
    all POVMs of <1>8;
    all corner Kraus instruments of <1>9;
    every retained collective context/parallel list of <1>12--<1>13;
    all asm and spl boxes of <1>15;
    all classical product, unit, relabeling, and routing boxes of D1218.

<2>1. A raw morphism is a finite typed planar circuit built by vertical
composition and horizontal ordered juxtaposition.

<2>2. Equality is the equivalence relation generated by typed planar graph
isomorphism, the strict category and monoidal axioms, equality of state/POVM
labels, fibre coefficient-Gram equality, the typed routed instrument and
history identities of D1218, retained-context identities <1>12--<1>13, and
the assembly relations <1>16--<1>17.

<2>3. This is an explicit generated equivalence relation; it is not defined
by hoped-for equality of UCP shadows.

<2>4. Every listed relation is closed under inserting the two sides into a
larger typed circuit, so it is a congruence.

<2>5. Quotienting the free strict monoidal category by this congruence gives
an honest category with identity, associative composition, ordered tensor,
and interchange.

<1>22. The assignments in OPLIM-2--3 define a strict monoidal operational
realization

    Real_q:Op_q -> HCPU_fd.

<2>1. Each generator has a UCP map with exactly the contravariant source and
target algebras proved above.

<2>2. Gram equality, routed list composition, collective parallel coherence,
classical history relabeling, and the assembly relations were each verified
as equality of those maps in OPLIM-2--3 and `classical-wiring.md`.

<2>3. Hence the universal property of a presented category gives a unique
functor on the quotient.

<2>4. `Real_q` may be nonfaithful: circuits are not identified merely
because their isolated UCP maps happen to agree.

<1>23. For an interval `I`, define `Op_I^cts` by the same presentation with
continuous positive normalized state/POVM sections and continuous normalized
corner Kraus sections as labels.

<2>1. Two continuous Kraus labels are equal when their coefficient Grams are
equal at every `q in I`.  Fibre Gram equality is a congruence pointwise by
<1>11 and D1218; no continuous environmental unitary is selected.

<2>2. Assembly, split, preparation, discard, retained embedding, and
classical wiring formulas are pointwise continuous by CLIM-1--2.  All
generator realization matrices therefore depend continuously on `q`.

<2>3. Evaluation of every label and every circuit gives a strict ordered
monoidal functor

    Ev_q:Op_I^cts -> Op_q.

<1>24. Restriction to smaller endpoint intervals gives functors, so taking
germs of labels and finite circuits defines `Op_1^germ`.

<2>1. Two circuit germs are equal only when representatives become equal by
the explicit presentation relations on some common smaller interval.  For
Kraus labels this means eventual pointwise coefficient-Gram equality, not a
continuous family of mixing unitaries.

<2>2. Endpoint evaluation gives `Ev_1:Op_1^germ->Op_1`.

<2>3. The corresponding realization is evaluation of continuous UCP matrix
families, not D1144's fixed-fibre apartment compression.

<1>25. Separately define `Kraus_n(1)` to be the set of normalized local lists
in `C[S_n]` modulo stable scalar-unitary mixing, with list composition and
direct disjoint collective assembly where typed.

<2>1. F1-OP-KCF proves that its defining equivalence is exactly equality of
the Kraus Gram and exactly equality of all retained finite-injection context
actions.

<2>2. D1125--D1126 prove that list composition and direct disjoint collective
assembly descend to this quotient.

<2>3. Sending a class to its correspondingly labelled generator gives a
well-defined process assignment into `Op_1`, because stable mixing is among
the presentation relations.

<2>4. No faithfulness of this assignment after adjoining all other circuit
generators and relations is asserted.  The exact all-context statement is
about `Kraus_n(1)` itself, while realization of the whole circuit category is
only a possibly nonfaithful functor.

<1>26. Steps <1>21--<1>25 prove OPLIM-4. **QED**

## Declared boundary

<1>27. `Op` contains all normalized states, all effects and finite POVMs on
every register, all preparations and discards, all normalized corner-Kraus
instruments, their retained collective extensions, and their finite circuits.

<2>1. It does not advertise arbitrary CP maps as retained local arrows when
they have no supplied corner-Kraus data.

<2>2. It does not identify the separated tensor algebra with the larger
collective corner algebra.

<2>3. It supplies no exchange at `q!=1`; every assembly and context order is
the displayed left-to-right order. **QED**
