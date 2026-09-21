def zeige_liste(liste):
    for nr, eintrag in enumerate(liste):
        print(f"{nr + 1}: {eintrag}")

module = ["Antrieb", "Sensor", "Schild"]
zeige_liste(module)
