"""Validate redirect coverage; --live checks the actual HTTP redirects after activation."""
import argparse
import concurrent.futures
import csv
import json
import subprocess
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--live', action='store_true', help='Check live redirects on anc.org; run only after activation')
args = parser.parse_args()
manifest = json.loads((ROOT / 'migration/download-manifest.json').read_text())
path_map = {x['url_path']: x['release_url'] for x in manifest}
expected = {}
for path, target in path_map.items():
    variants = [path]
    if path.startswith('/OANC/'): variants.append('/oanc/' + path[len('/OANC/'):])
    if path.startswith('/MASC/'): variants.append('/masc/' + path[len('/MASC/'):])
    for variant in variants:
        for host in ('anc.org', 'www.anc.org'): expected[host + variant] = target
for code, name in ((302, 'cloudflare-test-302.csv'), (301, 'cloudflare-permanent-301.csv')):
    with (ROOT / 'migration/redirects' / name).open(newline='') as f:
        rows = list(csv.reader(f))
    assert len(rows) == len(expected), 'Coverage count mismatch'
    seen = set()
    for row in rows:
        assert len(row) == 7, 'Invalid column count'
        source, target, status, *flags = row
        assert source not in seen, 'Duplicate source'
        seen.add(source)
        assert expected.get(source) == target, 'Missing, unexpected, or incorrect target'
        assert status == str(code) and flags == ['FALSE'] * 4, 'Incorrect matching options'
        assert urlsplit('https://' + source).netloc in ('anc.org', 'www.anc.org')
    assert seen == set(expected), 'Missing sources'
print('Validated both imports:', len(expected), 'exact host/path rules,', len(manifest), 'archive destinations.')

if args.live:
    # Deliberately do not follow redirects or fetch archive bodies.
    checks = [(scheme + '://' + source, target) for source, target in sorted(expected.items())
              for scheme in ('http', 'https')]
    # Check that legacy query strings do not alter the release destination.
    checks += [(scheme + '://' + source + '?download=1', target)
               for source, target in list(sorted(expected.items()))[:2] for scheme in ('http', 'https')]
    def check(item):
        url, target = item
        result = subprocess.run(['curl', '-q', '-sS', '--head', '--max-time', '20',
                                 '--output', '/dev/null', '--write-out', '%{http_code}\n%{redirect_url}', url],
                                capture_output=True, text=True)
        parts = result.stdout.split('\n', 1)
        status, location = (parts + [''])[:2]
        ok = result.returncode == 0 and status in ('301', '302') and location == target
        return {'url': url, 'status': status, 'location': location, 'expected': target,
                'ok': ok, 'error': result.stderr.strip()}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(check, checks))
    (ROOT / 'migration/redirects/live-check.json').write_text(json.dumps(results, indent=2) + '\n')
    failed = [x for x in results if not x['ok']]
    print('Live requests:', len(results), 'failures:', len(failed))
    raise SystemExit(1 if failed else 0)
