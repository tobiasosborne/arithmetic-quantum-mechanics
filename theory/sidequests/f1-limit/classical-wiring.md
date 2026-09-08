# Classical wiring and typed multi-outcome instrument identities

Status: PROVED within the stated hypotheses. Admission and repaired scope
are recorded in `../../verdicts/f1-limit-adjudication.md`.

## Theorem CWIR-1 (canonical classical wiring)

**ASSUME** the register words and uniform classical traces of D1205 and the
Heisenberg UCP target of D1206.

**PROVE** D1218's classical product, unit, relabeling, and routing boxes are
typed trace-preserving star-isomorphisms satisfying their stated coherence.

<1>1. A bijection `r:O->P` gives the relabeling arrow
`rel_r:underline(O)->underline(P)`.

<2>1. In Heisenberg orientation its map is

    r^*:C^P->C^O,             r^*(f)(o)=f(r(o)).

<2>2. It preserves products, star and the unit pointwise.

<2>3. Its inverse is `(r^(-1))^*`, so it is a star-isomorphism and hence UCP.

<2>4. Bijections preserve cardinality and permute the summands of the
uniform trace, so `tau_O r^*=tau_P`.

<2>5. Direct substitution gives `rel_id=id` and
`rel_s o rel_r=rel_(s after r)` with the displayed arrow directions.

<1>2. The classical product box

    mul_(O,P):underline(O)underline(P)->underline(O times P)

is the canonical product-set star-isomorphism.

<2>1. Its Heisenberg map sends
`delta_(o,p)` to `delta_o tensor delta_p` and extends linearly.

<2>2. The displayed minimal projections are pairwise orthogonal and sum to
the unit, proving that the map and its inverse preserve product, star and
unit.

<2>3. On elementary functions the product reference trace satisfies

    tau_(O times P)(f tensor g)=tau_O(f)tau_P(g).

<2>4. Therefore `mul_(O,P)` and its inverse preserve the chosen traces.

<2>5. For the fixed singleton `*`, the identical construction
`C^{*}=C` gives `unit_cl:underline(*)->1` and its inverse.

<1>3. Cartesian associativity and units are explicit relabelings.

<2>1. Put

    a_(O,P,R):((O times P) times R)->(O times (P times R)),
    ((o,p),r)|->(o,(p,r)).

<2>2. Put `lambda_O:(* times O)->O` and
`rho_O:(O times *)->O` for the coordinate projections.

<2>3. Their `rel` boxes identify the two bracketings and delete a singleton
history wire.

<2>4. The pentagon and triangle commute because both paths are the same
bijection on every tuple.  Thus these are actual typed coherence maps rather
than an identification of differently bracketed sets.

<1>4. For a classical wire and any operational object word `X`, define

    route_(O,X):underline(O)X->Xunderline(O).

<2>1. Write `A_X` for the ordered spatial tensor algebra of `X`.  The
Heisenberg map is the spatial flip

    flip_(O,X):A_X tensor C^O -> C^O tensor A_X,
    a tensor f |->f tensor a.

<2>2. The flip is a unital star-isomorphism, is its own inverse after the
source and target are exchanged, and preserves the product trace.

<2>3. For words `X,Y`, both sides of

    route_(O,XY)
      =(id_X tensor route_(O,Y))
         o(route_(O,X) tensor id_Y)

send the factor order `O,X,Y` to `X,Y,O` by the same spatial permutation.

<2>4. Routing past the empty word is the identity.  Routing a product
outcome wire agrees with routing its two factors successively, after the
`mul` boxes, because both maps make the same permutation of three tensor
factors.

<1>5. Routing is natural for every typed process `F:X->Y`.

<2>1. In arrow orientation the required square is

    (F tensor id_O) o route_(O,X)
      =route_(O,Y) o (id_O tensor F).

<2>2. If `Phi:A_Y->A_X` realizes `F`, the Heisenberg maps on an elementary
tensor both send `a tensor f` to `f tensor Phi(a)`.

