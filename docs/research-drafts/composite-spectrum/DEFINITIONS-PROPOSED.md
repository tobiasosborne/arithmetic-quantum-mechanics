# Proposed definitions for the completed degree boundary

2026-09-09. UNREVIEWED, proposed D1611--D1612. The finite CMP claims are
inputs; no claim about the Riemann zeros is part of these definitions.

## D1611 (divisor corners and their concrete completion)

For N>=2 put A_N=direct-sum_(d|N,d>1) M_d(C), with operator norm the
maximum of its block norms. For N|M define j_(N,M) by extending block
coordinates by zero. Put eta_d=phi(d)/d and
theta_N(a)=sum_(d|N,d>1)eta_d tr_d(a_d), with tr_d=Tr/d.

Let H_deg=Hilbert-direct-sum_(d>=2) C^d, and define A_deg to be the
block-diagonal operator algebra of sequences a=(a_d) with ||a_d||->0,
in the supremum operator norm. Let B_deg=A_deg+C I_H be its concrete
minimal unitization. For positive a in A_deg define the extended-valued
functional theta(a)=sum_(d>=2)eta_d tr_d(a_d). The symbol H_deg denotes
the Hilbert space, not a Hamiltonian.

These are proposed concrete objects; norm completion, trace properties,
and comparison with the arithmetic corner embeddings are claims. No
endpoint tensor or coherent direct-sum operation on the distinguished
primitive systems is stipulated by this choice of completion.

## D1612 (completed Frobenius and positive degree regularization)

On D1611's Hilbert space define U_deg=direct-sum_(d>=2) S_d, with S_d
the actual relative-cycle matrix from D1603. Put
alpha(a)_d=S_d a_d S_d^*, fixing the scalar unit in B_deg.
For a real beta>1 define

    Z_deg(beta)=sum_(d>=2)phi(d)/d^(beta+1),
    D_beta=direct-sum_(d>=2)d^(-beta)I_d,
    rho_beta=direct-sum_(d>=2)[phi(d)/(Z_deg(beta)d^(beta+2))]I_d,
    omega_beta(a)=Tr_(H_deg)(rho_beta a).

Define zeta(x)=sum_(m>=1)m^(-x) for real x>1. For an integer j define
the implementing-operator moment
M_beta(j)=Tr_(H_deg)(rho_beta U_deg^j). This expression uses the named
Hilbert implementation: U_deg need not belong to B_deg itself.

The regulator D_beta is additional central degree-weight data for this
completion, not an arithmetic amplitude, a Frobenius generator, or a
claim that degree energy has been uniquely selected by the quantum theory.
No analytic continuation or infinite unregularized trace is stipulated.
