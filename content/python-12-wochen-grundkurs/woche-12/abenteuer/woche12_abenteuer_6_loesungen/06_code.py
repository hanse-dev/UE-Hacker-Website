class Spieler:
    def __init__(self, name):
        self.name = name
        self.inventar = []

    def nimm(self, thing):
        self.inventar.append(thing)

mira = Spieler("Mira")
ben = Spieler("Ben")
mira.nimm("Fackel")
print("Mira:", mira.inventar)
print("Ben:", ben.inventar)