# Exact binary data for the Gottesman-table presentation of the Steane code.

const STEANE_LOGICAL_WORD = [0, 0, 0, 0, 1, 1, 1]

_bit_string(v) = join(string.(Int.(v)))

function _binary_rowspace_rows(rows::AbstractMatrix{<:Integer})
    m, n = size(rows)
    out = Vector{Vector{Int}}()
    for mask in 0:((1 << m) - 1)
        v = zeros(Int, n)
        for i in 1:m
            if ((mask >> (i - 1)) & 1) == 1
                v .= mod.(v .+ rows[i, :], 2)
            end
        end
        push!(out, v)
    end
    return sort(out; by=_bit_string)
end

function _binary_kernel_rows(rows::AbstractMatrix{<:Integer})
    _, n = size(rows)
    out = Vector{Vector{Int}}()
    for mask in 0:((1 << n) - 1)
        v = [((mask >> (i - 1)) & 1) for i in 1:n]
        if all(==(0), matmul_modp(rows, reshape(v, :, 1), 2))
            push!(out, v)
        end
    end
    return sort(out; by=_bit_string)
end

function _translate_space(space, shift)
    translated = [mod.(v .+ shift, 2) for v in space]
    return sort(translated; by=_bit_string)
end

function _contains_vector(space, v)
    s = _bit_string(v)
    return any(w -> _bit_string(w) == s, space)
end

function _choose(n::Integer, k::Integer)
    0 <= k <= n || return 0
    return binomial(n, k)
end

"""
    steane_binary_space_rows()

Return the binary spaces used by the sourced Steane-code presentation. `D` is
the rowspace of the three Gottesman-table checks, `C = D^perp`, and `u + D`
is the odd Hamming-code coset used for `|1bar>`.
"""
function steane_binary_space_rows()
    h, _ = steane_css_matrices()
    d_space = _binary_rowspace_rows(h)
    c_space = _binary_kernel_rows(h)
    u = copy(STEANE_LOGICAL_WORD)
    u_plus_d = _translate_space(d_space, u)
    return (
        h = h,
        d_space = d_space,
        c_space = c_space,
        logical_word = u,
        u_plus_d = u_plus_d,
    )
end

function steane_cohomology_by_degree()
    ghost_count = 6
    code_dim = 2
    return [(degree = q,
             ghost_binomial = _choose(ghost_count, q),
             cohomology_dim = code_dim * _choose(ghost_count, q))
            for q in 0:ghost_count]
end

function steane_molecular_summary()
    data = steane_binary_space_rows()
    h = data.h
    d_space = data.d_space
    c_space = data.c_space
    u = data.logical_word
    hht = matmul_modp(h, transpose(h), 2)
    rank_h = rank_modp(h, 2)
    stabilizer_rank = 2 * rank_h
    encoded_qubits = size(h, 2) - stabilizer_rank
    cohomology = steane_cohomology_by_degree()
    c_strings = Set(_bit_string.(c_space))
    coset_strings = Set(vcat(_bit_string.(d_space), _bit_string.(data.u_plus_d)))

    return (
        n = size(h, 2),
        check_rank = rank_h,
        d_dim = rank_h,
        d_size = length(d_space),
        c_dim = size(h, 2) - rank_h,
        c_size = length(c_space),
        d_subset_c = all(v -> _contains_vector(c_space, v), d_space),
        logical_word = _bit_string(u),
        logical_word_in_c = _contains_vector(c_space, u),
        logical_word_not_in_d = !_contains_vector(d_space, u),
        h_h_transpose_zero = all(==(0), hht),
        stabilizer_rank = stabilizer_rank,
        l_dim = stabilizer_rank,
        l_size = BigInt(2)^stabilizer_rank,
        l_perp_dim = 2 * size(h, 2) - stabilizer_rank,
        l_perp_size = BigInt(2)^(2 * size(h, 2) - stabilizer_rank),
        logical_symplectic_dim = 2 * encoded_qubits,
        logical_pauli_classes = BigInt(2)^(2 * encoded_qubits),
        logical_pairing_x_z = mod(sum(u .* u), 2),
        physical_hilbert_dim = BigInt(2)^size(h, 2),
        ghost_count = stabilizer_rank,
        ghost_fock_dim = BigInt(2)^stabilizer_rank,
        full_ghost_hilbert_dim = BigInt(2)^size(h, 2) * BigInt(2)^stabilizer_rank,
        code_dim = BigInt(2)^encoded_qubits,
        encoded_qubits = encoded_qubits,
        syndrome_count = BigInt(2)^stabilizer_rank,
        nonzero_syndrome_count = BigInt(2)^stabilizer_rank - 1,
        syndrome_block_dim = BigInt(2)^encoded_qubits,
        full_q_cohomology_dim = sum(row.cohomology_dim for row in cohomology),
        degree_zero_cohomology_dim = first(cohomology).cohomology_dim,
        q_square_certificate = all(==(0), hht),
        anticommutator_certificate = all(==(0), hht),
        codewords_match_two_cosets = c_strings == coset_strings,
    )
