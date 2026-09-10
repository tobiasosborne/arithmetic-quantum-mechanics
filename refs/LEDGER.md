<!-- ROLE: registry of primary sources for the wh-kappa-target increment
     (briefs/wh-kappa-target.md). Under L3 (CLAUDE.md), a quotation, theorem
     citation, or "cite" anywhere in this repo must trace to a file physically
     present on disk under refs/arxiv-<id>/ (page/theorem/equation/line given
     below), or to a GAP row here naming what is missing. v0.1/references/**/
     SOURCES.md are POINTERS ONLY (L12): they were read once, to learn which
     arXiv ids a prior campaign found useful, and nothing below copies a
     bibliographic claim from them. Every id in this file was independently
     re-fetched in this session from https://arxiv.org/e-print/<id> and every
     title/author below was read out of the freshly fetched TeX, not out of
     v0.1's manifest. -->

# refs/LEDGER.md — sources for `Spec κ` Weyl–Heisenberg increment

Retrieval session: 2026-08-31, this container, direct to arXiv over the
preconfigured proxy. SHA256 values are of the raw bytes returned by
`https://arxiv.org/e-print/<id>` (before gunzip/tar extraction); each is also
stored verbatim on disk as `refs/arxiv-<id>/source.tex.gz` or
`source.tar.gz`, and `sha256sum` on that file reproduces the value below.
Source bodies are git-ignored (scaffold lane); this ledger is the durable,
committed record of what was fetched and what it says.

## Coverage of the four topics named in briefs/lanes/refs.md

| topic | verdict | sources |
|---|---|---|
| T1 — finite / finite-abelian Stone–von Neumann (uniqueness, fixed nontrivial central character) | **citable** | 0912.0574 (general LCA, full proof), 2502.00387 (general-ring form, finite fields checked explicitly), 0808.1664 (finite Heisenberg group over 𝔽_{2^d} directly) |
| T2 — Heisenberg groups over finite fields + twisted group algebras (central simplicity, dim q², ≅ M_q(C)) | **citable** | 1412.2490 (general theory: semisimple, Artin–Wedderburn, "central type", abelian case = A×A), 2501.00650 (displacement operators as a C-basis of End(H), the operational form of the same fact), 2502.00387 + 2204.08162 (Heisenberg group / Weyl-system definitions matching D2/D4) |
| T3 — Weil/metaplectic representation over a finite field, characteristic 2, when it linearizes | **citable, and sharply** | 0808.1664 is a paper titled exactly this; states the char-2 obstruction and its resolution precisely |
| T4 — additive characters of finite fields, absolute-trace pairing ψ_ζ = ζ^Tr, κ^×-torsor of nontrivial characters | **citable** | 2202.00248 (explicit ζ^Tr formula, specializes Galois-ring trace to finite-field trace), 1710.09884 (generating characters differ by a unit — the torsor statement, proved in-source) |

**No GAP rows.** All ten fetches below succeeded on the first attempt; no
source named in this file was unobtainable. Two scope notes, not gaps:
`WH-FORM`'s "the group preserving ω is SL₂(κ)" and `WH-POL`'s "isotropic
lines ↔ P¹(κ)" are elementary finite-linear-algebra facts about the specific
object `V(κ)=κ⊕κ`, not textbook theorems needing a citation beyond
`definitions.md`; they are not covered here because `briefs/lanes/refs.md`
did not list them among the four required topics, and the prover shard
should derive them directly rather than expect a citation for them.

---

## Summary table

| id | title (verified from fetched source) | authors | main TeX | retrieved | SHA256 (raw bundle) |
|---|---|---|---|---|---|
| 0912.0574 | An Easy Proof of the Stone-von Neumann-Mackey Theorem | Amritanshu Prasad | `SvN.tex` | 2026-08-31 | `acea15774d71e3697f1828fcea0d4aabe3bdf51dac07700af50e3099359068e3` |
| 2502.00387 | Canonical Commutation Relations: A quick proof of the Stone-von Neumann theorem and an extension to general rings | Bachir Bekka | `CCR-GeneralRings-v5.tex` | 2026-08-31 | `c0515c59a93bb8c7a609dd0bf49b5d07f807cafdc5b8b821a20286d92cdf7413` |
| 2104.14890 | Towards canonical representations of finite Heisenberg groups | S. Lysenko | `Canonical_Heis_rep.tex` | 2026-08-31 | `6b289c6a0213d7edc8cd2f571a42412356af0611dc0cf01a2ea591a650ca384d` |
| 0808.1664 | The Weil representation in characteristic two | Shamgar Gurevich, Ronny Hadani | `WeilCharTwo12-8-08.tex` | 2026-08-31 | `50fe23420c57f444349d521d53be3315416642f4760373b1f67410ca08bf1b84` |
| 1412.2490 | Simple twisted group algebras of dimension $p^4$ and their semi-centers | Ofir Schnabel | `groupsp4andsemi.tex` | 2026-08-31 | `9e156b471dec99b5d68aee233111bc723c23215595179e97890aef4bd4a19b0e` |
| 2501.00650 | Towards a Theory of SIC-like Phenomena: Regular Bouquets and Generalised Heisenberg Groups | David Solomon | `TotslipVersion5_Aug_25.tex` | 2026-08-31 | `d08e9982450d4de2fb0871ef9d66c2372d267ed858685f5e83cda5e384f003b3` |
| 2204.08162 | Gaussian quantum information over general quantum kinematical systems I: Gaussian states | Cedric Beny, Jason Crann, Hun Hee Lee, Sang-Jun Park, Sang-Gyun Youn | `main.tex` | 2026-08-31 | `119a4db85def25894a36e34f8b7ad20701558c77a00f9274d5a77febe8b39e18` |
| 2202.00248 | Entanglement-Assisted Quantum Error-Correcting Codes over Local Frobenius Rings | Tania Sidana, Navin Kashyap | `EAQECCs_over_rings_v15.tex` | 2026-08-31 | `3e64afec04ada4f744ea224362055f06a002c384ca09504e2014a93728687ddc` |
| 1710.09884 | On Quantum Stabilizer Codes derived from Local Frobenius Rings | Heide Gluesing-Luerssen, Tefjol Pllaha | `StabCodesFrob5.tex` | 2026-08-31 | `6755f6c3e8e8077fc179e228ae50d4f0de98ae2f8aba6fab9ec273608891f5ef` |
| quant-ph/0602001 | Hudson's Theorem for finite-dimensional quantum systems | D. Gross | `poswig.tex` | 2026-08-31 | `1c5371144c5b8b58fb6a8272546fdee54de0045e7dad3c9135a507d987ca9dfe` |

