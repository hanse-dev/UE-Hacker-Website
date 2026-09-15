# Argument wird zur Variable: Schritt für Schritt
def gruesse_nach_name(name):  # "name" ist der Parameter (Platzhalter)
    """Begrüßt einen Helden mit seinem Namen"""
    # In der Funktion ist "name" jetzt eine Variable mit dem übergebenen Wert!
    print(f"In der Funktion: name = '{name}'")
    print(f"Willkommen, {name}!")

# Beim Aufruf: "Aria" ist das Argument
print("=== Aufruf: gruesse_nach_name('Aria') ===")
gruesse_nach_name("Aria")  # → name wird zu "Aria"

print("\n=== Aufruf: gruesse_nach_name('Thorin') ===")
gruesse_nach_name("Thorin")  # → name wird zu "Thorin"