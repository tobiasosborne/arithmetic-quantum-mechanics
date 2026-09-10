# SP-SUM — coherent lists, tagged blocks, and dephasing

Date: 2026-09-10. Planning model: `gpt-5.6-sol`, reasoning `xhigh`.

This is the next bounded local-interface task after the current process cluster.
It does not read or depend on any process prover/checker lane artifact. Begin
proof work only after canonical SP-CP is admitted, because SP-SUM currently
lists it as a dependency. Keep SP-SUM at `SKETCH` through planning and proving.

## Exact target

Prove only the canonical SP-SUM row:

1. For every odd prime `p` and all `m,n>=0`, the complex span inside actual
   linear maps of
   `Stab_p^amp(H_(F_p,n),H_(F_p,m))` is the full rectangular Hom-space.
2. D1707's matrix completion realizes all linear maps between the finite
   coherent Hilbert sums, including the empty-list zero object.
3. For a nonempty ordered list `(H_i)`, with `d_i=dim H_i`, the coherent
   algebra has dimension `(sum_i d_i)^2`; the tagged block-diagonal algebra
   has dimension `sum_i d_i^2`.
4. The block-dephasing map associated with the chosen ordered decomposition is
   an ordinary-trace-preserving channel onto the tagged subalgebra.

Do not enlarge this to a biproduct theorem, semisimplicity, a fusion category,
a rig source, distributivity, Gaussian closure, or arithmetic-source
exhaustion. Do not say coherent sums remain pure stabilizer maps: D1707 adds
complex linear combinations deliberately.

## Reuse ledger

- D1003 supplies the computational Schrödinger basis and Weyl translations.
- D1704 supplies actual `C_2` unitaries, `delta_0`, adjoints, tensor,
  composition and every actual complex scalar. Equality is equality of maps.
- F1-REAL already proves that Weyl operators span the full square
  endomorphism algebra of each finite configuration space. Reuse this result;
  do not reprove finite Stone--von Neumann.
- The admitted SP-STAB-REL equivalence may be used as a consistency check, but
  it is unnecessary for the rectangular matrix-unit construction and its
  `C^times` quotient is not where coherent addition is defined.
- D1706 supplies the ordinary-trace Kraus/channel criterion once SP-CP is
  admitted. Its systems are finite **nonempty** families of nonzero Hilbert
  spaces, so it does not create a channel on D1707's empty list.
- D1707 owns the ordered list, complex span, matrix completion, coherent
  Hilbert sum and separate tagged block algebra.
- SP-WAT18 §2.2, equation (2.162), printed pp.94--95, gives the completely
  dephasing channel and its “delete off-diagonal entries” action. The present
  block version is a direct finite Kraus calculation with block projections,
  not a quotation of a stronger source theorem.

## Proof cluster

### A. Rectangular matrix units

For `x in F_p^n`, tensor the one-register translations with `delta_0` to
construct the actual preparation

    e_x:C->H_n,  1 |-> delta_x.

For `y in F_p^m`, use `e_y`, and use D1704 adjoint closure for `e_x^*`.
Then

    E_(y,x)=e_y o e_x^*:H_n->H_m

is an actual stabilizer amplitude. These `p^(m+n)` maps are the computational
rectangular matrix units and form a complex basis of `Hom_C(H_n,H_m)`.
Include `m=0`, `n=0`, and `m=n=0` using the unique empty tuple and `H_0=C`.

State exactly where addition enters: individual `E_(y,x)` are actual D1704
maps; an arbitrary sum `sum c_(y,x)E_(y,x)` belongs to D1707's complex span.
It need not be a morphism of the uncompleted actual-amplitude category.

### B. Matrix completion and coherent realization

For ordered lists `X=(H_i)_(i=1)^r`, `Y=(K_j)_(j=1)^s`, expand a D1707 arrow
`T=(T_(ji))` in rectangular matrix units. Under the canonical block action

    (xi_i)_i |-> (sum_i T_(ji) xi_i)_j,

the matrix Hom-space maps bijectively to
`Hom_C(direct-sum_i H_i,direct-sum_j K_j)`. Prove compatibility with matrix
composition and adjoint transpose.

Handle the empty list explicitly: its Hilbert realization is `0`; every Hom
to or from it is the zero vector space with its unique empty block matrix, and
`End(0)` is the zero algebra. Do not apply D1706's nonempty-system channel
definition there.

