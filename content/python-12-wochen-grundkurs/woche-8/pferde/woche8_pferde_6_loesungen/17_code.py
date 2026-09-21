futter = {"Hafer": 3, "Heu": 5, "Möhren": 2}
gesamt = 0
for anzahl in futter.values():
    gesamt += anzahl
print(f"Gesamt: {gesamt}")
print(f"Sorten: {len(futter)}")
