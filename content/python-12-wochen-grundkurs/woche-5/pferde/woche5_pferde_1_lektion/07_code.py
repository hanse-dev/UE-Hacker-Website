# Beispiel 2: Funktion mit einem Parameter
def begruesse_reiter(name):
    """Begrüßt einen Reiter mit seinem Namen"""
    print(f"Hallo {name}!")
    print(f"Viel Erfolg beim Training, {name}!")

# Funktion mit verschiedenen Namen aufrufen
print("=== Verschiedene Reiter ===")
begruesse_reiter("Anna")
begruesse_reiter("Max")
begruesse_reiter("Lena")

print("\n=== Was passiert hier? ===")
print("1. name ist ein Platzhalter für den übergebenen Wert")
print("2. Jeder Aufruf übergibt einen anderen Namen")
print("3. Die Funktion arbeitet mit dem übergebenen Wert")