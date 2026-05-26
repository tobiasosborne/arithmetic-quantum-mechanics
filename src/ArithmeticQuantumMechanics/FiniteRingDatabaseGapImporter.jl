const FINITE_RING_DATABASE_GAP_SMALL_RING_SOURCE_LOCATOR =
    "references/finite_ring_database/SOURCES.md lines 103-118; " *
    "references/finite_ring_database/gap_rings_chapter_56.html lines " *
    "472-477, 1041-1071, 1115-1131"

const FINITE_RING_DATABASE_GAP_SMALL_RING_MAX_ORDER = 15

function finite_ring_gap_small_ring_import_status(
    max_order;
    gap_path=Sys.which("gap"),
)::NamedTuple
    requested_max_order = _frdb_gap_small_ring_max_order(max_order)
    resolved_gap_path = _frdb_gap_path(gap_path)
    if resolved_gap_path === nothing
        return _frdb_gap_small_ring_skip_record(requested_max_order, gap_path)
    end

    gap_output = _frdb_run_gap_small_ring_status_script(
        resolved_gap_path,
        requested_max_order,
    )
    parsed = _frdb_parse_gap_small_ring_status_output(
        gap_output.stdout,
        gap_output.stderr,
        requested_max_order,
    )

    return (
        status="reconciled",
        reason=nothing,
        tool_name="GAP",
        tool_status="available",
        tool_path=resolved_gap_path,
        tool_version=parsed.tool_version,
        requested_max_order=requested_max_order,
        small_ring_library_max_order=FINITE_RING_DATABASE_GAP_SMALL_RING_MAX_ORDER,
        scope="finite_commutative_unital_rings_only",
        rows=parsed.rows,
        imported_presentations=NamedTuple[],
        certifies_completeness=false,
        source_locator=FINITE_RING_DATABASE_GAP_SMALL_RING_SOURCE_LOCATOR,
    )
end

function _frdb_gap_small_ring_max_order(max_order)::Int
    max_order isa Integer && !(max_order isa Bool) ||
        throw(ArgumentError("max_order must be a positive integer no larger than 15"))
    requested_max_order = try
        Int(max_order)
    catch
        throw(ArgumentError("max_order must be a positive integer no larger than 15"))
    end
    requested_max_order >= 1 ||
        throw(ArgumentError("max_order must be a positive integer"))
    requested_max_order <= FINITE_RING_DATABASE_GAP_SMALL_RING_MAX_ORDER ||
        throw(ArgumentError("max_order must be no larger than 15"))
    return requested_max_order
end

function _frdb_gap_path(gap_path)
    gap_path === nothing && return nothing
    candidate = strip(String(gap_path))
    isempty(candidate) && return nothing
    isfile(candidate) && return candidate
    resolved = Sys.which(candidate)
    return resolved === nothing ? nothing : resolved
end

function _frdb_gap_small_ring_skip_record(requested_max_order::Int, gap_path)::NamedTuple
    return (
        status="skipped",
        reason="gap_not_available",
        tool_name="GAP",
        tool_status="missing",
        requested_gap_path=gap_path === nothing ? nothing : String(gap_path),
        tool_path=nothing,
        tool_version=nothing,
        requested_max_order=requested_max_order,
        small_ring_library_max_order=FINITE_RING_DATABASE_GAP_SMALL_RING_MAX_ORDER,
        scope="finite_commutative_unital_rings_only",
        rows=NamedTuple[],
        imported_presentations=NamedTuple[],
        certifies_completeness=false,
        source_locator=FINITE_RING_DATABASE_GAP_SMALL_RING_SOURCE_LOCATOR,
    )
end

function _frdb_run_gap_small_ring_status_script(gap_path::AbstractString, max_order::Int)
    stdout = IOBuffer()
    stderr = IOBuffer()
    command = _frdb_gap_small_ring_command(gap_path)
    ok = try
        success(
            pipeline(
                command;
                stdin=IOBuffer(_frdb_gap_small_ring_status_script(max_order)),
                stdout=stdout,
                stderr=stderr,
            ),
        )
    catch err
        print(stderr, sprint(showerror, err))
        false
    end

    stdout_text = String(take!(stdout))
    stderr_text = String(take!(stderr))
    ok || error(_frdb_gap_small_ring_failure_message(gap_path, stdout_text, stderr_text))
    return (stdout=stdout_text, stderr=stderr_text)
end

function _frdb_gap_small_ring_command(gap_path::AbstractString)::Cmd
    return Cmd([String(gap_path), "--bare", "-q"])
end

function _frdb_gap_small_ring_status_script(max_order::Int)::String
    return """
    if not IsBoundGlobal("IsCommutative") then
      Print("AQM_FRDB_ERROR|missing_commutativity_predicate|IsCommutative\\n");
      QUIT;
    fi;
    if not IsBoundGlobal("IsRingWithOne") then
      Print("AQM_FRDB_ERROR|missing_unital_predicate|IsRingWithOne\\n");
      QUIT;
    fi;
    Print("AQM_FRDB_GAP_VERSION|", GAPInfo.Version, "\\n");
    for s in [1..$(max_order)] do
      total := NumberSmallRings(s);
      scoped := 0;
      for i in [1..total] do
        R := SmallRing(s, i);
        if s = 1 and i = 1 then
          scoped := scoped + 1;
        elif IsRingWithOne(R) and IsCommutative(R) then
          scoped := scoped + 1;
        fi;
      od;
      Print("AQM_FRDB_ROW|", s, "|", total, "|", scoped, "\\n");
    od;
    QUIT;
    """
end

function _frdb_parse_gap_small_ring_status_output(
    stdout::AbstractString,
    stderr::AbstractString,
    requested_max_order::Int,
)::NamedTuple
    tool_version = nothing
    rows = NamedTuple[]
    for raw_line in split(stdout, '\n')
        line = strip(raw_line)
        isempty(line) && continue
        if startswith(line, "AQM_FRDB_ERROR|")
            error(_frdb_gap_small_ring_failure_message("gap", stdout, stderr))
        elseif startswith(line, "AQM_FRDB_GAP_VERSION|")
            tool_version = split(line, '|'; limit=2)[2]
        elseif startswith(line, "AQM_FRDB_ROW|")
            push!(rows, _frdb_parse_gap_small_ring_row(line))
        end
    end

    expected_orders = collect(1:requested_max_order)
    observed_orders = [row.order for row in rows]
    if tool_version === nothing || observed_orders != expected_orders
        error(_frdb_gap_small_ring_failure_message("gap", stdout, stderr))
    end

    return (tool_version=tool_version, rows=rows)
end

function _frdb_parse_gap_small_ring_row(line::AbstractString)::NamedTuple
    fields = split(line, '|')
    length(fields) == 4 || error("malformed GAP small-ring status row: $(line)")
    order = parse(Int, fields[2])
    total_count = parse(Int, fields[3])
    scoped_count = parse(Int, fields[4])
    0 <= scoped_count <= total_count ||
        error("invalid GAP small-ring scoped count in row: $(line)")
    return (
        order=order,
        total_count=total_count,
        scoped_commutative_unital_count=scoped_count,
    )
end

function _frdb_gap_small_ring_failure_message(
    gap_path,
    stdout::AbstractString,
    stderr::AbstractString,
)::String
    return """
    GAP small-ring status query failed for $(gap_path).
    stdout:
    $(stdout)
    stderr:
    $(stderr)
    """
end
