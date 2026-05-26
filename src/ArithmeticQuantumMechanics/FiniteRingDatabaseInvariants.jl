function finite_ring_additive_invariant_factors(
    R::FiniteRingStructureConstants,
)::Vector{Int}
    isempty(R.moduli) && return Int[]

    primary_parts = Dict{Int,Vector{Int}}()
    for modulus in R.moduli
        for (prime, exponent) in _frdb_trial_factorization(modulus)
            push!(get!(primary_parts, prime, Int[]), prime^exponent)
        end
    end

    factor_count = maximum(length, values(primary_parts); init=0)
    factors = ones(Int, factor_count)
    for prime_powers in values(primary_parts)
        sort!(prime_powers)
        offset = factor_count - length(prime_powers)
        for i in eachindex(prime_powers)
            factors[offset + i] *= prime_powers[i]
        end
    end
    filter!(!=(1), factors)
    sort!(factors)
    return factors
end

function finite_ring_basic_invariants(R::FiniteRingStructureConstants)::NamedTuple
    is_zero_ring = isempty(R.moduli)
    return (
        order_exact=finite_ring_order(R),
        characteristic_exact=finite_ring_characteristic_exact(R),
        additive_invariant_factors=finite_ring_additive_invariant_factors(R),
        local_status="unknown",
        reduced_status="unknown",
        field_status="unknown",
        product_status="unknown",
        maximal_ideals=is_zero_ring ? Any[] : :unknown,
        residue_field_sizes=is_zero_ring ? Int[] : :unknown,
        frobenius_status="unknown",
        generating_character_status="unknown",
    )
end

function _frdb_trial_factorization(n::Int)
    n > 0 || throw(ArgumentError("moduli must be positive integers"))
    factors = Pair{Int,Int}[]
    remaining = n
    exponent = 0
    while iseven(remaining)
        remaining = div(remaining, 2)
        exponent += 1
    end
    exponent > 0 && push!(factors, 2 => exponent)

    divisor = 3
    while divisor <= div(remaining, divisor)
        exponent = 0
        while mod(remaining, divisor) == 0
            remaining = div(remaining, divisor)
            exponent += 1
        end
        exponent > 0 && push!(factors, divisor => exponent)
        divisor += 2
    end
    remaining > 1 && push!(factors, remaining => 1)
    return factors
end
