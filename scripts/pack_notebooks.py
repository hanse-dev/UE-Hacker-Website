#!/usr/bin/env python3
"""
Erstellt ZIP-Pakete für den Python 12-Wochen-Kurs (Notebooks).

Seit der Umstellung auf das Zellen-Format gibt es kein .ipynb mehr - gepackt werden die von
scripts/build_cell_notebooks.py erzeugten _bundle/*.py-Dateien (eine Datei pro Notebook,
direkt mit `python3 datei.py` lauffähig, kein Jupyter nötig). Muss deshalb NACH
`npm run build:cells` laufen.
"""

import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
CONTENT_DIR = ROOT / "content" / "python-12-wochen-grundkurs"
OUTPUT_DIR = ROOT / "public"
WEEK_ZIPS_DIR = OUTPUT_DIR / "wochen-zips"


def bundle_arcname(bundle_path: Path, base_dir: Path) -> Path:
    # bundle_path liegt unter .../<typ-ordner>/_bundle/<name>.py - das Archiv soll wie frueher
    # flach nach Wochen-Ordner/Varianten-Ordner/<name>.py aussehen, ohne den _bundle-Zwischenordner.
    cell_dir = bundle_path.parent.parent
    return cell_dir.relative_to(base_dir).with_suffix(".py")


def main():
    if not CONTENT_DIR.is_dir():
        print(f"Fehler: {CONTENT_DIR} nicht gefunden.", flush=True)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    WEEK_ZIPS_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Gesamtpaket (alle Wochen)
    zip_path = OUTPUT_DIR / "python-12-wochen-notebooks.zip"
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for bundle in sorted(CONTENT_DIR.rglob("_bundle/*.py")):
            zf.write(bundle, bundle_arcname(bundle, CONTENT_DIR))
            count += 1
        # Cheat-Sheets/Gesamtglossar sind nicht Teil der Zellen-Migration (eigene Pipeline,
        # scripts/md_to_cheatsheet_notebook.py) - bleiben als .ipynb, aber weiterhin im Zip.
        for ipynb in sorted(CONTENT_DIR.rglob("*.ipynb")):
            zf.write(ipynb, ipynb.relative_to(CONTENT_DIR))
            count += 1
    print(f"✓ {count} Notebooks gepackt: {zip_path}", flush=True)

    # 2. Pro-Woche-ZIPs
    week_count = 0
    for week_dir in sorted(CONTENT_DIR.iterdir()):
        if not week_dir.is_dir() or not week_dir.name.startswith("woche-"):
            continue
        week_num = week_dir.name.replace("woche-", "")
        bundles = sorted(week_dir.rglob("_bundle/*.py"))
        cheat_sheets = sorted(week_dir.rglob("*.ipynb"))
        if not bundles and not cheat_sheets:
            continue
        week_zip = WEEK_ZIPS_DIR / f"woche-{week_num}.zip"
        with zipfile.ZipFile(week_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for bundle in bundles:
                zf.write(bundle, bundle_arcname(bundle, week_dir))
            for ipynb in cheat_sheets:
                zf.write(ipynb, ipynb.relative_to(week_dir))
        print(
            f"  Woche {week_num}: {len(bundles)} Notebooks + {len(cheat_sheets)} Cheat-Sheets → {week_zip.name}",
            flush=True,
        )
        week_count += 1
    print(f"✓ {week_count} Wochen-ZIPs erstellt: {WEEK_ZIPS_DIR}", flush=True)

    return 0


if __name__ == "__main__":
    exit(main())
