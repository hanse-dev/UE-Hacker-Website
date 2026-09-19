# Boss-Quest 2: Dein eigenes Mini-Abenteuer (Beispiellösung: "Der verlassene Turm")
turm = {
    "hof": {
        "beschreibung": "Ein verwilderter Hof. Vor dir ragt ein alter Turm auf.",
        "ausgaenge": {"norden": "treppe"},
        "gegenstaende": [Gegenstand("Laterne", "Spendet warmes Licht.")],
        "gegner": None,
    },
    "treppe": {
        "beschreibung": "Eine knarrende Wendeltreppe.",
        "ausgaenge": {"sueden": "hof", "oben": "labor", "unten": "keller"},
        "gegenstaende": [],
        "gegner": None,
    },
    "keller": {
        "beschreibung": "Ein feuchter Keller. Etwas funkelt im Dunkeln.",
        "ausgaenge": {"oben": "treppe"},
        "gegenstaende": [Gegenstand("Zauberstab", "Ein Stab voller Magie.")],
        "gegner": None,
    },
    "labor": {
        "beschreibung": "Das Labor des Turmmagiers. Ein Golem versperrt den Weg!",
        "ausgaenge": {"unten": "treppe", "norden": "dach"},
        "gegenstaende": [],
        "gegner": Gegner("Golem", 12, 5),
    },
    "dach": {
        "beschreibung": "Das Dach des Turms. Hier liegt die Krone der Sterne!",
        "ausgaenge": {"sueden": "labor"},
        "gegenstaende": [Gegenstand("Krone", "Die Krone der Sterne.")],
        "gegner": None,
    },
}

welt = turm  # die Spiel-Funktionen arbeiten mit dem Namen "welt" – wir tauschen die Welt einfach aus
held = Spieler("Ida", "hof")
held.hp = 30
spiele(held, ["nimm Laterne", "gehe norden", "gehe unten", "nimm Zauberstab", "gehe oben", "gehe oben", "gehe norden", "nimm Krone"], "Krone")