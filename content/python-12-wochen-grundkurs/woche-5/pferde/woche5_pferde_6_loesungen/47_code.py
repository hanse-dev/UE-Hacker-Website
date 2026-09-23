def berechne_punkte(spruenge, fehler):
    return spruenge * 10 - fehler * 5

def erstelle_startnummer(name, nummer):
    return f"{nummer}: {name}"
def zeige_starterkarte(name, nummer, spruenge, fehler):
    print(erstelle_startnummer(name, nummer))
    print(f"Punkte: {berechne_punkte(spruenge, fehler)}")
    print(f"Fehler: {fehler}")

zeige_starterkarte("Sturmwind", 7, 8, 2)
