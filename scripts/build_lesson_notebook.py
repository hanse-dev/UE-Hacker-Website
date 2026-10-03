#!/usr/bin/env python3
"""
Baut aus dem Lektions-Format (content/python-woche{N}-{thema}[-en]/lessons.json) und den
Referenzloesungen (content/python-12-wochen-grundkurs[-en]/woche-{N}/{variante}/*_6_loesungen)
JE WOCHE/VARIANTE/SPRACHE ZWEI echte Jupyter-Notebooks (.ipynb):

- "..._aufgaben.ipynb" / "..._tasks.ipynb": Aufgaben-Zellen leer (codeTemplate), zum Selberloesen
- "..._loesungen.ipynb" / "..._solutions.ipynb": gleiche Struktur, echte Aufgaben-Zellen enthalten
  bereits die Referenzloesung

Ergaenzt scripts/build_lesson_bundle.py (baut EIN flaches .py-Skript ohne Jupyter/Kernel) um ein
echtes Notebook-Format fuer Leute, die lieber in Jupyter/VS Code offline arbeiten. Nutzt Glossar/
Loesungen/Lektionstexte aus denselben Quellen, liest sie aber nur (schreibt nichts zurueck).

Wird von scripts/pack_notebooks.py aufgerufen (nur im Speicher, nichts wird hier auf die Platte
geschrieben - siehe build_all_notebook_pairs()); der --check/--out-CLI-Modus unten schreibt fuers
manuelle Testen zusaetzlich auf die Platte.
"""
import ast
import json
import re
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(SCRIPT_DIR))
from build_lesson_bundle import (  # noqa: E402
    CONTENT,
    VARIANTS,
    WEEKS,
    load_lesson_markdown,
    load_solutions,
    numeric_sorted,
    parse_markdown_cell,
    week_theme_title,
)
from notebook_utils import code_cell, markdown_cell, notebook, write_notebook  # noqa: E402

SECTION_HEADER = {
    "lektion": {"de": "📚 Lektionen", "en": "📚 Lessons"},
    "debug": {"de": "🐛 Debug-Quest", "en": "🐛 Debug Quest"},
    "mission": {"de": "⭐ Missionen", "en": "⭐ Missions"},
    "boss": {"de": "🔥 Extra-Herausforderungen", "en": "🔥 Extra Challenges"},
}


def load_glossary_cells(glossar_dir: Path) -> list[dict]:
    """Glossar-Zellen (Markdown + Code) in Original-Reihenfolge, als echte Notebook-Zellen -
    im Unterschied zu build_lesson_bundle.load_glossary() bleibt hier auch die Kurzbeispiel-
    Code-Zelle erhalten (im flachen .py-Bundle geht sie verloren, siehe todo.md)."""
    cells = []
    for path in numeric_sorted(list(glossar_dir.glob("*_markdown.py")) + list(glossar_dir.glob("*_code.py"))):
        if path.name.endswith("_markdown.py"):
            cells.append(markdown_cell(parse_markdown_cell(path)))
        else:
            code = ast.parse(path.read_text(encoding="utf-8"))
            # Code-Zellen liegen als Rohtext vor (kein Stringliteral) - direkt lesen
            cells.append(code_cell(path.read_text(encoding="utf-8")))
    return cells


