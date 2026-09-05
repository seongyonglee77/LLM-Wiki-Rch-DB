from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path

from llm_wiki_common import add_root_arg


SITE_NAME = "LLM Wiki / Research Archive"


def page_path(site: Path, source: Path, root: Path) -> Path:
    return site / source.relative_to(root).with_suffix(".html")


def link_for(raw: str, source: Path, root: Path, site: Path) -> str:
    target, _, label = raw.partition("|")
    target = target.strip()
    label = (label or target).strip()
    target_path = (source.parent / target).resolve()
    if target_path.suffix == "":
        target_path = target_path.with_suffix(".md")
    if target_path.exists() and target_path.is_relative_to(root):
        destination = page_path(site, target_path, root) if target_path.is_relative_to(root / "wiki") else target_path
        href = os.path.relpath(destination, page_path(site, source, root).parent).replace(chr(92), "/")
        return f'<a href="{html.escape(href)}">{html.escape(label)}</a>'
    return html.escape(label)


def markdown_to_html(text: str, source: Path, root: Path, site: Path) -> str:
    lines = text.splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    in_list = False

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            value = " ".join(x.strip() for x in paragraph)
            value = re.sub(r"\[\[([^\]]+)\]\]", lambda m: link_for(m.group(1), source, root, site), value)
            value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
            out.append(f"<p>{value}</p>")
            paragraph = []

    for line in lines:
        if line.startswith("---") or re.match(r"^[A-Za-z_]+:\s", line):
            continue
        heading = re.match(r"^(#{1,3})\s+(.+)$", line)
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        if heading:
            flush_paragraph()
            if in_list:
                out.append("</ul>"); in_list = False
            level = len(heading.group(1))
            content = re.sub(r"\[\[([^\]]+)\]\]", lambda m: link_for(m.group(1), source, root, site), heading.group(2))
            out.append(f"<h{level}>{content}</h{level}>")
        elif bullet:
            flush_paragraph()
            if not in_list:
                out.append("<ul>"); in_list = True
            content = re.sub(r"\[\[([^\]]+)\]\]", lambda m: link_for(m.group(1), source, root, site), bullet.group(1))
            out.append(f"<li>{content}</li>")
        elif not line.strip():
            flush_paragraph()
            if in_list:
                out.append("</ul>"); in_list = False
        else:
            paragraph.append(line)
    flush_paragraph()
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def title_of(source: Path) -> str:
    for line in source.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return source.stem.replace("-", " ").title()


def shell(title: str, body: str, source: Path, site: Path, output: Path | None = None) -> str:
    current = output or page_path(site, source, site.parent)
    rel = os.path.relpath(site / "index.html", current.parent).replace(chr(92), "/")
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · {SITE_NAME}</title><link rel="stylesheet" href="{rel.replace('index.html','styles.css')}"></head>
<body><div class="layout"><aside class="rail"><a class="brand" href="{rel}">LLM WIKI</a><p class="rail-note">RESEARCH ARCHIVE · 2026</p>
<nav><a href="{rel}">Home</a><a href="{rel}#catalog">Catalog</a><a href="{rel}#about">About</a></nav></aside>
<main class="content"><div class="eyebrow">ARCHIVE / {html.escape(source.relative_to(site.parent).as_posix())}</div>{body}
<footer>Static research wiki · generated from Markdown · paper records remain in English; wiki layer is localized.</footer></main></div></body></html>'''


def build(root: Path, site: Path) -> int:
    wiki = root / "wiki"
    site.mkdir(parents=True, exist_ok=True)
    pages = sorted(wiki.rglob("*.md"))
    for source in pages:
        destination = page_path(site, source, root)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(shell(title_of(source), markdown_to_html(source.read_text(encoding="utf-8"), source, root, site), source, site, destination), encoding="utf-8")
    rows = []
    for source in pages:
        if source.name == "index.md":
            continue
        destination = page_path(site, source, root)
        href = os.path.relpath(destination, site).replace(chr(92), "/")
        category = source.parent.name
        rows.append(f'<a class="row" data-search="{html.escape((title_of(source)+" "+category).lower())}" href="{href}"><span class="num">{len(rows)+1:03d}</span><span class="row-title">{html.escape(title_of(source))}</span><span class="meta">{html.escape(category.upper())}</span></a>')
    body = f'''<header class="hero"><div><div class="eyebrow">DIGITAL ARCHIVE · STATIC EDITION</div><h1>{SITE_NAME}</h1><p>논문을 읽고, 연결하고, 다시 찾아가기 위한 연구 위키입니다.</p></div><div class="count">{len(rows):02d}<small>WIKI PAGES</small></div></header>
