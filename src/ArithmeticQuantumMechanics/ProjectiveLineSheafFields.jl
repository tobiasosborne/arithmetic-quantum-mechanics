# Exact F_p projective-line sheaf-field certificates.

function p1_rational_point_labels(p::Integer=3)
    _assert_prime_field(p)
    return vcat(["[1:0]"], ["[$t:1]" for t in 0:(p - 1)])
end

function _pl_pow_mod(x::Integer, n::Integer, p::Integer)
    n >= 0 || throw(ArgumentError("exponent must be nonnegative"))
    n == 0 && return 1
    return powermod(mod(x, p), n, p)
end

function _pl_factor_label(var::String, exp::Integer)
    exp == 0 && return ""
    exp == 1 && return var
    return string(var, "^", exp)
end

function _pl_monomial_label(d::Integer, i::Integer)
    xexp = d - i
    yexp = i
    parts = String[]
    x = _pl_factor_label("X", xexp)
    y = _pl_factor_label("Y", yexp)
    isempty(x) || push!(parts, x)
    isempty(y) || push!(parts, y)
    return isempty(parts) ? "1" : join(parts, "")
end

function p1_od_basis_labels(d::Integer)
    d >= 0 || throw(ArgumentError("d must be nonnegative"))
    return [_pl_monomial_label(d, i) for i in 0:d]
end

function p1_od_evaluation_matrix(d::Integer, p::Integer=3)
    d >= 0 || throw(ArgumentError("d must be nonnegative"))
    _assert_prime_field(p)
    values = zeros(Int, d + 1, p + 1)
    for i in 0:d
        xexp = d - i
        yexp = i
        values[i + 1, 1] = yexp == 0 ? 1 : 0
        for t in 0:(p - 1)
            values[i + 1, t + 2] = mod(_pl_pow_mod(t, xexp, p) * _pl_pow_mod(1, yexp, p), p)
        end
    end
    return values
end

function _pl_gram(values::AbstractMatrix{<:Integer}, p::Integer)
    rows, points = size(values)
    gram = zeros(Int, rows, rows)
    for i in 1:rows, j in 1:rows
        s = 0
        for x in 1:points
            s += values[i, x] * values[j, x]
        end
        gram[i, j] = mod(s, p)
    end
    return gram
end

function projective_line_sheaf_field_examples(; p::Integer=3, max_degree::Integer=4)
    _assert_prime_field(p)
    max_degree >= 0 || throw(ArgumentError("max_degree must be nonnegative"))
    point_labels = p1_rational_point_labels(p)
    rows = NamedTuple[]
    for d in 0:max_degree
        basis = p1_od_basis_labels(d)
        values = p1_od_evaluation_matrix(d, p)
        gram = _pl_gram(values, p)
        scalar_dim = d + 1
        eval_rank = rank_modp(values, p)
        gram_rank = rank_modp(gram, p)
        field_phase_dim = 2scalar_dim
        symplectic_rank = 2gram_rank
        radical_dim = field_phase_dim - symplectic_rank
        reduced_phase_dim = symplectic_rank
        evaluation_kernel_dim = scalar_dim - eval_rank
        half_reduced_dim = div(reduced_phase_dim, 2)
        total_section_labels = BigInt(p)^field_phase_dim
        evaluation_kernel_labels = BigInt(p)^(2evaluation_kernel_dim)
        radical_labels = BigInt(p)^radical_dim
        reduced_weyl_labels = BigInt(p)^reduced_phase_dim
        hilbert_dim = BigInt(p)^half_reduced_dim

        push!(rows, (
            example = "P1_F$(p)_O$(d)",
            d = d,
            p = p,
            scheme = "P1_F$p",
            sheaf = "O($d)",
            rational_points = join(point_labels, " "),
            point_count = length(point_labels),
            scalar_section_dim = scalar_dim,
            evaluation_rank = eval_rank,
            evaluation_kernel_dim = evaluation_kernel_dim,
            scalar_pairing_rank = gram_rank,
            field_phase_dim = field_phase_dim,
            symplectic_rank = symplectic_rank,
            radical_dim = radical_dim,
            reduced_phase_dim = reduced_phase_dim,
            total_section_labels_exact = string(total_section_labels),
            evaluation_kernel_labels_exact = string(evaluation_kernel_labels),
            radical_labels_exact = string(radical_labels),
            reduced_weyl_labels_exact = string(reduced_weyl_labels),
            hilbert_dim_exact = string(hilbert_dim),
            observable_basis_dim_exact = string(hilbert_dim^2),
            nondegenerate = radical_dim == 0,
            basis_labels = basis,
            values = values,
            gram = gram,
        ))
    end
    return rows
end

