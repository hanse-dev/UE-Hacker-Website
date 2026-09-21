quests = [["Drachenjagd", "Berg", 4], ["Schatzjagd", "Höhle", 2], ["Rätselwald", "Wald", 3]]
def suche_quests(liste, begriff):
    gefunden = []
    for quest in liste:
        if begriff in quest[0]:
            gefunden.append(quest)
    return gefunden

treffer = suche_quests(quests, "jagd")
print(f"Gefunden: {len(treffer)}")
