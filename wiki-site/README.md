# LLM Wiki static site

This folder is a generated, dependency-free HTML presentation of `../wiki/`, the linked summary cards in `../cards/`, and parsed source pages in `../sources/`.

Regenerate from the repository root:

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\build_html_site.py --output wiki-site
```

The canonical records remain in `wiki/`, `cards/`, and `sources/`. Wiki pages link to generated card and parsed-source pages under `wiki-site/cards/` and `wiki-site/sources/`; the generated site can be published with GitHub Pages after the repository is pushed.
