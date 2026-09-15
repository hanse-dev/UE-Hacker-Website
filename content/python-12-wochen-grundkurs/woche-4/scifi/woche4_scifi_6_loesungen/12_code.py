# Schritt 1: Deck-Scanner
for deck in range(1, 11):
    print(f"Deck {deck}: System OK")

# Schritt 2: Warnungen für Deck 5 und 8
print()
for deck in range(1, 11):
    if deck == 5:
        print(f"Deck {deck}: ⚠️ WARNUNG – Schild schwach!")
    elif deck == 8:
        print(f"Deck {deck}: ⚠️ WARNUNG – Energie niedrig!")
    else:
        print(f"Deck {deck}: ✅ Alles normal")

# Schritt 3: Bonus für Decks 1-3
print()
for deck in range(1, 11):
    if deck <= 3:
        print(f"Deck {deck}: ⭐ Bonus-Effizienz aktiv")
    else:
        print(f"Deck {deck}: Standard")