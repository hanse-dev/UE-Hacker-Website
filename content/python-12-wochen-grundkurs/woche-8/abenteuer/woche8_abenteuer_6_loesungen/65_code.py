schaetze = [
    {"name": "Goldkrone", "wert": 800, "ort": "Turm"},
    {"name": "Silberkelch", "wert": 300, "ort": "Keller"},
    {"name": "Rubin", "wert": 650, "ort": "Höhle"},
]
werte = [s["wert"] for s in schaetze]
werte = sorted(werte, reverse=True)
print(f"Werte: {werte}")
