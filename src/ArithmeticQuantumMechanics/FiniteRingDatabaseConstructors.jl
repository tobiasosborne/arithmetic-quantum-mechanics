function finite_ring_characteristic_exact(R::FiniteRingStructureConstants)::Int
    characteristic = 1
    for (d, coordinate) in zip(R.moduli, R.one)
        characteristic = lcm(characteristic, div(d, gcd(d, coordinate)))
    end
    return characteristic
end

function finite_ring_zero_ring()
    return finite_ring_structure_constants(Int[], Int[], Array{Int,3}(undef, 0, 0, 0))
end

function finite_ring_zn(n)
    modulus = Int(n)
    modulus >= 2 || throw(ArgumentError("n must be at least 2 for the [n], [1] model"))
    products = zeros(Int, 1, 1, 1)
    products[1, 1, 1] = 1
    return finite_ring_structure_constants([modulus], [1], products)
end

function finite_ring_prime_field(p)
    prime = Int(p)
    _frdb_constructor_require_prime(prime)
    return finite_ring_zn(prime)
end

function finite_ring_dual_numbers(p)
    prime = Int(p)
    _frdb_constructor_require_prime(prime)
    products = zeros(Int, 2, 2, 2)
    products[1, 1, 1] = 1
    products[1, 2, 2] = 1
    products[2, 1, 2] = 1
    return finite_ring_structure_constants([prime, prime], [1, 0], products)
end

function finite_ring_product(factors::FiniteRingStructureConstants...)
    isempty(factors) && return finite_ring_zero_ring()

    total_rank = sum(length(factor.moduli) for factor in factors)
    moduli = Vector{Int}(undef, total_rank)
    one = Vector{Int}(undef, total_rank)
    products = zeros(Int, total_rank, total_rank, total_rank)

    offset = 0
    for factor in factors
        rank = length(factor.moduli)
        block = (offset + 1):(offset + rank)
        moduli[block] = factor.moduli
        one[block] = factor.one
        for i in 1:rank, j in 1:rank, k in 1:rank
            products[offset + i, offset + j, offset + k] = factor.products[i, j, k]
        end
        offset += rank
    end

    return finite_ring_structure_constants(moduli, one, products)
end

function finite_ring_mvp_examples()
    return [
        "zero_ring" => finite_ring_zero_ring(),
        "F_2" => finite_ring_prime_field(2),
        "F_3" => finite_ring_prime_field(3),
        "F_5" => finite_ring_prime_field(5),
        "Z/4Z" => finite_ring_zn(4),
        "Z/6Z" => finite_ring_zn(6),
        "Z/8Z" => finite_ring_zn(8),
        "Z/9Z" => finite_ring_zn(9),
        "F_2[e]/(e^2)" => finite_ring_dual_numbers(2),
        "F_3[e]/(e^2)" => finite_ring_dual_numbers(3),
        "F_2xF_2" => finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(2)),
        "F_2xF_3" => finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(3)),
        "F_3xF_3" => finite_ring_product(finite_ring_prime_field(3), finite_ring_prime_field(3)),
    ]
end

function _frdb_constructor_require_prime(p::Int)
    p >= 2 || throw(ArgumentError("p must be prime"))
    p == 2 && return nothing
    isodd(p) || throw(ArgumentError("p must be prime"))
    limit = isqrt(p)
    divisor = 3
    while divisor <= limit
        mod(p, divisor) == 0 && throw(ArgumentError("p must be prime"))
        divisor += 2
    end
    return nothing
end
