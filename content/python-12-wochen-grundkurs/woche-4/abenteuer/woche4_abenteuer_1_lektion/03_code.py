# Beispiel 1: Einfache for-Schleife mit range()
print("=== Beispiel 1: Zählen von 0 bis 4 ===")
# range(5) erzeugt die Zahlen 0, 1, 2, 3, 4
for i in range(5):
    print(f"Durchlauf {i}: Der Wert von i ist {i}")

print("\n=== Was passiert hier? ===")
print("1. range(5) erstellt: [0, 1, 2, 3, 4]")
print("2. i wird bei jedem Durchlauf auf das nächste Element gesetzt")
print("3. Die Schleife endet nach dem letzten Element")