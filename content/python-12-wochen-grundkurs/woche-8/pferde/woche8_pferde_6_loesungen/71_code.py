zonen = {
    "Wiese": {"hindernis": "Graben", "preis": "Schleife", "schwierigkeit": 3},
    "Wald": {"hindernis": "Wassergraben", "preis": "Pokal", "schwierigkeit": 5},
    "Moor": {"hindernis": "Mauer", "preis": "Medaille", "schwierigkeit": 8},
}
stark = 5
betretbar = []
for name, zone in zonen.items():
    if zone["schwierigkeit"] <= stark:
        betretbar.append(name)
print(f"Betretbar: {betretbar}")
