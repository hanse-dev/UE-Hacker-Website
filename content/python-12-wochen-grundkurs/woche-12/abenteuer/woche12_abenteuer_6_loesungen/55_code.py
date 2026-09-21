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

class Gegenstand:
    def __init__(self, name, beschreibung):
        self.name = name
        self.beschreibung = beschreibung

welt["keller"] = {"beschreibung": "Ein kühler Keller voller alter Fässer.", "ausgaenge": {"oben": "halle"}, "gegenstaende": [], "gegner": None}
welt["halle"]["ausgaenge"]["unten"] = "keller"
welt["keller"]["gegenstaende"].append(Gegenstand("Heiltrank", "Ein roter Trank, der Wunden heilt."))
print([g.name for g in welt["keller"]["gegenstaende"]])
