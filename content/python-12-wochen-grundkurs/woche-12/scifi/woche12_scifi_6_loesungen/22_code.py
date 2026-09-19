# Boss-Quest 2: Dein eigenes Mini-Abenteuer (Beispiellösung: "Das Frachtschiff")
frachter = {
    "dock": {
        "beschreibung": "Ein stilles Dock. Vor dir liegt ein altes Frachtschiff.",
        "ausgaenge": {"norden": "gang"},
        "gegenstaende": [Gegenstand("Schluessel", "Ein schwerer Schlüssel.")],
        "gegner": None,
    },
    "gang": {
        "beschreibung": "Ein enger Gang mit einer Treppe nach oben und unten.",
        "ausgaenge": {"sueden": "dock", "oben": "kabine", "unten": "laderaum"},
        "gegenstaende": [],
        "gegner": None,
    },
    "laderaum": {
        "beschreibung": "Ein dunkler Laderaum. Etwas glänzt zwischen den Kisten.",
        "ausgaenge": {"oben": "gang"},
        "gegenstaende": [Gegenstand("Werkzeug", "Ein stabiles Multifunktionswerkzeug.")],
        "gegner": None,
    },
    "kabine": {
        "beschreibung": "Die Kapitänskabine. Ein Wachroboter versperrt den Weg!",
        "ausgaenge": {"unten": "gang", "norden": "brücke"},
        "gegenstaende": [],
        "gegner": Gegner("Wachroboter", 12, 5),
    },
    "brücke": {
        "beschreibung": "Die Brücke des Schiffs. Hier liegt der Energiekristall!",
        "ausgaenge": {"sueden": "kabine"},
        "gegenstaende": [Gegenstand("Kristall", "Der Energiekristall.")],
        "gegner": None,
    },
}

welt = frachter  # die Spiel-Funktionen arbeiten mit dem Namen "welt" – wir tauschen die Welt einfach aus
held = Spieler("Ida", "dock")
held.hp = 30
spiele(held, ["nimm Schluessel", "gehe norden", "gehe unten", "nimm Werkzeug", "gehe oben", "gehe oben", "gehe norden", "nimm Kristall"], "Kristall")