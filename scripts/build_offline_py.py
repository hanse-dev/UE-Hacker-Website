#!/usr/bin/env python3
"""
Baut die beiden .py-Offline-Formate fuer die Python-Projekt-Kurse und das KI-Labor - analog zu
scripts/build_lesson_bundle.py (12-Wochen-Kurs), dessen Bausteine hier wiederverwendet werden:

- "komplett": EINE .py-Datei pro Projekt-Kurs bzw. KI-Labor-Woche
- "einzeln":  eine .py-Datei pro Lektion

Projekt-Kurse: echte Aufgaben enthalten die Loesung (inline task["solution"]), wie der
12-Wochen-Download. KI-Labor: hat (noch) keine gespeicherten Referenzloesungen im Content (siehe
scripts/build_kilabor_notebook.py) - echte Aufgaben enthalten deshalb die Vorlage (codeTemplate)
zum Selberloesen, Beispiele den fertigen Code.

Die Notebooks dazu bauen scripts/build_project_notebook.py / scripts/build_kilabor_notebook.py.
Wird von scripts/pack_notebooks.py aufgerufen (nur im Speicher). `--check` baut alles und
kompiliert jede Datei, ohne etwas zu schreiben.
"""
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from build_kilabor_notebook import SECTION_HEADER as KI_SECTION_HEADER, WEEK_TITLES, WEEKS as KI_WEEKS  # noqa: E402
from build_lesson_bundle import CONTENT, file_header, finish, render_lesson, section_banner  # noqa: E402
from build_project_notebook import PROJECT_COURSES  # noqa: E402

RUN_HINT = "Ausfuehren: `python3 <dateiname>.py` - kein Jupyter, kein Pyodide noetig."


def _lessons(folder: str) -> list[dict]:
    return json.loads((CONTENT / folder / "lessons.json").read_text(encoding="utf-8"))


def _build(title: str, folder: str, lessons: list[dict], code_for_task, intro: list[str],
           section_header: dict | None, number_bonus: bool, file_prefix: str):
    """Gemeinsamer Ablauf: (komplett_dateiname, inhalt), [(einzel_dateiname, inhalt), ...]."""
    lesson_dir = CONTENT / folder

    lines = file_header(title, intro)
    current_section = None
    for lesson in lessons:
        if section_header and lesson.get("section") != current_section:
            current_section = lesson.get("section")
            lines += section_banner(section_header[current_section])
            lines.append("")
        lines += render_lesson(lesson, lesson_dir, code_for_task, is_en=False, number_bonus=number_bonus)
        lines.append("")
    complete = (f"{file_prefix}_komplett.py", finish(lines, f"<{file_prefix}>"))

    single = []
    for idx, lesson in enumerate(lessons, start=1):
        heading = lesson["title"]
        if section_header:
            heading = f"{section_header[lesson['section']]}: {heading}"
        lines = file_header(f"{title} – {heading}", [intro[-1]])
        lines += render_lesson(lesson, lesson_dir, code_for_task, is_en=False, number_bonus=number_bonus)
        single.append((f"{idx:02d}_{lesson['id']}.py", finish(lines, f"<{file_prefix}-{lesson['id']}>")))
    return complete, single


def build_project_files(course: dict):
    """Projekt-Kurs -> (komplett, [einzeln...]); echte Aufgaben mit Loesung."""
    lessons = _lessons(course["folder"])
    missing = [
        (lesson["id"], task["instruction"][:40])
        for lesson in lessons for task in lesson["tasks"]
        if not task.get("example") and "solution" not in task
    ]
    if missing:
        raise AssertionError(f"{course['folder']}: Aufgaben ohne 'solution'-Feld: {missing}")

    intro = [
        "Alle Lektionen dieses Projekts in Python-Code, inklusive Loesungen. Versuch es zuerst",
        "selbst auf der Kursseite oder im Aufgaben-Notebook und vergleiche dann hier.",
        "",
        "Automatisch erzeugt aus der Kursseite (scripts/build_offline_py.py) - nicht von Hand",
        "bearbeiten.",
        RUN_HINT + " Inklusive Loesungen.",
    ]
    return _build(
        course["title"], course["folder"], lessons,
        lambda task: task["codeTemplate"] if task.get("example") else task["solution"],
        intro, section_header=None, number_bonus=False, file_prefix=course["folder"],
    )


def build_kilabor_files(week: int):
    """KI-Labor-Woche -> (komplett, [einzeln...]); echte Aufgaben mit Vorlage, ohne Loesung."""
    folder = f"ki-labor-woche{week}"
    intro = [
        "Lektionen, Debug-Quest, Missionen und Extra-Herausforderungen dieser Woche in",
        "Python-Code. OHNE Musterloesungen: echte Aufgaben enthalten die Vorlage zum",
        "Selberloesen, Beispiele den fertigen Code. Pruefe deine Loesung ueber den",
        "Wochen-Check auf der Kursseite.",
        "",
        "Automatisch erzeugt aus der Wochen-Tour (scripts/build_offline_py.py) - nicht von Hand",
        "bearbeiten.",
        RUN_HINT + " Ohne Musterloesungen.",
    ]
    return _build(
        f"UE Hacker – KI-Labor / Woche {week}: {WEEK_TITLES[week]}", folder, _lessons(folder),
        lambda task: task["codeTemplate"], intro,
        section_header=KI_SECTION_HEADER, number_bonus=True, file_prefix=folder,
    )


def build_all_project_files():
    """Generator ueber (folder, komplett, [einzeln...])."""
    for course in PROJECT_COURSES:
        complete, single = build_project_files(course)
        yield course["folder"], complete, single


def build_all_kilabor_files():
    """Generator ueber (week, komplett, [einzeln...])."""
    for week in KI_WEEKS:
        complete, single = build_kilabor_files(week)
        yield week, complete, single


def main():
    projects = list(build_all_project_files())
    weeks = list(build_all_kilabor_files())
    singles = sum(len(s) for *_, s in projects) + sum(len(s) for *_, s in weeks)
    print(f"✓ {len(projects)} Projekt-Kurse + {len(weeks)} KI-Labor-Wochen geprueft "
          f"({singles} Einzeldateien, alles kompiliert)", flush=True)
    return 0


if __name__ == "__main__":
    if "--check" not in sys.argv:
        print("Hinweis: schreibt nichts - die Dateien packt scripts/pack_notebooks.py.", flush=True)
    exit(main())
