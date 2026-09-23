preise = {"Batterie": 30, "Kabel": 5, "Sensor": 10}
teuerster = None
for name, preis in preise.items():
    if teuerster is None or preis > preise[teuerster]:
        teuerster = name
print(f"Teuerster Posten: {teuerster} ({preise[teuerster]})")
