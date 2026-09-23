funde = [
    {"name": "Kristallkern", "wert": 800, "ort": "Hangar"},
    {"name": "Sensorchip", "wert": 300, "ort": "Labor"},
    {"name": "Antimaterie", "wert": 650, "ort": "Brücke"},
]
ueber = 0
gesamt = 0
for s in funde:
    if s["wert"] > 500:
        ueber += 1
    gesamt += s["wert"]
print(f"Über 500: {ueber}")
print(f"Gesamtwert: {gesamt}")
