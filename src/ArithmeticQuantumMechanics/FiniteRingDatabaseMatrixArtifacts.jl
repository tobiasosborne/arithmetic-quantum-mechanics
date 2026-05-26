function finite_ring_prime_field_weyl_matrix_materialization(
    p;
    matrix_dump_threshold,
    source_locator,
)::NamedTuple
    field_size = _frdb_matrix_prime_field_size(p)
    threshold = _frdb_matrix_dump_threshold(matrix_dump_threshold)
    source = _frdb_quantization_nonempty_string("source_locator", source_locator)

    if field_size > threshold
        return (
            layer="matrix_artifact",
            status="blocked",
            base_layer="residue",
            construction="prime_field_weyl_monomial_matrices",
            field_size=field_size,
            matrix_dump_threshold=threshold,
            obstruction="matrix_dump_threshold_exceeded",
            checks=(threshold=false,),
            source_locator=source,
        )
    end

    matrices = [
        _frdb_prime_field_weyl_monomial(field_size, q, m) for q in 0:(field_size - 1)
        for m in 0:(field_size - 1)
    ]
    algebra_checks = _frdb_prime_field_weyl_matrix_checks(field_size, matrices)
    checks = (
        threshold=true,
        multiplication=algebra_checks.multiplication,
        commutator=algebra_checks.commutator,
        unitarity=algebra_checks.unitarity,
        hilbert_schmidt_orthogonality=algebra_checks.hilbert_schmidt_orthogonality,
    )
    all(getfield(checks, key) for key in keys(checks)) ||
        error("prime-field Weyl matrix materialisation failed exact verification")

    payload = (
        field_size=field_size,
        hilbert_dim_exact=field_size,
        matrix_count_exact=field_size^2,
        basis_elements=collect(0:(field_size - 1)),
        operator_order="W(q,m)=T(q)R(m)",
        cyclotomic_encoding="zero_or_exponent_mod_p",
        monomial_encoding=(
            row_index_by_column="one_indexed_basis_order_0_to_p_minus_1",
            phase_exponent_by_column="zeta_p_exponent_mod_p",
        ),
        matrices=matrices,
    )
    sha = _finite_ring_database_sha256_hex(payload)

    return (
        layer="matrix_artifact",
        status="available",
        base_layer="residue",
        construction="prime_field_weyl_monomial_matrices",
        field_size=field_size,
        hilbert_dim_exact=field_size,
        matrix_count_exact=field_size^2,
        cyclotomic_encoding="zero_or_exponent_mod_p",
        matrix_payload=payload,
        checks=checks,
        artifact_id="matrix_artifact:$(sha)",
        artifact_path="matrix_artifacts/$(sha).json",
        source_locator=source,
    )
end

function _frdb_matrix_prime_field_size(p)::Int
    field_size = try
        Int(p)
    catch
        throw(ArgumentError("p must be a prime integer"))
    end
    _frdb_constructor_require_prime(field_size)
    return field_size
end

function _frdb_matrix_dump_threshold(value)::Int
    threshold = try
        Int(value)
    catch
        throw(ArgumentError("matrix_dump_threshold must be an integer"))
    end
    threshold >= 2 || throw(ArgumentError("matrix_dump_threshold must be at least 2"))
    return threshold
end

function _frdb_prime_field_weyl_monomial(p::Int, q::Int, m::Int)::NamedTuple
    row_index_by_column = [mod(s + q, p) + 1 for s in 0:(p - 1)]
    phase_exponent_by_column = [mod(m * s, p) for s in 0:(p - 1)]
    return (
        q=q,
        m=m,
        row_index_by_column=row_index_by_column,
        phase_exponent_by_column=phase_exponent_by_column,
    )
end

function _frdb_prime_field_weyl_matrix_checks(p::Int, matrices)::NamedTuple
    by_label = Dict((matrix.q, matrix.m) => matrix for matrix in matrices)
    multiplication = true
    commutator = true
    for q in 0:(p - 1), m in 0:(p - 1), q2 in 0:(p - 1), m2 in 0:(p - 1)
        left = _frdb_monomial_product(p, by_label[(q, m)], by_label[(q2, m2)])
        product_phase = mod(m * q2, p)
        product_target = by_label[(mod(q + q2, p), mod(m + m2, p))]
        multiplication &= _frdb_monomial_equal_up_to_scalar(
            p,
            left,
            product_target,
            product_phase,
        )

        right = _frdb_monomial_product(p, by_label[(q2, m2)], by_label[(q, m)])
        commutator_phase = mod(m * q2 - m2 * q, p)
        commutator &= _frdb_monomial_equal_up_to_scalar(p, left, right, commutator_phase)
    end

    return (
        multiplication=multiplication,
        commutator=commutator,
        unitarity=all(_frdb_monomial_unitary_shape(p, matrix) for matrix in matrices),
        hilbert_schmidt_orthogonality=_frdb_hilbert_schmidt_orthogonal(p, matrices),
    )
end

function _frdb_monomial_product(p::Int, left, right)::NamedTuple
    rows = Vector{Int}(undef, p)
    phases = Vector{Int}(undef, p)
    for column in 1:p
        middle = right.row_index_by_column[column]
        rows[column] = left.row_index_by_column[middle]
        phases[column] = mod(
            right.phase_exponent_by_column[column] + left.phase_exponent_by_column[middle],
            p,
        )
    end
    return (row_index_by_column=rows, phase_exponent_by_column=phases)
end

function _frdb_monomial_equal_up_to_scalar(p::Int, left, right, scalar_exponent::Int)::Bool
    left.row_index_by_column == right.row_index_by_column || return false
    return all(
        mod(left.phase_exponent_by_column[i] - right.phase_exponent_by_column[i], p) ==
        scalar_exponent for i in 1:p
    )
end

function _frdb_monomial_unitary_shape(p::Int, matrix)::Bool
    matrix.row_index_by_column isa Vector{Int} || return false
    matrix.phase_exponent_by_column isa Vector{Int} || return false
    length(matrix.row_index_by_column) == p || return false
    length(matrix.phase_exponent_by_column) == p || return false
    sort(matrix.row_index_by_column) == collect(1:p) || return false
    return all(exponent -> 0 <= exponent < p, matrix.phase_exponent_by_column)
end

function _frdb_hilbert_schmidt_orthogonal(p::Int, matrices)::Bool
    for i in eachindex(matrices), j in eachindex(matrices)
        same_matrix = i == j
        exponents = Int[]
        for column in 1:p
            if matrices[i].row_index_by_column[column] == matrices[j].row_index_by_column[column]
                push!(
                    exponents,
                    mod(
                        matrices[j].phase_exponent_by_column[column] -
                        matrices[i].phase_exponent_by_column[column],
                        p,
                    ),
                )
            end
        end
        if same_matrix
            length(exponents) == p || return false
            all(==(0), exponents) || return false
        elseif !isempty(exponents)
            counts = [count(==(exponent), exponents) for exponent in 0:(p - 1)]
            all(==(first(counts)), counts) || return false
        end
    end
    return true
end
