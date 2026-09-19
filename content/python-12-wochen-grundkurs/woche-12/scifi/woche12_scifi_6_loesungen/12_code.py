# Mission 1: Der neue Raum
welt["kommandobruecke"] = {
    "beschreibung": "Bildschirme flimmern über einer verlassenen Steuerkonsole.",
    "ausgaenge": {"sueden": "korridor"},
    "gegenstaende": [Gegenstand("Datenchip", "Ein Chip voller Missionsdaten.")],
    "gegner": None,
}
welt["korridor"]["ausgaenge"]["norden"] = "kommandobruecke"

held = Spieler("Mira", "korridor")
held.gehe("norden")
held.nimm("Datenchip")
held.zeige_inventar()