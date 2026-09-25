"""Check local links and list remaining dependencies on the original ANC host."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src', 'action', 'poster') and value:
                self.references.append((tag, key, value))

missing, old_host, external_assets = [], [], []
exact_files = {p.relative_to(SITE).as_posix() for p in SITE.rglob('*') if p.is_file()}
html_files = list(SITE.rglob('*.html'))
for path in html_files:
    rel = path.relative_to(SITE).as_posix()
    parser = References(); parser.feed(path.read_text(errors='replace'))
    for tag, key, value in parser.references:
        url = urlsplit(urljoin('https://preview.invalid/' + rel, value))
        item = {'page': rel, 'tag': tag, 'attribute': key, 'url': value}
        if url.hostname in ('anc.org', 'www.anc.org'):
            old_host.append(item)
        elif url.hostname == 'preview.invalid':
            target = unquote(url.path).lstrip('/')
            if target.endswith('/') or not target: target += 'index.html'
            if target not in exact_files and target + '/index.html' not in exact_files:
                missing.append(item)
        elif key in ('src', 'poster') and url.scheme in ('http', 'https'):
            external_assets.append(item)
for path in SITE.rglob('*.css'):
    for value in re.findall(r'url\([\s\"\']*([^\)\"\']+)', path.read_text(errors='replace')):
        if value.startswith(('data:', 'http:', 'https:', '//')): continue
        target = path.parent / unquote(urlsplit(value).path)
        if not target.is_file():
            missing.append({'page': str(path.relative_to(SITE)), 'tag': 'css', 'attribute': 'url', 'url': value})
report = {'html_pages': len(html_files), 'static_bytes': sum(p.stat().st_size for p in SITE.rglob('*') if p.is_file()),
          'missing_local_targets': missing, 'original_host_references': old_host,
          'external_asset_references': external_assets}
(ROOT / 'migration' / 'link-check.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps({'html_pages':len(html_files), 'missing_local_targets':len(missing),
                  'unique_original_host_urls':len({x['url'] for x in old_host}),
                  'external_asset_references':len(external_assets)}, indent=2))
raise SystemExit(1 if missing else 0)
