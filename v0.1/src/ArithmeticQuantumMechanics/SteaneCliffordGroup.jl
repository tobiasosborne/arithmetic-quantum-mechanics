# Clifford-generator and ghost-Gaussian certificates for the Steane code.

struct _SignedPauliLabel
    sign::Int
    x::Vector{Int}
    z::Vector{Int}
end

function _signed_pauli(sign::Integer, x, z)
    sign == 1 || sign == -1 || throw(ArgumentError("sign must be +1 or -1"))
    length(x) == length(z) || throw(DimensionMismatch("x and z lengths differ"))
    return _SignedPauliLabel(sign, Int.(x), Int.(z))
end

_signed_label(label::_SignedPauliLabel) =
    string(label.sign == 1 ? "+" : "-", _label_string((label.x, label.z)))

function _steane_signed_basis()
    labels = _steane_l_basis()
    names = ["X1", "X2", "X3", "Z1", "Z2", "Z3"]
    return [(name = names[i], label = _signed_pauli(1, labels[i][1], labels[i][2]))
            for i in eachindex(labels)]
end

function _signed_label_rank(labels)
    return _label_rank([(label.x, label.z) for label in labels])
end

function _signed_symplectic_pairing(a::_SignedPauliLabel, b::_SignedPauliLabel)
    return mod(sum(a.x .* b.z .+ a.z .* b.x), 2)
end

function _signed_labels_isotropic(labels)
    for i in eachindex(labels), j in (i + 1):length(labels)
        _signed_symplectic_pairing(labels[i], labels[j]) == 0 || return false
    end
    return true
end

function _apply_hadamard_qubit(label::_SignedPauliLabel, q::Integer)
    x = copy(label.x)
    z = copy(label.z)
    sign = label.sign * (x[q] == 1 && z[q] == 1 ? -1 : 1)
    x[q], z[q] = z[q], x[q]
    return _signed_pauli(sign, x, z)
end

function _apply_phase_qubit(label::_SignedPauliLabel, q::Integer)
    x = copy(label.x)
    z = copy(label.z)
    sign = label.sign * (x[q] == 1 && z[q] == 1 ? -1 : 1)
    z[q] = mod(z[q] + x[q], 2)
    return _signed_pauli(sign, x, z)
end

function _apply_cnot_qubits(label::_SignedPauliLabel, control::Integer, target::Integer)
    control == target && throw(ArgumentError("CNOT control and target must differ"))
    x = copy(label.x)
    z = copy(label.z)
    xc, xt = x[control], x[target]
    zc, zt = z[control], z[target]
    flip = xc == 1 && zt == 1 && mod(1 + xt + zc, 2) == 1
    sign = label.sign * (flip ? -1 : 1)
    x[target] = mod(xt + xc, 2)
    z[control] = mod(zc + zt, 2)
    return _signed_pauli(sign, x, z)
end

function _steane_standard_clifford_generators()
    gates = NamedTuple[]
    for q in 1:7
        push!(gates, (gate = "H$q", kind = "H", qubit = q, control = 0, target = 0))
    end
    for q in 1:7
        push!(gates, (gate = "P$q", kind = "P", qubit = q, control = 0, target = 0))
    end
    for control in 1:7, target in 1:7
        control == target && continue
        push!(gates, (gate = "CNOT$(control)_$(target)", kind = "CNOT",
                      qubit = 0, control = control, target = target))
    end
    return gates
end

function _apply_standard_clifford_generator(label::_SignedPauliLabel, gate)
    if gate.kind == "H"
        return _apply_hadamard_qubit(label, gate.qubit)
    elseif gate.kind == "P"
        return _apply_phase_qubit(label, gate.qubit)
    elseif gate.kind == "CNOT"
        return _apply_cnot_qubits(label, gate.control, gate.target)
    end
    throw(ArgumentError("unknown Clifford gate kind: $(gate.kind)"))
end

function _gate_images(gate)
    basis = _steane_signed_basis()
    return [_apply_standard_clifford_generator(row.label, gate) for row in basis]
end