<2>3. Linearity proves the square on the whole finite-dimensional tensor
product.  This includes instruments, assembly/split, and preparation or
discard; no quantum block has been exchanged with another quantum block.

<1>6. Steps <1>1--<1>5 prove CWIR-1. **QED**

## Theorem CWIR-2 (routed sequential and parallel instruments)

**ASSUME** normalized corner instruments

    K:[alpha]->[beta]underline(O),
    L:[beta]->[gamma]underline(P),
    K':[alpha']->[beta']underline(P').

**PROVE** D1218 gives typed normalized sequential and parallel instruments
with exactly their displayed branch lists.

<1>7. The legal unfused sequential circuit is

    (L tensor id_underline(O)) o K:
      [alpha]->[gamma]underline(P)underline(O).

<2>1. It is composable because `L` acts on the retained `[beta]` output and
the identity retains the first classical history.

<2>2. Apply `route_(P,underline(O))` to put the older outcome first, then
apply `mul_(O,P)`.

<2>3. The resulting arrow is exactly

    Seq(L,K):[alpha]->[gamma]underline(O times P).

<2>4. On the branch `(o,p)`, the Schrödinger operator product is
`L_(p,j)K_(o,i)`, so the Kraus index is `(j,i)` and the history is `(o,p)`.

<1>8. The sequential product list is normalized.

<2>1. Direct calculation in the source corner gives

    sum_(o,p,i,j)(L_(p,j)K_(o,i))^*(L_(p,j)K_(o,i))
      =sum_(o,i)K_(o,i)^*(sum_(p,j)L_(p,j)^*L_(p,j))K_(o,i).

<2>2. The inner sum is `e_beta`; the outer sum is `e_alpha`.

<2>3. Thus `Seq(L,K)` is a normalized instrument, and its UCP realization is
the legal composite of the UCP instrument and wiring maps.

<1>9. The raw tensor circuit has type

    K tensor K':[alpha][alpha']
      ->[beta]underline(O)[beta']underline(P').

<2>1. Apply `route_(O,[beta'])` to move only the classical `O` wire past the
second quantum output.

<2>2. This produces `[beta][beta']underline(O)underline(P')`; applying
`mul_(O,P')` gives

    Par(K,K'):[alpha][alpha']
      ->[beta][beta']underline(O times P').

<2>3. Its branch list is
`(K_(o,i) tensor K'_(p',j'))_((o,p'),(i,j'))`.

<2>4. The movement in <2>1 is the classical spatial flip of CWIR-1.  It does
not use or imply a commutor between `[beta]` and `[beta']`.

<1>10. The parallel product list is normalized.

