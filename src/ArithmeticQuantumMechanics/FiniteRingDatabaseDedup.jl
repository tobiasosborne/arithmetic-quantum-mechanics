function finite_ring_find_isomorphism_certificate(
    source::FiniteRingStructureConstants,
    target::FiniteRingStructureConstants;
    max_order::Integer=64,
)::Union{Nothing,Matrix{Int}}
    _frdb_dedup_check_order_bound(source, target, max_order)

    source_rank = length(source.moduli)
    target_rank = length(target.moduli)
    target_elements = finite_ring_elements(target)
    rows = Vector{Int}[]

    function search_row(row_index::Int)
        if row_index > source_rank
            matrix = _frdb_dedup_rows_to_matrix(rows, source_rank, target_rank)
            check = finite_ring_verify_isomorphism_certificate(source, target, matrix)
            return check.ok ? matrix : nothing
        end

        for image in target_elements
            push!(rows, image)
            found = search_row(row_index + 1)
            pop!(rows)
            found === nothing || return found
        end
        return nothing
    end

    return search_row(1)
end

function finite_ring_deduplicate_small_rings(named_rings; max_order::Integer=64)::NamedTuple
    representatives = Pair{String,FiniteRingStructureConstants}[]
    representative_invariants = NamedTuple[]
    merges = NamedTuple[]

    for pair in named_rings
        name = String(first(pair))
        ring = last(pair)
        finite_ring_order(ring) <= max_order ||
            throw(ArgumentError("ring $(name) has order above max_order=$(max_order)"))
        invariants = _frdb_dedup_signature(ring)

        merged = false
        for i in eachindex(representatives)
            invariants == representative_invariants[i] || continue
            target_name, target_ring = representatives[i]
            certificate = finite_ring_find_isomorphism_certificate(
                ring,
                target_ring;
                max_order=max_order,
            )
            certificate === nothing && continue

            certificate_check = finite_ring_verify_isomorphism_certificate(
                ring,
                target_ring,
                certificate,
            )
            certificate_check.ok || error("internal error: dedup search returned bad certificate")
            push!(
                merges,
                (
                    source_name=name,
                    target_name=target_name,
                    certificate_matrix=certificate,
                    certificate_check=certificate_check,
                ),
            )
            merged = true
            break
        end

        if !merged
            push!(representatives, name => ring)
            push!(representative_invariants, invariants)
        end
    end

    return (representatives=representatives, merges=merges)
end

function _frdb_dedup_check_order_bound(source, target, max_order)
    bound = Int(max_order)
    bound >= 1 || throw(ArgumentError("max_order must be positive"))
    source_order = finite_ring_order(source)
    target_order = finite_ring_order(target)
    source_order <= bound ||
        throw(ArgumentError("source ring order $(source_order) exceeds max_order=$(bound)"))
    target_order <= bound ||
        throw(ArgumentError("target ring order $(target_order) exceeds max_order=$(bound)"))
    return nothing
end

function _frdb_dedup_signature(R::FiniteRingStructureConstants)::NamedTuple
    invariants = finite_ring_basic_invariants(R)
    return (
        order_exact=invariants.order_exact,
        characteristic_exact=invariants.characteristic_exact,
        additive_invariant_factors=invariants.additive_invariant_factors,
    )
end

function _frdb_dedup_rows_to_matrix(rows, source_rank::Int, target_rank::Int)::Matrix{Int}
    matrix = Matrix{Int}(undef, source_rank, target_rank)
    for i in 1:source_rank, j in 1:target_rank
        matrix[i, j] = rows[i][j]
    end
    return matrix
end