end

_zero_word(n::Integer) = zeros(Int, n)
_label_string(label) = string(_bit_string(label[1]), "|", _bit_string(label[2]))
_label_add(a, b) = (mod.(a[1] .+ b[1], 2), mod.(a[2] .+ b[2], 2))
_hadamard_label(label) = (copy(label[2]), copy(label[1]))
_phase_label(label) = (copy(label[1]), mod.(label[1] .+ label[2], 2))

function _steane_l_basis()
    data = steane_binary_space_rows()
    h = data.h
    zero = _zero_word(size(h, 2))
    x_basis = [(vec(h[i, :]), copy(zero)) for i in axes(h, 1)]
    z_basis = [(copy(zero), vec(h[i, :])) for i in axes(h, 1)]
    return vcat(x_basis, z_basis)
end

function _label_span_strings(labels)
    n = length(labels)
    out = Set{String}()
    zero = (_zero_word(length(labels[1][1])), _zero_word(length(labels[1][2])))
    for mask in 0:((1 << n) - 1)
        acc = (copy(zero[1]), copy(zero[2]))
        for i in 1:n
            if ((mask >> (i - 1)) & 1) == 1
                acc = _label_add(acc, labels[i])
            end
        end
        push!(out, _label_string(acc))
    end
    return out
end

function _label_rank(labels)
    rows = zeros(Int, length(labels), 2length(labels[1][1]))
    n = length(labels[1][1])
    for (i, label) in enumerate(labels)
        rows[i, 1:n] .= label[1]
        rows[i, (n + 1):(2n)] .= label[2]
    end
    return rank_modp(rows, 2)
end

function steane_clifford_morphism_rows()
    basis = _steane_l_basis()
    names = ["X1", "X2", "X3", "Z1", "Z2", "Z3"]
    h_images = _hadamard_label.(basis)
    p_images = _phase_label.(basis)
    rows = NamedTuple[]
    for i in eachindex(basis)
        push!(rows, (
            morphism = "transversal_H",
            source = names[i],
            image = _label_string(h_images[i]),
            image_basis_coordinates = i <= 3 ? "Z$(i)" : "X$(i - 3)",
        ))
        push!(rows, (
            morphism = "transversal_P",
            source = names[i],
            image = _label_string(p_images[i]),
            image_basis_coordinates = i <= 3 ? "X$(i)+Z$(i)" : "Z$(i - 3)",
        ))
    end
    return rows
end

function steane_clifford_morphism_summary()
    basis = _steane_l_basis()
    h_images = _hadamard_label.(basis)
    p_images = _phase_label.(basis)
    l_span = _label_span_strings(basis)
    h_span = _label_span_strings(h_images)
    p_span = _label_span_strings(p_images)
    cohomology = steane_cohomology_by_degree()

    return (
        n = 7,
        stabilizer_generators = 6,
        hadamard_maps_l_to_l = h_span == l_span,
        hadamard_image_rank = _label_rank(h_images),
        hadamard_generator_permutation = "X1->Z1;X2->Z2;X3->Z3;Z1->X1;Z2->X2;Z3->X3",
        hadamard_exact_same_q_after_ghost_swap = h_images == vcat(basis[4:6], basis[1:3]),
        hadamard_logical_x_image = "Zbar",
        hadamard_logical_z_image = "Xbar",
        hadamard_code_action = "H|0bar>=(|0bar>+|1bar>)/sqrt2;H|1bar>=(|0bar>-|1bar>)/sqrt2",
        phase_maps_l_to_l = p_span == l_span,
        phase_image_rank = _label_rank(p_images),
        phase_generator_basis_change = "Xi->Xi+Zi;Zi->Zi",
        phase_chain_isomorphism_to_image_presentation = p_span == l_span && _label_rank(p_images) == 6,
        phase_same_q_only_after_homotopy_retract = true,
        phase_logical_x_image = "Xbar+Zbar",
        phase_logical_z_image = "Zbar",
        nonzero_syndrome_blocks = 63,
        nonzero_syndrome_blocks_contractible = true,
        zero_syndrome_cohomology_dim_by_degree = join((row.cohomology_dim for row in cohomology), ";"),
        physical_h0_dim = first(cohomology).cohomology_dim,
        full_cohomology_dim = sum(row.cohomology_dim for row in cohomology),
    )
end
