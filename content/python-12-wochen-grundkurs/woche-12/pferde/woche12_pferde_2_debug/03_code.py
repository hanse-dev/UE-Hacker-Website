raum = {"beschreibung": "Eine große Halle.", "ausgaenge": {"norden": "keller", "osten": "turm"}}

richtung = "westen"
ziel = raum["ausgaenge"][richtung]
print(f"Du gehst nach {ziel}.")