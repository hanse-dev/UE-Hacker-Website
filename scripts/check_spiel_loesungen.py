#!/usr/bin/env python3
"""Prueft die Aufgaben der Spiel-Projekte (engine "spiel", z. B. content/ausweichen/).

Fuer jede Aufgabe in lessons.json:
- Die Loesung (`solution`) besteht alle Pruefschritte (`validation.checks`), mit mehreren Zufalls-Startwerten.
- Die unveraenderte Vorlage (`codeTemplate`) faellt durch - ausser bei Beispielen (`example`), die
  sofort bestehen muessen.
- Vorlage und Loesung lassen sich in Bloecke uebersetzen (src/spiel/zu_bloecken.py).

Laeuft mit normalem Python, ohne Browser: dieselbe Datei src/spiel/spiel.py wie in Pyodide.
Aufruf: python3 scripts/check_spiel_loesungen.py [content/ausweichen ...]
"""

import json
import random
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WURZEL / "src" / "spiel"))

import spiel  # noqa: E402
from zu_bloecken import zu_bloecken  # noqa: E402

KURSE = ["content/ausweichen"]
STARTWERTE = range(1, 6)


def pruefe(code, checks, startwert):
    """Fuehrt das Programm frisch aus und spielt die Pruefschritte durch -> (ok, Hinweis/Fehler)."""
    ns = {"__name__": "__main__"}
    spiel._neu(ns)
    random.seed(startwert)
    try:
        exec(compile(code, "<aufgabe>", "exec"), ns)
    except Exception as fehler:  # noqa: BLE001
        return False, f"Programm bricht ab: {type(fehler).__name__}: {fehler}"
    ergebnis = json.loads(spiel._pruefe(ns, json.dumps(checks)))
    if ergebnis["ok"]:
        return True, ""
    schritt = checks[ergebnis["schritt"]]
    return False, ergebnis["fehler"] or schritt.get("hint", "")


def main(ordner):
    fehler = []
    anzahl = 0
    for kurs in ordner:
        lektionen = json.loads((WURZEL / kurs / "lessons.json").read_text(encoding="utf-8"))
        for lektion in lektionen:
            for nr, aufgabe in enumerate(lektion["tasks"], 1):
                anzahl += 1
                ort = f"{kurs} {lektion['id']} Aufgabe {nr}"
                v = aufgabe.get("validation") or {}
                if v.get("type") != "spiel" or not v.get("checks"):
                    fehler.append(f"{ort}: validation.type 'spiel' mit checks fehlt")
                    continue
                for c in v["checks"]:
                    if not c.get("hint"):
                        fehler.append(f"{ort}: Pruefschritt ohne hint: {c}")
                vorlage = aufgabe.get("codeTemplate", "")
                loesung = vorlage if aufgabe.get("example") else aufgabe.get("solution")
                if not loesung:
                    fehler.append(f"{ort}: solution fehlt")
                    continue
                for startwert in STARTWERTE:
                    ok, info = pruefe(loesung, v["checks"], startwert)
                    if not ok:
                        fehler.append(f"{ort}: Loesung faellt durch (Startwert {startwert}): {info}")
                        break
                if not aufgabe.get("example"):
                    ok, _ = pruefe(vorlage, v["checks"], 1)
                    if ok:
                        fehler.append(f"{ort}: unveraenderte Vorlage besteht schon")
                for name, code in (("Vorlage", vorlage), ("Loesung", loesung)):
                    try:
                        zu_bloecken(code)
                    except (ValueError, SyntaxError) as e:
                        fehler.append(f"{ort}: {name} laesst sich nicht in Bloecke uebersetzen: {e}")
    for f in fehler:
        print("FEHLER", f)
    print(f"{anzahl} Aufgaben geprueft, {len(fehler)} Fehler")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or KURSE))
