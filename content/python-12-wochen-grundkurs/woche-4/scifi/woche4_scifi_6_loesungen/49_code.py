for deck in range(1, 11):
    print(f"Deck {deck}: OK")
    if deck == 3 or deck == 6 or deck == 9:
        print(f"⚠️ Warnung auf Deck {deck}")
    if deck == 5 or deck == 10:
        print(f"Bonus auf Deck {deck}")
