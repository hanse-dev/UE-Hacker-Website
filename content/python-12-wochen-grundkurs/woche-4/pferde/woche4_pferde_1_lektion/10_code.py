# Beispiel 1: Einfache while-Schleife
print("=== Beispiel 1: Bis 10 zählen ===")
zaehler = 0
while zaehler <= 10:
    print(f"Hufschlag {zaehler}")
    zaehler += 1  # WICHTIG: Hochzählen, sonst Endlosschleife!

print("\n=== Was passiert hier? ===")
print("1. zaehler startet bei 0")
print("2. Solange zaehler <= 10, wird der Code ausgeführt")
print("3. zaehler += 1 erhöht den Wert bei jedem Durchlauf")
print("4. Bei zaehler = 11 wird die Bedingung falsch → Schleife endet")