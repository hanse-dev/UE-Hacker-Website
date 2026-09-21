class Spieler:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.inventar = []

    def nimm(self, item_name):
        self.inventar.append(item_name)

spieler = Spieler("Mira", "eingang")
spieler.nimm("Fackel")
print(f"Anzahl: {len(spieler.inventar)}")
