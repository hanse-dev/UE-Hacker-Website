# Beispiel 2: Funktion mit einem Parameter
def gruesse_nach_name(name):
    """Begrüßt einen Helden mit seinem Namen"""
    print(f"Willkommen, {name}!")
    print(f"Viel Erfolg auf deiner Reise, {name}!")

# Funktion mit verschiedenen Namen aufrufen
print("=== Verschiedene Helden ===")
gruesse_nach_name("Aria")
gruesse_nach_name("Thorin")
gruesse_nach_name("Luna")

print("\n=== Was passiert hier? ===")
print("1. name ist ein Platzhalter für den übergebenen Wert")
print("2. Jeder Aufruf übergibt einen anderen Namen")
print("3. Die Funktion arbeitet mit dem übergebenen Wert")