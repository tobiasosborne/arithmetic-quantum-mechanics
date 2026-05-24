# Exact finite-field certificates for arithmetic quantum field examples.

function _aqf_join_values(v)
    return join(string.(Int.(v)), " ")
end

function _aqf_gram(basis::AbstractMatrix{<:Integer}, p::Integer)
    _assert_prime_field(p)
    rows, points = size(basis)
    gram = zeros(Int, rows, rows)
    for i in 1:rows, j in 1:rows
        s = 0
        for x in 1:points
            s += basis[i, x] * basis[j, x]
        end
        gram[i, j] = mod(s, p)
    end
    return gram
end

function _aqf_symplectic_matrix(gram::AbstractMatrix{<:Integer}, p::Integer)
    m = size(gram, 1)
    out = zeros(Int, 2m, 2m)
    out[1:m, (m + 1):(2m)] .= mod.(-gram, p)
    out[(m + 1):(2m), 1:m] .= mod.(gram, p)
    return out
end

function _aqf_identity_matrix(n::Integer)
    out = zeros(Int, n, n)
    for i in 1:n
        out[i, i] = 1
    end
    return out
end

function _aqf_example(example::String, physical_space::String, field_space::String,
                      point_labels::Vector{String}, basis_labels::Vector{String},
                      basis::AbstractMatrix{<:Integer}; p::Integer=3)
    length(basis_labels) == size(basis, 1) || throw(DimensionMismatch("basis label count does not match basis rows"))
    length(point_labels) == size(basis, 2) || throw(DimensionMismatch("point label count does not match basis columns"))
    rank_modp(basis, p) == size(basis, 1) || throw(ArgumentError("scalar basis rows must be independent"))
    gram = _aqf_gram(basis, p)
    scalar_dim = size(basis, 1)
    scalar_rank = rank_modp(gram, p)
    field_dim = 2scalar_dim
    symplectic_rank = 2scalar_rank
    radical_dim = field_dim - symplectic_rank
    reduced_dim = symplectic_rank
    half_reduced_dim = div(reduced_dim, 2)
    total_field_labels = BigInt(p)^field_dim
    radical_labels = BigInt(p)^radical_dim
    reduced_weyl_labels = BigInt(p)^reduced_dim
    hilbert_dim = BigInt(p)^half_reduced_dim
    observable_basis = hilbert_dim^2

    return (
        example = example,
        p = p,
        physical_space = physical_space,
        field_space = field_space,
        point_count = length(point_labels),
        scalar_basis_dim = scalar_dim,
        scalar_pairing_rank = scalar_rank,
        field_phase_dim = field_dim,
        symplectic_rank = symplectic_rank,
        radical_dim = radical_dim,
        reduced_phase_dim = reduced_dim,
        total_field_labels_exact = string(total_field_labels),
        radical_labels_exact = string(radical_labels),
        reduced_weyl_labels_exact = string(reduced_weyl_labels),
        hilbert_dim_exact = string(hilbert_dim),
        observable_basis_dim_exact = string(observable_basis),
        nondegenerate = radical_dim == 0,
        point_labels = point_labels,
        basis_labels = basis_labels,
        basis = mod.(Array{Int}(basis), p),
        gram = gram,
        symplectic_matrix = _aqf_symplectic_matrix(gram, p),
    )
end

