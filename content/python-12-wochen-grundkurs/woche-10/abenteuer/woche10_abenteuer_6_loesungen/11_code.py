# Schritt 1: Klasse Schwert anlegen
class Schwert:
    def __init__(self, name, schaden, material):
        self.name = name
        self.schaden = schaden
        self.material = material
    
    # Bonus: Angriff-Methode
    def angriff(self):
        return f"{self.name} schlägt zu und verursacht {self.schaden} Schaden!"

# Schritt 2: Erstes Objekt erstellen
excalibur = Schwert("Excalibur", 50, "Stahl")
print("=== Schwert 1 ===")
print(f"Name: {excalibur.name}")
print(f"Schaden: {excalibur.schaden}")
print(f"Material: {excalibur.material}")
print(excalibur.angriff())

# Schritt 3: Zweites Schwert
feuerschwert = Schwert("Feuerschwert", 75, "Drachenstahl")
print("\n=== Schwert 2 ===")
print(f"Name: {feuerschwert.name}")
print(f"Schaden: {feuerschwert.schaden}")
print(f"Material: {feuerschwert.material}")
print(feuerschwert.angriff())