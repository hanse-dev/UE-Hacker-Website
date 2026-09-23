turniere = [["Springturnier", "Halle", 4], ["Dressurturnier", "Platz", 2], ["Ausritt", "Wald", 3]]
def turnier_statistik(liste):
    anzahl = 0
    schwer = 0
    for turnier in liste:
        anzahl += 1
        if turnier[2] < 3:
            continue
        schwer += 1
    print(f"Turniere: {anzahl}")
    print(f"Schwere Turniere: {schwer}")

turnier_statistik(turniere)
