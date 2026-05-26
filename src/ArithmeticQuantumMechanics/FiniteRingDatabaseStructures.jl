struct FiniteRingStructureConstants
    moduli::Vector{Int}
    one::Vector{Int}
    products::Array{Int,3}
end

function finite_ring_structure_constants(moduli, one, products)::FiniteRingStructureConstants
    ds = _frdb_int_vector("moduli", moduli)
    identity = _frdb_int_vector("one", one)
    table = try
        Array{Int,3}(products)
    catch
        throw(ArgumentError("products must be a three-dimensional integer array"))
    end
    r = length(ds)

    size(table) == (r, r, r) ||
        throw(ArgumentError("products must have dimensions (rank, rank, rank)"))
    all(d -> d > 0, ds) || throw(ArgumentError("moduli must be positive integers"))
    length(identity) == r || throw(ArgumentError("one must have one coordinate per modulus"))
    _frdb_require_coordinates("one", ds, identity)
    for i in 1:r, j in 1:r, k in 1:r
        c = table[i, j, k]
        0 <= c < ds[k] ||
            throw(ArgumentError("products[$i,$j,$k] must be reduced modulo moduli[$k]"))
        mod(ds[i] * c, ds[k]) == 0 ||
            throw(ArgumentError("products[$i,$j,$k] is not compatible with modulus moduli[$i]"))
        mod(ds[j] * c, ds[k]) == 0 ||
            throw(ArgumentError("products[$i,$j,$k] is not compatible with modulus moduli[$j]"))
    end

    R = FiniteRingStructureConstants(ds, identity, table)
    _frdb_validate_unit(R)
    _frdb_validate_commutative(R)
    _frdb_validate_associative(R)
    return R
end

finite_ring_zero(R::FiniteRingStructureConstants) = zeros(Int, length(R.moduli))
finite_ring_one(R::FiniteRingStructureConstants) = copy(R.one)
finite_ring_order(R::FiniteRingStructureConstants) = prod(R.moduli; init=1)

function finite_ring_add(R::FiniteRingStructureConstants, x, y)
    xs = _frdb_checked_element(R, "x", x)
    ys = _frdb_checked_element(R, "y", y)
    return [mod(xs[i] + ys[i], R.moduli[i]) for i in eachindex(R.moduli)]
end

function finite_ring_neg(R::FiniteRingStructureConstants, x)
    xs = _frdb_checked_element(R, "x", x)
    return [mod(-xs[i], R.moduli[i]) for i in eachindex(R.moduli)]
end

function finite_ring_mul(R::FiniteRingStructureConstants, x, y)
    xs = _frdb_checked_element(R, "x", x)
    ys = _frdb_checked_element(R, "y", y)
    return _frdb_mul_coordinates(R, xs, ys)
end

function finite_ring_elements(R::FiniteRingStructureConstants)
    elements = Vector{Int}[Int[]]
    for d in R.moduli
        elements = [push!(copy(prefix), value) for prefix in elements for value in 0:(d - 1)]
    end
    return elements
end

function _frdb_int_vector(name, values)
    try
        return [Int(value) for value in values]
    catch
        throw(ArgumentError("$(name) must be an integer vector"))
    end
end

function _frdb_checked_element(R, name, values)
    xs = _frdb_int_vector(name, values)
    length(xs) == length(R.moduli) ||
        throw(ArgumentError("$(name) must have one coordinate per modulus"))
    _frdb_require_coordinates(name, R.moduli, xs)
    return xs
end

function _frdb_require_coordinates(name, moduli, xs)
    for i in eachindex(moduli)
        0 <= xs[i] < moduli[i] ||
            throw(ArgumentError("$(name)[$i] must be a canonical coordinate modulo moduli[$i]"))
    end
    return nothing
end

function _frdb_basis_vector(R, i)
    vector = finite_ring_zero(R)
    vector[i] = 1
    return vector
end

function _frdb_mul_coordinates(R, xs, ys)
    r = length(R.moduli)
    result = zeros(Int, r)
    for i in 1:r, j in 1:r
        factor = xs[i] * ys[j]
        iszero(factor) && continue
        for k in 1:r
            result[k] = mod(result[k] + factor * R.products[i, j, k], R.moduli[k])
        end
    end
    return result
end

function _frdb_validate_unit(R)
    for i in eachindex(R.moduli)
        e = _frdb_basis_vector(R, i)
        _frdb_mul_coordinates(R, R.one, e) == e ||
            throw(ArgumentError("one does not act as a left identity on basis element $i"))
        _frdb_mul_coordinates(R, e, R.one) == e ||
            throw(ArgumentError("one does not act as a right identity on basis element $i"))
    end
    return nothing
end

function _frdb_validate_commutative(R)
    r = length(R.moduli)
    for i in 1:r, j in 1:r
        R.products[i, j, :] == R.products[j, i, :] ||
            throw(ArgumentError("products table is not commutative at basis pair ($i,$j)"))
    end
    return nothing
end

function _frdb_validate_associative(R)
    r = length(R.moduli)
    basis = [_frdb_basis_vector(R, i) for i in 1:r]
    for i in 1:r, j in 1:r, k in 1:r
        left = _frdb_mul_coordinates(R, _frdb_mul_coordinates(R, basis[i], basis[j]), basis[k])
        right = _frdb_mul_coordinates(R, basis[i], _frdb_mul_coordinates(R, basis[j], basis[k]))
        left == right ||
            throw(ArgumentError("products table is not associative at basis triple ($i,$j,$k)"))
    end
    return nothing
end
