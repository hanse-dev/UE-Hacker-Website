raum = {"beschreibung": "Eine große Halle.", "ausgaenge": {"norden": "keller", "osten": "turm"}}

richtung = "westen"
if richtung in raum["ausgaenge"]:
    ziel = raum["ausgaenge"][richtung]
    print(f"Du gehst nach {ziel}.")
else:
    print("🚫 Dort geht es nicht weiter!")