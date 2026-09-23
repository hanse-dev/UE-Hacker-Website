missionen = [["Scan-Mission", "Mars", 4], ["Rettungs-Mission", "Titan", 2], ["Reparaturflug", "Station", 3]]
def missions_statistik(liste):
    anzahl = 0
    schwer = 0
    for mission in liste:
        anzahl += 1
        if mission[2] < 3:
            continue
        schwer += 1
    print(f"Missionen: {anzahl}")
    print(f"Schwere Missionen: {schwer}")

missions_statistik(missionen)
