zonen = {
    "Wiese": {"hindernis": "Graben", "preis": "Schleife", "schwierigkeit": 3},
    "Wald": {"hindernis": "Wassergraben", "preis": "Pokal", "schwierigkeit": 5},
    "Moor": {"hindernis": "Mauer", "preis": "Medaille", "schwierigkeit": 8},
}
gefaehrlichste = ""
hoechste = 0
for name, zone in zonen.items():
    if zone["schwierigkeit"] > hoechste:
        hoechste = zone["schwierigkeit"]
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({hoechste})")
