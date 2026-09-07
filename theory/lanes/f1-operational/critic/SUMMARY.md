# F1 operational critic summary

Blind same-family Sol/xhigh review completed once, with no prover summary or
patch reasoning read.

Verdict: `FAIL(O1,O2)`.

- **O1 MAJOR:** D1121 allows the zero object, where `d_X=0`, normalized
  `tau_X` is undefined, and CPOP-1--3 state semantics fail.  Exclude zero
  objects / require `d_X>0`.
- **O2 MAJOR:** all thirteen red modes fail, but each kills only an early
  assertion; many advertised acceptance assertions have no mutation that
  reaches them.  Add reachable data mutations before treating the checker as
  L1-compliant.
- **O3 MINOR:** `F1-HCK-LOW` calls `P_2` a preparation although its full
  coefficient-trace density is `((1+q+q^2)/q)P_2`; its stated Born formula is
  correct.
- **O4 MINOR:** proposed `tested in` cells are stale placeholders, and the
  tower checker is level four rather than a general through-level-five test.

The core positive mathematics survives: Hecke C*-positivity for every `q>0`,
the exact flag commutant, ordered parabolic inclusions/UCP expectations and
coherence, the `q/(q+1)^2` overlap memory, `H_n(1)=C[S_n]`, the finite-injection
operational net, and the `1 -> 1/4` local-context witness.

KCF-1 also survives in full at `q=1`: Kraus Gram equality, stable
scalar-unitary mixing, and equality in all finite contexts are equivalent;
ambient size `2n-1` is sufficient and sharply necessary.  Independent exact
enumeration reproduces Born gaps `1/2` for `n=2` and `1/18` for `n=3`.  The
separate `q>0` Hecke extension remains `SKETCH`, as it should.

PMAP-1 survives as well.  The support criterion for a partial injection proves
functoriality, trace adjunction proves the dagger law, and block support proves
lax symmetric monoidal naturality.  The empty partial map correctly becomes
`a -> tau(a)1`, so the endpoint is an actual functor on finite sets and partial
injections.  It is mathematically suitable for promotion after adjudication;
H12 agreement is supporting evidence only.

Generic fusion/Fibonacci material can remain supporting `SKETCH`.  The
categorical `Tr` and coefficient `tau` conventions are consistent after the
rescaling `h=d_X rho`; only the low-level claim-row wording needs repair.
