# LLM Wiki static site

This folder is generated from the canonical `wiki/` Markdown layer.

Run from the repository root:

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\build_html_site.py --output wiki-site
```

The public template starts empty by design. Ingested cards and wiki pages are generated locally and can be published only after review.
