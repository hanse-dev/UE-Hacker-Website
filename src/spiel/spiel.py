"""Das Spiel-Modul fuer die Spiel-Projekte (z. B. "Ausweichen").

Die Kinder schreiben:

    from spiel import *

    spieler = figur(180, 350, 40, 20, "blau")

    def jedes_bild():
        if taste("links"):
            spieler.x -= 5

Die Seite (src/composables/useSpiel.js) fuehrt zuerst das ganze Programm aus und ruft danach
60-mal pro Sekunde `jedes_bild()` auf, liest die Figuren und zeichnet sie auf ein Canvas. So
braucht es keine Endlosschleife (Pyodide laeuft im Browser-Tab und darf ihn nie blockieren).

Alles mit Unterstrich ist fuer die Seite und die Pruefung, nicht fuer die Kinder. Dieselbe Datei
laeuft auch in normalem Python (scripts/check_spiel_loesungen.py prueft damit alle Loesungen).
"""

import json
import random
import time

__all__ = ["BREITE", "HOEHE", "figur", "taste", "zufall", "zeige", "hintergrund", "spiel_ende"]

BREITE = 400
HOEHE = 400

# Deutsche Farbnamen -> Farben fuer das Canvas. Andere Werte (z. B. "#ff8800") gehen unveraendert durch.
FARBEN = {
    "rot": "#e5484d",
    "blau": "#3b82f6",
    "gruen": "#22a35a",
    "gelb": "#f5c518",
    "orange": "#f97316",
    "lila": "#8b5cf6",
    "pink": "#ec4899",
    "tuerkis": "#14b8a6",
    "braun": "#92400e",
    "grau": "#9ca3af",
    "schwarz": "#111827",
    "weiss": "#ffffff",
}

TASTEN = ("links", "rechts", "oben", "unten", "leertaste")

_figuren = []
_tasten = set()
_zustand = {"text": "", "vorbei": False, "endtext": "", "hintergrund": "#0f172a", "bild": 0}


class Figur:
    """Ein Rechteck auf der Buehne. x/y ist die linke obere Ecke, y waechst nach unten."""

    def __init__(self, x, y, breite, hoehe, farbe):
        self.x = x
        self.y = y
        self.breite = breite
        self.hoehe = hoehe
        self.farbe = farbe

    def beruehrt(self, andere):
        """True, wenn sich die beiden Rechtecke ueberlappen."""
        if self not in _figuren or andere not in _figuren:
            return False
        return (self.x < andere.x + andere.breite and andere.x < self.x + self.breite
                and self.y < andere.y + andere.hoehe and andere.y < self.y + self.hoehe)

    def entferne(self):
        """Nimmt die Figur von der Buehne."""
        if self in _figuren:
            _figuren.remove(self)

    def __repr__(self):
        return f"figur({self.x}, {self.y}, {self.breite}, {self.hoehe}, {self.farbe!r})"


def figur(x, y, breite, hoehe, farbe="blau"):
    """Erzeugt eine neue Figur und stellt sie auf die Buehne."""
    neu = Figur(x, y, breite, hoehe, farbe)
    _figuren.append(neu)
    return neu


def taste(name):
    """True, solange die Taste gedrueckt ist: "links", "rechts", "oben", "unten" oder "leertaste"."""
    if name not in TASTEN:
        raise ValueError(f'Diese Taste kenne ich nicht: {name!r}. Moeglich: {", ".join(TASTEN)}')
    return name in _tasten


def zufall(von, bis):
    """Eine zufaellige ganze Zahl von `von` bis `bis` (beide eingeschlossen)."""
    return random.randint(von, bis)


def zeige(text):
    """Schreibt einen Text oben links auf die Buehne (z. B. den Punktestand)."""
    _zustand["text"] = str(text)


def hintergrund(farbe):
    """Faerbt die Buehne ein."""
    _zustand["hintergrund"] = _farbe(farbe)


def spiel_ende(text="Spiel vorbei!"):
    """Haelt das Spiel an und zeigt den Text gross in der Mitte."""
    _zustand["vorbei"] = True
    _zustand["endtext"] = str(text)


