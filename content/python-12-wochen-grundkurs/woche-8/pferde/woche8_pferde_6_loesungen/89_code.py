futter = {"Hafer": 3, "Heu": 5, "Möhren": 2}
def menge_von(name):
    try:
        return futter[name]
    except KeyError:
        return 0

print(f"Hafer: {menge_von('Hafer')}")
print(f"Zuckerrüben: {menge_von('Zuckerrüben')}")
