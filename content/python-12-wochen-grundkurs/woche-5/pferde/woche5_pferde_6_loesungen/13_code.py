import random

# Schritt 1 – Trainingsplan erstellen
def erstelle_trainingsplan(pferd_name, rasse, level):
    """Erstellt einen Trainingsplan für ein Pferd.
    
    Parameter:
        pferd_name (str): Name des Pferdes
        rasse (str): Rasse des Pferdes
        level (int): Trainingslevel
    
    Ergebnis:
        dict: Dictionary mit name, rasse und level
    """
    return {"name": pferd_name, "rasse": rasse, "level": level}

# Schritt 2 – Energiebedarf berechnen
def berechne_energie(intensitaet, dauer):
    return intensitaet * dauer

# Schritt 3 – Trainingseinheit erstellen
def generiere_trainingseinheit(name, energie):
    return f"{name} absolviert eine Einheit mit {energie} Energiepunkten Verbrauch."

# Schritt 4 – Fortschritt anzeigen
def zeige_fortschritt(pferd, absolvierte_einheiten):
    print("=" * 35)
    print("      TRAININGS-FORTSCHRITT")
    print("=" * 35)
    print(f"Pferd:    {pferd['name']}")
    print(f"Rasse:    {pferd['rasse']}")
    print(f"Level:    {pferd['level']}")
    print(f"Einheiten absolviert: {absolvierte_einheiten}")
    print("=" * 35)

# Alles zusammen
plan = erstelle_trainingsplan("Sturm", "Andalusier", 5)
energie = berechne_energie(8, 4)
einheit = generiere_trainingseinheit(plan["name"], energie)
print(einheit)
zeige_fortschritt(plan, 12)

# Bonus – Wetter und Boden
def zufalls_bedingung():
    wetter = random.choice(["Sonne", "Regen", "Wind"])
    boden = random.choice(["trocken", "matschig", "sandig"])
    energie_bonus = {"Regen": 5, "Wind": 3, "Sonne": 0}
    extra = energie_bonus.get(wetter, 0)
    return wetter, boden, extra

wetter, boden, extra = zufalls_bedingung()
print(f"Wetter: {wetter}, Boden: {boden} → +{extra} Energiebedarf")