# Beispiel 1: Die Sektor-Scans
print("=== Alle Decks werden gescannt ===")
for deck in range(1, 4):
    print(f"Deck {deck}:")
    for raum in range(1, 3):
        print(f"  Raum {raum} wird gescannt...")

# Beispiel 2: Ein Hologramm-Muster
print("\n=== Ein Hologramm-Muster ===")
for zeile in range(3):
    for spalte in range(4):
        print("✨", end=" ")
    print()