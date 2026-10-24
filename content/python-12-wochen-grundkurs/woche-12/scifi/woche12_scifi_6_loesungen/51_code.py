class Spieler:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.inventar = []

    def nimm(self, gegenstand_name):
        self.inventar.append(gegenstand_name)

spieler = Spieler("Mira", "schleuse")
spieler.nimm("Zugangskarte")
print(f"Anzahl: {len(spieler.inventar)}")
