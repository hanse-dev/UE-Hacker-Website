pokale = [
    {"name": "Goldpokal", "wert": 800, "ort": "Halle"},
    {"name": "Silberschleife", "wert": 300, "ort": "Stall"},
    {"name": "Ehrenpreis", "wert": 650, "ort": "Reitplatz"},
]
werte = [s["wert"] for s in pokale]
werte = sorted(werte, reverse=True)
print(f"Werte: {werte}")