**Title-verification note (mismatch, recorded per instructions, not
silently fixed):** `v0.1/references/heisenberg_weil/SOURCES.md` records
2204.08162's title as "Gaussian Quantum Information over General Quantum
Kinematical Systems I" — no subtitle. The freshly fetched `main.tex:237`
carries the subtitle `: Gaussian states` in the `\title{}` macro. Minor, but
this file names it rather than absorbing it silently, per the brief. All
other nine titles/authors below matched the v0.1 pointer's bibliographic key
on the nose (case differences in v0.1's prose rendering aside); Solomon's
title has a commented-out (`%%`) draft fragment ("NUSV-Representations,")
between the two title lines that does not appear in the compiled title.

---

## T1 — Stone–von Neumann, finite / finite-abelian case

### 0912.0574 — Prasad, `SvN.tex`
- `SvN.tex:67-68` — `\title`/`\author`, verified.
- `SvN.tex:160-165` — defines the Heisenberg group `H` of an LCA group `L`
  from translation operators `T_x` and modulation operators `M_χ` on
  `L²(L)`, and the commutation relation `[T_x,M_χ]=e^{-2πiχ(x)}Id`.
- `SvN.tex:181-191` — the theorem itself, `\begin{theorem*}[Stone-von
  Neumann-Mackey]`: (1) `L²(L)` has no nontrivial proper closed `H`-invariant
  subspace (irreducibility of the canonical representation); (2) any unitary
  representation of `H` with the correct central character decomposes as an
  orthogonal sum of copies of the canonical representation, each isometry
  unique up to scaling. Stated for `L` a **general locally compact abelian
  group** — a finite abelian group is the compact-and-discrete special case,
  and no characteristic or parity restriction appears anywhere in the
  statement.
- `SvN.tex:193ff` — "The proof for groups with compact open subgroups": a
  finite `L` is literally a compact open subgroup of itself, so this is the
  branch of Prasad's own proof (not merely a citation) that specializes to
  our case.
- Role: primary, self-contained proof for `WH-SVN`'s uniqueness clause, valid
  uniformly in the characteristic including 2.

### 2502.00387 — Bekka, `CCR-GeneralRings-v5.tex`
- `CCR-GeneralRings-v5.tex:205-213` — `\title`/`\author`, verified.
- `CCR-GeneralRings-v5.tex:319-335`, `\label{Theo2}` — Theorem ("Stone-von
  Neumann Theorem"): for `R` a unital second-countable locally compact ring
  and `λ ∈ R̂` satisfying (Sym) `λ(ab)=λ(ba)` and (Isom) `∇_λ:R→R̂` an
  isomorphism, any pair of unitary representations of `R^d` satisfying the
  CCR is, after inflation, equivalent to the (inflated) Schrödinger pair.
- `CCR-GeneralRings-v5.tex:997-999` — explicit check that **`R` a finite
  field (or a direct sum of finite fields) satisfies condition (Isom) for
  every nontrivial character** — this is the clause that puts `κ` inside the
  theorem's hypothesis, with no parity exception stated or needed.
- `CCR-GeneralRings-v5.tex:1048-1070` — defines the matrix Heisenberg group
  `H_{2d+1}(R)` of `(2d+1)×(2d+1)` upper-triangular matrices over `R`, group
  law `m(a,b,c)m(a',b',c') = m(a+a', b+b', c+c'+a·b')`; center `≅ R`. This is
  the "matrix model" analogue of our `D4` Weyl-operator convention, over a
  general ring.
- `CCR-GeneralRings-v5.tex:1143-1151`, `\label{Theo2-bis}` — restates Theo2
  directly as: for `R,λ` as above and `d≥1`, any unitary representation `π`
  of `H_{2d+1}(R)` on a separable Hilbert space with central character `λ`
  has `π^{(∞)}` equivalent to `π_Schr^{(∞)}`. For `R=κ` finite this is
  precisely `WH-SVN` in Heisenberg-group form (dimension `q` of the model is
  then read off `L²(κ,μ)=ℂ^q`, an elementary count, not a further citation).
- `CCR-GeneralRings-v5.tex:971-972` — a general fact about central simple
  algebras over local fields, `𝒜 ≅ M_n(𝔻)`, is invoked (citing Weil's book,
  not proved here) for an unrelated example (real quaternions); flagged
  because it is adjacent to but **not** the twisted-group-algebra statement
  needed for `WH-ALG` — see T2 below for that.
- Role: primary for `WH-SVN` (Heisenberg-group form, uniform in
  characteristic), secondary for `WH-COMM`/`D4` (matrix-group realization of
  the Heisenberg group over a ring).

### 0808.1664 — Gurevich–Hadani (see T3 below for full entry)
- `WeilCharTwo12-8-08.tex:759-763`, `\label{S-vN_thm}` — Stone–von Neumann
  property stated and used directly for the finite Heisenberg group `H(V)`
  built from a symplectic `𝔽_{2^d}`-vector space `V`: unique (up to
  non-unique isomorphism) irreducible representation with a fixed faithful
  central character `ψ`. This is `WH-SVN` in exactly the characteristic-2
  case the brief is most worried about.

---

## T2 — Heisenberg groups over finite fields, twisted group algebras, central simplicity

### 1412.2490 — Schnabel, `groupsp4andsemi.tex`
- `groupsp4andsemi.tex:64-67` — `\title`/`\author`, verified.
- `groupsp4andsemi.tex:102-113` — defines the twisted group algebra `ℂ^fG`
  (basis `{u_g}_{g∈G}`, `u_x u_y = f(x,y) u_{xy}` for a 2-cocycle
  `f∈Z²(G,ℂ*)`); states that by a generalization of Maschke's theorem,
  `ℂ^fG` is **semisimple** (citing `[Karpilovsky, Thm 3.2.10]`, a textbook —
  not independently fetched, flagged honestly) and hence by Artin–Wedderburn
  is a direct sum of matrix algebras.
- `groupsp4andsemi.tex:114-125` — defines "`G` is of central type" as `ℂ^fG`
  being **simple** (a single matrix block) for some `f`, calls such `f`
  **nondegenerate**, and records "the size of any group of central type is a
  square" — for `G=V(κ)`, `|V(κ)|=q²`, automatically a square, consistent
  with `WH-ALG`'s claimed dimension.
- `groupsp4andsemi.tex:359-361` — "**Abelian groups of central type are
  exactly groups of the form `A×A`**" (cites `[BSZ, Thm 5]`, not
  independently fetched). `V(κ)=κ⊕κ` is literally of this form with `A=κ`,
  so this line is the general theorem `WH-ALG` specializes.
- Role: primary general-theory source for `WH-ALG`. **What it does not do**:
  it does not itself verify that our specific cocycle `ψ∘β` is nondegenerate
  in this sense — that check is exactly `WH-FORM`/`C2` (ω nondegenerate) and
  belongs to the prover's shard + `wh_kappa_check.py`, not to this citation.
  Combined with the dimension count (`ℂ^fG` simple + semisimple +
  `dim=|G|=q²` ⟹ the sole Wedderburn block is `M_q(ℂ)`, an immediate
  corollary of the two facts above), this closes `WH-ALG` "using no
  polarization," as the brief requires.

### 2501.00650 — Solomon, `TotslipVersion5_Aug_25.tex`
- `TotslipVersion5_Aug_25.tex:300-302` — `\title`/`\author`, verified
  (a commented-out draft fragment sits between the two title lines and is
  not part of the compiled title).
- `TotslipVersion5_Aug_25.tex:1637-1651` — Proposition (unlabeled, directly
  following `\subsection{Displacement Operators in the Schrödinger
  Representation}`): for displacement operators `D(a)=σ_p(𝒟(a))`,
  `Tr(D(a)†D(a')) = s·[a=a']` (trace orthogonality, `s=|A|`), and **the set
  `𝐃={D(a): a∈A⊕B}` is a ℂ-basis for `End_ℂ(ℳ(A))`** — i.e. the `s²`
  displacement operators are linearly independent and span the full
  `s×s` matrix algebra. This is the operational form of `WH-ALG` (and
  matches falsifier gate `C5` in `briefs/wh-kappa-target.md` almost exactly:
  "the `q²` Weyl operators are linearly independent, hence span `M_q(ℂ)`").
  Proof is given in-source (not deferred to another paper), with an
  alternative route pointed at `Theorem~\ref{thm:equivalent condits for SV}`.
- `TotslipVersion5_Aug_25.tex:405` — that theorem's relevant clause:
  irreducibility of `ρ` `⟺` `ρ(g_1),…,ρ(g_t)` linearly independent in
  `End_ℂ(V)` for coset representatives `g_i` of the center `Z` in `G` — a
  clean abstract SvN-adjacent criterion.
- Role: primary operational source for `WH-ALG`/`C5`; complements Schnabel's
  abstract central-simple-algebra framing with an explicit spanning proof.

### 2204.08162 — Beny–Crann–Lee–Park–Youn, `main.tex`
- `main.tex:237, 242-263` — `\title`/full author list, verified (5 authors:
  Beny, Crann, Hun Hee Lee, Sang-Jun Park, Sang-Gyun Youn).
- `main.tex:411-425` — defines a 2-cocycle `σ:G×G→𝕋` on an LCA group `G` and
  the associated **symplectic form** `Δ(a,b):=σ(a,b)σ(b,a)̄`; calls `σ` a
  **Heisenberg multiplier** when `Φ_Δ:G→Ĝ`, `Φ_Δ(a)(b)=Δ(a,b)`, is a
  topological group isomorphism.
- `main.tex:434` — "there is a unique (up to unitary equivalence) irreducible
  unitary projective representation with respect to `σ`" for any Heisenberg
  multiplier, **citing `[Digernes–Varadarajan 2004, Theorem 2]`** (not
  independently fetched here — flagged; this is the SvN-type fact this paper
  leans on rather than proves).
- `main.tex:461-473` — for `G=F×F̂`, the **canonical 2-cocycle**
  `σ_can((x,γ),(x',γ')) := γ(x')` and the resulting **Weyl operators**
  `W(x,γ)=T_xM_γ` satisfying `W(a)W(b)=σ(a,b)W(a+b)` (`main.tex:435-438`,
  eq. `eq-proj-rep`). Setting `F=κ` (so `F̂≅κ` via the trace pairing, T4
  below) reproduces `D2`'s `β((a,b),(a',b'))=ab'` and `D4`'s Weyl-operator
  law `W(v)W(v')=ψ(β(v,v'))W(v+v')` on the nose, up to the identification of
  `F̂` with `κ`.
- Role: secondary confirming source for the `D2`/`D4` conventions and for
  the general-LCA form of `WH-SVN` (with the caveat above about the
  Digernes–Varadarajan attribution).

*(2502.00387's `H_{2d+1}(R)` construction, T1 above, is also load-bearing
here as a second, independent finite-field Heisenberg-group definition.)*

---

## T3 — Weil / metaplectic representation over a finite field, characteristic 2

### 0808.1664 — Gurevich–Hadani, `WeilCharTwo12-8-08.tex`
- `WeilCharTwo12-8-08.tex:49-54` — `\title`/`\author`, verified: "The Weil
  representation in characteristic two", Shamgar Gurevich and Ronny Hadani.
- `WeilCharTwo12-8-08.tex:62-74` — abstract: constructs a Weil-representation
  variant `ρ:AMp(V)→GL(ℋ)` for `(V,ω)` symplectic over a finite field of
  characteristic 2, where `AMp(V)` is a **4th cover** of `ASp(V)` (a
  nontrivial gluing of `Sp(V)` and the dual group `V*`).
- `WeilCharTwo12-8-08.tex:88-110` — states precisely **why** the classical
  (odd-characteristic-style) construction fails at `p=2`: Weil's own char-2
  construction produces a representation not of `Sp(V)` but of a
  *pseudo-symplectic* group `Ps(V)` fitting `1→V*→Ps(V)→O(Q)→1`, and
  `O(Q) ⊊ Sp(V)` is a **proper** subgroup — the classical route does not
  even reach the group we want at `p=2`.
- `WeilCharTwo12-8-08.tex:612-665` — general setting: `k=𝔽_{2^d}` (a general
  finite field of characteristic 2, not just `𝔽_2`); the cocycle `β` with
  `β(v₁,v₂)−β(v₂,v₁)=ω(v₁,v₂)` (matching `D2` exactly, same non-symmetrized
  convention the brief mandates) is constructed **not** by a formula valued
  in `k` itself, but by lifting to a free symplectic module over
  `R=𝒪_K/𝔪_K²`, a ring of level-2 truncated Witt vectors (characteristic 4,
  not 2), and reducing. This is a substantive technical fact worth recording
  precisely for the prover: **the naive κ-valued recipe of `D2`/`D4` is not
  what makes the char-2 Weil representation work**; a genuine lift off `κ`
  is required.
- `WeilCharTwo12-8-08.tex:759-763`, Theorem `S-vN_thm` — Stone–von Neumann
  property for `H(V)`, `V` over `𝔽_{2^d}` (T1 above).
- `WeilCharTwo12-8-08.tex:771-793` — the **projective** Weil representation
  `ρ̃:ASp(V)→PGL(ℋ)` is a direct, standard consequence of `S-vN_thm` via the
  usual "intertwiner up to phase" argument (`Egorov`-type relation,
  `eq:Egorov`) — this part is characteristic-independent and always exists.
- `WeilCharTwo12-8-08.tex:796-803`, Theorem `Weilrep_thm` ("The Weil
  representation") — **this is where linearization is characteristic-
  sensitive**: the projective representation `ρ̃` lifts to a genuine linear
  representation `ρ:AMp(V)→GL(ℋ)` only after passing to `AMp(V)`, a central
  extension of `ASp(V)` by `μ₄` (**fourth** roots of unity) — not the
  classical `μ₂` (double-cover, "metaplectic") extension used away from
  `p=2`.
- `WeilCharTwo12-8-08.tex:805-822`, Theorem `Weilrep-split_thm` — records how
  this connects back to the classical picture: there is a splitting
  homomorphism `s:Mp(Ṽ)→AMp(V)` from the ordinary `μ₂`-metaplectic group of
  a symplectic module `Ṽ` over the Witt-vector ring, reducing mod 2 to `V`.
- Role: **the** primary source for `WH-WEIL`. It directly substantiates the
  brief's own instruction that "the cocycle's triviality is
  characteristic-sensitive and is NOT to be asserted": at `p=2` the
  projective representation always exists (standard SvN argument) but its
  linearization needs a `μ₄`-extension, not the `μ₂` one that suffices for
  odd characteristic — a strictly stronger obstruction than a mere sign
  ambiguity.

### quant-ph/0602001 — Gross, `poswig.tex` (contrast/background, not char 2)
- `poswig.tex:60-62` — `\title`/`\author`, verified: "Hudson's Theorem for
  finite-dimensional quantum systems", D. Gross.
- `poswig.tex:76-88` — abstract: results proved **explicitly and only for
  odd-dimensional** Hilbert spaces (`ℤ_d^n`, `d` odd); this restriction
  recurs at `poswig.tex:140, 172, 203, 342, 668, 2060` and is never lifted.
  Covers discrete Weyl operators, the Clifford group, and a discrete
  Stone–von Neumann/Clifford proof, all for odd `d`.
- Role: background/contrastive only. Explicitly **does not** cover `p=2`;
  registered because it is a clean, precise statement of the odd-
  characteristic Weyl-operator/Clifford picture that `WH-WEIL`'s odd-`p`
  case can be checked against, and because its explicit, repeated "`d` odd"
  hypothesis is itself evidence that the literature treats `p=2` as
  genuinely exceptional — consistent with Gurevich–Hadani above and with
  Lysenko's caveat below.

### 2104.14890 — Lysenko (even-order caveat, cross-referenced from T1)
- `Canonical_Heis_rep.tex:350` — uses "the Stone-von Neumann theorem" as a
  known fact (citing `[P]`, i.e. Prasad 0912.0574 above, at
  `Canonical_Heis_rep.tex:393`) to get an irreducible representation with
  the tautological central character, **defined up to a non-unique
  isomorphism** — ordinary SvN, no parity restriction.
- `Canonical_Heis_rep.tex:341-355` — but the paper's actual goal is a
  **canonical** (choice-free, unique-up-to-*unique*-isomorphism)
  representation, and this is constructed "only assuming the order of `M`
  odd; **the case of even order remains open**." This is a materially
  different, harder question than `WH-SVN`'s "up to unitary equivalence"
  uniqueness (which Bekka/Gurevich-Hadani settle at all `p` including 2) —
  flagged so the prover does not conflate the two and does not read this
  paper as contradicting `WH-SVN`.

---

## T4 — Additive characters of finite fields, absolute trace, κ^×-torsor

### 2202.00248 — Sidana–Kashyap, `EAQECCs_over_rings_v15.tex`
- `EAQECCs_over_rings_v15.tex:71-73` — `\title`/`\author`, verified.
- `EAQECCs_over_rings_v15.tex:103-108` — defines additive characters of a
  finite commutative ring `R` (`Hom(R,ℂ*)`), Frobenius rings (`∃χ` with
  `Hom(R,ℂ*)=R·χ`), and generating characters; states finite fields are
  Frobenius.
- `EAQECCs_over_rings_v15.tex:792-794` — the generalized trace map
  `Tr:GR(p^b,m)→ℤ_{p^b}` on a Galois ring, and **"For `b=1`, ... the
  generalized trace map `Tr` reduces to the usual trace map `tr:𝔽_{p^m}→𝔽_p`
  defined by `tr(z)=z+z^p+z^{p²}+⋯+z^{p^{m-1}}`"** — i.e. the absolute
  trace `Tr_{κ/𝔽_p}` of `D3`, for `κ=𝔽_{p^m}`.
- `EAQECCs_over_rings_v15.tex:805-807`, Proposition `prop:charGR`
  (**attributed in-source to `[shuqin]`, not independently fetched by this
  lane — flagged**): "The map `χ:GR(p^b,m)→ℂ*` defined by `χ(r)=ζ^{Tr(r)}`,
  with `ζ=exp(2πi/p^b)`, is a generating character of `GR(p^b,m)`." At
  `b=1` this is exactly `D3`'s `ψ_ζ = ζ^{Tr_{κ/𝔽_p}(·)}`.
- Role: primary source for the explicit trace-power formula. The specific
  proposition is second-hand within this paper (attributed to `[shuqin]`);
  the reduction-to-usual-trace statement at `:794` and the surrounding
  Frobenius-ring framework are this paper's own.

### 1710.09884 — Gluesing-Luerssen–Pllaha, `StabCodesFrob5.tex`
- `StabCodesFrob5.tex:141-143` — `\title`/`\author`, verified.
- `StabCodesFrob5.tex:232-243`, Theorem `T-Frob` (proved in-source, citing
  classical textbook results — Lam, Lamprecht, Hirano, Wood, Honold — for
  the equivalence of characterizations, not for the final clause): for `R` a
  finite commutative Frobenius ring, `R̂ ≅ R·χ` for a generating character
  `χ`, **and "any two generating characters `χ,χ'` differ by a unit, i.e.
  `χ'=u·χ` for some `u∈R*`."**
- `StabCodesFrob5.tex:254-261`, Remark `R-FrobProp`(a) (cites `[ClGo92, Cor
  3.6]`): `χ` is generating **iff** the only ideal contained in `ker χ` is
  the zero ideal.
- `StabCodesFrob5.tex:245` — finite fields are named explicitly among the
  examples of Frobenius rings.
- Derivation recorded here (mine, elementary, not a further citation): for
  `R=κ` a field, the only ideals are `0` and `κ`; `ker χ ≠ κ` for any
  nontrivial `χ`, so by Remark `R-FrobProp`(a) **every nontrivial character
  of a finite field is generating**. Combined with Theorem `T-Frob`, the set
  of nontrivial additive characters of `κ` is exactly `{u·χ₀ : u∈κ*}` for
  any fixed nontrivial `χ₀` — a free transitive `κ*`-action, i.e. the
  `κ^×`-torsor structure `WH-CHOICE` needs. The torsor *statement* traces to
  `T-Frob`+`R-FrobProp`(a) above; the one-line specialization to a field is
  routine and not separately sourced.
- Role: primary source for the torsor structure of nontrivial additive
  characters (stated in-source, not deferred to an unfetched paper).

---

## Fetch log (for reproducibility)

Refetch note (2026-09-01): the wh-kappa-era source bodies are git-ignored
and were absent from this working copy after the reboot; `1710.09884` and
`2202.00248` were refetched from `https://arxiv.org/e-print/<id>` and their
raw-bundle SHA256 values reproduced the table above exactly. Other absent
bodies remain readable at the v0.1 mirror paths until refetched.

All ten `curl -sSL https://arxiv.org/e-print/<id>` fetches in this session
returned HTTP 200 (after the expected redirect to `/src/<id>`) on the first
attempt; none needed a retry. `file` was run on every payload before
extraction: six were single gzipped `.tex` files (name recovered from the
gzip header), four were gzipped tar bundles (`quant-ph/0602001`'s gzip
header names `0602001.tar`; the other three tar bundles carry no embedded
name and were identified by `tar tzf` succeeding). Politeness: ~3s sleep
between fetches, as instructed.

---

## Orchestrator precision notes (2026-08-31, session 1)

Added by the orchestrator after independently re-reading the source. These
correct or sharpen the lane's summary and are binding on the prover shard.

**N1 — the characteristic-two Weil statement, stated precisely.**
`refs/arxiv-0808.1664/WeilCharTwo12-8-08.tex`:

- lines 92-99: away from characteristic two, `rho_Weil` is a representation of
  a **double** cover of `Sp(V)` (the metaplectic cover).
- lines 99-110: in characteristic two, Weil's own construction gives a
  representation of a double cover of the **pseudo-symplectic** group `Ps(V)`,
  which is a nontrivial gluing of an *orthogonal* group with the dual space:
  `1 -> V^* -> Ps(V) -> O(Q) -> 1`, where `Q(v) = beta(v,v)` for a
  **non-symmetric** bilinear form `beta` with `beta(v,u) - beta(u,v) = omega(v,u)`.
- lines 155-165: this paper's variant is a linear representation of
  `AMp(V)`, the *affine metaplectic group*, a central extension of `ASp(V)` by
  the group `mu_4` of **fourth** roots of unity — not by `mu_2`.

Two consequences the prover must respect rather than smooth over:

1. At `p = 2` the symmetry group carrying the Weil representation is **not**
   `Sp(V)`. Any statement of `WH-WEIL` that says "`SL_2(κ)` acts projectively"
   uniformly in `p` is claiming more than this source supports. Scope it, or
   state the `p = 2` case separately in the pseudo-symplectic / affine form.
2. The cover is by `mu_4` in characteristic two. "Projective representation
   lifting to a double cover" is an odd-characteristic statement.

**N2 — the non-symmetric cocycle is the literature's convention too, not our
invention.** The `beta` appearing in the source's characteristic-two setup
(lines 106-110) satisfies exactly the identity `briefs/wh-kappa-target.md`
mandates for D3: `beta(v,u) - beta(u,v) = omega(v,u)`, with `beta`
non-symmetric and the associated quadratic form `Q(v) = beta(v,v)`. Our
convention choice is therefore aligned with the source rather than a local
idiosyncrasy, and `Q(v) = beta(v,v)` is the object to watch at `p = 2`: it is
identically zero in odd characteristic under a symmetrized convention, and it
is not zero here.

---

# FCR-1 addendum — sources for the finite-local-ring increment

Registered 2026-09-01 by the orchestrator for `briefs/fcr-local-target.md`.
Retrieval route noted per source; bodies on disk under `refs/`, git-ignored;
this ledger is the committed record.

## Summary table

| id | title (verified from fetched file) | authors | file | retrieved | SHA256 |
|---|---|---|---|---|---|
| wood-ajm-1999 | Duality for modules over finite rings and applications to coding theory (Amer. J. Math. 121.3 (1999) 555–575, DOI 10.1353/ajm.1999.0024) | Jay A. Wood | `refs/wood-ajm-1999/wood_duality_ajm121_1999.pdf` (22 pp, full text; plus `pdftotext` extraction `.txt` whose line numbers are cited below) | 2026-09-01, `https://muse.jhu.edu/pub/1/article/849/pdf`, served in full without authentication | `11e84439cb3dc251c447e6cd792ad12ce332e3d9c7eb7b348a876114859d8963` |
| stacks-algebra | Stacks Project, chapter "Commutative Algebra" (`algebra.tex`, master snapshot) | The Stacks Project authors | `refs/stacks-algebra/algebra.tex` | 2026-09-01, `https://raw.githubusercontent.com/stacks/stacks-project/master/algebra.tex` | `fa8bb92e58a4f78a2bd01b3b6a4a87de0a0d279f5dd90641b574dd5fbfffa4f3` |

## wood-ajm-1999 — locators (into the `.txt` extraction; page numbers are the journal's)

- `.txt:492-…` — **Theorem 3.10** (p. 562): for a finite ring `R`, t.f.a.e.:
  (i) `R` is Frobenius; (ii) `R̂ ≅ R` as left modules; (iii) as right modules.
- `.txt:556-562` — §4 opening (p. 563): definition of (left/right) *generating
  character* as `ψ` with `r ↦ ψ(r·)` an isomorphism `R → R̂`; "From Theorem
  3.10, a finite ring is Frobenius if and only if it admits a right or a left
  generating character."
- `.txt:570-…` — **Lemma 4.1** (p. 563, attributed in-source to
  Claasen–Goldbach Cor. 3.6): `ψ` is a generating character iff `ker ψ`
  contains no nonzero (right) ideal.
- `.txt:595-…` — **Theorem 4.3** (p. 563): left generating iff right
  generating (moot in our commutative case, recorded for scope hygiene).
- `.txt:608-…` — **Example 4.4** (pp. 563–564): (i) finite fields via
  `ψ(x) = ζ^{tr(x)}`; (ii) `Z/(m)` via `ψ(x) = e^{2πix/m}` — the explicit
  generating character for the `Z/9`, `Z/27` seeds; (iii) finite direct sums
  of Frobenius rings are Frobenius with product character (reserved for
  FCR-4, registered now).
- Role: **primary source** for `FCR-GEN`'s Frobenius ⟺ generating-character
  equivalence and for the explicit seed characters. The `soc(R)`-simplicity
  form of "Frobenius" for commutative local `R` is to be *derived* in the
  shard (or checked by census), not read into Wood, whose definition of
  Frobenius is via `R/rad(R) ≅ soc(R)`.

## stacks-algebra — locators (line numbers in the fetched `algebra.tex`)

- `algebra.tex:12699` `\label{section-artinian}` — §Artinian rings.
- `algebra.tex:12724` `\label{lemma-artinian-finite-nr-max}` — finitely many
  maximal ideals.
- `algebra.tex:12739` `\label{lemma-artinian-radical-nilpotent}` — the
  Jacobson radical of an Artinian ring is nilpotent (for local finite `R`:
  `m` nilpotent).
- `algebra.tex:12758` `\label{lemma-product-local}` — a ring with finitely
  many maximal ideals and locally nilpotent Jacobson radical is the product
  of its localizations at maximal ideals (the canonical local decomposition;
  load-bearing only in FCR-4, registered now).
- `algebra.tex:12787` `\label{lemma-artinian-finite-length}` — Artinian ⟺
  finite length; Artinian ⟹ Noetherian.
- Role: structure facts for convention group 1 of the FCR-1 brief. A finite
  ring is Artinian (finite descending chains terminate — this one-line
  observation is the shard's, not a citation).

## Carried-over sources already registered above that FCR-1 may cite

- `1710.09884` (Gluesing-Luerssen–Pllaha) — `StabCodesFrob5.tex:232-243`
  Theorem `T-Frob`: for finite **commutative** Frobenius `R`, any two
  generating characters differ by a unit (`χ' = u·χ`, `u ∈ R^×`) — the
  torsor statement of `FCR-GEN`; `StabCodesFrob5.tex:254-261` Remark
  `R-FrobProp`(a): generating iff no nonzero ideal in the kernel.
- `2202.00248` (Sidana–Kashyap) — Galois-ring trace and generating
  characters over local Frobenius rings (Prop `prop:charGR`, attributed
  in-source to `[shuqin]`, flagged as second-hand there).
- `2502.00387` (Bekka) — Stone–von Neumann for general rings: condition
  (Isom) (`∇_λ : R → R̂` an isomorphism) **is precisely the generating-
  character condition**; `CCR-GeneralRings-v5.tex:319-335` Theo2 then gives
  uniqueness. The prover should check whether Bekka's (Sym)+(Isom)
  hypotheses hold verbatim for a finite commutative Frobenius `R` with
  `ψ ∈ Gen(R)` — if yes, `FCR-SVN` has a direct in-source proof path.
- `0912.0574` (Prasad) — Stone–von Neumann–Mackey for LCA groups; applies
  to `(R,+)` finite abelian with the duality `R ≅ R̂` supplied by `ψ`.

---

# FCR-2 addendum — sources for the residue-characteristic-2 increment

Registered 2026-09-01 by the orchestrator for `briefs/fcr2-target.md`.
Fetched from `https://arxiv.org/e-print/<id>`; SHA256 of the raw bundle,
stored as `refs/arxiv-<id>/raw`.

| id | title (verified from fetched TeX) | authors | main TeX | retrieved | SHA256 (raw) |
|---|---|---|---|---|---|
| 1108.0202 | Weil Representations associated to finite quadratic modules | Fredrik Strömberg | `weil_representations_for_fqm_arxiv.tex` | 2026-09-01 | `6b8a4fdcd016d6b75be05bf0632b15a4eb56e572a8fc95bf84338fc9f4f2669d` |
| 1705.04572 | Computing invariants of the Weil representation | Stephan Ehlen, Nils-Peter Skoruppa | `invariants.tex` (+`preamble.tex`) | 2026-09-01 | `e6db276f24998182abb4509d58b952fb2ec60b7ca58db6d73ec893dd5eada16a` |

- `1108.0202`, label `eq:milgrams_formula` — **Milgram's formula stated
  verbatim in-source**: `|D|^{-1/2} Σ_{μ∈D} e(Q(μ)) = e_8(sign(𝒬))` for a
  finite quadratic module `𝒬 = (D,Q)` — the `μ_8`-valued Gauss sum with
  mod-8 signature that `FCR2-EPS` conjectures is the thickened-ring
  generalization of the `WH-BETA-EPS` Arf sign. The paper also carries the
  `oddity`/`p-excess` decomposition machinery and Jordan-component
  formulas for such sums.
- **Scope caution for the prover:** a finite quadratic module in these
  sources is `Q : D → Q/Z` on a finite abelian group with
  `Q(x+y)−Q(x)−Q(y)` the bilinear pairing; our `Q_β : V(R) → R` composed
  with `ψ ∈ Gen(R)` gives `ψ∘Q_β : V → C^×`, and the corrected polarization
  identity has the extra `2β − ω` structure (brief convention 1). The
  bridge `(V, ψ∘Q_β)` ↦ finite quadratic module must be stated and checked,
  not assumed; whether `ψ∘ω`-compatibility puts it in the sources'
  hypotheses is part of `FCR2-EPS`.
- Wall (Topology 1963) and Brown (Ann. Math. 95, 1972) remain unfetched
  (paywalled); recorded as a GAP: `FCR2-EPS` cites Strömberg/Ehlen–Skoruppa
  or stays CONJECTURE.

---

**N3 — role-narrowing on 1412.2490.** Its verified title is "Simple twisted
group algebras of dimension `p^4` and their semi-centers", which is narrower
than the general role the coverage table assigns it. The general facts it is
cited for (semisimplicity of twisted group algebras, Artin-Wedderburn, groups
of central type, the abelian `A x A` characterization) appear in its
introductory material and are there **attributed to Karpilovsky**, which the
lane correctly flagged as attributed-through rather than independently
fetched. Treat those as ADMITTED steps under L3 until Karpilovsky is
registered, and let the affected claim's status reflect that.

---

## F1 sidequest — comparative literature, qubits and tensor products
Retrieved and inspected 2026-09-06. All source bodies below are local at
`refs/f1/<key>/paper.pdf`, with `paper.txt` from `pdftotext -layout` and
`retrieval.json`. PDFs are the source of record; SHA256 values are of PDF
bytes. These bodies remain git-ignored under the existing source policy.
Titles were checked against the PDF front matter. Source versions are
recorded separately from later publication dates.

| key | title / authors | date / version | retrieval URL | PDF SHA256 |
|---|---|---|---|---|
| `1312.4191` | Quantum F_un: the q=1 Limit of Galois Field Quantum Mechanics, Projective Geometry, and the Field with One Element — Chang, Lewis, Minic, Takeuchi | 2014; arXiv v3 | https://arxiv.org/pdf/1312.4191 | `9799a2d9566840921cf6bc51317b632475b81f0fb0aa65a3d1888a28935b955e` |
| `1808.09694` | Absolute Quantum Theory (after Chang, Lewis, Minic and Takeuchi), and a road to quantum deletion — Koen Thas | 2018 preprint; journal 2019 | https://arxiv.org/pdf/1808.09694 | `52f3cc735a1af7712b6e6721bd6f27993316b8abb27d8803a210b166502ce2c6` |
| `1607.04513` | Projective spaces over F1^ell — Koen Thas | 2016 | https://arxiv.org/pdf/1607.04513 | `ffe3085849f78524baf52fa10092dd9c091949299d5014e6eaf2ad865b90e26d` |
| `math-0404185` | Schemes over F1 — Anton Deitmar | arXiv v7, 2006 | https://arxiv.org/pdf/math/0404185 | `b61f5a5c88f224fa3d8c56120bcfcd7ba02eec58bec1da5e857f47b83b96ae09` |
| `math-0608179` | F1-schemes and toric varieties — Anton Deitmar | arXiv v10, 2014 | https://arxiv.org/pdf/math/0608179 | `ded5a59ebbf048184d6229a378a344e350e8ebb9ccbb2f2bbd4e6effe6434cb3` |
| `1201.1324` | The geometry of blueprints. Part II: Tits-Weyl models of algebraic groups — Oliver Lorscheid | 2012 preprint; published 2018 | https://arxiv.org/pdf/1201.1324 | `f65b90c9e98899ea6f72bbc234f518b64d755a02d44aa4bfa456abdbcab1c33a` |
| `1301.0083` | A blueprinted view on F1-geometry — Oliver Lorscheid | 2013, arXiv v2 | https://arxiv.org/pdf/1301.0083 | `1ec49646a2854cb96b47826cb6b4db7c46ecf94dde8d97ca49f56d8beae382fc` |
| `2305.13809` | Towards the horizons of Tits’s vision — on band schemes, crowds and F1-structures — Oliver Lorscheid and Koen Thas | 2023 | https://arxiv.org/pdf/2305.13809 | `eda73526a426070a09f7a5cc95537efbc1b788a1d2147afd65bdae6c25626914` |
| `1204.5395` | On the Hall algebra of semigroup representations over F1 — Matt Szczesny | 2012 | https://arxiv.org/pdf/1204.5395 | `517e2353f5448ee73dec4523ab131d59cc4529102f11328248f0f33c47265978` |
| `math-0004133` | From Finite Sets to Feynman Diagrams — John C. Baez and James Dolan | 2000 preprint; published 2001 | https://arxiv.org/pdf/math/0004133 | `687de8249639c7f27fe1413b26034340e4b37b155afcce2af9256b56183ccc5d` |
| `1207.2054` | The Categorified Heisenberg Algebra I: A Combinatorial Representation — Jeffrey C. Morton and Jamie Vicary | 2013, arXiv v2 | https://arxiv.org/pdf/1207.2054 | `a16e9513597feb440ee2f4923d95e5201785b650656a1cb3a6f66d7d4e6376d1` |
| `1009.3295` | Heisenberg algebra and a graphical calculus — Mikhail Khovanov | 2010 preprint | https://arxiv.org/pdf/1009.3295 | `c01811fc205984b892bce7e4599be093dc1dbfd1faf8496527bd17f1ab354adb` |
| `0906.3146` | Lambda-rings and the field with one element — James Borger | 2009 | https://arxiv.org/pdf/0906.3146 | `acf748e4c39b3a0a7462760dea0f3f9af6bd0abb647766f2740697b47d88cc92` |
| `0806.2401` | Fun with F1 — Alain Connes, Caterina Consani and Matilde Marcolli | 2008 preprint; journal 2009 | https://arxiv.org/pdf/0806.2401 | `db7b379eaf061bb87714b4e59f725cebdff54556bfb39178dcf167a29475f7fa` |
| `0809.1564` | Cyclotomy and analytic geometry over F1 — Yuri I. Manin | 2008 preprint | https://arxiv.org/pdf/0809.1564 | `d7186fe82b27d90d6c075cbe81303277cac4332ad54a3fcefe0d2870eaeed55c` |
| `1405.4527` | The Arithmetic Site — Alain Connes and Caterina Consani | 2014 | https://arxiv.org/pdf/1405.4527 | `bcac55c2479d4a3c66a163454002847d0b14911993a6fde34bf5da6c232e0a46` |
| `1901.00020` | Bost-Connes systems and F1-structures in Grothendieck rings, spectra, and Nori motives — Joshua F. Lieber, Yuri I. Manin and Matilde Marcolli | 2018/2019 preprint; book chapter 2022 | https://arxiv.org/pdf/1901.00020 | `313f74c69743222ae03e5becc2585c98c0151117f277266b4982cfbe9931da2d` |
| `math-0511263` | On the classification of rational quantum tori and the structure of their automorphism groups — Karl-Hermann Neeb | 2005 preprint; revised 2007; journal 2008 | https://arxiv.org/pdf/math/0511263 | `d928c760b3e8100f662bbd01e35d2550fe60845dd46a5cfd13c98d8b1fa6277d` |
| `bost-connes-1995` | Hecke Algebras, Type III Factors and Phase Transitions with Spontaneous Symmetry Breaking in Number Theory — Jean-Benoit Bost and Alain Connes | 1995 | https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf | `451920723394e27a9e17dad520444f7458fcb540ab8af8948b227cb109eb37c9` |
| `1209.4837` | Quantum field theory over F1 — Dori Bejleri and Matilde Marcolli | 2012 | https://arxiv.org/pdf/1209.4837 | `2e48a5ae3e70d92585103ee2d9dc611e5b5ffe091cc477b04372d5e0c0b9cd7c` |

### Claim-to-source locators and scope

- **1312.4191** — Sections 2.1, 2.4 and 3.2, equations (17)–(23), (32)–(34): finite-field amplitudes and coordinate-state q=1 model.
- **1808.09694** — Sections 3.2–3.5: Cartesian frames versus simple points; partial form equation (6), support orthogonality (7), monomial operators (9)–(11); Theorem 4.2: involution-dependent unitary group; section 6: cloning simple rays versus all frame states.
- **1607.04513** — Section 1.3, pp. 2–3: extension conventions and functor-of-points frames. Used to contextualize Thas quantum states, not as a Hilbert-space construction.
- **math-0404185** — Sections 1–2: monoids and monoid-algebra realization; section 5.1, pp. 14–16, and 5.2, p. 16: linear and symplectic F1 symmetries.
- **math-0608179** — Theorem 4.1: toric nature under its stated connectedness/integrality/finiteness assumptions. Supporting scope source; no universal no-go for other F1 frameworks.
- **1201.1324** — Definition 3.13 and Theorem 3.14, pp. 49–51: Tits–Weyl and extended Weyl data. Remark 5.4 and Proposition 5.5, pp. 78–79: standard GL_n parabolic unipotent radicals. Specialization to UT3 is our explicit deduction, not a quoted quantum theorem.
- **1301.0083** — Section 1.1.4, pp. 14–15: cyclotomic blueprints, different from raw group-ring extension; Remark 2.6: model dependence; section 3.2: geometric unitary-representation terminology.
- **2305.13809** — Theorems 1.1–1.2: Krasner combinatorial flags and crowd action. Definition 5.1: crowd axioms; Definition 5.9 and section 5.4: affine algebraic SL_n crowd. UT3 restriction and its signed/Krasner counts are new local derivations. Example 5.11 SL2 inverse closure MUST NOT be imported to UT3.
- **1204.5395** — Definition 3, pp. 5–6: pointed modules and dimension; Definition 6, p. 8: normal maps; section 3, equation (8), pp. 9–11: Hall convolution and enveloping-algebra theorem. Our one-point specialization gives binomial coefficients.
- **math-0004133** — Pages 14–16: groupoid cardinality; pp. 23–26: factorial-weighted Fock inner product, creation/removal, positive categorical CCR. The identification with the core of F1 vector spaces is our bridge.
- **1207.2054** — Equation (1), p. 1: dense-domain CCR; equations (15)–(19), pp. 8–9; Lemma 2.1 and Theorem 2.7: spans and categorical relation; Corollary 3.3 and equation (73), p. 25: representation-category tower WITH Ind/completeness caveat. This source does not itself call its construction F1 geometry.
- **1009.3295** — Theorem 1 and Conjecture 1, p. 4: Grothendieck-ring map injective, surjectivity conjectural in this source. Proposition 7, p. 31: induction/restriction decomposition. Do not present the full categorification conjecture as settled by this paper.
- **0906.3146** — Introduction p. 2: flatness-qualified commuting Frobenius-lift description; section 2.2 p. 8: monoid algebras, toric lifts, mu_n and group-ring base extension. Coordinate-power failure on Heisenberg multiplication is our example, not a universal descent no-go.
- **0806.2401** — Section 3 pp. 6–8: free cyclic sets and cyclotomic tower; section 4.1 equations (30)–(38), pp. 9–10: groupoid algebra/time evolution; Proposition 6.1 and Theorem 6.2, pp. 26–27: F1 endomotive model and realization.
- **0809.1564** — Section 1.10: comparison and homotopical perspectives, stated as perspectives; Definition 2.2 and section 2.3: Habiro completion and root-of-unity Taylor maps; sections 2–3: analytic theory. No quantum-torus Hilbert interpolation theorem is asserted.
- **1405.4527** — Definition 2.1: tropical semiring/topos; Theorems 2.6–2.7: adelic point space and zeta; section 4: Frobenius correspondences. Does not supply the proposed Weyl quantization functor.
- **1901.00020** — Introduction and section map: geometric/categorical lifts, Euler-characteristic and motivic realization comparisons. Used for the existence of this developed categorical route, not a fusion classification.
- **math-0511263** — Introduction and section 1: twisted lattice group algebras and central extensions; section 4: rational normal forms. The simple two-generator central-fibre example is rederived locally.
- **bost-connes-1995** — Section 2 and section 7, p. 32 equation (3), p. 33 Theorem 25: standard Hamiltonian log(n), Gibbs regime and quantum statistical realization. Historical primary paper obtained from the IHES archive.
- **1209.4837** — Introduction pp. 1–2 explicitly distinguishes geometry of Feynman-integral varieties from defining physical Lagrangians/rules over F1; Theorem 4.6, pp. 16–17: positive torification result under its hypotheses.

### Discovery boundary and unresolved comparisons

Search families: direct quantum F1 / absolute quantum theory; monoids,
blueprints, Tits–Weyl, bands and crowds; Hall/groupoid Heisenberg;
cyclotomy/Habiro/quantum tori; lambda Frobenius descent; Bost–Connes and
arithmetic-site dynamics; motivic QFT. Follow-up reads checked definitions,
finite-state scope, and the positive unipotent-radical theorem. The search
is not an exhaustive bibliometric census. No inspected paper supplies one
common functor covering all these quantum outputs. The finite phase model,
UT3 crowd, frame counts and fusion comparisons are local derivations with
separate status labels, not results attributed to these papers.

### Tensor/qubit follow-up: Shimizu

Kenichi Shimizu, *Frobenius–Schur indicators in Tambara–Yamagami categories*,
arXiv:1005.4500v1 (2010). Retrieved 2026-09-06 from
https://arxiv.org/pdf/1005.4500; local `refs/f1/1005.4500/paper.pdf`,
SHA256 `774476ad5ba0e17a5c6e59f720e865827d4bfa10584ab19d72ce50dbb4ad9988`.
Definition 3.1/equation (9), pp. 7–8: Tambara–Yamagami fusion rules;
Table 1 p. 19 and p. 20: Rep(D8) and Rep(Q8) identified with
TY(F2^2, alternating bicharacter, +1/2) and its -1/2 counterpart.
Our exact character calculation independently recovers tensor squares
and second indicators. This is the primary categorical source; simple
labels are not equated with Hilbert-space basis states.

### Adjacent fermionic tensor analogy and title verification

**1307.4522** — Bing-Sheng Lin, Zhi-Xi Wang, Ke Wu and Zi-Feng Yang, *A diagrammatic categorification of the fermion algebra* (2013). Retrieved 2026-09-06
from https://arxiv.org/pdf/1307.4522. Local `refs/f1/1307.4522/paper.pdf`; SHA256
`7448a7257f10a06fbad2f7f3a63f14b045791f8aa96901897b2ed3dcbad42390`. Sections 2–4: one-mode CAR, its diagrammatic categorification and categorical Fock states. The PDF carries a later generated date while its arXiv version and journal publication are 2013. No F1 descent is claimed.

**fermionic-circuits-2018** — Amar Hadzihasanovic, Giovanni de Felice and Kang Feng Ng, *A Diagrammatic Axiomatisation of Fermionic Quantum Circuits* (2018). Retrieved 2026-09-06
from https://drops.dagstuhl.de/storage/00lipics/lipics-vol108-fscd2018/LIPIcs.FSCD.2018.17/LIPIcs.FSCD.2018.17.pdf. Local `refs/f1/fermionic-circuits-2018/paper.pdf`; SHA256
`09e158fa61169c4040ec27c4b91c1c3d3737cbd736d62557c0be40a9573dadea`. Section 2, Definitions 1 and 3, pp. 17:2–17:4: graded Hilbert objects, definite-parity maps and tensor; physical fermionic swap. Section 4: completeness. Used for an adjacent categorical analogy, not as F1 geometry.

**1709.08086** — Amar Hadzihasanovic, *The algebra of entanglement and the geometry of composition* (2017 thesis, v2). Retrieved 2026-09-06
from https://arxiv.org/pdf/1709.08086. Local `refs/f1/1709.08086/paper.pdf`; SHA256
`d25f30d435e563240f540b26b7f04253323c57ae2fca86d227e17503f72824c7`. Consulted discovery pointer: sections on graded/fermionic interpretation of ZW diagrams. This is NOT the 2018 three-author fermionic-circuits paper; the latter was fetched separately from its publisher. No consequential F1 claim relies on the thesis.

## F1 clarification — subsystem composition and quantum operational semantics

Retrieved and inspected 2026-09-07. Each PDF and text extraction is local
under `refs/f1/<id>/`; hashes are of the PDF bytes. This records source
evidence for the conceptual scoping discussion, not new admitted claims.

**2105.06244** — Cole Comfort and Aleks Kissinger, *A Graphical Calculus for Lagrangian Relations* (2021; arXiv v2 2022).
Retrieved from https://arxiv.org/pdf/2105.06244; local `refs/f1/2105.06244/paper.pdf`.
SHA256 `f95e3d90654921fe2c1a66c6fb8e66bea8824d6246176003319cde149c7b8598`.
Definition 4.4: affine Lagrangian relation category and direct-sum tensor; Definition 4.14 and Theorem 4.16: odd-prime stabilizer process category modulo invertible scalars. Empty relation corresponds to zero. This quotient is not a complete normalized probabilistic semantics.

**2304.10584** — Cole Comfort, *The Algebra for Stabilizer Codes* (2023).
Retrieved from https://arxiv.org/pdf/2304.10584; local `refs/f1/2304.10584/paper.pdf`.
SHA256 `cfa0bcf6efe6873ae0e63bb9a15a6c1e08eab02bc4270d1cbf5c1fc63322c57c`.
Section 4, especially Theorems 4.2 and 4.5 and discussion of discarding: symplectic dilation and coisotropic semantics for the stated mixed stabilizer fragment. Does not identify every CP map with a relation.

**0705.4556** — Shamgar Gurevich and Ronny Hadani, *Quantization of symplectic vector spaces over finite fields* (2007; published 2009).
Retrieved from https://arxiv.org/pdf/0705.4556; local `refs/f1/0705.4556/paper.pdf`.
SHA256 `a55fa0ded9c36ec964ff973e7d0ea5c632624c28bf9fbbf9be0db11de921fbb3`.
Proposition 2.6.2: quantization functor on odd-characteristic symplectic isomorphisms; Proposition 2.7.1: monoidal product comparison; Proposition 2.7.5: isotropic reduction. Phase datum and source conventions are explicit; no characteristic-two theorem is imported.

**0707.4206** — Parsa Bonderson, Kirill Shtengel and J. K. Slingerland, *Interferometry of non-Abelian Anyons* (2007; published 2008).
Retrieved from https://arxiv.org/pdf/0707.4206; local `refs/f1/0707.4206/paper.pdf`.
SHA256 `969f3954785d88d88b2a2590298a42e5a9ff01ce00e6b843c3d9a87cea66aec2`.
Section 2: fusion spaces, ordinary/quantum traces and partial traces, density matrices and measurement formalism. Quantum-trace weights must be retained when comparing charge sectors; fixed-sector Hilbert densities use corresponding normalization.

**2211.03855** — Fatimah Rita Ahmadi and Aleks Kissinger, *The ZX-calculus as a Language for Topological Quantum Computation* (arXiv v3, 2023).
Retrieved from https://arxiv.org/pdf/2211.03855; local `refs/f1/2211.03855/paper.pdf`.
SHA256 `6cce2037f13baa7a8ec0af42c6ce17b58a344c0bbd02ec7d35505e0803051948`.
Sections on fusion categories, their Hilbert-space enrichment, and Fibonacci/Ising encodings and braiding. Title verified from v3: older pointers use Topological Quantum Computation Through the Lens of Categorical Quantum Mechanics. Hilbert enrichment of Hom spaces is not a strong monoidal fibre functor on the anyon objects.

## F1 operational increment — Hecke contexts, CP nets and exact specialization

Retrieved and inspected 2026-09-07. All entries below have local PDF,
text/OCR navigation data and retrieval.json under `refs/f1/<key>/`.
The proof, not finite checks, supports the general q>0 assertions.

**iwahori-1964** — Nagayoshi Iwahori, *On the structure of a Hecke ring of a Chevalley group over a finite field* (1964).
Route: https://repository.dl.itc.u-tokyo.ac.jp/record/39909/files/jfs100207.pdf. Local `refs/f1/iwahori-1964/paper.pdf`;
SHA256 `27efc0216ba5b152d4d4a411239cf66793ad93a4a05490f64c03f7101afc9a96`.
p. 215: flag permutation commutant; Proposition 1.4/Corollary 1.5 pp. 220–221: commutant and opposite convention; Theorem 2.6: reduced-word moves; Lemma 3.1 pp. 230–231: Bruhat basis and q^length; Theorems 3.2 and 4.1 pp. 231–234: multiplication and presentation. The PDF is a scan; OCR and primary-extracts.tex are navigation derivatives, not replacement sources.

**umegaki-1954** — Hisaharu Umegaki, *Conditional expectation in an operator algebra* (1954).
Route: https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_177/_pdf/-char/en. Local `refs/f1/umegaki-1954/paper.pdf`;
SHA256 `870e524af7fa7c7e6e99a11aaab413eca83704d903e3148ab83ef7ce448b0a21`.
Section 2, pp. 177–179: trace-pairing characterization, positive faithful conditional expectation, bimodule and Schwarz properties. Complete positivity is rederived by matrix amplification locally, not attributed to terminology absent from this paper.

**stinespring-1955** — W. Forrest Stinespring, *Positive functions on C*-algebras* (1955).
Route: https://www.ams.org/journals/proc/1955-006-02/S0002-9939-1955-0069403-4/S0002-9939-1955-0069403-4.pdf. Local `refs/f1/stinespring-1955/paper.pdf`;
SHA256 `cff456fa4c19c224b27b41117b894a047377123b5d37f4fc8545e2483ea54991`.
p. 211 section 2: matrix complete positivity; Theorem 1 pp. 212–213: dilation; Theorem 3 p. 215: positive functionals are CP. Used for operational meaning, not a claim that every isolated channel canonically extends to new fusion observables.

**curtis-1988** — Charles W. Curtis, *Representations of Hecke algebras* (1988).
Route: https://www.numdam.org/article/AST_1988__168__13_0.pdf. Local `refs/f1/curtis-1988/paper.pdf`;
SHA256 `44809fc53e1e09de0601437a4e44e37152128ab8b4f4ff495b4621b8fc704714`.
Sections on the standard basis, finite groups with a BN-pair and parabolic subalgebras. Supporting source for the type-A flag/Hecke and type-C comparison; local proofs carry the new subsystem-overlap and context claims.

**goodman-wenzl-1993** — Frederick M. Goodman and Hans Wenzl, *The Temperley-Lieb algebra at roots of unity* (1993).
Route: https://msp.org/pjm/1993/161-2/pjm-v161-n2-p05-p.pdf. Local `refs/f1/goodman-wenzl-1993/paper.pdf`;
SHA256 `e7d4a6036b9e1633f3afaf17eddb3d16a163a25df0bfa4d757648831fd2c19fa`.
Introduction pp. 307–309 and presentation/parameter conventions: Hecke quotient idempotents have adjacent coefficient q/(1+q)^2. The q=1 positive real endpoint and root-of-unity quotients are different constructions; the faithful flag trace does not descend through a nonzero ideal.

**math-0002087** — Joseph Bernstein, Igor Frenkel and Mikhail Khovanov, *A Categorification of the Temperley-Lieb Algebra and Schur Quotients of U(sl2) via Projective and Zuckerman Functors* (published 1999; arXiv 2000).
Route: https://arxiv.org/pdf/math/0002087. Local `refs/f1/math-0002087/paper.pdf`;
SHA256 `ec0ec4a078c256056458cbc4c97b5ad517b951c573604815d586f66951783569`.
Section 2.2 pp. 6–8: sl2 tensor-power centralizer/Temperley-Lieb interpretation. We use the endomorphism tower statement; a full rigid-category equivalence would need separately specified cups/caps and pivotal conventions.

**0804.4304** — Louis H. Kauffman and Samuel J. Lomonaco Jr., *The Fibonacci Model and the Temperley-Lieb Algebra* (2008).
Route: https://arxiv.org/pdf/0804.4304. Local `refs/f1/0804.4304/paper.pdf`;
SHA256 `188600fd04327e34dcbd603eccbdec78cfd03b1b248ac5b62144c04933305358`.
Sections constructing the Fibonacci recoupling model, golden ratio and root-of-unity loop parameter. This is an independently supplied quotient/trace construction, not the q=1 real Hecke family.

**1707.01196** — Kenji Iohara, Gustav I. Lehrer and Ruibin B. Zhang, *Temperley-Lieb at roots of unity, a fusion category and the Jones quotient* (2017).
Route: https://arxiv.org/pdf/1707.01196. Local `refs/f1/1707.01196/paper.pdf`;
SHA256 `f3a6f25dc59047dd38fa1a92107da96cb8c012dbca7bae88beeb76725bde29f3`.
Jones quotient and reduced fusion rules at roots of unity; at order-five data the even Fibonacci fusion rule is a separate specialization. Positive Markov/Jones trace and appropriate star structure are additional to the canonical real flag trace.

**1611.04620** — Corey Jones and David Penneys, *Operator algebras in rigid C*-tensor categories* (2016 preprint; published 2017).
Route: https://arxiv.org/pdf/1611.04620. Local `refs/f1/1611.04620/paper.pdf`;
SHA256 `9ee71c611eb66032931ebe3131cb7c6007bf0f88d34fa70d3aa5f9f572768287`.
Section 4.1 and Definition 4.20: conditional expectations and CP/ucp natural transformations on internal algebra objects; Lemma 4.27 and Theorem 4.28: categorical Stinespring; Definitions 4.29/4.32: states/traces. Their internal Vec(C) algebra objects are not silently identified with our object-indexed End_C(X) net.

### Additional locators in already registered sources

- **0707.4206** — section 2.4, equations (2.19)–(2.29): quantum traces;
  section 2.5, equations (2.30)–(2.33): braiding/removal paths; equations
  (2.43)–(2.45): density matrices with quantum-trace normalization.
- **2211.03855** — section III.A.2, equations (39)–(42): exact Fibonacci
  F/R data used in the supporting two- versus three-anyon channel witness.
- **1204.5395** — Definition 6, p. 8: normal F1 maps; deleting the basepoint
  identifies these with the partial injections in the q=1 operational functor.

### What is derived here

The intrinsic overlapping-subalgebra invariant q/(q+1)^2, the exact
Kraus-Gram operational quotient and sharp 2n-1 context bound, and the
partial-injection CP realization are local structured derivations. No
literature-novelty claim is made. The finite-field source proves a flag
context sector; it does not identify this with the full Weyl Hilbert space.
The partial-flag corner category is explicitly constructed over a localized
coefficient ring; no unspecified generic-category existence is assumed.

## Operational categorical limit — sources retrieved 2026-09-07

Primary PDFs and text navigation copies are local under `refs/f1/<key>/`.
Titles were checked against the PDF front pages. Each directory includes
`retrieval.json`; source bodies remain ignored and are not redistributed.

**1008.3739** — Alexei Davydov and Alexander Molev, *A categorical approach
to classical and quantum Schur–Weyl duality*.
Route: https://arxiv.org/pdf/1008.3739. Local `refs/f1/1008.3739/paper.pdf`;
SHA256 `414b0e84b16eb40b89b6bfa4fe36ceab37a3f1f554b0f5dc594a82efc972f28e`.
Section 2.1, pp. 5–7 and equation (2.1): multiplicative sequences, their
graded categories, and induction/Day tensor on right modules. Theorem 2.4:
presentations. Theorem 3.2 and Proposition 3.3, p. 12: universal symmetric
category. Proposition 3.4, p. 13: Schur–Weyl functor. Theorem 4.5 and
Proposition 4.6, p. 15: Hecke category and algebraic braiding. Proposition
4.7: quantum Schur–Weyl. The source's generator has eigenvalues v,-v^-1;
our convention is q=v^2 and T=v t. Algebraic braiding does not assert
unitarity for the project's positive real star structure.

**0707.2248** — Joel Kamnitzer and Peter Tingley, *The crystal commutor and
Drinfeld's unitarized R-matrix*.
Route: https://arxiv.org/pdf/0707.2248. Local `refs/f1/0707.2248/paper.pdf`;
SHA256 `a7af29cf268a9d2101b950712317f6fe0065144beac3959499e956f5043c5f48`.
The quantum-group commutor and coboundary comparison provide a lead for
physical exchange coherence; applying them to the abstract traced Hecke
tower requires a separate proof and matching conventions.

**math-0406478** — André Henriques and Joel Kamnitzer, *Crystals and
coboundary categories*.
Route: https://arxiv.org/pdf/math/0406478. Local
`refs/f1/math-0406478/paper.pdf`;
SHA256 `d90f2277709c09f697daf6ce4f71817cca5659752c1c31fca1ebe605b53833eb`.
Section 3: coboundary categories, commutors and cactus-group coherence.
The source concerns its specified crystal/representation settings; a
Hecke C*-category application must be derived explicitly.

**1310.3878** — Daniele Rosso, *The mirabolic Hecke algebra*.
Route: https://arxiv.org/pdf/1310.3878. Local `refs/f1/1310.3878/paper.pdf`;
SHA256 `82cf0f2287bc74b51a03b049174d29c520174191c8845fa894a04d1c8a02a6ea`.
Section 3, p. 5, equation (6): convolution on two flags and a vector;
Definition 3.2: polynomial-parameter algebra; Remarks 3.3–3.4: Hecke
subalgebra and anti-involution. Section 3.1, pp. 5–6: affine-group double
cosets. Section 4.3: cyclotomic quotient and presentation; Section 5:
comparison with q-rook algebras. Abstract semisimple algebra isomorphism
does not by itself identify the physical trace, star, or assembly maps.

## Frobenius and arithmetic hierarchy — retrieved 2026-09-08

The following source bodies are local under `refs/frobenius-hierarchy/` and
remain ignored. Titles/authors were checked against arXiv metadata and PDF
front pages, or the Stacks section heading. Each source has `retrieval.json`.

**1608.06596 (CGK17)** — Shawn X. Cui, Daniel Gottesman and Anirudh Krishna,
*Diagonal gates in the Clifford hierarchy*, Phys. Rev. A 95, 012329 (2017).
Route: https://arxiv.org/pdf/1608.06596, v1.
Local `refs/frobenius-hierarchy/1608.06596/paper.pdf`;
SHA256 `54cf35d7073a613c0a543bc58c2920b1abf447d32e0218f83fc5fa617e6a911a`.
Section II, printed p. 2, equations (3)--(7): Pauli group and hierarchy
conventions, and conjugation of translations by diagonal gates. Theorem 1
on p. 2: diagonal elements at a fixed hierarchy level form a group, while
the full higher levels are not groups. Section IV, Theorem 3 on p. 6:
multiqudit diagonal classification with weight `(p-1)(m-1)+sum a_i`.
The source includes p=2; its phase precision must not be suppressed when
using its classification. The arithmetic multilinear trace-phase and
multiplication-accumulator family is derived internally in this campaign.

**2212.05398 (AND24)** — Jonas T. Anderson,
*On Groups in the Qubit Clifford Hierarchy*, Quantum 8, 1370 (2024).
Route: https://arxiv.org/pdf/2212.05398, v2, 7 June 2024.
Local `refs/frobenius-hierarchy/2212.05398/paper.pdf`;
SHA256 `ddb7c55c3d208812926a20b3562d968711fedf43717bc240b2ca6234f1f6d122`.
Section 1, pp. 1--3: hierarchy and group-closure distinctions. This is a
qubit source. Its classification concerns the stated semi-Clifford and
generalized semi-Clifford scope, not all gates or all prime characteristics.
It motivates recording levels on generators rather than claiming that a
fixed higher hierarchy level supplies a composition-closed morphism class.

**Stacks 0BIE (ST-TRACE)** — The Stacks Project Authors,
*Fields*, Section 9.20, "Trace and norm".
Route: https://stacks.math.columbia.edu/tag/0BIE.
Local `refs/frobenius-hierarchy/stacks-0BIE/source.html`;
SHA256 `1fe21ce54aba4cebd3afe798c443a0544a3734e761a6dc4dce3f6322a0931213`.
Definition 9.20.1 (0BIF): trace/norm as trace/determinant of multiplication.
Lemma 9.20.5 (0BIJ): transitivity along finite field towers.
Definition 9.20.6 (0BIK): trace pairing.
Lemma 9.20.7 (0BIL): finite separability is equivalent to nonzero trace and
to nondegeneracy of the trace pairing; the proof explicitly notes that a
nonzero field-linear trace is surjective. Applied to finite fields, this
does not require the extension degree to be invertible in the base field.

**1303.5141 (HW13)** — Guy Henniart and Chun-Hui Wang,
*Weil representations over finite fields and Shintani lift*.
Route: https://arxiv.org/pdf/1303.5141, v1.
Local `refs/frobenius-hierarchy/1303.5141/paper.pdf`;
SHA256 `fb19867e189f9fa96ade5811a440af50a68ab440ee16efb0d203dc6fcdc63055`.
Theorem 4.1, p. 3: extension to the Galois semidirect product and the
Frobenius-twisted character identity using the stated Shintani/Gyoja norm.
Proposition 6.1, p. 5: compatibility with orthogonal symplectic decomposition.
The source assumes odd field cardinality. Its norm is a construction on
twisted conjugacy classes; it is not an arbitrary raw nonabelian product,
nor does the theorem supply a CP channel or a characteristic-two extension.

**quant-ph/0605054 (VOU06)** — A. Vourdas,
*The Frobenius formalism in Galois quantum systems*.
Route: https://arxiv.org/pdf/quant-ph/0605054, v1.
Local `refs/frobenius-hierarchy/quant-ph-0605054/paper.pdf`;
SHA256 `74346977ddf2e99fd882735955d95e036fcc9ee2b04646c9e14a0151cdd8dbcb`.
Section 4.1, pp. 8--9, equations (39)--(44): tensor coordinates, trace
Fourier kernel, and the distinct dual coordinates for momentum.
Sections 5.2--5.3: Frobenius orbit subspaces and unitary transformations.
The author's framework assumes odd p. The current all-characteristic
reference-Weyl formulas and field-transfer statements are proved internally;
this source is a comparison, not their characteristic-two justification.

## Frobenius orbit boundary — retrieved 2026-09-08

**1811.08601v2 (HY21)** — Trevor Hyde, *Cyclotomic factors of necklace
polynomials*. Title and author verified on the arXiv abstract page and PDF.
Route: https://arxiv.org/pdf/1811.08601v2 (revised 18 January 2021).
Local `refs/frobenius-boundary/1811.08601/paper.pdf`, with text extraction;
SHA256 `b2ab01f64b5261e9251f64d460f9a4c6de7c2e1a8b66ad7431552036fa5a66b1`.
Introduction, printed p. 1: necklace polynomial formula and its count of
degree-d monic irreducibles over a finite field. Our c_d is d times this
polynomial. The positive trace continuation and matrix-algebra construction
are local derivations, not results attributed to Hyde.

**YOSHIDA14** — Tomoyuki Yoshida, *The Burnside ring and the universal zeta
function of finite dynamical systems*. Title/author verified on PDF p. 1;
RIMS Kokyuroku 1872 (2014), pp. 122--131 (talk dated 9 January 2013).
Route: https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1872-13.pdf.
Local `refs/frobenius-boundary/yoshida-2014/paper.pdf`, with text extraction;
SHA256 `068e646e9fdedf5355278baaee775075be9b2deb0bf6ba2b0cae83fa0c6a7150`.
Section 2.2, printed p. 127: cycle-set multiplication by gcd/lcm in the
necklace algebra. Only that formula is used as comparison; the coherent
quantum multiplicity algebra and conditional trace are derived locally.

## General Galois and mixed-limit round — retrieved 2026-09-09

**STACKS-04JI** — The Stacks Project, *Schemes etale over a point*,
Section 58.2, title checked on the source page.
Route: https://stacks.math.columbia.edu/tag/04JI.
Local `refs/arithmetic-limits/stacks-04JI/source.html`;
SHA256 `1432489ebf2eb3912c170502f1fca4a63e00e6b9e95d2b37162cf8bff9508507`.
Lemma 58.2.2 (03QR): etale K-schemes and continuous absolute-Galois sets;
its explicit construction by embedding sets restricts to the finite objects.
Variance is contravariant when expressed in terms of K-algebras.

**STACKS-0BMI** — The Stacks Project, *Infinite Galois theory*, Section 9.22,
title checked on the source page.
Route: https://stacks.math.columbia.edu/tag/0BMI.
Local `refs/arithmetic-limits/stacks-0BMI/source.html`;
SHA256 `c52b47023edefc748584719222b70b537778eb6115c49ca1fd7351def9260b50`.
Lemma 9.22.1 (0BMJ): profiniteness. Lemma 9.22.2 (0BMK): surjective
restriction in Galois towers. Lemma 9.22.3: inverse limit over finite
Galois subextensions. Theorem 9.22.4 (0BML): closed/open/normal subgroup
correspondence, including arbitrary infinite Galois extensions.

**MILNE-FT-5.10** — J. S. Milne, *Fields and Galois Theory*, version 5.10,
September 2022. Title, author and version verified on PDF cover.
Route: https://jmilne.org/math/CourseNotes/FT.pdf.
Local `refs/arithmetic-limits/milne-FT/FT.pdf` and `FT.txt`;
SHA256 `5c43ea0bf4ec190b819727fe720414a80e09f9e762533d08bad5b8a0b6de7273`.
Theorem 8.21, printed p. 111: contravariant equivalence of finite etale
algebras with finite continuous Galois sets. The quantum fibre normalization,
CP instruments and conditional-limit statements are local derivations,
not assertions attributed to this source.
Additional exact locators used by the general Galois proof: Theorem 6.10
(existence/comparison of separable closures); Proposition 8.6, Corollary 8.7,
Proposition 8.9 and Corollary 8.10 (splitting, tensor and compositum facts);
Proposition 8.20 (full faithfulness of embedding sets); Remark 3.18,
printed p. 40 (normal core/normal closure); Propositions 4.19--4.20,
Corollary 4.21 and Proposition 4.23, printed pp. 53--54 (primitive
elements, finite fields, Frobenius and their subfields).

## Composite degree spectrum — 2026-09-09

**DLMF-27.4-E6** — NIST Digital Library of Mathematical Functions,
Section 27.4, *Euler Products and Dirichlet Series*, equation 27.4.6.
Section title, equation and version 1.2.7 (2026-06-15) verified from the
retrieved official page. Routes: https://dlmf.nist.gov/27.4 and
https://dlmf.nist.gov/27.4.E6.tex. Local bodies:
`refs/composite-spectrum/dlmf-27-4/source.html`, SHA256
`f89c9c55ae27caf5de5ac04c1725a021f537ef2763ad532bafc109fcb66c3ed0`,
and `27.4.E6.tex`, SHA256
`db6ca88fa941b66a791e30f85c1fe2a81dd0e6463488eb1fa4ad763556504f50`.
The equation states the classical totient Dirichlet series
sum phi(n)n^(-z)=zeta(z-1)/zeta(z) for Re z>2. Used as corroboration
for the independently derived real-domain identity at z=beta+1 in
CMP-MELLIN; the c0 quantum completion, its Frobenius automorphism and
the selection of the degree weights/regulator are not attributed to DLMF.

## Symplectic Phantasm — source-first bootstrap, 2026-09-09

The active quest is **The Hunting of the Symplectic Phantasm**. All bodies
below were fetched afresh from primary-source repositories, author sites,
or the named researcher-hosted preprint copy, not copied from `v0.1/`.
The retrieval script is `scripts/fetch-phantasm-sources.py`; local retrieval
JSON records preserve attempted and final URLs, time, format and file lists.
Raw hashes pin the actual retrieved bytes; source revisions require a new
inspection and ledger update. Third-party bodies remain git-ignored.

The source audit and full inventory of guidance-note leads are in
`docs/research-plans/symplectic-phantasm-sources.md`. LOCALLY VERIFIED means
the title and stated locators were inspected, not that all arguments in the
source were independently proved. GAP sources cannot support a DAG node.

<!-- PHANTASM-SOURCES-BEGIN -->
| source-id | availability | body | sha256 | readable-body | readable-sha256 |
|---|---|---|---|---|---|
| SP-GH07 | LOCAL | refs/symplectic-phantasm/SP-GH07/raw | 944cb30bde457137ca9604afc6ad44891ec3ac6cfe7994f45899754624a10f6d | refs/symplectic-phantasm/SP-GH07/source.tex | 68f135ec90d5c99347379a47d3ebdbc509ba434c68e214a08091647fd2c91362 |
| SP-GH09 | LOCAL | refs/symplectic-phantasm/SP-GH09/raw | 361310f8499da0bf1645b152ac8dfa432f52adc5d90d76abea9a21d5d693e1d6 | refs/symplectic-phantasm/SP-GH09/gurevich_hadani_4.tex | 96ee6a2de181d467cb5b04fe82f6207d9baa385d048011f163a44bfe4a4dd1eb |
| SP-W09 | LOCAL | refs/symplectic-phantasm/SP-W09/raw | ba2577e7f535a5c2fda42172e6a7f1334e1c2e6284dc79c6d7d2fa0f40f7f7a0 | refs/symplectic-phantasm/SP-W09/source.tex | 32231205137c1ea8f689d9b94a496c71ed8e0c903c392bb2a384406c11d268ef |
| SP-LW14 | LOCAL | refs/symplectic-phantasm/SP-LW14/raw | 7938ee52af059c4e8fb3e5840a29c75351814b1ab07c42aca67bc5b96875fb5d | refs/symplectic-phantasm/SP-LW14/sigma14-100.tex | eaea7876cbbc716728605b76deb654037eb4c08e7316e6f9c81276fa8c9e3d62 |
| SP-GROSS06 | LOCAL | refs/symplectic-phantasm/SP-GROSS06/raw | 1c5371144c5b8b58fb6a8272546fdee54de0045e7dad3c9135a507d987ca9dfe | refs/symplectic-phantasm/SP-GROSS06/poswig.tex | 31684a5e30c3f1f2d35ad23a31afef1712a9af4b2d5f96b0691d98788b7465a9 |
| SP-CK21 | LOCAL | refs/symplectic-phantasm/SP-CK21/raw | b519f4d757d1ddd002f815c9b4ac250b015571203cb8b2dbcebb32ad70a83a61 | refs/symplectic-phantasm/SP-CK21/lagrel.tex | 9a6c3cf2d21d105dda496bde29bfb71fda92b256f4aee3701ed1c392abba7b9a |
| SP-BC24 | LOCAL | refs/symplectic-phantasm/SP-BC24/raw | ae976f4a981047502cc339da064b9f4f715f4173a52910cb50bcae851cc35041 | refs/symplectic-phantasm/SP-BC24/main.tex | 1d463ecb073cf69a0c7337c7fbf8eed834ed9c21b4a5dac23eee0b4a136fda4b |
| SP-CGK17 | LOCAL | refs/symplectic-phantasm/SP-CGK17/raw | 37fb2f9497d056790e1ee92b25cd53dd85e2a566fd4d60d830aca9790a79c947 | refs/symplectic-phantasm/SP-CGK17/diagonalCliffordGates5.tex | 5f9c0df276e9a65a376470dc175db60c3dd5b8666ee66d59b0546e271bdcff4e |
| SP-SOULE04 | LOCAL | refs/symplectic-phantasm/SP-SOULE04/raw | f5c8ab62f082e45e2c06429dc4cb2cf4e554d7b2f240ff7a87410371195c75ab | refs/symplectic-phantasm/SP-SOULE04/source.tex | c3be252917902fbfa7447ec8ea5a64cfcf26248f8b37ff4d4a54d54c3e1b67c3 |
| SP-DEITMAR05 | LOCAL | refs/symplectic-phantasm/SP-DEITMAR05/raw | b61f5a5c88f224fa3d8c56120bcfcd7ba02eec58bec1da5e857f47b83b96ae09 | refs/symplectic-phantasm/SP-DEITMAR05/paper.txt | c3aaaa5e05ba552b5a3c073947b9d7636e14e43619f6a53d800a6bf4eae0c464 |
| SP-CC09 | LOCAL | refs/symplectic-phantasm/SP-CC09/raw | f09e4f8a917de991a84b508023598259e9d79694425ce5bd1ddd33d7c729e53f | refs/symplectic-phantasm/SP-CC09/announc3.tex | 8254a72d27b082e0a3550e6be9398bae1c7e267303dc2b86a904703f58569fd4 |
| SP-CC10 | LOCAL | refs/symplectic-phantasm/SP-CC10/raw | 873e37d692da714fff8ba0dea8a6ad2f0de4e1c48b9fbb686b45a2696d90d970 | refs/symplectic-phantasm/SP-CC10/Jamifine.tex | 4ba6cfeb554fd9954204a6e205e3230c6a5124713bbd0e71bd9d9fa44db01acd |
| SP-PRASAD09 | LOCAL | refs/symplectic-phantasm/SP-PRASAD09/raw | acea15774d71e3697f1828fcea0d4aabe3bdf51dac07700af50e3099359068e3 | refs/symplectic-phantasm/SP-PRASAD09/source.tex | e1950f55045d67961243a3d490de07ee929b241c6436da2e40160ab28c844418 |
| SP-GH08 | LOCAL | refs/symplectic-phantasm/SP-GH08/raw | 50fe23420c57f444349d521d53be3315416642f4760373b1f67410ca08bf1b84 | refs/symplectic-phantasm/SP-GH08/source.tex | 4b5b7ff9fb9a90fb17c02d4cc6fdfccedea36129042e1ba2e291d51df3117b23 |
| SP-BCL22 | LOCAL | refs/symplectic-phantasm/SP-BCL22/raw | 119a4db85def25894a36e34f8b7ad20701558c77a00f9274d5a77febe8b39e18 | refs/symplectic-phantasm/SP-BCL22/source.tex | d2fc4a2bc61fe27f433e174dd0e19114edd16f6ebfce162207e1cc083559b18c |
| SP-DER06 | LOCAL | refs/symplectic-phantasm/SP-DER06/raw | 739bee04644cdd516bb56b011803e845ebce4a7064c6ae6bbb90d7618d6e7c29 | refs/symplectic-phantasm/SP-DER06/derezinski.tex | eed86b49de5f88e89fde1d936c78d61e0ecd3f6d0bfd5ab5e19ce5eda9185f4b |
| SP-CCM07 | LOCAL | refs/symplectic-phantasm/SP-CCM07/raw | 564594d05e3a44203e073a80587965b2524bd0bac7489205ba3e883b36fe9b5d | refs/symplectic-phantasm/SP-CCM07/ncgandmotivesMarch8.tex | 6259952d5aac11f0c9d10eb254c96d18748818b73cd25838ea890d43f49bc9f3 |
| SP-CM04 | LOCAL | refs/symplectic-phantasm/SP-CM04/raw | 94dc934d5f7b11932f5d3486be2f11481f8f13d7e93df37eaeb9d2541db16a9b | refs/symplectic-phantasm/SP-CM04/houcheschapter1final7.tex | ce87e34046d5dee45d8ca604276c8d70b5bdf4b571767f0ff84a4801ec089038 |
| SP-BC95 | LOCAL | refs/symplectic-phantasm/SP-BC95/raw | 376e00d06bef1be27769f0f1c186010a6e6ad354608c3a273b0b3ae6479c1815 | refs/symplectic-phantasm/SP-BC95/paper.pdf | 376e00d06bef1be27769f0f1c186010a6e6ad354608c3a273b0b3ae6479c1815 |
| SP-CM08 | LOCAL | refs/symplectic-phantasm/SP-CM08/raw | 4154ad00fad638e06746f11cd476adb00d186d30cee11e9f531fd21c45aa71f7 | refs/symplectic-phantasm/SP-CM08/paper.txt | b2059a822f31afcf848cea369da3f3f4b1b7c3175495954adbea2ee7c5cc3db1 |
| SP-WAT18 | LOCAL | refs/symplectic-phantasm/SP-WAT18/raw | c8f30116586435fc265273b09ca2d63f4912a5d4b8901db1ada84b03373c6325 | refs/symplectic-phantasm/SP-WAT18/paper.txt | c0a99af6eafd2dd4e3acc9556560d2c9b6680e0ceb509cd1b7a92942fb3cb10e |
| SP-STFIELD | LOCAL | refs/symplectic-phantasm/SP-STFIELD/raw | 87e07f0373dc60cfc284e2f19078bc9bc7ab0b89c40eef83941f6c38c765c549 | refs/symplectic-phantasm/SP-STFIELD/source.tex | 87e07f0373dc60cfc284e2f19078bc9bc7ab0b89c40eef83941f6c38c765c549 |
| SP-SPECTOR98 | LOCAL | refs/symplectic-phantasm/SP-SPECTOR98/raw | d1ad2c8753b637f7fbe03b233511d7ec4aeb766d6d26a75b89c1833c2f068ab7 | refs/symplectic-phantasm/SP-SPECTOR98/source.tex | 6eb5f5b456b4c4deee3385e9dc343ad3304782671d652e9f34c56207598e58d2 |
| SP-KS95 | LOCAL | refs/symplectic-phantasm/SP-KS95/raw | 213f2e3b274dad06416d077e68de162ee71135cbb46ed8188debcde30754145b | refs/symplectic-phantasm/SP-KS95/paper.pdf | 213f2e3b274dad06416d077e68de162ee71135cbb46ed8188debcde30754145b |
| SP-JOY81 | LOCAL | refs/symplectic-phantasm/SP-JOY81/raw | f4dc51a9b1d0befce4621eee0876cb045bde2d7cb2f2b6c8f108cb779d6fdb3a | refs/symplectic-phantasm/SP-JOY81/paper.txt | fa291a88feb142965a57731e51f8dc6147f3d38af18c87141af465a12b86dd3b |
<!-- PHANTASM-SOURCES-END -->

### SP-GH07

**Shamgar Gurevich and Ronny Hadani**, *Quantization of symplectic vector spaces over finite fields*.

Route: https://arxiv.org/e-print/0705.4556 (TeX); final URL: https://arxiv.org/src/0705.4556.

Local readable body: `refs/symplectic-phantasm/SP-GH07/source.tex`.

Verified locators: title/authors lines 50–59; §0.1; Proposition labelled functor_prop at lines 961–966; §2.4, reduction_prop at 1098.

Scope: Odd characteristic; the canonical Hilbert/vector functor uses a fixed character and oriented models. Its convention is contravariant. Monoidality and oriented isotropic reduction do not themselves state a probability-preserving functor on all relations.

### SP-GH09

**Shamgar Gurevich and Ronny Hadani**, *Notes on Canonical Quantization of Symplectic Vector Spaces over Finite Fields*.

Route: https://arxiv.org/e-print/0708.0669 (TeX archive); final URL: https://arxiv.org/src/0708.0669.

Local readable body: `refs/symplectic-phantasm/SP-GH09/gurevich_hadani_4.tex`.

Verified locators: title/authors lines 38–42; §1.1 and §§2–3.

Scope: Companion exposition; the downloaded TeX title includes Canonical, unlike the arXiv abstract-page title. Keep orientation, character and variance conventions explicit.

### SP-W09

**Alan Weinstein**, *Symplectic categories*.

Route: https://arxiv.org/e-print/0911.4133 (TeX); final URL: https://arxiv.org/src/0911.4133.

Local readable body: `refs/symplectic-phantasm/SP-W09/source.tex`.

Verified locators: title/authors lines 108–113; §2, Relations and their composition; §2.1, The linear case, lines 421–470.

Scope: Definitions and reduction factorization for canonical relations. The smooth transversality issue is distinct from finite linear relational composition. Does not supply a finite-field probability normalization.

### SP-LW14

**David Li-Bland and Alan Weinstein**, *Selective Categories and Linear Canonical Relations*.

Route: https://arxiv.org/e-print/1401.7302 (TeX archive); final URL: https://arxiv.org/src/1401.7302.

Local readable body: `refs/symplectic-phantasm/SP-LW14/sigma14-100.tex`.

Verified locators: title/authors lines 79–88; §§2,4,7; linear hypercanonical relations, local lines 1571–1581, opposite-form dual and diagonal unit/counit (inspected 2026-09-10).

Scope: Indexed linear relations retain an excess integer. The ordinary linear-relation convention uses the opposite symplectic form and diagonal duality data; source arrow and factor orders must be matched explicitly. Source for keeping composition data visible, not a theorem identifying all quantum channels with Lagrangian relations.

### SP-GROSS06

**D. Gross**, *Hudson’s Theorem for finite-dimensional quantum systems*.

Route: https://arxiv.org/e-print/quant-ph/0602001 (TeX archive); final URL: https://arxiv.org/src/quant-ph/0602001.

Local readable body: `refs/symplectic-phantasm/SP-GROSS06/poswig.tex`.

Verified locators: title/authors lines 60--62; abstract lines 78--90; Weyl convention and grouped phase-space coordinates lines 340--420; Clifford definition lines 458--466; theorem `thCliffordStructure` lines 504--537; discrete Hudson theorem `thMain` lines 202--214.

Scope: Odd-dimensional cyclic configuration spaces, with a specified Weyl/phase-space convention. The Clifford structure theorem gives projective symplectic implementers and the Weyl-times-symplectic decomposition of Clifford unitaries. It does not construct the category generated by stabilizer preparations/effects, its scalar quotient or a dagger equivalence, and it does not classify every possible quantization of nonlinear maps.

### SP-CK21

**Cole Comfort and Aleks Kissinger**, *A Graphical Calculus for Lagrangian Relations*.

Route: https://arxiv.org/e-print/2105.06244 (TeX archive); final URL: https://arxiv.org/src/2105.06244.

Local readable body: `refs/symplectic-phantasm/SP-CK21/lagrel.tex`.

Verified locators: title/authors lines 276--279; standard form, row-space convention and Lagrangian relation definition lines 1712--1762; tensor regrouping and strong monoidality lines 1807--1820; compact currying lines 1860--1940; symplectic generator matrices/right actions lines 2299--2419; possibly-empty affine relations lines 2921--2929 and affine Lagrangian presentation lines 3096--3123; stabilizer and scalar-quotient definition lines 3611--3649; generator/state map lines 3652--3701; theorem `theorem:spekkens` lines 3703--3744.

Scope: The affine-Lagrangian/stabilizer comparison is for odd prime dimensions and modulo invertible complex scalars. The stated theorem is a symmetric monoidal equivalence; it does not state dagger preservation. The source uses row/right-action matrices, a strong tensor regrouping and a cap-based currying construction, so matching D1702's signed Hom-sets, bare converse dagger, affine sign and D1703's Weyl/Fourier conventions is an explicit local comparison. The quotient does not retain norm, probability or normalized instrument semantics; extension fields require a separate theorem.

### SP-BC24

**Robert I. Booth, Titouan Carette and Cole Comfort**, *Graphical Symplectic Algebra*.

Route: https://arxiv.org/e-print/2401.07914 (TeX archive); final URL: https://arxiv.org/src/2401.07914.

Local readable body: `refs/symplectic-phantasm/SP-BC24/main.tex`.

Verified locators: title/authors in `main.tex` lines 29--34; interleaved `(z,x)` coordinates in `section_AffLagRel.tex` lines 21--39; signed affine Lagrangian Hom-sets, relational composition, identity, compact cup/cap and time-reversal dagger lines 105--189; explicit generator semantics and dagger functor lines 207--345; zero normal form and dagger-compact prop isomorphism lines 389--402 and 568--579; stabilizer application in `section_Applications.tex` lines 140--174.

Scope: Primary follow-up giving a precise signed, dagger-compact presentation of affine Lagrangian relations over an arbitrary field, including empty semantics. Its dagger is relational converse followed by the anti-symplectic involution `(z,x)->(z,-x)` on both sides; this differs from D1702's bare converse and requires an explicit comparison. Its stabilizer subsection summarizes and cites the odd-prime projective comparison; it does not supply normalized instrument semantics or an arbitrary Gaussian-channel classification.

### SP-CGK17

**Shawn X. Cui, Daniel Gottesman and Anirudh Krishna**, *Diagonal gates in the Clifford hierarchy*.

Route: https://arxiv.org/e-print/1608.06596 (TeX archive); final URL: https://arxiv.org/src/1608.06596.

Local readable body: `refs/symplectic-phantasm/SP-CGK17/diagonalCliffordGates5.tex`.

Verified locators: title/authors lines 96–109; §II and §IV, Theorem 3.

Scope: Diagonal hierarchy classification depends on phase precision as well as polynomial exponents. D1307 and D1309 already register the campaign hierarchy and additive-difference conventions. Arbitrary nonlinear Lagrangians and the full hierarchy are not identified here.

### SP-SOULE04

**Christophe Soulé**, *Les variétés sur le corps à un élément*.

Route: https://arxiv.org/e-print/math/0304444 (TeX); final URL: https://arxiv.org/src/math/0304444.

Local readable body: `refs/symplectic-phantasm/SP-SOULE04/source.tex`.

Verified locators: title/authors lines 7–8; §6, condition (Z), zeta definition and associated lemma.

Scope: Polynomial-counting zeta comparison within its stated hypotheses. Do not generalize the rational-factor formula to every proposed F1 geometry.

### SP-DEITMAR05

**Anton Deitmar**, *Schemes over F1*.

Route: https://arxiv.org/pdf/math/0404185 (PDF); final URL: https://arxiv.org/pdf/math/0404185.

Local readable body: `refs/symplectic-phantasm/SP-DEITMAR05/paper.txt`.

Verified locators: PDF front page; §§1–3.

Scope: Monoid-scheme definitions and zeta discussion. TeX retrieval failed; the primary arXiv PDF identifies v7, 26 July 2006. This is a particular definition of F1 geometry, not a limit functor on our quantum systems.

### SP-CC09

**Alain Connes and Caterina Consani**, *Schemes over F1 and zeta functions*.

Route: https://arxiv.org/e-print/0903.2024 (TeX archive); final URL: https://arxiv.org/src/0903.2024.

Local readable body: `refs/symplectic-phantasm/SP-CC09/announc3.tex`.

Verified locators: title/authors lines 222–226; §2, integral and distrsubsect; §4, dthmfonesch.

Scope: Explicitly distinguishes polynomial counting from generalized counting functions/distributions; §2 corrects a sign misprint in the older zeta-limit convention. The guidance note’s blanket exclusion of nontrivial zeros from all F1 approaches is too broad.

### SP-CC10

**Alain Connes and Caterina Consani**, *Characteristic 1, entropy and the absolute point*.

Route: https://arxiv.org/e-print/0911.3537 (TeX archive); final URL: https://arxiv.org/src/0911.3537.

Local readable body: `refs/symplectic-phantasm/SP-CC10/Jamifine.tex`.

Verified locators: title/authors lines 232–236; sections on characteristic one, Witt construction and zeta functions.

Scope: Primary treatment of characteristic-one semirings and extensions of F1-scheme/zeta constructions. This does not define the sought symplectic arithmetic quantum system.

### SP-PRASAD09

**Amritanshu Prasad**, *An Easy Proof of the Stone-von Neumann-Mackey Theorem*.

Route: https://arxiv.org/e-print/0912.0574 (TeX); final URL: https://arxiv.org/src/0912.0574.

Local readable body: `refs/symplectic-phantasm/SP-PRASAD09/source.tex`.

Verified locators: title/authors lines 67–68; theorem at lines 181–191; compact-open-subgroup proof from line 193.

Scope: Finite LCA Schrödinger irreducibility and uniqueness, including characteristic two at the abelian-group level. General rank must be matched to the campaign cocycle and Hilbert normalization.

### SP-GH08

**Shamgar Gurevich and Ronny Hadani**, *The Weil representation in characteristic two*.

Route: https://arxiv.org/e-print/0808.1664 (TeX); final URL: https://arxiv.org/src/0808.1664.

Local readable body: `refs/symplectic-phantasm/SP-GH08/source.tex`.

Verified locators: title/authors lines 49–54; length-two ring and symplectic lift 616–651; chosen Lagrangian cocycle 650–674; R-central Heisenberg group 678–695; ASp defect equation, composition and raw Hom(V,R) kernel 699–729; S-vN_thm/projective representation 747–792; Weilrep_thm and the separate lifted symplectic comparison 794–828 (inspected 2026-09-10).

Scope: Characteristic-two construction uses additional affine/metaplectic and characteristic-four data. Its ASp is described by raw R-valued cocycle-defect pairs, not by a stipulated split V semidirect Sp(V). The raw Hom(V,R) kernel must be compared after applying the chosen central character before identifying a phase-level translation kernel. The later theorem retains a symplectic Witt lift; it is not a general splitting input. It does not justify applying the odd-characteristic half-form formula at p=2. The prepared comparison is in `docs/research-plans/phantasm-char2-source-comparison.md`.

### SP-BCL22

**Cedric Beny, Jason Crann, Hun Hee Lee, Sang-Jun Park and Sang-Gyun Youn**, *Gaussian quantum information over general quantum kinematical systems I: Gaussian states*.

Route: https://arxiv.org/e-print/2204.08162 (TeX); final URL: https://arxiv.org/src/2204.08162.

Local readable body: `refs/symplectic-phantasm/SP-BCL22/source.tex`.

Verified locators: title/authors lines 237–262; §2, Heisenberg multipliers and Gaussian-state definitions.

Scope: A source for an explicit meaning of Gaussian in LCA systems. The subtitle is Gaussian states; a theorem about all channels or stochastic closure cannot be attributed to it without a separate locator.

### SP-DER06

**Jan Dereziński**, *Introduction to Representations of the Canonical Commutation and Anticommutation Relations*.

Route: https://arxiv.org/e-print/math-ph/0511030 (TeX archive); final URL: https://arxiv.org/src/math-ph/0511030.

Local readable body: `refs/symplectic-phantasm/SP-DER06/derezinski.tex`.

Verified locators: title/authors lines 433–437; §5, Hilbert tensor sum and vacuum lines 1814–1829, second quantization and contraction boundedness 1843–1851, composition 1871–1875, symmetric Fock spaces 1911–1964, restricted second quantization 2019–2038 and exponential law tensor.1 at 2051–2090 (completion-scope inspection 2026-09-10).

Scope: Completed Fock Hilbert spaces, second quantization and tensor-product normalization. Algebraic symmetric algebra, Hilbert completion and a free commutative monoid in an unspecified category are distinct.

### SP-CCM07

**Alain Connes, Caterina Consani and Matilde Marcolli**, *Noncommutative geometry and motives: the thermodynamics of endomotives*.

Route: https://arxiv.org/e-print/math/0512138 (TeX archive); final URL: https://arxiv.org/src/math/0512138.

Local readable body: `refs/symplectic-phantasm/SP-CCM07/ncgandmotivesMarch8.tex`.

Verified locators: title/authors lines 156–161; §3 Endomotives; §4 Scaling as Frobenius in characteristic zero.

Scope: Explicit endomotive framework for the Frobenius/scaling comparison. The relevant construction includes more than choosing a reference state on an arbitrary tensor product.

### SP-CM04

**Alain Connes and Matilde Marcolli**, *From Physics to Number theory via Noncommutative Geometry*.

Route: https://arxiv.org/e-print/math/0404128 (TeX archive); final URL: https://arxiv.org/src/math/0404128.

Local readable body: `refs/symplectic-phantasm/SP-CM04/houcheschapter1final7.tex`.

Verified locators: title/authors lines 365–367; represented BC generator relations and time action at lines 1763–1783; zeta partition function 1829–1837 (completion-scope inspection 2026-09-10).

Scope: Fetched TeX has the shorter overall title; the arXiv record carries the Part I / Q-lattices subtitle. Primary comparison for arithmetic semigroup maps and KMS analysis, not an assertion of novelty for the proposed quest.

### SP-BC95

**J.-B. Bost and A. Connes**, *Hecke Algebras, Type III Factors and Phase Transitions with Spontaneous Symmetry Breaking in Number Theory*.

Route: https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf (PDF); final URL: https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf.

Local readable body: `refs/symplectic-phantasm/SP-BC95/paper.pdf`.

Verified locators: printed p.411 / PDF p.1: title, authors, introduction and §1 (visually inspected).

Scope: Original Selecta Mathematica 1 (1995), 411–457, author-hosted scan. Text extraction is empty; inspect images for further citations. Its title is English, unlike a later French transcription. Use SP-CM08 for searchable detailed formulas.

### SP-CM08

**Alain Connes and Matilde Marcolli**, *Noncommutative Geometry, Quantum Fields and Motives*.

Route: https://www.math.fsu.edu/~marcolli/coll-55.pdf (PDF); final URL: https://www.math.fsu.edu/~marcolli/coll-55.pdf.

Local readable body: `refs/symplectic-phantasm/SP-CM08/paper.txt`.

Verified locators: PDF title page; Chapter 3 §§4.1–4.4, printed pp.458ff; represented basis, logarithmic Hamiltonian and partition function equations (3.140)–(3.142), readable lines 23930–23947; Chapter 4 §4.1, printed pp.616–619, equations (4.117)–(4.119), readable lines 30474–30493, and Definition 4.46 (completion-scope inspection 2026-09-10).

Scope: Author-hosted book. BC algebra, time evolution, representations and modular theory have explicit hypotheses. GNS cyclicity alone is not enough to silently assume a separating vector or a prescribed factor type. The separating phrase following (4.118) is not used for arbitrary reference states; D1713 retains it as an additional modular hypothesis. These locators do not supply a theorem for the particular D1711 prime-indexed inductive system; its norm completion and product-state extension are proved locally.

### SP-WAT18

**John Watrous**, *The Theory of Quantum Information*.

Route: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf (PDF); final URL: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf.

Local readable body: `refs/symplectic-phantasm/SP-WAT18/paper.txt`.

Verified locators: PDF title page; finite product density operators, equation (2.18), readable lines 3029–3039; general linear-map adjoint, readable lines 1097–1105; Theorem 2.22, readable lines 3788–3808 (nonzero-map hypothesis); Theorem 2.26, lines 4020–4097; Corollary 2.27, lines 4125–4144; Kraus adjoint equations (2.69)–(2.70), lines 3640–3661; instruments and retained classical register, equations (2.258)–(2.262), lines 5139–5184; completely dephasing channel, equation (2.162), lines 4362–4379, printed pp.94–95; §2.2 Choi representation, equations (2.64)–(2.66), printed p.78 (inspected 2026-09-10).

Scope: Author-hosted 2018 draft; source for finite-dimensional CP/Kraus/trace-preservation, adjoints and instruments. Theorem 2.22 is stated for a nonzero map; zero components require a separate empty-Kraus treatment. Extension to the D1706 direct-sum blocks and retained outcome-pair indices is a local comparison, not an imported source theorem. Equation (2.162) is the one-dimensional-block dephasing model; the arbitrary summand-block formula of D1707 is derived locally using its projections. The Choi representation uses the displayed operator-vector convention and output/input tensor order, to be matched explicitly in a relation comparison. Personal-use source body remains ignored and is not redistributed.

### SP-STFIELD

**The Stacks Project Authors**, *Fields*.

Route: https://raw.githubusercontent.com/stacks/stacks-project/master/fields.tex (TeX); final URL: https://raw.githubusercontent.com/stacks/stacks-project/master/fields.tex.

Local readable body: `refs/symplectic-phantasm/SP-STFIELD/source.tex`.

Verified locators: title at line 7; Trace and norm, section-trace-pairing; lemma-trace-and-norm-tower; lemma-separable-trace-pairing.

Scope: Official TeX source; finite separable trace pairing and transitivity. Restriction of scalars is not the same operation as embedding a subfield with the uncorrected trace form.

### SP-SPECTOR98

**Donald Spector**, *Duality, Partial Supersymmetry, and Arithmetic Number Theory*.

Route: https://arxiv.org/e-print/hep-th/9710002 (TeX); final URL: https://arxiv.org/src/hep-th/9710002.

Local readable body: `refs/symplectic-phantasm/SP-SPECTOR98/source.tex`.

Verified locators: title/authors lines 7–15; §1 and bosonic/fermionic partition-function construction.

Scope: Author’s accessible primary follow-up on arithmetic gases; the earlier Spector 1990 and Julia/Bakas–Bowick references are pointers, not locally verified substitutes for those missing bodies.

### Historical guidance leads — GAP registry (2026-09-09)

These are bibliographic leads, not verified theorem sources. No bootstrap
DAG node may rely on them. Titles below have the verification boundary
shown explicitly; a source from another author is not a replacement body.

| source-id | availability | bibliographic lead and attempted primary route | next action |
|---|---|---|---|
| SP-TITS57 | GAP | J. Tits, Sur les analogues algébriques des groupes semi-simples complexes (1957), 261–289; title/author verified from ULB metadata https://difusion.ulb.ac.be/vufind/Record/ULB-DIPOT:oai:dipot.ulb.ac.be:2013/173612/Details ; no full text linked | Retrieve original; do not promote the informal symplectic F1 analogy |
| SP-JULIA90 | GAP | B. Julia, Statistical Theory of Numbers, Number Theory and Physics (1990), DOI 10.1007/978-3-642-75405-0_30; https://cds.cern.ch/record/203834 ; retrieval returned browser challenge | Find accessible original; SP-SPECTOR98 is separate evidence |
| SP-BB91 | GAP | I. Bakas and M. J. Bowick, Curiosities of arithmetic gases, J. Math. Phys. 32 (1991), 1881–1884; https://cds.cern.ch/record/212591 ; retrieval returned browser challenge | Retrieve original preprint or permitted publisher copy |
| SP-SPECTOR90 | GAP | D. Spector, Supersymmetry and the Möbius inversion function, Commun. Math. Phys. 127 (1990), 239–252; bibliography corroborated by SP-SPECTOR98 lines 47–56; attempted Euclid cmp/1104180217 PDF route returned HTML | Resolve the original primary record; the guessed retrieval identifier is not verified metadata |
| SP-POWERS67 | GAP | R. T. Powers, Representations of uniformly hyperfinite algebras and their associated von Neumann rings, Annals 86 (1967), 138–171; https://annals.math.princeton.edu/1967/86-1/p06 metadata verified, DOI 10.2307/1970364 | Retrieve original if factor classification becomes load-bearing |

### SP-KS95 — gap resolved during the bootstrap

**M. Kapranov and A. Smirnov**, *Cohomology determinants and reciprocity
laws: number field case*. The title and authors were visually verified on
PDF p.1; PDF p.4, §1.4 was also visually inspected. The preprint date 1995
is bibliographic metadata from the author profile, not printed on the
inspected title page.

Route: http://www.neverendingbooks.org/DATA/KapranovSmirnov.pdf (researcher-
hosted primary preprint scan). The HTTPS route refused connection, but the
linked HTTP route supplied the actual PDF. Local readable body:
`refs/symplectic-phantasm/SP-KS95/paper.pdf`. The text extraction is empty;
further citations require image inspection.

Verified scope: §1.4 defines pointed sets with a free action of roots of
unity away from zero, equivariant maps, bases, and direct/smash/tensor
operations. This is a specific model for extension-field analogies, not a
constructed symplectic quantization or an identification of Frobenius with
modular flow. No claim promotion follows from resolving the retrieval gap.

### SP-JOY81 — gap resolved during the bootstrap

**André Joyal**, *Une théorie combinatoire des séries formelles*, Advances
in Mathematics 42 (1981), 1–82. Title and author verified on the fetched
PDF p.1; §1.1, Definition 1 on PDF p.3 defines a finitary species as an
endofunctor of the groupoid of finite sets and bijections. Section 2 treats
combinatorial operations.

Route: https://mahalex.net/teaching/seminars/semag/joyal.pdf (primary article
copy linked by Alexander Luzgarev's research seminar page). The publisher
route returned 403; this independently accessible academic copy resolves
the body gap. Local readable body:
`refs/symplectic-phantasm/SP-JOY81/paper.txt`, with the original PDF beside it.

Scope: source for the species comparison at DG-RIG. No equivalence between
this combinatorial category and completed bosonic Fock Hilbert spaces is
attributed to Definition 1. The latter uses the separately registered
SP-DER06 normalization and analytic domain.
