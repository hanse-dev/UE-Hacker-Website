lager = {"Batterie": 3, "Kabel": 5, "Sensor": 2}
gesamt = 0
for anzahl in lager.values():
    gesamt += anzahl
print(f"Gesamt: {gesamt}")
print(f"Sorten: {len(lager)}")
