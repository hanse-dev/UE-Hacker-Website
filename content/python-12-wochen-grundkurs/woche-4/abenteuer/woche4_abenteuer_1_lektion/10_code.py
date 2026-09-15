# Beispiel 1: Einfache while-Schleife
print("=== Beispiel 1: Bis 5 zählen ===")
zaehler = 0
while zaehler <= 5:
    print(f"Zaehler: {zaehler}")
    zaehler += 1  # WICHTIG: Hochzählen, sonst Endlosschleife!

print("\n=== Was passiert hier? ===")
print("1. zaehler startet bei 0")
print("2. Solange zaehler <= 5, wird der Code ausgeführt")
print("3. zaehler += 1 erhöht den Wert bei jedem Durchlauf")
print("4. Bei zaehler = 6 wird die Bedingung falsch → Schleife endet")