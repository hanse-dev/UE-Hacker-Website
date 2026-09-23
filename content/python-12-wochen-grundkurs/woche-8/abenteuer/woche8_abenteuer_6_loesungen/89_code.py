beutel = {"Heiltrank": 3, "Fackel": 5, "Seil": 2}
def menge_von(name):
    try:
        return beutel[name]
    except KeyError:
        return 0

print(f"Heiltrank: {menge_von('Heiltrank')}")
print(f"Drachenei: {menge_von('Drachenei')}")
