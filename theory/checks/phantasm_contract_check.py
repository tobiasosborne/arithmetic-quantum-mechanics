#!/usr/bin/env python3
"""Check the Phantasm Markdown contracts, not mathematical truth.

Runs read-only against the repository (or --root). Every --red-* option
changes a copy of actual input data and must fail at its declared gate.
Source bodies must first be retrieved using scripts/fetch-phantasm-sources.py.
"""
import argparse
import copy
import hashlib
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {'Title', 'Status', 'Stage', 'Definitions', 'Dependencies',
            'Sources', 'Inputs', 'Output', 'Choices', 'Scope', 'Proof',
            'Review', 'Checks', 'Evidence', 'Inherited', 'Reuse', 'Remaining'}
STATUSES = {'PROVED', 'SKETCH', 'CONJECTURE', 'REFUTED'}
MUTATIONS = {
    'duplicate-node': 'G1', 'empty-scope': 'G1',
    'missing-node': 'G2', 'missing-definition': 'G2', 'status': 'G2',
    'orphan-claim': 'G2', 'decision-input': 'G2',
    'cycle': 'G3', 'decision-cycle': 'G3',
    'refuted': 'G4', 'promote': 'G4',
    'source-hash': 'G5', 'source-gap': 'G5',
    'labbook': 'G6', 'definition-drift': 'G6',
    'notation-alias': 'G7', 'notation-owner': 'G7',
    'inherited-status': 'G8', 'untracked-reuse': 'G8',
    'definition-reuse': 'G8', 'definition-cycle': 'G8',
}


class ContractFailure(Exception):
    def __init__(self, gate, detail):
        self.gate, self.detail = gate, detail


def require(condition, gate, detail):
    if not condition:
        raise ContractFailure(gate, detail)


def norm(text):
    return ' '.join(text.split())


def csv(text):
    return [] if text == 'none' else [s.strip() for s in text.split(',')]


def cells(line):
    return [s.strip() for s in re.split(r'(?<!\\)\|', line.strip())[1:-1]]


def table(text, header):
    rows, active = [], False
    for line in text.splitlines():
        if not line.startswith('|'):
            active = False
            continue
        row = cells(line)
        if row and row[0].lower() == header:
            active = True
            continue
        if active and row and not re.fullmatch(r':?-+:?', row[0]):
            rows.append(row)
    return rows


def read_inputs(root):
    def read(path):
        return (root / path).read_text()
    data = {
        'claims_text': read('claims/CLAIMS.md'),
        'dag_text': read('claims/PHANTASM-DAG.md'),
        'defs_text': read('definitions.md'),
        'ledger_text': read('refs/LEDGER.md'),
        'plan': read('docs/research-plans/symplectic-phantasm.md'),
        'notation': read('notation.md'), 'main': read('labbook/main.tex'),
        'tex': '\n'.join(read('labbook/sections/' + name + '.tex') for name in
                         ('symplectic_phantasm', 'symplectic_phantasm_contracts')),
    }
    return data


def parse(data):
    claims = {}
    for row in table(data['claims_text'], 'id'):
        cid = row[0].strip('`* ')
        require(cid not in claims, 'G1', 'duplicate canonical claim ' + cid)
        require(len(row) >= 6, 'G1', 'malformed canonical row ' + cid)
        claims[cid] = dict(statement=row[1], status=row[2].strip('`* '),
                           deps=row[3], proof_cell=row[4])
    nodes = {}
    for match in re.finditer(r'^## (SP-[A-Z0-9-]+)\n(.*?)(?=^## |\Z)',
                             data['dag_text'], re.M | re.S):
        cid, body = match.groups()
        require(cid not in nodes, 'G1', 'duplicate DAG node ' + cid)
        fields = re.findall(r'^- ([A-Za-z]+): (.*)$', body, re.M)
        require(len(fields) == len(dict(fields)), 'G1', 'duplicate field ' + cid)
        node = dict(fields)
        require(node.keys() == REQUIRED, 'G1', 'missing/unknown fields ' + cid)
        require(all(v.strip() for v in node.values()), 'G1', 'empty field ' + cid)
        require(node['Status'] in STATUSES and node['Stage'].isdigit(),
                'G1', 'bad status/stage ' + cid)
        require(node['Evidence'] in {'planned', 'draft', 'admitted'}, 'G1', 'bad evidence state ' + cid)
        for label in ('Construction outline', 'Falsifier scope', 'Required mutations'):
            require(re.search(r'\*\*' + label + r'\.\*\* \S', body),
                    'G1', 'missing ' + label + ': ' + cid)
        nodes[cid] = node
    require(nodes, 'G1', 'no Phantasm contracts found')
    defs = {}
    for match in re.finditer(r'^## (D\d+) ([^\n]*)\n(.*?)(?=^## D\d+ |\Z)',
                             data['defs_text'], re.M | re.S):
        did, title, body = match.groups()
        require(did not in defs, 'G1', 'duplicate definition ' + did)
        defs[did] = dict(title=title.strip('()'), body=body)
    sources, gaps = {}, set()
    for row in table(data['ledger_text'], 'source-id'):
        key, state = row[:2]
        require(key not in sources and key not in gaps, 'G1', 'duplicate source ' + key)
        if state == 'GAP':
            gaps.add(key)
        else:
            require(len(row) == 6 and state == 'LOCAL', 'G1', 'malformed source ' + key)
            sources[key] = dict(zip(('id', 'state', 'raw', 'raw_sha', 'readable', 'readable_sha'), row))
    order = table(data['dag_text'], 'claim')
    decisions = {}
    for row in table(data['dag_text'], 'decision'):
        require(len(row) == 5 and all(row), 'G1', 'malformed decision gate')
        key, deps, refs, output, state = row
        require(key.startswith('DG-') and key not in decisions and state == 'OPEN',
                'G1', 'duplicate or unsupported decision state ' + key)
        decisions[key] = dict(deps=csv(deps), sources=csv(refs), output=output)
    require(decisions, 'G1', 'no research decision gates recorded')
    data.update(claims=claims, nodes=nodes, defs=defs, sources=sources,
                gaps=gaps, order=order, decisions=decisions)
    return data


