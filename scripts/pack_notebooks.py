#!/usr/bin/env python3
"""Erstellt ZIP-Pakete für den Python 12-Wochen-Kurs (Notebooks + Fortschritt-Skript)."""

import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
CONTENT_DIR = ROOT / "content" / "python-12-wochen-grundkurs"
OUTPUT_DIR = ROOT / "public"
WEEK_ZIPS_DIR = OUTPUT_DIR / "wochen-zips"


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
        for ipynb in sorted(CONTENT_DIR.rglob("*.ipynb")):
            arcname = ipynb.relative_to(CONTENT_DIR)
            zf.write(ipynb, arcname)
            count += 1
        zf.write(SCRIPT_DIR / "fortschritt.py", "fortschritt.py")
        zf.write(SCRIPT_DIR / "rewards-manifest.json", "rewards-manifest.json")
    print(f"✓ {count} Notebooks + Fortschritt-Skript gepackt: {zip_path}", flush=True)

    # 2. Pro-Woche-ZIPs
    week_count = 0
    for week_dir in sorted(CONTENT_DIR.iterdir()):
        if not week_dir.is_dir() or not week_dir.name.startswith("woche-"):
            continue
        week_num = week_dir.name.replace("woche-", "")
        notebooks = sorted(week_dir.rglob("*.ipynb"))
        if not notebooks:
            continue
        week_zip = WEEK_ZIPS_DIR / f"woche-{week_num}.zip"
        with zipfile.ZipFile(week_zip, "w", zipfile.ZIP_DEFLATED) as zf:
            for ipynb in notebooks:
                arcname = ipynb.relative_to(week_dir)
                zf.write(ipynb, arcname)
        print(f"  Woche {week_num}: {len(notebooks)} Notebooks → {week_zip.name}", flush=True)
        week_count += 1
    print(f"✓ {week_count} Wochen-ZIPs erstellt: {WEEK_ZIPS_DIR}", flush=True)

    # 3. Fortschritt-Skript-ZIP
    fortschritt_zip = OUTPUT_DIR / "fortschritt-script.zip"
    with zipfile.ZipFile(fortschritt_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(SCRIPT_DIR / "fortschritt.py", "fortschritt.py")
        zf.write(SCRIPT_DIR / "rewards-manifest.json", "rewards-manifest.json")
    print(f"✓ Fortschritt-Skript gepackt: {fortschritt_zip}", flush=True)

    return 0


if __name__ == "__main__":
    exit(main())
