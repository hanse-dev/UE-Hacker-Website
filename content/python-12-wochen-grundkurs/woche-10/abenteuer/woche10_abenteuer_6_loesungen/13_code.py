# Schritt 1: Klasse Magier anlegen
class Magier:
    def __init__(self, name, level=1, zauber="Feuerball", element="Feuer"):
        self.name = name
        self.level = level
        self.zauber = zauber
        self.element = element  # Bonus

# Schritt 2: Drei Magier erstellen
merlin = Magier("Merlin", level=15, zauber="Blitz", element="Blitz")
gandalf = Magier("Gandalf", level=20, zauber="Licht", element="Licht")
dumbledore = Magier("Dumbledore", level=18, zauber="Expelliarmus", element="Arcana")

magier_liste = [merlin, gandalf, dumbledore]

print("=== Magiergilde ===")
for m in magier_liste:
    print(f"{m.name}: Level {m.level} ({m.element})")

# Schritt 3: Stärksten finden
staerkster = max(magier_liste, key=lambda m: m.level)
print(f"\nStärkster Magier: {staerkster.name} (Level {staerkster.level})")