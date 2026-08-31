const FINITE_RING_DATABASE_QUOTIENT_EXAMPLE_SOURCE_LOCATOR =
    "docs/finite_commutative_ring_database_prd.md lines 528-531; " *
    "CONVENTIONS.md (an) manual MVP constructors"

const FINITE_RING_DATABASE_QUOTIENT_BACKEND_SOURCE_LOCATOR =
    "references/finite_ring_database/SOURCES.md lines 134-206"

"""
    finite_ring_quotient_constructor_status(; ...)

Return the in-memory status for the MVP quotient-ring constructor slice.

This helper emits only the three PRD quotient examples through local core
structure-constant constructors. External quotient backends are reported as
available or explicitly skipped, but no backend completeness is certified.
"""
function finite_ring_quotient_constructor_status(;
    sage_path=Sys.which("sage"),
    oscar_available=Base.find_package("Oscar") !== nothing,
    nemo_available=Base.find_package("Nemo") !== nothing,
)::NamedTuple
    quotient_examples = [
        _frdb_quotient_example_row(
            "F_2[x]/(x^2+x)",
            finite_ring_product(finite_ring_prime_field(2), finite_ring_prime_field(2)),
            4,
            2,
        ),
        _frdb_quotient_example_row(
            "F_3[e]/(e^2)",
            finite_ring_dual_numbers(3),
            9,
            3,
        ),
        _frdb_quotient_example_row(
            "Z/6Z",
            finite_ring_zn(6),
            6,
            6,
        ),
    ]

    return (
        quotient_examples=quotient_examples,
        optional_backend_rows=[
            _frdb_quotient_backend_row("sage", _frdb_quotient_resolve_path(sage_path)),
            _frdb_quotient_backend_row("Oscar", oscar_available === true),
            _frdb_quotient_backend_row("Nemo", nemo_available === true),
        ],
        certifies_backend_completeness=false,
        source_locator=FINITE_RING_DATABASE_QUOTIENT_EXAMPLE_SOURCE_LOCATOR,
        backend_source_locator=FINITE_RING_DATABASE_QUOTIENT_BACKEND_SOURCE_LOCATOR,
    )
end

function _frdb_quotient_example_row(name, ring, expected_order, expected_characteristic)
    order = Int(expected_order)
    characteristic = Int(expected_characteristic)
    finite_ring_order(ring) == order ||
        error("quotient example $(name) has unexpected order")
    finite_ring_characteristic_exact(ring) == characteristic ||
        error("quotient example $(name) has unexpected characteristic")
    return (
        name=String(name),
        status="available",
        backend="local_core",
        expected_order=order,
        expected_characteristic=characteristic,
        ring=ring,
        source_locator=FINITE_RING_DATABASE_QUOTIENT_EXAMPLE_SOURCE_LOCATOR,
    )
end

function _frdb_quotient_backend_row(backend::AbstractString, available)
    is_available = available === true || available isa AbstractString
    return (
        backend=String(backend),
        status=is_available ? "available" : "skipped",
        reason=is_available ? nothing : "tool_not_available",
        tool_path=available isa AbstractString ? String(available) : nothing,
        certifies_completeness=false,
        source_locator=FINITE_RING_DATABASE_QUOTIENT_BACKEND_SOURCE_LOCATOR,
    )
end

function _frdb_quotient_resolve_path(path)
    path === nothing && return false
    candidate = strip(String(path))
    isempty(candidate) && return false
    isfile(candidate) && return candidate
    resolved = Sys.which(candidate)
    return resolved === nothing ? false : resolved
end
