# Beispiel 1: Einfache for-Schleife mit range()
print("=== Beispiel 1: 5 Runden reiten ===")
# range(5) erzeugt die Zahlen 0, 1, 2, 3, 4
for i in range(5):
    print(f"Runde {i+1}: Das Pferd trabt elegant")

print("\n=== Was passiert hier? ===")
print("1. range(5) erstellt: [0, 1, 2, 3, 4]")
print("2. i wird bei jedem Durchlauf auf das nächste Element gesetzt")
print("3. Wir geben i+1 aus, um von 1-5 zu zählen")
print("4. Die Schleife endet nach dem letzten Element")