def mutate(data, mutation):
    if not mutation:
        return data
    d = copy.deepcopy(data)
    cid = 'SP-WEYL'
    if mutation == 'missing-node':
        d['nodes'][cid]['Dependencies'] = 'SP-MISSING'
    elif mutation == 'missing-definition':
        del d['defs']['D1703']
    elif mutation == 'status':
        d['nodes'][cid]['Status'] = 'CONJECTURE'
    elif mutation == 'orphan-claim':
        d['claims']['SP-ORPHAN'] = copy.deepcopy(d['claims'][cid])
    elif mutation == 'cycle':
        d['nodes'][cid]['Dependencies'] = ','.join(csv(d['nodes'][cid]['Dependencies']) + ['SP-EGOROV'])
        d['claims'][cid]['deps'] += ',SP-EGOROV'
    elif mutation == 'decision-input':
        d['decisions']['DG-GLOBAL']['deps'].append('DG-MISSING')
    elif mutation == 'decision-cycle':
        d['decisions']['DG-GLOBAL']['deps'].append('DG-SPECTRUM')
        d['plan'] = d['plan'].replace('DG-CHAR2, DG-REL-LIFT, DG-RIG |',
                                    'DG-CHAR2, DG-REL-LIFT, DG-RIG, DG-SPECTRUM |')
    elif mutation == 'refuted':
        d['nodes'][cid]['Status'] = d['claims'][cid]['status'] = 'REFUTED'
    elif mutation == 'promote':
        d['nodes'][cid]['Status'] = d['claims'][cid]['status'] = 'PROVED'
        # Still a false promotion when this node is already admitted.
        d['nodes'][cid]['Evidence'] = 'draft'
    elif mutation == 'source-hash':
        d['sources']['SP-GH07']['readable_sha'] = '0' * 64
    elif mutation == 'source-gap':
        d['nodes'][cid]['Sources'] = 'SP-TITS57'
    elif mutation == 'labbook':
        d['tex'] = re.sub(r'faithful\s+normalized\s+trace', 'arbitrary normalized trace',
                          d['tex'], count=1)
    elif mutation == 'definition-drift':
        d['tex'] = d['tex'].replace('The zero space is allowed.', 'The zero space is excluded.', 1)
    elif mutation == 'notation-alias':
        d['notation'] += '\n| `P_(p,n)` | a second Pauli group name | D1704 |\n'
    elif mutation == 'notation-owner':
        d['notation'] = '\n'.join(x for x in d['notation'].splitlines() if '`W^s_(k,n)(a,b)`' not in x)
    elif mutation == 'inherited-status':
        d['claims']['F1-REAL']['status'] = 'SKETCH'
    elif mutation == 'untracked-reuse':
        d['nodes'][cid]['Dependencies'] = ','.join(x for x in csv(d['nodes'][cid]['Dependencies']) if x != 'F1-REAL')
        d['claims'][cid]['deps'] = ','.join(x for x in csv(d['claims'][cid]['deps']) if x != 'F1-REAL')
    elif mutation in ('definition-reuse', 'definition-cycle'):
        target = 'D999999' if mutation == 'definition-reuse' else 'D1703'
        d['defs']['D1701']['body'] = re.sub(r'(\*\*Reuses\.\*\* )[^\n]*',
                                          lambda m: m[1] + target + '.', d['defs']['D1701']['body'])
    return d