# ---------------------------------------------------------------- fuer die Seite und die Pruefung

def _farbe(name):
    name = str(name)
    return FARBEN.get(name.lower().replace("ü", "ue").replace("ß", "ss"), name)


def _neu(ns=None):
    """Vor jedem Lauf: Buehne leeren und eine alte jedes_bild()-Funktion vergessen."""
    _figuren.clear()
    _tasten.clear()
    _zustand.update({"text": "", "vorbei": False, "endtext": "", "hintergrund": "#0f172a", "bild": 0})
    if ns is not None:
        ns.pop("jedes_bild", None)


def _setze_tasten(namen):
    _tasten.clear()
    _tasten.update(n for n in namen if n in TASTEN)


def _bild(ns, zeitlimit=1.0):
    """Ein Bild weiterrechnen: ruft jedes_bild() aus dem Programm der Kinder auf.

    Der Loop-Guard aus usePyodide.js baut in jede Schleife eine Pruefung gegen __cell_deadline__
    ein - die muss vor jedem Aufruf neu gesetzt werden, sonst ist sie laengst abgelaufen.
    """
    if _zustand["vorbei"]:
        return
    funktion = ns.get("jedes_bild")
    if not callable(funktion):
        return
    ns["__cell_deadline__"] = time.time() + zeitlimit
    funktion()
    _zustand["bild"] += 1


def _hat_jedes_bild(ns):
    return callable(ns.get("jedes_bild"))


def _stand():
    """Was die Seite zum Zeichnen braucht, als JSON-Text (reine Werte, keine Python-Objekte)."""
    figuren = []
    for f in _figuren:
        try:
            figuren.append([float(f.x), float(f.y), float(f.breite), float(f.hoehe), _farbe(f.farbe)])
        except (TypeError, ValueError):
            pass
    return json.dumps({
        "figuren": figuren,
        "text": _zustand["text"],
        "vorbei": _zustand["vorbei"],
        "endtext": _zustand["endtext"],
        "hintergrund": _zustand["hintergrund"],
    })


def _pruefe(ns, pruefungen_json):
    """Spielt die Pruefschritte aus lessons.json (validation.checks) durch.

    Jeder Schritt: optional `setze` (Python-Code, der vorher im Programm laeuft, z. B. einen Stein
    ueber den Spieler legen), `tasten` (gedrueckt gehaltene Tasten), `bilder` (wie viele Bilder
    weiterrechnen) und `pruefe` (Python-Ausdruck, der danach True sein muss). Die Schritte bauen
    aufeinander auf. Im Ausdruck gibt es zusaetzlich `spiel_vorbei`, `angezeigt`, `alle_figuren` und
    `hintergrundfarbe`.

    Ergebnis (JSON): {"ok": bool, "schritt": Index des ersten Fehlers, "fehler": Python-Fehler}.
    """
    pruefungen = json.loads(pruefungen_json)
    for index, schritt in enumerate(pruefungen):
        try:
            if schritt.get("setze"):
                exec(schritt["setze"], ns)
            _setze_tasten(schritt.get("tasten", []))
            for _ in range(int(schritt.get("bilder", 0))):
                _bild(ns)
            _setze_tasten([])
            hilfen = {
                "spiel_vorbei": _zustand["vorbei"],
                "angezeigt": _zustand["text"],
                "alle_figuren": list(_figuren),
                "hintergrundfarbe": _zustand["hintergrund"],
            }
            if schritt.get("pruefe") and not eval(schritt["pruefe"], ns, hilfen):
                return json.dumps({"ok": False, "schritt": index, "fehler": ""})
        except BaseException as fehler:  # noqa: BLE001 - jeder Fehler im Kinder-Code zaehlt als "nicht bestanden",
            # auch _CellTimeout (Loop-Guard aus usePyodide.js), der bewusst von BaseException erbt.
            name = type(fehler).__name__
            if name == "_CellTimeout":
                return json.dumps({"ok": False, "schritt": index, "fehler": "timeout"})
            return json.dumps({"ok": False, "schritt": index, "fehler": f"{name}: {fehler}"})
    return json.dumps({"ok": True, "schritt": -1, "fehler": ""})
