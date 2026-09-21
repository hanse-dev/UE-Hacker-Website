# 🐴 Etappe 1: Die Karte der Welt

Willkommen, junger Reitmeister! Du hast in elf Wochen alles gelernt, was ein Programmierer des **Reiterhofs** braucht. Jetzt setzt du alles zu einem echten Spiel zusammen: einem **Text-Adventure**, das du selbst baust und später beliebig erweiterst.

**Deine Mission:** Mitten in der Nacht ist das kleine Fohlen verschwunden! Durchsuche den Reiterhof, sammle nützliche Dinge, vertreibe den zornigen Ziegenbock und bringe das Fohlen zurück!

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
    "hof": {
        "beschreibung": "Du stehst auf dem Hof. Der Mond scheint, und aus dem Stall hörst du ein leises Wiehern.",
        "ausgaenge": {"norden": "stallgasse"},
    },
    "stallgasse": {
        "beschreibung": "Eine lange Stallgasse. Rechts und links stehen die Boxen der Pferde.",
        "ausgaenge": {"sueden": "hof", "osten": "koppel", "westen": "sattelkammer"},
    },
    "sattelkammer": {"beschreibung": "Die Sattelkammer riecht nach Leder. An der Wand hängen Sättel und Zaumzeug.", "ausgaenge": {"osten": "stallgasse"}},
    "koppel": {"beschreibung": "Die nächtliche Koppel. Im Gras steht das Fohlen – und davor ein zorniger Ziegenbock!", "ausgaenge": {"westen": "stallgasse"}},
}

def beschreibe(room_name):
    raum = welt[room_name]
    print(f"📍 {room_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("hof")
```
