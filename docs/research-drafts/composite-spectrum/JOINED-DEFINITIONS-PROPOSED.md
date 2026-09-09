# Proposed D1621: finite degree assemblies and their joined boundary

2026-09-09. UNREVIEWED new definition for the joined-limit artifact.

## D1621 (degree-mixture preparation and normalized success profiles)

Fix an integer base degree s>=1, a real beta>1, and for each integer
d>=2 a named extension E_d/K with |K|=p^s and [E_d:K]=d. For an
integer cutoff D>=2 let L_D(beta)=sum_(d=2)^D d^(-beta). Prepare the
classical degree tag with probabilities d^(-beta)/L_D(beta), then the
D1604 copied primitive reference instrument in that degree. On its
success apply D1607's uniform relative randomization and explicitly
discard the randomization label. Keep every failed degree and its
primitive/averaging history. This degree prior is declared additional
classical preparation data, not an assertion that all such real weights
are coefficients of the original arithmetic amplitude source.

For t>1 set

    w_d(t)=c_d(t^s)/(d t^(sd)),
    v_d(t)=w_d(t)/(s(t-1)),
    Z_D(beta,t)=sum_(d=2)^D d^(-beta)v_d(t).

Set v_d(1)=phi(d)/d and use that value in Z_D(beta,1). On the named
Hilbert degree sum of D1611, define rho_(D,t) to have d-block
[d^(-beta)v_d(t)/(d Z_D(beta,t))]I_d for 2<=d<=D and zero elsewhere.
At t=1 this designates the retained first-grade conditional record,
not normalization of an actually successful zero-probability event.

Define L_infty(beta)=sum_(d>=2)d^(-beta),
Z_infty(beta,t)=sum_(d>=2)d^(-beta)v_d(t), and the corresponding
rho_(infty,t) by the same block formula when the sums converge. The
rho_beta of D1612 is the proposed t=1 value. The stated outputs are
restrictions to common quantum observables, not identifications of
physical arithmetic multiplicity states. Uniform randomization makes
this reference stationary under relative Frobenius; the unrandomized
D1604 experiment remains the separate coherence-sensitive witness.
