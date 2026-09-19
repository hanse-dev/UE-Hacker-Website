# Etappe 6: Spielstand speichern und laden
import json

def speichern(spieler, dateiname="spielstand.json"):
    daten = {
        "name": spieler.name,
        "position": spieler.position,
        "hp": spieler.hp,
        "inventar": [{"name": g.name, "beschreibung": g.beschreibung} for g in spieler.inventar],
    }
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=2)
    print(f"💾 Spielstand von {spieler.name} gespeichert.")

def laden(dateiname="spielstand.json"):
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
    except FileNotFoundError:
        print("📂 Es gibt noch keinen Spielstand.")
        return None
    spieler = Spieler(daten["name"], daten["position"])
    spieler.hp = daten["hp"]
    for eintrag in daten["inventar"]:
        spieler.inventar.append(Gegenstand(eintrag["name"], eintrag["beschreibung"]))
    print(f"📂 Spielstand von {spieler.name} geladen.")
    return spieler

speichern(held)
geladen = laden()
geladen.zeige_inventar()