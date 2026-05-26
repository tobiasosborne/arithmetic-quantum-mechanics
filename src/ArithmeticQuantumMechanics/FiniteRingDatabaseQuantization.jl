function _frdb_quantization_nonempty_string(field, value)::String
    text = try
        String(value)
    catch
        throw(ArgumentError("$(field) must be a string"))
    end
    isempty(text) && throw(ArgumentError("$(field) must be nonempty"))
    return text
end

function _frdb_quantization_order_exact(value)::Int
    order = try
        Int(value)
    catch
        throw(ArgumentError("order_exact must be an integer"))
    end
    order >= 2 || throw(ArgumentError("order_exact must be at least 2"))
    return order
end

function finite_ring_residue_quantization_record(
    name::AbstractString,
    residue_field_sizes;
    source_locator::AbstractString,
)::NamedTuple
    dims = Int[Int(q) for q in residue_field_sizes]
    isempty(dims) && throw(ArgumentError("residue_field_sizes must be nonempty"))
    all(q -> q >= 2, dims) ||
        throw(ArgumentError("residue field sizes must be at least 2"))
    isempty(source_locator) && throw(ArgumentError("source_locator must be nonempty"))

    hilbert_dim = prod(dims; init=1)
    label_order = prod(q -> q^2, dims; init=1)
    return (
        name=String(name),
        layer="residue",
        status="available",
        residue_qudit_dims=dims,
        hilbert_dim_exact=hilbert_dim,
        label_group_order_exact=label_order,
        observable_basis_dim_exact=label_order,
        construction="residue_field_weyl_tensor_product",
        source_locator=String(source_locator),
    )
end

function finite_ring_blocked_residue_quantization_record(
    name,
    obstruction;
    status="blocked",
)::NamedTuple
    status_string = String(status)
    status_string in ("blocked", "not_applicable_until_layer_semantics") ||
        throw(ArgumentError("unsupported residue quantization status: $(status_string)"))
    obstruction_string = String(obstruction)
    isempty(obstruction_string) && throw(ArgumentError("obstruction must be nonempty"))
    return (
        name=String(name),
        layer="residue",
        status=status_string,
        obstruction=obstruction_string,
    )
end

function finite_ring_mvp_residue_quantization_records()::Vector{Pair{String,NamedTuple}}
    prime_field_source = "CONVENTIONS.md (u): finite affine spectrum/residue-qudit convention"
    z6_source =
        "report/sections/23_spec_z6_residue_qudit_factorisation.tex " *
        "(sec:spec-z6-residue-qudit-factorisation)"
    product_field_source =
        "CONVENTIONS.md (ad); " *
        "report/sections/40_product_field_spectrum_qudit_stabilizers.tex " *
        "(sec:product-field-spectrum-qudit-stabilizers)"
    missing_residue_obstruction =
        "missing_certified_maximal_ideal_decomposition_in_this_slice"

    records = Pair{String,NamedTuple}[
        "zero_ring" => finite_ring_blocked_residue_quantization_record(
            "zero_ring",
            "zero_ring_quantization_policy_not_applicable_until_layer_semantics",
            status="not_applicable_until_layer_semantics",
        ),
    ]
    for (name, p) in (("F_2", 2), ("F_3", 3), ("F_5", 5))
        push!(
            records,
            name => finite_ring_residue_quantization_record(
                name,
                [p];
                source_locator=prime_field_source,
            ),
        )
    end
    append!(
        records,
        [
            "Z/4Z" => finite_ring_blocked_residue_quantization_record(
                "Z/4Z",
                missing_residue_obstruction,
            ),
            "Z/6Z" => finite_ring_residue_quantization_record(
                "Z/6Z",
                [2, 3];
                source_locator=z6_source,
            ),
            "Z/8Z" => finite_ring_blocked_residue_quantization_record(
                "Z/8Z",
                missing_residue_obstruction,
            ),
            "Z/9Z" => finite_ring_blocked_residue_quantization_record(
                "Z/9Z",
                missing_residue_obstruction,
            ),
            "F_2[e]/(e^2)" => finite_ring_blocked_residue_quantization_record(
                "F_2[e]/(e^2)",
                missing_residue_obstruction,
            ),
            "F_3[e]/(e^2)" => finite_ring_blocked_residue_quantization_record(
                "F_3[e]/(e^2)",
                missing_residue_obstruction,
            ),
            "F_2xF_2" => finite_ring_residue_quantization_record(
                "F_2xF_2",
                [2, 2];
                source_locator=product_field_source,
            ),
            "F_2xF_3" => finite_ring_residue_quantization_record(
                "F_2xF_3",
                [2, 3];
                source_locator=product_field_source,
            ),
            "F_3xF_3" => finite_ring_residue_quantization_record(
                "F_3xF_3",
                [3, 3];
                source_locator=product_field_source,
            ),
        ],
    )
    return records
