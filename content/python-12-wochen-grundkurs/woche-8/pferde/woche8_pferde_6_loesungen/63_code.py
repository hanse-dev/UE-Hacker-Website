pokale = [
    {"name": "Goldpokal", "wert": 800, "ort": "Halle"},
    {"name": "Silberschleife", "wert": 300, "ort": "Stall"},
    {"name": "Ehrenpreis", "wert": 650, "ort": "Reitplatz"},
]
ueber = 0
gesamt = 0
for s in pokale:
    if s["wert"] > 500:
        ueber += 1
    gesamt += s["wert"]
print(f"Über 500: {ueber}")
print(f"Gesamtwert: {gesamt}")
