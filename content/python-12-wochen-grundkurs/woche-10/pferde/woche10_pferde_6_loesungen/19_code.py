class Reitschueler:
    def __init__(self, name, level=1, lieblingspferd="Keins"):
        self.name = name
        self.level = level
        self.lieblingspferd = lieblingspferd

    def vorstellen(self):
        print(f"👤 {self.name} | Level {self.level} | Pferd: {self.lieblingspferd}")

    def unterricht(self, lektion):
        print(f"{self.name} lernt: {lektion}")
        self.level += 1

class Reitschule:
    def __init__(self, name):
        self.name = name
        self.schueler = []

    def anmelden(self, schueler):
        self.schueler.append(schueler)
        print(f"{schueler.name} in '{self.name}' angemeldet.")

    def zeige_alle(self):
        print(f"\n=== {self.name} ({len(self.schueler)} Schüler) ===")
        for s in self.schueler:
            s.vorstellen()

schule = Reitschule("Sonnental Reitschule")
schule.anmelden(Reitschueler("Lisa", 3, "Thunder"))
schule.anmelden(Reitschueler("Tom", 1))
schule.anmelden(Reitschueler("Sarah", 5, "Luna"))
schule.zeige_alle()