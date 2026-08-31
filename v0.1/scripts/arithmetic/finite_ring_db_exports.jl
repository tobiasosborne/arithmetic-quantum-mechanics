using ArithmeticQuantumMechanics

Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

const RUN = "2026-05-26-finite-ring-database"
const PRESENTATION_TYPE = "manual_mvp_structure_constants"
const PRESENTATION_SOURCE =
    "src/ArithmeticQuantumMechanics/FiniteRingDatabaseConstructors.jl " *
    "finite_ring_mvp_examples; CONVENTIONS.md (an)"
const CSV_SENTINEL =
    "in-memory MVP review export from local finite_ring_mvp_* helpers; " *
    "finite_rings.sqlite is not read or written; schema/index registration deferred to 16c"
const RING_SUMMARY_HEADER =
    "ring_id,representative_name,presentation_count,source_names,order_exact," *
    "characteristic_exact,additive_invariants_json,local_status,reduced_status," *
    "field_status,product_status,frobenius_status,generating_character_status," *
    "residue_field_sizes_json,audit_status"
const RING_PRESENTATIONS_HEADER =
    "presentation_id,name,canonical_ring_id,canonical_name,link_status,presentation_type," *
    "order_exact,characteristic_exact,additive_invariants_json,source_locator"
const CERTIFICATES_HEADER =
    "certificate_id,source_presentation_id,target_presentation_id,source_name,target_name," *
    "verdict,certificate_type,additive_generator_image_matrix_json,checked_by," *
    "checker_result,identity_preserved,addition_preserved,multiplication_preserved," *
    "bijective_additive_map"
const QUANTIZATION_SUMMARY_HEADER =
    "quantization_id,canonical_ring_id,presentation_name,layer,status,hilbert_dim_exact," *
    "label_group_order_exact,observable_basis_dim_exact,construction,source_locator,obstruction"
const QUANTIZATION_OBSTRUCTION_HEADER =
    "canonical_ring_id,presentation_name,layer,status,obstruction"

function csv_cell(value)
    value === nothing && return ""
    text = value isa Bool ? (value ? "true" : "false") : string(value)
    any(char -> occursin(char, text), (',', '"', '\n', '\r')) ||
        return text
    return "\"" * replace(text, "\"" => "\"\"") * "\""
end

csv_row(values...) = join(csv_cell.(values), ",")
json_cell(value) = finite_ring_database_canonical_json(value)
unknown_json(value) = value === :unknown ? json_cell("unknown") : json_cell(value)
maybe(record, field::Symbol) = field in propertynames(record) ? getfield(record, field) : ""

matrix_payload(matrix) =
    [[Int(matrix[i, j]) for j in axes(matrix, 2)] for i in axes(matrix, 1)]

products_payload(R) =
    [
        [[Int(R.products[i, j, k]) for k in 1:size(R.products, 3)] for j in 1:size(R.products, 2)]
        for i in 1:size(R.products, 1)
    ]

function id_segment(name)
    buffer = IOBuffer()
    for char in String(name)
        print(buffer, isletter(char) || isdigit(char) ? char : '_')
    end
    return "mvp_" * String(take!(buffer))
end

function presentation_payload(name, R)
    return (
        name=String(name),
        presentation_type=PRESENTATION_TYPE,
        additive_moduli=Int.(R.moduli),
        identity_coordinates=Int.(R.one),
        products=products_payload(R),
        source_locator=PRESENTATION_SOURCE,
    )
end

function export_context()
    examples = finite_ring_mvp_examples()
    dedup = finite_ring_deduplicate_small_rings(examples)
    presentations = [
        begin
            payload = presentation_payload(name, R)
            (
                name=String(name),
                ring=R,
                presentation_id=finite_ring_presentation_id(payload),
                invariants=finite_ring_basic_invariants(R),
            )
        end
        for (name, R) in examples
    ]
    by_name = Dict(row.name => row for row in presentations)
    canonical_name = Dict(row.name => row.name for row in presentations)
    link_status = Dict(row.name => "canonical" for row in presentations)
    source_names = Dict(String(name) => String[String(name)] for (name, _) in dedup.representatives)

    for merge in dedup.merges
        canonical_name[merge.source_name] = merge.target_name
        link_status[merge.source_name] = "certified_isomorphic_merge"
        push!(source_names[merge.target_name], merge.source_name)
    end

    scope = (commutative=true, unital=true, zero_ring_policy="include")
    ring_ids = Dict{String,String}()
    for (name, _) in dedup.representatives
        row = by_name[String(name)]
        inv = row.invariants
        payload = (
            representative_name=row.name,
            canonical_presentation_id=row.presentation_id,
            order_exact=inv.order_exact,
            characteristic_exact=inv.characteristic_exact,
            additive_invariant_factors=inv.additive_invariant_factors,
        )
        ring_ids[row.name] = finite_ring_id(payload, scope)
    end

    return (
        presentations=presentations,
        representatives=dedup.representatives,
        merges=dedup.merges,
        by_name=by_name,
        canonical_name=canonical_name,
        canonical_ring_id=Dict(row.name => ring_ids[canonical_name[row.name]] for row in presentations),
        link_status=link_status,
        source_names=source_names,
    )
