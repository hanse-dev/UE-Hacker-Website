missionen = [["Scan-Mission", "Mars", 4], ["Rettungs-Mission", "Titan", 2], ["Reparaturflug", "Station", 3]]
def suche_missionen(liste, begriff):
    gefunden = []
    for mission in liste:
        if begriff in mission[0]:
            gefunden.append(mission)
    return gefunden

treffer = suche_missionen(missionen, "Mission")
print(f"Gefunden: {len(treffer)}")
