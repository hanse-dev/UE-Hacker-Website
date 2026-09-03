#!/usr/bin/env python3
"""Extrahiert Markdown-Zellen aus .ipynb-Dateien in .md-Dateien, damit cspell
sie prüfen kann, ohne durch Code/JSON-Rauschen gestört zu werden.

Usage:
    python3 scripts/extract_notebook_text.py <glob-pattern> <output-dir>

Beispiel:
    python3 scripts/extract_notebook_text.py \
        "content/python-12-wochen-grundkurs/woche-*/abenteuer/*.ipynb" \
        /tmp/notebook-text/abenteuer-de
"""
import json
import sys
from pathlib import Path


def extract_markdown(notebook_path: Path) -> str:
    with open(notebook_path, encoding="utf-8") as f:
        nb = json.load(f)
    parts = []
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "markdown":
            continue
        source = cell.get("source", "")
        text = "".join(source) if isinstance(source, list) else source
        parts.append(text)
    return "\n\n".join(parts)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    pattern, out_dir = sys.argv[1], Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    repo_root = Path(__file__).resolve().parent.parent
    paths = sorted(repo_root.glob(pattern))
    if not paths:
        print(f"Keine Dateien gefunden für Pattern: {pattern}")
        sys.exit(1)

    for nb_path in paths:
        text = extract_markdown(nb_path)
        if not text.strip():
            continue
        out_name = str(nb_path.relative_to(repo_root)).replace("/", "__").replace(".ipynb", ".md")
        (out_dir / out_name).write_text(text, encoding="utf-8")

    print(f"{len(paths)} Notebooks verarbeitet → {out_dir}")


if __name__ == "__main__":
    main()
