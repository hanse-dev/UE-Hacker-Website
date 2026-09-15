# Beispiel 3: For-Schleife mit Schrittweite
print("=== Beispiel 3: Jede zweite Zahl von 0 bis 10 ===")
# range(0, 11, 2) erzeugt: 0, 2, 4, 6, 8, 10
for gerade in range(0, 11, 2):
    print(f"Gerade Zahl: {gerade}")

print("\n=== Die Schrittweite ===")
print("range(start, ende, schritt) springt immer 'schritt' Positionen weiter")
print("Hier: start=0, ende=11, schritt=2 → 0, 2, 4, 6, 8, 10")