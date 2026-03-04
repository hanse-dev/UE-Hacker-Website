#!/usr/bin/env python3
"""Erstellt ein ZIP-Paket mit allen Notebooks des Python 12-Wochen-Kurses."""

import os
import zipfile
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content" / "python-12-wochen-grundkurs"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "public"
ZIP_NAME = "python-12-wochen-notebooks.zip"


def main():
    if not CONTENT_DIR.is_dir():
        print(f"Fehler: {CONTENT_DIR} nicht gefunden.", flush=True)
        return 1

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    zip_path = OUTPUT_DIR / ZIP_NAME

    count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for ipynb in sorted(CONTENT_DIR.rglob("*.ipynb")):
            arcname = ipynb.relative_to(CONTENT_DIR)
            zf.write(ipynb, arcname)
            count += 1

    print(f"✓ {count} Notebooks gepackt: {zip_path}", flush=True)
    return 0


if __name__ == "__main__":
    exit(main())
