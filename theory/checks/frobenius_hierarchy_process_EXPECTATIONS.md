# Exact category/CP checker requirements, preregistered before admission

Definition interface: DEFINITIONS-PROPOSED.md D1325--D1327.
Checker ownership: sibling `check/` lane, A7. This document is a specification,
not a record that gates have passed. Fractions and finite field tables suffice
for the inclusion examples. For normalized Fourier/trace-fibre matrices use
an exact scaled representation or cyclotomic arithmetic; numerical tolerance
alone is not the proposed evidence.

| gate | independently recomputed assertion | required mutation |
|---|---|---|
| A7-TYPE | J,V:K->E; decoder success E->K, failure E->E; exact word and external tag targets of sequential/tensor arrows | reverse J dagger direction or give a partial-success branch the wrong output dimension |
| A7-PREP | basis kets are normalized; hidden basis-bra discard has sum K* K=I and returns ordinary trace | omit one discard bra |
| A7-NORM | for S=J and V, Q=I-SS* is an orthogonal projector and the success/failure effects sum to I | use I-S*S with wrong type or scale Q |
| A7-BORN | code input gives one, complementary input zero, I_E/|E| gives |K|/|E|; coherent F4 state (|0>+|alpha>)/sqrt2 gives J-success 1/2 and conditional |0> | replace ordinary trace by a normalized trace without density conversion |
| A7-TOWER | F2->F4->F16 three retained history Kraus amplitudes Q_j, Q_i J_j*, J_i* J_j* normalize, with last equal (J_j J_i)* | reverse the history product or drop the intermediate failure |
| A7-PAR | D_S tensor D_T has four typed tags ss,sf,fs,ff and effects P_S tensor P_T, P_S tensor Q_T, Q_S tensor P_T, Q_S tensor Q_T; success on correlated rho uses the joint effect | replace the four outcomes by a two-outcome global reset or drop sf |
| A7-COMP | independently form sequential Kraus products and tensor products, compare their CP actions on matrix units and their complete effect sums | reverse one sequential product or scramble one tensor index |
| A7-FOURIER | D_V after F_E equals D_J followed by F_K on success, F_E on failure, as maps on matrix units with tags retained | positive Fourier kernel in one field or wrong V fibre normalization |

Detailed finite examples:

- F4=F2[alpha]/(alpha^2+alpha+1), J columns |0>,|1>.
  Relative trace fibres are {0,1} and {alpha,alpha+1}; V columns are
  the normalized sums on those sets. This directly probes all outcomes.
- Tensor two J decoders. Test both a product state outside the first code
  and inside the second, and the entangled input
  (|0,0>+|alpha,alpha>)/sqrt2. In the latter case ss and ff have probability
  1/2, while sf and fs vanish; independent marginal multiplication would
  incorrectly give ss probability 1/4.
- A tower history is a genuinely different typed process from the one-step
  decoder: its output words are E,K,F2 (for E=F16,K=F4), rather than
  just E,F2. Compare the all-success branch; do not assert equality of the
  complete instruments unless explicit additional routing maps are supplied.
- Optional reset boundary: D_(J tensor J) resets both factors after any
  failure, whereas D_J tensor D_J preserves a successfully decoded factor.
  This is a scope sentinel, not a positive monoidality claim.

Every advertised gate needs a red path with a named data mutation reaching
that gate. Record gate reachability and exit nonzero. Static type gates are
part of the evidence because matrix formulas with the wrong codomain do not
define the asserted arithmetic morphism.
