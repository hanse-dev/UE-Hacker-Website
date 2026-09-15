# Beispiel 1: Einfache Vererbung
class Roboter:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def aktivieren(self):
        print(f"{self.name} wird aktiviert")

class Android(Roboter):
    def lernen(self, information):
        print(f"{self.name} lernt: {information}")

# Beispiel 2: Methoden überschreiben
class Kampfroboter(Android):
    def aktivieren(self):
        print(f"{self.name} im Kampfbetrieb aktiviert!")

    def angreifen(self, ziel):
        print(f"{self.name} greift {ziel} an!")

# Beispiel 3: super() verwenden
class Medizinroboter(Android):
    def __init__(self, id, name, spezialisierung):
        super().__init__(id, name)
        self.spezialisierung = spezialisierung

    def heilen(self, patient):
        print(f"{self.name} behandelt {patient} mit {self.spezialisierung}")
