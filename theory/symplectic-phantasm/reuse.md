# Reusing the finite Weyl results in the Phantasm contracts

2026-09-10. SP-WEYL is **PROVED** as the reviewed corollary in sections 1–2
of the already admitted F1-DUAL, F1-WEYL and F1-REAL. Section 3 supplies
the phase comparison used to reuse F1-FUNCT in SP-TENSOR; its affine
naturality and projective coherence are proved in `tensor.md`.
No earlier admitted result is reopened or assigned a new status.

Canonical definitions: D3–D5, D8–D9, D1001–D1004, D1701 and D1703.
The reused proofs are `../sidequests/f1-cyclotomic.md` §§0–3, admitted in
`../verdicts/f1-adjudication.md`. The rank-one sign convention is in
`../wh-kappa.md` §5, especially <1>1 and <1>5. The finite bridge probe is
`../checks/phantasm_reuse_check.py`; finite agreement does not replace
the proof review in `../verdicts/phantasm-weyl-r1.md`. The admission and
mechanically verified repairs are recorded in
`../verdicts/phantasm-stage1-adjudication.md`.

## 1. Symplectic coordinates and the finite character dual

**ASSUME** an odd-characteristic finite field k, q=|k|, a nontrivial
additive character psi:k->U(1), and a symplectic k-space V of dimension 2n.
**PROVE** the coordinate and character identification needed to apply
F1-REAL with A=(k^n,+), rather than assuming a rank-one result covers V.

<1>1. **ASSUME** V is nonzero. **PROVE** it splits off a symplectic plane.
  <2>1. Choose e!=0. Nondegeneracy gives f0 with omega(e,f0)!=0.
         Rescale to f=f0/omega(e,f0), so omega(e,f)=1.
         **BY** D1701 and field inverses.
  <2>2. For every v put
           v_perp=v-omega(v,f)e+omega(v,e)f.
         Then omega(v_perp,e)=omega(v,e)-omega(v,e)=0 and
         omega(v_perp,f)=omega(v,f)-omega(v,f)=0.
         **BY** bilinearity, alternation and omega(f,e)=-1.
  <2>3. The plane P=span(e,f) intersects P^perp only in zero: pairing
         ae+bf with e,f gives -b,a. The formula in <2>2 gives V=P+P^perp.
         Thus V=P direct-sum P^perp.
         **BY** the displayed pairings and decomposition.
  <2>4. A vector in the radical of the restricted form on P^perp pairs
         trivially with both summands, and hence with all of V. It is zero.
         **BY** D1701 and <2>3.
  <2>5. **QED** <1>1; the complement is symplectic of dimension 2n-2.

<1>2. **ASSUME** <1>1. **PROVE** a named symplectic coordinate map exists.
  <2>1. Induct on n using <1>1, with the unique map at n=0.
         This supplies e_1,...,e_n,f_1,...,f_n with
         omega(e_i,f_j)=delta_ij and the other pairings zero.
         **BY** the orthogonal direct sum in <1>1.
  <2>2. The map (a,b) |-> sum_i a_i e_i+b_i f_i is a k-linear isomorphism
         with omega((a,b),(a',b'))=a.b'-a'.b.
         **BY** the displayed basis pairings.
  <2>3. Record this coordinate map as a choice. It is not a preferred
         polarization or an additional datum of the abstract Weyl algebra.
         **BY** D1703's distinction between algebra and model coordinates.
  <2>4. **QED** <1>2.

<1>3. **ASSUME** psi as above. **PROVE** the phase datum fits D1001.
  <2>1. For every x, psi(x)^p=psi(px)=1. Its image is nontrivial and
         contained in the p-th roots of unity, so it has order p.
         **BY** the additive character law, D3 and primality of p.
  <2>2. Take mu_p=psi(k), with its actual inclusion iota into C^times.
         This is a named faithful realization of the cyclic phase group.
         The exponent of A=(k^n,+) divides p, including A=0.
         **BY** D1001–D1002 and characteristic p.
  <2>3. **QED** <1>3.

