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

Zusaetzlich (build_lesson_files()) dieselben Inhalte aufgeteilt in EINE .py-Datei pro Lektion/
Debug-Quest/Mission/Extra-Herausforderung (plus Glossar) - das Offline-Format "Einzeldateien".

Wird von scripts/pack_notebooks.py aufgerufen (nur im Speicher, nichts wird hier auf die Platte
geschrieben - siehe build_all_bundles()/build_all_lesson_files()). Die Bausteine
(file_header, render_lesson, ...) nutzt auch scripts/build_offline_py.py (Projekt-Kurse, KI-Labor).
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


def glossary_lines(glossar_dir: Path) -> list[str]:
    """Glossar in Original-Zellreihenfolge: Markdown als Kommentar, die Kurzbeispiel-Code-Zelle
    (`*_code.py`) als echter, lauffaehiger Code - frueher fehlte sie im .py-Download ganz."""
    lines: list[str] = []
    cells = numeric_sorted(list(glossar_dir.glob("*_markdown.py")) + list(glossar_dir.glob("*_code.py")))
    for path in cells:
        if lines:
            lines.append("")
        if path.name.endswith("_markdown.py"):
            lines += comment_lines(parse_markdown_cell(path))
        else:
            lines.append(path.read_text(encoding="utf-8").rstrip("\n"))
    return lines


def rule_line() -> str:
    return "# " + "=" * 68


def file_header(title: str, intro: list[str]) -> list[str]:
    """Kopfblock jeder erzeugten .py-Datei: Titel zwischen Trennlinien, dann Erklaerzeilen."""
    lines = [rule_line(), f"# {title}", rule_line(), "#"]
    lines += [f"# {line}" if line else "#" for line in intro]
    return lines + ["", ""]


def section_banner(text: str) -> list[str]:
    return [rule_line(), f"# {text}", rule_line()]


def render_lesson(lesson: dict, lesson_dir: Path, code_for_task, is_en: bool, number_bonus: bool = True) -> list[str]:
    """Eine Lektion als .py-Zeilen: Titel, Erzaehltext als Kommentar, dann je Aufgabe die
    Aufgabenstellung als Kommentar und den Code von `code_for_task(task)` als echten Code."""
    lines = [f"# --- {lesson['title']} ---"]
    narrative = load_lesson_markdown(lesson_dir, lesson["id"])
    if narrative:
        lines += comment_lines(narrative)
        lines.append("#")

    task_num = 0
    for task in lesson["tasks"]:
        is_example = bool(task.get("example"))
        is_bonus = bool(task.get("isBonus"))
        if is_bonus and not number_bonus:
            heading = "Bonus"
        else:
            task_num += 1
            heading = f"{'Task' if is_en else 'Aufgabe'} {task_num}"
            if is_example:
                heading += " (example)" if is_en else " (Beispiel)"
        lines.append(f"# --- {heading} ---")
        lines += wrapped_comment(task["instruction"])
        lines.append(code_for_task(task).rstrip("\n"))
        lines.append("")
    return lines


def finish(lines: list[str], label: str) -> str:
    """Zeilen zu Dateiinhalt zusammenfuegen und sofort kompilieren - eine kaputte Datei soll beim
    Bauen auffallen, nicht erst bei Lernenden."""
    content = "\n".join(lines).rstrip("\n") + "\n"
    compile(content, label, "exec")
    return content


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


def _load_week(week: int, variant: dict, lang: str) -> dict:
    """Liest alles, was komplett- und Einzel-Dateien einer Woche/Variante/Sprache brauchen.

    Wirft AssertionError, wenn Aufgaben- und Loesungsanzahl nicht zusammenpassen (Content-Fehler,
    nicht stillschweigend ignorieren).
    """
    is_en = lang == "en"
    thema_suffix = "-en" if is_en else ""
    lessons_dir = CONTENT / f"python-woche{week}-{variant['thema']}{thema_suffix}"
    lessons = json.loads((lessons_dir / "lessons.json").read_text(encoding="utf-8"))

    course_root = CONTENT / ("python-12-wochen-grundkurs-en" if is_en else "python-12-wochen-grundkurs")
    variant_dir = variant["dir_en"] if is_en else variant["dir_de"]
    prefix = f"week{week}_{variant_dir}" if is_en else f"woche{week}_{variant_dir}"
    type_dir = course_root / f"woche-{week}" / variant_dir
    glossar_dir = type_dir / f"{prefix}_0_glossar"

    solutions = load_solutions(type_dir / f"{prefix}_6_loesungen")
    real_tasks = [task for lesson in lessons for task in lesson["tasks"] if not task.get("example")]
    if len(real_tasks) != len(solutions):
        raise AssertionError(
            f"Woche {week} {variant_dir} ({lang}): {len(real_tasks)} zu loesende Aufgaben, "
            f"aber {len(solutions)} Loesungs-Zellen in {type_dir / f'{prefix}_6_loesungen'}"
        )
    solution_by_task_id = {id(task): code for task, code in zip(real_tasks, solutions)}

    variant_label = variant["label_en"] if is_en else variant["label_de"]
    theme_title = week_theme_title(load_glossary(glossar_dir), lang)
    week_word = "Week" if is_en else "Woche"
    return {
        "is_en": is_en,
        "lessons": lessons,
        "lessons_dir": lessons_dir,
        "glossar_dir": glossar_dir,
        "variant_dir": variant_dir,
        "prefix": prefix,
        "title": f"UE Hacker – Python 12-Wochen-Kurs / {week_word} {week}: {theme_title} – {variant_label}",
        "code_for_task": lambda task: task["codeTemplate"] if task.get("example") else solution_by_task_id[id(task)],
    }


