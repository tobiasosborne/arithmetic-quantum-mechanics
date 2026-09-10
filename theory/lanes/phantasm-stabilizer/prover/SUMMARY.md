# SP-STAB-REL prover summary

Lane model: `gpt-5.6-sol`, reasoning `xhigh`.

The prover pass constructs the canonical equivalence from the D1715
intertwiner space rather than importing a dagger claim from SP-CK21 or
SP-BC24.  SP-LREL and SP-COMPACT remain explicit `SKETCH` dependencies.

For a nonempty affine relation `R=r+L`, the operator-space Weyl action is

    rho(v,w)T=W_n(w) T W_m(v)^*.

Its multiplier is the half-form for `-omega_m+omega_n`.  On the Lagrangian
direction `L` it becomes an ordinary unitary representation.  The character
projector onto D1715's equations has trace

    dim Hom(H_m,H_n)/|L|=p^(m+n)/p^(m+n)=1.

Thus every nonempty relation gives one nonzero projective operator line; the
all-origin equations agree because changing an origin by `L` contributes a
zero symplectic pairing.  The projective Weyl stabilizer of a line is
isotropic and contains `L`, so maximality recovers `L`; its eigencharacter
then recovers the affine coset.  This proves injectivity independently of the
source presentation.

Composition uses exact support projectors.  The output support of a line for
`R` and input support of a line for `S` overlap precisely when the two affine
middle projections meet.  The Hilbert--Schmidt norm of their projector
product is the finite character sum over the intersection of the two
isotropic stabilizer groups.  It is positive exactly when the affine
characters agree there.  Consequently products are nonzero exactly for
nonempty relational composites; when nonempty, the two middle symplectic
terms cancel and the product spans the composite line.  This covers two
nonempty relations whose composite is empty.

Taking adjoints in the defining equation gives the line of D1702's bare
converse directly.  Tensoring equations and using admitted SP-TENSOR gives
the grouped direct-sum comparison, including zero objects and empty arrows.
The proof never uses SP-BC24's time-reversed dagger.

For target membership, the symplectic map
`c_m(a,b)=(a,-b):bar(V_m)->V_m` and ordinary vectorization turn an operator
line into an affine Lagrangian stabilizer-state line.  A symplectic-basis
construction and SP-EGOROV prepare every such state from
`delta_0^(tensor n)` using a D1307 second-level unitary.  Contracting with
the stabilizer Bell effect unvectorizes it inside D1704.

Fullness checks every `U in C_2(A)`.  Unique Weyl labels in
`U W(v)U^*=gamma(v)W(gv)` and the product/commutator laws force `g` to be
linear symplectic and `gamma(v)=psi_(F_p)(omega(t,gv))`.  Hence `U` spans
the affine graph line.  Together with preparation, adjoint, and scalar
generators, this gives every D1705 arrow class.  Recovery gives faithfulness,
and the object assignment is surjective.

Artifacts:

- `PROPOSAL.md`: canonical D1715 and exact constructive claim/DAG text;
- `intertwiner-line.md`: Lamport origin, rank-one projector, and recovery
  proof;
- `functor-laws.md`: Lamport support, composition, dagger, and tensor proof;
- `equivalence.md`: Lamport vectorization, all-C2 fullness, faithfulness, and
  source-convention proof;
- `SOURCE-LOCATORS.md`: exact source scope and locator record;
- `LABBOOK-FRAGMENTS.tex`: exact D1715 restatement and concise proof prose;
- `PATCH.md`: string-anchored integration plan.

The mathematical shards are each 200--500 lines and record the actual model
and reasoning setting.  No checker result is offered as proof; the independent
quantum checker lane owns finite expectations.  No trunk edit, status
promotion, Git action, representative normalization, probability claim, CP
claim, or compact-preservation claim was made.
