#!/usr/bin/env python3
"""
Baut aus dem Lektions-Format (content/python-woche{N}-{thema}[-en]/lessons.json) und den
Referenzloesungen (content/python-12-wochen-grundkurs[-en]/woche-{N}/{variante}/*_6_loesungen)
JE WOCHE/VARIANTE/SPRACHE EINE einzelne, direkt lauffaehige .py-Datei (Glossar, Lektionen,
Debug-Quest, Missionen, Extra-Herausforderungen inkl. Loesungen als Kommentare/Code).

Ersetzt seit dem Umbau auf das Lektions-Format (Wochen 1-12 sind kein Notebook-Schritt mehr in
der Tour, siehe HANDOFF.md 3.47-3.54) die alten 1_lektion/2_debug/3_missionen/5_boss-Zellenordner
als Quelle fuer den Offline-ZIP-Download - die gibt es nicht mehr (entfernt). 0_glossar und
6_loesungen bleiben als eigene interaktive Notebooks in der App bestehen und werden hier nur
GELESEN, nicht veraendert.

Wird von scripts/pack_notebooks.py aufgerufen (nur im Speicher, nichts wird hier auf die Platte
geschrieben - siehe build_all_bundles()).
"""
import ast
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

WEEKS = range(1, 13)

# thema = Ordnername in content/python-woche{N}-{thema}[-en]/ (immer deutsch, auch fuer -en)
# dir   = Ordnername in content/python-12-wochen-grundkurs[-en]/woche-{N}/{dir}/
VARIANTS = [
    {"thema": "abenteuer", "dir_de": "abenteuer", "dir_en": "adventure", "label_de": "Abenteuer", "label_en": "Adventure"},
    {"thema": "pferde",    "dir_de": "pferde",    "dir_en": "horses",    "label_de": "Pferde",    "label_en": "Horses"},
    {"thema": "scifi",     "dir_de": "scifi",     "dir_en": "scifi",     "label_de": "Sci-Fi",    "label_en": "Sci-Fi"},
]

SECTION_HEADER = {
    "lektion": {"de": "📚 Lektionen", "en": "📚 Lessons"},
    "debug":   {"de": "🐛 Debug-Quest", "en": "🐛 Debug Quest"},
    "mission": {"de": "⭐ Missionen", "en": "⭐ Missions"},
    "boss":    {"de": "🔥 Extra-Herausforderungen", "en": "🔥 Extra Challenges"},
}

WRAP_WIDTH = 92


