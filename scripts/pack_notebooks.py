#!/usr/bin/env python3
"""
Erstellt ZIP-Pakete für den Python 12-Wochen-Kurs (Offline-Download je Woche + Gesamtpaket).

Jede Woche/Variante/Sprache wird als EINE lauffähige .py-Datei gepackt (Glossar, Lektionen,
Debug-Quest, Missionen, Extra-Herausforderungen inkl. Lösungen), erzeugt von
scripts/build_lesson_bundle.py direkt aus dem Lektions-Format - kein Zellen-Format/Jupyter-Setup
mehr nötig für den Download. Dazu kommen die Cheat-Sheets/das Gesamtglossar (eigene Pipeline,
scripts/md_to_cheatsheet_notebook.py, bleiben .ipynb).
"""

import sys
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_lesson_bundle import build_all_bundles  # noqa: E402

OUTPUT_DIR = ROOT / "public"
WEEK_ZIPS_DIR = OUTPUT_DIR / "wochen-zips"

CHEAT_SHEET_ROOTS = {
    "de": ROOT / "content" / "python-12-wochen-grundkurs",
    "en": ROOT / "content" / "python-12-wochen-grundkurs-en",
}


def cheat_sheets_for_week(week: int, lang: str):
    root = CHEAT_SHEET_ROOTS[lang]
    week_dir = root / f"woche-{week}"
    if not week_dir.is_dir():
        return []
    return sorted(week_dir.glob("*.ipynb"))


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    WEEK_ZIPS_DIR.mkdir(parents=True, exist_ok=True)

    bundles_by_week = {}
    total = 0
    for week, variant_dir, lang, filename, content in build_all_bundles():
        bundles_by_week.setdefault(week, []).append((filename, content))
        total += 1

    zip_path = OUTPUT_DIR / "python-12-wochen-notebooks.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for week, bundles in sorted(bundles_by_week.items()):
            for filename, content in bundles:
                zf.writestr(f"woche-{week}/{filename}", content)
            for lang in ("de", "en"):
                for cs in cheat_sheets_for_week(week, lang):
                    suffix = "" if lang == "de" else "-en"
                    zf.write(cs, f"woche-{week}/{cs.name.replace('.ipynb', '')}{suffix}.ipynb")
    print(f"✓ {total} Wochen-Pakete gepackt: {zip_path}", flush=True)

    week_count = 0
    for week, bundles in sorted(bundles_by_week.items()):
        for lang, suffix in (("de", ""), ("en", "-en")):
            lang_bundles = [(f, c) for f, c in bundles if f.endswith("_komplett.py" if lang == "de" else "_complete.py")]
            cheat_sheets = cheat_sheets_for_week(week, lang)
            if not lang_bundles and not cheat_sheets:
                continue
            week_zip = WEEK_ZIPS_DIR / f"woche-{week}{suffix}.zip"
            with zipfile.ZipFile(week_zip, "w", zipfile.ZIP_DEFLATED) as zf:
                for filename, content in lang_bundles:
                    zf.writestr(filename, content)
                for cs in cheat_sheets:
                    zf.write(cs, cs.name)
            week_count += 1
    print(f"✓ {week_count} Wochen-ZIPs (DE+EN) erstellt: {WEEK_ZIPS_DIR}", flush=True)

    return 0


if __name__ == "__main__":
    exit(main())
