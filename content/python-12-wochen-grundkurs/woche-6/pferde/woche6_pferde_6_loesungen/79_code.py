def erstelle_faecher(anzahl, plaetze):
    faecher = []
    for nr in range(anzahl):
        fach = []
        for platz in range(plaetze):
            fach.append("leer")
        faecher.append(fach)
    return faecher

print(erstelle_faecher(3, 2))
