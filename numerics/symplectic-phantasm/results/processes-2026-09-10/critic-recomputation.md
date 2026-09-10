# Independent recomputation — process cluster

Date: 2026-09-10. Model: `gpt-5.6-sol`, reasoning `xhigh`.

This record contains the independent calculations used by the blind verdict.

## One-Kraus map

For an auxiliary space `E`,

    (id_E tensor Phi_T)(R)=(I_E tensor T)R(I_E tensor T)^*.

This is positive for every positive `R`. Direct indices give
`Tr(T rho T^*)=Tr(T^*T rho)`. Hence `T^*T<=I` implies TNI. Conversely,
testing `rho=|x><x|` gives `||Tx||^2<=||x||^2` for every `x`, which is exactly
`T^*T<=I`.

Scalar multiplication gives `Phi_(cT)=|c|^2Phi_T`. The raw formula therefore
does not descend through non-unit rescaling. But for `T!=0`,

    [T] |-> Phi_T/||T||^2

does descend and is TNI, because numerator and denominator both gain
`|c|^2`. This is the counterexample to the word “only” in OBJ-1. It is a new
normalization rule, not a rule stipulated by D1705, and its compatibility with
composition is not asserted.

## Direct-sum CP maps

For `Phi:B_X->B_Y`, block insertion and projection are CP, so each component
`Phi_(ba)` is CP. Nonzero components have same-family Kraus lists by Watrous
2.22; the zero component is the empty Kraus sum. Linearity reconstructs Phi.

For a chosen presentation define
`A_a=sum_(b,j)K_(ba,j)^*K_(ba,j)`. Rectangular trace gives

    Tr_Y Phi(rho)=sum_a Tr(A_a rho_a).

Positive inputs supported on one tag and one rank-one vector show that TNI is
equivalent to every `A_a<=I`; trace preservation is equivalent to equality.

For tensor branches the effect is `A_a tensor D_c`, and

    I tensor I-A tensor D=(I-A) tensor I+A tensor(I-D)>=0.

The identity on elementary matrix tensors extends the map equality to every
operator in the tensor block, including entangled positive inputs.

## Retention and adjoints

The retained map has blocks `(o,b)`, so its trace is exactly the sum of branch
traces. Sequential expansion gives

    sum_(o,r) Psi_r Phi_o=(sum_r Psi_r)(sum_o Phi_o),

and tensor expansion gives the analogous `(o,s)` formula.

For arbitrary finite-dimensional block linear maps, matrix units identify the
ordinary Hilbert--Schmidt pairing with a nondegenerate coordinate inner
product, so conjugate-transposing the superoperator coefficient matrix gives a
unique reverse adjoint. In the CP case this reduces to

    (Phi^(tr*)(y))_a=sum_(b,j)K_(ba,j)^*y_bK_(ba,j).

For discard `D(rho)=Tr(rho)` on `M_2`, `D^(tr*)(lambda)=lambda I_2`; input
trace one becomes output trace two. Thus unital CP does not imply reverse TNI.
