<!-- ROLE: pre-registration for the independent SP-LREL and compact-data
     falsifier. Written before this lane's checker existed. This lane did not
     read any prover-lane artifact. -->

# EXPECTATIONS — affine Lagrangian relations and compact data

Date: 2026-09-10. Lane: `phantasm-relations/checker`.
Model: `gpt-5.6-sol`, reasoning setting `xhigh`.

This is a finite exact falsifier, not a proof and not promotion evidence.  It
will use prime-field arithmetic only, with no floating-point mathematics.
The mathematical claim SP-LREL ranges over every finite field and every
finite-dimensional symplectic space; the exhaustive scopes below are only the
zero object and one standard symplectic register over `F2` and `F3`.  In
particular, the odd-characteristic source-sign control says nothing about an
odd-only restriction on SP-LREL: characteristic two remains in scope.

The compact datum is a separate proposed follow-up, not part of the current
SP-LREL statement.  Its convention in this pre-registration is exactly

    compact dual of V = bar(V),
    eta_V: 0 -> bar(V) + V,       eta_V = {(v,v): v in V},
    epsilon_V: V + bar(V) -> 0,  epsilon_V = {(v,v): v in V}.

Here `bar(V)=(V,-omega_V)`, `+` is ordered symplectic direct sum, and relation
coordinates always list all source coordinates before all target coordinates.
This agrees with the convention supplied to this lane.  If the independent
definition lane chooses another factor order, the mismatch must be resolved
before either artifact is integrated.

## Independently derived finite expectations

Let `P_q` be the standard symplectic plane over `F_q`, with
`omega((x,y),(x',y'))=x*y'-x'*y`, and let `0` be the zero space.  A
Lagrangian in a `2n`-dimensional symplectic space has dimension `n`.  The
number of linear Lagrangians is `product_(i=1)^n (q^i+1)`, and each has
`q^n` affine cosets.  Therefore the arrow counts, including one separately
retained empty relation in every Hom-set, are

| field | `Hom(0,0)` | `Hom(0,P_q)` | `Hom(P_q,0)` | `Hom(P_q,P_q)` |
|---|---:|---:|---:|---:|
| `F2` | 2 | `2(2+1)+1 = 7` | 7 | `2^2(2+1)(2^2+1)+1 = 61` |
| `F3` | 2 | `3(3+1)+1 = 13` | 13 | `3^2(3+1)(3^2+1)+1 = 361` |

Every nonempty relation in these four Hom-sets has respectively
`1,q,q,q^2` points.  The checker will enumerate all subspaces independently
by reduced row bases, test the fixed `-omega_source + omega_target` form,
and deduplicate actual affine cosets as point sets.  The diagonal identity
must occur in `Hom(P_q,P_q)`.  With the wrong `+omega_source + omega_target`
form the diagonal is still accidentally isotropic in characteristic two but
is not isotropic over `F3`; this is the required odd-characteristic sign
witness.

Relational composition and its oracle must be different computations.
The production route joins sparse point sets on a middle coordinate and
projects existentially.  The oracle converts the two affine spaces to linear
equations, solves their combined system by exact row reduction, projects the
solution basis, and reconstructs the expected affine point set.  It also
checks that a nonempty output has dimension `(dim(source)+dim(target))/2`.
No expected output is made by calling the relational composition routine.

The number of composable ordered pairs across the two objects is

    (h00+h0P)^2 + (hP0+hPP)^2,

namely 4,705 over `F2` and 140,101 over `F3`.  G2 checks every one of them.
Two registered witnesses are the horizontal Lagrangian line `L={(x,0)}` as
a state and the same line as an effect, whose closed composite is true with
`q` middle witnesses (a nontransverse composite), and the parallel affine
lines `{(x,0)}` and `{(x,1)}`, whose closed composite is empty.

For associativity, G3 is exhaustive over all 290,794 typed composable triples
on `{0,P_2}`.  Over `F3`, it uses 256 deterministic index-mixed triples for
each of the 16 object chains, 4,096 typed triples total.  Identity and dagger
checks remain exhaustive over every enumerated arrow in both fields, and
dagger reverses every one of the 4,705 and 140,101 composition cases.

For tensor, native Cartesian-product coordinates
`(source,target,source',target')` must be reordered to
`(source,source',target,target')`.  G4 checks every ordered pair of the 77
small arrows over `F2` (5,929 pairs) and 256 deterministic pairs for each of
the 16 Hom-type pairs over `F3` (4,096 pairs).  It checks the resulting affine
dimension and isotropy without using the tensor constructor, plus empty
absorption and both tensor-unit laws.  Selected typed quadruples check the
interchange law; associator and swap graphs check ordered-factor coherence.
The monoidal unit is the actual zero symplectic space.

