futter = {"Hafer": 3, "Heu": 5, "Möhren": 2}
try:
    print(futter["Zuckerrüben"])
except KeyError:
    print("Nicht im Lager: Zuckerrüben")
