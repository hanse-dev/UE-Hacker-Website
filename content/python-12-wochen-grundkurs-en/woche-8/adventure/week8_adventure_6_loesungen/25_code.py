bag = {"Potion": 3, "Torch": 5, "Rope": 2}
try:
    print(bag["Dragon egg"])
except KeyError:
    print("Not in store: Dragon egg")
