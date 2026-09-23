def berechne_belohnung(schwierigkeit):
    return schwierigkeit * 50

def darf_quest(level, schwierigkeit):
    return level >= schwierigkeit * 2
def zeige_quest(name, schwierigkeit, level):
    if darf_quest(level, schwierigkeit):
        print(f"{name}: Belohnung {berechne_belohnung(schwierigkeit)}")
    else:
        print(f"{name}: zu schwer")

zeige_quest("Drachenjagd", 4, 9)
zeige_quest("Schatzsuche", 2, 3)
