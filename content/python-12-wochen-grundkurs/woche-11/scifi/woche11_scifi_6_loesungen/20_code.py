# Lösungsvorschlag Boss-Quest 2 – Die Roboter-Familie

# Schritt 1: Basis-Klasse
class Roboter:
    def __init__(self, name, energie):
        self.name = name
        self.energie = energie

    def aufgabe(self):
        print(f"{self.name} führt eine allgemeine Aufgabe aus. (Energie: {self.energie})")

    def __str__(self):
        return f"🤖 {self.name} | Energie: {self.energie}"

    def __eq__(self, other):
        return self.energie == other.energie

# Schritt 2: Typen
class Kampfroboter(Roboter):
    def aufgabe(self):
        print(f"{self.name} (Kampf): Feinde neutralisieren! RATATATATA! (Energie -{15})")
        self.energie -= 15

class Heilroboter(Roboter):
    def aufgabe(self):
        print(f"{self.name} (Heilung): Verletzungen reparieren und Vitalzeichen stabilisieren. (Energie -{5})")
        self.energie -= 5

class Erkundungsroboter(Roboter):
    def aufgabe(self):
        print(f"{self.name} (Erkundung): Sektor scannen und Kartendaten aktualisieren. (Energie -{8})")
        self.energie -= 8

# Schritt 3: Einsatz
titan = Kampfroboter("Titan", 100)
medix = Heilroboter("Medix", 100)
explorer = Erkundungsroboter("Explorer", 100)

print("=== ROBOTER-EINSATZ ===")
for roboter in [titan, medix, explorer]:
    print(roboter)         # __str__
    roboter.aufgabe()
    print(f"  Verbleibende Energie: {roboter.energie}")
    print()

print(f"Titan und Medix gleich viel Energie? {titan == medix}")