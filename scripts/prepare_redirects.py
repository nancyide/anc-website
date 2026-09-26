"""Build exact Cloudflare download redirects from the verified release manifest.

This only writes configuration files. It makes no DNS or Cloudflare changes.
"""
import csv
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'migration' / 'redirects'
HOSTS = ('anc.org', 'www.anc.org')
# These directory symlinks were confirmed on the original server.
DIRECTORY_ALIASES = {'/OANC/': '/oanc/', '/MASC/': '/masc/'}

def build():
    manifest = json.loads((ROOT / 'migration/download-manifest.json').read_text())
    paths = {}
    for item in manifest:
        original, target = item['url_path'], item['release_url']
        url = urlsplit(target)
        if not (url.scheme == 'https' and url.netloc == 'github.com'
                and url.path.startswith('/nancyide/anc-website/releases/download/datasets-2026-09-25/')
                and not url.query and not url.fragment):
            raise ValueError('Unexpected release destination: ' + target)
        if not original.startswith('/') or any(c in original for c in ('?', '#', '\n', '\r')):
            raise ValueError('Unexpected source path: ' + original)
        variants = [original]
        for prefix, alias in DIRECTORY_ALIASES.items():
            if original.startswith(prefix): variants.append(alias + original[len(prefix):])
        for path in variants:
            if path in paths and paths[path] != target:
                raise ValueError('Conflicting redirect: ' + path)
            paths[path] = target
    rows = [(host + path, target) for path, target in sorted(paths.items()) for host in HOSTS]
    OUT.mkdir(parents=True, exist_ok=True)
    for status, filename in ((302, 'cloudflare-test-302.csv'), (301, 'cloudflare-permanent-301.csv')):
        with (OUT / filename).open('w', newline='') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            # Cloudflare CSV imports must not contain a column-name header.
            # No source scheme means both HTTP and HTTPS. Exact hosts/paths only.
            for source, target in rows:
                writer.writerow((source, target, status, 'FALSE', 'FALSE', 'FALSE', 'FALSE'))
    report = {'status': 'prepared_not_deployed', 'archives': len(manifest),
              'distinct_paths_including_aliases': len(paths), 'host_path_rules': len(rows),
              'http_and_https_urls_covered': len(rows) * 2, 'hosts': list(HOSTS),
              'directory_aliases': DIRECTORY_ALIASES,
              'preserve_query_string': False, 'include_subdomains': False,
              'subpath_matching': False, 'preserve_path_suffix': False}
    (OUT / 'coverage.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    build()
