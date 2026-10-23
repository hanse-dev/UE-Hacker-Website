preise = {"Hafer": 30, "Heu": 5, "Möhren": 10}
teuerster = ""
hoechster = 0
for name, preis in preise.items():
    if preis > hoechster:
        hoechster = preis
        teuerster = name
print(f"Teuerster Posten: {teuerster} ({hoechster})")
