zonen = {
    "Wiese": {"hindernis": "Graben", "preis": "Schleife", "schwierigkeit": 3},
    "Wald": {"hindernis": "Wassergraben", "preis": "Pokal", "schwierigkeit": 5},
    "Moor": {"hindernis": "Mauer", "preis": "Medaille", "schwierigkeit": 8},
}
for name, zone in zonen.items():
    print(f"{name}: {zone['hindernis']} / {zone['preis']}")
