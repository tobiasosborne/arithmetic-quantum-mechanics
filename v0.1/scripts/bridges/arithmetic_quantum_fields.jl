Base.include(@__MODULE__, joinpath(@__DIR__, "..", "_common.jl"))

using ArithmeticQuantumMechanics

const RUN = "2026-05-24-arithmetic-quantum-fields"

_cell(x) = replace(string(x), "," => ";")

function write_examples()
    header = join((
        "example",
        "p",
        "physical_space",
        "field_space",
        "point_count",
        "scalar_basis_dim",
        "scalar_pairing_rank",
        "field_phase_dim",
        "symplectic_rank",
        "radical_dim",
        "reduced_phase_dim",
        "total_field_labels_exact",
        "radical_labels_exact",
        "reduced_weyl_labels_exact",
        "hilbert_dim_exact",
        "observable_basis_dim_exact",
        "nondegenerate",
    ), ",")
    path = data_path(RUN, "arithmetic_quantum_field_examples.csv")
    with_csv(path, header;
             sentinel="Exact F3 arithmetic-field finite-function-space symplectic certificate; Weyl counts are label counts, no Hilbert matrices are built.") do io
        for row in arithmetic_quantum_field_summary_rows()
            println(io, join(_cell.([
                row.example,
                row.p,
                row.physical_space,
                row.field_space,
                row.point_count,
                row.scalar_basis_dim,
                row.scalar_pairing_rank,
                row.field_phase_dim,
                row.symplectic_rank,
                row.radical_dim,
                row.reduced_phase_dim,
                row.total_field_labels_exact,
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

function write_bases()
    header = "example,row_kind,label,values"
    path = data_path(RUN, "arithmetic_quantum_field_bases.csv")
    with_csv(path, header;
             sentinel="Basis value rows and scalar Gram rows for the exact F3 arithmetic-field examples.") do io
        for row in arithmetic_quantum_field_basis_rows()
            println(io, join(_cell.([
                row.example,
                row.row_kind,
                row.label,
                row.values,
            ]), ","))
        end
    end
    return path
end

function main()
    for path in (write_examples(), write_bases())
        println("wrote ", path)
    end
end

if abspath(PROGRAM_FILE) == @__FILE__
    main()
end
