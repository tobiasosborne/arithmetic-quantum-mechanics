function finite_ring_apply_generator_image_matrix(
    source::FiniteRingStructureConstants,
    target::FiniteRingStructureConstants,
    matrix,
    x,
)::Vector{Int}
    rows = _frdb_certificate_matrix(source, target, matrix)
    xs = _frdb_checked_element(source, "x", x)
    result = finite_ring_zero(target)
    for i in eachindex(source.moduli), j in eachindex(target.moduli)
        result[j] = mod(result[j] + xs[i] * rows[i][j], target.moduli[j])
    end
    return result
end

function finite_ring_verify_isomorphism_certificate(
    source::FiniteRingStructureConstants,
    target::FiniteRingStructureConstants,
    matrix,
)::NamedTuple
    failure_reasons = String[]
    rows = try
        _frdb_certificate_matrix(source, target, matrix)
    catch err
        reason = err isa ArgumentError ? sprint(showerror, err) : "invalid matrix"
        push!(failure_reasons, reason)
        return (
            ok=false,
            well_defined_additive_map=false,
            bijective_additive_map=false,
            identity_preserved=false,
            multiplication_preserved=false,
            failure_reasons=failure_reasons,
        )
    end

    well_defined = _frdb_certificate_additive_well_defined(source, target, rows)
    well_defined || push!(failure_reasons, "additive generator images are not well-defined")
    apply(x) = _frdb_certificate_apply_rows(source, target, rows, x)
    images = Set(Tuple(apply(x)) for x in finite_ring_elements(source))

    bijective = finite_ring_order(source) == finite_ring_order(target) &&
                length(images) == finite_ring_order(target)
    bijective || push!(failure_reasons, "additive map is not bijective")

    identity = apply(finite_ring_one(source)) == finite_ring_one(target)
    identity || push!(failure_reasons, "identity is not preserved")

    multiplicative = all(
        apply(finite_ring_mul(source, x, y)) == finite_ring_mul(target, apply(x), apply(y))
        for x in finite_ring_elements(source) for y in finite_ring_elements(source)
    )
    multiplicative || push!(failure_reasons, "multiplication is not preserved")

    ok = well_defined && bijective && identity && multiplicative
    return (
        ok=ok,
        well_defined_additive_map=well_defined,
        bijective_additive_map=bijective,
        identity_preserved=identity,
        multiplication_preserved=multiplicative,
        failure_reasons=failure_reasons,
    )
end

function _frdb_certificate_matrix(source, target, matrix)::Vector{Vector{Int}}
    source_rank = length(source.moduli)
    target_rank = length(target.moduli)
    rows = if matrix isa AbstractMatrix
        size(matrix) == (source_rank, target_rank) ||
            throw(ArgumentError("additive_generator_image_matrix has wrong shape"))
        [[Int(matrix[i, j]) for j in 1:target_rank] for i in 1:source_rank]
    elseif matrix isa AbstractVector
        length(matrix) == source_rank ||
            throw(ArgumentError("additive_generator_image_matrix has wrong row count"))
        [[Int(value) for value in row] for row in matrix]
    else
        throw(ArgumentError("additive_generator_image_matrix must be a matrix or vector of rows"))
    end

    for i in 1:source_rank
        length(rows[i]) == target_rank ||
            throw(ArgumentError("additive_generator_image_matrix row $i has wrong length"))
        _frdb_require_coordinates("additive_generator_image_matrix[$i]", target.moduli, rows[i])
    end
    return rows
end

function _frdb_certificate_additive_well_defined(source, target, rows)::Bool
    for i in eachindex(source.moduli), j in eachindex(target.moduli)
        mod(source.moduli[i] * rows[i][j], target.moduli[j]) == 0 || return false
    end
    return true
end

function _frdb_certificate_apply_rows(source, target, rows, x)::Vector{Int}
    xs = _frdb_checked_element(source, "x", x)
    result = finite_ring_zero(target)
    for i in eachindex(source.moduli), j in eachindex(target.moduli)
        result[j] = mod(result[j] + xs[i] * rows[i][j], target.moduli[j])
    end
    return result
end
