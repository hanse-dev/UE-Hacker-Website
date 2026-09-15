# Step 1: Deck scanner
for deck in range(1, 11):
    print(f"Deck {deck}: System OK")

# Step 2: Warnings for decks 5 and 8
print()
for deck in range(1, 11):
    if deck == 5:
        print(f"Deck {deck}: ⚠️ WARNING – Shield weak!")
    elif deck == 8:
        print(f"Deck {deck}: ⚠️ WARNING – Energy low!")
    else:
        print(f"Deck {deck}: ✅ All normal")

# Step 3: Bonus for decks 1-3
print()
for deck in range(1, 11):
    if deck <= 3:
        print(f"Deck {deck}: ⭐ Bonus efficiency active")
    else:
        print(f"Deck {deck}: Standard")