function projective_line_sheaf_field_summary_rows(; p::Integer=3, max_degree::Integer=4)
    return [(
        example = ex.example,
        d = ex.d,
        p = ex.p,
        scheme = ex.scheme,
        sheaf = ex.sheaf,
        rational_points = ex.rational_points,
        point_count = ex.point_count,
        scalar_section_dim = ex.scalar_section_dim,
        evaluation_rank = ex.evaluation_rank,
        evaluation_kernel_dim = ex.evaluation_kernel_dim,
        scalar_pairing_rank = ex.scalar_pairing_rank,
        field_phase_dim = ex.field_phase_dim,
        symplectic_rank = ex.symplectic_rank,
        radical_dim = ex.radical_dim,
        reduced_phase_dim = ex.reduced_phase_dim,
        total_section_labels_exact = ex.total_section_labels_exact,
        evaluation_kernel_labels_exact = ex.evaluation_kernel_labels_exact,
        radical_labels_exact = ex.radical_labels_exact,
        reduced_weyl_labels_exact = ex.reduced_weyl_labels_exact,
        hilbert_dim_exact = ex.hilbert_dim_exact,
        observable_basis_dim_exact = ex.observable_basis_dim_exact,
        nondegenerate = ex.nondegenerate,
    ) for ex in projective_line_sheaf_field_examples(; p, max_degree)]
end

function projective_line_sheaf_field_basis_rows(; p::Integer=3, max_degree::Integer=4)
    rows = NamedTuple[]
    for ex in projective_line_sheaf_field_examples(; p, max_degree)
        for (i, label) in enumerate(ex.basis_labels)
            push!(rows, (
                example = ex.example,
                d = ex.d,
                row_kind = "basis_values",
                label = label,
                values = _aqf_join_values(ex.values[i, :]),
            ))
        end
        for i in axes(ex.gram, 1)
            push!(rows, (
                example = ex.example,
                d = ex.d,
                row_kind = "scalar_gram_row",
                label = ex.basis_labels[i],
                values = _aqf_join_values(ex.gram[i, :]),
            ))
        end
    end
    return rows
end

function _pl_frame_string(chart_var::String, d::Integer)
    return "e_$(chart_var)^($d)"
end

function _pl_germ_string(coord::String, exp::Integer, frame::String)
    if exp == 0
        return frame
    elseif exp == 1
        return "$(coord)*$(frame)"
    else
        return "$(coord)^$(exp)*$(frame)"
    end
end

function _pl_finite_prime_string(t::Integer, p::Integer)
    if t == 0
        return "(X)"
    elseif p == 3 && t == 1
        return "(X-Y)"
    elseif p == 3 && t == 2
        return "(X-2Y)=(X+Y)"
    else
        return "(X-$(t)Y)"
    end
end

function _pl_finite_maximal_ideal_string(t::Integer)
    return t == 0 ? "(v)" : "(v-$t)"
end

function _pl_rational_stalk_points(p::Integer)
    points = NamedTuple[(
        point_label = "[1:0]",
        homogeneous_prime = "(Y)",
        chart = "D_+(X)",
        local_coordinate = "u=Y/X",
        coordinate_symbol = "u",
        coordinate_value = 0,
        local_maximal_ideal = "(u)",
        local_ring = "F$(p)[u]_(u)",
        frame_symbol = "X",
        is_infinity = true,
    )]
    for t in 0:(p - 1)
        push!(points, (
            point_label = "[$t:1]",
            homogeneous_prime = _pl_finite_prime_string(t, p),
            chart = "D_+(Y)",
            local_coordinate = "v=X/Y",
            coordinate_symbol = "v",
            coordinate_value = t,
            local_maximal_ideal = _pl_finite_maximal_ideal_string(t),
            local_ring = "F$(p)[v]_$(_pl_finite_maximal_ideal_string(t))",
            frame_symbol = "Y",
            is_infinity = false,
        ))
    end
    return points
end

function projective_line_stalk_rows(; p::Integer=3, max_degree::Integer=4)
    _assert_prime_field(p)
    max_degree >= 0 || throw(ArgumentError("max_degree must be nonnegative"))
    rows = NamedTuple[]
    for d in 0:max_degree
        labels = p1_od_basis_labels(d)
        for point in _pl_rational_stalk_points(p)
            frame = _pl_frame_string(point.frame_symbol, d)
            for i in 0:d
                xexp = d - i
                yexp = i
                local_exp = point.is_infinity ? yexp : xexp
                residue = point.is_infinity ? (yexp == 0 ? 1 : 0) :
                          _pl_pow_mod(point.coordinate_value, xexp, p)
                push!(rows, (
                    d = d,
                    point_label = point.point_label,
                    homogeneous_prime = point.homogeneous_prime,
                    chart = point.chart,
                    local_coordinate = point.local_coordinate,
                    local_maximal_ideal = point.local_maximal_ideal,
                    local_ring = point.local_ring,
                    residue_field = "F$p",
                    local_frame = frame,
                    basis_label = labels[i + 1],
                    x_exponent = xexp,
                    y_exponent = yexp,
                    germ_in_frame = _pl_germ_string(point.coordinate_symbol, local_exp, frame),
                    residue_value = residue,
                ))
            end
        end
    end
    return rows
end