def build_bundle(week: int, variant: dict, lang: str) -> tuple[str, str]:
    """Baut den kompletten Datei-Inhalt fuer eine Woche/Variante/Sprache.

    Gibt (dateiname, inhalt) zurueck.
    """
    w = _load_week(week, variant, lang)
    is_en = w["is_en"]
    if is_en:
        intro = [
            "This file bundles this week's glossary, lessons, debug quest, missions and",
            "extra challenges into one script - solutions included. Run with",
            "`python3 <filename>.py` (no Jupyter, no Pyodide needed). Some sections",
            "intentionally reuse/overwrite variables from earlier sections - every task",
            "stands on its own.",
            "",
            "Auto-generated from the guided week tour (scripts/build_lesson_bundle.py) -",
            "do not edit by hand.",
        ]
    else:
        intro = [
            "Diese Datei fasst Glossar, Lektionen, Debug-Quest, Missionen und Extra-",
            "Herausforderungen dieser Woche in einem Skript zusammen - inklusive Loesungen.",
            "Ausfuehren: `python3 <dateiname>.py` (kein Jupyter, kein Pyodide noetig). Manche",
            "Abschnitte ueberschreiben bewusst Variablen aus vorherigen Abschnitten - jede",
            "Aufgabe steht fuer sich.",
            "",
            "Automatisch erzeugt aus der gefuehrten Wochen-Tour",
            "(scripts/build_lesson_bundle.py) - nicht von Hand bearbeiten.",
        ]
    lines = file_header(w["title"], intro)
    lines += section_banner("📖 " + ("Glossary" if is_en else "Glossar"))
    lines += glossary_lines(w["glossar_dir"])
    lines += ["", ""]

    current_section = None
    for lesson in w["lessons"]:
        if lesson["section"] != current_section:
            current_section = lesson["section"]
            lines += section_banner(SECTION_HEADER[current_section]["en" if is_en else "de"])
            lines.append("")
        lines += render_lesson(lesson, w["lessons_dir"], w["code_for_task"], is_en)
        lines.append("")

    content = finish(lines, f"<woche{week}-{w['variant_dir']}-{lang}>")
    filename = f"{w['prefix']}_komplett.py" if not is_en else f"{w['prefix']}_complete.py"
    return filename, content


def build_lesson_files(week: int, variant: dict, lang: str) -> list[tuple[str, str]]:
    """Dieselben Inhalte wie build_bundle(), aber eine Datei pro Lektion (plus Glossar).

    Gibt [(dateiname, inhalt), ...] zurueck, Dateinamen fortlaufend nummeriert
    (`00_glossar.py`, `01_lektion-01.py`, ..., `09_debug-01.py`, ...), damit die Reihenfolge im
    Dateimanager der Kursreihenfolge entspricht.
    """
    w = _load_week(week, variant, lang)
    is_en = w["is_en"]
    run_hint = (
        "Run with `python3 <filename>.py` - no Jupyter, no Pyodide needed. Solutions included."
        if is_en else
        "Ausfuehren: `python3 <dateiname>.py` - kein Jupyter, kein Pyodide noetig. Inklusive Loesungen."
    )
    files = []
    glossary_name = "glossary" if is_en else "glossar"
    lines = file_header(f"{w['title']} – {'Glossary' if is_en else 'Glossar'}", [run_hint])
    lines += glossary_lines(w["glossar_dir"])
    files.append((f"00_{glossary_name}.py", finish(lines, f"<woche{week}-{w['variant_dir']}-{lang}-glossar>")))

    for idx, lesson in enumerate(w["lessons"], start=1):
        section = SECTION_HEADER[lesson["section"]]["en" if is_en else "de"]
        lines = file_header(f"{w['title']} – {section}: {lesson['title']}", [run_hint])
        lines += render_lesson(lesson, w["lessons_dir"], w["code_for_task"], is_en)
        label = f"<woche{week}-{w['variant_dir']}-{lang}-{lesson['id']}>"
        files.append((f"{idx:02d}_{lesson['id']}.py", finish(lines, label)))
    return files


def build_all_bundles():
    """Generator ueber (week, variant_dir, lang, filename, content) fuer alle Wochen/Varianten."""
    for week in WEEKS:
        for variant in VARIANTS:
            for lang in ("de", "en"):
                filename, content = build_bundle(week, variant, lang)
                yield week, (variant["dir_en"] if lang == "en" else variant["dir_de"]), lang, filename, content


def build_all_lesson_files():
    """Generator ueber (week, variant_dir, lang, [(dateiname, inhalt), ...])."""
    for week in WEEKS:
        for variant in VARIANTS:
            for lang in ("de", "en"):
                yield week, (variant["dir_en"] if lang == "en" else variant["dir_de"]), lang, build_lesson_files(week, variant, lang)


def main():
    count = 0
    for week, variant_dir, lang, filename, _ in build_all_bundles():
        count += 1
    file_count = sum(len(files) for *_, files in build_all_lesson_files())
    print(f"✓ {count} Wochen-Pakete geprueft (kompilieren fehlerfrei)", flush=True)
    print(f"✓ {file_count} Einzeldateien geprueft (kompilieren fehlerfrei)", flush=True)
    return 0


if __name__ == "__main__":
    exit(main())