def build_notebook_pair(week: int, variant: dict, lang: str) -> tuple[str, dict, str, dict]:
    """Gibt (aufgaben_dateiname, aufgaben_notebook, loesungen_dateiname, loesungen_notebook) zurueck.

    Wirft AssertionError bei Aufgaben-/Loesungs-Mismatch (Content-Fehler, wie build_lesson_bundle).
    """
    is_en = lang == "en"
    thema_suffix = "-en" if is_en else ""
    lessons_dir = CONTENT / f"python-woche{week}-{variant['thema']}{thema_suffix}"
    lessons = json.loads((lessons_dir / "lessons.json").read_text(encoding="utf-8"))

    course_root = CONTENT / ("python-12-wochen-grundkurs-en" if is_en else "python-12-wochen-grundkurs")
    variant_dir = variant["dir_en"] if is_en else variant["dir_de"]
    prefix = f"week{week}_{variant_dir}" if is_en else f"woche{week}_{variant_dir}"
    type_dir = course_root / f"woche-{week}" / variant_dir

    glossary_cells = load_glossary_cells(type_dir / f"{prefix}_0_glossar")
    solutions = load_solutions(type_dir / f"{prefix}_6_loesungen")

    real_tasks = [
        (lesson, task) for lesson in lessons for task in lesson["tasks"] if not task.get("example")
    ]
    if len(real_tasks) != len(solutions):
        raise AssertionError(
            f"Woche {week} {variant_dir} ({lang}): {len(real_tasks)} zu loesende Aufgaben, "
            f"aber {len(solutions)} Loesungs-Zellen in {type_dir / f'{prefix}_6_loesungen'}"
        )
    solution_by_task_id = {id(task): code for (lesson, task), code in zip(real_tasks, solutions)}

    variant_label = variant["label_en"] if is_en else variant["label_de"]
    theme_title = week_theme_title(
        parse_markdown_cell(numeric_sorted((type_dir / f"{prefix}_0_glossar").glob("*_markdown.py"))[0]),
        lang,
    )
    header = (
        f"UE Hacker – Python 12-Wochen-Kurs / Week {week}: {theme_title} – {variant_label}"
        if is_en else
        f"UE Hacker – Python 12-Wochen-Kurs / Woche {week}: {theme_title} – {variant_label}"
    )

    def build_one(with_solutions: bool) -> dict:
        cells: list[dict] = []
        if is_en:
            intro = (
                f"# {header}\n\n"
                "This notebook bundles this week's glossary, lessons, debug quest, missions and "
                "extra challenges - runs in Jupyter/VS Code, no website/Pyodide needed. Some "
                "sections intentionally reuse/overwrite variables from earlier sections - every "
                "task stands on its own.\n\n"
                + ("**This is the solutions notebook** - real tasks already contain the reference "
                   "solution, compare after trying it yourself.\n\n"
                   if with_solutions else
                   "**This is the tasks notebook** - real task cells start empty. Compare against "
                   "the separate solutions notebook once you're done.\n\n")
                + "Auto-generated from the guided week tour (`scripts/build_lesson_notebook.py`) - "
                "do not edit by hand."
            )
        else:
            intro = (
                f"# {header}\n\n"
                "Dieses Notebook fasst Glossar, Lektionen, Debug-Quest, Missionen und Extra-"
                "Herausforderungen dieser Woche zusammen - läuft in Jupyter/VS Code, keine Website/"
                "kein Pyodide nötig. Manche Abschnitte überschreiben bewusst Variablen aus "
                "vorherigen Abschnitten - jede Aufgabe steht für sich.\n\n"
                + ("**Das ist das Lösungs-Notebook** - echte Aufgaben-Zellen enthalten schon die "
                   "Referenzlösung, vergleiche erst, nachdem du es selbst versucht hast.\n\n"
                   if with_solutions else
                   "**Das ist das Aufgaben-Notebook** - echte Aufgaben-Zellen starten leer. "
                   "Vergleiche am Ende mit dem separaten Lösungs-Notebook.\n\n")
                + "Automatisch erzeugt aus der geführten Wochen-Tour "
                "(`scripts/build_lesson_notebook.py`) - nicht von Hand bearbeiten."
            )
        cells.append(markdown_cell(intro))
        cells.extend(glossary_cells)

        current_section = None
        for lesson in lessons:
            if lesson["section"] != current_section:
                current_section = lesson["section"]
                cells.append(markdown_cell(f"## {SECTION_HEADER[current_section]['en' if is_en else 'de']}"))

            narrative = load_lesson_markdown(lessons_dir, lesson["id"])
            lesson_md = f"### {lesson['title']}"
            if narrative:
                lesson_md += "\n\n" + narrative
            cells.append(markdown_cell(lesson_md))

            task_num = 0
            for task in lesson["tasks"]:
                task_num += 1
                is_example = bool(task.get("example"))
                if is_example:
                    label = "**Beispiel:**" if not is_en else "**Example:**"
                else:
                    label = f"**Aufgabe {task_num}:**" if not is_en else f"**Task {task_num}:**"
                cells.append(markdown_cell(f"{label} {task['instruction']}"))
                if is_example:
                    code = task["codeTemplate"]
                    guaranteed_valid = True
                elif with_solutions:
                    code = solution_by_task_id[id(task)]
                    guaranteed_valid = True
                else:
                    # Echte Aufgabe im Aufgaben-Notebook: codeTemplate ist bei Debug-Quests
                    # ABSICHTLICH kaputter Code (das ist die Aufgabe) - kein Syntax-Check moeglich.
                    code = task["codeTemplate"]
                    guaranteed_valid = False
                if guaranteed_valid:
                    compile(code, f"<woche{week}-{variant_dir}-{lang}-cell>", "exec")
                cells.append(code_cell(code))

        return notebook(cells)

    tasks_nb = build_one(with_solutions=False)
    solutions_nb = build_one(with_solutions=True)

    if is_en:
        tasks_filename = f"{prefix}_tasks.ipynb"
        solutions_filename = f"{prefix}_solutions.ipynb"
    else:
        tasks_filename = f"{prefix}_aufgaben.ipynb"
        solutions_filename = f"{prefix}_loesungen.ipynb"

    return tasks_filename, tasks_nb, solutions_filename, solutions_nb


