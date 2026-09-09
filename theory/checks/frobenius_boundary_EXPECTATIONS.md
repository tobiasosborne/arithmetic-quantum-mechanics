# Preregistered exact falsifiers — Frobenius boundary

Written before the proof shards. Green calculations use integers, Fractions
and exact integer matrices only. Finite tests do not prove general positivity
or category existence. Every mutation must fail the named mathematical gate.

* B1: enumerate cyclic words on alphabets of sizes 2 and 3, lengths 1--6;
  compare exact-period counts with the divisor polynomial, and all power
  fixed counts with p^gcd(r,k). Separately enumerate polynomial field models
  F4 and F16; this does not silently assume a chosen normal basis.
  `--red-count` changes one divisor-polynomial coefficient.
* B2: derivatives at one equal phi(d), d=2--48; higher logarithmic
  derivatives equal the Jordan products, orders 1--6. Exact rational
  reference weights sum to one and are positive at 1001/1000, 3/2, 2, 3.
  The all-real proof uses a convergent exponential series, not these samples.
  `--red-weight` replaces phi(d) by d.
* B3: cycle matrix units and shifts give a noncommutative algebra; the
  rank-one state has return probability 1 before shift and 0 afterwards.
  `--red-frobenius` replaces the shift by identity.
* B4: the CRT cycle-pair bijection is bijective and intertwines simultaneous
  shift for d,e=1--8; triple associativity is checked after transporting both
  routes to the same Cartesian basis, d,e,f=1--4. A cross-orbit superposition
  in two degree-two cycles is transported through the actual B matrix and
  compared to the fixed Born return value one. All matrix units undergo
  the same computed transport. Classical orbit dephasing is applied inside
  the multiplicity coordinates and reduces the return to 1/2.
  `--red-coherence` inserts that dephasing. The independent data mutation
  replacing the pure input by its diagonal must also fail the Born test.
* B5: inclusion-sector weights, tower products and normalized success/failure
  channels on all matrix units for degrees 2|4|8. Four independent outcomes
  are checked on the tensor matrix-unit basis, including off-diagonal inputs.
  `--red-decoder` drops the retained failure branch.
* B6: multiplication counts over F2, F3 and F4, arities 1--3; overlapping
  controls use union cardinality. In F4, nonzero cuts fail to intertwine V;
  the all-nonfixed-label corner fails to be preserved by multiplication.
  `--red-overlap` replaces union cardinality by the sum of cardinalities.

The public checker advertises only the above mutation modes in --help.
