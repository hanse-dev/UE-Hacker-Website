# 🚀 Etappe 1: Die Karte der Welt

Willkommen, Techniker! Du hast in elf Wochen alles gelernt, was ein Programmierer der **Nebula-7** braucht. Jetzt setzt du alles zu einem echten Spiel zusammen: einem **Text-Adventure**, das du selbst baust und später beliebig erweiterst.

**Deine Mission:** Auf der Raumstation Nebula-7 ist ein Notfall ausgebrochen! Erkunde die Station, sammle Ausrüstung, überwinde den defekten Wartungsroboter und schalte den Reaktor ab, bevor es zu spät ist!

Wir bauen das Spiel in **7 Etappen**. Bei jeder Etappe zeigt ein Hinweis, woher das Wissen stammt:

| Etappe | Was du baust | Wissen aus |
|---|---|---|
| 1 | Die Karte der Welt | Woche 8 (Dictionaries) |
| 2 | Bewegung | Woche 3–5 (if, Funktionen) |
| 3 | Gegenstände | Woche 6 + 10 (Listen, Klassen) |
| 4 | Spieler und Inventar | Woche 10 (Klassen, Komposition) |
| 5 | Gegner und Kampf | Woche 7 + 11 (random, Methoden) |
| 6 | Falsche Eingaben | Woche 8 (try/except) |
| 7 | Speichern und Finale | Woche 9 (JSON, Dateien) |

## 🗺️ Etappe 1: Die Karte der Welt

*Wissen aus Woche 8: Dictionaries*

Eine Welt besteht aus Räumen mit Beschreibung und Ausgängen. Das passt in ein **Dictionary, das weitere Dictionaries enthält**: Der Schlüssel ist der Raumname, der Wert ein Dictionary mit Beschreibung und Ausgängen (Richtung → nächster Raum). Die Funktion `beschreibe()` (Woche 5) schaut den Raum nach und gibt ihn mit einem f-String aus.



```python
welt = {
    "schleuse": {
        "beschreibung": "Du stehst in der Schleuse. Rote Warnlichter blinken, und die Station brummt bedrohlich.",
        "ausgaenge": {"norden": "korridor"},
    },
    "korridor": {
        "beschreibung": "Ein langer Korridor mit vielen Türen. Notbeleuchtung taucht alles in rotes Licht.",
        "ausgaenge": {"sueden": "schleuse", "osten": "reaktorraum", "westen": "labor"},
    },
    "labor": {"beschreibung": "Ein Labor voller Geräte. Auf einem Tisch liegt Werkzeug bereit.", "ausgaenge": {"osten": "korridor"}},
    "reaktorraum": {"beschreibung": "Der Reaktorraum! Der Reaktor summt – und davor steht ein defekter Wartungsroboter!", "ausgaenge": {"westen": "korridor"}},
}

def beschreibe(room_name):
    raum = welt[room_name]
    print(f"📍 {room_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("schleuse")
```