Repeated equal Hilbert blocks remain separately tagged list positions. Never
merge them merely because their dimensions or underlying spaces agree.

### C. Coherent and tagged algebras

For nonempty `X`, put `H=direct-sum_i H_i`, `D=sum_i d_i`, and let `P_i` be
the orthogonal projection onto the recorded `i`-th summand. Then

    End(H)=direct-sum_(i,j) Hom(H_j,H_i),

so its dimension is `D^2`. The tagged algebra is exactly the diagonal block
sum `direct-sum_i End(H_i)`, dimension `sum_i d_i^2`. Exhibit one off-diagonal
matrix unit when the list has at least two entries to prove the inclusion can
be proper.

### D. Ordinary-trace block dephasing

Use the explicit map

    Delta_X(A)=sum_i P_i A P_i.

Check from the block matrix entries that it fixes diagonal blocks and kills
all off-diagonal blocks. Its Kraus list is `(P_i)_i` and
`sum_i P_i^*P_i=1_H`, so D1706/SP-CP makes it a channel. Independently compute

    Tr(Delta_X(A))=sum_i Tr(P_i A P_i)=Tr(A)

with the ordinary matrix trace. Also verify `Delta_X^2=Delta_X`, its range is
the tagged algebra, and it is unital. Only trace preservation and the channel
statement belong to the canonical claim; idempotence/range are supporting
leaves, not a new conditional-expectation claim.

## Definition-ownership gate before proof integration

D1707 names object realization but does not explicitly prescribe the block
action of an arrow matrix on the coherent direct sum. It also refers to the
“corresponding” dephasing in SP-SUM without owning `Delta_X`, the projections
`P_i`, or the displayed formula. Before integrating a proof, the coordinator
must decide whether to add these two formulas to D1707/notation or to expand
the canonical claim so the maps are explicitly quantified there. Do not hide
either choice as proof-local notation while claiming a canonical realization.

No further definition is needed for the tagged algebra itself, the empty
list, or ordinary trace.

## Exact falsifier lane

Write `EXPECTATIONS.md` before the checker. Use exact integer/rational matrix
arithmetic; no tolerance is needed.

Required green controls:

- construct all `p^(m+n)` matrix-unit words for `p=3` and
  `(m,n)` in `{0,1,2}^2`, and verify their entry patterns and linear rank;
- compare D1707 block matrices with direct-sum linear maps, including empty
  source/target and repeated equal blocks;
- for `X=(C,C^3)`, verify coherent dimension `16`, tagged dimension `10`,
  six off-diagonal matrix units, and one explicit coherent cross-block map;
- verify `Delta_X` on every `4x4` matrix unit, Kraus completeness, ordinary
  trace preservation, unitality, idempotence and exact tagged range;
- add a second unequal/repeated-block case so the test does not fit only the
  `(1,3)` dimensions.

Required mutation families:

- delete a preparation/adjoint needed for one rectangular matrix unit;
- use the existing exact qutrit stabilizer census to misclassify the
  specific two-unit sum diag(1,1,0) as an actual stabilizer map;
- replace the coherent algebra by the tagged algebra;
- merge two repeated list positions;
- realize the empty list as `C`;
- retain an off-diagonal block during dephasing;
- omit one block projection or divide the channel by the number of blocks;
- substitute dimension-normalized block traces for D1706's ordinary trace.

Each caught red must exit 1 at its named first gate; a survivor exits 0,
and usage/unexpected errors exit 2. Mutate actual data, not expected counts.
A temporary disabled-comparison control must make the associated red survive;
restore the source afterward.

## Proof/review/landing discipline

Use one prover pass, one blind hostile pass, one repair wave, then mechanical
adjudication. Use one bounded shard `sum.md` for these linked matrix arguments; split
only if the 500-line cap requires it, and reuse the admitted foundations
without padding the proof. Keep the labbook statement and definition ownership
in lockstep. Passing finite examples does not prove arbitrary ranks/lists.

Completing SP-SUM closes the local coherent/tagged-sum interface while leaving
DG-RIG open. The next bounded arithmetic interfaces may then return to
SP-TRACE, SP-FROB and SP-SUBSYS with sums, tensors and process normalization
no longer conflated.
