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
