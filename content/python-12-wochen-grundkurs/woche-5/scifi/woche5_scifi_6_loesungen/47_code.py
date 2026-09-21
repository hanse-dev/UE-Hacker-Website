def berechne_gewinn(auftraege, fehlschlaege):
    return auftraege * 10 - fehlschlaege * 5

def erstelle_kennung(name, nummer):
    return f"{nummer}: {name}"
def zeige_missionsbericht(name, nummer, auftraege, fehlschlaege):
    print(erstelle_kennung(name, nummer))
    print(f"Gewinn: {berechne_gewinn(auftraege, fehlschlaege)}")
    print(f"Fehlschläge: {fehlschlaege}")

zeige_missionsbericht("Nova", 7, 8, 2)
