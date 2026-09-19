class Spieler:
    inventar = []

    def __init__(self, name):
        self.name = name

    def nimm(self, thing):
        self.inventar.append(thing)

mira = Spieler("Mira")
ben = Spieler("Ben")
mira.nimm("Taschenlampe")
print("Mira:", mira.inventar)
print("Ben:", ben.inventar)