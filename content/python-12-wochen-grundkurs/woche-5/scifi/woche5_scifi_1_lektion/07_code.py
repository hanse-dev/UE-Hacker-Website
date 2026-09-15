# Beispiel 2: Funktion mit einem Parameter
def begruesse_piloten(name):
    """Begrüßt einen Piloten mit seinem Namen"""
    print(f"Hallo {name}!")
    print(f"Viel Erfolg bei deiner Mission, {name}!")

# Funktion mit verschiedenen Namen aufrufen
print("=== Verschiedene Piloten ===")
begruesse_piloten("Alex")
begruesse_piloten("Zara")
begruesse_piloten("Nova")

print("\n=== Was passiert hier? ===")
print("1. name ist ein Platzhalter für den übergebenen Wert")
print("2. Jeder Aufruf übergibt einen anderen Namen")
print("3. Die Funktion arbeitet mit dem übergebenen Wert")