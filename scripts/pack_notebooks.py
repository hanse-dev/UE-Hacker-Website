#!/usr/bin/env python3
"""Erstellt ZIP-Pakete für den Python 12-Wochen-Kurs (Notebooks + Fortschritt-Skript)."""

import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
CONTENT_DIR = ROOT / "content" / "python-12-wochen-grundkurs"
OUTPUT_DIR = ROOT / "public"


def main():
    if not CONTENT_DIR.is_dir():
        print(f"Fehler: {CONTENT_DIR} nicht gefunden.", flush=True)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Notebook-Pack (mit Fortschritt-Skript und Manifest)
    zip_path = OUTPUT_DIR / "python-12-wochen-notebooks.zip"
    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for ipynb in sorted(CONTENT_DIR.rglob("*.ipynb")):
            arcname = ipynb.relative_to(CONTENT_DIR)
            zf.write(ipynb, arcname)
            count += 1
        # Fortschritt-Skript für lokale Nutzer
        zf.write(SCRIPT_DIR / "fortschritt.py", "fortschritt.py")
        zf.write(SCRIPT_DIR / "rewards-manifest.json", "rewards-manifest.json")
    print(f"✓ {count} Notebooks + Fortschritt-Skript gepackt: {zip_path}", flush=True)

    # 2. Kleines ZIP nur mit Fortschritt-Skript (für Nutzer, die schon Notebooks haben)
    fortschritt_zip = OUTPUT_DIR / "fortschritt-script.zip"
    with zipfile.ZipFile(fortschritt_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(SCRIPT_DIR / "fortschritt.py", "fortschritt.py")
        zf.write(SCRIPT_DIR / "rewards-manifest.json", "rewards-manifest.json")
    print(f"✓ Fortschritt-Skript gepackt: {fortschritt_zip}", flush=True)

    return 0


if __name__ == "__main__":
    exit(main())
