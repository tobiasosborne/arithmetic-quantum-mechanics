# Finite protocols, Born continuity, and the three-constituent witness

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

## Theorem PLIM-1 (finite protocol and conditioning continuity)

**ASSUME** a compact positive interval `I`, the continuous operational
category `Op_I^cts`, and the realization of OPLIM-4.

**PROVE** every finite instrument tree has continuous branch and event Born
weights; evaluation commutes with running the protocol; and conditioning is
continuous whenever the limiting event probability is positive.

<1>1. A finite protocol is the following typed data.

<2>1. It has a continuous normalized initial density on a finite register
word.

<2>2. Every internal vertex is labelled by a typed finite-outcome instrument
or circuit.  Following one outgoing edge selects its named classical outcome
and retains the quantum output declared by that instrument.

<2>3. The label at a later vertex may depend on the finite history of earlier
outcomes.

<2>4. Every leaf has a final effect, or equivalently a two-outcome POVM, on
the leaf register.

<2>5. A postselection event is a subset of the finite leaves.

<1>2. Every generator realization has continuous matrix entries in the fixed
regular bases.

<2>1. State and effect labels are continuous by definition.

<2>2. Corner-Kraus formulas are finite sums of products and adjoints of
continuous matrices.

<2>3. Their Schrödinger duals include only the continuous positive scalar
`P_alpha/P_beta` proved in OPLIM-2.

<2>4. Assembly and split are coefficient inclusion and deletion between
continuous corner sections by CLIM-2.

<2>5. Preparation, discard, retained context extension, and ordered parallel
extension are composites of these operations.

<1>3. Finite circuit realization is continuous.

<2>1. Vertical composition is matrix multiplication of the corresponding
finite-dimensional linear maps.

<2>2. Ordered horizontal juxtaposition is their Kronecker product.

<2>3. Matrix multiplication and Kronecker product have polynomial coordinate
formulas.

<2>4. Induction on the finite number of boxes therefore proves continuity of
every circuit matrix.

<1>4. The unnormalized density of every branch is continuous.

<2>1. At the root this is the assumed initial density.

<2>2. If a history density is continuous, applying one outcome CP map uses a
continuous circuit matrix and gives another continuous positive section.

<2>3. Induction on tree depth proves the assertion at all vertices and
leaves.

<1>5. Every leaf Born weight is continuous and nonnegative.

<2>1. It is the normalized trace pairing of the unnormalized leaf density
with the continuous leaf effect.

<2>2. In fixed coordinates this is a finite sum of products of continuous
coefficients and the continuous trace weights.

<2>3. Positivity of the density and effect makes the scalar nonnegative.

<1>6. The total weights have the expected probability bounds.

<2>1. At an instrument vertex, the sum of the branch CP maps is trace
preserving because the total Heisenberg map is unital.

<2>2. Therefore the sum of child masses equals the parent mass.

<2>3. Starting from mass one, the sum of all terminal branch masses is one
when every terminal effect is the unit, and is at most one for general
effects.

<1>7. Evaluation commutes with the protocol.

<2>1. `Ev_q` evaluates every generator label and preserves composition and
ordered tensor by OPLIM-4.

<2>2. Evaluation also commutes with the finite sums defining outcome and
event weights.

<2>3. Hence evaluating the continuous Born expression at `q` gives exactly
the result of running the evaluated fibre protocol.

<1>8. Let `N(q)` be the sum of weights of selected successful leaves and
`D(q)` the probability of a postselection event containing them.

<2>1. Both are continuous finite sums by <1>5.

<2>2. Suppose `D(1)>0`.

<2>3. Continuity gives an endpoint neighborhood on which
`D(q)>D(1)/2>0`.

<2>4. The conditioned probability `N(q)/D(q)` is continuous there and

    lim_(q->1) N(q)/D(q)=N(1)/D(1).

<2>5. Without `D(1)>0`, division need not be defined or continuous, so no
postselection claim is made.

<1>9. The proof is unchanged for a germ protocol: choose one common
representative interval for its finitely many labels.

<2>1. Such an interval exists by the definition of germ equality and finite
intersection.

<2>2. Only endpoint evaluation is canonical on the germ; other fibre values
refer to this chosen representative.

<1>10. Steps <1>1--<1>9 prove PLIM-1. **QED**

## Theorem PLIM-2 (three constituents, refinement, and retained context)

**ASSUME** `q>0`, put `d=1+q+q^2`, and work in the level-three Hecke algebra
of F1-HCK-LOW.

**PROVE** the protocol of D1217 is normalized, has strictly positive
postselection, detects retained context, and specializes continuously to
joint probability `1/6` at one.

<1>11. Put

    e_1=(T_1+1)/(q+1),       e_2=(T_2+1)/(q+1),
    alpha=(1,2),             x^3=(1,1,1).

<2>1. The source corner unit is `e_alpha=e_2`, and
`P_alpha(q)=1+q`.

<2>2. Its normalized corner trace is
`tau_alpha=(q+1)tau_3` by D1141.

