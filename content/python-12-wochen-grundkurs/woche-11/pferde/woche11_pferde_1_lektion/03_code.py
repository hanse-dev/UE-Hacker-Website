# Beispiel 1: Einfache Vererbung
class Pferd:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    def fressen(self):
        print(f"{self.name} frisst Heu")

class Reitpferd(Pferd):
    def reiten(self, geschwindigkeit):
        print(f"{self.name} reitet mit {geschwindigkeit} km/h")

# Beispiel 2: Methoden überschreiben
class Vollblut(Reitpferd):
    def fressen(self):
        print(f"{self.name} frisst spezielles Kraftfutter")

    def rennen(self):
        print(f"{self.name} galoppiert wie der Wind! 🐎")

# Beispiel 3: super() verwenden
class Kaltblut(Pferd):
    def __init__(self, name, alter, zugkraft):
        super().__init__(name, alter)
        self.zugkraft = zugkraft

    def ziehen(self, last):
        print(f"{self.name} zieht {last} mit {self.zugkraft}kg Kraft")