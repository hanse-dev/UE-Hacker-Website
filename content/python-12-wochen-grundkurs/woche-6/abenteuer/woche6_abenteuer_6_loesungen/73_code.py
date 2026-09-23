def erzeuge_eintrag(material, nummer):
    return f"{material}-{nummer}"

katalog = []
for nummer in range(1, 11):
    katalog.append(erzeuge_eintrag("Gold", nummer))
print(f"Anzahl: {len(katalog)}")
print(katalog[-1])
