bestenliste = {"Mira": 120, "Tom": 90, "Lena": 150}
for name in sorted(bestenliste, key=bestenliste.get, reverse=True):
    print(f"{name}: {bestenliste[name]}")
