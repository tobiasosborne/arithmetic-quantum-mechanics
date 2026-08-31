const FINITE_RING_DATABASE_GAP_SMALL_RING_SOURCE_LOCATOR =
    "references/finite_ring_database/SOURCES.md lines 103-120; " *
    "references/finite_ring_database/gap_rings_chapter_56.html lines " *
    "472-477, 1041-1071, 1115-1131; " *
    "references/finite_ring_database/SOURCES.md lines 122-160"

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
        throw(ArgumentError("max_order must be a positive integer"))
    max_order >= 1 ||
        throw(ArgumentError("max_order must be a positive integer"))
    max_order <= FINITE_RING_DATABASE_GAP_SMALL_RING_MAX_ORDER ||
        throw(ArgumentError("max_order must be at most 15 for GAP SmallRing"))
    return Int(max_order)
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
    requested_max_order = _frdb_gap_small_ring_max_order(max_order)
    return """
    if not IsBoundGlobal("NumberSmallRings") then
      Print("AQM_FRDB_ERROR|missing_small_ring_counter|NumberSmallRings\\n");
      QUIT_GAP(1);
    fi;
    if not IsBoundGlobal("SmallRing") then
      Print("AQM_FRDB_ERROR|missing_small_ring_constructor|SmallRing\\n");
      QUIT_GAP(1);
    fi;
    if not IsBoundGlobal("Elements") then
      Print("AQM_FRDB_ERROR|missing_elements_operation|Elements\\n");
      QUIT_GAP(1);
    fi;
    if not IsBoundGlobal("IsCommutative") then
      Print("AQM_FRDB_ERROR|missing_commutativity_predicate|IsCommutative\\n");
      QUIT_GAP(1);
    fi;
    AqmFrdbTwoSidedIdentities := function(xs)
      local identities, e, x, is_identity;
      identities := [];
      for e in xs do
        is_identity := true;
        for x in xs do
          if not ((e * x = x) and (x * e = x)) then
            is_identity := false;
            break;
          fi;
        od;
        if is_identity then
          Add(identities, e);
        fi;
      od;
      return identities;
    end;;
    Print("AQM_FRDB_GAP_VERSION|", GAPInfo.Version, "\\n");
    for s in [1..$(requested_max_order)] do
      total := NumberSmallRings(s);
      scoped := 0;
      unital := 0;
      commutative := 0;
      for i in [1..total] do
        R := SmallRing(s, i);
        elements := Elements(R);
        if Length(elements) <> s then
          Print("AQM_FRDB_ERROR|element_count_mismatch|", s, "|", i, "|",
                Length(elements), "\\n");
          QUIT_GAP(1);
        fi;
        identities := AqmFrdbTwoSidedIdentities(elements);
        if Length(identities) > 1 then
          Print("AQM_FRDB_ERROR|multiple_two_sided_identities|", s, "|", i,
                "|", Length(identities), "\\n");
          QUIT_GAP(1);
        fi;
        has_one := Length(identities) = 1;
        if s = 1 and i = 1 and not has_one then
          Print("AQM_FRDB_ERROR|order_one_zero_ring_identity_inconsistent\\n");
          QUIT_GAP(1);
        fi;
        is_commutative := IsCommutative(R);
        if has_one then
          unital := unital + 1;
        fi;
        if is_commutative then
          commutative := commutative + 1;
        fi;
        if has_one and is_commutative then
          scoped := scoped + 1;
        fi;
      od;
      Print("AQM_FRDB_ROW|", s, "|", total, "|", scoped, "|", unital, "|",
            commutative, "\\n");
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
    length(fields) == 6 || error("malformed GAP small-ring status row: $(line)")
    order = parse(Int, fields[2])
    total_count = parse(Int, fields[3])
    scoped_count = parse(Int, fields[4])
    exact_unital_count = parse(Int, fields[5])
    commutative_count = parse(Int, fields[6])
    0 <= scoped_count <= exact_unital_count <= total_count ||
        error("invalid GAP small-ring scoped count in row: $(line)")
    scoped_count <= commutative_count <= total_count ||
        error("invalid GAP small-ring commutative count in row: $(line)")
    return (
        order=order,
        total_count=total_count,
        scoped_commutative_unital_count=scoped_count,
        exact_unital_count=exact_unital_count,
        commutative_count=commutative_count,
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
