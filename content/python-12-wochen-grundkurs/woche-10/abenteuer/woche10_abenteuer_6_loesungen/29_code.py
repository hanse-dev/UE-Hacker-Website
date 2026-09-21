class Held:
    def __init__(self, name, level=1, energie=100):
        self.name = name
        self.level = level
        self.energie = energie

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

    def trainiere(self):
        self.level += 1
        print(f"{self.name} trainiert: Level {self.level}")

    def kaempfe(self, kosten):
        self.energie -= kosten
        if self.energie < 0:
            self.energie = 0

    def ruhe_aus(self, menge):
        self.energie += menge
        if self.energie > 100:
            self.energie = 100

gruppe = [Held("Aria", 3), Held("Thorin", 8), Held("Luna", 5)]
for h in gruppe:
    print(h.name)
