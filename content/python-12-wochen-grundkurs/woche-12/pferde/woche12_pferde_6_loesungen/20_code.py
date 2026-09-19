# Boss-Quest 1: Der vollständige Spielstand
def speichern_komplett(spieler, dateiname="komplett.json"):
    raeume_daten = {}
    for raum_name, raum in welt.items():
        gegner = raum["gegner"]
        raeume_daten[raum_name] = {
            "gegenstaende": [{"name": g.name, "beschreibung": g.beschreibung} for g in raum["gegenstaende"]],
            "gegner_hp": gegner.hp if gegner is not None else None,
        }
    daten = {
        "spieler": {
            "name": spieler.name,
            "position": spieler.position,
            "hp": spieler.hp,
            "inventar": [{"name": g.name, "beschreibung": g.beschreibung} for g in spieler.inventar],
        },
        "raeume": raeume_daten,
    }
    with open(dateiname, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, ensure_ascii=False, indent=2)
    print("💾 Kompletter Spielstand gespeichert.")

def laden_komplett(dateiname="komplett.json"):
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
    except FileNotFoundError:
        print("📂 Kein Spielstand gefunden.")
        return None
    for raum_name, zustand in daten["raeume"].items():
        raum = welt[raum_name]
        raum["gegenstaende"] = [Gegenstand(e["name"], e["beschreibung"]) for e in zustand["gegenstaende"]]
        if raum["gegner"] is not None:
            raum["gegner"].hp = zustand["gegner_hp"]
    s = daten["spieler"]
    spieler = Spieler(s["name"], s["position"])
    spieler.hp = s["hp"]
    for e in s["inventar"]:
        spieler.inventar.append(Gegenstand(e["name"], e["beschreibung"]))
    print("📂 Kompletter Spielstand geladen.")
    return spieler

# Test: Waffe nehmen, speichern, Welt zerstören, laden
held = Spieler("Tom", "sattelkammer")
held.nimm("Stallbesen")
speichern_komplett(held)
welt["sattelkammer"]["gegenstaende"] = [Gegenstand("Müll", "Nur Schrott.")]
held = laden_komplett()
held.zeige_inventar()
print("Im sattelkammer liegt:", [g.name for g in welt["sattelkammer"]["gegenstaende"]])