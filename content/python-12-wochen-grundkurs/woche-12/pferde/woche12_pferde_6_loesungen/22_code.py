# Boss-Quest 2: Dein eigenes Mini-Abenteuer (Beispiellösung: "Die alte Scheune")
scheune = {
    "weg": {
        "beschreibung": "Ein staubiger Feldweg. Vor dir steht eine alte Scheune.",
        "ausgaenge": {"norden": "tenne"},
        "gegenstaende": [Gegenstand("Leiter", "Eine stabile Holzleiter.")],
        "gegner": None,
    },
    "tenne": {
        "beschreibung": "Die Tenne der Scheune. Eine Leiter führt nach oben.",
        "ausgaenge": {"sueden": "weg", "oben": "heuboden", "osten": "box"},
        "gegenstaende": [],
        "gegner": None,
    },
    "heuboden": {
        "beschreibung": "Der Heuboden. Es duftet nach Sommer.",
        "ausgaenge": {"unten": "tenne"},
        "gegenstaende": [Gegenstand("Heu", "Weiches, trockenes Heu.")],
        "gegner": None,
    },
    "box": {
        "beschreibung": "Eine Box, in der ein Kater faucht!",
        "ausgaenge": {"westen": "tenne", "norden": "schatz"},
        "gegenstaende": [],
        "gegner": Gegner("Kater", 12, 5),
    },
    "schatz": {
        "beschreibung": "Hinter der Box hängt der goldene Sattel des Turniersiegers!",
        "ausgaenge": {"sueden": "box"},
        "gegenstaende": [Gegenstand("Sattel", "Der goldene Sattel.")],
        "gegner": None,
    },
}

welt = scheune  # die Spiel-Funktionen arbeiten mit dem Namen "welt" – wir tauschen die Welt einfach aus
held = Spieler("Ida", "weg")
held.hp = 30
spiele(held, ["nimm Leiter", "gehe norden", "gehe oben", "nimm Heu", "gehe unten", "gehe osten", "gehe norden", "nimm Sattel"], "Sattel")