<1>4. **ASSUME** A=(k^n,+). **PROVE** b gives all characters of A.
  <2>1. Define chi_b(x)=psi(-b.x), as a mu_p-valued character.
         **BY** D3 and bilinearity of the dot product.
  <2>2. If b!=0, one coordinate b_j is nonzero and x |-> b.x is onto k:
         set x_j=c/b_j and the other coordinates zero.
         Nontriviality of psi therefore implies chi_b is nontrivial.
         **BY** this explicit choice of x.
  <2>3. Consequently b |-> chi_b is injective. F1-DUAL gives
         |Hom(A,mu_p)|=|A|=q^n, so it is bijective.
         **BY** <2>2 and the admitted finite-character theorem.
  <2>4. Under (a,b) |-> (a,chi_b), the F1-WEYL cocycle is
         chi_b'(a)^(-1)=psi(a.b'). Its commutator is psi(a.b'-a'.b).
         **BY** F1-WEYL §1 <1>1 and <1>6.
  <2>5. **QED** <1>4. This is the required perfect finite-abelian frame.

## 2. The half-form cochain and the inherited matrix realization

**ASSUME** the identifications of §1 and the reference operators of
D1003/D8. **PROVE** the D1703 realization and its SP-WEYL consequences
by transporting F1-REAL. No new finite Stone–von Neumann proof is needed.

