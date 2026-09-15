# Argument wird zur Variable: Schritt für Schritt
def begruesse_reiter(name):  # "name" ist der Parameter (Platzhalter)
    """Begrüßt einen Reiter mit seinem Namen"""
    # In der Funktion ist "name" jetzt eine Variable mit dem übergebenen Wert!
    print(f"In der Funktion: name = '{name}'")
    print(f"Hallo {name}!")

# Beim Aufruf: "Anna" ist das Argument
print("=== Aufruf: begruesse_reiter('Anna') ===")
begruesse_reiter("Anna")  # → name wird zu "Anna"

print("\n=== Aufruf: begruesse_reiter('Max') ===")
begruesse_reiter("Max")  # → name wird zu "Max"