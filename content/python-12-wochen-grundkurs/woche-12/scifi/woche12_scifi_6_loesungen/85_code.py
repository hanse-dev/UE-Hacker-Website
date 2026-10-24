bestenliste = {"Mira": 120, "Tom": 90, "Lena": 150}
beste = None
for name in bestenliste:
    if beste is None or bestenliste[name] > bestenliste[beste]:
        beste = name
print(f"Bester: {beste}")
