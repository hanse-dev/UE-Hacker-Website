turniere = [["Springturnier", "Halle", 4], ["Dressurturnier", "Platz", 2], ["Ausritt", "Wald", 3]]
def suche_turniere(liste, begriff):
    gefunden = []
    for turnier in liste:
        if begriff in turnier[0]:
            gefunden.append(turnier)
    return gefunden

treffer = suche_turniere(turniere, "turnier")
print(f"Gefunden: {len(treffer)}")
