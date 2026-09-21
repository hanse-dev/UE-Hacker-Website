def berechne_gewinn(auftraege, fehlschlaege):
    return auftraege * 10 - fehlschlaege * 5

print(f"Gewinn: {berechne_gewinn(8, 2)}")
