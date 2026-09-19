# Etappe 1: Die Karte der Welt als Dictionary
welt = {
    "schleuse": {
        "beschreibung": "Du stehst in der Schleuse. Rote Warnlichter blinken, und die Station brummt bedrohlich.",
        "ausgaenge": {"norden": "korridor"},
    },
    "korridor": {
        "beschreibung": "Ein langer Korridor mit vielen Türen. Notbeleuchtung taucht alles in rotes Licht.",
        "ausgaenge": {"sueden": "schleuse", "osten": "reaktorraum", "westen": "labor"},
    },
    "labor": {
        "beschreibung": "Ein Labor voller Geräte. Auf einem Tisch liegt Werkzeug bereit.",
        "ausgaenge": {"osten": "korridor"},
    },
    "reaktorraum": {
        "beschreibung": "Der Reaktorraum! Der Reaktor summt – und davor steht ein defekter Wartungsroboter!",
        "ausgaenge": {"westen": "korridor"},
    },
}

def beschreibe(raum_name):
    raum = welt[raum_name]
    print(f"📍 {raum_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("schleuse")