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

class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["lager"] = {"beschreibung": "Ein Lager voller Kisten.", "ausgaenge": {"oben": "korridor"}, "gegenstaende": [], "gegner": None}
welt["korridor"]["ausgaenge"]["unten"] = "lager"
welt["lager"]["gegenstaende"].append(Gegenstand("Energiezelle", "Eine Zelle, die Energie zurückgibt."))
print([g.name for g in welt["lager"]["gegenstaende"]])
