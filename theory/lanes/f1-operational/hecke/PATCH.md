# String-anchored trunk proposal: ordered Hecke operational tower

Lane proposal only.  Apply nothing before the checker, hostile review, repair,
and adjudication.  All claim statuses proposed here remain `SKETCH`.  Because
this changes definitions and claims, the owning labbook section must land in
the same admission commit under L11.

## 1. `definitions.md`

Anchor: insert after the final sentence of D1013:

> Its clock/shift realization is claim `F1-TORUS`.

Insert exactly the five definition sections D1101--D1105 from
`theory/lanes/f1-operational/hecke/DEFINITIONS-PROPOSED.md`, beginning with

> ## D1101 (positive type-A Hecke systems and their coefficient traces)

and ending with

> two minimal projections are left unlabelled, are claim `F1-HCK-Q`.

Do not insert the lane preamble or its final coordination paragraph.
Definitions D1121 onward remain reserved for the CP lane.

## 2. `notation.md`

Anchor: replace the first table row beginning ``| `p`, `m`, `q` |`` with:

```markdown
| `p`, `m`, `q` | prime; degree; `q=p^m` on arithmetic fibres and the positive real Hecke parameter, agreeing at flag fibres | D1, D1101 |
```

Anchor: append these rows to the F1 sidequest notation table, after the row
beginning ``| `xi, T_xi, T_xi(1,1)` |``:

```markdown
| `H_n(q)`, `T_i`, `T_w`, `tau_n` | type-A Hecke level, simple generators, standard basis, coefficient trace | D1101 |
| `iota_(m,n)`, `E_(m,n)` | ordered contiguous-parabolic inclusion and coefficient-projection expectation | D1102 |
| `a(C;B_1,B_2)`, `P_i`, `z_std` | unlabelled overlap invariant; rank-one compressed projections; unique `M_2` central support at level three | D1103, F1-HCK-LOW |
| `Fl(L)`, `Cxt(L)`, `A_w`, `tr_Fl` | complete flags, their equivariant commutant, relative-position adjacency operators, normalized flag trace | D1104 |
| `e_triv`, `r_2` | marked trivial spectral projection at level two and its coefficient-trace weight | D1105 |
```

## 3. `claims/CLAIMS.md`

Anchor: append a new subtable after the final current F1 sidequest row
beginning ``| `F1-TORUS` |`` and before the next top-level heading.  Use the
table header and all seven rows in
`theory/lanes/f1-operational/hecke/CLAIMS-PROPOSED.md` exactly.  Do not promote
their `SKETCH` statuses merely because the prover lane and checker agree.

## 4. `refs/LEDGER.md`

Anchor: append after the last entry in
`## F1 clarification — subsystem composition and quantum operational semantics`:

```markdown

## F1 ordered Hecke operational tower

**iwahori-1964** — Nagayoshi Iwahori, *On the structure of a Hecke ring of a Chevalley group over a finite field* (1964). Retrieved 2026-09-07 from https://repository.dl.itc.u-tokyo.ac.jp/records/39909, file `jfs100207.pdf`; proposed local `refs/f1/iwahori-1964/paper.pdf`; SHA256 `27efc0216ba5b152d4d4a411239cf66793ad93a4a05490f64c03f7101afc9a96`. Page 215, opening: Hecke ring as the commutant on `G/B`; pp. 220--221, Proposition 1.4 and Corollary 1.5: commutant/opposite convention and block decomposition; pp. 230--234, Lemma 3.1, Theorems 3.2 and 4.1: Bruhat indices, standard basis, quadratic/braid relations and presentation; p. 236, Theorem 5.4: Goldman involution.

**umegaki-1954** — Hisaharu Umegaki, *Conditional expectation in an operator algebra* (1954). Retrieved 2026-09-07 from https://www.jstage.jst.go.jp/article/tmj1949/6/2-3/6_2-3_177/_pdf/-char/en; proposed local `refs/f1/umegaki-1954/paper.pdf`; SHA256 `870e524af7fa7c7e6e99a11aaab413eca83704d903e3148ab83ef7ce448b0a21`. Pages 177--179, section 2 theorem and identity (1): trace-preserving positive expectation, trace-pairing characterization, faithfulness, fixed points, bimodule property and Schwarz inequality. Complete positivity is derived in the Hecke shard rather than attributed anachronistically.

**stinespring-1955** — W. Forrest Stinespring, *Positive functions on C*-algebras* (1955). Retrieved 2026-09-07 from https://www.ams.org/journals/proc/1955-006-02/S0002-9939-1955-0069403-4/S0002-9939-1955-0069403-4.pdf; proposed local `refs/f1/stinespring-1955/paper.pdf`; SHA256 `cff456fa4c19c224b27b41117b894a047377123b5d37f4fc8545e2483ea54991`. Page 211 defines complete positivity; pp. 212--213, Theorem 1, gives its dilation form; p. 215, Theorem 3, treats positive scalar functionals.
```

The exact source bytes and searchable derivatives are currently under
`theory/lanes/f1-operational/hecke/sources/`; the orchestrator promotes them to
the proposed `refs/f1/` paths.

## 5. Owning theory, checks, and labbook

After repair, promote the proof shard to an orchestrator-chosen ground-truth
path under `theory/sidequests/` and update the seven `proved in` cells from the
lane path to that path.  Register the independent red/green checker path in
the `tested in` cells.

The lockstep labbook section should state, in this order: positive coefficient
trace; finite-field complete-flag model; ordered parabolic inclusions and UCP
expectations; `H_1=C`, `H_2=C^2`, `H_3=C^2 direct-sum M_2(C)`; the intrinsic
overlap `q/(q+1)^2`; the exact collective Born experiment; `q=1` as
`C[S_n]`; and the chosen-Lagrangian boundary.  It must say explicitly that
the braid generators are not unitary for `q!=1`, the assembly is not supplied
with a symmetry, and the flag-context algebra is not the full finite-field
Weyl--Heisenberg AQM.
