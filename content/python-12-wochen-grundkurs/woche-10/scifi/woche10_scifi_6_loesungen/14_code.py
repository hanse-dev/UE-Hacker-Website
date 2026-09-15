class Raumschiff:
    def __init__(self, name, klasse, besatzung):
        self.name = name
        self.klasse = klasse
        self.besatzung = besatzung

    def hypersprung(self):
        print(f"{self.name}: Hypersprung eingeleitet! 🚀")

    def vorstellen(self):
        print(f"🛸 {self.name} | {self.klasse} | Besatzung: {self.besatzung}")

nebula = Raumschiff("Nebula-7", "Forschungsschiff", 150)
titan = Raumschiff("Titan", "Kampfkreuzer", 500)
scout = Raumschiff("Scout-1", "Aufklärungsschiff", 25)

flotte = [nebula, titan, scout]
print("=== Flotte ===")
for schiff in flotte:
    schiff.vorstellen()

nebula.hypersprung()