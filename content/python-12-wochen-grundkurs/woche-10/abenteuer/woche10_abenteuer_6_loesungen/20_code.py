# Boss-Quest 2: Die Kreaturen-Menagerie

# Schritt 1: Kreatur-Klasse
class Kreatur:
    def __init__(self, name, art, lieblingsfutter, futter_menge_kg=2):
        self.name = name
        self.art = art
        self.lieblingsfutter = lieblingsfutter
        self.futter_menge_kg = futter_menge_kg
        self.sattheit = 0  # Bonus

    # Schritt 2: Methoden
    def vorstellen(self):
        print(f"Ich bin {self.name}, ein {self.art}! Mein Lieblingsfutter ist {self.lieblingsfutter}.")

    def fressen(self):
        print(f"{self.name} frisst {self.lieblingsfutter}. Nom nom! ({self.futter_menge_kg} kg)")

    # Bonus: füttern-Methode
    def füttern(self, menge):
        self.sattheit += menge
        print(f"{self.name} gefüttert: +{menge} kg. Sattheit: {self.sattheit} kg")

# Schritt 3: Menagerie füllen
menagerie = [
    Kreatur("Lumi", "Einhorn", "Mondblüten", futter_menge_kg=3),
    Kreatur("Greifar", "Greif", "Sternenstaub", futter_menge_kg=5),
    Kreatur("Ignira", "Phönix", "Glutbeeren", futter_menge_kg=1),
    Kreatur("Skalor", "Jungdrache", "Kristallerz", futter_menge_kg=20),
]

print("=== Magische Kreaturen-Menagerie von Pyralia ===")
for kreatur in menagerie:
    kreatur.vorstellen()
    kreatur.fressen()
    print()

# Kreatur mit dem meisten Futter finden
vielfresser = max(menagerie, key=lambda k: k.futter_menge_kg)
print(f"Größter Vielfresser: {vielfresser.name} ({vielfresser.art}) mit {vielfresser.futter_menge_kg} kg/Tag")

# Bonus: Füttern
print("\n=== Fütterungsrunde ===")
for kreatur in menagerie:
    kreatur.füttern(kreatur.futter_menge_kg)
