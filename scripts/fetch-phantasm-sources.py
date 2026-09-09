#!/usr/bin/env python3
"""Retrieve the quest's primary sources. Never execute downloaded material.

Source bodies stay ignored under refs/symplectic-phantasm/. The committed
ledger records verified titles, locators, routes and hashes. This script
retrieves candidates; successful HTTP retrieval does not verify a citation.
Existing successful downloads are retained unless --refresh is requested.
"""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import time
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ARXIV = {
    'SP-GH07': '0705.4556', 'SP-GH09': '0708.0669',
    'SP-W09': '0911.4133', 'SP-LW14': '1401.7302',
    'SP-GROSS06': 'quant-ph/0602001', 'SP-CK21': '2105.06244',
    'SP-BC24': '2401.07914', 'SP-CGK17': '1608.06596',
    'SP-SOULE04': 'math/0304444', 'SP-DEITMAR05': 'math/0404185',
    'SP-CC09': '0903.2024', 'SP-CC10': '0911.3537',
    'SP-PRASAD09': '0912.0574', 'SP-GH08': '0808.1664',
    'SP-BCL22': '2204.08162', 'SP-DER06': 'math-ph/0511030',
    'SP-CCM07': 'math/0512138', 'SP-CM04': 'math/0404128',
    'SP-SPECTOR98': 'hep-th/9710002',
}
EXTERNAL = {
    'SP-JOY81': ['https://mahalex.net/teaching/seminars/semag/joyal.pdf'],
    'SP-KS95': ['http://www.neverendingbooks.org/DATA/KapranovSmirnov.pdf'],
    'SP-BC95': ['https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf'],
    'SP-CM08': ['https://www.math.fsu.edu/~marcolli/coll-55.pdf'],
    'SP-WAT18': ['https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf'],
    'SP-STFIELD': ['https://raw.githubusercontent.com/stacks/stacks-project/master/fields.tex'],
}


def retrieve(key, urls, refresh):
    dest = ROOT / 'refs' / 'symplectic-phantasm' / key
    dest.mkdir(parents=True, exist_ok=True)
    record = dest / 'retrieval.json'
    if record.exists() and not refresh:
        old = json.loads(record.read_text())
        if old.get('status') == 'FETCHED':
            print(key, 'cached', old['format'], flush=True)
            return True
    attempts = []
    for url in urls:
        try:
            req = Request(url, headers={'User-Agent': 'AQM-source-registration/1.0'})
            with urlopen(req, timeout=30) as response:
                body = response.read()
                final_url = response.url
            raw = dest / 'raw'
            raw.write_bytes(body)
            sha = hashlib.sha256(body).hexdigest()
            payload = gzip.decompress(body) if body.startswith(b'\x1f\x8b') else body
            files = []
            if payload.startswith(b'%PDF'):
                (dest / 'paper.pdf').write_bytes(payload)
                subprocess.run(['pdftotext', '-layout', str(dest / 'paper.pdf'),
                                str(dest / 'paper.txt')], check=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                fmt, files = 'PDF', ['paper.pdf', 'paper.txt']
            elif tarfile.is_tarfile(io.BytesIO(payload)):
                with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
                    # Only regular files, rooted here; reject links and traversal.
                    for member in archive.getmembers():
                        if not member.isfile():
                            continue
                        target = dest / member.name
                        if not target.resolve().is_relative_to(dest.resolve()):
                            raise ValueError('Unsafe archive path')
                        target.parent.mkdir(parents=True, exist_ok=True)
                        target.write_bytes(archive.extractfile(member).read())
                        files.append(member.name)
                if not any(f.endswith('.tex') for f in files):
                    raise ValueError('Archive has no TeX source')
                fmt = 'TeX archive'
            elif any(token in payload for token in
                     (b'\\documentclass', b'\\documentstyle', b'\\chapter',
                      b'\\input harvmac', b'\\input{preamble}')):
                (dest / 'source.tex').write_bytes(payload)
                fmt, files = 'TeX', ['source.tex']
            else:
                raise ValueError('Response is neither TeX nor PDF')
            attempts.append({'url': url, 'result': 'FETCHED'})
            record.write_text(json.dumps({
                'id': key, 'status': 'FETCHED', 'url': url, 'final_url': final_url,
                'retrieved': datetime.now(timezone.utc).isoformat(),
                'sha256': sha, 'bytes': len(body), 'format': fmt,
                'files': files, 'attempts': attempts,
            }, indent=2) + '\n')
            print(key, fmt, len(body), sha, flush=True)
            return True
        except Exception as exc:
            attempts.append({'url': url, 'result': str(exc)})
    record.write_text(json.dumps({'id': key, 'status': 'GAP', 'attempts': attempts}, indent=2) + '\n')
    print(key, 'GAP', attempts, flush=True)
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--only', nargs='+', help='Source identifiers to retrieve')
    args = parser.parse_args()
    candidates = {key: [f'https://arxiv.org/e-print/{aid}',
                        f'https://arxiv.org/pdf/{aid}'] for key, aid in ARXIV.items()}
    candidates.update(EXTERNAL)
    selected = args.only or list(candidates)
    unknown = set(selected) - candidates.keys()
    if unknown:
        parser.error('Unknown identifiers: ' + ', '.join(sorted(unknown)))
    good = True
    for key in selected:
        good = retrieve(key, candidates[key], args.refresh) and good
        time.sleep(3)
    return 0 if good else 1


if __name__ == '__main__':
    raise SystemExit(main())
