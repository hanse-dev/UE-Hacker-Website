#!/usr/bin/env python3
"""
Baut aus dem Lektions-Format des KI-Labors (content/ki-labor-woche{N}/lessons.json) je Woche EIN
Aufgaben-Jupyter-Notebook (.ipynb) - NUR Aufgaben, KEIN Loesungs-Notebook.

Anders als der 12-Wochen-Kurs (externe *_6_loesungen-Zellenordner) und die Python-Projekt-Kurse
(inline task["solution"]) hat das KI-Labor bisher GAR KEINE gespeicherten Referenzloesungen im
Content - nur codeTemplate (bei Beispiel-Aufgaben bereits lauffaehiger Code, bei echten Aufgaben
Vorlage/leer). Die einzigen bekannten funktionierenden Loesungen stecken unvollstaendig als
Test-Fixtures in tests/ki-labor.spec.js (90 von 160 echten Aufgaben, nur genug fuer den
Wochen-Check) - als Content-Quelle ungeeignet (Tests sind keine Aufgaben-Loesungen, siehe
WORKFLOW.md). Ein echtes Loesungs-Notebook braeuchte zuerst echte Referenzloesungen im Content
(eigene Aufgabe, siehe todo.md), deshalb hier bewusst nur Aufgaben.

Wochentitel sind 1:1 aus src/data/kiLaborWeeks.js dupliziert (dort wiederum aus KURSPLAN.md) -
es gibt keine gemeinsame JS/Python-Quelle. Bei einer Titeländerung dort auch hier nachziehen.

Wird von scripts/pack_notebooks.py aufgerufen.
"""
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_lesson_bundle import load_lesson_markdown  # noqa: E402
from notebook_utils import code_cell, markdown_cell, notebook, write_notebook  # noqa: E402

CONTENT = ROOT / "content"
WEEKS = range(1, 9)

# 1:1 aus src/data/kiLaborWeeks.js (siehe Modul-Docstring) - keine gemeinsame Quelle mit JS.
WEEK_TITLES = {
    1: "Was ist KI?",
    2: "Daten sind alles",
    3: "Nächste Nachbarn (k-NN)",
    4: "Training & Test",
    5: "Entscheidungsbäume",
    6: "Neuronale Netze I",
    7: "Neuronale Netze II",
    8: "Grenzen & Ethik",
}

SECTION_HEADER = {
    "lektion": "📚 Lektionen",
    "debug": "🐛 Debug-Quest",
    "mission": "⭐ Missionen",
    "boss": "🔥 Extra-Herausforderungen",
}


def build_notebook(week: int) -> tuple[str, dict]:
    course_dir = CONTENT / f"ki-labor-woche{week}"
    lessons = json.loads((course_dir / "lessons.json").read_text(encoding="utf-8"))

    cells = [markdown_cell(
        f"# KI-Labor – Woche {week}: {WEEK_TITLES[week]}\n\n"
        "Dieses Notebook fasst Lektionen, Debug-Quest, Missionen und Extra-Herausforderungen "
        "dieser Woche zusammen - läuft in Jupyter/VS Code, keine Website/kein Pyodide nötig. "
        "**Reines Aufgaben-Notebook ohne Lösungen** - das KI-Labor hat (anders als der "
        "12-Wochen-Kurs) noch keine gespeicherten Referenzlösungen im Content, prüfe deine "
        "Lösung stattdessen über den Wochen-Check auf der Kursseite.\n\n"
        "Automatisch erzeugt aus der Wochen-Tour (`scripts/build_kilabor_notebook.py`) - nicht "
        "von Hand bearbeiten."
    )]

    current_section = None
    for lesson in lessons:
        if lesson["section"] != current_section:
            current_section = lesson["section"]
            cells.append(markdown_cell(f"## {SECTION_HEADER[current_section]}"))

        narrative = load_lesson_markdown(course_dir, lesson["id"])
        lesson_md = f"### {lesson['title']}"
        if narrative:
            lesson_md += "\n\n" + narrative
        cells.append(markdown_cell(lesson_md))

        task_num = 0
        for task in lesson["tasks"]:
            is_example = bool(task.get("example"))
            if is_example:
                label = "**Beispiel:**"
            else:
                task_num += 1
                label = f"**Aufgabe {task_num}:**"
            cells.append(markdown_cell(f"{label} {task['instruction']}"))
            code = task["codeTemplate"]
            if is_example:
                compile(code, f"<ki-labor-woche{week}-cell>", "exec")
            cells.append(code_cell(code))

    return f"ki-labor-woche{week}_aufgaben.ipynb", notebook(cells)


def build_all_notebooks():
    """Generator ueber (week, filename, nb)."""
    for week in WEEKS:
        filename, nb = build_notebook(week)
        yield week, filename, nb


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Nur bauen+validieren, nichts auf die Platte schreiben")
    parser.add_argument("--out", default="public/kilabor-notebooks", help="Ausgabeverzeichnis")
    args = parser.parse_args()

    out_root = Path(args.out)
    count = 0
    for week, filename, nb in build_all_notebooks():
        if not args.check:
            write_notebook(out_root / filename, nb)
            print(f"✓ {out_root / filename}")
        count += 1
    if args.check:
        print(f"✓ {count} KI-Labor-Wochen geprueft (Beispiel-Code compiliert)")
    else:
        print(f"✓ {count} Notebooks erzeugt")
    return 0


if __name__ == "__main__":
    exit(main())