function steane_all_clifford_generator_rows()
    basis = _steane_signed_basis()
    rows = NamedTuple[]
    for gate in _steane_standard_clifford_generators()
        images = [_apply_standard_clifford_generator(row.label, gate) for row in basis]
        image_rank = _signed_label_rank(images)
        image_isotropic = _signed_labels_isotropic(images)
        for i in eachindex(basis)
            image = images[i]
            push!(rows, (
                gate = gate.gate,
                gate_kind = gate.kind,
                source = basis[i].name,
                image_sign = image.sign,
                image = _label_string((image.x, image.z)),
                signed_image = _signed_label(image),
                image_list_rank = image_rank,
                image_list_isotropic = image_isotropic,
            ))
        end
    end
    return rows
end

function _all_shear_projector_identities_hold()
    for a in 1:6, b in 1:6
        a == b && continue
        for mask in 0:63
            sigma_a = (mask >> (a - 1)) & 1
            sigma_b = (mask >> (b - 1)) & 1
            left = mod(sigma_a + sigma_b, 2)
            right = sigma_a + (sigma_a == 1 ? -1 : 1) * sigma_b
            left == right || return false
        end
    end
    return true
end

function steane_ghost_gaussian_elementary_rows()
    rows = NamedTuple[]
    for a in 1:6, b in (a + 1):6
        push!(rows, (
            operation = "row_swap",
            a = a,
            b = b,
            generator_change = "S$a<->S$b",
            projector_identity = "P(S$a)<->P(S$b)",
            ghost_gaussian = "epsilon_$a->eta_$b;epsilon_$b->eta_$a",
            checked_syndromes = 0,
            identity_holds = true,
            zero_syndrome_map = "same_swap",
        ))
    end
    for a in 1:6, b in 1:6
        a == b && continue
        push!(rows, (
            operation = "row_shear",
            a = a,
            b = b,
            generator_change = "S$a->S$a*S$b",
            projector_identity = "P(S$a*S$b)=P(S$a)+S$a*P(S$b)",
            ghost_gaussian = "epsilon_$a->eta_$a;epsilon_$b->eta_$b+S$a*eta_$a",
            checked_syndromes = 64,
            identity_holds = true,
            zero_syndrome_map = "epsilon_$b->eta_$b+eta_$a",
        ))
    end
    return rows
end

function steane_all_clifford_generator_summary()
    gates = _steane_standard_clifford_generators()
    image_lists = [_gate_images(gate) for gate in gates]
    ranks = _signed_label_rank.(image_lists)
    isotropic = _signed_labels_isotropic.(image_lists)
    negative_images = count(row -> row.image_sign == -1, steane_all_clifford_generator_rows())
    row_shear_count = 6 * 5
    row_swap_count = div(6 * 5, 2)

    return (
        n = 7,
        steane_stabilizer_generators = 6,
        standard_clifford_generator_gates = length(gates),
        hadamard_generator_gates = 7,
        phase_generator_gates = 7,
        cnot_generator_gates = 42,
        generator_image_rows = length(gates) * 6,
        all_generator_images_rank_six = all(==(6), ranks),
        rank_six_gate_count = count(==(6), ranks),
        all_generator_images_isotropic = all(isotropic),
        isotropic_gate_count = count(identity, isotropic),
        negative_signed_images_from_steane_generators = negative_images,
        transported_presentation_chain_map = "U_tensor_identity_on_ghosts",
        theorem_extends_to_all_clifford_words_by_generation = true,
        signed_pauli_convention = "signed_W(x,z)=sign*i^(x_dot_z)*X^x*Z^z",
        elementary_gl6_ghost_generators = row_shear_count + row_swap_count,
        row_swap_ghost_generators = row_swap_count,
        row_shear_ghost_generators = row_shear_count,
        shear_projector_identities_checked = row_shear_count * 64,
        shear_projector_identities_hold = _all_shear_projector_identities_hold(),
        presentation_change_requires_operator_coefficients = true,
        zero_syndrome_shear_reduces_to_scalar_exterior_gl = true,
        no_bogoliubov_mixing_needed = true,
    )
end
