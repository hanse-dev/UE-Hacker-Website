quests = [["Drachenjagd", "Berg", 4], ["Schatzjagd", "Höhle", 2], ["Rätselwald", "Wald", 3]]
def quest_statistik(liste):
    anzahl = 0
    schwer = 0
    for quest in liste:
        anzahl += 1
        if quest[2] < 3:
            continue
        schwer += 1
    print(f"Quests: {anzahl}")
    print(f"Schwere Quests: {schwer}")

quest_statistik(quests)