end

function finite_ring_thickened_frobenius_quantization_record(
    name,
    order_exact;
    source_locator,
    construction="aqm36_top_coefficient_artin_weyl_schrodinger",
)::NamedTuple
    name_string = _frdb_quantization_nonempty_string("name", name)
    order = _frdb_quantization_order_exact(order_exact)
    source = _frdb_quantization_nonempty_string("source_locator", source_locator)
    construction_string = _frdb_quantization_nonempty_string("construction", construction)
    label_order = order^2
    return (
        name=name_string,
        layer="thickened_frobenius",
        status="available",
        hilbert_dim_exact=order,
        label_group_order_exact=label_order,
        observable_basis_dim_exact=label_order,
        construction=construction_string,
        source_locator=source,
    )
end

function finite_ring_blocked_thickened_frobenius_quantization_record(
    name,
    obstruction;
    status="blocked",
)::NamedTuple
    name_string = _frdb_quantization_nonempty_string("name", name)
    status_string = _frdb_quantization_nonempty_string("status", status)
    status_string in ("blocked", "not_applicable_until_layer_semantics") ||
        throw(ArgumentError("unsupported thickened Frobenius quantization status: $(status_string)"))
    obstruction_string = _frdb_quantization_nonempty_string("obstruction", obstruction)
    return (
        name=name_string,
        layer="thickened_frobenius",
        status=status_string,
        obstruction=obstruction_string,
    )
end

function finite_ring_mvp_thickened_frobenius_quantization_records()::Vector{Pair{String,NamedTuple}}
    aqm36_source =
        "report/sections/36_nilpotent_thickening_weyl_fields.tex " *
        "(AQM-36; sec:nilpotent-thickening-weyl-fields)"
    missing_character_obstruction = "missing_certified_generating_character_in_this_slice"
    missing_policy_obstruction = "missing_thickened_frobenius_policy_in_this_slice"

    blocked(name, obstruction=missing_character_obstruction) =
        name => finite_ring_blocked_thickened_frobenius_quantization_record(name, obstruction)

    records = Pair{String,NamedTuple}[
        "zero_ring" => finite_ring_blocked_thickened_frobenius_quantization_record(
            "zero_ring",
            "zero_ring_quantization_policy_not_applicable_until_layer_semantics",
            status="not_applicable_until_layer_semantics",
        ),
        blocked("F_2"),
        blocked("F_3", missing_policy_obstruction),
        blocked("F_5"),
        blocked("Z/4Z"),
        blocked("Z/6Z"),
        blocked("Z/8Z"),
        blocked("Z/9Z"),
        blocked("F_2[e]/(e^2)"),
        "F_3[e]/(e^2)" => finite_ring_thickened_frobenius_quantization_record(
            "F_3[e]/(e^2)",
            9;
            source_locator=aqm36_source,
        ),
        blocked("F_2xF_2"),
        blocked("F_2xF_3"),
        blocked("F_3xF_3", missing_policy_obstruction),
    ]
    return records
end
