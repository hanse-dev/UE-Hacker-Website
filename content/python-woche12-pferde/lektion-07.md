# 🐴 Etappe 7: Speichern und das Finale

*Wissen aus Woche 9: JSON und Dateien*

Ein Objekt wie der Spieler lässt sich nicht direkt als JSON speichern. Deshalb baust du zuerst ein **Dictionary** (Name, Position, HP, Inventar als Liste von Dictionaries). Beim Laden geht es rückwärts. Fehlt die Datei, fängt `try/except` den `FileNotFoundError` ab.

```python
import json

def speichern(spieler, dateiname="stand.json"):
    daten = {
        "name": spieler.name,
        "position": spieler.position,
        "hp": spieler.hp,
        "inventar": [{"name": g.name, "beschreibung": g.beschreibung} for g in spieler.inventar],
    }
    with open(dateiname, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=2)
    print(f"💾 Spielstand von {spieler.name} gespeichert.")

def laden(dateiname="stand.json"):
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            daten = json.load(f)
    except FileNotFoundError:
        print("📂 Es gibt noch keinen Spielstand.")
        return None
    spieler = Spieler(daten["name"], daten["position"])
    spieler.hp = daten["hp"]
    for entry in daten["inventar"]:
        spieler.inventar.append(Gegenstand(entry["name"], entry["beschreibung"]))
    print(f"📂 Spielstand von {spieler.name} geladen.")
    return spieler

def spiele(spieler, befehle, ziel_gegenstand="Fohlen"):
    for text in befehle:
        print(f"\n> {text}")
        fuehre_aus(spieler, text)
        if spieler.hp <= 0:
            print("💀 Game Over – zu stark. Versuche es noch einmal!")
            return
        if hat_gegenstand(spieler, ziel_gegenstand):
            print("🏆 Du hast das Fohlen gefunden und in den Stall zurückgebracht. Der Reiterhof feiert dich!")
            return
```

Die Funktion `spiele()` ist die **Spielschleife**: Sie führt Befehle aus und prüft nach jedem Schritt, ob du gewonnen (Ziel-Gegenstand im Beutel) oder verloren hast (HP 0).

> 🎓 Geschafft! Du hast fast alles aus dem Kurs in einem Projekt benutzt – jetzt kannst du dein Spiel beliebig erweitern.
