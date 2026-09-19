# Etappe 1: Die Karte der Welt als Dictionary
welt = {
    "hof": {
        "beschreibung": "Du stehst auf dem Hof. Der Mond scheint, und aus dem Stall hörst du ein leises Wiehern.",
        "ausgaenge": {"norden": "stallgasse"},
    },
    "stallgasse": {
        "beschreibung": "Eine lange Stallgasse. Rechts und links stehen die Boxen der Pferde.",
        "ausgaenge": {"sueden": "hof", "osten": "koppel", "westen": "sattelkammer"},
    },
    "sattelkammer": {
        "beschreibung": "Die Sattelkammer riecht nach Leder. An der Wand hängen Sättel und Zaumzeug.",
        "ausgaenge": {"osten": "stallgasse"},
    },
    "koppel": {
        "beschreibung": "Die nächtliche Koppel. Im Gras steht das Fohlen – und davor ein zorniger Ziegenbock!",
        "ausgaenge": {"westen": "stallgasse"},
    },
}

def beschreibe(raum_name):
    raum = welt[raum_name]
    print(f"📍 {raum_name.capitalize()}: {raum['beschreibung']}")
    print("   Ausgänge:", ", ".join(raum["ausgaenge"]))

beschreibe("hof")