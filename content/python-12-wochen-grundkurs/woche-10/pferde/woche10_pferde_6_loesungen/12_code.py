class Reiter:
    def __init__(self, name, level=1, lieblingspferd="Keins"):
        self.name = name
        self.level = level
        self.lieblingspferd = lieblingspferd

    def vorstellen(self):
        print(f"{self.name} (Level {self.level}) – Lieblingspferd: {self.lieblingspferd}")

    def trainieren(self):
        self.level += 1
        print(f"{self.name} hat trainiert! Neues Level: {self.level}")

lisa = Reiter("Lisa", 3, "Thunder")
tom = Reiter("Tom", 1)
sarah = Reiter("Sarah", 5, "Luna")

print("=== Reitschule ===")
for reiter in [lisa, tom, sarah]:
    reiter.vorstellen()

tom.trainieren()
print(f"Toms Level nach Training: {tom.level}")