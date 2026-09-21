def erstelle_faecher(anzahl, plaetze):
    faecher = []
    for _nr in range(anzahl):
        fach = []
        for _platz in range(plaetze):
            fach.append("leer")
        faecher.append(fach)
    return faecher
def platziere(faecher, index, name):
    fach = faecher[index]
    for platz in range(len(fach)):
        if fach[platz] == "leer":
            fach[platz] = name
            break

faecher = erstelle_faecher(3, 2)
platziere(faecher, 1, "Chip")
platziere(faecher, 1, "Kabel")
print(faecher)
