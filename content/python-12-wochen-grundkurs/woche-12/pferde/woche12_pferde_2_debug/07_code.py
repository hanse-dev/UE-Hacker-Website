import json

class Spieler:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

mira = Spieler("Mira", 20)

with open("debug_stand.json", "w") as datei:
    json.dump(mira, datei)

with open("debug_stand.json", "r") as datei:
    daten = json.load(datei)
print(daten["name"])