end

function write_export(name, header, rows)
    path = data_path(RUN, name)
    with_csv(path, header; sentinel=CSV_SENTINEL) do io
        for row in rows
            println(io, csv_row(row...))
        end
    end
    return path
end

function ring_summary_rows(ctx)
    return [
        begin
            row = ctx.by_name[String(name)]
            inv = row.invariants
            names = ctx.source_names[row.name]
            (
                ctx.canonical_ring_id[row.name], row.name, length(names), json_cell(names),
                inv.order_exact, inv.characteristic_exact,
                json_cell(inv.additive_invariant_factors), inv.local_status,
                inv.reduced_status, inv.field_status, inv.product_status,
                inv.frobenius_status, inv.generating_character_status,
                unknown_json(inv.residue_field_sizes), "not_audited",
            )
        end
        for (name, _) in ctx.representatives
    ]
end

function ring_presentation_rows(ctx)
    return [
        begin
            inv = row.invariants
            (
                row.presentation_id, row.name, ctx.canonical_ring_id[row.name],
                ctx.canonical_name[row.name], ctx.link_status[row.name],
                PRESENTATION_TYPE, inv.order_exact, inv.characteristic_exact,
                json_cell(inv.additive_invariant_factors), PRESENTATION_SOURCE,
            )
        end
        for row in ctx.presentations
    ]
end

function certificate_rows(ctx)
    rows = Tuple[]
    for merge in ctx.merges
        source = ctx.by_name[merge.source_name]
        target = ctx.by_name[merge.target_name]
        matrix = matrix_payload(merge.certificate_matrix)
        check = merge.certificate_check
        verdict = check.ok ? "isomorphic" : "rejected"
        certificate_id = finite_ring_certificate_id((
            source_presentation_id=source.presentation_id,
            target_presentation_id=target.presentation_id,
            verdict=verdict,
            additive_generator_image_matrix=matrix,
        ))
        push!(
            rows,
            (
                certificate_id, source.presentation_id, target.presentation_id,
                merge.source_name, merge.target_name, verdict,
                "additive_generator_image_matrix", json_cell(matrix),
                "finite_ring_verify_isomorphism_certificate",
                check.ok ? "ok" : "failed", check.identity_preserved,
                check.well_defined_additive_map, check.multiplication_preserved,
                check.bijective_additive_map,
            ),
        )
    end
    return rows
end

function quantization_rows(ctx)
    records = vcat(
        finite_ring_mvp_residue_quantization_records(),
        finite_ring_mvp_thickened_frobenius_quantization_records(),
    )
    return [
        begin
            pname = String(name)
            (
                finite_ring_quantization_id(ctx.canonical_ring_id[pname], record.layer, id_segment(pname)),
                ctx.canonical_ring_id[pname], pname, record.layer, record.status,
                maybe(record, :hilbert_dim_exact), maybe(record, :label_group_order_exact),
                maybe(record, :observable_basis_dim_exact), maybe(record, :construction),
                maybe(record, :source_locator), maybe(record, :obstruction),
            )
        end
        for (name, record) in records
    ]
end

function main()
    ctx = export_context()
    qrows = quantization_rows(ctx)
    paths = String[
        write_export("ring_summary.csv", RING_SUMMARY_HEADER, ring_summary_rows(ctx)),
        write_export("ring_presentations.csv", RING_PRESENTATIONS_HEADER, ring_presentation_rows(ctx)),
        write_export("ring_isomorphism_certificates.csv", CERTIFICATES_HEADER, certificate_rows(ctx)),
        write_export("ring_quantization_summary.csv", QUANTIZATION_SUMMARY_HEADER, qrows),
        write_export(
            "ring_quantization_obstruction.csv",
            QUANTIZATION_OBSTRUCTION_HEADER,
            [(row[2], row[3], row[4], row[5], row[11]) for row in qrows if row[5] != "available"],
        ),
    ]
    println("finite_ring_db_exports.jl: wrote ", length(paths), " CSV files under ", current_run_dir(RUN))
    return paths
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
