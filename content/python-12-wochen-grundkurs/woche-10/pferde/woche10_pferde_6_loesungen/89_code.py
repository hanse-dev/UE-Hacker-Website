class Pferd:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

    def trainiere(self):
        self.level += 1
        print(f"{self.name} trainiert: Level {self.level}")

    def galoppiere(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

    def ruhe_aus(self, menge):
        self.energie += menge
        if self.energie > 100:
            self.energie = 100

import json
pferd = Pferd("Blitz", 4)
daten = {"name": pferd.name, "level": pferd.level}
text = json.dumps(daten)
print(text)
neu = json.loads(text)
kopie = Pferd(neu["name"], neu["level"])
print(kopie.name)
