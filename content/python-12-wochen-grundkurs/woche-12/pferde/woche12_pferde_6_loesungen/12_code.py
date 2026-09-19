# Mission 1: Der neue Raum
welt["futterkammer"] = {
    "beschreibung": "Säcke voller Hafer und Heu stapeln sich bis zur Decke.",
    "ausgaenge": {"sueden": "stallgasse"},
    "gegenstaende": [Gegenstand("Hafersack", "Ein praller Sack mit frischem Hafer.")],
    "gegner": None,
}
welt["stallgasse"]["ausgaenge"]["norden"] = "futterkammer"

held = Spieler("Mira", "stallgasse")
held.gehe("norden")
held.nimm("Hafersack")
held.zeige_inventar()