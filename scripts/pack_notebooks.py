#!/usr/bin/env python3
"""
Erstellt die Offline-Downloads (ZIPs unter public/, gitignored) fuer alle Python-Kurse mit
eigenem Lernpfad - je Woche bzw. Projekt-Kurs DREI Formate, jedes als eigenes ZIP (ein Button pro
Format, siehe src/components/OfflineDownloads.vue):

- "-notebooks.zip": echte Jupyter-Notebooks (Aufgaben + Loesungen getrennt; KI-Labor nur Aufgaben)
- "-komplett.zip":  EINE zusammengesetzte .py-Datei (12-Wochen-Kurs: eine je Thema)
- "-einzeln.zip":   eine .py-Datei pro Lektion (12-Wochen-Kurs: ein Ordner je Thema)

Pfade:
- 12-Wochen-Kurs: public/wochen-zips/woche-{N}[-en]-{format}.zip (+ Cheat-Sheets der Woche in
  jedem der drei ZIPs) und das Gesamtpaket public/python-12-wochen-notebooks.zip
- Projekt-Kurse:  public/projekt-zips/{ordner}-{format}.zip (nur die Python-Projekte)
- KI-Labor:       public/ki-labor-zips/woche-{N}-{format}.zip

Quellen: scripts/build_lesson_bundle.py / build_lesson_notebook.py (12 Wochen),
build_offline_py.py / build_project_notebook.py / build_kilabor_notebook.py (Projekte, KI-Labor),
Cheat-Sheets aus scripts/md_to_cheatsheet_notebook.py (bleiben .ipynb).

Schreibt zusaetzlich public/offline-downloads.json (Liste aller erzeugten ZIPs) - daran prueft
scripts/ensure-test-prereqs.mjs, ob alles da und aktuell ist.
"""

import json
import shutil
import sys
import zipfile
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_kilabor_notebook import build_all_notebooks as build_all_kilabor_notebooks  # noqa: E402
from build_lesson_bundle import build_all_bundles, build_all_lesson_files  # noqa: E402
from build_lesson_notebook import build_all_notebook_pairs  # noqa: E402
from build_offline_py import build_all_kilabor_files, build_all_project_files  # noqa: E402
from build_project_notebook import build_all_notebook_pairs as build_all_project_notebook_pairs  # noqa: E402

OUTPUT_DIR = ROOT / "public"
WEEK_ZIPS_DIR = OUTPUT_DIR / "wochen-zips"
PROJECT_ZIPS_DIR = OUTPUT_DIR / "projekt-zips"
KILABOR_ZIPS_DIR = OUTPUT_DIR / "ki-labor-zips"
MANIFEST = OUTPUT_DIR / "offline-downloads.json"

CHEAT_SHEET_ROOTS = {
    "de": ROOT / "content" / "python-12-wochen-grundkurs",
    "en": ROOT / "content" / "python-12-wochen-grundkurs-en",
}


def cheat_sheets_for_week(week: int, lang: str):
    week_dir = CHEAT_SHEET_ROOTS[lang] / f"woche-{week}"
    if not week_dir.is_dir():
        return []
    return sorted(week_dir.glob("*.ipynb"))


def nb_json(nb: dict) -> str:
    return json.dumps(nb, indent=1, ensure_ascii=False)


def fresh_dir(path: Path):
    """Ordner leeren, damit keine ZIPs mit veralteten Namen liegen bleiben."""
    shutil.rmtree(path, ignore_errors=True)
    path.mkdir(parents=True)


def write_zip(path: Path, entries, extra_files=(), written=None):
    """entries: [(name_im_zip, text)], extra_files: [(Pfad, name_im_zip)]."""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        for name, content in entries:
            zf.writestr(name, content)
        for src, name in extra_files:
            zf.write(src, name)
    if written is not None:
        written.append(path.relative_to(OUTPUT_DIR).as_posix())


