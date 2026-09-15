class Pferd:
    def __init__(self, name, rasse, geschlecht):
        self.name = name
        self.rasse = rasse
        self.geschlecht = geschlecht

    def fuettern(self):
        print(f"{self.name} frisst. Mampf! 🐴")

    def vorstellen(self):
        print(f"{self.name} – {self.rasse} ({self.geschlecht})")

bella = Pferd("Bella", "Warmblut", "Stute")
max_pferd = Pferd("Max", "Pony", "Hengst")

bella.vorstellen()
max_pferd.vorstellen()
bella.fuettern()
max_pferd.fuettern()