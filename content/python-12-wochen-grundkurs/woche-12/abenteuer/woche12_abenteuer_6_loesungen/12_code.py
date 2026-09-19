# Mission 1: Der neue Raum
welt["bibliothek"] = {
    "beschreibung": "Staubige Regale voller uralter Schriftrollen.",
    "ausgaenge": {"sueden": "halle"},
    "gegenstaende": [Gegenstand("Zauberbuch", "Ein Buch, das von selbst umblättert.")],
    "gegner": None,
}
welt["halle"]["ausgaenge"]["norden"] = "bibliothek"

held = Spieler("Mira", "halle")
held.gehe("norden")
held.nimm("Zauberbuch")
held.zeige_inventar()