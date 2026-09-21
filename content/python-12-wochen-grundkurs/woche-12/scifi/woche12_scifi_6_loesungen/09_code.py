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

def gehe(position, richtung):
    ausgaenge = welt[position]["ausgaenge"]
    if richtung in ausgaenge:
        neue_position = ausgaenge[richtung]
        beschreibe(neue_position)
        return neue_position
    print("🚫 Dort geht es nicht weiter!")
    return position

position = gehe("schleuse", "norden")
print(f"Position: {position}")
