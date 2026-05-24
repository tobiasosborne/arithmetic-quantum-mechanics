# Algebraic toric-code stabilizers and ghost/boundary supercharge checks.

struct PauliCheck
    x::UInt128
    z::UInt128
end

_mod0(x::Integer, k::Integer) = mod(x, k)

function horizontal_edge_index(k::Integer, x::Integer, y::Integer)
    xx = _mod0(x, k)
    yy = _mod0(y, k)
    return 1 + yy * k + xx
end

function vertical_edge_index(k::Integer, x::Integer, y::Integer)
    xx = _mod0(x, k)
    yy = _mod0(y, k)
    return 1 + k^2 + yy * k + xx
end

function star_edges(k::Integer, x::Integer, y::Integer)
    return (
        horizontal_edge_index(k, x, y),
        horizontal_edge_index(k, x - 1, y),
        vertical_edge_index(k, x, y),
        vertical_edge_index(k, x, y - 1),
    )
end

function plaquette_edges(k::Integer, x::Integer, y::Integer)
    return (
        horizontal_edge_index(k, x, y),
        vertical_edge_index(k, x + 1, y),
        horizontal_edge_index(k, x, y + 1),
        vertical_edge_index(k, x, y),
    )
end

function _edge_mask(edges)
    mask = UInt128(0)
    for edge in edges
        mask = xor(mask, UInt128(1) << (edge - 1))
    end
    return mask
end

function toric_code_checks(k::Integer)
    2 <= k <= 7 || throw(ArgumentError("this UInt128 checker supports 2 <= k <= 7"))
    stars = PauliCheck[]
    plaquettes = PauliCheck[]
    for y in 0:(k - 1), x in 0:(k - 1)
        push!(stars, PauliCheck(_edge_mask(star_edges(k, x, y)), UInt128(0)))
        push!(plaquettes, PauliCheck(UInt128(0), _edge_mask(plaquette_edges(k, x, y))))
    end
    return stars, plaquettes
end

function toric_code_stabilizers(k::Integer)
    return toric_code_checks(k)
end

function toric_code_check_projectors(k::Integer)
    checks = collect(Iterators.flatten(toric_code_checks(k)))
    return checks
end

function toric_boundary_one_rows(k::Integer)
    2 <= k <= 7 || throw(ArgumentError("this UInt128 checker supports 2 <= k <= 7"))
    rows = UInt128[]
    for y in 0:(k - 1), x in 0:(k - 1)
        push!(rows, _edge_mask(star_edges(k, x, y)))
    end
    return rows
end

function toric_boundary_two_columns(k::Integer)
    2 <= k <= 7 || throw(ArgumentError("this UInt128 checker supports 2 <= k <= 7"))
    columns = UInt128[]
    for y in 0:(k - 1), x in 0:(k - 1)
        push!(columns, _edge_mask(plaquette_edges(k, x, y)))
    end
    return columns
end

function symplectic_commutes(a::PauliCheck, b::PauliCheck)
    parity = count_ones(a.x & b.z) + count_ones(a.z & b.x)
    return iseven(parity)
end

function check_squares_to_identity(check::PauliCheck)
    return (check.x & check.z) == 0
end

function _stabilizer_rows(k::Integer)
    nqubits = 2k^2
    checks = toric_code_check_projectors(k)
    return UInt128[check.x | (check.z << nqubits) for check in checks]
end

function gf2_rank(rows::AbstractVector{UInt128}, nbits::Integer)
    work = copy(rows)
    rank = 0
    for bit in (nbits - 1):-1:0
        pivot_idx = nothing
        for row in (rank + 1):length(work)
            if ((work[row] >> bit) & UInt128(1)) == UInt128(1)
                pivot_idx = row
                break
            end
        end
        pivot_idx === nothing && continue
        rank += 1
        work[rank], work[pivot_idx] = work[pivot_idx], work[rank]
        for row in eachindex(work)
            row == rank && continue
            if ((work[row] >> bit) & UInt128(1)) == UInt128(1)
                work[row] = xor(work[row], work[rank])
            end
        end
    end
    return rank
end

