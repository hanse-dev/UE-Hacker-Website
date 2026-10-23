preise = {"Heiltrank": 30, "Fackel": 5, "Seil": 10}
teuerster = ""
hoechster = 0
for name, preis in preise.items():
    if preis > hoechster:
        hoechster = preis
        teuerster = name
print(f"Teuerster Posten: {teuerster} ({hoechster})")
