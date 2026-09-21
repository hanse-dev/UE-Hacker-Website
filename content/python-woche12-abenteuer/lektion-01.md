# ⚔️ Etappe 1: Die Karte der Welt

Willkommen, junger Magier! Du hast in elf Wochen alles gelernt, was ein Programmierer der **Gilde von Pyralia** braucht. Jetzt setzt du alles zu einem echten Spiel zusammen: einem **Text-Adventure**, das du selbst baust und später beliebig erweiterst.

**Deine Mission:** Erkunde die Drachenhöhle, sammle Gegenstände, besiege den Drachen und finde den Schatz von Pyralia!

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
    "eingang": {
        "beschreibung": "Du stehst am Eingang der Drachenhöhle. Es riecht nach Rauch.",
        "ausgaenge": {"norden": "halle"},
    },
    "halle": {
        "beschreibung": "Eine riesige Halle. Fackeln flackern an den Wänden.",
        "ausgaenge": {"sueden": "eingang", "osten": "schatzkammer", "westen": "quelle"},
    },
    "quelle": {"beschreibung": "Eine stille Quelle. Das Wasser funkelt magisch.", "ausgaenge": {"osten": "halle"}},
    "schatzkammer": {"beschreibung": "Gold, so weit du blicken kannst – und mittendrin schläft der Drache!", "ausgaenge": {"westen": "halle"}},
}

def beschreibe(room_name):
    raum = welt[room_name]
    print(f"📍 {room_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("eingang")
```