The affine symplectic group of the plane has `q^2*q*(q^2-1)` arrows: 24 over
`F2` and 216 over `F3`.  G5 enumerates these independently, checks every graph
is a catalogued Lagrangian relation, checks graph equality is faithful, and
checks identities, inverses/daggers and all 576 (`F2`) and 46,656 (`F3`)
ordered compositions.  Tensor preservation is exhaustive over `F2` affine
arrow pairs and uses 4,096 deterministic `F3` pairs.

For the compact datum, direct form and cardinality checks give `q^2` points
in each cup and cap.  The two typed snakes are

    (epsilon_V + id_V) o (id_V + eta_V) = id_V,
    (id_barV + epsilon_V) o (eta_V + id_barV) = id_barV.

Dagger/factor compatibility is

    eta_V^dagger = epsilon_V o swap_(barV,V) = epsilon_barV,
    epsilon_V^dagger = eta_barV.

These equations are checked for `V=P_q` and for `V=0`, over both fields.
For every enumerated `R:V->W`, with `V,W` in `{0,P_q}`, its name is computed
diagrammatically as `(id_barV + R) o eta_V` and must be the same underlying
relation, now typed as a state `0->barV+W`.  Unnaming by
`(epsilon_V+id_W) o (id_V+state)` returns `R`.  Thus empty names remain empty.
The scalar Hom-set `Hom(0,0)` is exactly `{false,true}`: the empty and singleton
relations.  Its composition and tensor are Boolean conjunction, its unit is
true, and the closed cup/cap loop `epsilon_barV o eta_V` is true, including at
the zero object.

The horizontal state used by G2 has `q>1` outputs from the unique point of the
zero object, so it is also the explicit nonfunctional-relation witness.  For
the symmetric monoidal dagger compatibility, G4 must additionally check on
its full finite tensor sample that `(R+S)^dagger=R^dagger+S^dagger`.  On all
object pairs and triples from `{0,P_q}`, it must check swap involutivity and
the strict hexagon

    swap_(A,B+C)
      = (id_B + swap_(A,C)) o (swap_(A,B) + id_C).

These are direct relation equalities, while strict tensor associativity is
checked on relation samples.  They make the advertised coherence and dagger
scope explicit rather than leaving those words to a generic affine check.

The checker stores direct sums as flattened ordered tuples.  In that model
D1714's associator and left/right unitor graphs have the same point data as
the corresponding flattened identity, but they remain separately constructed
typed relations.  G6 composes those graph relations in both displayed snake
equations, G7 uses them in the registered unname formula, scalar tensor is
computed as `lambda_0 o (s+t) o lambda_0^{-1}`, and the loop is computed as
`epsilon_V o swap_(barV,V) o eta_V`.  Thus flattening is a coordinate model of
the registered coherence arrows, not a deletion of them.

## Green gates

| gate | scope |
|---|---|
| `G1` | Exact `F2`/`F3` Hom-set census, cardinalities, canonical-form membership, zero object, states/effects and explicit empty arrows |
| `G2` | Every small composable pair; existential sparse composition versus the independent affine-equation/dimension oracle; nontransverse and empty witnesses |
| `G3` | Exhaustive identities and converse dagger in both fields; exhaustive `F2` and 4,096-case `F3` associativity |
| `G4` | Direct-sum tensor, coordinate order, zero unit, symmetry/associativity coherence and selected interchange |
| `G5` | Faithful affine-symplectic graph embedding, composition, dagger and tensor preservation |
| `G6` | Opposite-form dual, typed diagonal cups/caps, dagger order and both snakes for `0,P_2,P_3` |
| `G7` | Exhaustive name/unname equality on the small catalogs; two unit scalars and true closed loop |

## Pre-registered mutation map

Each mutation changes actual enumerated relation, composition, dagger,
tensor, graph, cup or unit data.  No mode merely changes a synthetic expected
variable.  A red invocation runs its named gate economically and must fail
there.

