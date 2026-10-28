zonen = {
    "Wiese": {"hindernis": "Graben", "preis": "Schleife", "schwierigkeit": 3},
    "Wald": {"hindernis": "Wassergraben", "preis": "Pokal", "schwierigkeit": 5},
    "Moor": {"hindernis": "Mauer", "preis": "Medaille", "schwierigkeit": 8},
}
koennen = 5
machbar = []
for name, zone in zonen.items():
    if zone["schwierigkeit"] <= koennen:
        machbar.append(name)
print(f"Machbar: {machbar}")
