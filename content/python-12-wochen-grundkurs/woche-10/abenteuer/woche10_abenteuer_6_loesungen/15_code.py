# Schritt 1: Klasse Drache anlegen
class Drache:
    def __init__(self, name, alter, element):
        self.name = name
        self.alter = alter
        self.element = element

    # Schritt 2: Methode feuer_atmen
    def feuer_atmen(self):
        print(f"{self.name} atmet {self.element}: PUFF! 🔥")

    # Bonus: fliegen-Methode
    def fliegen(self):
        print(f"{self.name} breitet die Flügel aus und hebt ab! 🐉")

# Schritt 3: Zwei Drachen erstellen
feuerdrache = Drache("Smaug", 500, "Feuer")
eisdrache = Drache("Frostmaw", 300, "Eis")

drachen = [feuerdrache, eisdrache]

for drache in drachen:
    print(f"\n=== {drache.name} ===")
    print(f"Alter: {drache.alter} Jahre")
    print(f"Element: {drache.element}")
    drache.feuer_atmen()
    drache.fliegen()