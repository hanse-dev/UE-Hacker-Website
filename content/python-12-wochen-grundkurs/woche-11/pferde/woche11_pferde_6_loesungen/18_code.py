# Lösungsvorschlag Boss-Quest 1 – Die Reitschul-Hierarchie

# Schritt 1: Basis-Klasse
class Reiter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def unterricht(self):
        print(f"{self.name} (Level {self.level}): Allgemeiner Reitunterricht.")

    def __str__(self):
        return f"Reiter {self.name} | Level: {self.level}"

# Schritt 2: Stufen
class Anfaenger(Reiter):
    def __init__(self, name):
        super().__init__(name, 1)

    def unterricht(self):
        print(f"{self.name} (Anfänger): Sitzhaltung, Schritt und Trab lernen. Helm auf!")

class Fortgeschrittener(Reiter):
    def __init__(self, name):
        super().__init__(name, 2)

    def unterricht(self):
        print(f"{self.name} (Fortgeschritten): Galopp, Seitengänge und erste Sprünge üben.")

class Profi(Reiter):
    def __init__(self, name):
        super().__init__(name, 3)

    def unterricht(self):
        print(f"{self.name} (Profi): Grand-Prix-Dressur, Hindernisrennen und Turniervorbereitung.")

# Schritt 3: Reitschule mit Polymorphismus
reitschule = [
    Anfaenger("Mia"),
    Fortgeschrittener("Jonas"),
    Profi("Sarah")
]

print("=== REITSCHULE SONNENTAL ===")
for reiter in reitschule:
    print(reiter)           # __str__
    reiter.unterricht()
    print()