def build_all_notebook_pairs():
    """Generator ueber (week, variant_dir, lang, tasks_filename, tasks_nb, solutions_filename,
    solutions_nb) fuer alle Wochen/Varianten - analog build_lesson_bundle.build_all_bundles()."""
    for week in WEEKS:
        for variant in VARIANTS:
            for lang in ("de", "en"):
                variant_dir = variant["dir_en"] if lang == "en" else variant["dir_de"]
                tasks_filename, tasks_nb, solutions_filename, solutions_nb = build_notebook_pair(
                    week, variant, lang
                )
                yield week, variant_dir, lang, tasks_filename, tasks_nb, solutions_filename, solutions_nb


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--week", type=int, help="Nur diese Woche (z.B. 4)")
    parser.add_argument("--thema", help="Nur dieses Thema (abenteuer|pferde|scifi)")
    parser.add_argument("--lang", choices=["de", "en"], help="Nur diese Sprache")
    parser.add_argument(
        "--check", action="store_true",
        help="Nur bauen+validieren (Aufgaben-/Loesungsanzahl, Code-Syntax), nichts auf die Platte schreiben",
    )
    parser.add_argument(
        "--out", default="public/wochen-notebooks", help="Ausgabeverzeichnis (Default: public/wochen-notebooks)"
    )
    args = parser.parse_args()

    weeks = [args.week] if args.week else list(WEEKS)
    variants = [v for v in VARIANTS if not args.thema or v["thema"] == args.thema]
    langs = [args.lang] if args.lang else ["de", "en"]

    out_root = Path(args.out)
    count = 0
    for week in weeks:
        for variant in variants:
            for lang in langs:
                tasks_filename, tasks_nb, solutions_filename, solutions_nb = build_notebook_pair(
                    week, variant, lang
                )
                if not args.check:
                    week_dir = out_root / f"woche-{week}"
                    write_notebook(week_dir / tasks_filename, tasks_nb)
                    write_notebook(week_dir / solutions_filename, solutions_nb)
                    print(f"✓ {week_dir / tasks_filename}")
                    print(f"✓ {week_dir / solutions_filename}")
                count += 2
    if args.check:
        print(f"✓ {count // 2} Wochen-Pakete geprueft (Aufgaben-/Loesungsanzahl passt, Code compiliert)")
    else:
        print(f"✓ {count} Notebooks erzeugt")
    return 0


if __name__ == "__main__":
    exit(main())
