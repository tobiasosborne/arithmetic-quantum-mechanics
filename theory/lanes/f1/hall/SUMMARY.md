# A positive Hall/groupoid route from finite \(\mathbb F_1\)-vector spaces

Status of this note: literature synthesis plus an elementary specialization of
Szczesny's definitions.  It is a lane artifact, not an admitted project claim.
`SOURCE` means the cited paper states the result.  `DERIVED` means the displayed
calculation below follows directly from source definitions.  `OUR BRIDGE` marks
an identification or proposed north-star output not made by the cited authors.
Exact local source locators and hashes are in `SOURCE-MANIFEST.md`.

## The sourced chain

There is a developed positive construction, with three compatible levels.

1. **The explicitly \(\mathbb F_1\) level (SOURCE).**  Szczesny defines an
   \(A\)-module over \(\mathbb F_1\) to be a pointed set with an \(A\)-action.
   A finite \(\mathbb F_1\)-vector space is therefore a finite pointed set.
   Morphisms in the Hall category are *normal*: every fibre away from the
   basepoint has at most one element.  Subobjects are invariant pointed
   subsets, quotients collapse the subset to the basepoint, and direct sum is
   wedge sum.  The Hall product is the unweighted subobject convolution
   \[
     (f\star g)(M)=\sum_{N\subset M} f(M/N)g(N).
   \]
   For a finitely generated semigroup \(A\), the resulting rational Hall Hopf
   algebra is \(U(\mathfrak n_A)\), with \(\mathfrak n_A\) spanned by
   indecomposable \(A\)-modules (Szczesny, Definition 3 and pp. 5--6;
   Definition 6 and p. 8; Section 3, especially equation (8), coproduct, and
   Theorem 1 on pp. 9--11).  This is a genuinely nonadditive input category;
   the rational Hall algebra is an additive realization of it.

2. **The oscillator from finite sets (SOURCE).**  Baez--Dolan identify
   structure/stuff types over the groupoid of finite sets and bijections as a
   categorified Fock space.  Groupoid cardinality weights an isomorphism class
   by \(1/|\operatorname{Aut}|\), hence the \(n\)-element class has weight
   \(1/n!\).  They use
   \[
     f(x)=\sum_{n\ge0}f_n\frac{x^n}{n!},\qquad
     \langle f,g\rangle=\sum_{n\ge0}\frac{\overline{f_n}g_n}{n!},
   \]
   take annihilation to be \(a=d/dx\) and creation to be
   \(a^*=x\), and give the positive categorified relation
   \[
     AA^*\simeq A^*A+1
   \]
   by splitting histories according to whether the added and removed element
   are the same (Baez--Dolan, pp. 23--26).  The equality
   \(aa^*-a^*a=1\) appears only after decategorification.

3. **A rigorous categorified Heisenberg representation (SOURCE).**  Let
   \(\mathcal S\) be the groupoid of finite sets and bijections and
   \(+1:\mathcal S\to\mathcal S\) disjoint union with a singleton.
   Morton--Vicary encode the ladder operators by the mutually converse spans
   \[
   A=\bigl(\mathcal S\xleftarrow{\mathrm{id}}\mathcal S
                    \xrightarrow{+1}\mathcal S\bigr),\qquad
   A^\dagger=\bigl(\mathcal S\xleftarrow{+1}\mathcal S
                    \xrightarrow{\mathrm{id}}\mathcal S\bigr).
   \]
   Composition is weak pullback.  Their explicit calculation gives
   \[
      A\circ A^\dagger\simeq(A^\dagger\circ A)\oplus
      \mathrm{id}_{\mathcal S}
   \]
   (equation (15), pp. 8--9; Lemma 2.1/equation (24), p. 12).
   Theorem 2.7, p. 21, upgrades the combinatorics to a representation of
   Khovanov's categorified Heisenberg algebra in
   \(\operatorname{Span}(\mathbf{Gpd})\).  Their 2-linearization sends a
   groupoid to its complex representation category and produces the
   categorified Fock object
   \[
      \Lambda(\mathcal S)=[\mathcal S,\mathbf{Vect}]
          \simeq\coprod_{n\ge0}\operatorname{Rep}(S_n)
   \]
   (Corollary 3.3 and equation (73), p. 25).  Thus permutations of an actual
   \(n\)-element state survive categorification instead of disappearing when
   the state is replaced by the integer \(n\).

