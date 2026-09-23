lager = {"Batterie": 3, "Kabel": 5, "Sensor": 2}
def menge_von(name):
    try:
        return lager[name]
    except KeyError:
        return 0

print(f"Batterie: {menge_von('Batterie')}")
print(f"Warpkern: {menge_von('Warpkern')}")
