# Lösungsvorschlag Mission 1 – Die Pferde-Hierarchie

# Schritt 1: Basisklasse
class Pferd:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self.geschlecht = geschlecht

    def wiehern(self):
        print(f"{self.name} wiehert: WIEHERRR! 🐴")

# Schritt 2: Kind-Klassen
class Reitpferd(Pferd):
    def __init__(self, name, alter, geschlecht):
        super().__init__(name, alter, geschlecht)
        self.disziplin = "Dressur"

    def training(self):
        print(f"{self.name} übt {self.disziplin} – elegante Bewegungen!")

class Kaltblut(Pferd):
    def __init__(self, name, alter, geschlecht):
        super().__init__(name, alter, geschlecht)
        self.zugkraft_kg = 1500

    def ziehen(self):
        print(f"{self.name} zieht bis zu {self.zugkraft_kg} kg – ein starkes Arbeitspferd!")

class Pony(Pferd):
    def __init__(self, name, alter, geschlecht):
        super().__init__(name, alter, geschlecht)
        self.groesse_cm = 145

    def info(self):
        print(f"{self.name} ist ein Pony mit {self.groesse_cm} cm Stockmaß.")

# Schritt 3: Objekte erstellen und Methoden aufrufen
valencia = Reitpferd("Valencia", 7, "Stute")
valencia.wiehern()
valencia.training()

print()
bruno = Kaltblut("Bruno", 10, "Hengst")
bruno.wiehern()
bruno.ziehen()

print()
sterntaler = Pony("Sterntaler", 5, "Wallach")
sterntaler.wiehern()
sterntaler.info()

# Bonus: Dressurpferd erbt von Reitpferd
print()
class Dressurpferd(Reitpferd):
    def __init__(self, name, alter, geschlecht):
        super().__init__(name, alter, geschlecht)
        self.disziplin = "Grand-Prix-Dressur"
        self.titel = "Champion"

    def gala_auftritt(self):
        print(f"{self.name}, {self.titel}, zeigt eine Kür auf höchstem Niveau!")

bella_donna = Dressurpferd("Bella Donna", 12, "Stute")
bella_donna.wiehern()        # von Pferd geerbt
bella_donna.training()       # von Reitpferd geerbt
bella_donna.gala_auftritt()