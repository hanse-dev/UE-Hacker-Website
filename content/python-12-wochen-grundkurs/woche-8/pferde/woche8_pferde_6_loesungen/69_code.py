zonen = {
    "Wiese": {"hindernis": "Graben", "preis": "Schleife", "schwierigkeit": 3},
    "Wald": {"hindernis": "Wassergraben", "preis": "Pokal", "schwierigkeit": 5},
    "Moor": {"hindernis": "Mauer", "preis": "Medaille", "schwierigkeit": 8},
}
gefaehrlichste = None
for name, zone in zonen.items():
    if gefaehrlichste is None or zone["schwierigkeit"] > zonen[gefaehrlichste]["schwierigkeit"]:
        gefaehrlichste = name
print(f"Gefährlichste: {gefaehrlichste} ({zonen[gefaehrlichste]['schwierigkeit']})")
