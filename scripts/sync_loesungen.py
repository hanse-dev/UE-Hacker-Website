#!/usr/bin/env python3
"""Bringt die Loesungs-Notebooks (`*_6_loesungen`) in die Reihenfolge der Aufgaben.

Der Offline-Download (`build_lesson_bundle.py`) ordnet die Loesungs-Code-Zellen den
nicht-Beispiel-Aufgaben der `lessons.json` rein ueber die Reihenfolge zu. Wird eine Aufgabe
mitten in einer Woche ergaenzt, muss ihre Loesung deshalb an derselben Stelle stehen.

Arbeitsweise: neue Loesung als Markdown+Code-Zell-Paar mit beliebiger (z.B. der hoechsten)
Nummer anlegen - die Markdown-Zelle muss den Aufgabentext (`instruction`) enthalten. Dieses
Skript sortiert danach alle Paare in Aufgaben-Reihenfolge und nummeriert die Dateien neu. Die
Texte der Zellen bleiben unveraendert; nur die Abschnitts-Ueberschrift ("## ...") wandert zur
jeweils ersten Aufgabe ihres Abschnitts.

    python3 scripts/sync_loesungen.py            # alle Wochen/Themen/Sprachen
    python3 scripts/sync_loesungen.py --check    # nur pruefen, nichts schreiben (Exit 1 bei Abweichung)
"""
import json
import re
import sys
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / "content"
THEMES = {"abenteuer": "adventure", "pferde": "horses", "scifi": "scifi"}
CELL_RE = re.compile(r"^(\d+)_(markdown|code)\.py$")


def unescape(text: str) -> str:
    return text.replace('\\"', '"').replace("\\\\", "\\")


def sync(week: int, theme: str, lang: str, check: bool) -> bool:
    """Gibt True zurueck, wenn das Notebook schon passte."""
    is_en = lang == "en"
    lessons = json.loads((CONTENT / f"python-woche{week}-{theme}{'-en' if is_en else ''}" / "lessons.json").read_text(encoding="utf-8"))
    if is_en:
        nb = CONTENT / "python-12-wochen-grundkurs-en" / f"woche-{week}" / THEMES[theme] / f"week{week}_{THEMES[theme]}_6_loesungen"
    else:
        nb = CONTENT / "python-12-wochen-grundkurs" / f"woche-{week}" / theme / f"woche{week}_{theme}_6_loesungen"

    files = sorted((f for f in nb.iterdir() if CELL_RE.match(f.name)), key=lambda f: int(CELL_RE.match(f.name).group(1)))
    old = {f.name: f.read_text(encoding="utf-8") for f in files}

    # Kopf (alles vor der ersten Aufgaben-Zelle), danach Paare aus Markdown + Code
    header, pairs, section_heads = [], [], []
    pending = None
    for f in files:
        if f.name.endswith("_markdown.py"):
            raw = old[f.name].strip()[3:-3]  # Rohtext ohne die umschliessenden """ - wird unveraendert uebernommen
            if "### " not in raw:
                header.append(old[f.name])
                continue
            head, _, _ = raw.partition("### ")
            if head.strip():
                section_heads.append(head.strip())
            pending = raw
        else:
            pairs.append((pending, old[f.name]))
            pending = None

    sections = []
    for lesson in lessons:
        if lesson["section"] not in sections:
            sections.append(lesson["section"])
    if len(section_heads) != len(sections):
        raise SystemExit(f"{nb}: {len(section_heads)} Abschnitts-Ueberschriften, aber {len(sections)} Abschnitte in lessons.json")
    head_for = dict(zip(sections, section_heads))

    new, used, seen_sections = list(header), set(), set()
    for lesson in lessons:
        for task in lesson["tasks"]:
            if task.get("example"):
                continue
            wanted = task["instruction"].strip()
            free = [i for i in range(len(pairs)) if i not in used]
            match = [i for i in free if unescape(pairs[i][0]).rstrip().endswith(wanted)] or [i for i in free if wanted in unescape(pairs[i][0])]
            if not match:
                raise SystemExit(f"{nb}: keine Loesungs-Zelle fuer Aufgabe {lesson['id']}: {wanted[:70]}")
            used.add(match[0])
            # Abschnitts-Ueberschrift ("## ...") gehoert immer zur ersten Aufgabe des Abschnitts
            text = "### " + pairs[match[0]][0].partition("### ")[2]
            if lesson["section"] not in seen_sections:
                seen_sections.add(lesson["section"])
                text = f"{head_for[lesson['section']]}\n\n{text}"
            new.append(f'"""{text}"""')
            new.append(pairs[match[0]][1])
    if len(used) != len(pairs):
        raise SystemExit(f"{nb}: {len(pairs) - len(used)} Loesungs-Zelle(n) ohne passende Aufgabe")

    names, n_header = [], len(header)
    for i in range(len(new)):
        kind = "markdown" if i < n_header or (i - n_header) % 2 == 0 else "code"
        names.append(f"{i + 1:02d}_{kind}.py")
    target = dict(zip(names, new))
    if target == old:
        return True
    if not check:
        for f in files:
            f.unlink()
        for name, content in target.items():
            (nb / name).write_text(content, encoding="utf-8")
    print(f"{'ABWEICHUNG' if check else 'aktualisiert'}: {nb.relative_to(CONTENT)}")
    return False


def main():
    check = "--check" in sys.argv
    ok = True
    for week in range(1, 13):
        for theme in THEMES:
            for lang in ("de", "en"):
                ok = sync(week, theme, lang, check) and ok
    if check and not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
