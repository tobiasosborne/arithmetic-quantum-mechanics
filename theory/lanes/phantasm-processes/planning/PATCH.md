# String-anchored planning handoff

Planning model: `gpt-5.6-sol`, reasoning `xhigh`.

This lane changes no canonical definition, claim, proof, checker or status.

## Work-order landing

Copy `BRIEF.md` to the intended trunk path
`briefs/phantasm-processes-target.md`.

Anchor the new handoff pointer on the current completed relation-cluster
next-task sentence in `HANDOFF.md`, replacing only the next bounded task with
the new brief path after the current landing closes.

## Pre-proof D1706 repair

Before starting either proof, anchor in `definitions.md` inside D1706 after
the sentence beginning

> Its retained version has codomain

and apply the exact outcome-first retained-block, sequential-instrument,
tensor-instrument and ordinary-trace-adjoint prescriptions in `BRIEF.md`
section “Pre-proof type repair to D1706.”  Anchor its Scope and Delta edits on
the existing D1706 `**Scope.**` and `**Delta.**` fields.

In `notation.md`, anchor on the D1706 row containing

> `K_(b a,j)`, `Phi_o`

and add `Phi^(tr*)` as the ordinary-block-trace adjoint owned by D1706.  Do
not allocate a new definition number.

Restate the repaired D1706 body and Scope exactly in
`labbook/sections/symplectic_phantasm.tex`, anchored on its existing finite
quantum branches and instruments definition.  This is a definition-only
lockstep edit; it changes no claim status.

## Later proof/checker integration

After the definition repair, use the exact SP-SCALAR and SP-CP rows and DAG
nodes as anchors.  Proof/checker paths remain unset until the corresponding
artifacts exist.  The checker should be
`theory/checks/phantasm_process_check.py` with only the named no-argument red
flags specified in the brief.

Do not add SP-STAB-REL as a dependency of SP-SCALAR merely because D1705
motivates the representative corollary.  Do not turn the reverse
ordinary-trace adjoint into a D1706 branch without separately proving its
trace-nonincreasing condition.