| mode | actual mutation | intended gate |
|---|---|---|
| `--red-source-sign` | enumerate `P_3->P_3` Lagrangians using `+omega_source+omega_target` | `G1` |
| `--red-empty-loss` | omit the explicit empty relation from each actual catalog | `G1` |
| `--red-middle-forall` | replace the existential middle-point join by a universal join | `G2` |
| `--red-dagger-order` | take converse without swapping source and target coordinate blocks | `G3` |
| `--red-tensor-order` | retain native Cartesian-product coordinate order instead of source/source/target/target | `G4` |
| `--red-zero-unit` | use the standard plane as the actual tensor unit | `G4` |
| `--red-graph-translation` | omit the affine translation in actual graph point data | `G5` |
| `--red-cup-order` | type the actual cup as `0->V+bar(V)` instead of `0->bar(V)+V` | `G6` |
| `--red-name-order` | swap the dual-input and output blocks in the actual named state | `G7` |
| `--red-compact-dual` | replace `bar(V)` by `V` in the actual cup and cap data | `G6` |
| `--red-loop-multiplicity` | return a middle-witness count from the actual closed-loop evaluator instead of its Boolean relation | `G7` |
| `--red-empty-name` | send the actual empty `0->0` relation to the nonempty named scalar | `G7` |

Expected process exits are: green `0`; a caught advertised red `1`; a red
whose mutation survives `0`, so the repository session-close runner rejects
it; invalid usage or failure at a gate other than the registered target `2`.
The first executions after implementation must be every advertised red,
before the first green.  `RUNS.md` must retain their specific failure paths
and one later temporary control in which an acceptance comparison is disabled
and its now-surviving red is observed to exit zero.

## Runtime and interpretation

The large green work is the 140,101 exact `F3` composition/oracle comparisons
and 46,656 graph-composition comparisons.  Composition tables and point-index
slices should be cached; rank-two catalogs are never exhaustively generated.
Red modes execute only their target gate.  A green result can refute a faulty
finite formula, but cannot prove closure, coherence, compactness or the
arbitrary-field statements.

## One checker repair wave — pre-registration after blind review

The blind verdict's OBJ-3--OBJ-5 are accepted for the checker.  The following
repair expectations were written before changing the frozen executable.

1. Help will advertise only concrete `--red-<name>` flags.  Bare `--red` will
   be unsupported usage and exit `2`, so the repository runner cannot count a
   missing argument as a killed mathematical mutation.
2. G6 will order and label its checks so the existing actual-data mutations
   have distinct paths.  `compact-dual` changes both cup/cap dual objects to
   `V` and must first fail `G6a dual-isotropy` over F3.  `cup-order` retains
   `bar(V)` but reverses eta's factors; its diagonal remains Lagrangian and it
   must first fail `G6b cup-factor-order` over F3.
3. New `dagger-swap` literally omits `sigma_(bar(V),V)` from the actual
   dagger diagram, leaving `epsilon_V` with domain `V+bar(V)` where
   `eta_V^dagger` has domain `bar(V)+V`.  Cup/cap typing and order remain
   canonical, and the first failure must be `G6c dagger-swap`.
4. New `snake-wire` replaces only the first snake's cap by the same-typed
   empty relation.  It must pass cup/cap typing, factor order and dagger
   compatibility before failing `G6d first-snake`; the second snake continues
   to use canonical data.
5. `tensor_expected` will be replaced by an independent Boolean-relation
   matrix route.  It indexes target points as rows and source points as
   columns, takes the Boolean Kronecker product, then decodes true matrix
   entries in the ordered direct-sum bases.  This route shares no point-set
   regrouping comprehension with `tensor`.  `tensor-order` will mutate every
   actual tensor in the registered sample and first fail the named
   `G4a Boolean-Kronecker coordinate oracle`, rather than a special duplicate
   probe.

The two new advertised rows are therefore:

| mode | actual mutation | intended first subcheck |
|---|---|---|
| `--red-dagger-swap` | omit the compact dagger equation's swap graph, exposing the reversed cap domain | `G6c dagger-swap` |
| `--red-snake-wire` | replace only the first snake's cap by a same-typed empty relation | `G6d first-snake` |

The changed `compact-dual`, `cup-order`, and `tensor-order` modes and both new
modes must be observed red before the repaired green.  As the independent
survival control, temporarily disabling only `G6c` must make
`dagger-swap` exit `0`; restoring it must return exit `1` at G6c.  Bad usage
and any wrong-gate/exception path remain exit `2`.

The first attempted same-typed no-block-swap graph survived because every cup
point is diagonal and block swap fixes the diagonal pointwise.  That observed
exit `0` is a useful negative control, but it is not the canonical
drop-the-swap mutation.  The literal omission above is the repaired mutation
and must be observed red before green.
