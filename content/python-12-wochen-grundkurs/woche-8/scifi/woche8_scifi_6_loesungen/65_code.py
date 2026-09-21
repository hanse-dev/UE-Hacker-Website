funde = [
    {"name": "Kristallkern", "wert": 800, "ort": "Hangar"},
    {"name": "Sensorchip", "wert": 300, "ort": "Labor"},
    {"name": "Antimaterie", "wert": 650, "ort": "Brücke"},
]
werte = [s["wert"] for s in funde]
werte = sorted(werte, reverse=True)
print(f"Werte: {werte}")