<section class="toolbar"><label for="search">SEARCH / 검색</label><input id="search" type="search" placeholder="개념, 주제, 논문 검색"><span id="result-count">{len(rows)} pages</span></section>
<section id="catalog" class="catalog"><div class="catalog-head"><span>NO.</span><span>TITLE</span><span>SECTION</span></div>{''.join(rows)}</section>
<section id="about" class="about"><h2>읽는 순서</h2><p>개념·overview 페이지에서 주제를 잡고, 논문 페이지에서 상세 카드와 source로 이동하세요. 이 사이트는 <code>wiki/</code>의 구조화된 탐색층을 정적으로 보여줍니다.</p></section>
<script src="app.js"></script>'''
    (site / "index.html").write_text(shell(SITE_NAME, body, root / "wiki" / "index.md", site, site / "index.html"), encoding="utf-8")
    (site / "styles.css").write_text(CSS, encoding="utf-8")
    (site / "app.js").write_text(JS, encoding="utf-8")
    return len(pages)


CSS = r''':root{--paper:#e8e3d5;--surface:#efebdf;--ink:#1f1d18;--muted:#6b665a;--rule:#bdb6a4;--accent:#7a3b2e}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.6}.layout{display:grid;grid-template-columns:240px minmax(0,1fr);min-height:100vh}.rail{border-right:1px solid var(--rule);padding:36px 24px;position:sticky;top:0;height:100vh}.brand{color:var(--ink);font:600 1.15rem 'IBM Plex Mono',Consolas,monospace;letter-spacing:.08em;text-decoration:none}.rail-note,.eyebrow,.meta,.num,label,#result-count,.catalog-head,footer{font:12px 'IBM Plex Mono',Consolas,monospace;letter-spacing:.05em;color:var(--muted)}.rail-note{margin:10px 0 42px}.rail nav{display:grid;gap:12px;border-top:2px solid var(--ink);padding-top:16px}.rail nav a{color:var(--ink);text-decoration:none}.rail nav a:hover{color:var(--accent);text-decoration:underline}.content{max-width:1240px;width:100%;padding:40px clamp(20px,5vw,64px) 60px}.hero{display:flex;justify-content:space-between;gap:30px;border-bottom:2px solid var(--ink);padding:28px 0 34px}.hero h1{font-size:clamp(2rem,4vw,4rem);font-weight:500;line-height:1.1;margin:10px 0}.hero p{font-size:1.1rem;margin:0;max-width:680px}.count{font:500 3.8rem Georgia;color:var(--accent);text-align:right;line-height:1}.count small{display:block;font:11px 'IBM Plex Mono',Consolas,monospace;color:var(--muted);margin-top:8px}.toolbar{display:flex;align-items:center;gap:18px;padding:24px 0;border-bottom:1px solid var(--rule)}input{background:transparent;border:1px solid var(--rule);padding:10px 12px;min-width:min(360px,55vw);font:14px 'IBM Plex Mono',Consolas,monospace;color:var(--ink)}input:focus{outline:2px solid var(--accent);outline-offset:2px}.catalog-head,.row{display:grid;grid-template-columns:70px minmax(0,1fr) 160px;gap:20px;align-items:center}.catalog-head{padding:14px 12px;border-bottom:1px solid var(--ink)}.row{padding:14px 12px;color:var(--ink);text-decoration:none;border-bottom:1px solid var(--rule);transition:background 120ms linear}.row:nth-child(even){background:var(--surface)}.row:hover{background:#dfd9c8}.num{color:var(--accent)}.row-title{font-size:1.07rem}.row-title:hover{text-decoration:underline;text-decoration-color:var(--accent)}.about{border-top:2px solid var(--ink);margin-top:50px;padding-top:22px;max-width:720px}.about h2,h2{font-size:1.8rem;font-weight:500}.content>h1{font-size:clamp(2rem,4vw,3.4rem);font-weight:500;line-height:1.15;border-bottom:2px solid var(--ink);padding-bottom:22px}.content>h2{margin-top:38px;border-top:1px solid var(--rule);padding-top:18px}.content p,.content ul{max-width:760px}.content li{margin:5px 0}.content a{color:var(--accent)}code{font-family:'IBM Plex Mono',Consolas,monospace;font-size:.9em}footer{border-top:2px solid var(--ink);margin-top:70px;padding-top:15px}@media(max-width:760px){.layout{display:block}.rail{position:static;height:auto;border-right:0;border-bottom:1px solid var(--rule);padding:20px}.rail nav{display:flex;border-top:0;padding-top:12px}.content{padding:28px 18px}.hero{display:block}.count{text-align:left;margin-top:25px}.catalog-head,.row{grid-template-columns:44px minmax(0,1fr)}.catalog-head span:last-child,.meta{display:none}.toolbar{flex-wrap:wrap}input{min-width:100%}}'''

JS = r'''const input=document.querySelector('#search');const rows=[...document.querySelectorAll('.row')];const count=document.querySelector('#result-count');if(input){input.addEventListener('input',()=>{const q=input.value.toLowerCase().trim();let n=0;rows.forEach(r=>{const show=!q||r.dataset.search.includes(q);r.hidden=!show;if(show)n++});count.textContent=`${n} pages`})}'''


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("--output", default="wiki-site")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(f"built {build(root, (root / args.output).resolve())} markdown pages")
