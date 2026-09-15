def generiere_datensatz(datentyp, komplexitaet):
    basis = ["A-01", "B-02", "C-03"]
    erweitert = ["D-04", "E-05", "F-06"]
    profi = ["G-07", "H-08", "I-09"]
    daten = [f"{datentyp}-{eintrag}" for eintrag in basis]
    if komplexitaet >= 2:
        daten += [f"{datentyp}-{e}" for e in erweitert]
    if komplexitaet >= 3:
        daten += [f"{datentyp}-{e}" for e in profi]
    return daten

schiffsdaten = generiere_datensatz("Schiff", 2)
missionsdaten = generiere_datensatz("Mission", 3)
print(f"Schiffsdaten: {schiffsdaten}")
print(f"Missionsdaten: {missionsdaten}")
gefiltert = [d for d in missionsdaten if "G" in d or "H" in d]
print(f"Gefiltert: {gefiltert}")