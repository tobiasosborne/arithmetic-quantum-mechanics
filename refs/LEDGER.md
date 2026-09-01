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

**N3 — role-narrowing on 1412.2490.** Its verified title is "Simple twisted
group algebras of dimension `p^4` and their semi-centers", which is narrower
than the general role the coverage table assigns it. The general facts it is
cited for (semisimplicity of twisted group algebras, Artin-Wedderburn, groups
of central type, the abelian `A x A` characterization) appear in its
introductory material and are there **attributed to Karpilovsky**, which the
lane correctly flagged as attributed-through rather than independently
fetched. Treat those as ADMITTED steps under L3 until Karpilovsky is
registered, and let the affected claim's status reflect that.
