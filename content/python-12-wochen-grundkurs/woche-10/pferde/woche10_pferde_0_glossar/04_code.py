class Pferd:
    def __init__(self, name, rasse="Unbekannt"):
        self.name = name
        self.rasse = rasse
        self.fitness = 0

    def vorstellen(self):
        print(f"Ich bin {self.name}, ein {self.rasse}!")

    def trainieren(self):
        self.fitness += 10
        print(f"{self.name} trainiert! Fitness jetzt: {self.fitness}")

# Objekte erstellen
pferd1 = Pferd("Bobby")
pferd2 = Pferd("Blitz", rasse="Haflinger")

pferd1.vorstellen()   # Ich bin Bobby, ein Unbekannt!
pferd1.trainieren()   # Bobby trainiert! Fitness jetzt: 10
print(pferd2.rasse)   # Haflinger