beutel = {"Heiltrank": 3, "Fackel": 5, "Seil": 2}
try:
    print(beutel["Drachenei"])
except KeyError:
    print("Nicht im Lager: Drachenei")
