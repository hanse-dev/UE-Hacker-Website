# Schritt 1 – Trainingsnamen erzeugen
def generiere_training_name(pferde_typ, schwierigkeit):
    return f"{pferde_typ.upper()}-L{schwierigkeit}"

# Schritt 2 – Intensität berechnen
def berechne_intensitaet(dauer, pferde_typ):
    faktoren = {"Sportpferd": 1.4, "Freizeitpferd": 0.8, "Rennpferd": 1.8}
    faktor = faktoren.get(pferde_typ, 1.0)
    return min(100, int(dauer * faktor * 5))

# Schritt 3 – Trainings-Daten erstellen
def erstelle_training(pferde_typ, schwierigkeit, dauer):
    name = generiere_training_name(pferde_typ, schwierigkeit)
    intensitaet = berechne_intensitaet(dauer, pferde_typ)
    return {"name": name, "typ": pferde_typ, "schwierigkeit": schwierigkeit, "intensitaet": intensitaet}

# Schritt 4 – Trainingsplan verwalten
trainings_plan = []

def speichere_training(plan, training):
    plan.append(training)

# Schritt 5 – Generator nutzen
speichere_training(trainings_plan, erstelle_training("Sportpferd", 3, 6))
speichere_training(trainings_plan, erstelle_training("Freizeitpferd", 1, 4))
speichere_training(trainings_plan, erstelle_training("Rennpferd", 5, 8))
speichere_training(trainings_plan, erstelle_training("Sportpferd", 2, 5))
speichere_training(trainings_plan, erstelle_training("Freizeitpferd", 2, 3))

print("=== TRAININGSPLAN ===")
for t in trainings_plan:
    print(f"{t['name']} – Typ: {t['typ']}, Stufe: {t['schwierigkeit']}, Intensität: {t['intensitaet']}")

gesamt = sum(t["intensitaet"] for t in trainings_plan)
print(f"\nAnzahl Trainings: {len(trainings_plan)}")
print(f"Durchschnittliche Intensität: {gesamt // len(trainings_plan)}")

# Bonus – sortiert nach Intensität
print("\n--- Sortiert nach Intensität ---")
for t in sorted(trainings_plan, key=lambda x: x["intensitaet"], reverse=True):
    print(f"  {t['name']}: {t['intensitaet']}")