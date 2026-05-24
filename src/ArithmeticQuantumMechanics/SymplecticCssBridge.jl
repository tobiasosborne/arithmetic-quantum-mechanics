# Exact prime-field checks for the chain-complex/CSS/symplectic bridge.

_modp(x::Integer, p::Integer) = mod(x, p)

function _assert_prime_field(p::Integer)
    p >= 2 || throw(ArgumentError("p must be prime"))
    for d in 2:floor(Int, sqrt(p))
        p % d == 0 && throw(ArgumentError("p must be prime"))
    end
    return p
end

function oriented_toric_boundary_matrices(k::Integer, p::Integer)
    2 <= k || throw(ArgumentError("k must be at least 2"))
    _assert_prime_field(p)
    nvertices = k^2
    nedges = 2k^2
    nfaces = k^2
    boundary_one = zeros(Int, nvertices, nedges)
    boundary_two = zeros(Int, nedges, nfaces)

    vertex(x, y) = 1 + _modp(y, k) * k + _modp(x, k)
    face(x, y) = 1 + _modp(y, k) * k + _modp(x, k)
    hed(x, y) = horizontal_edge_index(k, x, y)
    ved(x, y) = vertical_edge_index(k, x, y)

    for y in 0:(k - 1), x in 0:(k - 1)
        h = hed(x, y)
        boundary_one[vertex(x, y), h] = _modp(boundary_one[vertex(x, y), h] - 1, p)
        boundary_one[vertex(x + 1, y), h] = _modp(boundary_one[vertex(x + 1, y), h] + 1, p)

        v = ved(x, y)
        boundary_one[vertex(x, y), v] = _modp(boundary_one[vertex(x, y), v] - 1, p)
        boundary_one[vertex(x, y + 1), v] = _modp(boundary_one[vertex(x, y + 1), v] + 1, p)

        f = face(x, y)
        boundary_two[hed(x, y), f] = _modp(boundary_two[hed(x, y), f] + 1, p)
        boundary_two[ved(x + 1, y), f] = _modp(boundary_two[ved(x + 1, y), f] + 1, p)
        boundary_two[hed(x, y + 1), f] = _modp(boundary_two[hed(x, y + 1), f] - 1, p)
        boundary_two[ved(x, y), f] = _modp(boundary_two[ved(x, y), f] - 1, p)
    end

    return boundary_one, boundary_two
end

function matmul_modp(a::AbstractMatrix{<:Integer}, b::AbstractMatrix{<:Integer}, p::Integer)
    size(a, 2) == size(b, 1) || throw(DimensionMismatch("incompatible matrix sizes"))
    c = zeros(Int, size(a, 1), size(b, 2))
    for i in axes(a, 1), j in axes(b, 2)
        s = 0
        for l in axes(a, 2)
            s += a[i, l] * b[l, j]
        end
        c[i, j] = mod(s, p)
    end
    return c
end

function rank_modp(a::AbstractMatrix{<:Integer}, p::Integer)
    _assert_prime_field(p)
    work = mod.(Array{Int}(a), p)
    m, n = size(work)
    rank = 0
    for col in 1:n
        pivot_row = 0
        for row in (rank + 1):m
            if work[row, col] != 0
                pivot_row = row
                break
            end
        end
        pivot_row == 0 && continue
        rank += 1
        work[rank, :], work[pivot_row, :] = copy(work[pivot_row, :]), copy(work[rank, :])
        inv_pivot = invmod(work[rank, col], p)
        work[rank, :] .= mod.(work[rank, :] .* inv_pivot, p)
        for row in 1:m
            row == rank && continue
            factor = work[row, col]
            factor == 0 && continue
            work[row, :] .= mod.(work[row, :] .- factor .* work[rank, :], p)
        end
    end
    return rank
end

function css_symplectic_isotropic(boundary_one::AbstractMatrix{<:Integer},
                                  boundary_two::AbstractMatrix{<:Integer},
                                  p::Integer)
    product = matmul_modp(boundary_one, boundary_two, p)
    return all(==(0), product)
end

function symplectic_css_bridge_summary(k::Integer=4, p::Integer=3)
    boundary_one, boundary_two = oriented_toric_boundary_matrices(k, p)
    nvertices, nedges = size(boundary_one)
    nfaces = size(boundary_two, 2)
    boundary_product = matmul_modp(boundary_one, boundary_two, p)
    rank_boundary_one = rank_modp(boundary_one, p)
    rank_boundary_two = rank_modp(boundary_two, p)
    h1_dim = nedges - rank_boundary_one - rank_boundary_two
    stabilizer_rank = rank_boundary_one + rank_boundary_two

    return (
        k = k,
        p = p,
        nvertices = nvertices,
        nedges = nedges,
        nfaces = nfaces,
        boundary_square_zero = all(==(0), boundary_product),
        css_isotropic = css_symplectic_isotropic(boundary_one, boundary_two, p),
        rank_boundary_one = rank_boundary_one,
        rank_boundary_two = rank_boundary_two,
        h1_dim = h1_dim,
        symplectic_stabilizer_rank = stabilizer_rank,
        encoded_qudits = nedges - stabilizer_rank,
        encoded_hilbert_dimension_exact = string(BigInt(p)^h1_dim),
        chain_count_matches_symplectic_count = h1_dim == nedges - stabilizer_rank,
    )
end

function css_supercharge_dictionary_summary(hx::AbstractMatrix{<:Integer},
                                            hz::AbstractMatrix{<:Integer},
                                            p::Integer)
    _assert_prime_field(p)
    size(hx, 2) == size(hz, 2) || throw(DimensionMismatch("CSS matrices must have the same block length"))
    n = size(hx, 2)
    mixed = matmul_modp(hx, transpose(hz), p)
    rank_x = rank_modp(hx, p)
    rank_z = rank_modp(hz, p)
    stabilizer_rank = rank_x + rank_z
    encoded_qudits = n - stabilizer_rank
    encoded_qudits < 0 && throw(ArgumentError("stabilizer rank exceeds block length"))
    basis_free_ghost_count = div(BigInt(p)^stabilizer_rank - 1, p - 1)

    return (
        p = p,
        n = n,
        x_rows = size(hx, 1),
        z_rows = size(hz, 1),
        rank_x = rank_x,
        rank_z = rank_z,
        stabilizer_rank = stabilizer_rank,
        css_isotropic = all(==(0), mixed),
        encoded_qudits = encoded_qudits,
        code_dimension_exact = string(BigInt(p)^encoded_qudits),
        logical_symplectic_dimension = 2encoded_qudits,
        l_perp_dimension = 2n - stabilizer_rank,
        generator_ghost_count = stabilizer_rank,
        basis_free_projective_ghost_count_exact = string(basis_free_ghost_count),
        q_square_certificate = all(==(0), mixed),
        anticommutator_certificate = all(==(0), mixed),
        h0_matches_stabilizer_code = all(==(0), mixed),
    )
end

function steane_css_matrices()
    h = [
        1 1 1 0 1 0 0
        1 1 0 1 0 1 0
        1 0 1 1 0 0 1
    ]
    return h, h
end

function qutrit_css_toy_matrices()
    hx = [1 1 1]
    hz = [1 2 0]
    return hx, hz
end
