lager = {"Batterie": 3, "Kabel": 5, "Sensor": 2}
try:
    print(lager["Warpkern"])
except KeyError:
    print("Nicht im Lager: Warpkern")
