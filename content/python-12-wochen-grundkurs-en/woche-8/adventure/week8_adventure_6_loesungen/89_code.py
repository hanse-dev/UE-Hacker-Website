bag = {"Potion": 3, "Torch": 5, "Rope": 2}
def amount_of(name):
    try:
        return bag[name]
    except KeyError:
        return 0

print(f"Potion: {amount_of('Potion')}")
print(f"Dragon egg: {amount_of('Dragon egg')}")
