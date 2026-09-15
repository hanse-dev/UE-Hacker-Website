# Lösungsvorschlag Boss-Quest 3 – Das Stallbewohner-System

# Schritt 1: Basis-Klasse
class Stallbewohner:
    def __init__(self, name):
        self.name = name

    def laut_machen(self):
        print(f"{self.name} macht ein Geräusch...")

    def __str__(self):
        return f"Stallbewohner: {self.name}"

    def __len__(self):
        return len(self.name)

# Schritt 2: Tiere ableiten
class Stallpferd(Stallbewohner):
    def laut_machen(self):
        print(f"{self.name} (Pferd): WIEHERRR! 🐴")

class Stallhund(Stallbewohner):
    def laut_machen(self):
        print(f"{self.name} (Hund): WUFF WUFF! 🐕")

class Stallkatze(Stallbewohner):
    def laut_machen(self):
        print(f"{self.name} (Katze): Miau~ 🐱")

class Stallhuhn(Stallbewohner):
    def laut_machen(self):
        print(f"{self.name} (Huhn): GACKGACK! 🐔")

# Schritt 3: Morgenrunde
stall = [
    Stallpferd("Sterntaler"),
    Stallhund("Rex"),
    Stallkatze("Mimi"),
    Stallhuhn("Henriette")
]

print("=== MORGENRUNDE IM STALL ===")
for tier in stall:
    print(tier)             # __str__
    tier.laut_machen()      # Polymorphismus!
    print(f"  Namenslänge: {len(tier)}")   # __len__
    print()

print("🎉 Herausforderung abgeschlossen!")
print("🏆 Du hast die Meisterzüchterin besiegt!")
print("⭐ Titel erhalten: Meister der Pferde-OOP")
print()
print("🎊 GLÜCKWUNSCH! Du hast Woche 11 gemeistert!")