<2>3. Since `tau_3(e_2)=1/(q+1)`, the element `rho_alpha=e_2` is a positive
normalized source density.

<1>12. The canonical refinement isometry from `alpha` to the complete flag
object is `v=e_2`.

<2>1. In the corner convention it belongs to
`e_(x^3)H_3e_alpha=H_3e_2`.

<2>2. It satisfies `v^*v=e_2`, the source identity.

<2>3. OPLIM-2's normalized density transport sends `rho_alpha` to

    h(q)=(P_alpha/P_(x^3))v rho_alpha v^*=(q+1)e_2.

<2>4. Its coefficient trace is one, as required.

<1>13. Let `z_std(q)` be the central support of the unique `M_2` summand from
F1-HCK-LOW, and put

    P_2(q)=z_std(q)e_2(q).

<2>1. In the displayed standard representation of F1-HCK-LOW, `P_2` is a
rank-one projection.

<2>2. The one-dimensional trivial and sign central projections are the
continuous parabolic symmetrizer and antisymmetrizer sections.

<2>3. Their complement `z_std` is therefore continuous, so `P_2` is a
continuous projection effect.

<2>4. F1-HCK-LOW gives the coefficient-trace weight of the standard block as

    gamma(q)=q/d,

so `tau_3(P_2)=gamma(q)`.

<1>14. Apply the two-outcome Lüders instrument after refinement,

    K_s=P_2,                  K_f=1-P_2,
    [x^3]->[x^3]underline({s,f}).

<2>1. The Kraus effects are `K_s^*K_s=P_2` and
`K_f^*K_f=1-P_2`, so this instrument has the POVM `(P_2,1-P_2)` and retains
the full quantum output in either branch.

<2>2. Its success probability is

    s(q)=tau_3(h(q)P_2(q))
        =(q+1)q/(1+q+q^2).

<2>3. This is strictly positive for every `q>0`.

<2>4. The successful Schrödinger branch is determined by the stated Kraus
operator:

    K_s h K_s^*=P_2((q+1)e_2)P_2=(q+1)P_2.

<2>5. Dividing by `s(q)` gives the normalized full-algebra density

    h_s(q)=P_2(q)/gamma(q)=((1+q+q^2)/q)P_2(q).

<2>6. At `q=1`, `s(1)=2/3` and `h_s(1)=3P_2(1)`.  A POVM with the same
effects but different successful Kraus operator need not produce this state;
the Lüders label is load-bearing.

<1>15. Put `u_1=2e_1-1` in the first two-constituent Hecke algebra and use
its direct retained right context extension to the third constituent.

<2>1. `u_1` is a self-adjoint unitary because `e_1` is a projection.

<2>2. The isolated algebra `H_2(q)=C[e_1]` is commutative, so
`Ad_(u_1)` is its identity channel.

<2>3. The retained extension is conjugation by the same embedded `u_1` on
the full collective algebra `H_3(q)`.

<2>4. It is not replaced by the identity label in `Op_q`, because their
one-element coefficient Grams differ.

<1>16. On the successful branch, measure the two-outcome POVM
`(P_2,1-P_2)` again after this retained process.

<2>1. F1-HCK-LOW gives the rank-one overlap

    a(q)=q/(q+1)^2.

<2>2. In the standard block `u_1=2P_1-1`, so the conditional return
probability is

    r(q)=tau_3(h_s u_1P_2u_1)
        =(1-2a(q))^2.

<2>3. This differs from the return probability one of the identity retained
process whenever `q>0`.

<2>4. At one, `a(1)=1/4` and `r(1)=1/4`.

<1>17. The full joint success-and-return probability is

    p(q)=s(q)r(q)
        =q(q+1)/(1+q+q^2)
           (1-2q/(q+1)^2)^2.

<2>1. Every denominator is positive on `(0,infinity)`, so `p` is continuous.

<2>2. Substitution gives `p(1)=(2/3)(1/4)=1/6`.

<2>3. PLIM-1 identifies this substitution with endpoint evaluation of the
typed instrument tree: refinement, successful Lüders branch, retained
context process, and final measurement.

<1>18. The example uses all three structural layers.

<2>1. `e_2:alpha->x^3` is a typed corner refinement.

<2>2. The first measurement is the specified Lüders instrument, and its
successful quantum output has the correctly normalized full coefficient-trace
density, including the factor `1/gamma` after conditioning.

<2>3. `u_1` is retained before extension to the collective third-constituent
context, so an isolated-channel quotient cannot erase it.

<2>4. The postselection event stays positive at the endpoint, satisfying the
hypothesis of PLIM-1.

<1>19. Steps <1>11--<1>18 prove PLIM-2. **QED**

## Proposition PLIM-3 (the positive postselection hypothesis is necessary)

**ASSUME** the complete level-three corner on the one-sided interval
`1<=q<=3/2`, and the continuous normalized density
`rho(q)=P_2(q)/gamma(q)` from PLIM-2.

**PROVE** there is a continuous two-outcome instrument whose success
probability tends to zero while its conditional return probability has no
limit.

