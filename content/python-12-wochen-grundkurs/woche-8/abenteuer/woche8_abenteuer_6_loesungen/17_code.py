beutel = {"Heiltrank": 3, "Fackel": 5, "Seil": 2}
gesamt = 0
for anzahl in beutel.values():
    gesamt += anzahl
print(f"Gesamt: {gesamt}")
print(f"Sorten: {len(beutel)}")
