# Etappe 1: Die Karte der Welt als Dictionary
welt = {
    "eingang": {
        "beschreibung": "Du stehst am Eingang der Drachenhöhle. Es riecht nach Rauch.",
        "ausgaenge": {"norden": "halle"},
    },
    "halle": {
        "beschreibung": "Eine riesige Halle. Fackeln flackern an den Wänden.",
        "ausgaenge": {"sueden": "eingang", "osten": "schatzkammer", "westen": "quelle"},
    },
    "quelle": {
        "beschreibung": "Eine stille Quelle. Das Wasser funkelt magisch.",
        "ausgaenge": {"osten": "halle"},
    },
    "schatzkammer": {
        "beschreibung": "Gold, so weit du blicken kannst – und mittendrin schläft der Drache!",
        "ausgaenge": {"westen": "halle"},
    },
}

def beschreibe(raum_name):
    raum = welt[raum_name]
    print(f"📍 {raum_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("eingang")