def check(d, root):
    nodes, claims, defs = d['nodes'], d['claims'], d['defs']
    require(set(nodes) == {c for c in claims if c.startswith('SP-')},
            'G2', 'canonical SP rows and contracts are not in bijection')
    require(len(d['order']) == len(nodes) and {r[0] for r in d['order']} == set(nodes),
            'G2', 'order table does not cover the contracts exactly once')
    require(all(len(r) == 3 and r[1].isdigit() and r[2].isdigit() for r in d['order']),
            'G2', 'malformed stage/priority table')
    priorities = [int(r[2]) for r in d['order']]
    require(sorted(priorities) == list(range(1, len(nodes) + 1)),
            'G2', 'priorities must be a permutation of 1..number of nodes')
    for cid, stage, _ in d['order']:
        require(stage == nodes[cid]['Stage'], 'G2', 'stage drift ' + cid)
    for cid, node in nodes.items():
        require(claims[cid]['status'] == node['Status'], 'G2', 'status drift ' + cid)
        dids, deps = csv(node['Definitions']), csv(node['Dependencies'])
        require(len(dids) == len(set(dids)) and len(deps) == len(set(deps)),
                'G2', 'duplicate inputs/dependencies ' + cid)
        require(all(did in defs for did in dids), 'G2', 'unresolved definition ' + cid)
        require(all(dep in claims for dep in deps), 'G2', 'unresolved dependency ' + cid)
        require(set(csv(claims[cid]['deps'])) == set(dids + deps),
                'G2', 'canonical dependency drift ' + cid)
        require(all(s in d['sources'] or s in d['gaps'] for s in csv(node['Sources'])),
                'G2', 'unregistered source ' + cid)
        for field in ('Proof', 'Review', 'Checks'):
            for path in csv(node[field]):
                p = root / path
                require(p.resolve().is_relative_to(root.resolve()) and p.is_file(),
                        'G2', 'missing or non-repository ' + field + ': ' + cid)
    plan_decisions = {r[0]: r for r in table(d['plan'], 'gate')}
    require(set(plan_decisions) == set(d['decisions']), 'G2', 'plan/decision gate drift')
    for key, decision in d['decisions'].items():
        require(all(x in claims or x in d['decisions'] for x in decision['deps']),
                'G2', 'unresolved decision prerequisite ' + key)
        require(all(x in d['sources'] or x in d['gaps'] for x in decision['sources']),
                'G2', 'unresolved decision source ' + key)
        recorded = set(re.findall(r'\b[A-Z][A-Z0-9]*(?:-[A-Za-z0-9]+)+\b', plan_decisions[key][1]))
        recorded -= d['sources'].keys() | d['gaps']
        require(recorded == set(decision['deps']), 'G2', 'plan prerequisite drift ' + key)
    print('G2 PASS: contract, definition, dependency and source references resolve')

    visiting, visited = set(), set()
    def visit(cid):
        require(cid not in visiting, 'G3', 'dependency cycle at ' + cid)
        if cid in visited:
            return
        visiting.add(cid)
        deps = csv(nodes[cid]['Dependencies']) if cid in nodes else d['decisions'][cid]['deps']
        for dep in deps:
            if dep in nodes or dep in d['decisions']:
                visit(dep)
        visiting.remove(cid)
        visited.add(cid)
    for cid in nodes.keys() | d['decisions'].keys():
        visit(cid)
    print(f"G3 PASS: {len(nodes)} lemmas and {len(d['decisions'])} decision gates form a DAG")

    # Check inherited provenance before generic promotion requirements:
    # an inherited-status defect must reach G8 even after an SP promotion.
    for cid, node in nodes.items():
        inherited = csv(node['Inherited'])
        require(set(inherited) <= set(csv(node['Dependencies'])), 'G8', 'untracked inherited result ' + cid)
        for old in inherited:
            require(old in claims and claims[old]['status'] == 'PROVED' and not old.startswith('SP-'),
                    'G8', 'inherited result is not an admitted earlier claim: ' + old)
            paths = re.findall(r'theory/[^\s`|;,]+\.md', claims[old]['proof_cell'])
            require(paths and all((root/path).is_file() for path in paths),
                    'G8', 'inherited proof does not resolve: ' + old)

    for cid, node in nodes.items():
        deps = csv(node['Dependencies'])
        require(all(claims[x]['status'] != 'REFUTED' for x in deps),
                'G4', 'refuted dependency of ' + cid)
        if node['Status'] == 'PROVED':
            require(all(claims[x]['status'] == 'PROVED' for x in deps),
                    'G4', 'unproved dependency of promoted node ' + cid)
            require(node['Evidence'] == 'admitted' and
                    all(node[k] != 'none' for k in ('Proof', 'Review', 'Checks')),
                    'G4', 'promotion has no admitted proof/review/checks ' + cid)
            proof = (root / node['Proof']).read_text()
            review = (root / node['Review']).read_text()
            require(all(s in proof for s in ('<1>', 'ASSUME', 'PROVE', 'QED')),
                    'G4', 'missing structured proof markers ' + cid)
            require('Admitted: ' + cid in review, 'G4', 'missing explicit adjudication ' + cid)
    for key, decision in d['decisions'].items():
        require(all(x not in claims or claims[x]['status'] != 'REFUTED'
                    for x in decision['deps']), 'G4', 'refuted prerequisite of ' + key)
    print('G4 PASS: no refuted dependencies or unsupported promotions')

    used = {s for node in nodes.values() for s in csv(node['Sources'])}
    used |= {s for node in d['decisions'].values() for s in node['sources']}
    for source in used:
        require(source in d['sources'], 'G5', 'GAP source used as evidence: ' + source)
    for source, record in d['sources'].items():
        for path_key, hash_key in (('raw', 'raw_sha'), ('readable', 'readable_sha')):
            path = root / record[path_key]
            require(path.resolve().is_relative_to((root / 'refs').resolve()) and path.is_file(),
                    'G5', 'missing local body: ' + source)
            expected = record[hash_key]
            require(re.fullmatch('[0-9a-f]{64}', expected), 'G5', 'bad hash: ' + source)
            require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                    'G5', 'source hash mismatch: ' + source + ' / ' + path_key)
    print(f"G5 PASS: {len(d['sources'])} local sources pinned; {len(d['gaps'])} GAP leads unused")

    def_envs = re.findall(
        r'\\begin\{definition\}\[([^\]]+)\]\s*(.*?)\\end\{definition\}\s*'
        r'\\begin\{scope\}\s*(.*?)\\end\{scope\}\s*\\provenance\{(D\d+)\}',
        d['tex'], re.S)
    active_defs = {key for key in defs if 1701 <= int(key[1:]) <= 1799}
    def_envs = [x for x in def_envs if x[3] in active_defs]
    require(len(def_envs) == len(active_defs) and {x[3] for x in def_envs} == active_defs,
            'G6', 'labbook definition coverage drift')
    for title, body, scope, did in def_envs:
        match = re.fullmatch(r'\s*(.*?)\s*\*\*Scope\.\*\* (.*?)\s*'
                             r'\*\*Sources\.\*\* (.*?)\s*\*\*Obligations\.\*\* (.*?)\s*'
                             r'\*\*Reuses\.\*\* (.*?)\s*\*\*Delta\.\*\* (\S.*?)\s*',
                             defs[did]['body'], re.S)
        require(match is not None, 'G6', 'definition metadata malformed ' + did)
        require(norm(title) == norm(defs[did]['title']) and
                norm(body) == norm(match[1]) and norm(scope) == norm(match[2]),
                'G6', 'exact definition/scope drift ' + did)
        require(did in d['notation'], 'G6', 'definition missing from notation ' + did)
        require(all(s in d['sources'] for s in csv(match[3].rstrip('.'))),
                'G6', 'definition source missing or GAP ' + did)
        require(all(c in nodes or c in d['decisions'] for c in csv(match[4].rstrip('.'))),
                'G6', 'definition obligation is not in DAG ' + did)
    prop_envs = re.findall(
        r'\\begin\{proposition\}\[([^\]]+)\]\s*\\status(\w+)\{\}\s*'
        r'(.*?)\\end\{proposition\}\s*\\begin\{scope\}\s*(.*?)'
        r'\\end\{scope\}\s*\\provenance\{(SP-[A-Z0-9-]+)\}', d['tex'], re.S)
    require(len(prop_envs) == len(nodes) and {x[4] for x in prop_envs} == set(nodes),
            'G6', 'labbook claim coverage drift')
    for title, status, statement, scope, cid in prop_envs:
        require(status.upper() == nodes[cid]['Status'] and
                norm(title) == norm(nodes[cid]['Title']) and
                norm(statement) == norm(claims[cid]['statement']) and
                norm(scope) == norm(nodes[cid]['Scope']),
                'G6', 'claim statement/status/scope drift ' + cid)
    for name in ('symplectic_phantasm', 'symplectic_phantasm_contracts'):
        require('\\input{sections/' + name + '}' in d['main'], 'G6', 'missing LaTeX input ' + name)
    print(f'G6 PASS: {len(active_defs)} exact definitions and {len(nodes)} exact claim restatements')

    # Selected semantic-name contracts, not a general mathematics parser.
    notation = d['notation'].split('## Symplectic Phantasm', 1)[1]
    obsolete = ('A_(k,psi)(V)', 'w_v', 'P_(p,n)', 'psi_p', 'B(bold H)', 'Tr_(bold H)', 'U_F')
    require(not any('`'+x+'`' in notation for x in obsolete), 'G7', 'retired duplicate alias reintroduced')
    owned = {'W^s_(k,n)(a,b)': 'D1703', 'chi_(E/K)': 'D1709',
             'U_(E/K,n)': 'D1709', 'Stab_p^amp': 'D1704'}
    rows = [line for line in notation.splitlines() if line.startswith('|')]
    for symbol, owner in owned.items():
        matches = [line for line in rows if '`'+symbol+'`' in line]
        require(len(matches) == 1 and owner in matches[0], 'G7', 'missing/duplicate notation owner ' + symbol)
    require('\\psi(-b\\cdot x+a\\cdot b/2)f(x-a)' in defs['D1703']['body'],
            'G7', 'reference-aligned symmetrized wavefunction convention drift')
    require('P_A' in defs['D1704']['body'] and 'C_2(A)' in defs['D1704']['body'] and
            '\\mathcal P' not in defs['D1704']['body'], 'G7', 'second Pauli/Clifford definition')
    require('\\chi_K' in defs['D1709']['body'] and '\\psi_K' not in defs['D1709']['body'] and
            '\\chi_{E/K}' in defs['D1709']['body'], 'G7', 'relative character notation conflated')
    print('G7 PASS: selected shared-name ownership and convention guards')

    reuse_edges = {}
    for did in active_defs:
        reused = re.search(r'\*\*Reuses\.\*\* ([^\n]+)', defs[did]['body'])
        parents = csv(reused[1].rstrip('.'))
        require(all(x in defs for x in parents), 'G8', 'unresolved reused definition ' + did)
        reuse_edges[did] = parents
    done, stack = set(), set()
    def definition_visit(did):
        require(did not in stack, 'G8', 'definition reuse cycle at ' + did)
        if did in done or did not in reuse_edges:
            return
        stack.add(did)
        for parent in reuse_edges[did]:
            definition_visit(parent)
        stack.remove(did)
        done.add(did)
    for did in active_defs:
        definition_visit(did)
    print('G8 PASS: inherited proof status/paths and acyclic definition reuse')
    ready = [cid for cid, n in nodes.items() if n['Status'] != 'PROVED' and
             all(claims[x]['status'] == 'PROVED' for x in csv(n['Dependencies']))]
    priorities = {cid: int(priority) for cid, _, priority in d['order']}
    print('Ready for proof work: ' + ', '.join(sorted(ready, key=priorities.get)))
    print('PASS: recorded contracts only; no mathematical claim promoted')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    group = parser.add_mutually_exclusive_group()
    for name, gate in MUTATIONS.items():
        group.add_argument('--red-' + name, dest='mutation', action='store_const',
                           const=name, help='mutate actual input copies; must fail at ' + gate)
    args = parser.parse_args()
    try:
        d = read_inputs(args.root)
        if args.mutation == 'duplicate-node':
            block = d['dag_text'].split('## SP-WEYL\n', 1)[1].split('\n## ', 1)[0]
            d['dag_text'] += '\n## SP-WEYL\n' + block
        elif args.mutation == 'empty-scope':
            d['dag_text'] = re.sub(r'^- Scope: .*$', '- Scope: ', d['dag_text'], count=1, flags=re.M)
        d = parse(d)
        print(f"G1 PASS: {len(d['nodes'])} unique contracts with explicit input/output/scope fields")
        check(mutate(d, args.mutation), args.root)
        if args.mutation:
            print('MUTATION SURVIVED: ' + args.mutation)
        return 0
    except ContractFailure as error:
        print(error.gate + ' FAIL: ' + error.detail)
        if args.mutation:
            expected = MUTATIONS[args.mutation]
            if error.gate != expected:
                print('WRONG GATE: expected ' + expected)
                return 2
        return 1
    except (OSError, ValueError) as error:
        print('INPUT ERROR (not a successful mutation check): ' + str(error))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
