schaetze = [
    {"name": "Goldkrone", "wert": 800, "ort": "Turm"},
    {"name": "Silberkelch", "wert": 300, "ort": "Keller"},
    {"name": "Rubin", "wert": 650, "ort": "Höhle"},
]
ueber = 0
gesamt = 0
for s in schaetze:
    if s["wert"] > 500:
        ueber += 1
    gesamt += s["wert"]
print(f"Über 500: {ueber}")
print(f"Gesamtwert: {gesamt}")