<1>1. **ASSUME** standard coordinates v=(a,b), w=(a',b').
**PROVE** the cochain c(v)=psi(a.b/2) converts the reference cocycle.
  <2>1. The field identity
           a.b' + a.b/2 + a'.b'/2 - (a+a').(b+b')/2
             = (a.b'-a'.b)/2
         follows by expanding the last dot product.
         **BY** distributivity and invertibility of 2 in k.
  <2>2. Put W^s(v)=c(v)W_ref(a,chi_b). Its product multiplier is
         c(v)c(w)c(v+w)^(-1)psi(a.b')=psi(omega(v,w)/2).
         **BY** <2>1 and F1-WEYL's admitted multiplication law.
  <2>3. W^s(v) is unitary, since both factors are. With w=-v, the
         multiplier is 1, hence (W^s(v))^*=W^s(-v).
         **BY** F1-REAL §2 <1>4 and alternation of omega.
  <2>4. **QED** <1>1: this is a star-preserving transport of the algebra.

<1>2. **ASSUME** the computational basis delta_x. **PROVE** the model sign.
  <2>1. The existing reference action is
           W_ref(a,chi_b)delta_y=psi(-b.(y+a))delta_(y+a).
         **BY** D1003 and §1 <1>4; it is D8's Z(-b)X(a) convention.
         More explicitly, the n coordinate D8 operators have product
         coefficient product_j psi(-b_j(y_j+a_j))=psi(-b.(y+a))
         and send the tuple y to y+a. Thus D1703's tensor formula is
         this same reference action, by the additive character law and
         the named coordinate identification, without assuming SP-TENSOR.
  <2>2. Multiplying by c(v) gives
           W^s(a,b)delta_y=psi(-b.y-a.b/2)delta_(y+a).
         **BY** <1>1 and the dot-product expansion.
  <2>3. At output coordinate x=y+a this is
           (W^s(a,b)f)(x)=psi(-b.x+a.b/2)f(x-a).
         **BY** substitution y=x-a.
  <2>4. **QED** <1>2. Position labels agree with D8; the superscript s
         distinguishes the changed phase convention from W_ref.

<1>3. **ASSUME** F1-REAL for A=(k^n,+).
**PROVE** the matrix and trace clauses transport to D1703.
  <2>1. Rephasing a family by nonzero scalars does not change its span.
         F1-REAL supplies q^(2n) independent unitary operators spanning
         End_C(C[A]); hence W^s has that same full matrix image.
         **BY** F1-REAL §2 <1>3–<1>5 and c(v)!=0.
  <2>2. The abstract algebra has a basis of q^(2n) labels; the displayed
         map to the independent matrix family is bijective and respects
         product and star by <1>1. Its unit maps to the identity.
         **BY** D1703 and <2>1.
  <2>3. F1-REAL gives Tr(W_ref(v))=q^n[v=0]. Since c(0)=1,
         tau_V(x)=q^(-n)Tr(pi(x)) for every x.
         **BY** F1-REAL §2 <1>3 and linearity.
  <2>4. For a matrix B, Tr(B^*B) is the sum of squared absolute values
         of its entries, and vanishes only for B=0. The transported
         coefficient trace is therefore positive, faithful and normalized.
         Cyclicity follows by swapping the finite sums in Tr(BC)=Tr(CB).
         **BY** <2>2–<2>3 and these entry calculations.
  <2>5. **QED** <1>3.

<1>4. **ASSUME** the raw k-central half-form Heisenberg group and unitary
representations with the stipulated central character.
**PROVE** its fixed-psi representations use the same finite-abelian block.
  <2>1. Define
           (t,a,b) |-> (psi(t+a.b/2),a,chi_b)
         in H_p(A). Comparing two products reduces precisely to <1>1.<2>1.
         Thus it is a group homomorphism.
         **BY** the two displayed multiplication laws.
  <2>2. It is onto: the phase coordinate ranges through mu_p and §1
         identifies all b-characters. Its kernel is
           {(t,0,0):psi(t)=1}.
         **BY** §1 <1>3–<1>4 and the displayed map.
  <2>3. A raw-group unitary representation with central character psi kills
         that kernel. Conversely a unitary representation of H_p(A) with central
         character iota pulls back to central character psi; this pullback
         preserves the unitary structure.
         **BY** <2>2 and the explicit central coordinate.
  <2>4. Apply F1-REAL's uniqueness, dimension and unitary-intertwiner
         assertions after this quotient; the same module algebra and
         operators act. Unitary intertwiners are unique up to U(1).
         **BY** F1-REAL §2 <1>6–<1>8.
  <2>5. **QED** <1>4. The raw center map is not called injective; its
         kernel has q/p elements and can be nontrivial.

<1>5. **ASSUME** n=0 or n=1. **PROVE** the stated endpoint conventions.
  <2>1. At n=0, A=0, the model is C, the sole basis operator is 1 and
         its normalized trace is 1; the raw center reduction still applies.
         **BY** D1002, F1-REAL and the empty products in D1703.
  <2>2. At n=1, D1703's abstract cocycle is literally D4 with beta=omega/2.
         Its model is the phase change of D8 in <1>2, with the same labels.
         **BY** D4, D8 and <1>1–<1>2.
  <2>3. **QED** <1>5 and the admitted SP-WEYL corollary.

The September 9 wavefunction formula used f(x+a) and the opposite phase
coordinate signs. It was a valid realization obtained by v |-> -v from
the model above. This repair removes that unnecessary relabeling; it does
not assert that the archived bootstrap model failed its Weyl relations.

## 3. Reusing the tensor theorem

**ASSUME** configurations A=k^m and B=k^n, a common character and the
named coordinate order. **PROVE** the half-form phase change respects
F1-FUNCT's configuration-product tensor map.

<1>1. Write v=((a_1,a_2),(b_1,b_2)). Then
       c(v)=psi((a_1.b_1+a_2.b_2)/2)=c(a_1,b_1)c(a_2,b_2).
       **BY** the additive character law and the dot-product convention.
<1>2. F1-FUNCT maps the reference operator on A times B to the tensor
       of its two reference operators on C[A] tensor C[B]. Multiplying
       by <1>1 gives the same assertion for W^s.
       **BY** F1-FUNCT §3 <1>5–<1>6.
<1>3. The basis identification sends delta_(x,y) to delta_x tensor delta_y;
       its unit, associativity and permutation comparisons are the ones
       already admitted in F1-FUNCT. The phase factor in <1>1 is unchanged
       by rebracketing and by permuting whole factors.
       **BY** F1-FUNCT §3 <1>3–<1>6 and the sum of component dot products.
<1>4. **QED** for the transported configuration-product comparison.

SP-TENSOR's proof in `tensor.md` supplies the affine symplectic naturality
from SP-EGOROV. This section does not identify a source consisting only of
configuration isomorphisms with the full affine symplectic groupoid.

## 4. Reuse boundaries for the remaining contracts

FRB-TRACE and FRB-FROB already prove the finite-field trace and absolute
permutation statements. D1709 names the relative power and character
separately: U_(E/K,n)=(U_E^s)^tensor n and chi_(E/K)=chi_K o Tr_(E/K).
Matching these to the symmetrized frame is the remaining finite interface.
The fixed absolute character psi_E is not renamed or generalized in place.

FRP-CP already proves sound arithmetic Kraus composition, ordinary-trace
normalization and actual discards. D1706 extends its realized target to
arbitrary Hilbert blocks. Equality of target maps is not D1325's source
equality; neither source soundness nor a field-code decoder proves an
exhaustion theorem for all CP maps or a general symplectic subsystem theorem.

The precise inherited clauses and remaining work for every SP lemma are
recorded once in `claims/PHANTASM-DAG.md`, in Inherited, Reuse and Remaining.
SKETCH comparisons such as F1-CORR and F1-HALL, Hecke-specific completions,
and the separate degree-block algebra are not promoted by association.
