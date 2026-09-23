def zeige_liste(liste):
    for nr, eintrag in enumerate(liste):
        print(f"{nr + 1}: {eintrag}")

schaetze = ["Gold", "Kristall", "Amulett"]
zeige_liste(schaetze)
