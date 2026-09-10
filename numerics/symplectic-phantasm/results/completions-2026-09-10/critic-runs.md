# Checker verification — completion controls

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.
All modified checkers were temporary `/tmp` copies.

## Frozen hashes

| artifact | SHA-256 |
|---|---|
| `fock.md` | `10b05e43ba54e12ca7d4c6c9bb2551976d5ddb040b075cdda7312fb04318358e` |
| `prime-tensor.md` | `45eda8795015d244722b8543e8d798aaad4dd66859a440f8dcafd5636c495ad7` |
| `bc-control.md` | `629d0900be215a7b61128bb456804a6a5564397931cdeac46b77c94004d85210` |
| checker | `de4ed53d12be8e8a7414b28aec57ce0bad8b617f804e57deec418c6baefceaa8` |
| expectations | `a4fe32ea5d163d1430961f05ac4d8f8281573954ee6c7fa6381dbf91b953cf0b` |

The checker imports only the Python standard library.

## Advertised reds before green

`--help` exposed exactly thirteen red flags. Every mode exited 1 at its
intended gate:

| mode | observed first path | seconds |
|---|---|---:|
| `L-multiplicative` | B3 corner product | 0.042 |
| `b1-trace-class` | B4 harmonic bound 3 | 0.038 |
| `density-trace` | P2 state compatibility | 0.045 |
| `fock-binomial` | F2 at `(1,1)` | 0.040 |
| `fock-expansive` | F3 contraction deficit | 0.036 |
| `fock-vacuum` | F1 at `d=0,r=0` | 0.043 |
| `gns-separating` | P2 Gram-action injectivity | 0.072 |
| `mu-unitary` | B1 range projection | 0.039 |
| `one-mode-factorial` | F1 at `r=2` | 0.038 |
| `prime-nonunital` | P1 inserted unit | 0.051 |
| `prime-position` | P1 factor order | 0.050 |
| `root-average` | B2 normalization | 0.044 |
| `time-sign` | B3 valuation exponent | 0.037 |

No red reached a wrong gate or exception exit 2.

## Greens

Normal green exited 0 in 0.22 seconds; optimized green exited 0 in 0.34
seconds. Both passed F1--F3, P1--P2 and B1--B4 and reported 15 symmetrizers,
15 exponential cases, 14 prime inclusions, 30 triangles, GNS ranks
576/192/3, 360 root-average cases and eight dyadic harmonic witnesses.

## Gate simplification

| gate | substantive comparison | limitation/red |
|---|---|---|
| F1 | permutation-average matrices versus projection laws and independent occupation counts | vacuum and factorial reds |
| F2 | raw rational symmetrizer norm versus factorial formula | binomial red; its one-mode scalar naturality is only scalar commutation |
| F3 | actual contraction deficits and finite composition for diagonal/swap fixtures | expansive red; reported `2I` growth is detached, objection 1 |
| P1 | explicit slot insertion versus units, products, stars, polynomials and triangles | order and nonunital reds |
| P2 | product densities/states and exact diagonal Gram weights | density and faithful-to-pure reds; cyclicity itself is definitional |
| B1 | semigroup, range-left-inverse and proper projection | unitary red; nonmultiple adjoint is untested, objection 2 |
| B2 | rational root parameterization and a symbolic divisibility oracle | root-average red; no floating character sum is claimed |
| B3 | valuation differences and independent symbolic nu/L operator actions | sign and L-multiplicative reds |
| B4 | exact rational tail intervals and harmonic lower witnesses | b=1 bound red |

Every gate has at least one advertised red. The red effects are distinct.
B2's `root_average` uses the same divisibility split as its expected tuple;
its useful independent work is root parameterization and the omitted-factor
mutation. This matches its explicitly symbolic finite scope and is not counted
as an analytic convergence test.

## Disabled-guard reachability

With only the named comparison disabled, the actual mutation survived and
exited 0:

| temporary control | result |
|---|---|
| F3 contraction guard disabled with `fock-expansive` | `RED SURVIVED`, 0.041 s |
| P1 position guard disabled with `prime-position` | `RED SURVIVED`, 0.168 s |
| B3 time guard disabled with `time-sign` | `RED SURVIVED`, 0.042 s |
| B4 b=1 guard disabled | `RED SURVIVED`, 0.038 s |

## Independent actual-data mutations

| copy mutation | ordinary path |
|---|---|
| change the permutation-average denominator | exit 1 at F1 projection |
| replace inserted identity support by one coordinate | exit 1 at P1 unit |
| give rho_5 a negative final diagonal entry | exit 1 at P2 compatibility |
| use floor division for every nondivisible shift adjoint | exit 1 later at B3 |

Two additional false-acceptance controls establish the numbered findings:

- replacing every `tensor_power(a,r)` by an identity matrix left the complete
  run green and retained the printed `2I` growth;
- returning floor division only for nonmultiples of five in `mu_star` left
  the complete run green, including B1.

The installed files were not changed by any control.