def pack_weekly_course(written):
    fresh_dir(WEEK_ZIPS_DIR)
    by_key = {}  # (week, lang) -> {"notebooks": [...], "komplett": [...], "einzeln": [...]}

    def slot(week, lang):
        return by_key.setdefault((week, lang), {"notebooks": [], "komplett": [], "einzeln": []})

    for week, variant_dir, lang, tasks_name, tasks_nb, solutions_name, solutions_nb in build_all_notebook_pairs():
        slot(week, lang)["notebooks"] += [(tasks_name, nb_json(tasks_nb)), (solutions_name, nb_json(solutions_nb))]
    for week, variant_dir, lang, filename, content in build_all_bundles():
        slot(week, lang)["komplett"].append((filename, content))
    for week, variant_dir, lang, files in build_all_lesson_files():
        prefix = f"week{week}_{variant_dir}" if lang == "en" else f"woche{week}_{variant_dir}"
        slot(week, lang)["einzeln"] += [(f"{prefix}/{name}", content) for name, content in files]

    for (week, lang), formats in sorted(by_key.items()):
        suffix = "" if lang == "de" else "-en"
        cheat_sheets = [(cs, cs.name) for cs in cheat_sheets_for_week(week, lang)]
        for fmt, entries in formats.items():
            write_zip(WEEK_ZIPS_DIR / f"woche-{week}{suffix}-{fmt}.zip", entries, cheat_sheets, written)

    # Gesamtpaket: alle Wochen, alle Formate, beide Sprachen
    total = OUTPUT_DIR / "python-12-wochen-notebooks.zip"
    with zipfile.ZipFile(total, "w", zipfile.ZIP_DEFLATED) as zf:
        for (week, lang), formats in sorted(by_key.items()):
            lang_dir = "deutsch" if lang == "de" else "english"
            for fmt, entries in formats.items():
                for name, content in entries:
                    zf.writestr(f"woche-{week}/{lang_dir}/{fmt}/{name}", content)
            for cs in cheat_sheets_for_week(week, lang):
                zf.write(cs, f"woche-{week}/{lang_dir}/{cs.name}")
    written.append(total.relative_to(OUTPUT_DIR).as_posix())
    return len(by_key)


def pack_project_courses(written):
    fresh_dir(PROJECT_ZIPS_DIR)
    notebooks = {
        folder: [(tasks_name, nb_json(tasks_nb)), (solutions_name, nb_json(solutions_nb))]
        for folder, tasks_name, tasks_nb, solutions_name, solutions_nb in build_all_project_notebook_pairs()
    }
    count = 0
    for folder, complete, single in build_all_project_files():
        write_zip(PROJECT_ZIPS_DIR / f"{folder}-notebooks.zip", notebooks[folder], written=written)
        write_zip(PROJECT_ZIPS_DIR / f"{folder}-komplett.zip", [complete], written=written)
        write_zip(PROJECT_ZIPS_DIR / f"{folder}-einzeln.zip", single, written=written)
        count += 1
    return count


def pack_kilabor(written):
    fresh_dir(KILABOR_ZIPS_DIR)
    notebooks = {week: (name, nb) for week, name, nb in build_all_kilabor_notebooks()}
    count = 0
    for week, complete, single in build_all_kilabor_files():
        name, nb = notebooks[week]
        write_zip(KILABOR_ZIPS_DIR / f"woche-{week}-notebooks.zip", [(name, nb_json(nb))], written=written)
        write_zip(KILABOR_ZIPS_DIR / f"woche-{week}-komplett.zip", [complete], written=written)
        write_zip(KILABOR_ZIPS_DIR / f"woche-{week}-einzeln.zip", single, written=written)
        count += 1
    return count


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    written: list[str] = []
    weeks = pack_weekly_course(written)
    projects = pack_project_courses(written)
    ki_weeks = pack_kilabor(written)
    MANIFEST.write_text(json.dumps({"files": written}, indent=1) + "\n", encoding="utf-8")
    print(f"✓ 12-Wochen-Kurs: {weeks} Wochen-Sprach-Pakete × 3 Formate + Gesamtpaket", flush=True)
    print(f"✓ Projekt-Kurse: {projects} × 3 Formate", flush=True)
    print(f"✓ KI-Labor: {ki_weeks} Wochen × 3 Formate", flush=True)
    print(f"✓ {len(written)} ZIPs erstellt, Liste in {MANIFEST.relative_to(ROOT)}", flush=True)
    return 0


if __name__ == "__main__":
    exit(main())