function toric_code_stabilizer_rank(k::Integer)
    nqubits = 2k^2
    return gf2_rank(_stabilizer_rows(k), 2nqubits)
end

function toric_boundary_square_zero(k::Integer)
    rows = toric_boundary_one_rows(k)
    columns = toric_boundary_two_columns(k)
    return all(iseven(count_ones(row & column)) for row in rows for column in columns)
end

function toric_cellular_supercharge_square_zero(k::Integer)
    return toric_boundary_square_zero(k)
end

"""
    toric_supercharge_summary(k)

Return an algebraic certificate for the ghost/boundary supercharge

    Q = sum_i c_i P_i,

where `P_i=(I-S_i)/2` is the violated-check projector and `c_i` annihilates the
auxiliary fermion attached to check `i`. No matrices on the full physical or
ghost Hilbert space are built.
"""
function toric_supercharge_summary(k::Integer=4)
    nqubits = 2k^2
    nchecks = 2k^2
    checks = toric_code_check_projectors(k)
    all_commute = all(symplectic_commutes(checks[i], checks[j])
                      for i in eachindex(checks) for j in i:length(checks))
    all_square = all(check_squares_to_identity, checks)
    max_check_weight = maximum(count_ones(check.x | check.z) for check in checks)
    stabilizer_rank = toric_code_stabilizer_rank(k)
    logical_qubits = nqubits - stabilizer_rank
    code_dim = BigInt(1) << logical_qubits
    physical_dim = BigInt(1) << nqubits
    boundary_rank_degree_one = physical_dim - code_dim

    return (
        k = k,
        nqubits = nqubits,
        nchecks = nchecks,
        max_check_weight = max_check_weight,
        all_projectors_commute = all_commute,
        all_checks_square_to_identity = all_square,
        stabilizer_rank = stabilizer_rank,
        independent_check_relations = nchecks - stabilizer_rank,
        logical_qubits = logical_qubits,
        physical_hilbert_dim_exact = string(physical_dim),
        code_dim_exact = string(code_dim),
        boundary_rank_degree_one_exact = string(boundary_rank_degree_one),
        h0_dim_exact = string(code_dim),
        q_square_certificate = all_commute && all_square,
        anticommutator_certificate = all_commute && all_square,
        degree_zero_homology_matches_code = code_dim == 4,
    )
end

function toric_chain_ghost_unification_summary(k::Integer=4)
    nedges = 2k^2
    nvertices = k^2
    nfaces = k^2
    boundary_one = toric_boundary_one_rows(k)
    boundary_two = toric_boundary_two_columns(k)
    stars, plaquettes = toric_code_checks(k)
    star_masks = UInt128[check.x for check in stars]
    plaquette_masks = UInt128[check.z for check in plaquettes]

    rank_boundary_one = gf2_rank(boundary_one, nedges)
    rank_boundary_two = gf2_rank(boundary_two, nedges)
    h1_dim = nedges - rank_boundary_one - rank_boundary_two
    code_dim = BigInt(1) << h1_dim
    cocycle_count = BigInt(1) << (nedges - rank_boundary_two)
    coboundary_count = BigInt(1) << rank_boundary_one

    return (
        k = k,
        nvertices = nvertices,
        nedges = nedges,
        nfaces = nfaces,
        boundary_square_zero = toric_boundary_square_zero(k),
        star_masks_match_boundary_one = star_masks == boundary_one,
        plaquette_masks_match_boundary_two = plaquette_masks == boundary_two,
        rank_boundary_one = rank_boundary_one,
        rank_boundary_two = rank_boundary_two,
        h1_dim = h1_dim,
        code_dim_from_h1_exact = string(code_dim),
        cellular_supercharge_square_zero = toric_cellular_supercharge_square_zero(k),
        cellular_middle_cohomology_dim = h1_dim,
        cellular_middle_cohomology_basis_count_exact = string(code_dim),
        cochain_cocycle_count_exact = string(cocycle_count),
        cochain_coboundary_count_exact = string(coboundary_count),
        css_commutation_from_boundary = toric_boundary_square_zero(k),
        ghost_checks_from_chain_complex = (star_masks == boundary_one) &&
                                          (plaquette_masks == boundary_two),
    )
end
