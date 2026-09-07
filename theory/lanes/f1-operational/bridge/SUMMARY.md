# Operational F1 bridge: flags, Hecke sectors, and two TL boundaries

## Main result

For `L=F_p^n`, complete flags in the selected configuration Lagrangian are
exactly a `GL(L)`-orbit of maximal chains of commuting Weyl constraints.  Each
subspace `U` gives explicit nested stabilizer projectors in the original AQM
matrix algebra.  The Iwahori--Hecke algebra

`H_n(p)=End_{GL(L)} C[Flag(L)]`

is therefore a genuine finite-dimensional quantum sector of **context
amplitudes** and `GL(L)`-invariant transitions between contexts.  It is coupled
to the original AQM system by controlled constraint projectors and by the same
Clifford/permutation action of the symplectic Levi `GL(L)`.

It is not the original system.  `C[Flag(L)]` has dimension `[n]_p!`, whereas
the Schrodinger space `C[L]` has dimension `p^n`.  The Hecke commutant does not
recover the phase character, cocycle, full Weyl algebra, arbitrary AQM states,
or Fourier/Weil operators.  The exact construction and a bounded refinement
conjecture are in `BRIDGE.md`.

## Three sourced bridges

### 1. Arithmetic flags to AQM contexts

- Iwahori and Curtis identify the flag permutation commutant with the
  specialized Weyl-group Hecke algebra.  Relative positions of pairs of flags
  form its standard basis, and `T_i^2=p+(p-1)T_i` retains the field cardinality.
- If one forgets the distinguished basis/module/trace and keeps only the
  abstract complex algebra, Curtis's deformation result identifies it with
  `C[S_n]`; `p` is then lost.
- `GL(L)` embeds in `Sp(L direct-sum L^vee)` as the Siegel Levi and acts on
  `C[L]` by exact Clifford permutation unitaries.  The flag projector chains
  transform equivariantly.
- Partial-flag forgetting maps have normalized incidence isometries.  Their
  compressions are composable UCP maps on the Hecke commutants, so the context
  family already has density operators, positive functionals, CP dynamics and
  Born probabilities at every finite `p`.

### 2. Type A through Temperley--Lieb

- Goodman--Wenzl give the exact quotient coefficient
  `p/(p+1)^2=delta^{-2}`, hence
  `delta=sqrt(p)+1/sqrt(p)`.
- The algebraic positive specialization `q->1` gives `delta=2`.  Bernstein--
  Frenkel--Khovanov identify this Temperley--Lieb tower with the commutant on
  tensor powers of the two-dimensional `sl2` module.  Its completed tensor
  category is the ordinary `SU(2)` spin-composition category.
- This requires a rank-two Temperley--Lieb quotient and the Jones/Markov trace.
  The faithful canonical flag-Hecke trace does not descend through a nonzero
  quotient.  At `q=1`, the regular flag weights `(1/2,1/2)` on `C[S_2]` differ
  from the singlet/triplet normalized matrix-trace weights `(1/4,3/4)`.
  Therefore `SU(2)` is a valid positive endpoint with extra composition/state
  data, not the unchanged full-flag quantum system.

### 3. Fibonacci and type C mark different boundaries

- Fibonacci uses `delta=phi`, equivalently the fifth-root Hecke parameter
  `q_H=e^{2 pi i/5}` under `delta=sqrt(q_H)+1/sqrt(q_H)`.  Root-of-unity TL is
  nonsemisimple; the Jones/tilting reduction at order five has even subcategory
  `{0,2}` with `2 tensor 2=0 direct-sum 2`.  This is the Fibonacci category.
  It is a different specialization of the same generic TL family, not the
  positive `q=1` endpoint.
- Symplectic complete flags give a type-`C_n` Hecke context sector.  At `q=1`
  its Weyl group is the signed permutation group `B_n`; these contexts range
  over all Lagrangians, rather than flags in one selected Lagrangian.
- Direct sum embeds `B_m x B_n` in `B_{m+n}`, but this full-rank proper
  reflection subgroup is not parabolic.  The usual generic parabolic Hecke
  tensor law is therefore unavailable.  Decomposable composite flags are
  exactly product flags plus an `(m,n)` shuffle, giving a concrete collective
  context sector, but a generic type-C Hecke bimodule and its coherence remain
  to be constructed.

## Retained versus forgotten

| Object retained | Consequence | Data still absent |
|---|---|---|
| `GL(L)`-set of flags and standard Hecke basis | Remembers `p`, rank, incidence and context-relative position | Central character and cocycle |
| Flag Hilbert space and commutant | Honest finite C*-quantum context sector | Original AQM state space and full matrix algebra |
| Equivariant projector-chain map | Connects flags to commuting Weyl constraints | Noncommuting half of phase space and Fourier intertwiners |
| TL quotient plus Markov state | Positive `q=1`, `delta=2` `SU(2)` composition | Full flag trace/state and discarded Hecke blocks |
| Fifth-root Jones fusion quotient | Fibonacci fusion and process Hilbert spaces | Any identification with F1 or positive `q=1` |
| Type-C isotropic flags | All Lagrangian contexts and signed Weyl limit | Standard two-factor parabolic tensor law |

## Honest next step

Promote the explicitly defined partial-flag Hecke algebroid and controlled Weyl
projectors as a comparison object.  The next theorem should ask whether its
refinement/forgetting maps admit one integral `q`-deformation compatible with
finite-p Clifford realization and type-A parabolic composition.  This is
strictly stronger and more useful than claiming that an unspecified category
exists, while it leaves the type-C nonparabolic composition problem visible.

Source hashes, URLs and locators are in `SOURCES.md` and `evidence/`.
