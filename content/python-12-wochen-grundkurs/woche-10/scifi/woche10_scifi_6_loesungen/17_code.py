class Raumschiff:
    def __init__(self, name, typ, crew_staerke, schild=100):
        self.name = name
        self.typ = typ
        self.crew_staerke = crew_staerke
        self.schild = schild

    def vorstellen(self):
        print(f"🛸 {self.name} | {self.typ} | Crew: {self.crew_staerke} | Schild: {self.schild}%")

    def angreifen(self, ziel):
        schaden = self.crew_staerke * 2
        ziel.schild = max(0, ziel.schild - schaden)
        print(f"{self.name} greift {ziel.name} an! Schaden: {schaden}. Schild: {ziel.schild}%")

    def reparieren(self):
        self.schild = min(100, self.schild + 25)
        print(f"{self.name} repariert. Schild: {self.schild}%")

nova = Raumschiff("Nova-Hawk", "Kampfschiff", 30)
defender = Raumschiff("Defender", "Kreuzer", 20, 80)
nova.vorstellen()
defender.vorstellen()
nova.angreifen(defender)
defender.reparieren()