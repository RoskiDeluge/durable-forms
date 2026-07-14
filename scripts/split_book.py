import re, os, pathlib

src = pathlib.Path('full-book.md').read_text()
lines = src.split('\n')

def clean_heading(h):
    # "# **Title**" -> level, "Title"
    m = re.match(r'^(#+)\s+\*\*(.+?)\*\*\s*$', h)
    if m: return len(m.group(1)), m.group(2)
    m = re.match(r'^(#+)\s+(.+?)\s*$', h)
    return len(m.group(1)), m.group(2)

# ---- Parse TOC descriptions (lines 9..143, 0-indexed 8..142) ----
toc_text = '\n'.join(lines[8:143])

# ---- Body starts at "# **On the Name**" (line 145, idx 144) ----
body = lines[144:]

parts = [
    ('I', 'Inheritance'),
    ('II', 'The Argument'),
    ('III', 'The Construction'),
    ('IV', 'Horizon'),
]
chapter_titles = {}  # num -> title
toc_desc = {}        # key -> description
key = None
for i, ln in enumerate(lines[8:145]):
    m = re.match(r'^##\s+\*\*(.+?)\*\*', ln)
    if m:
        h = m.group(1)
        cm = re.match(r'Chapter (\d+): (.+)', h)
        if cm:
            key = f'ch{cm.group(1)}'
            chapter_titles[int(cm.group(1))] = cm.group(2)
        elif h.startswith('Preface'):
            key = 'preface'
        else:
            key = None
    elif ln.startswith('- ') and key:
        toc_desc[key] = toc_desc.get(key, '') + ln[2:].strip() + ' '

# ---- Split body into sections ----
# markers: plain "Part X" lines, plain "Chapter <Word>" lines, H1 headings
sections = []  # (kind, title, lines)
cur = None
i = 0
skip_next_blank_and_bold = 0
n = len(body)
chnum = 0
while i < n:
    ln = body[i]
    if re.match(r'^Part (I|II|III|IV)$', ln.strip()):
        # skip "Part X", blank, "**Name**"
        i += 1
        while i < n and (not body[i].strip() or re.match(r'^\*\*.+\*\*$', body[i].strip())):
            i += 1
        continue
    if re.match(r'^Chapter (One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten)$', ln.strip()):
        i += 1
        continue
    if ln.startswith('# '):
        lvl, title = clean_heading(ln)
        if cur: sections.append(cur)
        if title == 'On the Name':
            cur = ('preface', title, [])
        elif title == 'Works Cited':
            cur = ('cited', title, [])
        else:
            chnum += 1
            cur = (f'ch{chnum}', title, [])
        i += 1
        continue
    if cur:
        # normalize ## **X** -> ## X
        if ln.startswith('#'):
            lvl, t = clean_heading(ln)
            ln = '#'*lvl + ' ' + t
        cur[2].append(ln)
    i += 1
if cur: sections.append(cur)

for k, t, c in sections:
    print(k, '|', t, '|', len('\n'.join(c).split()), 'words')

# verify chapter titles match TOC
for num, t in chapter_titles.items():
    print(num, t)

part_of = {1:0,2:0,3:0, 4:1,5:1,6:1, 7:2,8:2,9:2, 10:3}

def fm(title, order, parent=None, desc=None):
    out = ['---', f'title: "{title}"', f'nav_order: {order}', 'layout: default']
    if parent: out.append(f'parent: "{parent}"')
    if desc: out.append(f'description: "{desc.strip()}"')
    out.append('---')
    return '\n'.join(out) + '\n\n'

os.makedirs('docs', exist_ok=True)
slugify = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

for kind, title, content in sections:
    body_txt = '\n'.join(content).strip() + '\n'
    if kind == 'preface':
        path = 'docs/00-preface.md'
        text = fm('Preface: On the Name', 2, desc=toc_desc.get('preface')) + f'# Preface: On the Name\n\n{body_txt}'
    elif kind == 'cited':
        path = 'docs/99-works-cited.md'
        text = fm('Works Cited', 99) + f'# Works Cited\n\n{body_txt}'
    else:
        num = int(kind[2:])
        pn = part_of[num]
        pname = f'Part {parts[pn][0]} — {parts[pn][1]}'
        path = f'docs/{num:02d}-{slugify(title)}.md'
        text = fm(f'Chapter {num}: {title}', num, parent=pname, desc=toc_desc.get(kind)) + f'# Chapter {num}: {title}\n\n{body_txt}'
    pathlib.Path(path).write_text(text)
    print('wrote', path)

# part index pages
for pi, (rn, name) in enumerate(parts):
    ptitle = f'Part {rn} — {name}'
    chaps = [num for num, p in part_of.items() if p == pi]
    lines_out = ['---', f'title: "{ptitle}"', f'nav_order: {pi+3}', 'layout: default', 'has_children: true', '---', '', f'# {ptitle}', '']
    for num in chaps:
        t = chapter_titles[num]
        lines_out.append(f'## [Chapter {num}: {t}]({num:02d}-{slugify(t)}.html)')
        lines_out.append('')
        if toc_desc.get(f'ch{num}'):
            lines_out.append(toc_desc[f'ch{num}'].strip())
            lines_out.append('')
    pathlib.Path(f'docs/part-{pi+1}.md').write_text('\n'.join(lines_out))
    print('wrote', f'docs/part-{pi+1}.md')
