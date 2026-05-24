Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

using ArithmeticQuantumMechanics

const RUN = "2026-05-24-projective-line-sheaf-fields"

_cell(x) = replace(string(x), "," => ";")

function write_summary()
    header = join((
        "example",
        "d",
        "p",
        "scheme",
        "sheaf",
        "rational_points",
        "point_count",
        "scalar_section_dim",
        "evaluation_rank",
        "evaluation_kernel_dim",
        "scalar_pairing_rank",
        "field_phase_dim",
        "symplectic_rank",
        "radical_dim",
        "reduced_phase_dim",
        "total_section_labels_exact",
        "evaluation_kernel_labels_exact",
        "radical_labels_exact",
        "reduced_weyl_labels_exact",
        "hilbert_dim_exact",
        "observable_basis_dim_exact",
        "nondegenerate",
    ), ",")
    path = data_path(RUN, "projective_line_sheaf_field_summary.csv")
    with_csv(path, header;
             sentinel="Exact F3 certificate for P1 sheaf-field examples H0(P1,O(d)) tensor F3^2, d=0..4; no Weyl matrices are built.") do io
        for row in projective_line_sheaf_field_summary_rows(; p=3, max_degree=4)
            println(io, join(_cell.([
                row.example,
                row.d,
                row.p,
                row.scheme,
                row.sheaf,
                row.rational_points,
                row.point_count,
                row.scalar_section_dim,
                row.evaluation_rank,
                row.evaluation_kernel_dim,
                row.scalar_pairing_rank,
                row.field_phase_dim,
                row.symplectic_rank,
                row.radical_dim,
                row.reduced_phase_dim,
                row.total_section_labels_exact,
                row.evaluation_kernel_labels_exact,
                row.radical_labels_exact,
                row.reduced_weyl_labels_exact,
                row.hilbert_dim_exact,
                row.observable_basis_dim_exact,
                row.nondegenerate,
            ]), ","))
        end
    end
    return path
end

function write_basis_rows()
    header = "example,d,row_kind,label,values"
    path = data_path(RUN, "projective_line_sheaf_field_basis_rows.csv")
    with_csv(path, header;
             sentinel="Basis-value rows and scalar Gram rows for the exact P1(F3), O(d), d=0..4 sheaf-field examples.") do io
        for row in projective_line_sheaf_field_basis_rows(; p=3, max_degree=4)
            println(io, join(_cell.([
                row.example,
                row.d,
                row.row_kind,
                row.label,
                row.values,
            ]), ","))
        end
    end
    return path
end

function main()
    for path in (write_summary(), write_basis_rows())
        println("wrote ", path)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
