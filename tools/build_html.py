#!/usr/bin/env python3
"""Build the single-file interactive guide (site/index.html) from guide/*.md.

Usage:
  python3 tools/build_html.py          # write site/index.html
  python3 tools/build_html.py --check  # exit 1 if site/index.html is out of date

Only the Python standard library is required.
Chapter order comes from the links in guide/README.md.
"""
from pathlib import Path
import html, json, re, sys

ROOT = Path(__file__).resolve().parent.parent
GUIDE = ROOT / 'guide'
DATA = ROOT / 'data'
OUT = ROOT / 'site' / 'index.html'
EXPECTED_CONCEPTS = 120

BULLET = r'^(\d+\. |- |• )'
CONCEPT = re.compile(r'(C\d{3}) (.*?) 【(.*?)】')
SOURCE = re.compile(r'^\[(S\d+)\] (.+)\n+(https://\S+)', re.M)


def manifest():
    toc = (GUIDE / 'README.md').read_text(encoding='utf-8')
    return [GUIDE / name for name in re.findall(r'\]\(([\w-]+\.md)\)', toc)]


def clean(text):
    """Drop GitHub-only markup: link reference definitions and HTML comments."""
    text = re.sub(r'^\[S\d+\]: .*\n?', '', text, flags=re.M)
    text = re.sub(r'<!-- ARCHITECTURE.*?-->', '[ARCHITECTURE]', text)
    return re.sub(r'<!--.*?-->\n?', '', text, flags=re.S)


def inline(t):
    t = html.escape(t)
    t = re.sub(r'\[S(\d+)–S(\d+)\]', lambda m: ''.join(f'[S{i:02}]' for i in range(int(m[1]), int(m[2]) + 1)), t)
    return re.sub(r'\[(S\d{2})\]', r'<a class="ref" href="#source-\1" aria-label="查看来源 \1">[\1]</a>', t)


def blocks(txt):
    out = []
    lines = txt.strip().splitlines()
    i = 0
    while i < len(lines):
        l = lines[i].strip()
        i += 1
        if not l:
            continue
        if l == '[ARCHITECTURE]':
            out.append('<div class="architecture-slot"></div>')
            continue
        if l.startswith('|'):
            rows = [l]
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append(lines[i].strip())
                i += 1
            rows = [r for r in rows if not re.match(r'^\|[-:| ]+\|$', r)]
            out.append('<div class="table-scroll"><table>')
            for j, r in enumerate(rows):
                tag = 'th' if j == 0 else 'td'
                out.append('<tr>' + ''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in r.strip('|').split('|')) + '</tr>')
            out.append('</table></div>')
            continue
        if re.match(BULLET, l):
            tag = 'ol' if re.match(r'^\d+\.', l) else 'ul'
            items = [l]
            # GitHub-style lists may be separated by blank lines only between groups; consecutive lines form one list
            while i < len(lines) and re.match(BULLET, lines[i].strip()):
                items.append(lines[i].strip())
                i += 1
            out.append(f'<{tag}>' + ''.join('<li>' + inline(re.sub(BULLET, '', x)) + '</li>' for x in items) + f'</{tag}>')
            continue
        if l.startswith('https://'):
            out.append(f'<p><a href="{html.escape(l)}" target="_blank" rel="noopener noreferrer">{html.escape(l)}</a></p>')
            continue
        out.append('<p>' + inline(l) + '</p>')
    return '\n'.join(out)


def build():
    aliases = json.loads((DATA / 'term_aliases.json').read_text(encoding='utf-8'))
    interview = json.loads((DATA / 'interview.json').read_text(encoding='utf-8'))
    chapters, concepts, sources = [], [], []
    for path in manifest():
        part = clean(path.read_text(encoding='utf-8')).strip()
        title = part.splitlines()[0][2:]
        body = '\n'.join(part.splitlines()[1:])
        m = re.match(r'(\d+) ', title)
        cid = f'ch-{int(m[1])}' if m else path.stem
        secs = re.split(r'^## (.+)$', body, flags=re.M)
        sections = []
        for j in range(1, len(secs), 2):
            st, raw = secs[j], secs[j + 1].strip()
            cm = CONCEPT.match(st)
            sections.append({'id': cm[1] if cm else f'{cid}-s{j // 2}', 'title': st, 'html': blocks(raw)})
            if cm:
                first = next(x for x in raw.split('\n') if x.strip())
                definition = first.split('。')[0] + '。'
                concepts.append({'id': cm[1], 'name': cm[2], 'status': cm[3], 'chapter': cid,
                                 'chapterName': re.sub(r'^\d+ ', '', title), 'html': blocks(raw),
                                 'definition': re.sub(r'\[S\d+\]', '', definition),
                                 'search': st + ' ' + raw + ' ' + aliases.get(cm[1], ''),
                                 'refs': re.findall(r'\[(S\d+)\]', raw)})
        chapters.append({'id': cid, 'number': int(m[1]) if m else None, 'title': title,
                         'intro': blocks(secs[0]), 'sections': sections, 'search': part})
        sources += [{'id': s[1], 'title': s[2], 'url': s[3]} for s in SOURCE.finditer(part)]

    ids = [s['id'] for s in sources]
    assert len(concepts) == EXPECTED_CONCEPTS, f'expected {EXPECTED_CONCEPTS} concepts, got {len(concepts)}'
    assert len(ids) == len(set(ids)), 'duplicate source ids'
    cited = set()
    for c in chapters:
        text = c['search']
        cited |= set(re.findall(r'\[(S\d+)\]', text))
        for a, b in re.findall(r'\[S(\d+)–S(\d+)\]', text):
            cited |= {f'S{i:02}' for i in range(int(a), int(b) + 1)}
    missing = sorted(cited - set(ids))
    assert not missing, f'cited but undefined sources: {missing}'

    data = json.dumps({'chapters': chapters, 'concepts': concepts, 'sources': sources, 'interview': interview},
                      ensure_ascii=False).replace('</', '<\\/')
    template = (ROOT / 'tools' / 'template.html').read_text(encoding='utf-8')
    return template.replace('__GUIDE_DATA__', data), (len(concepts), len(chapters), len(sources))


if __name__ == '__main__':
    page, (nc, nch, ns) = build()
    if '--check' in sys.argv:
        ok = OUT.exists() and OUT.read_text(encoding='utf-8') == page
        print('site/index.html is up to date' if ok else 'site/index.html is out of date; run tools/build_html.py')
        sys.exit(0 if ok else 1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding='utf-8')
    print(f'Built {OUT.relative_to(ROOT)}: {nc} concepts, {nch} pages, {ns} sources')
