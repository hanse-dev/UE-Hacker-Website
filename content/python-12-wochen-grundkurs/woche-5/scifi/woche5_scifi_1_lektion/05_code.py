# Argument wird zur Variable: Schritt für Schritt
def begruesse_piloten(name):  # "name" ist der Parameter (Platzhalter)
    """Begrüßt einen Piloten mit seinem Namen"""
    # In der Funktion ist "name" jetzt eine Variable mit dem übergebenen Wert!
    print(f"In der Funktion: name = '{name}'")
    print(f"Hallo {name}!")

# Beim Aufruf: "Alex" ist das Argument
print("=== Aufruf: begruesse_piloten('Alex') ===")
begruesse_piloten("Alex")  # → name wird zu "Alex"

print("\n=== Aufruf: begruesse_piloten('Zara') ===")
begruesse_piloten("Zara")  # → name wird zu "Zara"