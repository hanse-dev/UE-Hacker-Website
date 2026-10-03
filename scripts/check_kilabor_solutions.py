#!/usr/bin/env python3
"""
Prueft die Musterloesungen des KI-Labors (content/ki-labor-woche{N}/lessons.json, Feld
"referenceSolution" an jeder echten, d.h. nicht-Beispiel-Aufgabe):

- jede echte Aufgabe hat eine referenceSolution,
- sie laeuft mit python3 fehlerfrei,
- ihre Ausgabe enthaelt validation.expected (tolerant wie normalizeForComparison() in
  src/composables/useTaskValidation.js: Gross-/Kleinschreibung, Leerzeichen, Satzzeichen am Ende),
- sie nutzt alle validation.codeContains-Bausteine.

Das Feld heisst bewusst NICHT "solution": LessonView.vue blendet bei task.solution einen
"Loesung anzeigen"-Button ein (so bei den Projekt-Kursen) - im KI-Labor soll die Oberflaeche
unveraendert bleiben. Genutzt werden die Loesungen fuer die Offline-Downloads
(scripts/build_kilabor_notebook.py, scripts/build_offline_py.py).

Exit-Code 1 bei jedem Fehler. Ausgabe am Ende: "✓ N KI-Labor-Musterloesungen geprueft".
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEEKS = range(1, 9)


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text.lower()).strip()
    return re.sub(r"[.,!?:;]+$", "", text)


def main():
    problems = []
    checked = 0
    for week in WEEKS:
        lessons = json.loads((ROOT / "content" / f"ki-labor-woche{week}" / "lessons.json").read_text(encoding="utf-8"))
        for lesson in lessons:
            for idx, task in enumerate(lesson["tasks"]):
                if task.get("example"):
                    continue
                where = f"Woche {week} {lesson['id']} Aufgabe {idx}"
                code = task.get("referenceSolution")
                if not code:
                    problems.append(f"{where}: referenceSolution fehlt")
                    continue
                validation = task["validation"]
                try:
                    run = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, timeout=30)
                except subprocess.TimeoutExpired:
                    problems.append(f"{where}: Timeout")
                    continue
                if run.returncode != 0:
                    problems.append(f"{where}: Fehler - {run.stderr.strip().splitlines()[-1][:150]}")
                elif normalize(validation["expected"]) not in normalize(run.stdout):
                    problems.append(f"{where}: Ausgabe enthaelt nicht {validation['expected']!r}")
                for fragment in validation.get("codeContains") or []:
                    if fragment not in code:
                        problems.append(f"{where}: codeContains {fragment!r} fehlt")
                checked += 1

    for problem in problems:
        print("✘", problem)
    if problems:
        return 1
    print(f"✓ {checked} KI-Labor-Musterloesungen geprueft (laufen, richtige Ausgabe)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
