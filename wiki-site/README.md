# LLM Wiki static site

This folder is a generated, dependency-free HTML presentation of `../wiki/`, the linked summary cards in `../cards/`, and parsed source pages in `../sources/`. It is a convenience/readability layer; the Markdown files remain canonical.

Regenerate from the repository root:

```powershell
py -3 scripts\build_html_site.py --output wiki-site
```

From WSL/Linux/macOS, run `python3 scripts/build_html_site.py --output wiki-site` from the repository root. The normal `ingest_batch.py` workflow rebuilds the site after each finalized paper. To refresh after a manual wiki/card/source edit, run the command above. Open `wiki-site/index.html` locally to browse; publishing through GitHub Pages is optional and requires reviewing all included content first.

The canonical records remain in `wiki/`, `cards/`, and `sources/`. Wiki pages link to generated card and parsed-source pages under `wiki-site/cards/` and `wiki-site/sources/`; the generated site can be published with GitHub Pages after the repository is pushed. Do not publish private source text or unpublished work without review.
