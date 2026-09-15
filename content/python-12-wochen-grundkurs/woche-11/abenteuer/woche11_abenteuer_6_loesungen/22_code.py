# Lösungsvorschlag Boss-Quest 3 – Das polymorphe Tier-System

# Schritt 1: Basis-Klasse
class Tier:
    def __init__(self, name):
        self.name = name

    def laut_machen(self):
        print(f"{self.name} macht ein allgemeines Geräusch...")

    def __str__(self):
        return f"Tier: {self.name}"

    def __len__(self):
        return len(self.name)

# Schritt 2: Tier-Arten
class Hund(Tier):
    def laut_machen(self):
        print(f"{self.name}: WUFF WUFF! 🐕")

class Katze(Tier):
    def laut_machen(self):
        print(f"{self.name}: Miau~ 🐱")

class Drache(Tier):
    def laut_machen(self):
        print(f"{self.name}: ROOOAAAAR! 🐉 *Feuer*")

class Eule(Tier):
    def laut_machen(self):
        print(f"{self.name}: Uhuu~ 🦉")

# Schritt 3: Tier-Parade
tiere = [
    Hund("Bello"),
    Katze("Whiskers"),
    Drache("Infernox"),
    Eule("Minerva")
]

print("=== TIER-PARADE ===")
for tier in tiere:
    print(tier)              # __str__
    tier.laut_machen()       # Polymorphismus!
    print(f"  Namenslänge: {len(tier)}")   # __len__
    print()

print("🎉 Boss-Quest abgeschlossen!")
print("🏆 Du hast den Archimagier besiegt!")
print("⭐ Titel erhalten: Meister der OOP-Künste")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 11 gemeistert!")