def parse_markdown_cell(path: Path) -> str:
    """Liest eine NN_markdown.py-Zellendatei (Python-Stringliteral) und gibt den rohen
    Markdown-Text zurueck - exakt wie scripts/build_cell_notebooks.py es tut."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return tree.body[0].value.value


def comment_lines(text: str) -> list[str]:
    """Zerlegt einen (Markdown-)Text in Kommentarzeilen ('# ...'), leere Zeilen bleiben '#'."""
    out = []
    for line in text.split("\n"):
        line = line.rstrip()
        out.append(f"# {line}" if line else "#")
    return out


def wrapped_comment(text: str) -> list[str]:
    wrapped = textwrap.wrap(text, width=WRAP_WIDTH) or [""]
    return [f"# {line}" for line in wrapped]


def numeric_sorted(paths):
    def key(p: Path):
        m = re.match(r"(\d+)_", p.name)
        return int(m.group(1)) if m else 0
    return sorted(paths, key=key)


def load_solutions(loesungen_dir: Path) -> list[str]:
    """Referenzloesungen in Zellen-Reihenfolge (eine pro echter, d.h. nicht-example-Aufgabe)."""
    code_files = numeric_sorted(loesungen_dir.glob("*_code.py"))
    return [f.read_text(encoding="utf-8").rstrip("\n") for f in code_files]


def load_glossary(glossar_dir: Path) -> str:
    """Alle Markdown-Zellen des Glossars zusammengefuegt (Begriffstabelle + Wiederholung)."""
    md_files = numeric_sorted(glossar_dir.glob("*_markdown.py"))
    parts = [parse_markdown_cell(f) for f in md_files]
    return "\n\n".join(parts)


def load_lesson_markdown(lesson_dir: Path, lesson_id: str) -> str:
    """Erzaehltext einer Lektion/Mission/Boss-Etappe (ohne die fuehrende '# Titel'-Zeile)."""
    path = lesson_dir / f"{lesson_id}.md"
    if not path.is_file():
        return ""
    lines = path.read_text(encoding="utf-8").split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    return "\n".join(lines).strip("\n")


def week_theme_title(glossary_text: str, lang: str) -> str:
    first_line = glossary_text.split("\n", 1)[0]
    marker = "Woche " if lang == "de" else "Week "
    idx = first_line.find(marker)
    if idx == -1:
        return ""
    rest = first_line[idx + len(marker):]
    # "4 – Schleifen (for, while): ..." -> Zahl abschneiden
    m = re.match(r"\d+\s*[–-]\s*(.+)", rest)
    return m.group(1).strip() if m else ""


def build_bundle(week: int, variant: dict, lang: str) -> tuple[str, str]:
    """Baut den kompletten Datei-Inhalt fuer eine Woche/Variante/Sprache.

    Gibt (dateiname, inhalt) zurueck. Wirft AssertionError, wenn Aufgaben- und
    Loesungsanzahl nicht zusammenpassen (Content-Fehler, nicht stillschweigend ignorieren).
    """
    is_en = lang == "en"
    thema_suffix = "-en" if is_en else ""
    lessons_dir = CONTENT / f"python-woche{week}-{variant['thema']}{thema_suffix}"
    lessons = json.loads((lessons_dir / "lessons.json").read_text(encoding="utf-8"))

    course_root = CONTENT / ("python-12-wochen-grundkurs-en" if is_en else "python-12-wochen-grundkurs")
    variant_dir = variant["dir_en"] if is_en else variant["dir_de"]
    prefix = f"week{week}_{variant_dir}" if is_en else f"woche{week}_{variant_dir}"
    type_dir = course_root / f"woche-{week}" / variant_dir

    glossary_text = load_glossary(type_dir / f"{prefix}_0_glossar")
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
    theme_title = week_theme_title(glossary_text, lang)
    lines: list[str] = []

    def rule():
        lines.append("# " + "=" * 68)

    header = (
        f"UE Hacker – Python 12-Wochen-Kurs / Week {week}: {theme_title} – {variant_label}"
        if is_en else
        f"UE Hacker – Python 12-Wochen-Kurs / Woche {week}: {theme_title} – {variant_label}"
    )
    rule()
    lines.append(f"# {header}")
    rule()
    lines.append("#")
    if is_en:
        lines += [
            "# This file bundles this week's glossary, lessons, debug quest, missions and",
            "# extra challenges into one script - solutions included. Run with",
            "# `python3 <filename>.py` (no Jupyter, no Pyodide needed). Some sections",
            "# intentionally reuse/overwrite variables from earlier sections - every task",
            "# stands on its own.",
            "#",
            "# Auto-generated from the guided week tour (scripts/build_lesson_bundle.py) -",
            "# do not edit by hand.",
        ]
    else:
        lines += [
            "# Diese Datei fasst Glossar, Lektionen, Debug-Quest, Missionen und Extra-",
            "# Herausforderungen dieser Woche in einem Skript zusammen - inklusive Loesungen.",
            "# Ausfuehren: `python3 <dateiname>.py` (kein Jupyter, kein Pyodide noetig). Manche",
            "# Abschnitte ueberschreiben bewusst Variablen aus vorherigen Abschnitten - jede",
            "# Aufgabe steht fuer sich.",
            "#",
            "# Automatisch erzeugt aus der gefuehrten Wochen-Tour",
            "# (scripts/build_lesson_bundle.py) - nicht von Hand bearbeiten.",
        ]
    lines.append("")
    lines.append("")

    rule()
    lines.append("# 📖 " + ("Glossary" if is_en else "Glossar"))
    rule()
    lines += comment_lines(glossary_text)
    lines.append("")
    lines.append("")

    current_section = None
    for lesson in lessons:
        if lesson["section"] != current_section:
            current_section = lesson["section"]
            rule()
            lines.append(f"# {SECTION_HEADER[current_section]['en' if is_en else 'de']}")
            rule()
            lines.append("")

        lines.append(f"# --- {lesson['title']} ---")
        narrative = load_lesson_markdown(lessons_dir, lesson["id"])
        if narrative:
            lines += comment_lines(narrative)
            lines.append("#")

        task_num = 0
        for task in lesson["tasks"]:
            task_num += 1
            is_example = bool(task.get("example"))
            suffix = " (Beispiel)" if is_example and not is_en else " (example)" if is_example else ""
            label = "Aufgabe" if not is_en else "Task"
            lines.append(f"# --- {label} {task_num}{suffix} ---")
            lines += wrapped_comment(task["instruction"])
            code = task["codeTemplate"] if is_example else solution_by_task_id[id(task)]
            lines.append(code.rstrip("\n"))
            lines.append("")
        lines.append("")

    content = "\n".join(lines).rstrip("\n") + "\n"
    compile(content, f"<woche{week}-{variant_dir}-{lang}>", "exec")  # sofort auffallen, wenn kaputt
    filename = f"{prefix}_komplett.py" if not is_en else f"{prefix}_complete.py"
    return filename, content


def build_all_bundles():
    """Generator ueber (week, variant_dir, lang, filename, content) fuer alle Wochen/Varianten."""
    for week in WEEKS:
        for variant in VARIANTS:
            for lang in ("de", "en"):
                filename, content = build_bundle(week, variant, lang)
                yield week, (variant["dir_en"] if lang == "en" else variant["dir_de"]), lang, filename, content


def main():
    count = 0
    for week, variant_dir, lang, filename, _ in build_all_bundles():
        count += 1
    print(f"✓ {count} Wochen-Pakete geprueft (kompilieren fehlerfrei)", flush=True)
    return 0


if __name__ == "__main__":
    exit(main())
