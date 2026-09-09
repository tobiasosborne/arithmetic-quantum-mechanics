# Symplectic Phantasm argument-contract expectations

Registered before the first checker run, 2026-09-09. This checks the new
quest slice and its direct references to older claims, not the entire
historical argument graph. It does not prove mathematical types, lemma
statements, or source theorems. No mathematical falsifier for the new lemmas
is implemented by this checker.

Inputs: the canonical claim and definition registers, notation, the
Markdown quest DAG, the local source ledger and source bodies, and the two
owning labbook files. The source data must exist on disk; a new checkout
must run the retrieval script and verify its hashes before this passes.

| Gate | Contract | Mutations which must exit nonzero at this gate |
|---|---|---|
| G1 | Unique, nonempty node schema and fields; parseable claim/source/order rows | duplicate-node, empty-scope |
| G2 | One contract per SP claim, matching status/dependencies/stage; definitions, source ids, decision prerequisites and evidence paths resolve; plan and decision graph agree | missing-node, missing-definition, status, orphan-claim, decision-input |
| G3 | Acyclic lemma and decision dependency graph | cycle, decision-cycle |
| G4 | No reliance on REFUTED nodes; a PROVED node has PROVED dependencies, admitted evidence, real structured proof, adjudication and checker paths | refuted, promote |
| G5 | Every cited source is LOCAL with readable body and correct raw/readable SHA256; GAP cannot serve as evidence | source-hash, source-gap |
| G6 | Exact definition/claim restatement, scope and status in the owning labbook; all new definitions in notation and root LaTeX inputs | labbook, definition-drift |

Mutations alter copies of the actual parsed input records or their raw
Markdown/LaTeX text, not repository files. Every advertised red mode must
name the expected gate. The verifier records the first red run before the
first green run, and subsequently verifies every red mode against this map.

The formal proof/evidence gate is a record-presence and dependency check.
It does not certify that a proof or adjudication is valid. A future
promotion still requires the capped human-readable L6 process and actual
red/green mathematical falsifiers; a filled path alone proves nothing.