Khovanov supplies the diagrammatic algebra which Morton--Vicary realize.  His
additive monoidal category has generating objects \(Q_+,Q_-\); its Karoubi
envelope contains the symmetrizer/antisymmetrizer summands.  The map from his
integral Heisenberg algebra \(H_{\mathbb Z}\) into the Grothendieck ring is
**injective** (Theorem 1, p. 4), while surjectivity is explicitly Conjecture 1.
The symmetric-group model is induction/restriction along
\(S_n\subset S_{n+1}\), with the Mackey decomposition
\[
 \operatorname{Res}^{S_{n+1}}_{S_n}\operatorname{Ind}^{S_{n+1}}_{S_n}
 \cong
 \operatorname{Ind}^{S_n}_{S_{n-1}}\operatorname{Res}^{S_n}_{S_{n-1}}
 \oplus\operatorname{Id}
\]
(Khovanov, Proposition 7, p. 31).  This is relevant antecedent and target
structure; Morton--Vicary is the direct finite-set realization.

The categorical data should not be blurred together:

| construction | objects | morphisms/processes |
|---|---|---|
| Szczesny \(\mathcal C_A^N\) | finite pointed \(A\)-sets | pointed, \(A\)-equivariant normal maps |
| Baez--Dolan stuff types | a groupoid \(G\) equipped with \(G\to\mathcal S\) | stuff operators are groupoids over \(\mathcal S\times\mathcal S\); composition uses weak pullback |
| Morton--Vicary \(\operatorname{Span}(\mathbf{Gpd})\) | tame groupoids | tame/cotame spans; 2-morphisms are equivalence classes of tame/cotame spans of spans |
| Khovanov \(H'\), then its Karoubi envelope \(H\) | direct sums of tensor words in \(Q_+,Q_-\), then idempotent summands | linear combinations of oriented planar diagrams modulo the stated local relations |

## The elementary pointed-set Hall product (DERIVED)

Let \(V_n=\{*,1,\ldots,n\}\), and let \(u_n\) be the delta function of its
isomorphism class in the Hall algebra of finite \(\mathbb F_1\)-vector spaces.
There is one isomorphism class in each dimension.  Szczesny's convention puts
the right factor in the subobject: the coefficient of \(u_r\) in
\(u_m\star u_n\) counts pointed subsets \(L\subset V_r\) with
\(L\simeq V_n\) and \(V_r/L\simeq V_m\).  It vanishes unless \(r=m+n\), and
then choosing \(L\setminus\{*\}\) gives
\[
             u_m\star u_n={m+n\choose n}u_{m+n}
                          ={m+n\choose m}u_{m+n}.                 \tag{H}
\]
This uses no automorphism quotient.  Indeed
\(\operatorname{Aut}(V_n)=S_n\), so
\(|\operatorname{Aut}(V_n)|=n!\); Szczesny's equations (2)/(8) say the
subobject count multiplied by \(m!n!\) counts the corresponding exact
sequences with fixed endpoint identifications.

The map
\[
       \Phi:\mathcal H_{\mathbb F_1}\otimes_{\mathbb Q}\mathbb C
          \longrightarrow\mathbb C[x],\qquad
       \Phi(u_n)=\frac{x^n}{n!}
\]
is an algebra isomorphism by (H).  It also matches the coproduct:
Szczesny's \(\Delta(f)(M,N)=f(M\oplus N)\) gives
\[
       \Delta u_n=\sum_{i+j=n}u_i\otimes u_j,
\]
which is exactly \(\Delta(x^n/n!)\) for primitive \(x\).  Equivalently,
\(b_n:=n!u_n\leftrightarrow x^n\) is the ordinary monomial basis.  Since
\(V_1\) is the sole indecomposable, this also specializes Szczesny's
universal-enveloping theorem to
\(\mathcal H_{\mathbb F_1}\cong\mathbb Q[x]\).

The agreement with Baez--Dolan's \(1/n!\) is not an extra Hall-algebra
normalization: it is the automorphism weight introduced by groupoid
cardinality.  The useful basis dictionary is

| basis vector | polynomial | squared norm | \(a^\dagger=x\) | \(a=d/dx\) |
|---|---:|---:|---:|---:|
| Hall/divided power \(u_n\) | \(x^n/n!\) | \(1/n!\) | \((n+1)u_{n+1}\) | \(u_{n-1}\) |
| monomial \(b_n=n!u_n\) | \(x^n\) | \(n!\) | \(b_{n+1}\) | \(n b_{n-1}\) |
| orthonormal \(|n\rangle=\sqrt{n!}\,u_n\) | \(x^n/\sqrt{n!}\) | \(1\) | \(\sqrt{n+1}|n+1\rangle\) | \(\sqrt n|n-1\rangle\) |

Thus Hall multiplication by \(u_1\) is exactly \(a^\dagger\).  In the
monomial basis it adjoins a new element with coefficient one, while \(a\)
sums over the \(n\) possible elements to remove.  In the divided-power basis
the same counts move to the creation coefficient \(n+1\) through the
factorial rescaling.

Here \(a u_0=0\).  Direct calculation on
\(\mathcal F_{\mathrm{alg}}=\mathbb C[x]\) gives
\[
       (aa^\dagger-a^\dagger a)f
       =\frac d{dx}(xf)-x\frac{df}{dx}=f.                       \tag{CCR}
\]
With the displayed inner product, \(a^\dagger\) is adjoint to \(a\) on this
common invariant domain.  Completing gives the usual one-mode bosonic Fock
Hilbert space.  The operators are unbounded, so (CCR) is asserted on the dense
algebraic domain, exactly as Morton--Vicary caution on p. 1.

## The \(\mathbb F_1\) bridge and a separate north-star candidate

**OUR BRIDGE.**  Removing the basepoint gives an equivalence between the core
groupoid of finite \(\mathbb F_1\)-vector spaces and \(\mathcal S\):
\[
   (\text{finite pointed sets with normal maps})^\simeq
       \simeq (\text{finite sets and bijections}).
\]
The inverse adjoins a basepoint.  Szczesny explicitly calls the left-hand
objects \(\mathbb F_1\)-vector spaces.  Baez--Dolan, Morton--Vicary, and
Khovanov do **not** present their finite-set constructions as
\(\mathbb F_1\)-geometry.  Joining the two literatures through this core
equivalence is our inference, albeit a literal categorical equivalence rather
than a numerical analogy.

This yields a concrete positive candidate at the \(\mathbb F_1\) point:

\[
\begin{array}{c}
 \text{finite }\mathbb F_1\text{-vector spaces}\\
 \downarrow\ \text{core/groupoid and Hall realization}\\
 \bigl(\mathcal S;A,A^\dagger;
       AA^\dagger\simeq A^\dagger A\oplus\mathrm{id}\bigr)\\
 \downarrow\ \text{groupoid cardinality/complex linearization}\\
 \bigl(\mathcal F,\ A_1(\mathbb C),\ a^\dagger a\bigr).
\end{array}
\]

Here the kinematics is the automorphism-weighted completion of
\(\mathbb C[\pi_0\mathcal S]\), the observable algebra is the first Weyl/CCR
algebra
\[
 A_1(\mathbb C)=
 \mathbb C\langle a,a^\dagger\rangle/(aa^\dagger-a^\dagger a-1)
\]
on \(\mathbb C[x]\), and the standard number operator is
\(N=a^\dagger a\) (Morton--Vicary, p. 27).  The categorified object retains the full tower of
\(S_n\)-symmetries.  This candidate is choice-light at the point: disjoint
union with a singleton is unique up to the equivalence appropriate to the
groupoid setting, and no additive character or polarization is introduced.

The parts native to the combinatorics are pointed sets, normal maps,
subobjects, bijections, spans, and the positive direct-sum isomorphism.  The
Hall coefficients already take values in \(\mathbb Q\); subtraction in the
CCR, complex amplitudes, the Hilbert inner product, adjoints as analytic
operators, and completion are realization steps.  In particular, neither
\(a\) nor \(a^\dagger\) is a linear endomorphism internal to a nonexistent
additive category of \(\mathbb F_1\)-vector spaces.  Removal is naturally a
correspondence with a choice of element, which is why spans are the right
native carrier.

## What this is, and what it is not

This is the **infinite bosonic/second-quantized route**.  Particle number
\(n\) is unbounded, \(\mathcal F\) is infinite-dimensional, and
\(A_1(\mathbb C)\) is infinite-dimensional.  It is distinct from the
campaign's finite phase-space route over \(\mathbb F_p\), whose Weyl operators
satisfy a root-of-unity relation such as \(ZX=\zeta XZ\), whose observable
algebra is a finite matrix algebra, and whose Schrödinger space has dimension
\(p\).  A nonzero finite-dimensional characteristic-zero representation of
(CCR) cannot exist: taking traces would give
\(0=\operatorname{tr}[a,a^\dagger]=\operatorname{tr}I\).

The **Weyl/CCR algebra** here must also not be confused with a **finite Weyl
group** (a reflection/Coxeter group).  Abstractly, \(S_n\) is the Weyl group of
type \(A_{n-1}\), but that is not its role in these papers: it occurs as the
automorphism group of an \(n\)-element set and acts on repeated creation or
annihilation histories.  No root system or reflection representation enters.
These \(S_n\) are not a finite Heisenberg group and do not turn the Fock
representation into a finite Weyl--Heisenberg system.

The strongest honest scope statement is therefore:

* the literature already gives a positive, rigorous combinatorial
  Heisenberg/oscillator construction on the core of finite
  \(\mathbb F_1\)-vector spaces, together with complex and 2-linear
  realizations;
* Szczesny extends the Hall input to finite representations of any finitely
  generated semigroup with zero, and his free-monoid nilpotent example reaches
  the rooted-forest/Kreimer Hopf algebra;
* no cited source turns this into a functor on arbitrary \(\mathbb F_1\)-schemes,
  proves a canonical Hilbert completion for every monoid-representation Hall
  algebra, or recovers the finite \(\mathbb F_p\) Weyl--Heisenberg system.
  Morton--Vicary explicitly say their finite-set groupoidification does not
  directly handle the \(q\)-deformed case (p. 5).  Their 2-linearization over
  all finite sets also carries an Ind/completeness caveat immediately after
  Corollary 3.3 (p. 25).

So this lane supplies a separate viable north-star candidate, not a replacement
for the finite cyclotomic one: quantize the combinatorial population of
\(\mathbb F_1\)-states by Hall/groupoid correspondences, then linearize to the
bosonic Fock system.  Its next research question is functorial extension from
the affine monoid/point case to a suitable exact category attached to an
arithmetic scheme, with the realization and completion choices stated as
data.

## Tensor/qubit follow-up

`TENSOR-QUBIT.md` separates four notions which dimension alone obscures.  Its
main new derivation is that the complex span of Szczesny's normal
endomorphisms of the rank-two pointed set contains all matrix units, hence is
\(M_2(\mathbb C)\), while smash product realizes to the ordinary Hilbert tensor
product.  This finite pointed-set qubit uses noninvertible normal maps and is
therefore absent from the FinBij core.

For the order-eight finite Heisenberg groups, the unique two-dimensional
central-character representation is the noninvertible simple of the
Tambara--Yamagami fusion categories \(\operatorname{Rep}(D_8)\) and
\(\operatorname{Rep}(Q_8)\).  Its square is the sum of four invertible objects,
so the fixed nontrivial central-character sector is not tensor closed.
Internal fusion, external tensor product of independent systems, and central
product with a shared phase are three different composition laws.  Shimizu's
primary-source identifications and indicator distinction, together with the
exact character calculation, are recorded there and in `SOURCE-MANIFEST.md`.
