# Beispiel 3: For-Schleife mit Schrittweite
print("=== Beispiel 3: Jeder zweite Sektor ===")
# range(0, 11, 2) erzeugt: 0, 2, 4, 6, 8, 10
for sektor in range(0, 11, 2):
    print(f"Sektor {sektor}: Verstärkung aktiviert")

print("\n=== Die Schrittweite ===")
print("range(start, ende, schritt) überspringt Sektoren")
print("Hier: jeder zweite Sektor überspringen")