<1>20. For `q>1`, put

    t(q)=q-1,
    theta(q)=(pi/2)(1+sin(1/(q-1))),
    r_1(q)=1-e_1(q),
    U(q)=e_1(q)+exp(i theta(q))r_1(q).

<2>1. `e_1,r_1` are complementary projections, so `U(q)` is unitary.

<2>2. When `theta=0`, `U=1`; when `theta=pi`,
`U=e_1-r_1=2e_1-1=u_1`.

<1>21. Define Kraus labels for `q>1` by

    K_s(q)=t(q)U(q),
    K_f(q)=sqrt(1-t(q)^2)1,

and define `K_s(1)=0`, `K_f(1)=1`.

<2>1. Although `U(q)` has no endpoint limit, `||K_s(q)||=t(q)->0`, so
`K_s` is continuous at one.

<2>2. `K_f` is continuous on the whole interval.

<2>3. Exact normalization is

    K_s^*K_s+K_f^*K_f=(t^2+1-t^2)1=1.

<2>4. Thus these labels define a continuous instrument, including at the
endpoint.

<1>22. Its success probability is `D(q)=t(q)^2`.

<2>1. This follows from `K_s^*K_s=t^2 1` for every normalized input state.

<2>2. Hence `D(q)>0` for `q>1` but `D(1)=0`.

<2>3. Conditioned on success, the scalar factor cancels and the density is
`U(q)rho(q)U(q)^*`.

<1>23. The conditioned probability of the effect `P_2(q)` has no endpoint
limit.

<2>1. Along a sequence with `sin(1/(q-1))=-1`, `theta=0`, so the return
probability tends to `1`.

<2>2. Along a sequence with `sin(1/(q-1))=1`, `theta=pi`, so `U=u_1` and
PLIM-2 makes the return probability tend to `1/4`.

<2>3. Both kinds of sequence tend to one, for example by taking the
reciprocals of `3pi/2+2pi k` and `pi/2+2pi k` as `q-1`.

<2>4. Therefore the conditioned return has two distinct subsequential
limits.

<1>24. There is also a fully rational fixed-endpoint sample for an exact
checker.

<2>1. In `H_3(1)`, for `n>=1` put

    t_n=2n/(n^2+1),       c_n=(n^2-1)/(n^2+1),
    U_n=1 for even n,     U_n=u_1 for odd n.

<2>2. The rational identity

    t_n^2+c_n^2
      =(4n^2+(n^2-1)^2)/(n^2+1)^2=1

makes `(t_nU_n,c_n1)` a normalized instrument.

<2>3. Its success probability tends to zero, while the conditioned `P_2`
return alternates between `1` and `1/4`.

<2>4. This finite-support rational family is a falsifier for any theorem
that drops the positive limiting denominator; the continuous construction
<1>20--<1>23 is the actual topological counterexample.

<1>25. Steps <1>20--<1>24 prove PLIM-3. **QED**

## Executable finite falsifiers for the core claims

<1>26. The executable probes are the following actual checker gates.

<2>1. `theory/checks/f1_limit_check.py` supplies `L1` for finite Hecke base
change and ordered block multiplication; `L2`--`L5` for normalization,
instruments, corner trace ratio and the level-three protocol; `L6` for the
endpoint Gram-recovery context; `L11` for the zero-success conditioning
counterexample; and `L14` for the proper assembly retraction.

<2>2. `theory/checks/f1_operational_check.py` supplies `H1`--`H2` for the
finite Hecke product/trace form, `H3` for block expectations, `H5` for the
retained level-three witness, `H8` for normalized Kraus operations, `H9` for
the finite-field flag realization, `H11` for endpoint context separation, and
`H13` for parabolic corner traces, refinement and concatenation.

<2>3. `theory/checks/f1_limit_wiring_check.py` supplies `W1` for routed
sequential instruments, `W2` for parallel routing past a quantum output,
`W3` for the uniform classical-trace density factor, `W4` for deriving the
Lüders successful density from the Kraus data, and `W5` for associativity,
interchange and singleton history bijections.

<2>4. Every checker exposes named red data mutations.  The continuous
closedness, local functional-calculus normalization, germ equality and general
Born-continuity conclusions rest on the written proofs; no finite gate is
claimed to prove those quantifiers.

<1>27. Each probe is binding only in the negative: a discrepancy blocks the
corresponding claim, while a green finite sample does not prove its uniform
quantifier. **QED**

## Endpoint interpretation boundary

<1>28. The endpoint is the evaluated symmetric-group/corner operational
category with its reviewed contextual local-process quotient.

<2>1. Arithmetic fibres occur at the parameter values `Q=p^r` and have the
partial-flag realization of D1141.

<2>2. The continuous path to one is in real parameter space; no sequence of
prime powers tends to one.

<2>3. The category retains the chosen type-A flag context and does not claim
to specialize the full Weyl system, every phase, or every polarization.

<2>4. D1144's apartment channel remains a useful fixed-fibre UCP comparison,
but it is not the evaluation functor and fails the required multiplicativity
for `Q>1`.

<2>5. These limitations are part of the proposed claim statements. **QED**
