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

def staerkere(a, b):
    if a.level >= b.level:
        return a
    return b

sieger = staerkere(Pferd("Blitz", 4), Pferd("Stella", 9))
print(f"Sieger: {sieger.name}")
