"""
Baut aus den Zellen-Ordnern des 12-Wochen-Kurses (content/python-12-wochen-grundkurs(-en)/**)
zwei Artefakte je Ordner - NICHT committed (siehe .gitignore), laeuft bei jedem `npm run dev`/
`npm run build` neu:

- _generated/<name>.ipynb.json  - notebook-foermige JSON fuer JupyterNotebook.vue (Browser)
- _bundle/<name>.py             - alle Zellen einer Lektion zu einer Datei zusammengefuegt,
  laeuft direkt mit `python3 <name>.py` (Offline-Download, ersetzt die alten .ipynb-Downloads)
"""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COURSE_ROOTS = [
    ROOT / "content" / "python-12-wochen-grundkurs",
    ROOT / "content" / "python-12-wochen-grundkurs-en",
]


def is_cell_dir(d: Path) -> bool:
    if d.name in ("_generated", "_bundle"):
        return False
    return any(d.glob("[0-9][0-9]_markdown.py")) or any(d.glob("[0-9][0-9]_code.py"))


def build_json(cell_dir: Path, name: str):
    files = sorted(cell_dir.glob("*.py"))
    cells = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        if f.name.endswith("_markdown.py"):
            tree = ast.parse(text)
            value = tree.body[0].value.value
            cells.append({"cell_type": "markdown", "source": value})
        else:
            cells.append({"cell_type": "code", "source": text})

    out_dir = cell_dir / "_generated"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"{name}.ipynb.json"
    out_file.write_text(json.dumps({"cells": cells}, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(cells)


def build_bundle(cell_dir: Path, name: str):
    files = sorted(cell_dir.glob("*.py"))
    parts = [f.read_text(encoding="utf-8").rstrip("\n") for f in files]
    bundle = "\n\n".join(parts) + "\n"

    out_dir = cell_dir / "_bundle"
    out_dir.mkdir(exist_ok=True)
    out_file = out_dir / f"{name}.py"
    out_file.write_text(bundle, encoding="utf-8")
    return out_file


def main():
    count = 0
    for course_root in COURSE_ROOTS:
        if not course_root.is_dir():
            continue
        for cell_dir in sorted(course_root.rglob("*")):
            if not cell_dir.is_dir() or not is_cell_dir(cell_dir):
                continue
            name = cell_dir.name
            build_json(cell_dir, name)
            build_bundle(cell_dir, name)
            count += 1

    print(f"✓ {count} Zellen-Ordner verarbeitet (JSON + Bundle erzeugt).", flush=True)


if __name__ == "__main__":
    main()