<2>1. In the separated source algebra,

    sum (K_(o,i) tensor K'_(p',j'))^*
          (K_(o,i) tensor K'_(p',j'))
      =(sum K_(o,i)^*K_(o,i)) tensor
        (sum K'_(p',j')^*K'_(p',j')).

<2>2. This is `e_alpha tensor e_alpha'`, the source unit.

<2>3. The same calculation after the Hecke block inclusion proves
normalization of D1209's direct collective `boxtimes_c` list.  Its quantum
source and target are the named collective atoms rather than the separated
words above.

<1>11. Uniform classical trace normalization agrees with branch masses.

<2>1. OPLIM-2 gives an unnormalized quantum branch density `T_o(rho)` whose
`tau_beta` trace is the outcome probability.

<2>2. Relative to `tau_beta tensor tau_O`, the recorded output density has
block `|O|T_o(rho)`.

<2>3. Therefore its total trace is

    |O|^(-1)sum_o tau_beta(|O|T_o(rho))=1.

<2>4. Product and route boxes preserve the product uniform trace by CWIR-1,
so sequential and parallel history routing introduces no additional density
factor beyond the cardinality of the fused history set.

<1>12. Steps <1>7--<1>11 prove CWIR-2. **QED**

## Theorem CWIR-3 (history coherence and Gram congruence)

**ASSUME** further composable instruments `M` with outcome set `R`, and two
composable pairs `K,K'` and `L,L'` with respective outcome sets
`O,P` and `O',P'`.

**PROVE** sequential associativity, parallel associativity, interchange, and
Kraus-label equality are typed relations preserved by realization.

<1>13. Sequential associativity uses the history bijection

    a:((O times P) times R)->(O times (P times R)),
      ((o,p),r)|->(o,(p,r)).

<2>1. The two parenthesized sequential lists have the same operator
`M_(r,k)L_(p,j)K_(o,i)` and differ only by the displayed history bracketing.

<2>2. Consequently

    Seq(Seq(M,L),K)
      =(id tensor rel_a) o Seq(M,Seq(L,K))

as typed arrows.

<2>3. CWIR-1 proves the relabeling realizations agree; the pentagon follows
because all rebracketings flatten to the same tuple `(o,p,r)`.

<1>14. Parallel associativity is proved identically.

<2>1. Both lists have operator `K_(o,i) tensor L_(p,j) tensor M_(r,k)`.

<2>2. Their outcome types are related by the same Cartesian associator, and
their quantum output order never changes.

<1>15. Sequential/parallel interchange uses the explicit bijection

    chi:((O times P) times (O' times P'))
           ->((O times O') times (P times P')),
    ((o,p),(o',p')) |->((o,o'),(p,p')).

<2>1. Parallel composition of the two sequential instruments has the
left-hand history and branch operator

    (K'_(p,j)K_(o,i)) tensor (L'_(p',j')L_(o',i')).

<2>2. Sequential composition of the two parallel instruments has the
right-hand history.  Multiplicativity of the block inclusion makes its
branch operator equal to <2>1.

<2>3. Postcomposing the first arrow with `rel_chi` therefore gives the
second as a typed arrow.  This is D1209's repaired collective interchange
relation.

<1>16. One-outcome instruments are handled by the singleton unitor.

<2>1. Their raw target is `[beta]underline(*)`.

<2>2. Postcomposition with `id_[beta] tensor unit_cl` gives an arrow
`[alpha]->[beta]`; no silent identification of object words is used.

<2>3. For the single Kraus operator `e_alpha` and `alpha=beta`, this
unit-retyped box is declared equal to the identity process. Its Heisenberg
map is `a |-> e_alpha a e_alpha=a`, so this identity relation is sound.

<1>17. Fibre coefficient-Gram equality is a sequential and parallel
congruence.

<2>1. At a fixed fibre, equal Grams in one outcome are equivalent to a
scalar-unitary mixing of its Kraus-index vectors after zero padding.

<2>2. For sequential products, mixings of `K` and `L` induce the tensor
unitary on `(j,i)` separately for each history `(o,p)`.

<2>3. For parallel products they induce the tensor unitary on `(i,j')`
separately for `(o,p')`.

<2>4. Thus the product-list Grams agree.  Relabeling merely renames outcome
blocks, and retained Hecke inclusion changes neither scalar mixing nor its
Gram cancellation.

<1>18. The same conclusion holds for intervals and germs without a
continuous environmental unitary.

<2>1. If continuous lists have equal Grams pointwise on `I`, apply <1>17 at
each `q`; the induced product Grams are pointwise equal and the resulting
continuous labels are equal in `Op_I^cts`.

<2>2. This argument quantifies fibre by fibre.  It neither chooses nor needs
a continuous family of the scalar unitaries witnessing the finite Gram
lemma.

<2>3. For germs, restrict to a common interval on which the input Grams
agree and repeat <2>1.  Hence eventual Gram equality is a congruence.

<1>19. All wiring boxes are constant permutation matrices in the fixed
finite tensor bases.

<2>1. They are therefore continuous on every parameter interval and have
canonical endpoint evaluations.

<2>2. The routed relations hold pointwise and consequently descend to germ
relations.

<1>20. Steps <1>13--<1>19 prove CWIR-3. **QED**
