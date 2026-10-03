#!/usr/bin/env python3
"""
Baut aus dem Lektions-Format des KI-Labors (content/ki-labor-woche{N}/lessons.json) je Woche ZWEI
echte Jupyter-Notebooks (.ipynb):

- "ki-labor-woche{N}_aufgaben.ipynb": echte Aufgaben mit ihrer Vorlage (codeTemplate)
- "ki-labor-woche{N}_loesungen.ipynb": gleiche Struktur, echte Aufgaben mit der Musterloesung

Die Musterloesungen stehen im Feld "referenceSolution" (nicht "solution" - das wuerde in
LessonView.vue einen "Loesung anzeigen"-Button einblenden); scripts/check_kilabor_solutions.py
prueft, dass jede davon laeuft und die erwartete Ausgabe liefert.

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


def build_notebook_pair(week: int) -> tuple[str, dict, str, dict]:
    """Gibt (aufgaben_dateiname, aufgaben_notebook, loesungen_dateiname, loesungen_notebook) zurueck.

    Wirft AssertionError, wenn einer echten Aufgabe die referenceSolution fehlt.
    """
    course_dir = CONTENT / f"ki-labor-woche{week}"
    lessons = json.loads((course_dir / "lessons.json").read_text(encoding="utf-8"))
    missing = [
        (lesson["id"], task["instruction"][:40])
        for lesson in lessons for task in lesson["tasks"]
        if not task.get("example") and not task.get("referenceSolution")
    ]
    if missing:
        raise AssertionError(f"ki-labor-woche{week}: Aufgaben ohne 'referenceSolution': {missing}")

    def build_one(with_solutions: bool) -> dict:
        cells = [markdown_cell(
            f"# KI-Labor – Woche {week}: {WEEK_TITLES[week]}\n\n"
            "Dieses Notebook fasst Lektionen, Debug-Quest, Missionen und Extra-Herausforderungen "
            "dieser Woche zusammen - läuft in Jupyter/VS Code, keine Website/kein Pyodide nötig.\n\n"
            + ("**Das ist das Lösungs-Notebook** - echte Aufgaben-Zellen enthalten schon die "
               "Musterlösung, vergleiche erst, nachdem du es selbst versucht hast.\n\n"
               if with_solutions else
               "**Das ist das Aufgaben-Notebook** - echte Aufgaben-Zellen starten mit der Vorlage. "
               "Vergleiche am Ende mit dem separaten Lösungs-Notebook.\n\n")
            + "Automatisch erzeugt aus der Wochen-Tour (`scripts/build_kilabor_notebook.py`) - nicht "
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
                if is_example or with_solutions:
                    # Nur garantiert gueltigen Code kompilieren - Debug-Vorlagen sind absichtlich kaputt.
                    code = task["codeTemplate"] if is_example else task["referenceSolution"]
                    compile(code, f"<ki-labor-woche{week}-cell>", "exec")
                else:
                    code = task["codeTemplate"]
                cells.append(code_cell(code))

        return notebook(cells)

    return (
        f"ki-labor-woche{week}_aufgaben.ipynb", build_one(with_solutions=False),
        f"ki-labor-woche{week}_loesungen.ipynb", build_one(with_solutions=True),
    )


def build_all_notebook_pairs():
    """Generator ueber (week, tasks_filename, tasks_nb, solutions_filename, solutions_nb)."""
    for week in WEEKS:
        yield (week, *build_notebook_pair(week))


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Nur bauen+validieren, nichts auf die Platte schreiben")
    parser.add_argument("--out", default="public/kilabor-notebooks", help="Ausgabeverzeichnis")
    args = parser.parse_args()

    out_root = Path(args.out)
    count = 0
    for week, tasks_name, tasks_nb, solutions_name, solutions_nb in build_all_notebook_pairs():
        if not args.check:
            write_notebook(out_root / tasks_name, tasks_nb)
            write_notebook(out_root / solutions_name, solutions_nb)
            print(f"✓ {out_root / tasks_name}")
            print(f"✓ {out_root / solutions_name}")
        count += 1
    if args.check:
        print(f"✓ {count} KI-Labor-Wochen geprueft (Musterloesungen vorhanden, Code compiliert)")
    else:
        print(f"✓ {count} Notebooks erzeugt")
    return 0


if __name__ == "__main__":
    exit(main())
