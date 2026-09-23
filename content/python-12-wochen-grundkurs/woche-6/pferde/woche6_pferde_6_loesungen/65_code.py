def zeige_liste(liste):
    for nr, eintrag in enumerate(liste):
        print(f"{nr + 1}: {eintrag}")

pferde = ["Sturmwind", "Blitz", "Luna"]
zeige_liste(pferde)
