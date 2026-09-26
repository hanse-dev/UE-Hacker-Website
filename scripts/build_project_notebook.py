#!/usr/bin/env python3
"""
Baut aus dem Lektions-Format der Python-Projekt-Kurse (content/{kurs}/lessons.json, Loesungen
INLINE als task["solution"] - anders als der 12-Wochen-Kurs gibt es hier keine externen
Referenzloesungs-Ordner) je Kurs ZWEI echte Jupyter-Notebooks (.ipynb):

- "{kurs}_aufgaben.ipynb": Aufgaben-Zellen leer/mit Vorlage (codeTemplate), zum Selberloesen
- "{kurs}_loesungen.ipynb": gleiche Struktur, echte Aufgaben-Zellen enthalten die Loesung

Nur DE (die Projekt-Kurse haben noch keine EN-Version, siehe todo.md). Analog zu
scripts/build_lesson_notebook.py (12-Wochen-Kurs), wird von scripts/pack_notebooks.py aufgerufen.
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

# folder = Ordnername in content/ = contentPath-Prop von ProjectCourse.vue (auch als Dateiname-
# Praefix fuer den Download genutzt, damit das Frontend ohne Mapping-Tabelle auskommt), title wie
# in public/kurse.json (dort mit "projekt-"-Id-Praefix - siehe todo.md fuer den EN-Fehlbestand)
PROJECT_COURSES = [
    {"folder": "caesar-chiffre", "title": "Projekt: Cäsar-Chiffre"},
    {"folder": "vigenere-chiffre", "title": "Projekt: Vigenère-Chiffre"},
    {"folder": "morsecode", "title": "Projekt: Morsecode-Übersetzer"},
    {"folder": "zahlendetektiv", "title": "Projekt: Zahlen-Detektiv"},
    {"folder": "text-adventure-fluchtraum", "title": "Projekt: Text-Adventure – Der Fluchtraum"},
]


def build_notebook_pair(course: dict) -> tuple[str, dict, str, dict]:
    """Gibt (aufgaben_dateiname, aufgaben_notebook, loesungen_dateiname, loesungen_notebook) zurueck.

    Wirft AssertionError, wenn eine echte (nicht-Beispiel-)Aufgabe kein "solution"-Feld hat -
    Content-Fehler, nicht stillschweigend mit leerer Loesungs-Zelle weiterlaufen.
    """
    course_dir = CONTENT / course["folder"]
    lessons = json.loads((course_dir / "lessons.json").read_text(encoding="utf-8"))
    beschreibung = (course_dir / "beschreibung.md").read_text(encoding="utf-8").strip()

    missing = [
        (lesson["id"], task["instruction"][:40])
        for lesson in lessons
        for task in lesson["tasks"]
        if not task.get("example") and "solution" not in task
    ]
    if missing:
        raise AssertionError(f"{course['folder']}: Aufgaben ohne 'solution'-Feld: {missing}")

    def build_one(with_solutions: bool) -> dict:
        cells = [markdown_cell(
            f"# {course['title']}\n\n{beschreibung}\n\n"
            + ("**Das ist das Lösungs-Notebook** - echte Aufgaben-Zellen enthalten schon die "
               "Referenzlösung, vergleiche erst, nachdem du es selbst versucht hast.\n\n"
               if with_solutions else
               "**Das ist das Aufgaben-Notebook** - echte Aufgaben-Zellen starten leer/mit Vorlage. "
               "Vergleiche am Ende mit dem separaten Lösungs-Notebook.\n\n")
            + "Automatisch erzeugt aus der Kursseite (`scripts/build_project_notebook.py`) - "
              "nicht von Hand bearbeiten."
        )]

        for lesson in lessons:
            narrative = load_lesson_markdown(course_dir, lesson["id"])
            lesson_md = f"## {lesson['title']}"
            if narrative:
                lesson_md += "\n\n" + narrative
            cells.append(markdown_cell(lesson_md))

            task_num = 0
            for task in lesson["tasks"]:
                is_bonus = bool(task.get("isBonus"))
                if not is_bonus:
                    task_num += 1
                label = "**Bonus:**" if is_bonus else f"**Aufgabe {task_num}:**"
                cells.append(markdown_cell(f"{label} {task['instruction']}"))
                if with_solutions:
                    code = task["solution"]
                    compile(code, f"<{course['folder']}-cell>", "exec")
                else:
                    code = task["codeTemplate"]
                cells.append(code_cell(code))

        return notebook(cells)

    tasks_nb = build_one(with_solutions=False)
    solutions_nb = build_one(with_solutions=True)
    return (
        f"{course['folder']}_aufgaben.ipynb", tasks_nb,
        f"{course['folder']}_loesungen.ipynb", solutions_nb,
    )


def build_all_notebook_pairs():
    """Generator ueber (folder, tasks_filename, tasks_nb, solutions_filename, solutions_nb)."""
    for course in PROJECT_COURSES:
        tasks_filename, tasks_nb, solutions_filename, solutions_nb = build_notebook_pair(course)
        yield course["folder"], tasks_filename, tasks_nb, solutions_filename, solutions_nb


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Nur bauen+validieren, nichts auf die Platte schreiben")
    parser.add_argument("--out", default="public/projekt-notebooks", help="Ausgabeverzeichnis")
    args = parser.parse_args()

    out_root = Path(args.out)
    count = 0
    for folder, tasks_filename, tasks_nb, solutions_filename, solutions_nb in build_all_notebook_pairs():
        if not args.check:
            write_notebook(out_root / tasks_filename, tasks_nb)
            write_notebook(out_root / solutions_filename, solutions_nb)
            print(f"✓ {out_root / tasks_filename}")
            print(f"✓ {out_root / solutions_filename}")
        count += 2
    if args.check:
        print(f"✓ {count // 2} Projekt-Kurse geprueft (Loesungen vorhanden, Code compiliert)")
    else:
        print(f"✓ {count} Notebooks erzeugt")
    return 0


if __name__ == "__main__":
    exit(main())