function arithmetic_quantum_field_examples()
    p = 3
    return [
        _aqf_example(
            "finite_two_points_all_maps",
            "two unstructured points",
            "all functions X -> F3^2, delta scalar basis",
            ["a", "b"],
            ["delta_a", "delta_b"],
            [1 0; 0 1]; p),
        _aqf_example(
            "finite_set_3_full",
            "three unstructured points",
            "all functions X -> F3^2, delta scalar basis",
            ["a", "b", "c"],
            ["delta_a", "delta_b", "delta_c"],
            [1 0 0; 0 1 0; 0 0 1]; p),
        _aqf_example(
            "vector_space_F3_linear",
            "X = F3",
            "F3-linear maps X -> F3^2, scalar basis t",
            ["0", "1", "2"],
            ["t"],
            reshape([0, 1, 2], 1, 3); p),
        _aqf_example(
            "vector_space_F3_affine",
            "X = F3",
            "affine maps X -> F3^2, scalar basis 1,t",
            ["0", "1", "2"],
            ["1", "t"],
            [1 1 1; 0 1 2]; p),
        _aqf_example(
            "vector_space_F3_poly_deg_le_2",
            "X = F3",
            "polynomial functions of degree <= 2, scalar basis 1,t,t^2",
            ["0", "1", "2"],
            ["1", "t", "t^2"],
            [1 1 1; 0 1 2; 0 1 1]; p),
        _aqf_example(
            "affine_plane_F3_linear",
            "X = F3^2",
            "linear coordinate functions, scalar basis x,y",
            ["(0,0)", "(0,1)", "(0,2)", "(1,0)", "(1,1)", "(1,2)", "(2,0)", "(2,1)", "(2,2)"],
            ["x", "y"],
            [0 0 0 1 1 1 2 2 2; 0 1 2 0 1 2 0 1 2]; p),
        _aqf_example(
            "affine_plane_F3_all_maps",
            "X = F3^2",
            "all functions X -> F3^2, delta scalar basis",
            ["(0,0)", "(0,1)", "(0,2)", "(1,0)", "(1,1)", "(1,2)", "(2,0)", "(2,1)", "(2,2)"],
            ["d00", "d01", "d02", "d10", "d11", "d12", "d20", "d21", "d22"],
            _aqf_identity_matrix(9); p),
        _aqf_example(
            "parabola_F3_constants",
            "X = {(x,y) in F3^2 : y = x^2}",
            "constant coordinate functions, scalar basis 1",
            ["(0,0)", "(1,1)", "(2,1)"],
            ["1"],
            reshape([1, 1, 1], 1, 3); p),
        _aqf_example(
            "parabola_F3_homogeneous_linear",
            "X = {(x,y) in F3^2 : y = x^2}",
            "homogeneous linear coordinate functions, scalar basis x,y",
            ["(0,0)", "(1,1)", "(2,1)"],
            ["x", "y"],
            [0 1 2; 0 1 1]; p),
        _aqf_example(
            "parabola_F3_degree_le_1",
            "X = {(x,y) in F3^2 : y = x^2}",
            "ambient degree <= 1 coordinate functions, scalar basis 1,x,y",
            ["(0,0)", "(1,1)", "(2,1)"],
            ["1", "x", "y"],
            [1 1 1; 0 1 2; 0 1 1]; p),
        _aqf_example(
            "torus_Gm_F3_laurent_0_1",
            "X = G_m(F3) = {1,2}",
            "Laurent coordinate functions, scalar basis 1,t",
            ["1", "2"],
            ["1", "t"],
            [1 1; 1 2]; p),
    ]
end

function arithmetic_quantum_field_summary_rows()
    return [(
        example = ex.example,
        p = ex.p,
        physical_space = ex.physical_space,
        field_space = ex.field_space,
        point_count = ex.point_count,
        scalar_basis_dim = ex.scalar_basis_dim,
        scalar_pairing_rank = ex.scalar_pairing_rank,
        field_phase_dim = ex.field_phase_dim,
        symplectic_rank = ex.symplectic_rank,
        radical_dim = ex.radical_dim,
        reduced_phase_dim = ex.reduced_phase_dim,
        total_field_labels_exact = ex.total_field_labels_exact,
        radical_labels_exact = ex.radical_labels_exact,
        reduced_weyl_labels_exact = ex.reduced_weyl_labels_exact,
        hilbert_dim_exact = ex.hilbert_dim_exact,
        observable_basis_dim_exact = ex.observable_basis_dim_exact,
        nondegenerate = ex.nondegenerate,
    ) for ex in arithmetic_quantum_field_examples()]
end

function arithmetic_quantum_field_basis_rows()
    rows = NamedTuple[]
    for ex in arithmetic_quantum_field_examples()
        for (i, label) in enumerate(ex.basis_labels)
            push!(rows, (
                example = ex.example,
                row_kind = "basis_values",
                label = label,
                values = _aqf_join_values(ex.basis[i, :]),
            ))
        end
        for i in axes(ex.gram, 1)
            push!(rows, (
                example = ex.example,
                row_kind = "scalar_gram_row",
                label = ex.basis_labels[i],
                values = _aqf_join_values(ex.gram[i, :]),
            ))
        end
    end
    return rows
end
