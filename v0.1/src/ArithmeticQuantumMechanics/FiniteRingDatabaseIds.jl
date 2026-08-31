import SHA

"""
    finite_ring_database_canonical_json(value)::String

Return the deterministic JSON form used as finite-ring database ID input.

Supported payload values are `NamedTuple`s, dictionaries with `String` or
`Symbol` keys, vectors, tuples, strings, booleans, `nothing`, and integers.
Object keys are serialized in lexicographic order.
"""
function finite_ring_database_canonical_json(value)::String
    buffer = IOBuffer()
    _write_finite_ring_database_canonical_json(buffer, value)
    return String(take!(buffer))
end

finite_ring_presentation_id(payload)::String =
    "pres:" * _finite_ring_database_sha256_hex(payload)

finite_ring_certificate_id(payload)::String =
    "iso:" * _finite_ring_database_sha256_hex(payload)

function finite_ring_id(representative_payload, scope_payload)::String
    payload = (representative=representative_payload, scope=scope_payload)
    return "ring:" * _finite_ring_database_sha256_hex(payload)
end

function finite_ring_quantization_id(
    ring_id::AbstractString,
    layer::AbstractString,
    version::AbstractString,
)::String
    startswith(ring_id, "ring:") ||
        throw(ArgumentError("finite-ring quantization IDs require a ring:<sha256> ring_id"))
    _require_finite_ring_database_id_segment("layer", layer)
    _require_finite_ring_database_id_segment("version", version)
    return "quant:$(ring_id):$(layer):$(version)"
end

function _finite_ring_database_sha256_hex(payload)
    return bytes2hex(SHA.sha256(finite_ring_database_canonical_json(payload)))
end

function _write_finite_ring_database_canonical_json(io, value::NamedTuple)
    pairs = [(String(key), getfield(value, key)) for key in keys(value)]
    _write_finite_ring_database_json_object(io, pairs)
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value::AbstractDict)
    pairs = Tuple{String,Any}[]
    for (key, item) in value
        if key isa AbstractString
            push!(pairs, (String(key), item))
        elseif key isa Symbol
            push!(pairs, (String(key), item))
        else
            throw(ArgumentError("canonical JSON object keys must be strings or symbols"))
        end
    end
    _write_finite_ring_database_json_object(io, pairs)
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value::Union{AbstractVector,Tuple})
    print(io, '[')
    for (index, item) in enumerate(value)
        index == 1 || print(io, ',')
        _write_finite_ring_database_canonical_json(io, item)
    end
    print(io, ']')
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value::AbstractString)
    _write_finite_ring_database_json_string(io, value)
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value::Bool)
    print(io, value ? "true" : "false")
    return nothing
end

function _write_finite_ring_database_canonical_json(io, ::Nothing)
    print(io, "null")
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value::Integer)
    print(io, value)
    return nothing
end

function _write_finite_ring_database_canonical_json(io, value)
    throw(ArgumentError("unsupported canonical JSON value of type $(typeof(value))"))
end

function _write_finite_ring_database_json_object(io, pairs)
    sorted_pairs = sort(pairs; by=first)
    seen_keys = Set{String}()
    print(io, '{')
    for (index, (key, value)) in enumerate(sorted_pairs)
        key in seen_keys &&
            throw(ArgumentError("canonical JSON object key appears more than once: $(key)"))
        push!(seen_keys, key)
        index == 1 || print(io, ',')
        _write_finite_ring_database_json_string(io, key)
        print(io, ':')
        _write_finite_ring_database_canonical_json(io, value)
    end
    print(io, '}')
    return nothing
end

function _write_finite_ring_database_json_string(io, value::AbstractString)
    print(io, '"')
    for char in value
        if char == '"'
            print(io, "\\\"")
        elseif char == '\\'
            print(io, "\\\\")
        elseif Int(char) < 0x20
            print(io, "\\u", lpad(string(Int(char); base=16), 4, '0'))
        else
            print(io, char)
        end
    end
    print(io, '"')
    return nothing
end

function _require_finite_ring_database_id_segment(name, value)
    isempty(value) && throw(ArgumentError("finite-ring quantization $(name) must be nonempty"))
    occursin(':', value) && throw(ArgumentError("finite-ring quantization $(name) must not contain ':'"))
    return nothing
end
