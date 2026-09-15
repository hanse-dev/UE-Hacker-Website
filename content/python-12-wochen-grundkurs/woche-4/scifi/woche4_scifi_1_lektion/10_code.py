# Beispiel 1: Einfache while-Schleife
print("=== Beispiel 1: Bis 10 scannen ===")
scan = 0
while scan <= 10:
    print(f"Scan {scan}: Daten empfangen")
    scan += 1  # WICHTIG: Hochzählen, sonst Endlosschleife!

print("\n=== Was passiert hier? ===")
print("1. scan startet bei 0")
print("2. Solange scan <= 10, wird der Code ausgeführt")
print("3. scan += 1 erhöht den Wert bei jedem Durchlauf")
print("4. Bei scan = 11 wird die Bedingung falsch → Schleife endet")