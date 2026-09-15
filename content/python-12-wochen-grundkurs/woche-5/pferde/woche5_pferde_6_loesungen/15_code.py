import random

# Schritt 1 – Turnierplan erstellen
def erstelle_teilnehmer(name, disziplin, start_punkte):
    return {"name": name, "disziplin": disziplin, "punkte": start_punkte}

# Schritt 2 – Punkte berechnen
def berechne_punkte(noten, schwierigkeit):
    durchschnitt = sum(noten) / len(noten)
    return round(durchschnitt * schwierigkeit, 1)

# Schritt 3 – Voraussetzungen prüfen
def kann_teilnehmen(reiter_level, mindest_level, hat_ausruestung):
    return reiter_level >= mindest_level and hat_ausruestung

# Schritt 4 – Turnier-Ergebnis zusammenfassen
def zeige_turnier_ergebnis(teilnehmer_liste):
    print("=== TURNIER-ERGEBNISSE ===")
    sortiert = sorted(teilnehmer_liste, key=lambda t: t["punkte"], reverse=True)
    for i, t in enumerate(sortiert, 1):
        print(f"  {i}. {t['name']} ({t['disziplin']}): {t['punkte']} Punkte")
    print(f"\nSieger: {sortiert[0]['name']} mit {sortiert[0]['punkte']} Punkten!")

# Turnier simulieren
teilnehmer = [
    erstelle_teilnehmer("Lena", "Dressur", 0),
    erstelle_teilnehmer("Max", "Springen", 0),
    erstelle_teilnehmer("Sophie", "Dressur", 0),
]

for t in teilnehmer:
    noten = [random.randint(6, 10) for _ in range(3)]
    schwierigkeit = random.uniform(1.0, 1.5)
    t["punkte"] = berechne_punkte(noten, schwierigkeit)

zeige_turnier_ergebnis(teilnehmer)

# Bonus – Ranking ausgeben
print("\n--- Ranking ---")
for i, t in enumerate(sorted(teilnehmer, key=lambda x: x["punkte"], reverse=True), 1):
    print(f"  Platz {i}: {t['name']} – {t['punkte']} Pkt")