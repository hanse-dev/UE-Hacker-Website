class Robot:
    def __init__(self, id, modell, energie, funktion):
        self.id = id
        self.modell = modell
        self.energie = energie
        self.funktion = funktion

    def vorstellen(self):
        print(f"Robot {self.id} | {self.modell} | Funktion: {self.funktion} | Energie: {self.energie}%")

r1 = Robot("R-001", "ServoX", 90, "Wartung")
r2 = Robot("R-002", "MediBot", 75, "Medizin")
r3 = Robot("R-003", "CombatX", 100, "Sicherheit")

for robot in [r1, r2, r3]:
    robot.vorstellen()

print(f"\nR-001 Modell: {r1.modell}")
print(f"R-002 Energie: {r2.energie}%")